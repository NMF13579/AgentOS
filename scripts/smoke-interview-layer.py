#!/usr/bin/env python3
"""M45 interview layer smoke runner.

All expected checker output, including RESULT, must be written to stdout.
parse checker RESULT from the first stdout line that starts with "RESULT:"
treat missing RESULT line as INTERVIEW_LAYER_SMOKE_CHECK_FAILED
do not assume RESULT is the first stdout line
scan all checker stdout lines and use the first line that starts with "RESULT:"
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

SMOKE_PASS = "INTERVIEW_LAYER_SMOKE_PASS"
SMOKE_FAIL = "INTERVIEW_LAYER_SMOKE_FAIL"
SMOKE_CHECK_FAILED = "INTERVIEW_LAYER_SMOKE_CHECK_FAILED"

EXIT_MAP = {
    SMOKE_PASS: 0,
    SMOKE_FAIL: 1,
    SMOKE_CHECK_FAILED: 2,
}


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Smoke test for M45 interview layer")
    p.add_argument("--json", action="store_true", help="Output JSON summary")
    p.add_argument("--explain", action="store_true", help="Output extra explanation lines")
    p.add_argument(
        "--fixtures-root",
        default="tests/fixtures/problem-interview",
        help="Root directory for smoke fixtures",
    )
    return p.parse_args()


def parse_result_from_stdout(stdout_text: str) -> str | None:
    for line in stdout_text.splitlines():
        if line.startswith("RESULT:"):
            return line.split(":", 1)[1].strip()
    return None


def run_case(checker: Path, fixture: Path, expected_result: str, expected_exit: int) -> dict:
    proc = subprocess.run(
        [sys.executable, str(checker), str(fixture)],
        capture_output=True,
        text=True,
    )

    parsed_result = parse_result_from_stdout(proc.stdout)

    case = {
        "case": fixture.name,
        "fixture": str(fixture),
        "expected_result": expected_result,
        "actual_result": parsed_result if parsed_result is not None else "MISSING_RESULT_LINE",
        "expected_exit": expected_exit,
        "actual_exit": proc.returncode,
        "case_result": "PASS",
        "runner_error": "",
    }

    if parsed_result is None:
        case["case_result"] = "CHECK_FAILED"
        case["runner_error"] = "Missing RESULT line in checker stdout"
        return case

    if proc.returncode != expected_exit or parsed_result != expected_result:
        case["case_result"] = "FAIL"

    return case


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parent.parent
    checker = repo_root / "scripts" / "check-interview-completeness.py"
    fixtures_root = repo_root / args.fixtures_root

    if not checker.exists() or not checker.is_file():
        payload = {
            "smoke_result": SMOKE_CHECK_FAILED,
            "total_cases": 4,
            "passed_cases": 0,
            "failed_cases": 4,
            "cases": [],
            "error": "Missing checker script",
        }
        if args.json:
            print(json.dumps(payload, ensure_ascii=False, indent=2))
        else:
            print(f"SMOKE_RESULT: {SMOKE_CHECK_FAILED}")
            print("TOTAL_CASES: 4")
            print("PASSED_CASES: 0")
            print("FAILED_CASES: 4")
        return EXIT_MAP[SMOKE_CHECK_FAILED]

    cases_def = [
        (
            fixtures_root / "positive" / "complete-interview.json",
            "COMPLETENESS_COMPLETE",
            0,
        ),
        (
            fixtures_root / "negative" / "missing-user.json",
            "COMPLETENESS_NEEDS_CLARIFICATION",
            1,
        ),
        (
            fixtures_root / "negative" / "missing-success-criteria.json",
            "COMPLETENESS_NEEDS_CLARIFICATION",
            1,
        ),
        (
            fixtures_root / "negative" / "unknowns-without-followup.json",
            "COMPLETENESS_INCOMPLETE",
            1,
        ),
    ]

    case_results = []
    has_check_failed = False

    for fixture, expected_result, expected_exit in cases_def:
        if not fixture.exists() or not fixture.is_file():
            case_results.append(
                {
                    "case": fixture.name,
                    "fixture": str(fixture),
                    "expected_result": expected_result,
                    "actual_result": "FIXTURE_MISSING",
                    "expected_exit": expected_exit,
                    "actual_exit": 2,
                    "case_result": "CHECK_FAILED",
                    "runner_error": "Fixture not found",
                }
            )
            has_check_failed = True
            continue

        case = run_case(checker, fixture, expected_result, expected_exit)
        if case["case_result"] == "CHECK_FAILED":
            has_check_failed = True
        case_results.append(case)

    total_cases = len(case_results)
    passed_cases = sum(1 for c in case_results if c["case_result"] == "PASS")
    failed_cases = total_cases - passed_cases

    if has_check_failed:
        smoke_result = SMOKE_CHECK_FAILED
    elif failed_cases == 0:
        smoke_result = SMOKE_PASS
    else:
        smoke_result = SMOKE_FAIL

    if args.json:
        payload = {
            "smoke_result": smoke_result,
            "total_cases": total_cases,
            "passed_cases": passed_cases,
            "failed_cases": failed_cases,
            "cases": case_results,
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(f"SMOKE_RESULT: {smoke_result}")
        print(f"TOTAL_CASES: {total_cases}")
        print(f"PASSED_CASES: {passed_cases}")
        print(f"FAILED_CASES: {failed_cases}")

        for c in case_results:
            print(f"CASE: {c['case']}")
            print(f"EXPECTED_RESULT: {c['expected_result']}")
            print(f"ACTUAL_RESULT: {c['actual_result']}")
            print(f"EXPECTED_EXIT: {c['expected_exit']}")
            print(f"ACTUAL_EXIT: {c['actual_exit']}")
            if c["case_result"] == "PASS":
                print("CASE_RESULT: PASS")
            else:
                print("CASE_RESULT: FAIL")

        if args.explain:
            print("EXPLAIN:")
            print("- Smoke result values are smoke outcomes, not interview_status values.")
            print("- Smoke PASS is not approval.")
            print("- Smoke PASS does not authorize implementation.")

    return EXIT_MAP[smoke_result]


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"UNEXPECTED_INTERNAL_ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2)
