#!/usr/bin/env python3
import subprocess
import sys
import tempfile
from pathlib import Path


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def main() -> int:
    repo = Path(__file__).resolve().parent.parent
    checker = repo / "scripts" / "check-template-integrity.py"

    ran = 0
    passed = 0
    failed = 0

    # Case 1: repository root should be PASS after template contract files exist.
    ran += 1
    c1 = run([sys.executable, str(checker), "--root", str(repo)])
    ok1 = c1.returncode == 0 and "TEMPLATE_INTEGRITY_RESULT: PASS" in c1.stdout
    if ok1:
        passed += 1
    else:
        failed += 1

    # Case 2: empty root should be NOT_IMPLEMENTED (non-strict exit 0)
    ran += 1
    with tempfile.TemporaryDirectory() as td:
        c2 = run([sys.executable, str(checker), "--root", td])
        ok2 = c2.returncode == 0 and "TEMPLATE_INTEGRITY_RESULT: NOT_IMPLEMENTED" in c2.stdout
        if ok2:
            passed += 1
        else:
            failed += 1

    # Case 3: empty root strict should be non-zero + NOT_IMPLEMENTED marker
    ran += 1
    with tempfile.TemporaryDirectory() as td:
        c3 = run([sys.executable, str(checker), "--root", td, "--strict"])
        ok3 = c3.returncode != 0 and "TEMPLATE_INTEGRITY_RESULT: NOT_IMPLEMENTED" in c3.stdout
        if ok3:
            passed += 1
        else:
            failed += 1

    result = "PASS" if failed == 0 else "FAIL"
    print(f"TEMPLATE_INTEGRITY_FIXTURES_RESULT: {result}")
    print(f"TEMPLATE_INTEGRITY_FIXTURES_RUN: {ran}")
    print(f"TEMPLATE_INTEGRITY_FIXTURES_PASSED: {passed}")
    print(f"TEMPLATE_INTEGRITY_FIXTURES_FAILED: {failed}")

    return 0 if result == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
