#!/usr/bin/env python3
import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

OK = "PROPOSAL_TO_TASK_CONVERSION_VALIDATION_OK"
FAILED = "PROPOSAL_TO_TASK_CONVERSION_VALIDATION_FAILED"
BLOCKED = "PROPOSAL_TO_TASK_CONVERSION_VALIDATION_BLOCKED"

NON_AUTHORITY_MARKERS = [
    "VALIDATOR_CREATES_NO_APPROVAL_RECORD",
    "VALIDATOR_DOES_NOT_AUTHORIZE_EXECUTION",
    "VALIDATOR_DOES_NOT_PLACE_TASK_IN_QUEUE",
    "VALIDATOR_DOES_NOT_MODIFY_ACTIVE_TASK",
    "VALIDATOR_DOES_NOT_START_IMPLEMENTATION",
]

ALLOWED_INPUT_STATUSES = {
    "CONVERSION_INPUT_READY",
    "CONVERSION_INPUT_READY_WITH_LIMITATIONS",
    "CONVERSION_INPUT_NEEDS_HUMAN_AUTHORIZATION",
    "CONVERSION_INPUT_BLOCKED",
    "CONVERSION_INPUT_INVALID",
}

ALLOWED_PROPOSAL_VALIDATION = {
    "TASK_CONTRACT_PROPOSAL_VALIDATED",
    "TASK_CONTRACT_PROPOSAL_VALIDATED_WITH_LIMITATIONS",
}

REJECTED_PROPOSAL_VALIDATION = {
    "TASK_CONTRACT_PROPOSAL_DRAFT",
    "TASK_CONTRACT_PROPOSAL_NEEDS_CLARIFICATION",
    "TASK_CONTRACT_PROPOSAL_BLOCKED",
    "TASK_CONTRACT_PROPOSAL_INVALID",
    "TASK_CONTRACT_PROPOSAL_REJECTED",
    "UNKNOWN",
    "FAILED",
    "MISSING",
}

REQUIRED_FIELD_LABELS = [
    "conversion_package:",
    "conversion_id:",
    "conversion_input_status:",
    "source_task_contract_proposal:",
    "proposal_validation_result:",
    "source_ux_contract:",
    "source_readiness_report:",
    "source_boundary_policy:",
    "source_sections:",
    "accepted_limitations:",
    "open_questions:",
    "downstream_limits:",
    "non_authority_boundary:",
    "human_authorization_record:",
    "conversion_scope:",
    "candidate_output:",
    "task_contract_candidate:",
    "source_proposal:",
    "source_authorization:",
    "goal:",
    "scope:",
    "allowed_changes:",
    "forbidden_changes:",
    "validation:",
    "expected_final_report:",
    "carry_forward:",
    "boundaries:",
]

FORBIDDEN_REGEX_PATTERNS = [
    r"(?m)^\s*mode:\s*EXECUTION\s*$",
    r'"mode"\s*:\s*"EXECUTION"',
    r"(?m)^\s*execution_authorized:\s*true\s*$",
    r"(?m)^\s*execution_permission_granted:\s*true\s*$",
    r"(?m)^\s*active_task_allowed:\s*true\s*$",
    r"(?m)^\s*task_queue_allowed:\s*true\s*$",
    r"(?m)^\s*execution_approval_granted:\s*true\s*$",
    r"(?m)^\s*queue_placement_approval_granted:\s*true\s*$",
    r"(?m)^\s*active_task_replacement_approval_granted:\s*true\s*$",
    r"(?m)^\s*implementation_approval_granted:\s*true\s*$",
    r"(?m)^\s*approval_record_creation_allowed:\s*true\s*$",
    r"validator created approval",
    r"validator-created approval",
    r"approval created by validator",
    r"validator generated authorization",
    r"validator generated approval record",
    r"validator pass treated as approval",
    r"human authorization treated as execution approval",
    r"forbidden changes weakened",
    r"allowed changes expanded",
]

# Required explicit forbidden literal markers for policy traceability:
# approval_record_creation_allowed: true
# validator-created approval

