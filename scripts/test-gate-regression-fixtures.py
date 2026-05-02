#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    validator = root / "scripts" / "validate-gate-contract.py"

    checks_run = 1
    proc = subprocess.run([sys.executable, str(validator)], capture_output=True, text=True)
    ok = proc.returncode == 0 and "GATE_CONTRACT_VALIDATE_RESULT: PASS" in proc.stdout

    checks_passed = 1 if ok else 0
    checks_failed = 0 if ok else 1
    result = "PASS" if ok else "FAIL"

    print(f"GATE_REGRESSION_FIXTURES_RESULT: {result}")
    print(f"GATE_REGRESSION_FIXTURES_RUN: {checks_run}")
    print(f"GATE_REGRESSION_FIXTURES_PASSED: {checks_passed}")
    print(f"GATE_REGRESSION_FIXTURES_FAILED: {checks_failed}")

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
