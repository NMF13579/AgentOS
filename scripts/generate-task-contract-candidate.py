#!/usr/bin/env python3
import argparse
import json
import re
import sys
from pathlib import Path

RESULT_DRY_RUN_OK = "TASK_CONTRACT_CANDIDATE_GENERATION_DRY_RUN_OK"
RESULT_WRITE_OK = "TASK_CONTRACT_CANDIDATE_GENERATION_WRITE_OK"
RESULT_FAILED = "TASK_CONTRACT_CANDIDATE_GENERATION_FAILED"
RESULT_BLOCKED = "TASK_CONTRACT_CANDIDATE_GENERATION_BLOCKED"

EXIT_CODES = {
    RESULT_DRY_RUN_OK: 0,
    RESULT_WRITE_OK: 0,
    RESULT_FAILED: 1,
    RESULT_BLOCKED: 2,
}

NON_AUTHORITY_MARKERS = [
    "GENERATOR_DOES_NOT_AUTHORIZE_EXECUTION",
    "GENERATOR_DOES_NOT_PLACE_TASK_IN_QUEUE",
    "GENERATOR_DOES_NOT_MODIFY_ACTIVE_TASK",
    "GENERATOR_DOES_NOT_CREATE_APPROVAL_RECORDS",
    "GENERATOR_OUTPUT_REQUIRES_LATER_PLACEMENT_GATE",
    "GENERATOR_PASS_IS_NOT_APPROVAL",
    "GENERATOR_PASS_IS_NOT_EXECUTION_PERMISSION",
    "GENERATOR_PASS_IS_NOT_QUEUE_PLACEMENT",
    "GENERATOR_PASS_IS_NOT_ACTIVE_TASK_REPLACEMENT",
    "GENERATOR_PASS_IS_NOT_IMPLEMENTATION_AUTHORIZATION",
]

REQUIRED_KEYS = [
    "generator_input:",
    "input_id:",
    "generator_input_status:",
    "source_conversion_package:",
    "source_task_contract_proposal:",
    "source_authorization:",
    "source_candidate_template:",
    "source_conversion_policy:",
    "source_validator:",
    "generation_mode:",
    "output_target:",
    "primary_output_format:",
    "primary_validator_target:",
    "carry_forward:",
    "accepted_limitations:",
    "open_questions:",
    "downstream_limits:",
    "non_authority_boundary:",
    "boundaries:",
    "dry_run_required:",
    "write_to_staging_only:",
    "active_task_write_allowed:",
    "queue_write_allowed:",
    "execution_authorized:",
    "approval_record_creation_allowed:",
]

EXPECTED_VALUES = {
    "source_validator": "scripts/validate-proposal-to-task-conversion.py",
    "primary_output_format": "generated_conversion_package_with_embedded_candidate",
    "dry_run_required": "true",
    "write_to_staging_only": "true",
    "active_task_write_allowed": "false",
    "queue_write_allowed": "false",
    "execution_authorized": "false",
    "approval_record_creation_allowed": "false",
}


class GenError(Exception):
    def __init__(self, message, blocked=True):
        super().__init__(message)
        self.message = message
        self.blocked = blocked


def parse_args():
    p = argparse.ArgumentParser(description="Generate M50-compatible task contract candidate conversion package record")
    p.add_argument("--input", help="Path to generator input markdown")
    p.add_argument("--dry-run", action="store_true", help="Run in dry-run mode")
    p.add_argument("--write", action="store_true", help="Write generated conversion package")
    p.add_argument("--out", help="Output directory (required with --write)")
    p.add_argument("--json", action="store_true", help="Emit JSON output")
    p.add_argument("--explain", action="store_true", help="Explain non-authority boundaries")
    p.add_argument("--fixtures", action="store_true", help="Run generator fixtures")
    return p.parse_args()


def print_explain():
    lines = [
        "Task contract candidate generator creates M50-compatible generated conversion packages only.",
        "Generator dry-run does not write files.",
        "Generator write mode writes only to generated/task-contract-candidates/.",
        "Generator output requires later placement gate.",
    ] + NON_AUTHORITY_MARKERS
    print("\n".join(lines))


def json_out(payload):
    print(json.dumps(payload, indent=2, sort_keys=True))