INVALID_AUTHORIZATION_SOURCES = [
    "agent",
    "self",
    "auto",
    "simulated",
    "generated",
    "synthetic",
    "validator",
    "script",
    "system-inferred",
]


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--conversion", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    parser.add_argument("--explain", action="store_true")
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def iso_to_dt(value):
    try:
        if value.endswith("Z"):
            value = value[:-1] + "+00:00"
        dt = datetime.fromisoformat(value)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except Exception:
        return None


def find_value(text, key):
    m = re.search(rf"^\s*{re.escape(key)}\s*:\s*(.+?)\s*$", text, flags=re.MULTILINE)
    if not m:
        return None
    return m.group(1).strip()


def has_nonempty_list(text, key):
    block = re.search(rf"^\s*{re.escape(key)}\s*:\s*(?:\n(?:(?:\s{{2,}}.*\n?)+))?", text, flags=re.MULTILINE)
    if not block:
        return False
    start = block.end()
    rest = text[start:]
    m = re.search(r"^\s*-\s*\S+", rest, flags=re.MULTILINE)
    if m:
        return True
    same_line = re.search(rf"^\s*{re.escape(key)}\s*:\s*\S+", text, flags=re.MULTILINE)
    return bool(same_line)


def check_required_labels(text, findings):
    ok = True
    for label in REQUIRED_FIELD_LABELS:
        if label not in text:
            findings.append(f"missing required field label: {label}")
            ok = False
    if "mode: EXECUTION_SHAPE" not in text:
        findings.append("missing required candidate mode: EXECUTION_SHAPE")
        ok = False
    return ok


def validate_single_text(text, path):
    findings = []
    warnings = []

    if "human_authorization_record:" not in text:
        findings.append("human authorization missing")
        return BLOCKED, findings, warnings
    if "human_authorization:" not in text:
        findings.append("human authorization missing")
        return BLOCKED, findings, warnings

    if not check_required_labels(text, findings):
        return FAILED, findings, warnings

    input_status = find_value(text, "conversion_input_status")
    if input_status not in ALLOWED_INPUT_STATUSES:
        findings.append("invalid conversion_input_status")
        return FAILED, findings, warnings
    if input_status == "CONVERSION_INPUT_NEEDS_HUMAN_AUTHORIZATION":
        findings.append("conversion input needs human authorization")
        return BLOCKED, findings, warnings
    if input_status == "CONVERSION_INPUT_BLOCKED":
        findings.append("conversion input is blocked")
        return BLOCKED, findings, warnings
    if input_status == "CONVERSION_INPUT_INVALID":
        findings.append("conversion input is invalid")
        return FAILED, findings, warnings

    proposal_validation = find_value(text, "proposal_validation_result")
    if proposal_validation is None:
        findings.append("proposal validation missing")
        return FAILED, findings, warnings
    if proposal_validation in REJECTED_PROPOSAL_VALIDATION:
        findings.append("proposal validation rejected")
        return FAILED, findings, warnings
    if proposal_validation not in ALLOWED_PROPOSAL_VALIDATION:
        findings.append("proposal validation unknown")
        return FAILED, findings, warnings

    auth_type = find_value(text, "authorization_type")
    if not auth_type:
        findings.append("human authorization missing")
        return BLOCKED, findings, warnings
    if auth_type != "proposal_to_task_contract_candidate_conversion":
        findings.append("authorization_type invalid")
        return FAILED, findings, warnings

    auth_status = find_value(text, "authorization_status")
    if not auth_status:
        findings.append("authorization_status missing")
        return BLOCKED, findings, warnings
    if auth_status != "AUTHORIZATION_VALID":
        findings.append("authorization_status invalid")
        return FAILED, findings, warnings

    expires = find_value(text, "expires_at")
    if not expires:
        findings.append("expires_at missing")
        return BLOCKED, findings, warnings
    exp_dt = iso_to_dt(expires)
    if exp_dt is None:
        findings.append("expires_at parse failed")
        return FAILED, findings, warnings
    if exp_dt <= datetime.now(timezone.utc):
        findings.append("authorization expired")
        return BLOCKED, findings, warnings

    authorized_scope = find_value(text, "authorized_scope")
    if not authorized_scope:
        findings.append("authorized_scope missing")
        return BLOCKED, findings, warnings
    not_authorized = find_value(text, "not_authorized")
    if not not_authorized and "not_authorized:" not in text:
        findings.append("not_authorized missing")
        return BLOCKED, findings, warnings

    src1 = find_value(text, "source_task_contract_proposal")
    src2 = find_value(text, "source_proposal")
    if not src1 or not src2:
        findings.append("source proposal missing")
        return FAILED, findings, warnings
    if src1 != src2:
        findings.append("authorization scope mismatch / source proposal mismatch")
        return FAILED, findings, warnings

    for key in ["authorized_by", "decision_source", "authorization_source"]:
        value = find_value(text, key)
        if value:
            low = value.lower()
            for bad in INVALID_AUTHORIZATION_SOURCES:
                if bad in low:
                    findings.append(f"invalid authorization source in {key}")
                    return FAILED, findings, warnings

    for key in [
        "accepted_limitations",
        "open_questions",
        "downstream_limits",
        "non_authority_boundary",
        "source_sections",
        "allowed_changes",
        "forbidden_changes",
        "validation",
        "expected_final_report",
    ]:
        if not has_nonempty_list(text, key):
            findings.append(f"missing or empty list field: {key}")
            return FAILED, findings, warnings

    boundary_expectations = {
        "conversion_validated": "true",
        "executable_contract_shape": "true",
        "candidate_ready_for_placement_review": "true",
        "placement_review_required": "true",
        "execution_authorized": "false",
        "execution_permission_granted": "false",
        "active_task_allowed": "false",
        "task_queue_allowed": "false",
    }
    for key, val in boundary_expectations.items():
        pattern = f"{key}: {val}"
        if pattern not in text:
            findings.append(f"boundary flag mismatch: {pattern}")
            return FAILED, findings, warnings

    for pattern in FORBIDDEN_REGEX_PATTERNS:
        if re.search(pattern, text, flags=re.IGNORECASE):
            findings.append(f"forbidden pattern found: {pattern}")
            return FAILED, findings, warnings

    return OK, findings, warnings


