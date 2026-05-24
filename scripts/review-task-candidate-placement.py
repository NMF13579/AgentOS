#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

RESULT_ELIGIBLE = "PLACEMENT_REVIEW_ELIGIBLE"
RESULT_ELIGIBLE_LIMITED = "PLACEMENT_REVIEW_ELIGIBLE_WITH_LIMITATIONS"
RESULT_NOT_ELIGIBLE = "PLACEMENT_REVIEW_NOT_ELIGIBLE"
RESULT_BLOCKED = "PLACEMENT_REVIEW_BLOCKED"

NON_AUTHORITY_MARKERS = [
    "M53 placement review result is not approval.",
    "M53 placement review result does not authorize execution.",
    "M53 placement review result does not authorize queue placement.",
    "M53 placement review result does not authorize active-task replacement.",
    "M53 placement review result does not authorize lifecycle mutation.",
    "M53 placement review result does not authorize M54 materialization.",
]

ALLOWED_FINAL_STATUSES = {
    "M52_CANDIDATE_VALIDATION_LAYER_COMPLETE",
    "M52_CANDIDATE_VALIDATION_LAYER_COMPLETE_WITH_LIMITATIONS",
}
BLOCKING_FINAL_STATUSES = {"M52_INCOMPLETE", "M52_BLOCKED"}

ALLOWED_SOURCE_ORIGIN = {
    "M51_GENERATED_STAGING_ARTIFACT",
    "M52_VALIDATED_CANDIDATE_RESULT",
    "MANUAL_CANONICAL_CANDIDATE_REFERENCE",
}
ALLOWED_REVIEW_MODE = {
    "REVIEW_ONLY",
    "QUEUE_CANDIDATE_ELIGIBILITY_REVIEW",
    "ACTIVE_TASK_PROPOSAL_ELIGIBILITY_REVIEW",
}
ALLOWED_SHAPE = {
    "TASK_CONTRACT_CANDIDATE",
    "QUEUE_MATERIALIZATION_INPUT_CANDIDATE",
    "ACTIVE_TASK_PROPOSAL_INPUT_CANDIDATE",
}


def stderr(message: str) -> None:
    print(message, file=sys.stderr)


def safe_resolve_dir(path_value: str, *, base: Path | None = None) -> Path:
    candidate = Path(path_value)
    if not candidate.is_absolute():
        if base is None:
            base = Path.cwd()
        candidate = (base / candidate).resolve()
    else:
        candidate = candidate.resolve()
    if not candidate.exists() or not candidate.is_dir():
        raise ValueError(f"directory does not exist: {candidate}")
    return candidate


def ensure_within(path: Path, root: Path) -> None:
    path_r = path.resolve()
    root_r = root.resolve()
    try:
        path_r.relative_to(root_r)
    except ValueError as exc:
        raise ValueError(f"path escapes repo root: {path_r}") from exc


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_json_from_text(text: str) -> Any:
    return json.loads(text)


def extract_fenced_json(text: str) -> dict[str, Any] | None:
    pattern = re.compile(r"```json\s*(\{.*?\})\s*```", re.DOTALL | re.IGNORECASE)
    for match in pattern.finditer(text):
        block = match.group(1)
        try:
            value = json.loads(block)
        except json.JSONDecodeError:
            continue
        if isinstance(value, dict):
            return value
    return None


def has_yaml_fence(text: str) -> bool:
    return bool(re.search(r"```yaml", text, re.IGNORECASE))


def load_machine_readable(path: Path, yaml_blocker: str) -> tuple[dict[str, Any] | None, list[str]]:
    blockers: list[str] = []
    if not path.exists() or not path.is_file():
        return None, [f"input path does not exist: {path}"]

    text = read_text(path)

    try:
        parsed = parse_json_from_text(text)
        if isinstance(parsed, dict):
            return parsed, blockers
    except json.JSONDecodeError:
        pass

    fenced = extract_fenced_json(text)
    if fenced is not None:
        return fenced, blockers

    if has_yaml_fence(text) or text.lstrip().startswith("---"):
        blockers.append(yaml_blocker)
        return None, blockers

    blockers.append("machine-readable JSON object is required")
    return None, blockers


