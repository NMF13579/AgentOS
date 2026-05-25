#!/usr/bin/env python3
"""M56 execution readiness fixture runner."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

TIMEOUT_SECONDS = 30

RESULT_PASS = "M56_FIXTURE_RUNNER_PASS"
RESULT_FAIL = "M56_FIXTURE_RUNNER_FAIL"
RESULT_BLOCKED = "M56_FIXTURE_RUNNER_BLOCKED"

CASE_PASS = "CASE_PASS"
CASE_FAIL = "CASE_FAIL"
CASE_BLOCKED = "CASE_BLOCKED"

NON_AUTHORITY_MARKERS = [
    "M56 fixture runner is test harness only.",
    "M56 fixture runner does not authorize execution.",
    "M56 fixture runner does not start execution.",
    "M56 fixture runner does not create approval records.",
    "M56 fixture runner does not authorize lifecycle mutation.",
    "M56 fixture runner does not authorize M57.",
    "M56 fixture runner does not start M57.",
]

EXPLAIN_LINES = [
    "M56 fixture runner validates positive and negative readiness fixtures.",
    "The fixture runner may invoke the M56 readiness CLI against fixtures only.",
    "The fixture runner uses TIMEOUT_SECONDS=30 for each CLI invocation.",
    "The fixture runner treats subprocess.TimeoutExpired as CASE_BLOCKED.",
    "The fixture runner rejects any case path that resolves outside the fixture root.",
    "The fixture runner rejects paths that point to tasks/, approvals/, or generated/.",
    "Default mode executes all configured cases and reports all mismatches.",
    "Strict mode stops on the first CASE_FAIL or CASE_BLOCKED.",
    "In strict mode, the cases array contains only executed cases up to and including the first CASE_FAIL or CASE_BLOCKED.",
    "The fixture runner does not execute active tasks.",
    "The fixture runner does not run validation commands from active-task files.",
    "The fixture runner does not authorize execution.",
    "The fixture runner does not authorize lifecycle mutation.",
    "The fixture runner does not authorize M57.",
    "The fixture runner does not start M57.",
]

REQUIRED_POSITIVE_README_MARKER = "These fixtures are positive M56 execution readiness test data only."
REQUIRED_NEGATIVE_README_MARKER = "These fixtures are negative M56 execution readiness test data only."

REQUIRED_CLI_MARKERS = [
    "M56 execution readiness CLI is read-only.",
    "The CLI does not execute the active task.",
    "The CLI does not run validation commands.",
    "The CLI does not authorize execution.",
    "The CLI does not authorize lifecycle mutation.",
    "The CLI does not authorize M57.",
    "The CLI does not start M57.",
]

REQUIRED_FIXTURE_RUNNER_DOC_MARKERS = [
    "This document defines the M56 execution readiness fixture runner.",
    "The fixture runner validates positive and negative readiness fixtures only.",
    "The fixture runner may invoke the M56 readiness CLI against fixtures only.",
    "The fixture runner uses TIMEOUT_SECONDS=30 for each CLI invocation.",
    "The fixture runner treats subprocess.TimeoutExpired as CASE_BLOCKED.",
    "Timeout handling is contractually required but not directly exercised by the fixture matrix in Task 56.8 validation.",
    "Fixture runner PASS is not execution authorization.",
    "Fixture runner PASS is not evidence approval.",
    "Fixture runner PASS does not start M57.",
]

CASE_DEFINITIONS = [
    {
        "case_id": "positive_clean_confirmed",
        "input": "positive/valid-execution-readiness-input.json",
        "preconditions": "positive/valid-execution-preconditions-pass.json",
        "active_task": "positive/valid-active-task-ready.md",
        "expected_result": "EXECUTION_READINESS_CONFIRMED",
        "expected_exit_code": 0,
    },
    {
        "case_id": "positive_input_limitations",
        "input": "positive/valid-execution-readiness-input-with-limitations.json",
        "preconditions": "positive/valid-execution-preconditions-pass.json",
        "active_task": "positive/valid-active-task-ready.md",
        "expected_result": "EXECUTION_READINESS_CONFIRMED_WITH_LIMITATIONS",
        "expected_exit_code": 0,
    },
    {
        "case_id": "positive_markdown_input_with_warning_preconditions",
        "input": "positive/valid-execution-readiness-input-markdown.md",
        "preconditions": "positive/valid-execution-preconditions-pass-with-warnings.json",
        "active_task": "positive/valid-active-task-ready.md",
        "expected_result": "EXECUTION_READINESS_CONFIRMED_WITH_LIMITATIONS",
        "expected_exit_code": 0,
    },
    {
        "case_id": "negative_missing_required_input_key",
        "input": "negative/missing-required-input-key.json",
        "preconditions": "positive/valid-execution-preconditions-pass.json",
        "active_task": "positive/valid-active-task-ready.md",
        "expected_result": "EXECUTION_READINESS_BLOCKED",
        "expected_exit_code": 2,
    },
    {
        "case_id": "negative_unknown_input_status",
        "input": "negative/unknown-input-status.json",
        "preconditions": "positive/valid-execution-preconditions-pass.json",
        "active_task": "positive/valid-active-task-ready.md",
        "expected_result": "EXECUTION_READINESS_BLOCKED",
        "expected_exit_code": 2,
    },
    {
        "case_id": "negative_empty_traceability",
        "input": "negative/empty-traceability.json",
        "preconditions": "positive/valid-execution-preconditions-pass.json",
        "active_task": "positive/valid-active-task-ready.md",
        "expected_result": "EXECUTION_READINESS_BLOCKED",
        "expected_exit_code": 2,
    },
    {
        "case_id": "negative_source_path_mismatch",
        "input": "positive/valid-execution-readiness-input.json",
        "preconditions": "negative/source-path-mismatch.json",
        "active_task": "positive/valid-active-task-ready.md",
        "expected_result": "EXECUTION_READINESS_BLOCKED",
        "expected_exit_code": 2,
    },
    {
        "case_id": "negative_unsafe_authorization_claim",
        "input": "negative/unsafe-authorization-claim.json",
        "preconditions": "positive/valid-execution-preconditions-pass.json",
        "active_task": "positive/valid-active-task-ready.md",
        "expected_result": "EXECUTION_READINESS_BLOCKED",
        "expected_exit_code": 2,
    },
    {
        "case_id": "negative_performed_action_violation",
        "input": "positive/valid-execution-readiness-input.json",
        "preconditions": "negative/performed-action-violation.json",
        "active_task": "positive/valid-active-task-ready.md",
        "expected_result": "EXECUTION_READINESS_BLOCKED",
        "expected_exit_code": 2,
    },
    {
        "case_id": "negative_preconditions_blocked",
        "input": "positive/valid-execution-readiness-input.json",
        "preconditions": "negative/preconditions-blocked.json",
        "active_task": "positive/valid-active-task-ready.md",
        "expected_result": "EXECUTION_READINESS_BLOCKED",
        "expected_exit_code": 2,
    },
    {
        "case_id": "negative_active_task_missing_validation",
        "input": "positive/valid-execution-readiness-input.json",
        "preconditions": "positive/valid-execution-preconditions-pass.json",
        "active_task": "negative/active-task-missing-validation.md",
        "expected_result": "EXECUTION_READINESS_NOT_CONFIRMED",
        "expected_exit_code": 1,
    },
    {
        "case_id": "negative_malformed_markdown_multiple_json_blocks",
        "input": "negative/malformed-markdown-multiple-json-blocks.md",
        "preconditions": "positive/valid-execution-preconditions-pass.json",
        "active_task": "positive/valid-active-task-ready.md",
        "expected_result": "EXECUTION_READINESS_BLOCKED",
        "expected_exit_code": 2,
    },
]


class RunnerError(Exception):
    pass


def explain() -> int:
    sys.stdout.write("\n".join(EXPLAIN_LINES) + "\n")
    return 0


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="check-m56-execution-readiness-fixtures")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--explain", action="store_true")
    parser.add_argument("--fi" "xtures-root", default="tests/fixtures/execution-readiness")
    parser.add_argument("--readiness-cli", default="scripts/check-execution-readiness.py")
    return parser.parse_args(argv)


def load_text(path: Path) -> str:
    if not path.exists():
        raise RunnerError(f"missing file: {path}")
    return path.read_text(encoding="utf-8")


def validate_contains(text: str, markers: list[str], label: str) -> None:
    missing = [marker for marker in markers if marker not in text]
    if missing:
        raise RunnerError(f"{label} missing markers: {', '.join(missing)}")


def resolve_case_path(root: Path, relative: str) -> Path:
    root_resolved = root.resolve()
    resolved = (root_resolved / relative).resolve()
    try:
        relative_path = resolved.relative_to(root_resolved)
    except ValueError as exc:
        raise RunnerError(f"case path resolves outside fixture root: {relative}") from exc
    if relative_path.parts and relative_path.parts[0] in {"tasks", "approvals", "generated"}:
        raise RunnerError(f"forbidden case path detected: {relative}")
    return resolved


def dependency_validation(fixtures_root: Path, readiness_cli: Path, runner_source: Path) -> None:
    required_paths = [
        readiness_cli,
        fixtures_root / "positive" / "README.md",
        fixtures_root / "positive" / "valid-execution-readiness-input.json",
        fixtures_root / "positive" / "valid-execution-readiness-input-with-limitations.json",
        fixtures_root / "positive" / "valid-execution-readiness-input-markdown.md",
        fixtures_root / "positive" / "valid-execution-preconditions-pass.json",
        fixtures_root / "positive" / "valid-execution-preconditions-pass-with-warnings.json",
        fixtures_root / "positive" / "valid-active-task-ready.md",
        fixtures_root / "positive" / "valid-result-confirmed.json",
        fixtures_root / "negative" / "README.md",
        fixtures_root / "negative" / "missing-required-input-key.json",
        fixtures_root / "negative" / "unknown-input-status.json",
        fixtures_root / "negative" / "empty-traceability.json",
        fixtures_root / "negative" / "source-path-mismatch.json",
        fixtures_root / "negative" / "unsafe-authorization-claim.json",
        fixtures_root / "negative" / "performed-action-violation.json",
        fixtures_root / "negative" / "preconditions-blocked.json",
        fixtures_root / "negative" / "active-task-missing-validation.md",
        fixtures_root / "negative" / "malformed-markdown-multiple-json-blocks.md",
        runner_source,
    ]
    for path in required_paths:
        if not path.exists():
            raise RunnerError(f"missing dependency: {path}")

    cli_text = load_text(readiness_cli)
    validate_contains(cli_text, REQUIRED_CLI_MARKERS, "CLI documentation")

    positive_readme = load_text(fixtures_root / "positive" / "README.md")
    negative_readme = load_text(fixtures_root / "negative" / "README.md")
    validate_contains(positive_readme, [REQUIRED_POSITIVE_README_MARKER], "positive fixtures README")
    validate_contains(negative_readme, [REQUIRED_NEGATIVE_README_MARKER], "negative fixtures README")

    runner_doc = load_text(Path("docs/TASK-EXECUTION-READINESS-FIXTURE-RUNNER.md"))
    validate_contains(runner_doc, REQUIRED_FIXTURE_RUNNER_DOC_MARKERS, "fixture runner documentation")


def run_cli_case(readiness_cli: Path, case: dict[str, str], fixtures_root: Path) -> dict[str, object]:
    input_path = resolve_case_path(fixtures_root, case["input"])
    preconditions_path = resolve_case_path(fixtures_root, case["preconditions"])
    active_task_path = resolve_case_path(fixtures_root, case["active_task"])

    for path in (input_path, preconditions_path, active_task_path):
        if not path.exists():
            return {
                "case_id": case["case_id"],
                "expected_result": case["expected_result"],
                "expected_exit_code": case["expected_exit_code"],
                "actual_result": None,
                "actual_exit_code": None,
                "status": CASE_BLOCKED,
                "timed_out": False,
                "input": str(input_path),
                "preconditions": str(preconditions_path),
                "active_task": str(active_task_path),
                "blockers": [f"missing case file: {path}"],
            }

    command = [
        sys.executable,
        str(readiness_cli),
        "--input",
        str(input_path),
        "--preconditions",
        str(preconditions_path),
        "--active-task",
        str(active_task_path),
        "--json",
    ]

    try:
        completed = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired:
        return {
            "case_id": case["case_id"],
            "expected_result": case["expected_result"],
            "expected_exit_code": case["expected_exit_code"],
            "actual_result": None,
            "actual_exit_code": None,
            "status": CASE_BLOCKED,
            "timed_out": True,
            "input": str(input_path),
            "preconditions": str(preconditions_path),
            "active_task": str(active_task_path),
            "blockers": [f"timeout after {TIMEOUT_SECONDS} seconds"],
        }

    try:
        payload = json.loads(completed.stdout)
        root = payload["execution_readiness_result"]
        actual_result = root["result"]
        actual_exit_code = root["exit_code"]
    except (json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
        return {
            "case_id": case["case_id"],
            "expected_result": case["expected_result"],
            "expected_exit_code": case["expected_exit_code"],
            "actual_result": None,
            "actual_exit_code": None,
            "status": CASE_BLOCKED,
            "timed_out": False,
            "input": str(input_path),
            "preconditions": str(preconditions_path),
            "active_task": str(active_task_path),
            "blockers": [f"malformed CLI JSON output: {exc}"],
        }

    if not isinstance(actual_result, str) or not isinstance(actual_exit_code, int):
        return {
            "case_id": case["case_id"],
            "expected_result": case["expected_result"],
            "expected_exit_code": case["expected_exit_code"],
            "actual_result": actual_result,
            "actual_exit_code": actual_exit_code,
            "status": CASE_BLOCKED,
            "timed_out": False,
            "input": str(input_path),
            "preconditions": str(preconditions_path),
            "active_task": str(active_task_path),
            "blockers": ["malformed CLI JSON output: wrong types"],
        }

    if actual_result != case["expected_result"] or actual_exit_code != case["expected_exit_code"]:
        blockers = []
        if actual_result != case["expected_result"]:
            blockers.append(
                f"result mismatch: expected {case['expected_result']} got {actual_result}"
            )
        if actual_exit_code != case["expected_exit_code"]:
            blockers.append(
                f"exit code mismatch: expected {case['expected_exit_code']} got {actual_exit_code}"
            )
        return {
            "case_id": case["case_id"],
            "expected_result": case["expected_result"],
            "expected_exit_code": case["expected_exit_code"],
            "actual_result": actual_result,
            "actual_exit_code": actual_exit_code,
            "status": CASE_FAIL,
            "timed_out": False,
            "input": str(input_path),
            "preconditions": str(preconditions_path),
            "active_task": str(active_task_path),
            "blockers": blockers,
        }

    return {
        "case_id": case["case_id"],
        "expected_result": case["expected_result"],
        "expected_exit_code": case["expected_exit_code"],
        "actual_result": actual_result,
        "actual_exit_code": actual_exit_code,
        "status": CASE_PASS,
        "timed_out": False,
        "input": str(input_path),
        "preconditions": str(preconditions_path),
        "active_task": str(active_task_path),
        "blockers": [],
    }


def build_summary(
    result: str,
    exit_code: int,
    strict: bool,
    fixtures_root: Path,
    readiness_cli: Path,
    cases: list[dict[str, object]],
) -> dict[str, object]:
    passed_cases = sum(1 for case in cases if case["status"] == CASE_PASS)
    failed_cases = sum(1 for case in cases if case["status"] == CASE_FAIL)
    blocked_cases = sum(1 for case in cases if case["status"] == CASE_BLOCKED)
    timed_out_cases = sum(1 for case in cases if case["timed_out"] is True)
    positive_cases_passed = sum(
        1 for case in cases if case["status"] == CASE_PASS and str(case["case_id"]).startswith("positive_")
    )
    negative_cases_passed = sum(
        1 for case in cases if case["status"] == CASE_PASS and str(case["case_id"]).startswith("negative_")
    )

    return {
        "execution_readiness_fixture_runner_result": {
            "result": result,
            "exit_code": exit_code,
            "total_cases": len(cases),
            "passed_cases": passed_cases,
            "failed_cases": failed_cases,
            "blocked_cases": blocked_cases,
            "fixture_root": str(fixtures_root),
            "readiness_cli": str(readiness_cli),
            "strict": strict,
            "cases": cases,
            "boundary_flags": {
                "fixture_runner_only": True,
                "execution_authorized": False,
                "execution_started": False,
                "approval_created": False,
                "lifecycle_mutation_authorized": False,
                "m57_authorized": False,
                "m57_started": False,
            },
            "non_authority_markers": NON_AUTHORITY_MARKERS[:],
            "timed_out_cases": timed_out_cases,
            "positive_cases_passed": positive_cases_passed,
            "negative_cases_passed": negative_cases_passed,
        }
    }


def render_human(summary: dict[str, object]) -> str:
    root = summary["execution_readiness_fixture_runner_result"]
    lines = [
        f"M56_FIXTURE_RUNNER_RESULT: {root['result']}",
        f"EXIT_CODE: {root['exit_code']}",
        f"TOTAL_CASES: {root['total_cases']}",
        f"PASSED_CASES: {root['passed_cases']}",
        f"FAILED_CASES: {root['failed_cases']}",
        f"BLOCKED_CASES: {root['blocked_cases']}",
        f"STRICT: {root['strict']}",
        f"NON_AUTHORITY: {', '.join(root['non_authority_markers'])}",
        "M56 fixture runner is test harness only.",
    ]
    return "\n".join(lines) + "\n"


def run_runner(args: argparse.Namespace) -> tuple[dict[str, object], int]:
    fixtures_root = Path(args.fixtures_root)
    readiness_cli = Path(args.readiness_cli)
    runner_source = Path(__file__)

    try:
        dependency_validation(fixtures_root, readiness_cli, runner_source)
    except RunnerError as exc:
        summary = build_summary(
            RESULT_BLOCKED,
            2,
            args.strict,
            fixtures_root,
            readiness_cli,
            [],
        )
        summary["execution_readiness_fixture_runner_result"]["cases"] = []
        root = summary["execution_readiness_fixture_runner_result"]
        root["blocked_cases"] = 0
        root["failed_cases"] = 0
        root["passed_cases"] = 0
        root["total_cases"] = 0
        root["non_authority_markers"] = NON_AUTHORITY_MARKERS[:]
        root["boundary_flags"]["fixture_runner_only"] = True
        root["blockers"] = [str(exc)] if "blockers" not in root else []
        return summary, 2

    if not readiness_cli.exists():
        summary = build_summary(RESULT_BLOCKED, 2, args.strict, fixtures_root, readiness_cli, [])
        summary["execution_readiness_fixture_runner_result"]["blockers"] = [f"missing dependency: {readiness_cli}"]
        return summary, 2

    cases_results: list[dict[str, object]] = []
    blocked_seen = False
    fail_seen = False

    for case in CASE_DEFINITIONS:
        case_result = run_cli_case(readiness_cli, case, fixtures_root)
        cases_results.append(case_result)

        if case_result["status"] == CASE_BLOCKED:
            blocked_seen = True
            if args.strict:
                break
        elif case_result["status"] == CASE_FAIL:
            fail_seen = True
            if args.strict:
                break

    if blocked_seen:
        result = RESULT_BLOCKED
        exit_code = 2
    elif fail_seen:
        result = RESULT_FAIL
        exit_code = 1
    else:
        result = RESULT_PASS
        exit_code = 0

    summary = build_summary(result, exit_code, args.strict, fixtures_root, readiness_cli, cases_results)
    root = summary["execution_readiness_fixture_runner_result"]
    root["blocked_cases"] = sum(1 for case in cases_results if case["status"] == CASE_BLOCKED)
    root["failed_cases"] = sum(1 for case in cases_results if case["status"] == CASE_FAIL)
    root["passed_cases"] = sum(1 for case in cases_results if case["status"] == CASE_PASS)
    root["total_cases"] = len(cases_results)
    return summary, exit_code


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    if args.explain:
        return explain()

    summary, exit_code = run_runner(args)

    if args.json:
        sys.stdout.write(json.dumps(summary, indent=2) + "\n")
    else:
        sys.stdout.write(render_human(summary))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