def read_text(path):
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return None


def extract_expected_result(text):
    m = re.search(r"^\s*expected_result\s*:\s*(\S+)\s*$", text, flags=re.MULTILINE)
    return m.group(1).strip() if m else None


def result_to_exit(result):
    if result == OK:
        return 0
    if result == FAILED:
        return 1
    return 2


def print_or_json(payload, as_json):
    if as_json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(payload["result"])
        for f in payload.get("findings", []):
            print(f"finding: {f}")
        for w in payload.get("warnings", []):
            print(f"warning: {w}")


def run_conversion(path, as_json):
    if not path or not path.exists() or not path.is_file():
        payload = {
            "result": BLOCKED,
            "exit_code": 2,
            "mode": "conversion",
            "checked_path": str(path) if path else "",
            "findings": ["conversion file missing or unreadable"],
            "warnings": [],
            "non_authority_markers": NON_AUTHORITY_MARKERS,
        }
        print_or_json(payload, as_json)
        return 2

    text = read_text(path)
    if text is None:
        payload = {
            "result": BLOCKED,
            "exit_code": 2,
            "mode": "conversion",
            "checked_path": str(path),
            "findings": ["conversion file unreadable"],
            "warnings": [],
            "non_authority_markers": NON_AUTHORITY_MARKERS,
        }
        print_or_json(payload, as_json)
        return 2

    result, findings, warnings = validate_single_text(text, path)
    payload = {
        "result": result,
        "exit_code": result_to_exit(result),
        "mode": "conversion",
        "checked_path": str(path),
        "findings": findings,
        "warnings": warnings,
        "non_authority_markers": NON_AUTHORITY_MARKERS,
    }
    print_or_json(payload, as_json)
    return payload["exit_code"]


