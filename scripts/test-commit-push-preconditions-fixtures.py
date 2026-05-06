#!/usr/bin/env python3
"""
test-commit-push-preconditions-fixtures.py — M26 Fixture Test Runner.

Exits non-zero if any fixture fails.
This runner verifies fixture behavior only.
"""

import json
import subprocess
import sys
from pathlib import Path

FIXTURES_ROOT = Path("tests/fixtures/commit-push-preconditions")
CHECKER_SCRIPT = Path("scripts/check-commit-push-preconditions.py")

PASS_STATUS = "PASS"
FAIL_STATUS = "FAIL"


def find_fixtures(root: Path) -> list:
    return sorted(path.parent for path in root.rglob("expected-result.txt"))


def run_fixture(fixture_dir: Path) -> tuple:
    expected_file = fixture_dir / "expected-result.txt"
    request_file = fixture_dir / "request.yaml"
    expected_result = expected_file.read_text(encoding="utf-8").strip()

    if request_file.exists():
        request_path = request_file
    else:
        request_path = fixture_dir / "nonexistent-request.yaml"

    cmd = [
        sys.executable,
        str(CHECKER_SCRIPT),
        "--request-file",
        str(request_path),
        "--json",
    ]

    try:
        proc = subprocess.run(cmd, capture_output=True, text=True)
    except Exception as exc:
        return FAIL_STATUS, None, expected_result, f"Subprocess error: {exc}"

    stdout = proc.stdout.strip()
    if not stdout:
        return FAIL_STATUS, "EMPTY_OUTPUT", expected_result, "Checker produced no output."

    try:
        output = json.loads(stdout)
        actual_result = output.get("result", "UNKNOWN")
    except json.JSONDecodeError:
        actual_result = stdout.splitlines()[0].strip().split(":")[0].strip()

    if actual_result == expected_result:
        return PASS_STATUS, actual_result, expected_result, ""

    return FAIL_STATUS, actual_result, expected_result, (
        f"Expected '{expected_result}', got '{actual_result}'"
    )


def main():
    if not CHECKER_SCRIPT.exists():
        print(f"ERROR: Checker script not found: {CHECKER_SCRIPT}")
        sys.exit(1)

    if not FIXTURES_ROOT.exists():
        print(f"ERROR: Fixtures root not found: {FIXTURES_ROOT}")
        sys.exit(1)

    fixtures = find_fixtures(FIXTURES_ROOT)
    if not fixtures:
        print(f"ERROR: No fixtures found under {FIXTURES_ROOT}")
        sys.exit(1)

    print(f"Running {len(fixtures)} fixture(s) from {FIXTURES_ROOT}")
    print()

    passed = failed = 0

    for fixture_dir in fixtures:
        label = str(fixture_dir.relative_to(FIXTURES_ROOT))
        status, actual, expected, detail = run_fixture(fixture_dir)

        if status == PASS_STATUS:
            passed += 1
            print(f"  PASS  {label}")
        else:
            failed += 1
            print(f"  FAIL  {label}")
            print(f"        {detail}")

    print()
    print(f"Results: {passed} passed  {failed} failed  0 skipped")
    print()
    print(
        "Notice: COMMIT_ALLOWED is not approval. "
        "PUSH_ALLOWED is not approval. "
        "This runner verifies fixture results only. "
        "It does not authorize commit or push."
    )

    sys.exit(1 if failed > 0 else 0)


if __name__ == "__main__":
    main()
