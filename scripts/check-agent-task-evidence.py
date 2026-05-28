#!/usr/bin/env python3
import argparse
import json
from pathlib import Path
import re
import sys
from typing import Any, Dict, List, Optional, Sequence, Tuple

RESULT_PASS = "M64_EVIDENCE_CHECK_PASS"
RESULT_WARN = "M64_EVIDENCE_CHECK_PASS_WITH_WARNINGS"
RESULT_BLOCKED = "M64_EVIDENCE_CHECK_BLOCKED"
RESULT_NOE = "M64_EVIDENCE_CHECK_NOT_ENOUGH_EVIDENCE"

ALLOWED_RESULT_VALUES = {"PASS", "FAIL", "NOT_RUN", "UNKNOWN"}

REQUIRED_TOP_LEVEL_FIELDS = [
    "contract_version",
    "evidence_type",
    "task_id",
    "task_brief_path",
    "agent_identity",
    "files_changed",
    "created_artifacts",
    "modified_artifacts",
    "deleted_artifacts",
    "commands_run",
    "validation_results",
    "known_limitations",
    "warnings",
    "blockers",
    "forbidden_actions_performed",
    "human_review_required",
    "non_authority_boundary",
]

REQUIRED_NON_AUTHORITY_STATEMENTS = [
    "Agent evidence is not approval.",
    "Agent evidence does not complete the task.",
    "Agent evidence does not replace human review.",
    "Agent evidence does not authorize merge, push, or release.",
    "Human review remains required.",
]

FORBIDDEN_PHRASES = [
    "approved",
    "approval granted",
    "task approved",
    "task is approved",
    "task completion approved",
    "acceptance criteria approved",
    "task accepted by system",
    "auto-approved",
    "auto approval",
    "complete without review",
    "completed without review",
    "human review not required",
    "human_review_required: false",
    "review not required",
    "merged",
    "merge completed",
    "merge authorized",
    "push authorized",
    "pushed",
    "release authorized",
    "released",
    "deployment authorized",
    "deployed",
    "lifecycle mutated",
    "lifecycle state mutated",
    "completion gate passed",
    "production task acceptance gate passed",
    "production ready",
    "ready for production",
    "m65 started automatically",
    "m66 started automatically",
    "m67 started automatically",
]

HIGH_CONF_HIDDEN_BLOCKER_TERMS = [
    "blocked",
    "cannot proceed",
    "critical",
    "unsafe",
    "failed required",
    "required check failed",
]

AMBIG_HIDDEN_BLOCKER_TERMS = [
    "must fix",
    "blocker",
    "not safe",
]

SAFE_POLICY_MARKERS = [
    "must not",
    "does not",
    "is not",
    "not approval",
    "forbidden",
    "example",
]

EVIDENCE_BEARING_ARRAYS = [
    "files_changed",
    "created_artifacts",
    "modified_artifacts",
    "deleted_artifacts",
    "commands_run",
    "validation_results",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="M64 agent task evidence checker")
    parser.add_argument("--evidence", required=True, help="Path to agent task output evidence JSON")
    parser.add_argument("--task-id", help="Expected task id for cross-check")
    parser.add_argument("--strict", action="store_true", help="Increase visibility of ambiguous risks")
    parser.add_argument("--json", action="store_true", help="Emit JSON output")
    return parser.parse_args()


def is_real_bool(value: Any) -> bool:
    return type(value) is bool


def make_payload(strict: bool) -> Dict[str, Any]:
    return {
        "result": RESULT_BLOCKED,
        "evidence_checked": True,
        "evidence_json_valid": False,
        "required_fields_present": False,
        "required_field_types_valid": False,
        "contract_version_supported": False,
        "evidence_type_supported": False,
        "task_id_check_performed": False,
        "task_id_match": None,
        "agent_identity_valid": False,
        "commands_run_valid": False,
        "validation_results_valid": False,
        "human_review_required": False,
        "forbidden_actions_performed": False,
        "non_authority_boundary_present": False,
        "required_non_authority_statements_present": False,
        "forbidden_claims_found": False,
        "hidden_blocker_candidate_found": False,
        "not_enough_evidence": False,
        "m65_m67_scope_absorption_found": False,
        "strict": bool(strict),
        "warnings": [],
        "blockers": [],
    }


