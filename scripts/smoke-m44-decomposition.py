#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

M44_SMOKE_PASS = "M44_SMOKE_PASS"
M44_SMOKE_FAIL = "M44_SMOKE_FAIL"
M44_SMOKE_FAILED = "M44_SMOKE_FAILED"

POSITIVE_MAP = {
    "tests/fixtures/task-contract-linter/positive/valid-task-contract.md": "TASK_LINT_PASS",
    "tests/fixtures/task-contract-linter/positive/valid-ui-task-contract.md": "TASK_LINT_PASS",
    "tests/fixtures/task-contract-linter/positive/valid-queue-entry.json": "TASK_LINT_PASS",
}

NEGATIVE_MAP = {
    "tests/fixtures/task-contract-linter/negative/missing-required-field-task.md": "TASK_LINT_FAIL",
    "tests/fixtures/task-contract-linter/negative/execution-authority-field-task.md": "TASK_LINT_FAIL",
    "tests/fixtures/task-contract-linter/negative/ui-raw-import-task.md": "TASK_LINT_FAIL",
    "tests/fixtures/task-contract-linter/negative/ui-missing-contract-task.md": "TASK_LINT_FAIL",
    "tests/fixtures/task-contract-linter/negative/task-todo-fields-needs-review.md": "TASK_LINT_NEEDS_REVIEW",
    "tests/fixtures/task-contract-linter/negative/queue-ready-with-blockers.json": "TASK_LINT_FAIL",
    "tests/fixtures/task-contract-linter/negative/queue-execution-authority-field.json": "TASK_LINT_FAIL",
    "tests/fixtures/task-contract-linter/negative/queue-invalid-created-at.json": "TASK_LINT_FAIL",
    "tests/fixtures/task-contract-linter/negative/queue-invalid-entry-id.json": "TASK_LINT_FAIL",
    "tests/fixtures/task-contract-linter/negative/queue-unicode-entry-id.json": "TASK_LINT_FAIL",
}


def ts_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def run_cmd(argv: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(argv, cwd=str(cwd), capture_output=True, text=True, check=False)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="M44 decomposition smoke")
    p.add_argument("--json", action="store_true", dest="json_mode", help="--json output must be written to stdout")
    return p.parse_args()


def add_step(steps: list[dict], name: str, result: str, token: str, exit_code: int, details: str) -> None:
    steps.append({"name": name, "result": result, "token": token, "exit_code": exit_code, "details": details})