def text_out(result, findings):
    print(result)
    for item in findings:
        print(item)


def base_payload(result, dry_run=True, written=False, output_path=None, primary_validator_target=None, would_write_to=None):
    return {
        "result": result,
        "exit_code": EXIT_CODES[result],
        "dry_run": dry_run,
        "written": written,
        "output_path": output_path,
        "generated_candidate_path": None,
        "primary_validator_target": primary_validator_target,
        "would_write_to": would_write_to,
        "findings": [],
        "warnings": [],
        "non_authority_markers": list(NON_AUTHORITY_MARKERS),
    }


def parse_simple_fields(text):
    fields = {}
    for line in text.splitlines():
        m = re.match(r"^\s*([a-zA-Z0-9_]+):\s*(.*?)\s*$", line)
        if m:
            key = m.group(1)
            val = m.group(2)
            if val.startswith("#"):
                val = ""
            fields[key] = val
    return fields


def ensure_required_text_keys(text):
    missing = [k for k in REQUIRED_KEYS if k not in text]
    if missing:
        raise GenError("MISSING_REQUIRED_FIELDS: " + ", ".join(missing), blocked=False)


def resolve_safe_path(path_value, repo_root):
    p = Path(path_value)
    if ".." in p.parts:
        raise GenError("PATH_TRAVERSAL_REQUESTED", blocked=True)
    if str(path_value).strip() in {"tasks/active-task.md", "tasks/queue", "tasks/queue/", "approvals", "approvals/"}:
        raise GenError("FORBIDDEN_TARGET_PATH", blocked=True)
    if p.is_absolute():
        return p.resolve()
    return (repo_root / p).resolve()


def ensure_inside_staging(resolved_path, repo_root):
    staging = (repo_root / "generated" / "task-contract-candidates").resolve()
    try:
        resolved_path.relative_to(staging)
    except ValueError as exc:
        raise GenError("OUTPUT_OUTSIDE_STAGING", blocked=True) from exc


def safe_candidate_id(fields):
    input_id = (fields.get("input_id") or "").strip()
    source_pkg = (fields.get("source_conversion_package") or "").strip()

    candidate_base = input_id
    if not candidate_base and source_pkg:
        candidate_base = Path(source_pkg).stem

    if not re.fullmatch(r"[a-z0-9_-]+", candidate_base):
        raise GenError("UNSAFE_OR_EMPTY_CANDIDATE_ID", blocked=True)

    candidate = candidate_base.strip("-_")
    if not candidate:
        raise GenError("UNSAFE_OR_EMPTY_CANDIDATE_ID", blocked=True)
    return candidate


def validate_fields(fields):
    for key, expected in EXPECTED_VALUES.items():
        actual = (fields.get(key) or "").strip()
        if actual != expected:
            raise GenError(f"INVALID_FIELD_{key.upper()}", blocked=True)

    status = (fields.get("generator_input_status") or "").strip()
    allowed = {
        "GENERATOR_INPUT_READY",
        "GENERATOR_INPUT_READY_WITH_LIMITATIONS",
        "GENERATOR_INPUT_BLOCKED",
        "GENERATOR_INPUT_INVALID",
    }
    if status not in allowed:
        raise GenError("INVALID_GENERATOR_INPUT_STATUS", blocked=False)
    if status in {"GENERATOR_INPUT_BLOCKED", "GENERATOR_INPUT_INVALID"}:
        raise GenError("INPUT_STATUS_BLOCKED_OR_INVALID", blocked=True)


def validate_source_conversion_package(fields):
    src = (fields.get("source_conversion_package") or "").strip()
    if not src:
        raise GenError("SOURCE_CONVERSION_PACKAGE_MISSING", blocked=True)
    src_path = Path(src)
    if not src_path.exists() or not src_path.is_file():
        raise GenError("SOURCE_CONVERSION_PACKAGE_NOT_FOUND", blocked=True)
    try:
        content = src_path.read_text(encoding="utf-8")
    except Exception as exc:
        raise GenError(f"SOURCE_CONVERSION_PACKAGE_UNREADABLE: {exc}", blocked=True) from exc
    if "conversion_package:" not in content or "task_contract_candidate" not in content:
        raise GenError("SOURCE_CONVERSION_PACKAGE_NOT_M50_COMPATIBLE_SHAPE", blocked=True)
    return content


