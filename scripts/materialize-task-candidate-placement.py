#!/usr/bin/env python3
import argparse
import json
import re
import sys
from pathlib import Path

WRITE_CONFIRMATION_TOKEN = "QUEUE_PLACEMENT_WRITE_ALLOWED_BY_M54_POLICY"

DRY_RUN_ALLOWED = "M54_QUEUE_PLACEMENT_DRY_RUN_ALLOWED"
DRY_RUN_ALLOWED_WITH_LIMITATIONS = "M54_QUEUE_PLACEMENT_DRY_RUN_ALLOWED_WITH_LIMITATIONS"
DRY_RUN_NOT_ALLOWED = "M54_QUEUE_PLACEMENT_DRY_RUN_NOT_ALLOWED"
DRY_RUN_BLOCKED = "M54_QUEUE_PLACEMENT_DRY_RUN_BLOCKED"

RESULT_MATERIALIZED = "QUEUE_PLACEMENT_MATERIALIZED"
RESULT_MATERIALIZED_WITH_LIMITATIONS = "QUEUE_PLACEMENT_MATERIALIZED_WITH_LIMITATIONS"
RESULT_NOT_MATERIALIZED = "QUEUE_PLACEMENT_NOT_MATERIALIZED"
RESULT_BLOCKED = "QUEUE_PLACEMENT_BLOCKED"

NON_AUTHORITY_MARKERS = [
    "M54 CLI is not approval.",
    "M54 CLI does not authorize execution.",
    "M54 CLI does not replace active-task.md.",
    "M54 CLI does not create approval records.",
    "M54 CLI does not authorize M55.",
]

