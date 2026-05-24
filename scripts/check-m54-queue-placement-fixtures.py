#!/usr/bin/env python3
import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path


POSITIVE_FILES = [
    "README.md",
    "valid-canonical-root-input.json",
    "valid-alt-root-input.json",
    "valid-markdown-fenced-json-input.md",
    "valid-input-with-limitations.json",
    "valid-m54-intake-ready.md",
    "valid-m54-intake-ready-with-limitations.md",
    "valid-m53-placement-result-eligible.json",
    "valid-m53-placement-result-eligible-with-limitations.json",
    "valid-queue-placement-artifact.json",
    "valid-materialization-result-blocked-safe-default.json",
    "valid-dry-run-allowed.json",
]

NEGATIVE_FILES = [
    "README.md",
    "missing-input-root.json",
    "both-input-roots-present.json",
    "unsafe-boundary-execution-authorized.json",
    "unsafe-boundary-approval-created.json",
    "unsafe-boundary-active-task-replacement.json",
    "unsafe-boundary-m55-authorized.json",
    "target-outside-queue.json",
    "target-active-task-path.json",
    "missing-source-traceability.json",
    "missing-carry-forward.json",
    "m53-placement-result-not-eligible.json",
    "m53-placement-result-materialization-authorized.json",
    "m53-placement-result-already-queued.json",
    "m54-intake-blocked.md",
    "materialization-result-claims-execution.json",
    "materialization-result-claims-m55.json",
]

FORBIDDEN_MARKERS = [
    "final_status: M53_PLACEMENT_REVIEW_LAYER_COMPLETE",
    "m53_handoff_ready:",
    "reports/m54-queue-placement-materialization-integration.md",
    "reports/m54-task-candidate-queue-placement-evidence-report.md",
    "reports/m54-completion-review.md",
]


def parse_args():
    p = argparse.ArgumentParser(description="Check M54 queue placement fixtures")
    p.add_argument("--fixtures", action="store_true", help="Run fixture checks")
    p.add_argument("--json", action="store_true", help="Output JSON")
    p.add_argument("--repo-root", default=".", help="Repository root")
    return p.parse_args()


def emit(payload, as_json):
    if as_json:
        sys.stdout.write(json.dumps(payload, ensure_ascii=False) + "\n")
    else:
        sys.stdout.write(payload["m54_fixture_integration"]["result"] + "\n")


def blocked(message, blockers=None, as_json=False):
    payload = {
        "m54_fixture_integration": {
            "result": "M54_FIXTURE_INTEGRATION_BLOCKED",
            "exit_code": 2,
            "positive_fixture_count": 0,
            "negative_fixture_count": 0,
            "positive_required_files_present": False,
            "negative_required_files_present": False,
            "json_files_valid": False,
            "markdown_fenced_json_valid": False,
            "positive_semantics_valid": False,
            "negative_semantics_valid": False,
            "expected_blockers_valid": False,
            "production_content_not_copied": False,
            "cli_compile_ok": False,
            "sandbox_dry_run_positive_ok": False,
            "sandbox_dry_run_negative_ok": False,
            "no_write_mode_executed": True,
            "no_queue_files_created_in_production": True,
            "no_reports_created": True,
            "findings": [message] if message else [],
            "warnings": [],
            "blockers": blockers or [message] if message else [],
            "boundary_flags": {
                "fixture_check_only": True,
                "write_mode_allowed": False,
                "production_materialization_allowed": False,
                "queue_write_allowed": False,
                "active_task_replacement_allowed": False,
                "approval_creation_allowed": False,
                "execution_authorized": False,
                "m55_authorized": False,
            },
        }
    }
    emit(payload, as_json)
    return 2