def evaluate_input(input_path, mode, out_dir=None, allow_write=True):
    repo_root = Path(__file__).resolve().parent.parent

    path_obj = Path(input_path)
    if not path_obj.exists() or not path_obj.is_file():
        payload = base_payload(RESULT_BLOCKED, dry_run=True, written=False, output_path=None, primary_validator_target=None, would_write_to=None)
        payload["findings"].append("INPUT_FILE_MISSING")
        return payload

    try:
        text = path_obj.read_text(encoding="utf-8")
    except Exception as exc:
        payload = base_payload(RESULT_BLOCKED, dry_run=True, written=False, output_path=None, primary_validator_target=None, would_write_to=None)
        payload["findings"].append(f"INPUT_FILE_UNREADABLE: {exc}")
        return payload

    write_mode = mode == "write"
    dry_run_mode = not write_mode

    try:
        ensure_required_text_keys(text)
        fields = parse_simple_fields(text)
        validate_fields(fields)

        output_target = (fields.get("output_target") or "").strip()
        if not output_target:
            raise GenError("OUTPUT_TARGET_MISSING", blocked=True)

        output_target_resolved = resolve_safe_path(output_target, repo_root)
        ensure_inside_staging(output_target_resolved, repo_root)

        if write_mode:
            if not out_dir:
                raise GenError("WRITE_REQUIRES_OUT", blocked=True)
            out_resolved = resolve_safe_path(out_dir, repo_root)
            ensure_inside_staging(out_resolved, repo_root)
        else:
            out_resolved = output_target_resolved

        candidate_id = safe_candidate_id(fields)
        filename = f"{candidate_id}.generated-conversion-package.md"
        predicted_abs = (out_resolved / filename).resolve()
        ensure_inside_staging(predicted_abs, repo_root)
        predicted_rel = predicted_abs.relative_to(repo_root.resolve()).as_posix()

        src_content = validate_source_conversion_package(fields)

        if dry_run_mode:
            return base_payload(
                RESULT_DRY_RUN_OK,
                dry_run=True,
                written=False,
                output_path=None,
                primary_validator_target=None,
                would_write_to=predicted_rel,
            )

        if not allow_write:
            raise GenError("FIXTURE_RUN_WRITE_NOT_ALLOWED", blocked=True)

        out_resolved.mkdir(parents=True, exist_ok=True)
        predicted_abs.write_text(src_content, encoding="utf-8")

        return base_payload(
            RESULT_WRITE_OK,
            dry_run=False,
            written=True,
            output_path=predicted_rel,
            primary_validator_target=predicted_rel,
            would_write_to=predicted_rel,
        )

    except GenError as exc:
        token = RESULT_BLOCKED if exc.blocked else RESULT_FAILED
        payload = base_payload(token, dry_run=True, written=False, output_path=None, primary_validator_target=None, would_write_to=None)
        payload["findings"].append(exc.message)
        return payload
    except Exception as exc:
        payload = base_payload(RESULT_FAILED, dry_run=True, written=False, output_path=None, primary_validator_target=None, would_write_to=None)
        payload["findings"].append(f"UNHANDLED_ERROR: {exc}")
        return payload


def parse_fixture_meta(text):
    if "fixture:" not in text:
        raise GenError("FIXTURE_METADATA_MISSING", blocked=False)

    def find(name):
        m = re.search(rf"^\s*{re.escape(name)}:\s*(.*?)\s*$", text, flags=re.MULTILINE)
        return m.group(1).strip() if m else None

    fixture_type = find("fixture_type")
    expected_result = find("expected_result")
    expected_exit = find("expected_exit_code")
    cli_mode = find("fixture_cli_mode") or "dry_run"

    if not fixture_type or not expected_result or not expected_exit:
        raise GenError("FIXTURE_METADATA_INCOMPLETE", blocked=False)

    try:
        expected_exit_code = int(expected_exit)
    except ValueError as exc:
        raise GenError("FIXTURE_EXPECTED_EXIT_NOT_INT", blocked=False) from exc

    return fixture_type, expected_result, expected_exit_code, cli_mode


