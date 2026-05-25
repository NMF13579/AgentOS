#!/usr/bin/env python3
import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

RESULT_CONFIRMED = "ACTIVE_TASK_READINESS_CONFIRMED"
RESULT_CONFIRMED_WITH_LIMITATIONS = "ACTIVE_TASK_READINESS_CONFIRMED_WITH_LIMITATIONS"
RESULT_NOT_CONFIRMED = "ACTIVE_TASK_READINESS_NOT_CONFIRMED"
RESULT_BLOCKED = "ACTIVE_TASK_READINESS_BLOCKED"

EXIT_BY_RESULT = {
    RESULT_CONFIRMED: 0,
    RESULT_CONFIRMED_WITH_LIMITATIONS: 0,
    RESULT_NOT_CONFIRMED: 1,
    RESULT_BLOCKED: 2,
}

FORBIDDEN_FLAGS = {
    "--write",
    "--apply",
    "--replace-active-task",
    "--approve",
    "--execute",
    "--start-m56",
    "--fixtures",
}

INPUT_MARKERS = [
    "Active-task readiness is not approval.",
    "Active-task readiness does not authorize execution.",
    "Active-task readiness does not authorize active-task replacement.",
    "Active-task readiness does not write tasks/active-task.md.",
    "Active-task readiness does not create approval records.",
    "Active-task readiness does not authorize M56.",
    "Active-task readiness does not start M56.",
]

PROPOSAL_MARKERS = [
    "Active-task proposal is not approval.",
    "Active-task proposal does not authorize execution.",
    "Active-task proposal does not authorize active-task replacement.",
    "Active-task proposal does not write tasks/active-task.md.",
    "Active-task proposal does not create approval records.",
    "Active-task proposal does not authorize M56.",
    "Active-task proposal does not start M56.",
]

OUTPUT_MARKERS = [
    "M55 readiness output is not approval.",
    "M55 readiness output does not authorize execution.",
    "M55 readiness output does not authorize active-task replacement.",
    "M55 readiness output does not write tasks/active-task.md.",
    "M55 readiness output does not create approval records.",
    "M55 readiness output does not authorize M56.",
    "M55 readiness output does not start M56.",
]

REQUIRED_INPUT_FIELDS = [
    "input_id",
    "input_status",
    "source_m54_completion_review",
    "source_m54_materialization_result",
    "source_queue_entry",
    "source_m53_placement_result",
    "source_m52_validation_result",
    "target_active_task_path",
    "required_traceability",
    "carry_forward",
    "boundary_flags",
    "non_authority_markers",
]

REQUIRED_PROPOSAL_FIELDS = [
    "proposal_id",
    "proposal_status",
    "source_active_task_readiness_input",
    "source_m54_completion_review",
    "source_m54_materialization_result",
    "source_queue_entry",
    "source_m53_placement_result",
    "source_m52_validation_result",
    "checked_queue_entry_id",
    "target_active_task_path",
    "proposed_active_task",
    "required_traceability",
    "carry_forward",
    "proposal_findings",
    "warnings",
    "blockers",
    "boundary_flags",
    "non_authority_markers",
]

TRACEABILITY_KEYS = [
    "source_proposal",
    "source_authorization",
    "source_conversion_package",
    "source_generated_artifact",
    "m50_traceability",
    "m51_generator_evidence",
    "m52_validation_evidence",
    "m53_placement_review_evidence",
    "m54_materialization_evidence",
    "queue_entry_evidence",
    "m55_readiness_input_evidence",
]

CARRY_FORWARD_KEYS = [
    "accepted_limitations",
    "warnings",
    "open_questions",
    "downstream_limits",
    "known_gaps",
    "non_authority_boundary",
]

