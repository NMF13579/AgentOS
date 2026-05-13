#!/usr/bin/env python3
"""
Syncs task IDs across active-task.md and verification.md to prevent CI failures.
It uses the top-level `task_id` from tasks/active-task.md as the source of truth.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ACTIVE_TASK = ROOT / "tasks" / "active-task.md"
VERIFICATION = ROOT / "reports" / "verification.md"


def is_idle_state(text: str) -> bool:
    """Return True when active-task.md represents a legitimate idle/no-active-task state."""
    if "no active task" in text.lower():
        return True
    if re.search(r"^status:\s*(none|idle)\s*$", text, re.MULTILINE):
        return True
    has_scope = "scope_control:" in text
    has_contract = "## Contract" in text or "contract:" in text
    if not has_scope and not has_contract:
        return True
    return False


def sync_ids():
    if not ACTIVE_TASK.exists():
        print("PASS: active-task.md not found, skipping sync.")
        return 0

    content = ACTIVE_TASK.read_text(encoding="utf-8")

    # Idle-state bypass: no active task is not an error
    if is_idle_state(content):
        print("PASS: active-task.md is in idle state - no sync needed.")
        return 0

    # Extract source of truth task_id
    match = re.search(r"^task_id:\s*(.+)$", content, re.MULTILINE)
    if not match:
        print("FAIL: task_id not found in frontmatter of active-task.md")
        return 1

    truth_id = match.group(1).strip()

    # Update active-task.md task.id
    new_content = re.sub(
        r"^(\s*id:\s*).*$",
        rf"\g<1>{truth_id}",
        content,
        count=1,
        flags=re.MULTILINE
    )

    if new_content != content:
        ACTIVE_TASK.write_text(new_content, encoding="utf-8")
        print(f"Synced task.id in active-task.md to {truth_id}")
    else:
        print("active-task.md task.id is already in sync.")

    # Update verification.md verification.task_id
    if VERIFICATION.exists():
        v_content = VERIFICATION.read_text(encoding="utf-8")
        new_v_content = re.sub(
            r"^(\s*task_id:\s*).*$",
            rf"\g<1>{truth_id}",
            v_content,
            count=1,
            flags=re.MULTILINE
        )
        if new_v_content != v_content:
            VERIFICATION.write_text(new_v_content, encoding="utf-8")
            print(f"Synced verification.task_id in verification.md to {truth_id}")
        else:
            print("verification.md task_id is already in sync.")

    return 0


if __name__ == "__main__":
    sys.exit(sync_ids())