EXPLAIN_TEXT = """M54 CLI is not approval.
M54 CLI does not authorize execution.
M54 CLI does not replace active-task.md.
M54 CLI does not create approval records.
M54 CLI does not authorize M55.
M54 CLI performs controlled queue placement materialization checks.
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="M54 queue placement materialization CLI")
    parser.add_argument("--explain", action="store_true", help="Show CLI boundary explanation")
    parser.add_argument("--input", help="Path to input JSON or Markdown with one fenced JSON block")
    parser.add_argument("--target", help="Target queue path like tasks/queue/<safe-target-file>.md")
    parser.add_argument("--dry-run", action="store_true", help="Run checks without writing")
    parser.add_argument("--write", action="store_true", help="Write mode")
    parser.add_argument("--confirm-write", help="Required token for write mode")
    parser.add_argument("--repo-root", help="Repository root for safe path and evidence resolution")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    return parser.parse_args()


def emit_json(payload: dict) -> None:
    sys.stdout.write(json.dumps(payload, ensure_ascii=False) + "\n")


def dry_run_payload(result: str, exit_code: int, target: str, checked_input: str, blockers=None, warnings=None, carry_forward=None) -> dict:
    blockers = blockers or []
    warnings = warnings or []
    carry_forward = carry_forward or {
        "accepted_limitations": [],
        "warnings": [],
        "open_questions": [],
        "downstream_limits": [],
        "known_gaps": [],
        "non_authority_boundary": [],
    }
    would_materialize = result in {DRY_RUN_ALLOWED, DRY_RUN_ALLOWED_WITH_LIMITATIONS}
    return {
        "queue_placement_dry_run": {
            "result": result,
            "exit_code": exit_code,
            "would_materialize": would_materialize,
            "would_create_queue_entry": would_materialize,
            "target_queue_path": target,
            "checked_input": checked_input,
            "blockers": blockers,
            "warnings": warnings,
            "carry_forward": carry_forward,
            "boundary_flags": {
                "queue_materialization_only": True,
                "active_task_replacement_authorized": False,
                "execution_authorized": False,
                "approval_created": False,
                "m55_authorized": False,
            },
            "non_authority_markers": NON_AUTHORITY_MARKERS,
        }
    }


def output_blocked(json_mode: bool, target: str, checked_input: str, blockers, diagnostics: str) -> int:
    if json_mode:
        emit_json(dry_run_payload(DRY_RUN_BLOCKED, 2, target, checked_input, blockers=blockers))
    sys.stderr.write(diagnostics + "\n")
    return 2


def output_not_allowed(json_mode: bool, target: str, checked_input: str, blockers, warnings, carry_forward) -> int:
    if json_mode:
        emit_json(
            dry_run_payload(
                DRY_RUN_NOT_ALLOWED,
                1,
                target,
                checked_input,
                blockers=blockers,
                warnings=warnings,
                carry_forward=carry_forward,
            )
        )
    else:
        sys.stdout.write("NOT_ALLOWED\n")
        if blockers:
            sys.stderr.write("; ".join(blockers) + "\n")
    return 1


def output_allowed(json_mode: bool, with_limitations: bool, target: str, checked_input: str, warnings, carry_forward) -> int:
    token = DRY_RUN_ALLOWED_WITH_LIMITATIONS if with_limitations else DRY_RUN_ALLOWED
    if json_mode:
        emit_json(
            dry_run_payload(
                token,
                0,
                target,
                checked_input,
                blockers=[],
                warnings=warnings,
                carry_forward=carry_forward,
            )
        )
    else:
        sys.stdout.write(("ALLOWED_WITH_LIMITATIONS" if with_limitations else "ALLOWED") + "\n")
    return 0


def parse_frontmatter_value(text: str, key: str):
    m = re.search(rf"(?m)^\s*{re.escape(key)}\s*:\s*(\S+)\s*$", text)
    if m:
        return m.group(1).strip()

    lines = text.splitlines()
    for idx, line in enumerate(lines):
        if re.match(rf"^\s*{re.escape(key)}\s*:\s*$", line):
            base_indent = len(line) - len(line.lstrip(" "))
            for nxt in lines[idx + 1 :]:
                if not nxt.strip():
                    continue
                indent = len(nxt) - len(nxt.lstrip(" "))
                if indent <= base_indent:
                    break
                item = re.match(r"^\s*-\s*(\S+)\s*$", nxt)
                if item:
                    return item.group(1).strip()
    return None


def parse_input_payload(path: Path):
    text = path.read_text(encoding="utf-8")
    suffix = path.suffix.lower()

    if suffix == ".json":
        return json.loads(text)

    if suffix in {".md", ".markdown", ".txt"}:
        matches = re.findall(r"```\s*json\s*(.*?)\s*```", text, flags=re.DOTALL | re.IGNORECASE)
        if len(matches) != 1:
            raise ValueError("Machine-readable JSON input is required. YAML-only input is not supported in 54.6.")
        return json.loads(matches[0])

    raise ValueError("Machine-readable JSON input is required. YAML-only input is not supported in 54.6.")


def validate_target(repo_root: Path, target_raw: str):
    blockers = []
    rel_target = Path(target_raw)

    if rel_target.is_absolute():
        blockers.append("TARGET_QUEUE_PATH_UNSAFE")
        return None, blockers

    normalized = rel_target.as_posix()
    if ".." in rel_target.parts:
        blockers.append("TARGET_QUEUE_PATH_UNSAFE")
        return None, blockers

    if not normalized.startswith("tasks/queue/"):
        blockers.append("TARGET_QUEUE_PATH_UNSAFE")
        return None, blockers

    if normalized == "tasks/active-task.md":
        blockers.append("TARGET_QUEUE_PATH_UNSAFE")
        return None, blockers

    if not normalized.endswith(".md"):
        blockers.append("TARGET_QUEUE_PATH_UNSAFE")
        return None, blockers

    if normalized.startswith("approvals/") or normalized.startswith("reports/") or normalized.startswith("generated/"):
        blockers.append("TARGET_QUEUE_PATH_UNSAFE")
        return None, blockers

    resolved_root = repo_root.resolve()
    resolved_target = (resolved_root / rel_target).resolve()
    queue_root = (resolved_root / "tasks" / "queue").resolve()

    try:
        resolved_target.relative_to(resolved_root)
        resolved_target.relative_to(queue_root)
    except Exception:
        blockers.append("TARGET_QUEUE_PATH_UNSAFE")
        return None, blockers

    return resolved_target, blockers


def has_non_empty_entries(carry_forward: dict) -> bool:
    keys = ["accepted_limitations", "warnings", "open_questions", "downstream_limits", "known_gaps"]
    for key in keys:
        value = carry_forward.get(key)
        if isinstance(value, list) and len(value) > 0:
            return True
    return False


def candidate_already_queued(queue_dir: Path, candidate_id: str) -> bool:
    if not queue_dir.exists() or not queue_dir.is_dir():
        return False
    for p in queue_dir.glob("*.md"):
        try:
            content = p.read_text(encoding="utf-8")
        except Exception:
            continue
        if candidate_id and candidate_id in content:
            return True
    return False


def candidate_already_active(active_task_path: Path, candidate_id: str) -> bool:
    if not active_task_path.exists():
        return False
    try:
        content = active_task_path.read_text(encoding="utf-8")
    except Exception:
        return True
    return bool(candidate_id and candidate_id in content)


def approval_exists(approvals_dir: Path, candidate_id: str) -> bool:
    if not approvals_dir.exists() or not approvals_dir.is_dir():
        return False
    for p in approvals_dir.rglob("*"):
        if not p.is_file():
            continue
        try:
            content = p.read_text(encoding="utf-8")
        except Exception:
            continue
        if candidate_id and candidate_id in content:
            return True
    return False


def main() -> int:
    args = parse_args()

    used_other_with_explain = any(
        [
            args.input,
            args.target,
            args.dry_run,
            args.write,
            args.confirm_write,
            args.repo_root,
            args.json,
        ]
    )

    # mode conflict checks must run before explain success
    if args.explain and used_other_with_explain:
        return output_blocked(
            args.json,
            args.target or "",
            args.input or "",
            blockers=["MODE_CONFLICT"],
            diagnostics="BLOCKED: --explain must be standalone",
        )

    if args.dry_run and args.write:
        return output_blocked(
            args.json,
            args.target or "",
            args.input or "",
            blockers=["MODE_CONFLICT"],
            diagnostics="BLOCKED: --dry-run and --write are mutually exclusive",
        )

    if args.explain:
        sys.stdout.write(EXPLAIN_TEXT)
        return 0

    # confirmation validation before repository evidence checks
    if args.write and args.confirm_write != WRITE_CONFIRMATION_TOKEN:
        return output_blocked(
            args.json,
            args.target or "",
            args.input or "",
            blockers=["WRITE_CONFIRMATION_TOKEN_REQUIRED"],
            diagnostics="BLOCKED: missing or incorrect write confirmation token",
        )

    if args.repo_root:
        repo_root = Path(args.repo_root)
        if not repo_root.exists() or not repo_root.is_dir():
            return output_blocked(
                args.json,
                args.target or "",
                args.input or "",
                blockers=["REPO_ROOT_INVALID"],
                diagnostics="BLOCKED: missing or invalid --repo-root",
            )
    else:
        repo_root = Path.cwd()

    if not args.input or not args.target:
        return output_blocked(
            args.json,
            args.target or "",
            args.input or "",
            blockers=["MISSING_REQUIRED_ARGUMENTS"],
            diagnostics="BLOCKED: --input and --target are required",
        )

    mode_write = bool(args.write)

    target_resolved, target_blockers = validate_target(repo_root, args.target)
    if target_blockers:
        return output_blocked(
            args.json,
            args.target,
            args.input,
            blockers=target_blockers,
            diagnostics="BLOCKED: target path is unsafe",
        )

    input_path = Path(args.input)
    if not input_path.exists() or not input_path.is_file():
        return output_blocked(
            args.json,
            args.target,
            args.input,
            blockers=["INPUT_MISSING"],
            diagnostics="BLOCKED: input file missing",
        )

    try:
        raw = parse_input_payload(input_path)
    except Exception as exc:
        return output_blocked(
            args.json,
            args.target,
            args.input,
            blockers=["INPUT_PARSE_FAILED", "Machine-readable JSON input is required. YAML-only input is not supported in 54.6."],
            diagnostics=f"BLOCKED: input parse failed: {exc}",
        )

    input_data = None
    if isinstance(raw, dict):
        if "queue_placement_input" in raw and isinstance(raw["queue_placement_input"], dict):
            input_data = raw["queue_placement_input"]
        elif "task_candidate_queue_placement_input" in raw and isinstance(raw["task_candidate_queue_placement_input"], dict):
            input_data = raw["task_candidate_queue_placement_input"]

    if input_data is None:
        return output_blocked(
            args.json,
            args.target,
            args.input,
            blockers=["INPUT_ROOT_KEY_INVALID"],
            diagnostics="BLOCKED: missing queue_placement_input or task_candidate_queue_placement_input root",
        )

    blockers = []
    warnings = []

    intake_path = repo_root / "reports" / "m54-m53-readiness-intake.md"
    completion_path = repo_root / "reports" / "m53-completion-review.md"
    placement_result_path = repo_root / "reports" / "m53-placement-review-result-agent-action-review.json"

    if not intake_path.exists():
        blockers.append("M54_INTAKE_MISSING")
    else:
        intake_text = intake_path.read_text(encoding="utf-8")
        intake_status = parse_frontmatter_value(intake_text, "intake_status")
        if intake_status not in {"M54_INTAKE_READY", "M54_INTAKE_READY_WITH_LIMITATIONS"}:
            blockers.append("M54_INTAKE_NOT_READY")

    if not completion_path.exists():
        blockers.append("M53_COMPLETION_REVIEW_MISSING")
    else:
        completion_text = completion_path.read_text(encoding="utf-8")
        completion_status = parse_frontmatter_value(completion_text, "final_status")
        if completion_status not in {
            "M53_PLACEMENT_REVIEW_LAYER_COMPLETE",
            "M53_PLACEMENT_REVIEW_LAYER_COMPLETE_WITH_LIMITATIONS",
        }:
            blockers.append("M53_COMPLETION_STATUS_BLOCKING")

    placement_result = None
    if not placement_result_path.exists():
        blockers.append("M53_PLACEMENT_RESULT_MISSING")
    else:
        try:
            placement_raw = json.loads(placement_result_path.read_text(encoding="utf-8"))
            placement_result = placement_raw.get("placement_review_result", {})
        except Exception:
            blockers.append("M53_PLACEMENT_RESULT_MALFORMED")

    if placement_result is not None:
        if placement_result.get("result") not in {"PLACEMENT_REVIEW_ELIGIBLE", "PLACEMENT_REVIEW_ELIGIBLE_WITH_LIMITATIONS"}:
            blockers.append("M53_PLACEMENT_RESULT_NOT_ELIGIBLE")

        expected_truths = {
            "eligible_for_downstream_placement": True,
            "eligible_as_m54_active_task_proposal_input": False,
            "m54_materialization_authorized": False,
            "queue_placement_performed": False,
            "active_task_replacement_performed": False,
            "approval_created": False,
        }
        for k, v in expected_truths.items():
            if placement_result.get(k) is not v:
                blockers.append(f"M53_PLACEMENT_FIELD_UNSAFE:{k}")

    if input_data.get("placement_kind") != "queue_materialization":
        blockers.append("INPUT_PLACEMENT_KIND_INVALID")

    expected_input_flags = {
        "queue_materialization_requested": True,
        "active_task_replacement_requested": False,
        "approval_requested": False,
        "execution_requested": False,
        "m55_requested": False,
    }
    for k, v in expected_input_flags.items():
        if input_data.get(k) is not v:
            blockers.append(f"INPUT_FLAG_UNSAFE:{k}")

    boundary_flags = input_data.get("boundary_flags")
    if not isinstance(boundary_flags, dict):
        blockers.append("INPUT_BOUNDARY_FLAGS_MISSING")
    else:
        expected_boundaries = {
            "queue_materialization_authorized_by_input": False,
            "active_task_replacement_authorized": False,
            "execution_authorized": False,
            "approval_created": False,
            "m55_authorized": False,
        }
        for k, v in expected_boundaries.items():
            if boundary_flags.get(k) is not v:
                blockers.append(f"INPUT_BOUNDARY_FLAG_UNSAFE:{k}")

    source_traceability = input_data.get("source_traceability")
    trace_keys = [
        "source_proposal",
        "source_authorization",
        "source_conversion_package",
        "source_generated_artifact",
        "m50_traceability",
        "m51_generator_evidence",
        "m52_validation_evidence",
        "m53_placement_review_evidence",
        "m54_materialization_evidence",
    ]
    if not isinstance(source_traceability, dict) or not all(source_traceability.get(k) for k in trace_keys):
        blockers.append("SOURCE_TRACEABILITY_INCOMPLETE")

    carry_forward = input_data.get("carry_forward")
    carry_keys = [
        "accepted_limitations",
        "warnings",
        "open_questions",
        "downstream_limits",
        "known_gaps",
        "non_authority_boundary",
    ]
    if not isinstance(carry_forward, dict):
        blockers.append("CARRY_FORWARD_MISSING")
        carry_forward = {
            "accepted_limitations": [],
            "warnings": [],
            "open_questions": [],
            "downstream_limits": [],
            "known_gaps": [],
            "non_authority_boundary": [],
        }
    else:
        for k in carry_keys:
            if k not in carry_forward or not isinstance(carry_forward.get(k), list):
                blockers.append(f"CARRY_FORWARD_FIELD_MISSING:{k}")

    queue_parent = (repo_root / "tasks" / "queue").resolve()
    if not queue_parent.exists() or not queue_parent.is_dir():
        blockers.append("QUEUE_PARENT_DIR_MISSING")

    if target_resolved.exists():
        blockers.append("TARGET_FILE_ALREADY_EXISTS")

    candidate_id = str(input_data.get("source_candidate_id") or "")
    try:
        if candidate_already_queued(queue_parent, candidate_id):
            blockers.append("CANDIDATE_ALREADY_QUEUED")
    except Exception:
        blockers.append("REPOSITORY_STATE_READ_FAILED")

    try:
        if candidate_already_active((repo_root / "tasks" / "active-task.md").resolve(), candidate_id):
            blockers.append("CANDIDATE_ALREADY_ACTIVE")
    except Exception:
        blockers.append("REPOSITORY_STATE_READ_FAILED")

    try:
        if approval_exists((repo_root / "approvals").resolve(), candidate_id):
            blockers.append("APPROVAL_ALREADY_EXISTS")
    except Exception:
        blockers.append("REPOSITORY_STATE_READ_FAILED")

    if blockers:
        return output_blocked(
            args.json,
            args.target,
            args.input,
            blockers=blockers,
            diagnostics="BLOCKED: pre-materialization checks failed",
        )

    has_limits = has_non_empty_entries(carry_forward)
    if has_limits:
        warnings.append("CARRY_FORWARD_LIMITATIONS_PRESENT")

    if not mode_write:
        return output_allowed(args.json, has_limits, args.target, args.input, warnings, carry_forward)

    # write mode: exclusive create only ("x" means exclusive)
    artifact_payload = {
        "queue_placement_artifact": {
            "task_id": target_resolved.stem,
            "queue_status": "QUEUED_CANDIDATE",
            "source_candidate_id": candidate_id,
            "source_m53_completion_review": "reports/m53-completion-review.md",
            "source_m53_placement_result": "reports/m53-placement-review-result-agent-action-review.json",
            "source_m52_validation_result": str(input_data.get("source_m52_validation_result", "")),
            "source_generated_candidate": str(input_data.get("source_generated_candidate", "")),
            "placement_created_by": "M54",
            "placement_created_at": "1970-01-01T00:00:00Z",
            "placement_authority": "QUEUE_PLACEMENT_ONLY",
            "approval_status": "NOT_APPROVED",
            "execution_status": "NOT_STARTED",
            "active_task_status": "NOT_ACTIVE",
            "required_traceability": source_traceability,
            "carry_forward": carry_forward,
            "boundaries": {
                "queue_entry_created": True,
                "active_task_replacement_performed": False,
                "execution_authorized": False,
                "approval_created": False,
                "lifecycle_active_transition_performed": False,
                "m55_start_authorized": False,
            },
        }
    }

    try:
        with target_resolved.open("x", encoding="utf-8") as f:
            f.write(json.dumps(artifact_payload, indent=2, ensure_ascii=False) + "\n")
    except FileExistsError:
        return output_blocked(
            args.json,
            args.target,
            args.input,
            blockers=["TARGET_FILE_ALREADY_EXISTS"],
            diagnostics="BLOCKED: target file already exists",
        )

    result_payload = {
        "queue_placement_result": {
            "result": RESULT_MATERIALIZED_WITH_LIMITATIONS if has_limits else RESULT_MATERIALIZED,
            "exit_code": 0,
            "materialized": True,
            "queue_entry_created": True,
            "queue_entry_path": args.target,
            "checked_candidate_id": candidate_id,
            "source_m53_completion_review": "reports/m53-completion-review.md",
            "source_m53_placement_result": "reports/m53-placement-review-result-agent-action-review.json",
            "source_m52_validation_result": str(input_data.get("source_m52_validation_result", "")),
            "source_generated_candidate": str(input_data.get("source_generated_candidate", "")),
            "source_traceability": source_traceability,
            "carry_forward": carry_forward,
            "materialization_findings": [],
            "warnings": warnings,
            "blockers": [],
            "boundary_flags": {
                "queue_materialization_only": True,
                "active_task_write_allowed": False,
                "execution_authorized": False,
                "approval_record_creation_allowed": False,
                "lifecycle_active_transition_allowed": False,
                "m55_start_authorized": False,
            },
            "performed_actions": {
                "queue_entry_created": True,
                "active_task_replacement_performed": False,
                "approval_created": False,
                "execution_started": False,
                "m55_started": False,
            },
            "non_authority_markers": [
                "Queue placement is not approval.",
                "Queue placement is not execution.",
                "Queue placement is not active-task replacement.",
                "Queue placement is not M55 authorization.",
            ],
        }
    }

    if args.json:
        emit_json(result_payload)
    else:
        sys.stdout.write((RESULT_MATERIALIZED_WITH_LIMITATIONS if has_limits else RESULT_MATERIALIZED) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