def add_warning(payload: Dict[str, Any], message: str) -> None:
    payload["warnings"].append(str(message))


def add_blocker(payload: Dict[str, Any], message: str) -> None:
    payload["blockers"].append(str(message))


def load_json(path: Path) -> Tuple[Optional[Dict[str, Any]], Optional[str], Optional[str]]:
    try:
        text = path.read_text(encoding="utf-8")
    except Exception as exc:
        return None, None, f"evidence file missing or unreadable: {exc}"

    try:
        obj = json.loads(text)
    except Exception as exc:
        return None, text, f"evidence JSON malformed: {exc}"

    if not isinstance(obj, dict):
        return None, text, "evidence JSON root must be object"

    return obj, text, None


def scan_strings(value: Any, path: Sequence[str] = ()) -> List[Tuple[Tuple[str, ...], str]]:
    out: List[Tuple[Tuple[str, ...], str]] = []
    if isinstance(value, str):
        out.append((tuple(path), value))
    elif isinstance(value, dict):
        for key, sub in value.items():
            out.extend(scan_strings(sub, tuple(path) + (str(key),)))
    elif isinstance(value, list):
        for idx, sub in enumerate(value):
            out.extend(scan_strings(sub, tuple(path) + (str(idx),)))
    return out


def is_safe_context(path: Tuple[str, ...], text: str) -> bool:
    if path and path[0] == "non_authority_boundary":
        lower = text.lower()
        if any(phrase in lower for phrase in [
            "task approved",
            "task completion approved",
            "merge authorized",
            "release authorized",
            "human review not required",
            "completion gate passed",
        ]):
            if not any(marker in lower for marker in SAFE_POLICY_MARKERS):
                return False
        return True

    lower = text.lower()
    return any(marker in lower for marker in SAFE_POLICY_MARKERS)


def ensure_array_of_non_empty_strings(payload: Dict[str, Any], evidence: Dict[str, Any], field: str) -> bool:
    value = evidence.get(field)
    if not isinstance(value, list):
        add_blocker(payload, f"{field} must be array")
        return False
    ok = True
    for idx, item in enumerate(value):
        if not isinstance(item, str) or len(item.strip()) == 0:
            add_blocker(payload, f"{field}[{idx}] must be non-empty string")
            ok = False
    return ok


def contains_required_marker(text: str) -> bool:
    low = text.lower()
    markers = ["required", "must run", "required validation", "must"]
    return any(marker in low for marker in markers)


