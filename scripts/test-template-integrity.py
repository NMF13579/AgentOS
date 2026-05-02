#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    runner = root / "scripts" / "test-template-integrity-fixtures.py"

    print("Template Integrity Checker Self-Test")

    if not runner.exists():
        print("Result: FAIL")
        print("- Missing script: scripts/test-template-integrity-fixtures.py")
        return 1

    completed = subprocess.run(
        [sys.executable, str(runner)],
        cwd=str(root),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
    )

    stdout = completed.stdout or ""
    stderr = completed.stderr or ""

    ok = completed.returncode == 0 and "TEMPLATE_INTEGRITY_FIXTURES_RESULT: PASS" in stdout
    if ok:
        print("fixture-suite: PASS")
        print("Result: PASS")
        return 0

    print("fixture-suite: FAIL")
    if stdout.strip():
        for line in stdout.strip().splitlines()[:6]:
            print(f"- {line}")
    if stderr.strip():
        print(f"- stderr: {stderr.strip()}")
    print("Result: FAIL")
    return 1


if __name__ == "__main__":
    sys.exit(main())