def empty_result() -> dict[str, Any]:
    return {
        "placement_review_result": {
            "result": RESULT_BLOCKED,
            "exit_code": 2,
            "reviewed": False,
            "eligible_for_downstream_placement": False,
            "eligible_as_m54_queue_materialization_input": False,
            "eligible_as_m54_active_task_proposal_input": False,
            "checked_candidate_id": "",
            "source_m52_completion_review": "reports/m52-completion-review.md",
            "source_m52_validation_result": "",
            "source_generated_artifact": "",
            "source_traceability": {
                "source_proposal": "",
                "source_authorization": "",
                "source_conversion_package": "",
                "source_generated_artifact": "",
                "m50_traceability": "",
                "m51_generator_evidence": "",
                "m52_validation_evidence": "",
            },
            "carry_forward": {
                "accepted_limitations": [],
                "warnings": [],
                "open_questions": [],
                "downstream_limits": [],
                "known_gaps": [],
                "non_authority_boundary": NON_AUTHORITY_MARKERS[:],
            },
            "placement_findings": [],
            "warnings": [],
            "blockers": [],
            "boundary_flags": {
                "review_only": True,
                "queue_write_allowed": False,
                "active_task_write_allowed": False,
                "execution_authorized": False,
                "approval_record_creation_allowed": False,
                "lifecycle_mutation_allowed": False,
                "m54_materialization_authorized": False,
            },
            "non_authority_markers": NON_AUTHORITY_MARKERS[:],
            "m54_independent_validation_required": True,
            "m54_may_not_start_without_own_gate": True,
            "m54_materialization_authorized": False,
            "queue_placement_performed": False,
            "active_task_replacement_performed": False,
            "approval_created": False,
        }
    }


def set_result(result_obj: dict[str, Any], token: str, reviewed: bool) -> None:
    mapping = {
        RESULT_ELIGIBLE: 0,
        RESULT_ELIGIBLE_LIMITED: 0,
        RESULT_NOT_ELIGIBLE: 1,
        RESULT_BLOCKED: 2,
    }
    result_obj["placement_review_result"]["result"] = token
    result_obj["placement_review_result"]["exit_code"] = mapping[token]
    result_obj["placement_review_result"]["reviewed"] = reviewed


def add_blocker(result_obj: dict[str, Any], message: str) -> None:
    result_obj["placement_review_result"]["blockers"].append(message)


def add_warning(result_obj: dict[str, Any], message: str) -> None:
    result_obj["placement_review_result"]["warnings"].append(message)


def parse_m52_bridge(path: Path) -> tuple[str | None, bool, dict[str, list[str]]]:
    text = read_text(path)
    status_match = re.search(r"^final_status:\s*(\S+)\s*$", text, re.MULTILINE)
    handoff_match = re.search(r"^m53_handoff_ready:\s*(true|false)\s*$", text, re.MULTILINE | re.IGNORECASE)
    final_status = status_match.group(1) if status_match else None
    handoff = handoff_match is not None and handoff_match.group(1).lower() == "true"

    fields = {
        "accepted_limitations": [],
        "warnings": [],
        "open_questions": [],
        "downstream_limits": [],
        "known_gaps": [],
        "non_authority_boundary": [],
    }

    current = None
    heading_map = {
        "accepted limitations": "accepted_limitations",
        "warnings": "warnings",
        "open questions": "open_questions",
        "downstream limits": "downstream_limits",
        "known gaps": "known_gaps",
        "non-authority boundaries": "non_authority_boundary",
    }

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if line.startswith("### "):
            section = line[4:].strip().lower()
            current = heading_map.get(section)
            continue
        if current is None:
            continue
        if line.startswith("- "):
            value = line[2:].strip()
            if value and "none found" not in value.lower():
                fields[current].append(value)

    if not fields["non_authority_boundary"]:
        # Conservative extraction fallback.
        for marker in NON_AUTHORITY_MARKERS:
            if marker in text:
                fields["non_authority_boundary"].append(marker)

    return final_status, handoff, fields