def check_commands_run(payload: Dict[str, Any], evidence: Dict[str, Any]) -> bool:
    items = evidence.get("commands_run")
    if not isinstance(items, list):
        add_blocker(payload, "commands_run must be array")
        return False

    ok = True
    unknown_count = 0
    for idx, item in enumerate(items):
        if not isinstance(item, dict):
            add_blocker(payload, f"commands_run[{idx}] must be object")
            ok = False
            continue

        required = {"command", "purpose", "exit_code", "result", "notes"}
        keys = set(item.keys())
        missing = required - keys
        extra = keys - required
        if missing:
            add_blocker(payload, f"commands_run[{idx}] missing fields: {sorted(missing)}")
            ok = False
        if extra:
            add_blocker(payload, f"commands_run[{idx}] has unsupported fields: {sorted(extra)}")
            ok = False

        command = item.get("command")
        purpose = item.get("purpose")
        exit_code = item.get("exit_code")
        result = item.get("result")
        notes = item.get("notes")

        if not isinstance(command, str) or len(command.strip()) == 0:
            add_blocker(payload, f"commands_run[{idx}].command must be non-empty string")
            ok = False
        if not isinstance(purpose, str):
            add_blocker(payload, f"commands_run[{idx}].purpose must be string")
            ok = False
        if not isinstance(notes, str):
            add_blocker(payload, f"commands_run[{idx}].notes must be string")
            ok = False
        if not isinstance(exit_code, int):
            add_blocker(payload, f"commands_run[{idx}].exit_code must be integer")
            ok = False
        elif exit_code < -1:
            add_blocker(payload, f"commands_run[{idx}].exit_code must be >= -1")
            ok = False

        if not isinstance(result, str) or result not in ALLOWED_RESULT_VALUES:
            add_blocker(payload, f"commands_run[{idx}].result must be one of {sorted(ALLOWED_RESULT_VALUES)}")
            ok = False
            continue

        if result == "UNKNOWN":
            unknown_count += 1
            add_warning(payload, f"commands_run[{idx}] has UNKNOWN result")

        required_cmd = contains_required_marker(f"{purpose} {notes} {command}") if isinstance(purpose, str) and isinstance(notes, str) and isinstance(command, str) else False

        if result == "FAIL":
            if required_cmd:
                add_blocker(payload, f"commands_run[{idx}] FAIL for required command")
            else:
                add_warning(payload, f"commands_run[{idx}] FAIL for non-required command")

        if result == "NOT_RUN":
            if required_cmd:
                add_blocker(payload, f"commands_run[{idx}] NOT_RUN for required command")
            else:
                add_warning(payload, f"commands_run[{idx}] NOT_RUN for non-required command")

        if isinstance(exit_code, int) and exit_code == -1:
            if result == "PASS":
                add_warning(payload, f"commands_run[{idx}] contradictory: PASS with exit_code -1")
            elif result == "FAIL":
                if required_cmd:
                    add_blocker(payload, f"commands_run[{idx}] FAIL with unknown exit code for required command")
                else:
                    add_warning(payload, f"commands_run[{idx}] FAIL with unknown exit code")

    if isinstance(items, list) and len(items) > 0 and unknown_count == len(items):
        add_warning(payload, "commands_run contains UNKNOWN-only evidence")

    return ok


def check_validation_results(payload: Dict[str, Any], evidence: Dict[str, Any]) -> bool:
    items = evidence.get("validation_results")
    if not isinstance(items, list):
        add_blocker(payload, "validation_results must be array")
        return False

    ok = True
    unknown_count = 0
    for idx, item in enumerate(items):
        if not isinstance(item, dict):
            add_blocker(payload, f"validation_results[{idx}] must be object")
            ok = False
            continue

        required = {"check_name", "result", "notes"}
        keys = set(item.keys())
        missing = required - keys
        extra = keys - required
        if missing:
            add_blocker(payload, f"validation_results[{idx}] missing fields: {sorted(missing)}")
            ok = False
        if extra:
            add_blocker(payload, f"validation_results[{idx}] has unsupported fields: {sorted(extra)}")
            ok = False

        check_name = item.get("check_name")
        result = item.get("result")
        notes = item.get("notes")

        if not isinstance(check_name, str) or len(check_name.strip()) == 0:
            add_blocker(payload, f"validation_results[{idx}].check_name must be non-empty string")
            ok = False
        if not isinstance(notes, str):
            add_blocker(payload, f"validation_results[{idx}].notes must be string")
            ok = False
        if not isinstance(result, str) or result not in ALLOWED_RESULT_VALUES:
            add_blocker(payload, f"validation_results[{idx}].result must be one of {sorted(ALLOWED_RESULT_VALUES)}")
            ok = False
            continue

        if result == "UNKNOWN":
            unknown_count += 1
            add_warning(payload, f"validation_results[{idx}] has UNKNOWN result")

        required_check = contains_required_marker(f"{check_name} {notes}") if isinstance(check_name, str) and isinstance(notes, str) else False

        if result == "FAIL":
            if required_check:
                add_blocker(payload, f"validation_results[{idx}] FAIL for required validation")
            else:
                add_warning(payload, f"validation_results[{idx}] FAIL for non-required validation")

        if result == "NOT_RUN":
            if required_check:
                add_blocker(payload, f"validation_results[{idx}] NOT_RUN for required validation")
            else:
                add_warning(payload, f"validation_results[{idx}] NOT_RUN for non-required validation")

    if isinstance(items, list) and len(items) > 0 and unknown_count == len(items):
        add_warning(payload, "validation_results contains UNKNOWN-only evidence")

    return ok


