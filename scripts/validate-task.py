#!/usr/bin/env python3
import pathlib
import re
import sys

import yaml
from jsonschema import validate

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_TARGET = ROOT / "tasks" / "active-task.md"
SCHEMA_PATH = ROOT / "schemas" / "task.schema.json"


def is_idle_state(text: str) -> bool:
    """Return True when active-task.md is in legitimate idle state."""
    text_lower = text.lower()
    if "no active task" in text_lower:
        return True
    if re.search(r"^status:\s*(none|idle)\s*$", text, re.MULTILINE):
        return True
    has_scope = "scope_control:" in text
    has_contract = "## Contract" in text or "contract:" in text
    if not has_scope and not has_contract:
        return True
    return False


def load_frontmatter(markdown_path: pathlib.Path):
    text = markdown_path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError("frontmatter is missing")

    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("frontmatter is missing")

    try:
        closing_index = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration as exc:
        raise ValueError("frontmatter is missing") from exc

    for line in lines[closing_index + 1 :]:
        if line.strip() == "---":
            raise ValueError("more than one frontmatter block found")

    frontmatter = "\n".join(lines[1:closing_index])
    data = yaml.safe_load(frontmatter)
    if not isinstance(data, dict):
        raise ValueError("frontmatter must be a YAML object")
    return data


def main():
    target = pathlib.Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else DEFAULT_TARGET
    try:
        text = target.read_text(encoding="utf-8")
    except Exception as exc:
        print("FAIL: task validation failed")
        print(str(exc))
        return 1

    # Idle-state: no active task — skip schema validation entirely
    if is_idle_state(text):
        print("PASS: idle state - no active task")
        return 0

    try:
        data = load_frontmatter(target)
        schema = yaml.safe_load(SCHEMA_PATH.read_text(encoding="utf-8"))
        validate(instance=data, schema=schema)
        print("PASS: task validation passed")
        return 0
    except Exception as exc:
        print("FAIL: task validation failed")
        print(str(exc))
        return 1


if __name__ == "__main__":
    sys.exit(main())
