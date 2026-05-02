#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    audit = root / "scripts" / "audit-gate-contract.py"

    proc = subprocess.run([sys.executable, str(audit)], capture_output=True, text=True)
    ok = proc.returncode == 0 and "GATE_CONTRACT_AUDIT_RESULT: PASS" in proc.stdout

    result = "PASS" if ok else "FAIL"
    reason = "unified gate smoke passed" if ok else "unified gate smoke failed"

    print("UNIFIED_GATE_SMOKE: run")
    print(f"UNIFIED_GATE_SMOKE_RESULT: {result}")
    print(f"UNIFIED_GATE_SMOKE_REASON: {reason}")

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