def text_has_explanation(text: str) -> bool:
    low = text.lower()
    markers = ["because", "due to", "explained", "reason", "not in files_changed", "correlat", "объяс"]
    return any(marker in low for marker in markers)


def apply_cross_field_rules(payload: Dict[str, Any], evidence: Dict[str, Any]) -> None:
    commands_run = evidence.get("commands_run", []) if isinstance(evidence.get("commands_run"), list) else []
    validation_results = evidence.get("validation_results", []) if isinstance(evidence.get("validation_results"), list) else []

    if len(validation_results) > 0 and len(commands_run) == 0:
        add_warning(payload, "validation_results present while commands_run is empty")

    files_changed = evidence.get("files_changed", []) if isinstance(evidence.get("files_changed"), list) else []
    files_set = {x for x in files_changed if isinstance(x, str)}

    combined_texts: List[str] = []
    for k in ["known_limitations", "warnings", "blockers"]:
        v = evidence.get(k)
        if isinstance(v, list):
            combined_texts.extend([x for x in v if isinstance(x, str)])
    for item in commands_run:
        if isinstance(item, dict) and isinstance(item.get("notes"), str):
            combined_texts.append(item["notes"])
    for item in validation_results:
        if isinstance(item, dict) and isinstance(item.get("notes"), str):
            combined_texts.append(item["notes"])
    explanation_present = text_has_explanation("\n".join(combined_texts))

    for array_name in ["created_artifacts", "modified_artifacts", "deleted_artifacts"]:
        arr = evidence.get(array_name, [])
        if not isinstance(arr, list):
            continue
        missing = [x for x in arr if isinstance(x, str) and x not in files_set]
        if missing:
            if explanation_present:
                add_warning(payload, f"{array_name} not fully represented in files_changed, explanation found")
            else:
                add_warning(payload, f"{array_name} not fully represented in files_changed: {missing}")


def detect_hidden_blockers(payload: Dict[str, Any], evidence: Dict[str, Any], strict: bool) -> None:
    strings_to_scan: List[Tuple[str, str]] = []
    for field in ["known_limitations", "warnings", "blockers", "non_authority_boundary"]:
        values = evidence.get(field)
        if isinstance(values, list):
            for idx, item in enumerate(values):
                if isinstance(item, str):
                    strings_to_scan.append((f"{field}[{idx}]", item))

    for field in ["commands_run", "validation_results"]:
        values = evidence.get(field)
        if isinstance(values, list):
            for idx, item in enumerate(values):
                if isinstance(item, dict) and isinstance(item.get("notes"), str):
                    strings_to_scan.append((f"{field}[{idx}].notes", item["notes"]))

    high = False
    ambiguous = False
    for path, raw in strings_to_scan:
        low = raw.lower()
        if path.startswith("non_authority_boundary") and is_safe_context(("non_authority_boundary",), raw):
            continue

        if any(term in low for term in HIGH_CONF_HIDDEN_BLOCKER_TERMS):
            high = True
        elif any(term in low for term in AMBIG_HIDDEN_BLOCKER_TERMS):
            ambiguous = True

    if high:
        payload["hidden_blocker_candidate_found"] = True
        add_blocker(payload, "high-confidence hidden blocker signal detected")
    elif ambiguous:
        payload["hidden_blocker_candidate_found"] = True
        if strict:
            add_warning(payload, "ambiguous hidden blocker signal detected (strict mode)")
        else:
            add_warning(payload, "ambiguous hidden blocker signal detected")