REQUIRED_UPSTREAM_FILES = [
    "reports/m55-m54-readiness-intake.md",
    "docs/TASK-CANDIDATE-ACTIVE-TASK-READINESS-ARCHITECTURE.md",
    "docs/TASK-CANDIDATE-ACTIVE-TASK-READINESS-INPUT-CONTRACT.md",
    "docs/ACTIVE-TASK-PROPOSAL-CONTRACT.md",
    "docs/TASK-CANDIDATE-ACTIVE-TASK-READINESS-OUTPUT-CONTRACT.md",
    "docs/TASK-CANDIDATE-ACTIVE-TASK-READINESS-POLICY.md",
    "schemas/task-candidate-active-task-readiness-input.schema.json",
    "schemas/active-task-proposal.schema.json",
    "schemas/task-candidate-active-task-readiness-result.schema.json",
    "templates/task-candidate-active-task-readiness-input.md",
    "templates/active-task-proposal.md",
    "templates/task-candidate-active-task-readiness-result.md",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("--explain", action="store_true")
    parser.add_argument("--input")
    parser.add_argument("--proposal")
    parser.add_argument("--queue-entry")
    parser.add_argument("--repo-root")
    parser.add_argument("--json", action="store_true")
    args, unknown = parser.parse_known_args()
    setattr(args, "unknown_args", unknown)
    return args


def block_result(
    blocker: str,
    message: str,
    input_path: str = "",
    proposal_path: str = "",
    queue_entry: str = "",
) -> Dict[str, Any]:
    return _base_result(
        result=RESULT_BLOCKED,
        blockers=[blocker],
        readiness_findings=[message],
        input_path=input_path,
        proposal_path=proposal_path,
        queue_entry=queue_entry,
    )


def not_confirmed_result(
    blocker: str,
    message: str,
    input_path: str,
    proposal_path: str,
    queue_entry: str,
) -> Dict[str, Any]:
    return _base_result(
        result=RESULT_NOT_CONFIRMED,
        blockers=[blocker],
        readiness_findings=[message],
        input_path=input_path,
        proposal_path=proposal_path,
        queue_entry=queue_entry,
    )


def confirmed_result(
    result_token: str,
    input_obj: Dict[str, Any],
    proposal_obj: Dict[str, Any],
    queue_entry: str,
) -> Dict[str, Any]:
    checked_id = proposal_obj.get("checked_queue_entry_id") or input_obj.get("checked_queue_entry_id") or "QUEUE_ENTRY_ID"
    carry = proposal_obj.get("carry_forward") if isinstance(proposal_obj.get("carry_forward"), dict) else input_obj.get("carry_forward", {})
    return {
        "active_task_readiness_result": {
            "result": result_token,
            "exit_code": EXIT_BY_RESULT[result_token],
            "readiness_confirmed": result_token in {RESULT_CONFIRMED, RESULT_CONFIRMED_WITH_LIMITATIONS},
            "proposal_ready_for_review": result_token in {RESULT_CONFIRMED, RESULT_CONFIRMED_WITH_LIMITATIONS},
            "active_task_replacement_authorized": False,
            "active_task_file_created": False,
            "checked_queue_entry_id": checked_id,
            "target_active_task_path": "tasks/active-task.md",
            "source_active_task_readiness_input": "",
            "source_active_task_proposal": "",
            "source_m54_completion_review": "reports/m54-completion-review.md",
            "source_m54_materialization_result": _as_str(input_obj.get("source_m54_materialization_result")),
            "source_queue_entry": queue_entry,
            "source_m53_placement_result": _as_str(input_obj.get("source_m53_placement_result")),
            "source_m52_validation_result": _as_str(input_obj.get("source_m52_validation_result")),
            "required_traceability": proposal_obj.get("required_traceability", input_obj.get("required_traceability", {})),
            "carry_forward": carry,
            "readiness_findings": [],
            "warnings": _as_list(proposal_obj.get("warnings", [])),
            "blockers": [],
            "boundary_flags": _boundary_flags(),
            "performed_actions": _performed_actions(),
            "non_authority_markers": OUTPUT_MARKERS,
        }
    }


def load_json_or_markdown_json(path: Path) -> Tuple[Optional[Dict[str, Any]], Optional[str]]:
    if not path.is_file():
        return None, "QUEUE_ENTRY_MISSING"
    text = path.read_text(encoding="utf-8")
    suffix = path.suffix.lower()
    if suffix == ".json":
        try:
            return json.loads(text), None
        except json.JSONDecodeError:
            return None, "MALFORMED_JSON"

    matches = re.findall(r"```\s*json\s*(.*?)\s*```", text, flags=re.DOTALL | re.IGNORECASE)
    if len(matches) == 0:
        return None, "MISSING_JSON_BLOCK"
    if len(matches) > 1:
        return None, "MULTIPLE_JSON_BLOCKS"
    try:
        return json.loads(matches[0]), None
    except json.JSONDecodeError:
        return None, "MALFORMED_JSON"


def validate_repo_root(repo_root: str) -> Optional[str]:
    path = Path(repo_root)
    if not path.is_dir():
        return "REPO_ROOT_INVALID"
    return None


def validate_queue_entry_path(repo_root: Path, queue_entry: str) -> Tuple[Optional[Path], Optional[str]]:
    if not queue_entry or queue_entry.startswith("/"):
        return None, "QUEUE_ENTRY_PATH_UNSAFE"
    if ".." in queue_entry.split("/"):
        return None, "QUEUE_ENTRY_PATH_UNSAFE"
    if queue_entry == "tasks/active-task.md":
        return None, "QUEUE_ENTRY_PATH_UNSAFE"
    if not queue_entry.startswith("tasks/queue/") or not queue_entry.endswith(".md"):
        return None, "QUEUE_ENTRY_PATH_UNSAFE"
    for denied in ("approvals/", "reports/", "generated/"):
        if queue_entry.startswith(denied):
            return None, "QUEUE_ENTRY_PATH_UNSAFE"

    resolved = (repo_root / queue_entry).resolve()
    queue_root = (repo_root / "tasks/queue").resolve()
    if not str(resolved).startswith(str(queue_root) + "/"):
        return None, "QUEUE_ENTRY_PATH_UNSAFE"
    if not resolved.is_file():
        return None, "QUEUE_ENTRY_MISSING"
    return resolved, None


def load_required_upstream_files(repo_root: Path) -> Optional[str]:
    for rel in REQUIRED_UPSTREAM_FILES:
        if not (repo_root / rel).is_file():
            return "UPSTREAM_CONTRACT_MISSING"
    return None


def parse_intake_status(repo_root: Path) -> Tuple[Optional[str], Optional[str]]:
    intake = repo_root / "reports/m55-m54-readiness-intake.md"
    text = intake.read_text(encoding="utf-8")
    match = re.search(r"^\s*intake_status:\s*(\S+)\s*$", text, flags=re.MULTILINE)
    if not match:
        return None, "M55_INTAKE_UNKNOWN"
    status = match.group(1).strip()
    if status == "M55_INTAKE_BLOCKED":
        return None, "M55_INTAKE_BLOCKED"
    if status not in {"M55_INTAKE_READY", "M55_INTAKE_READY_WITH_LIMITATIONS"}:
        return None, "M55_INTAKE_UNKNOWN"
    return status, None


def validate_input_package(input_obj: Dict[str, Any], queue_entry: str) -> Optional[str]:
    for key in REQUIRED_INPUT_FIELDS:
        if key not in input_obj:
            return "INPUT_REQUIRED_FIELD_MISSING"
    if input_obj.get("target_active_task_path") != "tasks/active-task.md":
        return "INPUT_TARGET_ACTIVE_TASK_PATH_INVALID"
    if input_obj.get("source_m54_completion_review") != "reports/m54-completion-review.md":
        return "INPUT_REQUIRED_FIELD_MISSING"
    if input_obj.get("source_queue_entry") != queue_entry:
        return "INPUT_QUEUE_ENTRY_MISMATCH"

    flags = input_obj.get("boundary_flags")
    if not isinstance(flags, dict):
        return "INPUT_REQUIRED_FIELD_MISSING"
    unsafe = [
        "active_task_replacement_authorized",
        "active_task_write_allowed",
        "execution_authorized",
        "approval_created",
        "lifecycle_mutation_authorized",
        "m56_authorized",
        "m56_started",
    ]
    for key in unsafe:
        if flags.get(key) is True:
            return "INPUT_AUTHORITY_ESCALATION"
    return None


def validate_proposal_package(
    proposal_obj: Dict[str, Any],
    queue_entry: str,
    input_path: str,
) -> Optional[str]:
    for key in REQUIRED_PROPOSAL_FIELDS:
        if key not in proposal_obj:
            return "PROPOSAL_REQUIRED_FIELD_MISSING"

    status = proposal_obj.get("proposal_status")
    if status not in {
        "ACTIVE_TASK_PROPOSAL_DRAFT",
        "ACTIVE_TASK_PROPOSAL_READY_FOR_REVIEW",
        "ACTIVE_TASK_PROPOSAL_BLOCKED",
    }:
        return "PROPOSAL_STATUS_UNKNOWN"

    if proposal_obj.get("target_active_task_path") != "tasks/active-task.md":
        return "PROPOSAL_TARGET_ACTIVE_TASK_PATH_INVALID"
    if proposal_obj.get("source_m54_completion_review") != "reports/m54-completion-review.md":
        return "PROPOSAL_REQUIRED_FIELD_MISSING"
    if proposal_obj.get("source_queue_entry") != queue_entry:
        return "PROPOSAL_QUEUE_ENTRY_MISMATCH"

    if _normalize_path(proposal_obj.get("source_active_task_readiness_input")) != _normalize_path(input_path):
        return "PROPOSAL_INPUT_MISMATCH"

    proposed = proposal_obj.get("proposed_active_task")
    if not isinstance(proposed, dict):
        return "PROPOSAL_REQUIRED_FIELD_MISSING"
    if proposed.get("required_human_review") is not True:
        return "PROPOSAL_HUMAN_REVIEW_REQUIRED"
    if proposed.get("source_queue_entry") != queue_entry:
        return "PROPOSAL_QUEUE_ENTRY_MISMATCH"

    flags = proposal_obj.get("boundary_flags")
    if not isinstance(flags, dict):
        return "PROPOSAL_REQUIRED_FIELD_MISSING"
    required_false = [
        "active_task_file_created",
        "active_task_replacement_authorized",
        "active_task_write_allowed",
        "execution_authorized",
        "approval_created",
        "lifecycle_mutation_authorized",
        "m56_authorized",
        "m56_started",
    ]
    if flags.get("proposal_only") is not True:
        return "PROPOSAL_AUTHORITY_ESCALATION"
    for key in required_false:
        if flags.get(key) is True:
            return "PROPOSAL_AUTHORITY_ESCALATION"
    return None


def validate_queue_entry_content(text: str) -> Optional[str]:
    required = [
        "Queue entry is not active task.",
        "Queue entry does not authorize active-task replacement.",
        "Queue entry does not authorize execution.",
        "Queue entry does not authorize M56.",
    ]
    for marker in required:
        if marker not in text:
            return "QUEUE_ENTRY_BOUNDARY_MARKERS_MISSING"

    unsafe_claims = [
        "active_task_replacement_authorized: true",
        "active_task_file_created: true",
        "active_task_write_allowed: true",
        "execution_authorized: true",
        "approval_created: true",
        "lifecycle_mutation_authorized: true",
        "m56_authorized: true",
        "m56_started: true",
    ]
    for claim in unsafe_claims:
        if claim in text:
            return "QUEUE_ENTRY_AUTHORITY_ESCALATION"
    return None


def validate_traceability(
    input_obj: Dict[str, Any],
    proposal_obj: Dict[str, Any],
) -> Optional[str]:
    input_trace = input_obj.get("required_traceability")
    proposal_trace = proposal_obj.get("required_traceability")
    if not isinstance(input_trace, dict) or not isinstance(proposal_trace, dict):
        return "TRACEABILITY_INCOMPLETE"
    for key in TRACEABILITY_KEYS:
        if not _non_empty_str(input_trace.get(key)):
            return "TRACEABILITY_INCOMPLETE"
        if not _non_empty_str(proposal_trace.get(key)):
            return "TRACEABILITY_INCOMPLETE"
    if not _non_empty_str(proposal_trace.get("m55_active_task_proposal_evidence")):
        return "TRACEABILITY_INCOMPLETE"
    return None


def validate_carry_forward(
    input_obj: Dict[str, Any],
    proposal_obj: Dict[str, Any],
) -> Optional[str]:
    input_carry = input_obj.get("carry_forward")
    proposal_carry = proposal_obj.get("carry_forward")
    if not isinstance(input_carry, dict) or not isinstance(proposal_carry, dict):
        return "CARRY_FORWARD_INCOMPLETE"

    for key in CARRY_FORWARD_KEYS:
        if not isinstance(input_carry.get(key), list):
            return "CARRY_FORWARD_INCOMPLETE"
        if not isinstance(proposal_carry.get(key), list):
            return "CARRY_FORWARD_INCOMPLETE"

    if len(input_carry.get("non_authority_boundary", [])) == 0:
        return "NON_AUTHORITY_BOUNDARY_MISSING"
    if len(proposal_carry.get("non_authority_boundary", [])) == 0:
        return "NON_AUTHORITY_BOUNDARY_MISSING"
    return None


def validate_non_authority_markers(
    input_obj: Dict[str, Any],
    proposal_obj: Dict[str, Any],
) -> Optional[str]:
    input_pool = set(_as_list(input_obj.get("non_authority_markers"))) | set(
        _as_list(input_obj.get("carry_forward", {}).get("non_authority_boundary", []))
    )
    proposal_pool = set(_as_list(proposal_obj.get("non_authority_markers"))) | set(
        _as_list(proposal_obj.get("carry_forward", {}).get("non_authority_boundary", []))
    )

    for marker in INPUT_MARKERS:
        if marker not in input_pool:
            return "NON_AUTHORITY_MARKERS_MISSING"
    for marker in PROPOSAL_MARKERS:
        if marker not in proposal_pool:
            return "NON_AUTHORITY_MARKERS_MISSING"
    return None


def validate_no_authority_escalation(input_obj: Dict[str, Any], proposal_obj: Dict[str, Any]) -> Optional[str]:
    unsafe_fields = {
        "active_task_replacement_authorized",
        "active_task_file_created",
        "active_task_write_allowed",
        "execution_authorized",
        "approval_created",
        "lifecycle_mutation_authorized",
        "m56_authorized",
        "m56_started",
    }

    def find_unsafe(value: Any) -> bool:
        if isinstance(value, dict):
            for k, v in value.items():
                if k in unsafe_fields and v is True:
                    return True
                if find_unsafe(v):
                    return True
        elif isinstance(value, list):
            for item in value:
                if find_unsafe(item):
                    return True
        return False

    if find_unsafe(input_obj) or find_unsafe(proposal_obj):
        return "AUTHORITY_ESCALATION"

    actions = proposal_obj.get("performed_actions")
    if isinstance(actions, dict):
        for key in [
            "active_task_file_created",
            "active_task_replacement_performed",
            "approval_created",
            "execution_started",
            "lifecycle_mutation_performed",
            "m56_started",
        ]:
            if actions.get(key) is True:
                return "AUTHORITY_ESCALATION"

    return None


def select_result(input_obj: Dict[str, Any], proposal_obj: Dict[str, Any]) -> str:
    proposal_status = proposal_obj.get("proposal_status")
    if proposal_status in {"ACTIVE_TASK_PROPOSAL_DRAFT", "ACTIVE_TASK_PROPOSAL_BLOCKED"}:
        return RESULT_NOT_CONFIRMED

    carry_input = input_obj.get("carry_forward", {})
    carry_proposal = proposal_obj.get("carry_forward", {})
    has_limits = False
    for key in ["accepted_limitations", "warnings", "open_questions", "downstream_limits", "known_gaps"]:
        if _as_list(carry_input.get(key)):
            has_limits = True
        if _as_list(carry_proposal.get(key)):
            has_limits = True

    proposal_blockers = _as_list(proposal_obj.get("blockers", []))
    if proposal_blockers:
        has_limits = True

    if has_limits:
        return RESULT_CONFIRMED_WITH_LIMITATIONS
    return RESULT_CONFIRMED


def emit_json(payload: Dict[str, Any]) -> None:
    sys.stdout.write(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


def emit_human(payload: Dict[str, Any]) -> None:
    result = payload["active_task_readiness_result"]
    sys.stdout.write("M55_ACTIVE_TASK_READINESS_RESULT:\n")
    sys.stdout.write(f"result: {result['result']}\n")
    sys.stdout.write(f"exit_code: {result['exit_code']}\n")
    sys.stdout.write(f"readiness_confirmed: {str(result['readiness_confirmed']).lower()}\n")
    sys.stdout.write(f"proposal_ready_for_review: {str(result['proposal_ready_for_review']).lower()}\n")
    sys.stdout.write(f"blockers: {json.dumps(result['blockers'])}\n")
    sys.stdout.write("M55 readiness output is not approval.\n")
    sys.stdout.write("M55 readiness output does not authorize execution.\n")
    sys.stdout.write("M55 readiness output does not authorize active-task replacement.\n")
    sys.stdout.write("M55 readiness output does not authorize M56.\n")


def _base_result(
    result: str,
    blockers: List[str],
    readiness_findings: List[str],
    input_path: str,
    proposal_path: str,
    queue_entry: str,
) -> Dict[str, Any]:
    return {
        "active_task_readiness_result": {
            "result": result,
            "exit_code": EXIT_BY_RESULT[result],
            "readiness_confirmed": result in {RESULT_CONFIRMED, RESULT_CONFIRMED_WITH_LIMITATIONS},
            "proposal_ready_for_review": result in {RESULT_CONFIRMED, RESULT_CONFIRMED_WITH_LIMITATIONS},
            "active_task_replacement_authorized": False,
            "active_task_file_created": False,
            "checked_queue_entry_id": "QUEUE_ENTRY_ID",
            "target_active_task_path": "tasks/active-task.md",
            "source_active_task_readiness_input": input_path,
            "source_active_task_proposal": proposal_path,
            "source_m54_completion_review": "reports/m54-completion-review.md",
            "source_m54_materialization_result": "",
            "source_queue_entry": queue_entry,
            "source_m53_placement_result": "",
            "source_m52_validation_result": "",
            "required_traceability": {},
            "carry_forward": {
                "accepted_limitations": [],
                "warnings": [],
                "open_questions": [],
                "downstream_limits": [],
                "known_gaps": [],
                "non_authority_boundary": OUTPUT_MARKERS,
            },
            "readiness_findings": readiness_findings,
            "warnings": [],
            "blockers": blockers,
            "boundary_flags": _boundary_flags(),
            "performed_actions": _performed_actions(),
            "non_authority_markers": OUTPUT_MARKERS,
        }
    }


def _boundary_flags() -> Dict[str, Any]:
    return {
        "readiness_result_only": True,
        "active_task_file_created": False,
        "active_task_replacement_authorized": False,
        "active_task_write_allowed": False,
        "execution_authorized": False,
        "approval_created": False,
        "lifecycle_mutation_authorized": False,
        "m56_authorized": False,
        "m56_started": False,
    }


def _performed_actions() -> Dict[str, bool]:
    return {
        "active_task_file_created": False,
        "active_task_replacement_performed": False,
        "approval_created": False,
        "execution_started": False,
        "lifecycle_mutation_performed": False,
        "m56_started": False,
    }


def _as_list(value: Any) -> List[Any]:
    if isinstance(value, list):
        return value
    return []


def _as_str(value: Any) -> str:
    return value if isinstance(value, str) else ""


def _non_empty_str(value: Any) -> bool:
    return isinstance(value, str) and len(value.strip()) > 0


def _normalize_path(value: Any) -> str:
    if not isinstance(value, str):
        return ""
    return str(Path(value))


def _explain() -> str:
    return "\n".join(
        [
            "M55 active-task readiness CLI is read-only.",
            "The CLI does not write tasks/active-task.md.",
            "The CLI does not create approval records.",
            "The CLI does not authorize execution or M56.",
            "The CLI does not include a fixture mode.",
        ]
    )


def main() -> int:
    args = parse_args()

    if getattr(args, "unknown_args", []):
        known_forbidden = [flag for flag in args.unknown_args if flag in FORBIDDEN_FLAGS]
        blocker = "FORBIDDEN_FLAG" if known_forbidden else "INPUT_REQUIRED_FIELD_MISSING"
        message = "Forbidden flag provided." if known_forbidden else "Unknown argument provided."
        payload = block_result(blocker, message, args.input or "", args.proposal or "", args.queue_entry or "")
        if args.json:
            emit_json(payload)
        else:
            emit_human(payload)
        return EXIT_BY_RESULT[RESULT_BLOCKED]

    if any(flag in sys.argv for flag in FORBIDDEN_FLAGS):
        payload = block_result("FORBIDDEN_FLAG", "Forbidden flag provided.", args.input or "", args.proposal or "", args.queue_entry or "")
        if args.json:
            emit_json(payload)
        else:
            emit_human(payload)
        return EXIT_BY_RESULT[RESULT_BLOCKED]

    if args.explain:
        if args.input or args.proposal or args.queue_entry or args.repo_root or args.json:
            payload = block_result("FORBIDDEN_FLAG", "--explain must be standalone.", args.input or "", args.proposal or "", args.queue_entry or "")
            emit_human(payload)
            return EXIT_BY_RESULT[RESULT_BLOCKED]
        sys.stdout.write(_explain() + "\n")
        return 0

    if not (args.input and args.proposal and args.queue_entry and args.repo_root):
        payload = block_result("INPUT_REQUIRED_FIELD_MISSING", "Missing required arguments.", args.input or "", args.proposal or "", args.queue_entry or "")
        if args.json:
            emit_json(payload)
        else:
            emit_human(payload)
        return EXIT_BY_RESULT[RESULT_BLOCKED]

    err = validate_repo_root(args.repo_root)
    if err:
        payload = block_result(err, "Invalid --repo-root.", args.input, args.proposal, args.queue_entry)
        if args.json:
            emit_json(payload)
        else:
            emit_human(payload)
        return EXIT_BY_RESULT[RESULT_BLOCKED]

    repo_root = Path(args.repo_root).resolve()

    qpath, qerr = validate_queue_entry_path(repo_root, args.queue_entry)
    if qerr:
        payload = block_result(qerr, "Queue-entry path validation failed.", args.input, args.proposal, args.queue_entry)
        if args.json:
            emit_json(payload)
        else:
            emit_human(payload)
        return EXIT_BY_RESULT[RESULT_BLOCKED]

    up_err = load_required_upstream_files(repo_root)
    if up_err:
        payload = block_result(up_err, "Required upstream files are missing.", args.input, args.proposal, args.queue_entry)
        if args.json:
            emit_json(payload)
        else:
            emit_human(payload)
        return EXIT_BY_RESULT[RESULT_BLOCKED]

    _, intake_err = parse_intake_status(repo_root)
    if intake_err:
        payload = block_result(intake_err, "Intake status does not allow execution.", args.input, args.proposal, args.queue_entry)
        if args.json:
            emit_json(payload)
        else:
            emit_human(payload)
        return EXIT_BY_RESULT[RESULT_BLOCKED]

    input_payload, input_err = load_json_or_markdown_json(Path(args.input))
    if input_err:
        blocker = input_err if input_err in {"MISSING_JSON_BLOCK", "MULTIPLE_JSON_BLOCKS", "MALFORMED_JSON"} else "MALFORMED_JSON"
        payload = block_result(blocker, "Input parsing failed.", args.input, args.proposal, args.queue_entry)
        if args.json:
            emit_json(payload)
        else:
            emit_human(payload)
        return EXIT_BY_RESULT[RESULT_BLOCKED]

    proposal_payload, proposal_err = load_json_or_markdown_json(Path(args.proposal))
    if proposal_err:
        blocker = proposal_err if proposal_err in {"MISSING_JSON_BLOCK", "MULTIPLE_JSON_BLOCKS", "MALFORMED_JSON"} else "MALFORMED_JSON"
        payload = block_result(blocker, "Proposal parsing failed.", args.input, args.proposal, args.queue_entry)
        if args.json:
            emit_json(payload)
        else:
            emit_human(payload)
        return EXIT_BY_RESULT[RESULT_BLOCKED]

    if not isinstance(input_payload, dict) or "active_task_readiness_input" not in input_payload:
        payload = block_result("MISSING_ACTIVE_TASK_READINESS_INPUT_ROOT", "Input root is missing.", args.input, args.proposal, args.queue_entry)
        if args.json:
            emit_json(payload)
        else:
            emit_human(payload)
        return EXIT_BY_RESULT[RESULT_BLOCKED]

    if not isinstance(proposal_payload, dict) or "active_task_proposal" not in proposal_payload:
        payload = block_result("MISSING_ACTIVE_TASK_PROPOSAL_ROOT", "Proposal root is missing.", args.input, args.proposal, args.queue_entry)
        if args.json:
            emit_json(payload)
        else:
            emit_human(payload)
        return EXIT_BY_RESULT[RESULT_BLOCKED]

    input_obj = input_payload["active_task_readiness_input"]
    proposal_obj = proposal_payload["active_task_proposal"]

    in_err = validate_input_package(input_obj, args.queue_entry)
    if in_err:
        payload = block_result(in_err, "Input package validation failed.", args.input, args.proposal, args.queue_entry)
        if args.json:
            emit_json(payload)
        else:
            emit_human(payload)
        return EXIT_BY_RESULT[RESULT_BLOCKED]

    prop_err = validate_proposal_package(proposal_obj, args.queue_entry, args.input)
    if prop_err:
        payload = block_result(prop_err, "Proposal package validation failed.", args.input, args.proposal, args.queue_entry)
        if args.json:
            emit_json(payload)
        else:
            emit_human(payload)
        return EXIT_BY_RESULT[RESULT_BLOCKED]

    queue_text = qpath.read_text(encoding="utf-8")
    queue_err = validate_queue_entry_content(queue_text)
    if queue_err == "QUEUE_ENTRY_BOUNDARY_MARKERS_MISSING":
        payload = not_confirmed_result(queue_err, "Queue entry does not contain required boundary markers.", args.input, args.proposal, args.queue_entry)
        if args.json:
            emit_json(payload)
        else:
            emit_human(payload)
        return EXIT_BY_RESULT[RESULT_NOT_CONFIRMED]
    if queue_err:
        payload = block_result(queue_err, "Queue entry contains unsafe authority claims.", args.input, args.proposal, args.queue_entry)
        if args.json:
            emit_json(payload)
        else:
            emit_human(payload)
        return EXIT_BY_RESULT[RESULT_BLOCKED]

    tr_err = validate_traceability(input_obj, proposal_obj)
    if tr_err:
        payload = block_result(tr_err, "Traceability is incomplete.", args.input, args.proposal, args.queue_entry)
        if args.json:
            emit_json(payload)
        else:
            emit_human(payload)
        return EXIT_BY_RESULT[RESULT_BLOCKED]

    cf_err = validate_carry_forward(input_obj, proposal_obj)
    if cf_err:
        payload = block_result(cf_err, "Carry-forward is incomplete.", args.input, args.proposal, args.queue_entry)
        if args.json:
            emit_json(payload)
        else:
            emit_human(payload)
        return EXIT_BY_RESULT[RESULT_BLOCKED]

    nm_err = validate_non_authority_markers(input_obj, proposal_obj)
    if nm_err:
        payload = block_result(nm_err, "Non-authority markers are missing.", args.input, args.proposal, args.queue_entry)
        if args.json:
            emit_json(payload)
        else:
            emit_human(payload)
        return EXIT_BY_RESULT[RESULT_BLOCKED]

    ae_err = validate_no_authority_escalation(input_obj, proposal_obj)
    if ae_err:
        payload = block_result(ae_err, "Authority escalation detected.", args.input, args.proposal, args.queue_entry)
        if args.json:
            emit_json(payload)
        else:
            emit_human(payload)
        return EXIT_BY_RESULT[RESULT_BLOCKED]

    result_token = select_result(input_obj, proposal_obj)

    if result_token == RESULT_NOT_CONFIRMED:
        payload = not_confirmed_result(
            "PROPOSAL_STATUS_UNKNOWN",
            "Proposal is parseable but not reviewable for readiness confirmation.",
            args.input,
            args.proposal,
            args.queue_entry,
        )
        if args.json:
            emit_json(payload)
        else:
            emit_human(payload)
        return EXIT_BY_RESULT[RESULT_NOT_CONFIRMED]

    payload = confirmed_result(result_token, input_obj, proposal_obj, args.queue_entry)
    payload["active_task_readiness_result"]["source_active_task_readiness_input"] = args.input
    payload["active_task_readiness_result"]["source_active_task_proposal"] = args.proposal

    if args.json:
        emit_json(payload)
    else:
        emit_human(payload)
    return EXIT_BY_RESULT[result_token]


if __name__ == "__main__":
    sys.exit(main())