def main() -> int:
    if sys.version_info < (3, 10):
        payload = {
            "result": M44_SMOKE_FAILED,
            "exit_code": 2,
            "steps": [{"name": "python_runtime", "result": "failed", "token": M44_SMOKE_FAILED, "exit_code": 2, "details": "Python runtime below 3.10 is M44_SMOKE_FAILED."}],
            "issue_count": 1,
            "failed_steps": ["python_runtime"],
            "infrastructure_failures": ["python_runtime"],
            "non_approval_warning": "Smoke PASS is not approval and does not authorize execution.",
            "timestamp": ts_utc(),
        }
        print(json.dumps(payload, ensure_ascii=False))
        return 2

    args = parse_args()
    repo_root = Path(__file__).resolve().parent.parent
    steps: list[dict] = []
    failed_steps: list[str] = []
    infra_failures: list[str] = []

    required_files = [
        "scripts/generate-tasks-from-spec.py",
        "scripts/generate-tasks-from-ux.py",
        "scripts/build-task-dependency-map.py",
        "scripts/lint-task-contract.py",
        "schemas/task-contract-v2.schema.json",
        "schemas/task-queue-entry.schema.json",
        "docs/TASK-CONTRACT-QUEUE-LINTER.md",
    ]
    fixture_files = list(POSITIVE_MAP.keys()) + list(NEGATIVE_MAP.keys())

    missing = [p for p in required_files if not (repo_root / p).exists()]
    if missing:
        add_step(steps, "preconditions_upstream", "failed", "PRECONDITION_FAILED_M44_10_UPSTREAM_MISSING", 2, "; ".join(missing))
        failed_steps.append("preconditions_upstream")
        infra_failures.append("preconditions_upstream")
    else:
        add_step(steps, "preconditions_upstream", "pass", "OK", 0, "all upstream artifacts present")

    missing_fixtures = [p for p in fixture_files if not (repo_root / p).exists()]
    if missing_fixtures:
        add_step(steps, "preconditions_44_9_fixtures", "failed", "PRECONDITION_FAILED_M44_10_44_9_FIXTURES_MISSING", 2, "; ".join(missing_fixtures))
        failed_steps.append("preconditions_44_9_fixtures")
        infra_failures.append("preconditions_44_9_fixtures")
    else:
        add_step(steps, "preconditions_44_9_fixtures", "pass", "OK", 0, "all 44.9 fixtures present")

    cli_checks = [
        ([sys.executable, "scripts/generate-tasks-from-spec.py", "--help"], "--dry-run"),
        ([sys.executable, "scripts/generate-tasks-from-spec.py", "--help"], "--out"),
        ([sys.executable, "scripts/generate-tasks-from-spec.py", "--help"], "--spec"),
        ([sys.executable, "scripts/generate-tasks-from-ux.py", "--help"], "--dry-run"),
        ([sys.executable, "scripts/generate-tasks-from-ux.py", "--help"], "--out"),
        ([sys.executable, "scripts/generate-tasks-from-ux.py", "--help"], "--ux"),
        ([sys.executable, "scripts/build-task-dependency-map.py", "--help"], "--input"),
        ([sys.executable, "scripts/build-task-dependency-map.py", "--help"], "--out"),
        ([sys.executable, "scripts/build-task-dependency-map.py", "--help"], "--write"),
        ([sys.executable, "scripts/lint-task-contract.py", "--help"], "--target"),
        ([sys.executable, "scripts/lint-task-contract.py", "--help"], "--kind"),
        ([sys.executable, "scripts/lint-task-contract.py", "--help"], "--json"),
    ]

    cli_bad: list[str] = []
    for cmd, token in cli_checks:
        cp = run_cmd(cmd, repo_root)
        if cp.returncode != 0 or token not in (cp.stdout + cp.stderr):
            cli_bad.append(" ".join(cmd) + f" token={token}")

    if cli_bad:
        add_step(steps, "preconditions_cli", "failed", "PRECONDITION_FAILED_M44_10_CLI_INCOMPATIBLE", 2, " | ".join(cli_bad))
        failed_steps.append("preconditions_cli")
        infra_failures.append("preconditions_cli")
    else:
        add_step(steps, "preconditions_cli", "pass", "OK", 0, "cli compatibility checks are normative for M44.10")

    with tempfile.TemporaryDirectory() as td:
        tdir = Path(td)

        # canonical lint token precheck
        lint_json = tdir / "lint-token-check.json"
        cp = run_cmd(
            [
                sys.executable,
                "scripts/lint-task-contract.py",
                "--target",
                "tests/fixtures/task-contract-linter/positive/valid-task-contract.md",
                "--kind",
                "task",
                "--json",
            ],
            repo_root,
        )
        lint_json.write_text(cp.stdout, encoding="utf-8")
        token_ok = False
        json_ok = True
        try:
            payload = json.loads(cp.stdout)
            token_ok = payload.get("result") == "TASK_LINT_PASS" and "Lint PASS is not approval and does not authorize execution" in str(payload.get("non_approval_warning", ""))
        except Exception:
            json_ok = False

        if cp.returncode != 0 or (not json_ok) or (not token_ok):
            add_step(
                steps,
                "preconditions_lint_token",
                "failed",
                "PRECONDITION_FAILED_M44_10_LINT_TOKEN_INCOMPATIBLE",
                2,
                f"json_ok={json_ok}; token_ok={token_ok}; rc={cp.returncode}",
            )
            failed_steps.append("preconditions_lint_token")
            infra_failures.append("preconditions_lint_token")
        else:
            add_step(steps, "preconditions_lint_token", "pass", "TASK_LINT_PASS", 0, "canonical lint token vocabulary compatible")

        # Stop if infrastructure preconditions failed
        if infra_failures:
            result = M44_SMOKE_FAILED
            code = 2
        else:
            # Spec generator dry-run
            cp_spec = run_cmd(
                [
                    sys.executable,
                    "scripts/generate-tasks-from-spec.py",
                    "--spec",
                    "tests/fixtures/spec-to-task/positive/approved-spec.md",
                    "--dry-run",
                ],
                repo_root,
            )
            if cp_spec.returncode == 0 and "SPEC_TO_TASK_DRY_RUN_OK" in cp_spec.stdout:
                add_step(steps, "spec_generator_smoke", "pass", "SPEC_TO_TASK_DRY_RUN_OK", 0, "spec dry-run ok")
            else:
                add_step(steps, "spec_generator_smoke", "fail", M44_SMOKE_FAIL, cp_spec.returncode, "spec generator dry-run failed")
                failed_steps.append("spec_generator_smoke")

            # UX generator dry-run
            cp_ux = run_cmd(
                [
                    sys.executable,
                    "scripts/generate-tasks-from-ux.py",
                    "--ux",
                    "tests/fixtures/ux-to-task/positive/approved-ux-with-ui-contract.md",
                    "--dry-run",
                ],
                repo_root,
            )
            if cp_ux.returncode == 0 and "UX_TO_TASK_DRY_RUN_OK" in cp_ux.stdout:
                add_step(steps, "ux_generator_smoke", "pass", "UX_TO_TASK_DRY_RUN_OK", 0, "ux dry-run ok")
            else:
                add_step(steps, "ux_generator_smoke", "fail", M44_SMOKE_FAIL, cp_ux.returncode, "ux generator dry-run failed")
                failed_steps.append("ux_generator_smoke")

            # dependency map temp output
            dep_out = tdir / "dep"
            cp_dep = run_cmd(
                [
                    sys.executable,
                    "scripts/build-task-dependency-map.py",
                    "--input",
                    "tests/fixtures/task-dependency-map/positive/valid-chain",
                    "--out",
                    str(dep_out),
                    "--write",
                ],
                repo_root,
            )
            if cp_dep.returncode == 0 and (dep_out / "dependency-map.md").exists():
                add_step(steps, "dependency_map_smoke", "pass", "TASK_DEPENDENCY_MAP_WRITE_OK", 0, "dependency map built into temp dir")
            else:
                add_step(steps, "dependency_map_smoke", "fail", M44_SMOKE_FAIL, cp_dep.returncode, "dependency map smoke failed")
                failed_steps.append("dependency_map_smoke")

            # linter positive explicit kind
            for path, token in POSITIVE_MAP.items():
                kind = "task" if path.endswith(".md") else "queue"
                cp = run_cmd([sys.executable, "scripts/lint-task-contract.py", "--target", path, "--kind", kind, "--json"], repo_root)
                step_name = f"lint_positive::{Path(path).name}"
                if cp.returncode == 2:
                    add_step(steps, step_name, "failed", "TASK_LINT_FAILED", 2, "linter infrastructure failure")
                    failed_steps.append(step_name)
                    infra_failures.append(step_name)
                    continue
                try:
                    payload = json.loads(cp.stdout)
                    got = payload.get("result")
                except Exception:
                    add_step(steps, step_name, "failed", "M44_SMOKE_FAILED", 2, "Malformed JSON output is M44_SMOKE_FAILED")
                    failed_steps.append(step_name)
                    infra_failures.append(step_name)
                    continue
                if cp.returncode == 0 and got == token:
                    add_step(steps, step_name, "pass", got, 0, "positive fixture token ok")
                else:
                    add_step(steps, step_name, "fail", got or M44_SMOKE_FAIL, cp.returncode, "positive fixture token mismatch")
                    failed_steps.append(step_name)

            # linter negative explicit kind
            for path, token in NEGATIVE_MAP.items():
                kind = "task" if path.endswith(".md") else "queue"
                cp = run_cmd([sys.executable, "scripts/lint-task-contract.py", "--target", path, "--kind", kind, "--json"], repo_root)
                step_name = f"lint_negative::{Path(path).name}"
                if cp.returncode == 2:
                    add_step(steps, step_name, "failed", "TASK_LINT_FAILED", 2, "TASK_LINT_FAILED is not an acceptable substitute for TASK_LINT_FAIL")
                    failed_steps.append(step_name)
                    infra_failures.append(step_name)
                    continue
                try:
                    payload = json.loads(cp.stdout)
                    got = payload.get("result")
                except Exception:
                    add_step(steps, step_name, "failed", "M44_SMOKE_FAILED", 2, "Malformed JSON output is M44_SMOKE_FAILED")
                    failed_steps.append(step_name)
                    infra_failures.append(step_name)
                    continue
                if cp.returncode != 0 and got == token:
                    add_step(steps, step_name, "pass", got, cp.returncode, "negative fixture token ok")
                else:
                    add_step(steps, step_name, "fail", got or M44_SMOKE_FAIL, cp.returncode, "negative fixture token mismatch or unexpected PASS")
                    failed_steps.append(step_name)

            if infra_failures:
                result = M44_SMOKE_FAILED
                code = 2
            elif failed_steps:
                result = M44_SMOKE_FAIL
                code = 1
            else:
                result = M44_SMOKE_PASS
                code = 0

    issue_count = len(failed_steps) + len(infra_failures)
    payload = {
        "result": result,
        "exit_code": code,
        "steps": steps if steps else [{"name": "no_steps", "result": "failed", "token": M44_SMOKE_FAILED, "exit_code": 2, "details": "steps must contain at least one step entry."}],
        "issue_count": issue_count,
        "failed_steps": failed_steps,
        "infrastructure_failures": infra_failures,
        "non_approval_warning": "Smoke PASS is not approval and does not authorize execution.",
        "timestamp": ts_utc(),
    }

    if args.json_mode:
        # --json output must be written to stdout.
        print(json.dumps(payload, ensure_ascii=False))
    else:
        print(f"Result: {result}")
        print(f"Exit code: {code}")
        for s in payload["steps"]:
            print(f"- {s['name']}: {s['result']} token={s['token']} rc={s['exit_code']}")
        print("Smoke PASS is not approval and does not authorize execution.")

    return code


if __name__ == "__main__":
    raise SystemExit(main())