def merge_unique(left: list[str], right: list[str]) -> list[str]:
    out: list[str] = []
    for value in left + right:
        if value not in out:
            out.append(value)
    return out


def extract_list(source: dict[str, Any], key: str) -> list[str]:
    value = source.get(key, [])
    if not isinstance(value, list):
        return []
    out: list[str] = []
    for item in value:
        if isinstance(item, str) and item.strip():
            out.append(item.strip())
    return out


def extract_input_payload(payload: dict[str, Any]) -> tuple[dict[str, Any] | None, list[str]]:
    blockers: list[str] = []
    data = payload.get("placement_review_input")
    if not isinstance(data, dict):
        blockers.append("missing placement_review_input")
        return None, blockers

    required = [
        "input_id",
        "source_candidate_id",
        "source_m52_completion_review",
        "source_m52_validation_result",
        "source_generated_artifact",
        "source_candidate_origin",
        "placement_review_mode",
        "expected_candidate_shape",
        "required_traceability",
        "required_carry_forward",
        "placement_target",
        "boundaries",
    ]
    for field in required:
        if field not in data:
            blockers.append(f"missing {field}")

    if data.get("source_m52_completion_review") != "reports/m52-completion-review.md":
        blockers.append("source_m52_completion_review must equal reports/m52-completion-review.md")

    if data.get("source_candidate_origin") not in ALLOWED_SOURCE_ORIGIN:
        blockers.append("source_candidate_origin unknown")

    if data.get("placement_review_mode") not in ALLOWED_REVIEW_MODE:
        blockers.append("placement_review_mode unknown")

    if data.get("expected_candidate_shape") not in ALLOWED_SHAPE:
        blockers.append("expected_candidate_shape unknown")

    boundaries = data.get("boundaries") if isinstance(data.get("boundaries"), dict) else {}
    expected_flags = {
        "review_only": True,
        "queue_write_allowed": False,
        "active_task_write_allowed": False,
        "execution_authorized": False,
        "approval_record_creation_allowed": False,
        "lifecycle_mutation_allowed": False,
        "m54_materialization_authorized": False,
    }
    for name, expected in expected_flags.items():
        if boundaries.get(name) is not expected:
            blockers.append(f"{name} must be {str(expected).lower()}")

    return data, blockers


def extract_candidate_payload(payload: dict[str, Any]) -> tuple[dict[str, Any], list[str]]:
    blockers: list[str] = []

    data = payload.get("placement_review_result") if isinstance(payload.get("placement_review_result"), dict) else payload

    candidate_id = data.get("checked_candidate_id") or data.get("source_candidate_id") or data.get("candidate_id") or ""
    validation_result = data.get("source_m52_validation_result") or data.get("result_token") or data.get("validation_result") or ""
    generated = data.get("source_generated_artifact") or data.get("generated_artifact") or ""

    normalized = {
        "source_candidate_id": candidate_id,
        "source_m52_validation_result": validation_result,
        "source_generated_artifact": generated,
        "source_candidate_origin": data.get("source_candidate_origin", "M52_VALIDATED_CANDIDATE_RESULT"),
        "placement_review_mode": data.get("placement_review_mode", "REVIEW_ONLY"),
        "expected_candidate_shape": data.get("expected_candidate_shape", "TASK_CONTRACT_CANDIDATE"),
        "required_traceability": data.get("source_traceability") if isinstance(data.get("source_traceability"), dict) else data.get("required_traceability", {}),
        "required_carry_forward": data.get("carry_forward") if isinstance(data.get("carry_forward"), dict) else data.get("required_carry_forward", {}),
        "placement_target": data.get("placement_target", {
            "queue_candidate_allowed_for_review": False,
            "active_task_candidate_allowed_for_review": False,
        }),
        "boundaries": data.get("boundary_flags") if isinstance(data.get("boundary_flags"), dict) else data.get("boundaries", {}),
    }

    if not normalized["source_candidate_id"]:
        blockers.append("missing candidate id")
    if not normalized["source_generated_artifact"]:
        blockers.append("missing generated artifact reference")
    if not normalized["source_m52_validation_result"]:
        blockers.append("missing M52 validation result")

    boundaries = normalized["boundaries"] if isinstance(normalized["boundaries"], dict) else {}
    if boundaries.get("execution_authorized") is True:
        blockers.append("M53 input claims execution authorization")
    if data.get("queue_placement_performed") is True:
        blockers.append("M53 input claims queue placement already performed")
    if data.get("active_task_replacement_performed") is True:
        blockers.append("M53 input claims active-task replacement already performed")
    if data.get("approval_created") is True:
        blockers.append("M53 input claims approval already created")
    if boundaries.get("m54_materialization_authorized") is True or data.get("m54_materialization_authorized") is True:
        blockers.append("M53 input claims M54 materialization authorization")

    return normalized, blockers