def run_fixtures(as_json):
    root = Path("tests/fixtures/proposal-to-task-conversion/")
    if not root.exists() or not root.is_dir():
        payload = {
            "result": BLOCKED,
            "exit_code": 2,
            "mode": "fixtures",
            "checked_path": "tests/fixtures/proposal-to-task-conversion/",
            "fixture_summary": {"total": 0, "passed": 0, "failed": 0},
            "fixtures": [],
            "findings": ["fixture root missing or unreadable"],
            "warnings": [],
            "non_authority_markers": NON_AUTHORITY_MARKERS,
        }
        print_or_json(payload, as_json)
        return 2

    fixtures = sorted(root.rglob("*.md"))
    if not fixtures:
        payload = {
            "result": BLOCKED,
            "exit_code": 2,
            "mode": "fixtures",
            "checked_path": "tests/fixtures/proposal-to-task-conversion/",
            "fixture_summary": {"total": 0, "passed": 0, "failed": 0},
            "fixtures": [],
            "findings": ["no fixtures found"],
            "warnings": [],
            "non_authority_markers": NON_AUTHORITY_MARKERS,
        }
        print_or_json(payload, as_json)
        return 2

    items = []
    mismatches = 0
    aggregate_findings = []

    for path in fixtures:
        text = read_text(path)
        if text is None:
            expected = None
            actual = BLOCKED
            findings = ["fixture unreadable"]
        else:
            expected = extract_expected_result(text)
            actual, findings, _warnings = validate_single_text(text, path)
        passed = expected == actual
        if not passed:
            mismatches += 1
        item = {
            "path": str(path),
            "expected_result": expected,
            "actual_result": actual,
            "passed": passed,
            "findings": findings,
        }
        items.append(item)
        if not passed:
            aggregate_findings.append(f"fixture mismatch: {path}")

    if mismatches == 0:
        result = OK
        exit_code = 0
    else:
        result = FAILED
        exit_code = 1

    payload = {
        "result": result,
        "exit_code": exit_code,
        "mode": "fixtures",
        "checked_path": "tests/fixtures/proposal-to-task-conversion/",
        "fixture_summary": {
            "total": len(items),
            "passed": len(items) - mismatches,
            "failed": mismatches,
        },
        "fixtures": items,
        "findings": aggregate_findings,
        "warnings": [],
        "non_authority_markers": NON_AUTHORITY_MARKERS,
    }

    if as_json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(result)
        for item in items:
            status = "PASS" if item["passed"] else "FAIL"
            print(f"{status}: {item['path']} expected={item['expected_result']} actual={item['actual_result']}")

    return exit_code


def run_explain(as_json):
    payload = {
        "result": OK,
        "exit_code": 0,
        "mode": "explain",
        "checked_path": "",
        "findings": [
            "Conversion validator checks whether conversion is valid.",
            "Conversion validator does not authorize execution.",
            "Conversion validator does not place task into queue.",
            "Conversion validator does not create active task state.",
            "Conversion validator does not create approval records.",
            "Conversion validator PASS is not approval.",
        ],
        "warnings": [],
        "non_authority_markers": NON_AUTHORITY_MARKERS,
    }
    if as_json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        for marker in NON_AUTHORITY_MARKERS:
            print(marker)
        for line in payload["findings"]:
            print(line)
    return 0


def main():
    args = parse_args()

    modes = sum([bool(args.conversion), bool(args.fixtures), bool(args.explain)])
    if modes != 1:
        payload = {
            "result": BLOCKED,
            "exit_code": 2,
            "mode": "invalid",
            "checked_path": "",
            "findings": ["select exactly one mode: --conversion, --fixtures, or --explain"],
            "warnings": [],
            "non_authority_markers": NON_AUTHORITY_MARKERS,
        }
        print_or_json(payload, args.json)
        return 2

    if args.conversion:
        return run_conversion(args.conversion, args.json)
    if args.fixtures:
        return run_fixtures(args.json)
    return run_explain(args.json)


if __name__ == "__main__":
    sys.exit(main())
