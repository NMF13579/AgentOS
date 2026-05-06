#!/usr/bin/env python3
"""
test-pre-merge-corridor-fixtures.py
M26 Pre-Merge Corridor Smoke Fixture Runner
Task: 26.11.1

READ-ONLY. This script does not modify files, commit, push, self-heal,
or rewrite fixtures.

Runs scripts/audit-pre-merge-corridor.py against each fixture directory
and compares actual result to expected-result.txt.
"""

import json
import os
import subprocess
import sys

FIXTURE_ROOT = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "tests", "fixtures", "pre-merge-corridor",
)

AUDIT_SCRIPT = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "audit-pre-merge-corridor.py",
)

EXPECTED_RESULT_FILENAME = "expected-result.txt"
RUNNER_ERROR = "RUNNER_ERROR"


def find_fixtures(root: str) -> list[str]:
    """Return all fixture dirs that contain expected-result.txt."""
    fixtures = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames.sort()
        if EXPECTED_RESULT_FILENAME in filenames:
            fixtures.append(dirpath)
    return sorted(fixtures)


def read_expected(fixture_dir: str) -> str:
    path = os.path.join(fixture_dir, EXPECTED_RESULT_FILENAME)
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()
    except OSError as e:
        return f"UNREADABLE: {e}"


def run_audit(fixture_dir: str) -> tuple[str, str]:
    """
    Run audit script with --repo-root <fixture_dir> --json.
    Returns (result_string, raw_output).
    result_string is RUNNER_ERROR if audit fails to produce valid JSON.
    """
    cmd = [
        sys.executable,
        AUDIT_SCRIPT,
        "--repo-root", fixture_dir,
        "--json",
    ]

    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=30,
        )
    except subprocess.TimeoutExpired:
        return RUNNER_ERROR, "TIMEOUT: audit script did not complete within 30s"
    except Exception as e:
        return RUNNER_ERROR, f"EXCEPTION: {e}"

    raw_output = proc.stdout
    stderr_output = proc.stderr.strip()

    if not raw_output.strip():
        detail = stderr_output if stderr_output else "(no output)"
        return RUNNER_ERROR, f"RUNNER_ERROR: audit produced no output. stderr: {detail}"

    try:
        data = json.loads(raw_output)
    except json.JSONDecodeError as e:
        detail = stderr_output if stderr_output else raw_output[:200]
        return RUNNER_ERROR, (
            f"RUNNER_ERROR: audit output is not valid JSON: {e}\n"
            f"stderr/output: {detail}"
        )

    result = data.get("result", RUNNER_ERROR)
    return result, raw_output


def run_fixtures() -> int:
    """Run all fixtures. Return 0 if all pass, 1 if any fail."""
    if not os.path.isfile(AUDIT_SCRIPT):
        print(f"ERROR: audit script not found: {AUDIT_SCRIPT}", file=sys.stderr)
        return 1

    fixtures = find_fixtures(FIXTURE_ROOT)
    if not fixtures:
        print(f"ERROR: no fixtures found in {FIXTURE_ROOT}", file=sys.stderr)
        return 1

    passed = []
    failed = []

    print("=" * 70)
    print("M26 Pre-Merge Corridor Smoke Fixture Runner — Task 26.11.1")
    print("=" * 70)
    print()

    for fixture_dir in fixtures:
        rel = os.path.relpath(fixture_dir, FIXTURE_ROOT)
        expected = read_expected(fixture_dir)
        actual, raw = run_audit(fixture_dir)

        if actual == expected:
            passed.append(rel)
            print(f"  PASS  {rel}")
            print(f"        expected={expected}  actual={actual}")
        else:
            failed.append(rel)
            print(f"  FAIL  {rel}")
            print(f"        expected={expected}  actual={actual}")
            if actual == RUNNER_ERROR:
                for line in raw.splitlines():
                    print(f"        {line}")
        print()

    print("=" * 70)
    print(f"PASSED: {len(passed)}  FAILED: {len(failed)}  TOTAL: {len(fixtures)}")
    print("=" * 70)
    print()

    if failed:
        print("FAILED fixtures:")
        for f in failed:
            print(f"  - {f}")
        print()
        return 1

    print("All fixtures passed.")
    return 0


if __name__ == "__main__":
    sys.exit(run_fixtures())