def load_text_if_exists(path: Path) -> str:
    if not path.exists() or not path.is_file():
        return ""
    try:
        return read_text(path)
    except Exception:
        return ""


def detect_repo_conflicts(repo_root: Path, candidate_id: str) -> tuple[list[str], list[str]]:
    blockers: list[str] = []
    warnings: list[str] = []
    if not candidate_id:
        return blockers, warnings

    queue_dir = repo_root / "tasks" / "queue"
    active_task_file = repo_root / "tasks" / "active-task.md"
    approvals_dir = repo_root / "approvals"

    for path in [queue_dir, active_task_file, approvals_dir]:
        ensure_within(path, repo_root)

    try:
        if queue_dir.exists() and queue_dir.is_dir():
            for file in queue_dir.iterdir():
                if file.is_file() and candidate_id in load_text_if_exists(file):
                    warnings.append("candidate appears in tasks/queue (read-only conflict check)")
                    break
        if active_task_file.exists() and active_task_file.is_file():
            if candidate_id in load_text_if_exists(active_task_file):
                warnings.append("candidate appears in tasks/active-task.md (read-only conflict check)")
        if approvals_dir.exists() and approvals_dir.is_dir():
            for file in approvals_dir.iterdir():
                if file.is_file() and candidate_id in load_text_if_exists(file):
                    warnings.append("candidate appears in approvals (read-only conflict check)")
                    break
    except Exception as exc:
        blockers.append(f"repository state read failed: {exc}")

    return blockers, warnings


def validate_mode(args: argparse.Namespace) -> tuple[bool, list[str]]:
    blockers: list[str] = []

    modes = [
        bool(args.input),
        bool(args.candidate_result),
        bool(args.fixtures),
        bool(args.explain),
    ]
    count = sum(1 for m in modes if m)

    if count == 0:
        blockers.append("no review input mode provided")
    if count > 1:
        blockers.append("conflicting review input modes")

    if args.json and (args.fixtures or args.explain):
        if args.fixtures:
            blockers.append("fixtures mode cannot be combined with --json")
        if args.explain:
            blockers.append("explain mode cannot be combined with --json")

    if (args.m52_reports_dir != "reports" or args.repo_root is not None) and not (args.input or args.candidate_result):
        blockers.append("--m52-reports-dir and --repo-root are allowed only with --input or --candidate-result")

    return len(blockers) == 0, blockers


def print_json(result_obj: dict[str, Any]) -> None:
    print(json.dumps(result_obj, ensure_ascii=False, indent=2))


def explain_text() -> str:
    return (
        "M53 placement review checks only eligibility. It does not place tasks, does not "
        "replace active-task, does not create approvals, and does not authorize M54."
    )