def detect_forbidden_claims(payload: Dict[str, Any], evidence: Dict[str, Any], strict: bool) -> None:
    findings_block: List[str] = []
    findings_warn: List[str] = []

    for path, raw in scan_strings(evidence):
        low = raw.lower()

        if path and path[0] == "non_authority_boundary" and is_safe_context(path, raw):
            continue

        safe = is_safe_context(path, raw)
        for phrase in FORBIDDEN_PHRASES:
            if phrase in low:
                if safe:
                    continue

                if any(marker in low for marker in ["maybe", "could", "possible", "suspect", "might"]):
                    findings_warn.append(f"ambiguous forbidden claim at {'.'.join(path)}: {phrase}")
                else:
                    findings_block.append(f"forbidden claim at {'.'.join(path)}: {phrase}")

                if phrase in ["m65 started automatically", "m66 started automatically", "m67 started automatically"]:
                    payload["m65_m67_scope_absorption_found"] = True

    if findings_block:
        payload["forbidden_claims_found"] = True
        for msg in findings_block:
            add_blocker(payload, msg)

    if findings_warn:
        payload["forbidden_claims_found"] = True
        for msg in findings_warn:
            add_warning(payload, msg)

    if strict and findings_warn and not findings_block:
        add_warning(payload, "strict mode: ambiguous forbidden claims require explicit human attention")


def check_not_enough_evidence(payload: Dict[str, Any], evidence: Dict[str, Any]) -> bool:
    arrays = []
    for key in EVIDENCE_BEARING_ARRAYS:
        value = evidence.get(key)
        arrays.append(value if isinstance(value, list) else [])

    all_empty = all(len(v) == 0 for v in arrays)
    if all_empty:
        return True

    commands = evidence.get("commands_run", [])
    validations = evidence.get("validation_results", [])
    if isinstance(commands, list) and len(commands) > 0:
        only_unknown_commands = all(isinstance(i, dict) and i.get("result") == "UNKNOWN" for i in commands)
    else:
        only_unknown_commands = False

    if isinstance(validations, list) and len(validations) > 0:
        only_unknown_validations = all(isinstance(i, dict) and i.get("result") == "UNKNOWN" for i in validations)
    else:
        only_unknown_validations = False

    if only_unknown_commands and (len(validations) == 0 or only_unknown_validations):
        return True
    if only_unknown_validations and len(commands) == 0:
        return True

    return False