def fail(message, blockers=None, as_json=False):
    payload = {
        "m54_fixture_integration": {
            "result": "M54_FIXTURE_INTEGRATION_FAIL",
            "exit_code": 1,
            "positive_fixture_count": 0,
            "negative_fixture_count": 0,
            "positive_required_files_present": False,
            "negative_required_files_present": False,
            "json_files_valid": False,
            "markdown_fenced_json_valid": False,
            "positive_semantics_valid": False,
            "negative_semantics_valid": False,
            "expected_blockers_valid": False,
            "production_content_not_copied": False,
            "cli_compile_ok": False,
            "sandbox_dry_run_positive_ok": False,
            "sandbox_dry_run_negative_ok": False,
            "no_write_mode_executed": True,
            "no_queue_files_created_in_production": True,
            "no_reports_created": True,
            "findings": [message] if message else [],
            "warnings": [],
            "blockers": blockers or [message] if message else [],
            "boundary_flags": {
                "fixture_check_only": True,
                "write_mode_allowed": False,
                "production_materialization_allowed": False,
                "queue_write_allowed": False,
                "active_task_replacement_allowed": False,
                "approval_creation_allowed": False,
                "execution_authorized": False,
                "m55_authorized": False,
            },
        }
    }
    emit(payload, as_json)
    return 1


def read_text(path):
    return path.read_text(encoding="utf-8")


def load_json(path):
    return json.loads(read_text(path))


def count_files(path):
    return len([p for p in path.iterdir() if p.is_file()])


def has_exact_files(path, names):
    present = {p.name for p in path.iterdir() if p.is_file()}
    return set(names) == present


def parse_json_block(md_text):
    blocks = re.findall(r"```\s*json\s*(.*?)\s*```", md_text, re.DOTALL)
    return blocks


def parse_frontmatter_value(text, key):
    match = re.search(rf"(?m)^\\s*{re.escape(key)}\\s*:\\s*(\\S+)\\s*$", text)
    return match.group(1).strip() if match else None


def write_file(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def run(cmd, cwd):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, check=False)


def git_diff_clean(repo_root, paths):
    cmd = ["git", "diff", "--quiet", "--"]
    cmd.extend(paths)
    proc = run(cmd, repo_root)
    return proc.returncode == 0


def cli_compile_ok(repo_root):
    proc = run([sys.executable, "-m", "py_compile", str(repo_root / "scripts/materialize-task-candidate-placement.py")], repo_root)
    return proc.returncode == 0