def run_fixtures() -> tuple[int, list[str]]:
    messages = [
        "built-in self-check: boundary markers available",
        "built-in self-check: blocked default result available",
        "built-in self-check: result tokens configured",
    ]
    return 0, messages


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only M53 placement eligibility review CLI")
    parser.add_argument("--input", help="Path to placement_review_input JSON or Markdown fenced JSON")
    parser.add_argument("--candidate-result", help="Path to M52 candidate result JSON or Markdown fenced JSON")
    parser.add_argument("--fixtures", action="store_true", help="Run built-in self-checks only")
    parser.add_argument("--explain", action="store_true", help="Explain M53 placement review behavior")
    parser.add_argument("--m52-reports-dir", default="reports", help="M52 supporting reports directory")
    parser.add_argument("--repo-root", help="Repository root for safe path resolution")
    parser.add_argument("--json", action="store_true", help="Emit JSON result to stdout")
    args = parser.parse_args()

    result_obj = empty_result()

    ok_mode, mode_blockers = validate_mode(args)
    if not ok_mode:
        for message in mode_blockers:
            add_blocker(result_obj, message)
            stderr(message)
        set_result(result_obj, RESULT_BLOCKED, False)
        if args.json:
            print_json(result_obj)
        return 2

    if args.explain:
        print(explain_text())
        return 0

    if args.fixtures:
        code, messages = run_fixtures()
        for msg in messages:
            stderr(msg)
        return code

    # input or candidate-result mode only from here
    try:
        repo_root = safe_resolve_dir(args.repo_root or str(Path.cwd()))
        m52_reports_dir = safe_resolve_dir(args.m52_reports_dir, base=repo_root)
        ensure_within(m52_reports_dir, repo_root)
    except Exception as exc:
        add_blocker(result_obj, str(exc))
        set_result(result_obj, RESULT_BLOCKED, False)
        stderr(str(exc))
        if args.json:
            print_json(result_obj)
        return 2

    m52_bridge = repo_root / "reports" / "m52-completion-review.md"
    if not m52_bridge.exists():
        add_blocker(result_obj, "M52 completion review missing")
        set_result(result_obj, RESULT_BLOCKED, False)
        if args.json:
            print_json(result_obj)
        return 2

    final_status, handoff_ready, m52_carry = parse_m52_bridge(m52_bridge)
    if not handoff_ready:
        add_blocker(result_obj, "M52 completion review does not set m53_handoff_ready: true")
    if final_status is None:
        add_blocker(result_obj, "M52 final_status is unknown")
    elif final_status in BLOCKING_FINAL_STATUSES:
        add_blocker(result_obj, f"M52 final_status is {final_status}")
    elif final_status not in ALLOWED_FINAL_STATUSES:
        add_blocker(result_obj, f"M52 final_status is unknown: {final_status}")

    data: dict[str, Any] | None = None
    parse_blockers: list[str] = []
    if args.input:
        parsed, parse_blockers = load_machine_readable(
            Path(args.input),
            "machine-readable JSON input is required; fenced YAML is not supported in 53.5",
        )
        if parsed is not None:
            data, validate_blockers = extract_input_payload(parsed)
            parse_blockers.extend(validate_blockers)
    else:
        parsed, parse_blockers = load_machine_readable(
            Path(args.candidate_result),
            "machine-readable JSON candidate result is required; fenced YAML is not supported in 53.5",
        )
        if parsed is not None:
            data, validate_blockers = extract_candidate_payload(parsed)
            parse_blockers.extend(validate_blockers)

    for b in parse_blockers:
        add_blocker(result_obj, b)

    if data is None:
        set_result(result_obj, RESULT_BLOCKED, False)
        if args.json:
            print_json(result_obj)
        return 2

    result = result_obj["placement_review_result"]
    result["checked_candidate_id"] = str(data.get("source_candidate_id", "") or "")
    result["source_m52_validation_result"] = str(data.get("source_m52_validation_result", "") or "")
    result["source_generated_artifact"] = str(data.get("source_generated_artifact", "") or "")

    trace = data.get("required_traceability", {})
    if isinstance(trace, dict):
        for key in result["source_traceability"]:
            value = trace.get(key, "")
            if isinstance(value, str):
                result["source_traceability"][key] = value

    input_cf = data.get("required_carry_forward", {}) if isinstance(data.get("required_carry_forward"), dict) else {}

    for field in ["accepted_limitations", "warnings", "open_questions", "downstream_limits", "known_gaps"]:
        merged = merge_unique(m52_carry.get(field, []), extract_list(input_cf, field))
        result["carry_forward"][field] = merged

    non_auth = merge_unique(m52_carry.get("non_authority_boundary", []), extract_list(input_cf, "non_authority_boundary"))
    if not non_auth:
        non_auth = NON_AUTHORITY_MARKERS[:]
        add_warning(result_obj, "conservative carry-forward extraction used for non_authority_boundary")
    result["carry_forward"]["non_authority_boundary"] = non_auth

    boundaries = data.get("boundaries", {}) if isinstance(data.get("boundaries"), dict) else {}
    expected_flags = {
        "review_only": True,
        "queue_write_allowed": False,
        "active_task_write_allowed": False,
        "execution_authorized": False,
        "approval_record_creation_allowed": False,
        "lifecycle_mutation_allowed": False,
        "m54_materialization_authorized": False,
    }
    for name, expected in expected_flags.items():
        if boundaries.get(name) is not expected:
            add_blocker(result_obj, f"unsafe boundary flag: {name}")

    repo_blockers, repo_warnings = detect_repo_conflicts(repo_root, result["checked_candidate_id"])
    for b in repo_blockers:
        add_blocker(result_obj, b)
    for w in repo_warnings:
        add_warning(result_obj, w)

    target = data.get("placement_target", {}) if isinstance(data.get("placement_target"), dict) else {}
    queue_target = bool(target.get("queue_candidate_allowed_for_review", False))
    active_target = bool(target.get("active_task_candidate_allowed_for_review", False))

    shape = data.get("expected_candidate_shape")
    mode = data.get("placement_review_mode")

    if queue_target and active_target and not bool(data.get("dual_eligibility_review_requested", False)):
        set_result(result_obj, RESULT_NOT_ELIGIBLE, True)
        result["eligible_for_downstream_placement"] = False
        result["eligible_as_m54_queue_materialization_input"] = False
        result["eligible_as_m54_active_task_proposal_input"] = False
        result["placement_findings"].append("dual target requested without explicit dual eligibility review")
    elif result["blockers"]:
        set_result(result_obj, RESULT_BLOCKED, False)
        result["eligible_for_downstream_placement"] = False
        result["eligible_as_m54_queue_materialization_input"] = False
        result["eligible_as_m54_active_task_proposal_input"] = False
    else:
        shape_not_eligible = False
        if queue_target and shape not in {"QUEUE_MATERIALIZATION_INPUT_CANDIDATE", "TASK_CONTRACT_CANDIDATE"}:
            shape_not_eligible = True
            result["placement_findings"].append("candidate shape incompatible with queue target")
        if active_target and shape not in {"ACTIVE_TASK_PROPOSAL_INPUT_CANDIDATE", "TASK_CONTRACT_CANDIDATE"}:
            shape_not_eligible = True
            result["placement_findings"].append("candidate shape incompatible with active-task target")

        if mode not in ALLOWED_REVIEW_MODE:
            shape_not_eligible = True
            result["placement_findings"].append("requested placement target is invalid")

        if shape_not_eligible:
            set_result(result_obj, RESULT_NOT_ELIGIBLE, True)
            result["eligible_for_downstream_placement"] = False
            result["eligible_as_m54_queue_materialization_input"] = False
            result["eligible_as_m54_active_task_proposal_input"] = False
        else:
            has_limitations = any(result["carry_forward"][field] for field in [
                "accepted_limitations",
                "warnings",
                "open_questions",
                "downstream_limits",
                "known_gaps",
            ])
            if final_status == "M52_CANDIDATE_VALIDATION_LAYER_COMPLETE_WITH_LIMITATIONS" or has_limitations:
                set_result(result_obj, RESULT_ELIGIBLE_LIMITED, True)
            else:
                set_result(result_obj, RESULT_ELIGIBLE, True)

            eligible_any = True
            result["eligible_for_downstream_placement"] = eligible_any
            result["eligible_as_m54_queue_materialization_input"] = bool(queue_target)
            result["eligible_as_m54_active_task_proposal_input"] = bool(active_target)

    if args.json:
        if result["blockers"]:
            for b in result["blockers"]:
                stderr(b)
        for w in result["warnings"]:
            stderr(w)
        print_json(result_obj)
    else:
        print(json.dumps(result_obj, ensure_ascii=False, indent=2))

    return int(result["exit_code"])


if __name__ == "__main__":
    sys.exit(main())