def main() -> int:
    try:
        args = parse_args()
        payload = make_payload(args.strict)

        evidence_path = Path(args.evidence)
        evidence, raw_text, load_error = load_json(evidence_path)
        if load_error is not None or evidence is None:
            add_blocker(payload, load_error or "evidence unavailable")
            payload["result"] = RESULT_BLOCKED
            if args.json:
                print(json.dumps(payload, ensure_ascii=False, indent=2))
            else:
                print(payload["result"])
            return 1

        payload["evidence_json_valid"] = True

        missing_fields = [k for k in REQUIRED_TOP_LEVEL_FIELDS if k not in evidence]
        if missing_fields:
            add_blocker(payload, f"required evidence fields missing: {missing_fields}")
            payload["required_fields_present"] = False
        else:
            payload["required_fields_present"] = True

        types_ok = True

        if not isinstance(evidence.get("contract_version"), str):
            types_ok = False
            add_blocker(payload, "contract_version must be string")
        if not isinstance(evidence.get("evidence_type"), str):
            types_ok = False
            add_blocker(payload, "evidence_type must be string")

        task_id = evidence.get("task_id")
        if not isinstance(task_id, str) or len(task_id.strip()) == 0:
            types_ok = False
            add_blocker(payload, "task_id must be non-empty string")

        task_brief_path = evidence.get("task_brief_path")
        if not isinstance(task_brief_path, str) or len(task_brief_path.strip()) == 0:
            types_ok = False
            add_blocker(payload, "task_brief_path must be non-empty string")

        if not isinstance(evidence.get("agent_identity"), dict):
            types_ok = False
            add_blocker(payload, "agent_identity must be object")

        for field in ["files_changed", "created_artifacts", "modified_artifacts", "deleted_artifacts"]:
            if not ensure_array_of_non_empty_strings(payload, evidence, field):
                types_ok = False

        for field in ["known_limitations", "warnings", "blockers"]:
            value = evidence.get(field)
            if not isinstance(value, list):
                types_ok = False
                add_blocker(payload, f"{field} must be array")
            else:
                for idx, item in enumerate(value):
                    if not isinstance(item, str):
                        types_ok = False
                        add_blocker(payload, f"{field}[{idx}] must be string")

        forbidden_actions = evidence.get("forbidden_actions_performed")
        if not is_real_bool(forbidden_actions) or forbidden_actions is not False:
            types_ok = False
            add_blocker(payload, "forbidden_actions_performed must be bool false")
        payload["forbidden_actions_performed"] = bool(forbidden_actions is True)

        human_review_required = evidence.get("human_review_required")
        if not is_real_bool(human_review_required) or human_review_required is not True:
            types_ok = False
            add_blocker(payload, "human_review_required must be bool true")
        payload["human_review_required"] = bool(human_review_required is True)

        non_auth = evidence.get("non_authority_boundary")
        if not isinstance(non_auth, list) or len(non_auth) == 0 or not all(isinstance(x, str) for x in non_auth):
            types_ok = False
            add_blocker(payload, "non_authority_boundary must be non-empty array of strings")
            payload["non_authority_boundary_present"] = False
        else:
            payload["non_authority_boundary_present"] = True

        payload["required_field_types_valid"] = types_ok

        payload["contract_version_supported"] = evidence.get("contract_version") == "m64.agent_task_output_evidence.v1"
        if not payload["contract_version_supported"]:
            add_blocker(payload, "unsupported contract_version")

        payload["evidence_type_supported"] = evidence.get("evidence_type") == "agent_task_output_evidence"
        if not payload["evidence_type_supported"]:
            add_blocker(payload, "unsupported evidence_type")

        if args.task_id is not None:
            payload["task_id_check_performed"] = True
            payload["task_id_match"] = isinstance(task_id, str) and task_id == args.task_id
            if not payload["task_id_match"]:
                add_blocker(payload, f"task_id mismatch: expected {args.task_id}, got {task_id}")
        else:
            payload["task_id_check_performed"] = False
            payload["task_id_match"] = None

        agent_identity_valid = True
        agent_identity = evidence.get("agent_identity")
        if not isinstance(agent_identity, dict):
            agent_identity_valid = False
        else:
            name = agent_identity.get("agent_name")
            role = agent_identity.get("agent_role")
            keys = set(agent_identity.keys())
            if keys != {"agent_name", "agent_role"}:
                agent_identity_valid = False
                add_blocker(payload, "agent_identity has missing or unsupported fields")
            if not isinstance(name, str) or len(name.strip()) == 0:
                agent_identity_valid = False
                add_blocker(payload, "agent_identity.agent_name must be non-empty string")
            if not isinstance(role, str) or len(role.strip()) == 0:
                agent_identity_valid = False
                add_blocker(payload, "agent_identity.agent_role must be non-empty string")
        payload["agent_identity_valid"] = agent_identity_valid

        payload["commands_run_valid"] = check_commands_run(payload, evidence)
        payload["validation_results_valid"] = check_validation_results(payload, evidence)

        if payload["non_authority_boundary_present"]:
            boundary_set = set(non_auth)
            required_present = all(s in boundary_set for s in REQUIRED_NON_AUTHORITY_STATEMENTS)
            payload["required_non_authority_statements_present"] = required_present
            if not required_present:
                add_blocker(payload, "required non-authority statement missing")
        else:
            payload["required_non_authority_statements_present"] = False

        apply_cross_field_rules(payload, evidence)
        detect_hidden_blockers(payload, evidence, args.strict)
        detect_forbidden_claims(payload, evidence, args.strict)

        not_enough = check_not_enough_evidence(payload, evidence)
        payload["not_enough_evidence"] = bool(not_enough)

        if not payload["strict"]:
            pass

        if payload["blockers"]:
            payload["result"] = RESULT_BLOCKED
            exit_code = 1
        elif not_enough:
            payload["result"] = RESULT_NOE
            exit_code = 1
        elif payload["warnings"]:
            payload["result"] = RESULT_WARN
            exit_code = 0
        else:
            payload["result"] = RESULT_PASS
            exit_code = 0

        if args.json:
            print(json.dumps(payload, ensure_ascii=False, indent=2))
        else:
            print(payload["result"])
        return exit_code

    except SystemExit:
        raise
    except Exception as exc:
        payload = make_payload(False)
        add_blocker(payload, f"checker internal error: {exc}")
        payload["result"] = RESULT_BLOCKED
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