def fixture_semantics(repo_root):
    positive_dir = repo_root / "tests/fixtures/task-candidate-queue-placement/positive"
    negative_dir = repo_root / "tests/fixtures/task-candidate-queue-placement/negative"

    # Positive checks
    canonical = load_json(positive_dir / "valid-canonical-root-input.json")
    alt = load_json(positive_dir / "valid-alt-root-input.json")
    limited = load_json(positive_dir / "valid-input-with-limitations.json")
    m53_ok = load_json(positive_dir / "valid-m53-placement-result-eligible.json")
    m53_lim = load_json(positive_dir / "valid-m53-placement-result-eligible-with-limitations.json")
    artifact = load_json(positive_dir / "valid-queue-placement-artifact.json")
    blocked = load_json(positive_dir / "valid-materialization-result-blocked-safe-default.json")
    dry = load_json(positive_dir / "valid-dry-run-allowed.json")

    assert "queue_placement_input" in canonical
    assert "task_candidate_queue_placement_input" in alt and "queue_placement_input" not in alt
    assert limited["queue_placement_input"]["carry_forward"]["accepted_limitations"]
    assert limited["queue_placement_input"]["carry_forward"]["warnings"]
    assert limited["queue_placement_input"]["carry_forward"]["downstream_limits"]
    assert m53_ok["placement_review_result"]["result"] == "PLACEMENT_REVIEW_ELIGIBLE"
    assert m53_ok["placement_review_result"]["eligible_as_m54_queue_materialization_input"] is True
    assert m53_ok["placement_review_result"]["eligible_as_m54_active_task_proposal_input"] is False
    assert m53_ok["placement_review_result"]["m54_materialization_authorized"] is False
    assert m53_lim["placement_review_result"]["result"] == "PLACEMENT_REVIEW_ELIGIBLE_WITH_LIMITATIONS"
    assert artifact["queue_placement_artifact"]["target_queue_path"].startswith("tasks/queue/")
    assert blocked["queue_placement_result"]["result"] == "QUEUE_PLACEMENT_BLOCKED"
    assert blocked["queue_placement_result"]["queue_entry_path"] is None
    assert dry["queue_placement_dry_run"]["result"] == "M54_QUEUE_PLACEMENT_DRY_RUN_ALLOWED"

    # Negative checks
    missing_root = load_json(negative_dir / "missing-input-root.json")
    both = load_json(negative_dir / "both-input-roots-present.json")
    exec_auth = load_json(negative_dir / "unsafe-boundary-execution-authorized.json")
    approval = load_json(negative_dir / "unsafe-boundary-approval-created.json")
    active = load_json(negative_dir / "unsafe-boundary-active-task-replacement.json")
    m55 = load_json(negative_dir / "unsafe-boundary-m55-authorized.json")
    outside = load_json(negative_dir / "target-outside-queue.json")
    active_target = load_json(negative_dir / "target-active-task-path.json")
    missing_trace = load_json(negative_dir / "missing-source-traceability.json")
    missing_carry = load_json(negative_dir / "missing-carry-forward.json")
    not_eligible = load_json(negative_dir / "m53-placement-result-not-eligible.json")
    mat_auth = load_json(negative_dir / "m53-placement-result-materialization-authorized.json")
    already = load_json(negative_dir / "m53-placement-result-already-queued.json")
    blocked_intake = read_text(negative_dir / "m54-intake-blocked.md")
    claim_exec = load_json(negative_dir / "materialization-result-claims-execution.json")
    claim_m55 = load_json(negative_dir / "materialization-result-claims-m55.json")

    assert "queue_placement_input" not in missing_root and "task_candidate_queue_placement_input" not in missing_root
    assert "queue_placement_input" in both and "task_candidate_queue_placement_input" in both
    assert exec_auth["queue_placement_input"]["boundary_flags"]["execution_authorized"] is True
    assert approval["queue_placement_input"]["boundary_flags"]["approval_created"] is True
    assert active["queue_placement_input"]["boundary_flags"]["active_task_replacement_authorized"] is True
    assert m55["queue_placement_input"]["boundary_flags"]["m55_authorized"] is True
    assert outside["queue_placement_input"]["target_queue_path"] == "generated/escaped-target.md"
    assert active_target["queue_placement_input"]["target_queue_path"] == "tasks/active-task.md"
    assert "source_traceability" not in missing_trace["queue_placement_input"]
    assert "carry_forward" not in missing_carry["queue_placement_input"]
    assert not_eligible["placement_review_result"]["result"] == "PLACEMENT_REVIEW_NOT_ELIGIBLE"
    assert mat_auth["placement_review_result"]["m54_materialization_authorized"] is True
    assert already["placement_review_result"]["queue_placement_performed"] is True
    assert "intake_status: M54_INTAKE_BLOCKED" in blocked_intake
    assert claim_exec["queue_placement_result"]["boundary_flags"]["execution_authorized"] is True
    assert claim_m55["queue_placement_result"]["boundary_flags"]["m55_start_authorized"] is True

    return True


def markdown_fixture_ok(path):
    blocks = parse_json_block(read_text(path))
    return len(blocks) == 1 and "queue_placement_input" in json.loads(blocks[0])


def production_markers_absent(repo_root):
    positive_dir = repo_root / "tests/fixtures/task-candidate-queue-placement/positive"
    negative_dir = repo_root / "tests/fixtures/task-candidate-queue-placement/negative"
    for marker in FORBIDDEN_MARKERS:
        for p in list(positive_dir.iterdir()) + list(negative_dir.iterdir()):
            if p.is_file() and marker in read_text(p):
                return False
    return True


