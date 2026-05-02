#!/usr/bin/env python3
import json
import subprocess
import sys
from pathlib import Path


def parse_args(argv):
    return {
        "json_mode": "--json" in argv,
        "strict": "--strict" in argv,
    }


def main() -> int:
    args = parse_args(sys.argv[1:])
    root = Path(__file__).resolve().parent.parent
    validator = root / "scripts" / "validate-gate-contract.py"
    fixtures = root / "scripts" / "test-gate-regression-fixtures.py"

    checks = []

    v = subprocess.run([sys.executable, str(validator)], capture_output=True, text=True)
    checks.append({
        "name": "validate-gate-contract",
        "status": "PASS" if v.returncode == 0 else "FAIL",
        "reason": "validator passed" if v.returncode == 0 else "validator failed",
    })

    f = subprocess.run([sys.executable, str(fixtures)], capture_output=True, text=True)
    checks.append({
        "name": "test-gate-regression-fixtures",
        "status": "PASS" if f.returncode == 0 else "FAIL",
        "reason": "fixtures passed" if f.returncode == 0 else "fixtures failed",
    })

    has_fail = any(c["status"] == "FAIL" for c in checks)
    result = "FAIL" if has_fail else "PASS"
    reason = "gate contract checks failed" if has_fail else "gate contract checks passed"

    if args["json_mode"]:
        print(json.dumps({"result": result, "reason": reason, "checks": checks}, ensure_ascii=False))
    else:
        print("GATE_CONTRACT_AUDIT: run")
        print(f"GATE_CONTRACT_AUDIT_RESULT: {result}")
        print(f"GATE_CONTRACT_AUDIT_REASON: {reason}")
        for c in checks:
            print(f"GATE_CONTRACT_AUDIT_CHECK: {c['name']} {c['status']} {c['reason']}")

    if args["strict"]:
        return 0 if result == "PASS" else 1
    return 0 if result in {"PASS", "WARN"} else 1


if __name__ == "__main__":
    sys.exit(main())