def run_fixtures(json_mode):
    root = Path("tests/fixtures/task-contract-candidate-generator/")
    pos_dir = root / "positive"
    neg_dir = root / "negative"

    if not root.exists() or not root.is_dir() or not pos_dir.is_dir() or not neg_dir.is_dir():
        payload = base_payload(RESULT_BLOCKED, dry_run=True, written=False, output_path=None, primary_validator_target=None, would_write_to=None)
        payload["findings"].append("GENERATOR_FIXTURES_MISSING")
        if json_mode:
            json_out(payload)
        else:
            text_out(payload["result"], payload["findings"])
        return payload["exit_code"]

    fixtures = sorted(list(pos_dir.glob("*.md")) + list(neg_dir.glob("*.md")))
    entries = []
    failed = 0

    for fx in fixtures:
        try:
            text = fx.read_text(encoding="utf-8")
            fixture_type, expected_result, expected_exit_code, cli_mode = parse_fixture_meta(text)

            mode = "dry_run"
            if cli_mode == "write":
                mode = "write"

            payload = evaluate_input(str(fx), mode=mode, out_dir=None, allow_write=False)
            actual_result = payload["result"]
            actual_exit = payload["exit_code"]

            passed = (actual_result == expected_result and actual_exit == expected_exit_code)

            if fixture_type == "positive" and passed:
                if payload.get("would_write_to") is None:
                    passed = False
                if payload.get("primary_validator_target") is not None:
                    passed = False
                if payload.get("generated_candidate_path") is not None:
                    passed = False

            if not passed:
                failed += 1

            entries.append({
                "path": fx.as_posix(),
                "fixture_type": fixture_type,
                "expected_result": expected_result,
                "actual_result": actual_result,
                "expected_exit_code": expected_exit_code,
                "actual_exit_code": actual_exit,
                "passed": passed,
            })

        except GenError as exc:
            failed += 1
            entries.append({
                "path": fx.as_posix(),
                "fixture_type": "unknown",
                "expected_result": "unknown",
                "actual_result": RESULT_FAILED,
                "expected_exit_code": 1,
                "actual_exit_code": 1,
                "passed": False,
                "error": exc.message,
            })

    total = len(entries)
    passed_count = total - failed

    final_result = RESULT_DRY_RUN_OK if failed == 0 else RESULT_FAILED
    final_payload = base_payload(
        final_result,
        dry_run=True,
        written=False,
        output_path=None,
        primary_validator_target=None,
        would_write_to=None,
    )
    final_payload["fixture_summary"] = {
        "total": total,
        "passed": passed_count,
        "failed": failed,
    }
    final_payload["fixtures"] = entries

    if json_mode:
        json_out(final_payload)
    else:
        text_out(final_payload["result"], final_payload["findings"])
        print(json.dumps(final_payload["fixture_summary"], sort_keys=True))

    return final_payload["exit_code"]


def emit(payload, json_mode):
    if json_mode:
        json_out(payload)
    else:
        text_out(payload["result"], payload["findings"])
    return payload["exit_code"]


def main():
    args = parse_args()

    if args.explain:
        print_explain()
        return 0

    if args.fixtures:
        return run_fixtures(args.json)

    if not args.input:
        payload = base_payload(RESULT_BLOCKED, dry_run=True, written=False, output_path=None, primary_validator_target=None, would_write_to=None)
        payload["findings"].append("INPUT_FILE_MISSING")
        return emit(payload, args.json)

    if args.write and args.dry_run:
        payload = base_payload(RESULT_FAILED, dry_run=True, written=False, output_path=None, primary_validator_target=None, would_write_to=None)
        payload["findings"].append("MUTUALLY_EXCLUSIVE_MODES")
        return emit(payload, args.json)

    if args.write and not args.out:
        payload = base_payload(RESULT_BLOCKED, dry_run=True, written=False, output_path=None, primary_validator_target=None, would_write_to=None)
        payload["findings"].append("WRITE_REQUIRES_OUT")
        return emit(payload, args.json)

    mode = "write" if args.write else "dry_run"
    payload = evaluate_input(args.input, mode=mode, out_dir=args.out, allow_write=True)
    return emit(payload, args.json)


if __name__ == "__main__":
    sys.exit(main())