def create_sandbox(repo_root):
    sandbox = Path(tempfile.mkdtemp(prefix="m54-fixture-integration-"))
    (sandbox / "reports").mkdir()
    (sandbox / "tasks/queue").mkdir(parents=True)
    (sandbox / "approvals").mkdir()
    (sandbox / "generated").mkdir()
    write_file(sandbox / "reports/m54-m53-readiness-intake.md", "---\nintake_status: M54_INTAKE_READY\n---\n")
    write_file(sandbox / "reports/m53-completion-review.md", "---\nfinal_status: M53_PLACEMENT_REVIEW_LAYER_COMPLETE\n---\n")
    write_file(
        sandbox / "reports/m53-placement-review-result-agent-action-review.json",
        json.dumps(
            {
                "placement_review_result": {
                    "result": "PLACEMENT_REVIEW_ELIGIBLE",
                    "exit_code": 0,
                    "eligible_for_downstream_placement": True,
                    "eligible_as_m54_queue_materialization_input": True,
                    "eligible_as_m54_active_task_proposal_input": False,
                    "m54_materialization_authorized": False,
                    "queue_placement_performed": False,
                    "active_task_replacement_performed": False,
                    "approval_created": False,
                    "boundary_flags": {
                        "review_only": True,
                        "queue_write_allowed": False,
                        "active_task_write_allowed": False,
                        "execution_authorized": False,
                        "approval_record_creation_allowed": False,
                        "lifecycle_mutation_allowed": False,
                        "m54_materialization_authorized": False,
                    },
                    "source_m52_completion_review": "reports/m52-completion-review.md",
                    "source_m52_validation_result": "reports/m52-candidate-validation-result-agent-action-review.json",
                    "source_generated_artifact": "generated/agent-action-review-task-candidate.md",
                    "source_traceability": {
                        "source_proposal": "TRACE",
                        "source_authorization": "TRACE",
                        "source_conversion_package": "TRACE",
                        "source_generated_artifact": "TRACE",
                        "m50_traceability": "TRACE",
                        "m51_generator_evidence": "TRACE",
                        "m52_validation_evidence": "TRACE",
                    },
                    "carry_forward": {
                        "accepted_limitations": [],
                        "warnings": [],
                        "open_questions": [],
                        "downstream_limits": [],
                        "known_gaps": [],
                        "non_authority_boundary": [
                            "M53 placement review result is not approval.",
                        ],
                    },
                    "non_authority_markers": [
                        "M53 placement review result is not approval.",
                        "M53 placement review result does not authorize execution.",
                        "M53 placement review result does not authorize queue placement.",
                        "M53 placement review result does not authorize active-task replacement.",
                        "M53 placement review result does not authorize lifecycle mutation.",
                        "M53 placement review result does not authorize M54 materialization.",
                    ],
                    "m54_independent_validation_required": True,
                    "m54_may_not_start_without_own_gate": True,
                    "queue_placement_performed": False,
                    "active_task_replacement_performed": False,
                }
            },
            ensure_ascii=False,
        ),
    )
    return sandbox


def run_cli(repo_root, input_path, target, sandbox_root, json_mode=True):
    cmd = [
        sys.executable,
        str(repo_root / "scripts/materialize-task-candidate-placement.py"),
        "--input",
        str(input_path),
        "--target",
        target,
        "--repo-root",
        str(sandbox_root),
        "--dry-run",
    ]
    if json_mode:
        cmd.append("--json")
    proc = run(cmd, repo_root)
    return proc


def parse_cli_json(stdout):
    return json.loads(stdout)


def expected_negative_blocker(name):
    mapping = {
        "unsafe-boundary-execution-authorized.json": ["EXECUTION_AUTHORIZATION_FORBIDDEN", "INPUT_FLAG_UNSAFE:execution_requested", "INPUT_BOUNDARY_FLAG_UNSAFE:execution_authorized"],
        "unsafe-boundary-approval-created.json": ["APPROVAL_CREATION_FORBIDDEN", "INPUT_FLAG_UNSAFE:approval_requested", "INPUT_BOUNDARY_FLAG_UNSAFE:approval_created"],
        "unsafe-boundary-active-task-replacement.json": ["ACTIVE_TASK_REPLACEMENT_FORBIDDEN", "INPUT_FLAG_UNSAFE:active_task_replacement_requested", "INPUT_BOUNDARY_FLAG_UNSAFE:active_task_replacement_authorized"],
        "unsafe-boundary-m55-authorized.json": ["M55_AUTHORIZATION_FORBIDDEN", "INPUT_FLAG_UNSAFE:m55_requested", "INPUT_BOUNDARY_FLAG_UNSAFE:m55_authorized"],
        "target-outside-queue.json": ["TARGET_QUEUE_PATH_UNSAFE"],
        "target-active-task-path.json": ["TARGET_QUEUE_PATH_UNSAFE"],
        "missing-source-traceability.json": ["SOURCE_TRACEABILITY_INCOMPLETE"],
        "missing-carry-forward.json": ["CARRY_FORWARD_MISSING"],
    }
    return mapping[name]


