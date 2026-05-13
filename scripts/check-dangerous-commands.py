#!/usr/bin/env python3
import re
import sys
from pathlib import Path

DANGEROUS_PATTERNS = [
    r"\brm\s+-rf\b",
    r"\bgit\s+reset\s+--hard\b",
    r"\bgit\s+clean\s+-fdx?\b",
    r"\bdrop\s+table\b",
    r"\btruncate\s+table\b",
    r"\bdelete\s+from\b",
    r"\bchmod\s+777\b",
    r"\bsudo\s+rm\b",
    r"\bformat\s+[a-z]:",
    r"\bdd\s+if=",
    r">\s*/dev/sd",
    r"\boverwrite\s+prod\s+config\b",
]

FILES_TO_CHECK = [
    "tasks/active-task.md",
    "reports/verification.md",
]


def main():
    task_path = sys.argv[1] if len(sys.argv) > 1 else "tasks/active-task.md"

    # Idle-state bypass
    try:
        text = Path(task_path).read_text(encoding="utf-8")
        text_lower = text.lower()
        if ("no active task" in text_lower or
            not text.startswith("---")):
            print("PASS: idle state - no active task")
            return 0
    except Exception:
        pass

    matches = []

    for relative_path in FILES_TO_CHECK:
        path = Path(relative_path)
        if not path.exists():
            print("FAIL: dangerous command check failed")
            print(f"missing file: {relative_path}")
            return 1

        content = path.read_text(encoding="utf-8")
        for pattern in DANGEROUS_PATTERNS:
            if re.search(pattern, content, re.IGNORECASE):
                matches.append(f"{relative_path}: matched pattern: {pattern}")

    if matches:
        print("FAIL: dangerous command check failed")
        for match in matches:
            print(match)
        return 1

    print("PASS: dangerous command check passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
