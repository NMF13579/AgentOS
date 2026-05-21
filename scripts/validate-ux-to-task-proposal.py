#!/usr/bin/env python3
"""
M49 UX-to-Task Proposal Validator
Read-only validator for non-executable proposal artifacts.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

RESULT_OK = "UX_TO_TASK_PROPOSAL_VALIDATION_OK"
RESULT_FAILED = "UX_TO_TASK_PROPOSAL_VALIDATION_FAILED"
RESULT_BLOCKED = "UX_TO_TASK_PROPOSAL_VALIDATION_BLOCKED"

ALLOWED_PROPOSAL_STATUS = {
    "PROPOSED_ONLY",
    "PROPOSAL_READY_FOR_REVIEW",
    "PROPOSAL_BLOCKED",
    "PROPOSAL_INVALID",
}

ALLOWED_READINESS_DECISION = {
    "UX_PLANNING_READY",
    "UX_PLANNING_READY_WITH_LIMITATIONS",
}

MAX_FILE_SIZE = 1024 * 1024

REQUIRED_SECTIONS = [
    "## Purpose",
    "## Source Traceability",
    "## Proposed Task Contract Summary",
    "## Proposed Goal",
    "## Proposed Scope",
    "## Proposed Allowed Changes",
    "## Proposed Forbidden Changes",
    "## Proposed Validation",
    "## Proposed Risk Notes",
    "## Carry-Forward Requirements",
    "## Human Authorization Requirement",
    "## Non-Executable Boundary",
    "## Summary",
]

POSITIVE_AUTHORITY_CLAIMS = [
    r"task contract proposal authorizes implementation",
    r"task contract proposal authorizes execution",
    r"proposal authorizes implementation",
    r"proposal authorizes execution",
    r"PROPOSED_ONLY authorizes execution",
    r"PROPOSAL_READY_FOR_REVIEW authorizes execution",
    r"validator PASS authorizes implementation",
    r"validator PASS authorizes execution",
    r"readiness authorizes task generation",
    r"readiness authorizes implementation",
    r"readiness authorizes execution",
    r"may be copied into tasks/active-task\.md",
    r"may be copied into tasks/queue/",
]

RULES = [
    "Frontmatter must exist and contain required keys.",
    "type must be task-contract-proposal.",
    "proposal_status must be one of allowed values.",
    "execution_authorized must be false.",
    "implementation_authorized must be false.",
    "human_authorization_required must be true.",
    "source_section is forbidden singular key.",
    "source_sections is required.",
    "ux_contract_validation_result must be UX_CONTRACT_VALIDATION_OK.",
    "readiness_validation_result must be UX_PLANNING_READINESS_VALIDATION_OK.",
    "readiness_decision must be UX_PLANNING_READY or UX_PLANNING_READY_WITH_LIMITATIONS.",
    "blocking_gaps must be absent or empty.",
    "carry-forward fields must exist.",
    "active_task_allowed must be false.",
    "task_queue_allowed must be false.",
    "positive authority claims must be absent.",
]


class ValidationResult:
    def __init__(self, mode: str, checked_file: str = "") -> None:
        self.mode = mode
        self.checked_file = checked_file
        self.errors: List[str] = []
        self.warnings: List[str] = []

    def token(self) -> str:
        if self.errors:
            return RESULT_FAILED
        return RESULT_OK

    def to_json(self) -> Dict[str, object]:
        payload: Dict[str, object] = {
            "mode": self.mode,
            "result": self.token(),
            "errors": self.errors,
            "warnings": self.warnings,
        }
        if self.checked_file:
            payload["checked_file"] = self.checked_file
        return payload


def _stderr(msg: str) -> None:
    print(msg, file=sys.stderr)


def read_text_file(path: Path) -> Tuple[str, str]:
    if not path.exists():
        raise FileNotFoundError(f"MISSING_FILE: {path}")
    if not path.is_file():
        raise OSError(f"NOT_A_FILE: {path}")
    try:
        size = path.stat().st_size
    except OSError as exc:
        raise OSError(f"UNREADABLE_FILE: {path}: {exc}")
    if size > MAX_FILE_SIZE:
        raise ValueError(f"FILE_TOO_LARGE_GT_1MB: {path}")
    try:
        raw = path.read_bytes()
    except OSError as exc:
        raise OSError(f"UNREADABLE_FILE: {path}: {exc}")
    text = raw.decode("utf-8-sig")
    return text, str(path)


def parse_frontmatter(text: str) -> Tuple[Dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    block = text[4:end]
    body = text[end + 5 :]
    data: Dict[str, str] = {}
    for line in block.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data, body


def contains_forbidden_source_section(text: str) -> bool:
    return re.search(r"(?mi)^\s*source_section\s*:\s*", text) is not None


def has_required_sections(body: str, errors: List[str]) -> None:
    for sec in REQUIRED_SECTIONS:
        if sec not in body:
            errors.append(f"MISSING_REQUIRED_SECTION: {sec}")


def extract_scalar(text: str, key: str) -> str:
    m = re.search(rf"(?mi)^\s*{re.escape(key)}\s*:\s*(.+?)\s*$", text)
    if not m:
        return ""
    return m.group(1).strip()


def check_positive_authority_claims(text: str, errors: List[str]) -> None:
    for patt in POSITIVE_AUTHORITY_CLAIMS:
        if re.search(patt, text, flags=re.IGNORECASE):
            errors.append(f"FORBIDDEN_AUTHORITY_CLAIM: {patt}")


def check_required_presence(text: str, key: str, errors: List[str], label: str = "") -> None:
    if not re.search(rf"(?mi)^\s*{re.escape(key)}\s*:", text):
        errors.append(f"MISSING_{label or key.upper()}")


def check_literal_bool(text: str, key: str, expected: str, errors: List[str], code: str) -> None:
    value = extract_scalar(text, key)
    if not value:
        errors.append(f"MISSING_{code}")
        return
    if value != expected:
        errors.append(f"INVALID_{code}: expected {expected}, got {value}")


def check_readiness_constraints(text: str, errors: List[str]) -> None:
    ucv = extract_scalar(text, "ux_contract_validation_result")
    if not ucv:
        errors.append("MISSING_UX_CONTRACT_VALIDATION_RESULT")
    elif ucv != "UX_CONTRACT_VALIDATION_OK":
        errors.append("INVALID_UX_CONTRACT_VALIDATION_RESULT")

    rv = extract_scalar(text, "readiness_validation_result")
    if not rv:
        errors.append("MISSING_READINESS_VALIDATION_RESULT")
    elif rv != "UX_PLANNING_READINESS_VALIDATION_OK":
        errors.append("INVALID_READINESS_VALIDATION_RESULT")

    rd = extract_scalar(text, "readiness_decision")
    if not rd:
        errors.append("MISSING_READINESS_DECISION")
    elif rd not in ALLOWED_READINESS_DECISION:
        errors.append("INVALID_OR_BLOCKING_READINESS_DECISION")


def check_blocking_gaps(text: str, errors: List[str]) -> None:
    m = re.search(r"(?mis)^\s*blocking_gaps\s*:\s*(.+?)$", text)
    if not m:
        return
    val = m.group(1).strip()
    if val not in ("[]", ""):
        errors.append("BLOCKING_GAPS_PRESENT")


def validate_proposal(path: Path) -> Tuple[str, Dict[str, object], int]:
    result = ValidationResult(mode="proposal", checked_file=str(path))
    try:
        text, checked = read_text_file(path)
        result.checked_file = checked
    except FileNotFoundError as exc:
        result.errors.append(str(exc))
        payload = result.to_json()
        payload["result"] = RESULT_BLOCKED
        return RESULT_BLOCKED, payload, 2
    except ValueError as exc:
        result.errors.append(str(exc))
        payload = result.to_json()
        payload["result"] = RESULT_BLOCKED
        return RESULT_BLOCKED, payload, 2
    except Exception as exc:
        result.errors.append(str(exc))
        payload = result.to_json()
        payload["result"] = RESULT_BLOCKED
        return RESULT_BLOCKED, payload, 2

    frontmatter, body = parse_frontmatter(text)
    if not frontmatter:
        result.errors.append("MISSING_FRONTMATTER")

    if contains_forbidden_source_section(text):
        result.errors.append("FORBIDDEN_SINGULAR_SOURCE_SECTION")

    if frontmatter.get("type", "") != "task-contract-proposal":
        result.errors.append("INVALID_TYPE")

    # Frontmatter-level required keys
    for key in [
        "proposal_id",
        "proposal_status",
        "source_draft_id",
        "source_task_draft_path",
        "source_ux_contract",
        "source_readiness_report",
        "source_boundary_policy",
    ]:
        if key not in frontmatter or not frontmatter.get(key, "").strip():
            result.errors.append(f"MISSING_FRONTMATTER_{key.upper()}")

    proposal_status = frontmatter.get("proposal_status", "")
    if proposal_status and proposal_status not in ALLOWED_PROPOSAL_STATUS:
        result.errors.append("INVALID_PROPOSAL_STATUS")

    # boundary booleans in frontmatter
    if frontmatter.get("execution_authorized", "") != "false":
        result.errors.append("INVALID_EXECUTION_AUTHORIZED_FRONTMATTER")
    if frontmatter.get("implementation_authorized", "") != "false":
        result.errors.append("INVALID_IMPLEMENTATION_AUTHORIZED_FRONTMATTER")
    if frontmatter.get("human_authorization_required", "") != "true":
        result.errors.append("INVALID_HUMAN_AUTH_REQUIRED_FRONTMATTER")

    # Required sections
    has_required_sections(body, result.errors)

    # Required body model root and keys
    check_required_presence(text, "task_contract_proposal", result.errors, "TASK_CONTRACT_PROPOSAL_MODEL")
    check_required_presence(text, "source_sections", result.errors, "SOURCE_SECTIONS")
    check_required_presence(text, "accepted_limitations", result.errors, "ACCEPTED_LIMITATIONS")
    check_required_presence(text, "open_questions", result.errors, "OPEN_QUESTIONS")
    check_required_presence(text, "downstream_limits", result.errors, "DOWNSTREAM_LIMITS")
    check_required_presence(text, "non_authority_boundary", result.errors, "NON_AUTHORITY_BOUNDARY")

    check_readiness_constraints(text, result.errors)
    check_blocking_gaps(text, result.errors)

    # body boundaries
    check_literal_bool(text, "active_task_allowed", "false", result.errors, "ACTIVE_TASK_ALLOWED")
    check_literal_bool(text, "task_queue_allowed", "false", result.errors, "TASK_QUEUE_ALLOWED")

    # Also enforce body-level bools
    check_literal_bool(text, "execution_authorized", "false", result.errors, "EXECUTION_AUTHORIZED")
    check_literal_bool(text, "implementation_authorized", "false", result.errors, "IMPLEMENTATION_AUTHORIZED")
    check_literal_bool(text, "human_authorization_required", "true", result.errors, "HUMAN_AUTHORIZATION_REQUIRED")

    check_positive_authority_claims(text, result.errors)

    token = result.token()
    exit_code = 0 if token == RESULT_OK else 1
    payload = result.to_json()
    return token, payload, exit_code


def list_markdown_files(path: Path) -> List[Path]:
    return sorted([p for p in path.rglob("*.md") if p.is_file()])


def validate_fixtures() -> Tuple[str, Dict[str, object], int]:
    positive_dir = Path("tests/fixtures/ux-to-task-proposal/valid")
    negative_dir = Path("tests/fixtures/ux-to-task-proposal/negative")
    errors: List[str] = []
    warnings: List[str] = []

    if not positive_dir.exists() or not negative_dir.exists():
        payload = {
            "mode": "fixtures",
            "result": RESULT_BLOCKED,
            "fixture_summary": {
                "positive_passed": 0,
                "positive_failed": 0,
                "negative_failed_as_expected": 0,
                "negative_unexpectedly_passed": 0,
            },
            "errors": ["MISSING_FIXTURE_DIRECTORIES"],
            "warnings": warnings,
        }
        return RESULT_BLOCKED, payload, 2

    positives = list_markdown_files(positive_dir)
    negatives = list_markdown_files(negative_dir)

    summary = {
        "positive_passed": 0,
        "positive_failed": 0,
        "negative_failed_as_expected": 0,
        "negative_unexpectedly_passed": 0,
    }

    for file_path in positives:
        token, payload, _ = validate_proposal(file_path)
        if token == RESULT_OK:
            summary["positive_passed"] += 1
        elif token == RESULT_BLOCKED:
            errors.append(f"POSITIVE_BLOCKED: {file_path}")
            summary["positive_failed"] += 1
        else:
            summary["positive_failed"] += 1
            errors.append(f"POSITIVE_FAILED: {file_path}: {payload.get('errors', [])}")

    for file_path in negatives:
        token, payload, _ = validate_proposal(file_path)
        if token == RESULT_OK:
            summary["negative_unexpectedly_passed"] += 1
            errors.append(f"NEGATIVE_UNEXPECTED_PASS: {file_path}")
        elif token == RESULT_BLOCKED:
            errors.append(f"NEGATIVE_BLOCKED: {file_path}")
        else:
            summary["negative_failed_as_expected"] += 1

    if errors:
        token = RESULT_FAILED
        exit_code = 1
    else:
        token = RESULT_OK
        exit_code = 0

    payload = {
        "mode": "fixtures",
        "result": token,
        "fixture_summary": summary,
        "errors": errors,
        "warnings": warnings,
    }
    return token, payload, exit_code


def explain_payload() -> Dict[str, object]:
    return {
        "mode": "explain",
        "result": RESULT_OK,
        "rules": RULES,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate M49 UX-to-task proposal artifacts (read-only)."
    )
    parser.add_argument("--proposal", help="Path to proposal markdown file")
    parser.add_argument("--fixtures", action="store_true", help="Run fixture suite")
    parser.add_argument("--explain", action="store_true", help="Print rules only")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    return parser.parse_args()


def print_non_json_proposal(token: str, payload: Dict[str, object]) -> None:
    print(token)
    if payload.get("checked_file"):
        print(f"checked_file: {payload['checked_file']}")
    errs = payload.get("errors", [])
    warns = payload.get("warnings", [])
    if errs:
        print("errors:")
        for item in errs:
            print(f"- {item}")
    if warns:
        print("warnings:")
        for item in warns:
            print(f"- {item}")


def print_non_json_fixtures(token: str, payload: Dict[str, object]) -> None:
    print(token)
    summary = payload.get("fixture_summary", {})
    print("fixture_summary:")
    print(f"  positive_passed: {summary.get('positive_passed', 0)}")
    print(f"  positive_failed: {summary.get('positive_failed', 0)}")
    print(f"  negative_failed_as_expected: {summary.get('negative_failed_as_expected', 0)}")
    print(f"  negative_unexpectedly_passed: {summary.get('negative_unexpectedly_passed', 0)}")
    errs = payload.get("errors", [])
    warns = payload.get("warnings", [])
    if errs:
        print("errors:")
        for item in errs:
            print(f"- {item}")
    if warns:
        print("warnings:")
        for item in warns:
            print(f"- {item}")


def main() -> int:
    args = parse_args()

    selected = int(bool(args.proposal)) + int(bool(args.fixtures)) + int(bool(args.explain))
    if selected != 1:
        payload = {
            "mode": "invalid",
            "result": RESULT_BLOCKED,
            "errors": ["INVALID_MODE_COMBINATION"],
            "warnings": [],
        }
        if args.json:
            print(json.dumps(payload, ensure_ascii=False))
        else:
            _stderr("INVALID_MODE_COMBINATION")
            print(RESULT_BLOCKED)
        return 2

    if args.explain:
        payload = explain_payload()
        if args.json:
            print(json.dumps(payload, ensure_ascii=False))
        else:
            print(RESULT_OK)
            print("rules:")
            for idx, rule in enumerate(RULES, start=1):
                print(f"{idx}. {rule}")
        return 0

    if args.fixtures:
        token, payload, code = validate_fixtures()
        if args.json:
            print(json.dumps(payload, ensure_ascii=False))
        else:
            print_non_json_fixtures(token, payload)
        return code

    token, payload, code = validate_proposal(Path(args.proposal))

    if token == RESULT_BLOCKED:
        payload["result"] = RESULT_BLOCKED
        code = 2

    if args.json:
        # --json mode must write only valid JSON to stdout; all non-JSON diagnostics must go to stderr.
        print(json.dumps(payload, ensure_ascii=False))
    else:
        print_non_json_proposal(payload.get("result", token), payload)

    return code


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        _stderr(f"UNHANDLED_EXCEPTION: {exc}")
        payload = {
            "mode": "proposal",
            "result": RESULT_BLOCKED,
            "errors": [f"UNHANDLED_EXCEPTION: {exc}"],
            "warnings": [],
        }
        if "--json" in sys.argv:
            print(json.dumps(payload, ensure_ascii=False))
        raise SystemExit(2)
