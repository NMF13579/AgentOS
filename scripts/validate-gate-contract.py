#!/usr/bin/env python3
import sys
from pathlib import Path


REQUIRED_DOCS = [
    "docs/UNIFIED-GATE-CONTRACT.md",
    "docs/GATE-RESULT-SEMANTICS.md",
    "docs/GATE-OUTPUT-CONTRACT.md",
]


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    missing = [rel for rel in REQUIRED_DOCS if not (root / rel).is_file()]

    if missing:
        print("GATE_CONTRACT_VALIDATE: run")
        print("GATE_CONTRACT_VALIDATE_RESULT: FAIL")
        print("GATE_CONTRACT_VALIDATE_REASON: missing required docs")
        for rel in missing:
            print(f"GATE_CONTRACT_VALIDATE_CHECK: artifact:{rel} FAIL missing")
        return 1

    print("GATE_CONTRACT_VALIDATE: run")
    print("GATE_CONTRACT_VALIDATE_RESULT: PASS")
    print("GATE_CONTRACT_VALIDATE_REASON: required gate contract docs present")
    for rel in REQUIRED_DOCS:
        print(f"GATE_CONTRACT_VALIDATE_CHECK: artifact:{rel} PASS present")
    return 0


if __name__ == "__main__":
    sys.exit(main())