def main():
    args = parse_args()
    if not args.fixtures:
        return 2 if not args.json else blocked("Missing --fixtures mode", as_json=True)

    repo_root = Path(args.repo_root).resolve()
    if not repo_root.exists() or not repo_root.is_dir():
        return blocked("Invalid repo root", ["REPO_ROOT_INVALID"], args.json)

    positive_dir = repo_root / "tests/fixtures/task-candidate-queue-placement/positive"
    negative_dir = repo_root / "tests/fixtures/task-candidate-queue-placement/negative"

    if not positive_dir.exists() or not negative_dir.exists():
        return blocked("Missing fixture directory", ["FIXTURE_DIRECTORY_MISSING"], args.json)

    positive_count = count_files(positive_dir)
    negative_count = count_files(negative_dir)
    if positive_count != 12:
        return blocked("Positive fixture count mismatch", [f"POSITIVE_COUNT_{positive_count}"], args.json)
    if negative_count != 17:
        return blocked("Negative fixture count mismatch", [f"NEGATIVE_COUNT_{negative_count}"], args.json)

    if not has_exact_files(positive_dir, POSITIVE_FILES):
        return blocked("Positive required files missing", ["POSITIVE_REQUIRED_FILES_MISSING"], args.json)
    if not has_exact_files(negative_dir, NEGATIVE_FILES):
        return blocked("Negative required files missing", ["NEGATIVE_REQUIRED_FILES_MISSING"], args.json)

    cli_ok = cli_compile_ok(repo_root)
    if not cli_ok:
        return blocked("CLI compile failed", ["CLI_COMPILE_FAILED"], args.json)

    try:
        for p in list(positive_dir.iterdir()) + list(negative_dir.iterdir()):
            if p.suffix == ".json":
                load_json(p)
        md = read_text(positive_dir / "valid-markdown-fenced-json-input.md")
        if len(parse_json_block(md)) != 1:
            return blocked("Positive markdown fenced JSON malformed", ["MARKDOWN_FENCED_JSON_INVALID"], args.json)
        json.loads(parse_json_block(md)[0])
        if "intake_status: M54_INTAKE_BLOCKED" not in read_text(negative_dir / "m54-intake-blocked.md"):
            return blocked("Negative blocked intake marker missing", ["NEGATIVE_BLOCKED_INTAKE_MISSING"], args.json)
    except Exception as exc:
        return blocked(f"JSON or markdown parse failed: {exc}", ["JSON_PARSE_FAILED"], args.json)

    try:
        semantics_ok = fixture_semantics(repo_root)
        md_ok = markdown_fixture_ok(positive_dir / "valid-markdown-fenced-json-input.md")
        prod_ok = production_markers_absent(repo_root)
    except Exception as exc:
        return fail(f"Fixture semantics failed: {exc}", ["FIXTURE_SEMANTICS_FAILED"], args.json)

    if not semantics_ok or not md_ok:
        return fail("Fixture semantics invalid", ["FIXTURE_SEMANTICS_INVALID"], args.json)
    if not prod_ok:
        return fail("Production markers copied into fixtures", ["PRODUCTION_MARKERS_COPIED"], args.json)

    sandbox = create_sandbox(repo_root)
    cli_dry_run_positive_ok = True
    cli_dry_run_negative_ok = True

    positive_cases = [
        ("valid-canonical-root-input.json", "tasks/queue/valid-sandbox-target.md"),
        ("valid-alt-root-input.json", "tasks/queue/valid-alt-root-target.md"),
        ("valid-markdown-fenced-json-input.md", "tasks/queue/valid-md-input-target.md"),
    ]
    for name, target in positive_cases:
        input_path = positive_dir / name
        proc = run_cli(repo_root, input_path, target, sandbox)
        if proc.returncode != 0:
            cli_dry_run_positive_ok = False
            break
        try:
            data = parse_cli_json(proc.stdout)
            dry = data["queue_placement_dry_run"]
            if dry["result"] != "M54_QUEUE_PLACEMENT_DRY_RUN_ALLOWED" or dry["exit_code"] != 0 or not dry["would_materialize"] or not dry["would_create_queue_entry"]:
                cli_dry_run_positive_ok = False
                break
        except Exception:
            cli_dry_run_positive_ok = False
            break
        if (sandbox / target).exists():
            cli_dry_run_positive_ok = False
            break

    negative_cases = [
        "unsafe-boundary-execution-authorized.json",
        "target-outside-queue.json",
        "missing-source-traceability.json",
        "missing-carry-forward.json",
    ]
    for name in negative_cases:
        fixture = load_json(negative_dir / name)
        input_obj = fixture.get("queue_placement_input", fixture)
        target = input_obj.get("target_queue_path", "tasks/queue/candidate-for-validation.md")
        if name == "target-outside-queue.json":
            target = input_obj["target_queue_path"]
        proc = run_cli(repo_root, negative_dir / name, target, sandbox)
        if proc.returncode != 2:
            cli_dry_run_negative_ok = False
            break
        try:
            data = parse_cli_json(proc.stdout)
            dry = data["queue_placement_dry_run"]
            if dry["result"] != "M54_QUEUE_PLACEMENT_DRY_RUN_BLOCKED" or dry["exit_code"] != 2:
                cli_dry_run_negative_ok = False
                break
            blockers = dry.get("blockers", []) + dry.get("warnings", []) + dry.get("findings", [])
            expected = expected_negative_blocker(name)
            if not any(b == expected or b in blockers for b in expected):
                # tolerate current generic markers that are semantically equivalent
                if name == "unsafe-boundary-execution-authorized.json":
                    if not any(x in blockers for x in ["INPUT_FLAG_UNSAFE:execution_requested", "INPUT_BOUNDARY_FLAG_UNSAFE:execution_authorized"]):
                        cli_dry_run_negative_ok = False
                        break
                elif name == "target-outside-queue.json":
                    if "TARGET_QUEUE_PATH_UNSAFE" not in blockers:
                        cli_dry_run_negative_ok = False
                        break
                elif name == "missing-source-traceability.json":
                    if "SOURCE_TRACEABILITY_INCOMPLETE" not in blockers:
                        cli_dry_run_negative_ok = False
                        break
                elif name == "missing-carry-forward.json":
                    if "CARRY_FORWARD_MISSING" not in blockers:
                        cli_dry_run_negative_ok = False
                        break
        except Exception:
            cli_dry_run_negative_ok = False
            break
        if any((sandbox / "tasks/queue").glob("*.md")):
            cli_dry_run_negative_ok = False
            break

    no_write_mode_executed = True
    no_queue_files_created_in_production = not any((repo_root / "tasks/queue").glob("agent-action-review-task-candidate.md")) and git_diff_clean(repo_root, ["tasks/queue"])
    no_reports_created = git_diff_clean(repo_root, ["reports"])

    result = "M54_FIXTURE_INTEGRATION_PASS"
    exit_code = 0
    if not cli_dry_run_positive_ok or not cli_dry_run_negative_ok:
        result = "M54_FIXTURE_INTEGRATION_FAIL"
        exit_code = 1

    payload = {
        "m54_fixture_integration": {
            "result": result,
            "exit_code": exit_code,
            "positive_fixture_count": positive_count,
            "negative_fixture_count": negative_count,
            "positive_required_files_present": True,
            "negative_required_files_present": True,
            "json_files_valid": True,
            "markdown_fenced_json_valid": md_ok,
            "positive_semantics_valid": True,
            "negative_semantics_valid": True,
            "expected_blockers_valid": True,
            "production_content_not_copied": True,
            "cli_compile_ok": cli_ok,
            "sandbox_dry_run_positive_ok": cli_dry_run_positive_ok,
            "sandbox_dry_run_negative_ok": cli_dry_run_negative_ok,
            "no_write_mode_executed": no_write_mode_executed,
            "no_queue_files_created_in_production": no_queue_files_created_in_production,
            "no_reports_created": no_reports_created,
            "findings": [],
            "warnings": [],
            "blockers": [],
            "boundary_flags": {
                "fixture_check_only": True,
                "write_mode_allowed": False,
                "production_materialization_allowed": False,
                "queue_write_allowed": False,
                "active_task_replacement_allowed": False,
                "approval_creation_allowed": False,
                "execution_authorized": False,
                "m55_authorized": False,
            },
        }
    }
    emit(payload, args.json)
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
