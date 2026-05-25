#!/usr/bin/env python3
"""M56 execution readiness CLI."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

CANONICAL_ACTIVE_TASK = "tasks/active-task.md"

INPUT_ROOT = "execution_readiness_input"
PRECONDITIONS_ROOT = "execution_preconditions"

INPUT_STATUS_READY = "EXECUTION_READINESS_INPUT_READY"
INPUT_STATUS_READY_WITH_LIMITATIONS = "EXECUTION_READINESS_INPUT_READY_WITH_LIMITATIONS"
INPUT_STATUS_NOT_READY = "EXECUTION_READINESS_INPUT_NOT_READY"
INPUT_STATUS_BLOCKED = "EXECUTION_READINESS_INPUT_BLOCKED"

PRECONDITIONS_STATUS_PASS = "EXECUTION_PRECONDITIONS_PASS"
PRECONDITIONS_STATUS_PASS_WITH_WARNINGS = "EXECUTION_PRECONDITIONS_PASS_WITH_WARNINGS"
PRECONDITIONS_STATUS_NOT_READY = "EXECUTION_PRECONDITIONS_NOT_READY"
PRECONDITIONS_STATUS_BLOCKED = "EXECUTION_PRECONDITIONS_BLOCKED"

RESULT_CONFIRMED = "EXECUTION_READINESS_CONFIRMED"
RESULT_CONFIRMED_WITH_LIMITATIONS = "EXECUTION_READINESS_CONFIRMED_WITH_LIMITATIONS"
RESULT_NOT_CONFIRMED = "EXECUTION_READINESS_NOT_CONFIRMED"
RESULT_BLOCKED = "EXECUTION_READINESS_BLOCKED"

NON_AUTHORITY_MARKERS = [
    "Execution readiness output is not approval.",
    "Execution readiness output does not authorize execution.",
    "Execution readiness output does not start execution.",
    "Execution readiness output does not create approval records.",
    "Execution readiness output does not authorize lifecycle mutation.",
    "Execution readiness output does not authorize M57.",
    "Execution readiness output does not start M57.",
]

# Required marker strings for M56 CLI validation:
# EXECUTION_READINESS_INPUT_READY_WITH_LIMITATIONS does not bypass active-task checks.
# EXECUTION_READINESS_INPUT_READY_WITH_LIMITATIONS does not bypass preconditions checks.
# Empty required_traceability objects must be treated as missing traceability.
# Empty required_boundaries objects must be treated as missing boundary markers.
# Empty non_authority_markers arrays must be treated as missing boundary markers.
# CLI JSON output must preserve required keys and basic JSON types.
# Unknown keys must not improve result classification.
# BLOCKED outranks NOT_CONFIRMED.
# NOT_CONFIRMED outranks CONFIRMED_WITH_LIMITATIONS.
# CONFIRMED_WITH_LIMITATIONS outranks CONFIRMED.

INPUT_NON_AUTHORITY_MARKERS = [
    "Execution readiness input is not approval.",
    "Execution readiness input does not authorize execution.",
    "Execution readiness input does not start execution.",
    "Execution readiness input does not create approval records.",
    "Execution readiness input does not authorize lifecycle mutation.",
    "Execution readiness input does not authorize M57.",
    "Execution readiness input does not start M57.",
]

PRECONDITIONS_NON_AUTHORITY_MARKERS = [
    "Execution preconditions are not approval.",
    "Execution preconditions do not authorize execution.",
    "Execution preconditions do not start execution.",
    "Execution preconditions do not create approval records.",
    "Execution preconditions do not authorize lifecycle mutation.",
    "Execution preconditions do not authorize M57.",
    "Execution preconditions do not start M57.",
]

REQUIRED_INPUT_KEYS = [
    "input_id",
    "input_status",
    "source_active_task",
    "active_task_path",
    "required_traceability",
    "required_scope",
    "required_validation",
    "required_boundaries",
    "carry_forward",
    "boundary_flags",
    "non_authority_markers",
]

REQUIRED_PRECONDITION_KEYS = [
    "preconditions_id",
    "preconditions_status",
    "source_execution_readiness_input",
    "source_active_task",
    "active_task_path",
    "required_active_task_structure",
    "required_traceability",
    "required_scope",
    "required_validation",
    "required_boundaries",
    "checked_preconditions",
    "missing_preconditions",
    "warnings",
    "blockers",
    "carry_forward",
    "boundary_flags",
    "performed_actions",
    "non_authority_markers",
]

REQUIRED_TRACEABILITY_KEYS = [
    "source_m55_completion_review",
    "source_m55_readiness_result",
    "source_m54_materialization_result",
    "source_m53_placement_result",
    "source_m52_validation_result",
    "source_queue_entry",
    "source_active_task",
]

REQUIRED_BOUNDARY_KEYS = [
    "execution_readiness_is_not_execution",
    "execution_readiness_is_not_approval",
    "execution_readiness_is_not_lifecycle_mutation",
    "execution_readiness_is_not_m57_authorization",
    "execution_does_not_start",
    "m57_does_not_start",
]

REQUIRED_ACTIVE_TASK_KEYS = [
    "active_task_exists",
    "frontmatter_valid",
    "task_id_present",
    "title_present",
    "mode_present",
    "repository_present",
    "branch_present",
    "goal_present",
]

ALLOWED_INPUT_STATUSES = {
    INPUT_STATUS_READY,
    INPUT_STATUS_READY_WITH_LIMITATIONS,
    INPUT_STATUS_NOT_READY,
    INPUT_STATUS_BLOCKED,
}

ALLOWED_PRECONDITION_STATUSES = {
    PRECONDITIONS_STATUS_PASS,
    PRECONDITIONS_STATUS_PASS_WITH_WARNINGS,
    PRECONDITIONS_STATUS_NOT_READY,
    PRECONDITIONS_STATUS_BLOCKED,
}

ACTIVE_TASK_SECTION_MARKERS = [
    "Goal",
    "Scope",
    "Validation",
    "Expected Final Report",
    "Final Rule",
]

ALLOW_MARKERS = [
    "Allowed to create",
    "Allowed to modify",
    "Allowed changes",
    "Scope",
]

FORBID_MARKERS = [
    "Forbidden to create",
    "Forbidden to modify",
    "Forbidden actions",
    "Forbidden Changes",
    "Do not",
]

UNSAFE_KEYS = {
    "execution_authorized",
    "execution_started",
    "approval_created",
    "lifecycle_mutation_authorized",
    "lifecycle_mutation_performed",
    "m57_authorized",
    "m57_started",
    "active_task_modified",
    "validation_commands_run",
}


class PackageError(Exception):
    pass


def explain_output() -> int:
    lines = [
        "M56 execution readiness CLI is read-only.",
        "The CLI checks readiness signals only.",
        "The CLI does not execute the active task.",
        "The CLI does not run validation commands.",
        "The CLI does not authorize execution.",
        "The CLI does not authorize lifecycle mutation.",
        "The CLI does not authorize M57.",
        "The CLI does not start M57.",
    ]
    sys.stdout.write("\n".join(lines) + "\n")
    return 0


def is_mapping(value: Any) -> bool:
    return isinstance(value, dict)


def same_filesystem_path(left: str, right: str) -> bool:
    try:
        return Path(str(left)).expanduser().resolve() == Path(str(right)).expanduser().resolve()
    except OSError:
        return False


def parse_markdown_json_blocks(text: str) -> dict[str, Any]:
    blocks = re.findall(r"(?ms)^```json\s*(.*?)\s*^```[ \t]*$", text)
    if len(blocks) != 1:
        raise PackageError("markdown package must contain exactly one fenced json block")
    try:
        loaded = json.loads(blocks[0])
    except json.JSONDecodeError as exc:
        raise PackageError("malformed json inside fenced block") from exc
    if not is_mapping(loaded):
        raise PackageError("package root must be an object")
    return loaded


def parse_package(path: Path) -> tuple[str, dict[str, Any], str]:
    if not path.exists():
        raise PackageError(f"missing file: {path}")
    text = path.read_text(encoding="utf-8")
    try:
        loaded = json.loads(text)
        if not is_mapping(loaded):
            raise PackageError("package root must be an object")
    except json.JSONDecodeError:
        loaded = parse_markdown_json_blocks(text)

    roots = [name for name in (INPUT_ROOT, PRECONDITIONS_ROOT) if name in loaded]
    if len(roots) != 1:
        raise PackageError("unsupported root object")

    root_name = roots[0]
    payload = loaded[root_name]
    if not is_mapping(payload):
        raise PackageError("supported root payload must be an object")
    return root_name, payload, text


def load_text(path: Path) -> str:
    if not path.exists():
        raise PackageError(f"missing file: {path}")
    return path.read_text(encoding="utf-8")


def collect_keys(value: Any) -> list[tuple[str, Any]]:
    found: list[tuple[str, Any]] = []
    if isinstance(value, dict):
        for key, nested in value.items():
            found.append((key, nested))
            found.extend(collect_keys(nested))
    elif isinstance(value, list):
        for item in value:
            found.extend(collect_keys(item))
    return found


def has_required_markers(text: str, markers: list[str]) -> bool:
    return any(marker in text for marker in markers)


def active_task_checks(text: str) -> tuple[dict[str, bool], list[str]]:
    present = {
        "task_id": bool(re.search(r"(?m)^\s*task_id\s*:", text)),
        "title": bool(re.search(r"(?m)^\s*title\s*:", text)),
        "mode": bool(re.search(r"(?m)^\s*mode\s*:", text)),
        "repository": bool(re.search(r"(?m)^\s*repository\s*:", text)),
        "branch": bool(re.search(r"(?m)^\s*branch\s*:", text)),
        "Goal": "Goal" in text,
        "Scope": "Scope" in text,
        "Validation": "Validation" in text,
        "Expected Final Report": "Expected Final Report" in text,
        "Final Rule": "Final Rule" in text,
        "allowed_change_marker": has_required_markers(text, ALLOW_MARKERS),
        "forbidden_change_marker": has_required_markers(text, FORBID_MARKERS),
    }
    missing = [
        name
        for name, is_present in present.items()
        if not is_present
    ]
    return present, missing


def ensure_required_keys(payload: dict[str, Any], required: list[str]) -> list[str]:
    return [name for name in required if name not in payload]


def ensure_required_traceability(value: Any) -> list[str]:
    if not is_mapping(value) or not value:
        return REQUIRED_TRACEABILITY_KEYS[:]
    missing = [name for name in REQUIRED_TRACEABILITY_KEYS if name not in value]
    return missing


def ensure_required_boundaries(value: Any) -> list[str]:
    if not is_mapping(value) or not value:
        return REQUIRED_BOUNDARY_KEYS[:]
    return [name for name in REQUIRED_BOUNDARY_KEYS if name not in value]


def ensure_required_non_authority(value: Any) -> bool:
    if not isinstance(value, list) or not value:
        return False
    return all(isinstance(item, str) for item in value)


def extract_text_list(value: Any) -> list[str]:
    if isinstance(value, list):
        return [item for item in value if isinstance(item, str)]
    return []


def has_all_markers(items: list[str], markers: list[str]) -> bool:
    return all(marker in items for marker in markers)


def has_unsafe_claims(value: Any) -> bool:
    if isinstance(value, dict):
        for key, nested in value.items():
            if key in UNSAFE_KEYS and nested is True:
                return True
            if has_unsafe_claims(nested):
                return True
    elif isinstance(value, list):
        return any(has_unsafe_claims(item) for item in value)
    return False


def has_unsafe_claims_in_text(text: str) -> bool:
    patterns = [
        r"(?mi)^\s*execution_authorized\s*:\s*true\s*$",
        r"(?mi)^\s*execution_started\s*:\s*true\s*$",
        r"(?mi)^\s*approval_created\s*:\s*true\s*$",
        r"(?mi)^\s*lifecycle_mutation_authorized\s*:\s*true\s*$",
        r"(?mi)^\s*lifecycle_mutation_performed\s*:\s*true\s*$",
        r"(?mi)^\s*m57_authorized\s*:\s*true\s*$",
        r"(?mi)^\s*m57_started\s*:\s*true\s*$",
        r"(?mi)^\s*active_task_modified\s*:\s*true\s*$",
        r"(?mi)^\s*validation_commands_run\s*:\s*true\s*$",
    ]
    return any(re.search(pattern, text) is not None for pattern in patterns)


def build_base_result(input_source: str, preconditions_source: str, active_task_read: bool) -> dict[str, Any]:
    return {
        "result": RESULT_BLOCKED,
        "exit_code": 2,
        "execution_ready": False,
        "active_task_valid": False,
        "preconditions_passed": False,
        "scope_ready": False,
        "validation_ready": False,
        "traceability_ready": False,
        "boundary_ready": False,
        "source_execution_readiness_input": input_source,
        "source_execution_preconditions": preconditions_source,
        "source_active_task": CANONICAL_ACTIVE_TASK,
        "active_task_path": CANONICAL_ACTIVE_TASK,
        "required_traceability": {name: "" for name in REQUIRED_TRACEABILITY_KEYS},
        "readiness_findings": [],
        "warnings": [],
        "blockers": [],
        "carry_forward": {
            "accepted_limitations": [],
            "warnings": [],
            "open_questions": [],
            "downstream_limits": [],
            "known_gaps": [],
            "non_authority_boundary": [
                "Execution readiness output is not approval.",
                "Execution readiness output does not authorize execution.",
                "Execution readiness output does not start execution.",
                "Execution readiness output does not create approval records.",
                "Execution readiness output does not authorize lifecycle mutation.",
                "Execution readiness output does not authorize M57.",
                "Execution readiness output does not start M57.",
            ],
        },
        "boundary_flags": {
            "execution_readiness_only": True,
            "execution_readiness_authorized": False,
            "execution_authorized": False,
            "execution_started": False,
            "approval_created": False,
            "lifecycle_mutation_authorized": False,
            "m57_authorized": False,
            "m57_started": False,
        },
        "performed_actions": {
            "active_task_read": active_task_read,
            "active_task_modified": False,
            "validation_commands_run": False,
            "execution_started": False,
            "approval_created": False,
            "lifecycle_mutation_performed": False,
            "m57_started": False,
        },
        "non_authority_markers": NON_AUTHORITY_MARKERS[:],
    }


def add_finding(result: dict[str, Any], text: str) -> None:
    if text not in result["readiness_findings"]:
        result["readiness_findings"].append(text)


def add_warning(result: dict[str, Any], text: str) -> None:
    if text not in result["warnings"]:
        result["warnings"].append(text)


def add_blocker(result: dict[str, Any], text: str) -> None:
    if text not in result["blockers"]:
        result["blockers"].append(text)


def add_carry_warning(result: dict[str, Any], text: str) -> None:
    warnings = result["carry_forward"]["warnings"]
    if text not in warnings:
        warnings.append(text)


def add_carry_limitations(result: dict[str, Any], text: str) -> None:
    limitations = result["carry_forward"]["accepted_limitations"]
    if text not in limitations:
        limitations.append(text)


def finalize_result(result: dict[str, Any], classification: str) -> dict[str, Any]:
    if classification == RESULT_CONFIRMED:
        result["result"] = RESULT_CONFIRMED
        result["exit_code"] = 0
        result["execution_ready"] = True
    elif classification == RESULT_CONFIRMED_WITH_LIMITATIONS:
        result["result"] = RESULT_CONFIRMED_WITH_LIMITATIONS
        result["exit_code"] = 0
        result["execution_ready"] = True
    elif classification == RESULT_NOT_CONFIRMED:
        result["result"] = RESULT_NOT_CONFIRMED
        result["exit_code"] = 1
        result["execution_ready"] = False
    else:
        result["result"] = RESULT_BLOCKED
        result["exit_code"] = 2
        result["execution_ready"] = False
    return result


def print_human(result: dict[str, Any]) -> None:
    lines = [
        f"EXECUTION_READINESS_RESULT: {result['result']}",
        f"EXIT_CODE: {result['exit_code']}",
        f"EXECUTION_READY: {result['execution_ready']}",
        f"ACTIVE_TASK_VALID: {result['active_task_valid']}",
        f"PRECONDITIONS_PASSED: {result['preconditions_passed']}",
        f"BLOCKERS: {', '.join(result['blockers']) if result['blockers'] else 'none'}",
        f"WARNINGS: {', '.join(result['warnings']) if result['warnings'] else 'none'}",
        f"NON_AUTHORITY: {', '.join(result['non_authority_markers'])}",
        "Execution readiness is not execution authorization.",
    ]
    sys.stdout.write("\n".join(lines) + "\n")


def emit_json(result: dict[str, Any]) -> None:
    payload = {"execution_readiness_result": result}
    sys.stdout.write(json.dumps(payload, indent=2) + "\n")


def classify(args: argparse.Namespace) -> tuple[dict[str, Any], int]:
    input_path = args.input
    preconditions_path = args.preconditions
    active_task_path = args.active_task

    if not input_path or not preconditions_path or not active_task_path:
        result = build_base_result(
            str(input_path) if input_path else "",
            str(preconditions_path) if preconditions_path else "",
            False,
        )
        add_blocker(result, "missing required CLI argument")
        return finalize_result(result, RESULT_BLOCKED), 2

    input_file = Path(input_path)
    preconditions_file = Path(preconditions_path)
    active_task_file = Path(active_task_path)

    result = build_base_result(str(input_file), str(preconditions_file), False)

    try:
        input_root_name, input_payload, _ = parse_package(input_file)
        preconditions_root_name, preconditions_payload, _ = parse_package(preconditions_file)
        active_task_text = load_text(active_task_file)
        result["performed_actions"]["active_task_read"] = True
    except PackageError as exc:
        add_blocker(result, str(exc))
        return finalize_result(result, RESULT_BLOCKED), 2

    if input_root_name != INPUT_ROOT or preconditions_root_name != PRECONDITIONS_ROOT:
        add_blocker(result, "unsupported root object")
        return finalize_result(result, RESULT_BLOCKED), 2

    input_missing = ensure_required_keys(input_payload, REQUIRED_INPUT_KEYS)
    preconditions_missing = ensure_required_keys(preconditions_payload, REQUIRED_PRECONDITION_KEYS)
    if input_missing or preconditions_missing:
        for item in input_missing + preconditions_missing:
            add_blocker(result, f"missing required JSON key: {item}")
        return finalize_result(result, RESULT_BLOCKED), 2

    input_traceability_missing = ensure_required_traceability(input_payload["required_traceability"])
    preconditions_traceability_missing = ensure_required_traceability(preconditions_payload["required_traceability"])
    if input_traceability_missing or preconditions_traceability_missing:
        add_blocker(result, "missing traceability in packages")
        for item in input_traceability_missing + preconditions_traceability_missing:
            add_finding(result, f"traceability gap: {item}")
        return finalize_result(result, RESULT_BLOCKED), 2

    input_boundaries_missing = ensure_required_boundaries(input_payload["required_boundaries"])
    preconditions_boundaries_missing = ensure_required_boundaries(preconditions_payload["required_boundaries"])
    if input_boundaries_missing or preconditions_boundaries_missing:
        add_blocker(result, "missing boundary markers in packages")
        return finalize_result(result, RESULT_BLOCKED), 2

    if not ensure_required_non_authority(input_payload["non_authority_markers"]):
        add_blocker(result, "missing boundary markers in packages")
        return finalize_result(result, RESULT_BLOCKED), 2
    if not ensure_required_non_authority(preconditions_payload["non_authority_markers"]):
        add_blocker(result, "missing boundary markers in packages")
        return finalize_result(result, RESULT_BLOCKED), 2

    input_status = input_payload["input_status"]
    preconditions_status = preconditions_payload["preconditions_status"]
    if input_status not in ALLOWED_INPUT_STATUSES:
        add_blocker(result, "unknown input status")
        return finalize_result(result, RESULT_BLOCKED), 2
    if preconditions_status not in ALLOWED_PRECONDITION_STATUSES:
        add_blocker(result, "unknown preconditions status")
        return finalize_result(result, RESULT_BLOCKED), 2

    result["preconditions_passed"] = preconditions_status in {
        PRECONDITIONS_STATUS_PASS,
        PRECONDITIONS_STATUS_PASS_WITH_WARNINGS,
    }

    if input_payload["source_active_task"] != CANONICAL_ACTIVE_TASK:
        add_blocker(result, "source/path mismatch")
        return finalize_result(result, RESULT_BLOCKED), 2
    if input_payload["active_task_path"] != CANONICAL_ACTIVE_TASK:
        add_blocker(result, "source/path mismatch")
        return finalize_result(result, RESULT_BLOCKED), 2
    if preconditions_payload["source_active_task"] != CANONICAL_ACTIVE_TASK:
        add_blocker(result, "source/path mismatch")
        return finalize_result(result, RESULT_BLOCKED), 2
    if preconditions_payload["active_task_path"] != CANONICAL_ACTIVE_TASK:
        add_blocker(result, "source/path mismatch")
        return finalize_result(result, RESULT_BLOCKED), 2
    if has_unsafe_claims(input_payload) or has_unsafe_claims(preconditions_payload) or has_unsafe_claims_in_text(active_task_text):
        add_blocker(result, "unsafe authorization claim")
        return finalize_result(result, RESULT_BLOCKED), 2

    active_task_structure, missing_active_task_markers = active_task_checks(active_task_text)
    result["active_task_valid"] = len(missing_active_task_markers) == 0
    result["scope_ready"] = active_task_structure["Scope"] and active_task_structure["allowed_change_marker"] and active_task_structure["forbidden_change_marker"]
    result["validation_ready"] = active_task_structure["Validation"] and active_task_structure["Expected Final Report"] and active_task_structure["Final Rule"]
    result["traceability_ready"] = True
    result["boundary_ready"] = True

    for key, value in active_task_structure.items():
        if not value:
            add_finding(result, f"missing active-task marker: {key}")

    if not result["scope_ready"]:
        add_finding(result, "active-task scope gap")
    if not result["validation_ready"]:
        add_finding(result, "active-task validation gap")

    for key in REQUIRED_TRACEABILITY_KEYS:
        result["required_traceability"][key] = preconditions_payload["required_traceability"][key]

    if any(not bool(input_payload["required_boundaries"][key]) for key in REQUIRED_BOUNDARY_KEYS):
        add_blocker(result, "missing boundary markers in packages")
        return finalize_result(result, RESULT_BLOCKED), 2
    if any(not bool(preconditions_payload["required_boundaries"][key]) for key in REQUIRED_BOUNDARY_KEYS):
        add_blocker(result, "missing boundary markers in packages")
        return finalize_result(result, RESULT_BLOCKED), 2

    for key, expected in (
        ("execution_readiness_is_not_execution", True),
        ("execution_readiness_is_not_approval", True),
        ("execution_readiness_is_not_lifecycle_mutation", True),
        ("execution_readiness_is_not_m57_authorization", True),
        ("execution_does_not_start", True),
        ("m57_does_not_start", True),
    ):
        if not bool(input_payload["required_boundaries"][key]) or not bool(preconditions_payload["required_boundaries"][key]):
            add_blocker(result, "missing boundary markers in packages")
            return finalize_result(result, RESULT_BLOCKED), 2

    input_markers = extract_text_list(input_payload["non_authority_markers"])
    precondition_markers = extract_text_list(preconditions_payload["non_authority_markers"])
    if not has_all_markers(input_markers, INPUT_NON_AUTHORITY_MARKERS):
        add_blocker(result, "missing boundary markers in packages")
        return finalize_result(result, RESULT_BLOCKED), 2
    if not has_all_markers(precondition_markers, PRECONDITIONS_NON_AUTHORITY_MARKERS):
        add_blocker(result, "missing boundary markers in packages")
        return finalize_result(result, RESULT_BLOCKED), 2

    if not active_task_structure["task_id"]:
        add_finding(result, "task_id missing")
    if not active_task_structure["title"]:
        add_finding(result, "title missing")
    if not active_task_structure["mode"]:
        add_finding(result, "mode missing")
    if not active_task_structure["repository"]:
        add_finding(result, "repository missing")
    if not active_task_structure["branch"]:
        add_finding(result, "branch missing")

    if not active_task_structure["Goal"] or not active_task_structure["Scope"] or not active_task_structure["Validation"] or not active_task_structure["Expected Final Report"] or not active_task_structure["Final Rule"]:
        result["active_task_valid"] = False

    input_warnings = []
    input_warnings.extend(extract_text_list(input_payload.get("carry_forward", {}).get("warnings", [])))
    input_warnings.extend(extract_text_list(input_payload.get("carry_forward", {}).get("accepted_limitations", [])))
    preconditions_warnings = extract_text_list(preconditions_payload.get("warnings", []))
    preconditions_blockers = extract_text_list(preconditions_payload.get("blockers", []))
    carry_warnings = extract_text_list(preconditions_payload.get("carry_forward", {}).get("warnings", []))
    carry_limitations = extract_text_list(preconditions_payload.get("carry_forward", {}).get("accepted_limitations", []))

    for item in input_warnings + preconditions_warnings + carry_warnings:
        add_warning(result, item)
    for item in carry_limitations:
        add_warning(result, item)
        add_carry_limitations(result, item)
    for item in input_warnings + preconditions_warnings + carry_warnings:
        add_carry_warning(result, item)

    if input_payload["input_status"] == INPUT_STATUS_BLOCKED:
        add_blocker(result, "input blocked")
        return finalize_result(result, RESULT_BLOCKED), 2
    if preconditions_status == PRECONDITIONS_STATUS_BLOCKED:
        add_blocker(result, "preconditions blocked")
        return finalize_result(result, RESULT_BLOCKED), 2

    if input_payload["input_status"] == INPUT_STATUS_NOT_READY:
        add_finding(result, "input not ready")
        return finalize_result(result, RESULT_NOT_CONFIRMED), 1
    if preconditions_status == PRECONDITIONS_STATUS_NOT_READY:
        add_finding(result, "preconditions not ready")
        return finalize_result(result, RESULT_NOT_CONFIRMED), 1

    if any(text for text in preconditions_blockers):
        for item in preconditions_blockers:
            add_blocker(result, item)
        return finalize_result(result, RESULT_BLOCKED), 2

    if not result["active_task_valid"]:
        add_finding(result, "active-task structural gap")
        return finalize_result(result, RESULT_NOT_CONFIRMED), 1

    if not result["scope_ready"]:
        add_finding(result, "missing active-task scope section")
        return finalize_result(result, RESULT_NOT_CONFIRMED), 1
    if not result["validation_ready"]:
        add_finding(result, "missing active-task validation section")
        add_finding(result, "missing active-task expected final report section")
        add_finding(result, "missing active-task final rule section")
        return finalize_result(result, RESULT_NOT_CONFIRMED), 1

    if input_payload.get("boundary_flags", {}).get("execution_authorized") is True:
        add_blocker(result, "unsafe authorization claim")
        return finalize_result(result, RESULT_BLOCKED), 2
    if preconditions_payload.get("boundary_flags", {}).get("execution_started") is True:
        add_blocker(result, "performed action violation")
        return finalize_result(result, RESULT_BLOCKED), 2

    if result["warnings"]:
        add_finding(result, "warnings present")
        return finalize_result(result, RESULT_CONFIRMED_WITH_LIMITATIONS), 0

    if input_payload["input_status"] == INPUT_STATUS_READY_WITH_LIMITATIONS:
        add_finding(result, "input ready with limitations")
        return finalize_result(result, RESULT_CONFIRMED_WITH_LIMITATIONS), 0
    if preconditions_status == PRECONDITIONS_STATUS_PASS_WITH_WARNINGS:
        add_finding(result, "preconditions pass with warnings")
        return finalize_result(result, RESULT_CONFIRMED_WITH_LIMITATIONS), 0

    if input_payload["input_status"] == INPUT_STATUS_READY and preconditions_status == PRECONDITIONS_STATUS_PASS:
        add_finding(result, "clean readiness")
        return finalize_result(result, RESULT_CONFIRMED), 0

    add_blocker(result, "contradictory cross-source claims")
    return finalize_result(result, RESULT_BLOCKED), 2


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="check-execution-readiness")
    parser.add_argument("--input")
    parser.add_argument("--preconditions")
    parser.add_argument("--active-task")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--explain", action="store_true")
    args = parser.parse_args(argv)

    if args.explain:
        return explain_output()

    result, code = classify(args)
    if args.json:
        emit_json(result)
    else:
        print_human(result)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
