#!/usr/bin/env python3
"""Negative state machine fixture runner for AgentOS.

Expected rejection is PASS.
This runner uses isolated temporary workspaces.
It must not modify production task files.
"""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = REPO_ROOT / "scripts"


CASES = [
    {
        "name": "active-without-approval",
        "kind": "transition",
        "script": "check-transition.py",
        "args": ["--to", "active"],
        "expected_exit": 1,
        "build": "build_active_without_approval",
    },
    {
        "name": "contract-without-trace",
        "kind": "state",
        "script": "validate-task-state.py",
        "args": [],
        "expected_exit": 1,
        "build": "build_contract_without_trace",
    },
    {
        "name": "review-ready-without-task",
        "kind": "state",
        "script": "validate-task-state.py",
        "args": [],
        "expected_exit": 1,
        "build": "build_review_ready_without_task",
    },
    {
        "name": "completed-and-active-conflict",
        "kind": "state",
        "script": "validate-task-state.py",
        "args": [],
        "expected_exit": 1,
        "build": "build_completed_and_active_conflict",
    },
    {
        "name": "dropped-and-active-conflict",
        "kind": "state",
        "script": "validate-task-state.py",
        "args": [],
        "expected_exit": 1,
        "build": "build_dropped_and_active_conflict",
    },
    {
        "name": "invalid-transition-brief-to-active",
        "kind": "transition",
        "script": "check-transition.py",
        "args": ["--to", "active"],
        "expected_exit": 1,
        "build": "build_invalid_transition_brief_to_active",
    },
]


def usage() -> None:
    print("Usage: python3 scripts/test-state-fixtures.py")


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def build_task_base(workspace: Path, task_name: str) -> Path:
    tasks_root = workspace / "tasks"
    task_dir = tasks_root / task_name
    task_dir.mkdir(parents=True, exist_ok=True)
    (tasks_root / "drafts").mkdir(parents=True, exist_ok=True)
    (tasks_root / "done").mkdir(parents=True, exist_ok=True)
    (tasks_root / "dropped").mkdir(parents=True, exist_ok=True)
    (tasks_root / "active-task.md").write_text("", encoding="utf-8")
    return task_dir


def build_active_without_approval(workspace: Path, task_name: str) -> Path:
    task_dir = build_task_base(workspace, task_name)
    write_file(
        task_dir / "TASK.md",
        "task_id: {task}\nstatus: APPROVED\n".format(task=task_name),
    )
    write_file(
        task_dir / "REVIEW.md",
        "review_status: READY\nexecution_allowed: true\n",
    )
    write_file(task_dir / "TRACE.md", "trace evidence\n")
    write_file(
        workspace / "tasks" / "drafts" / f"{task_name}-contract-draft.md",
        "contract draft evidence\n",
    )
    return task_dir


def build_contract_without_trace(workspace: Path, task_name: str) -> Path:
    task_dir = build_task_base(workspace, task_name)
    write_file(
        task_dir / "TASK.md",
        "task_id: {task}\nstatus: APPROVED\n".format(task=task_name),
    )
    write_file(
        task_dir / "REVIEW.md",
        "review_status: READY\nexecution_allowed: true\n",
    )
    write_file(
        workspace / "tasks" / "drafts" / f"{task_name}-contract-draft.md",
        "contract draft evidence\n",
    )
    return task_dir


def build_review_ready_without_task(workspace: Path, task_name: str) -> Path:
    task_dir = build_task_base(workspace, task_name)
    write_file(task_dir / "REVIEW.md", "review_status: READY\nexecution_allowed: true\n")
    return task_dir


def build_completed_and_active_conflict(workspace: Path, task_name: str) -> Path:
    task_dir = build_task_base(workspace, task_name)
    write_file(task_dir / "TASK.md", f"task_id: {task_name}\nstatus: APPROVED\n")
    write_file(workspace / "tasks" / "active-task.md", f"{task_name}\n")
    write_file(workspace / "tasks" / "done" / f"{task_name}.md", f"{task_name}\n")
    return task_dir


def build_dropped_and_active_conflict(workspace: Path, task_name: str) -> Path:
    task_dir = build_task_base(workspace, task_name)
    write_file(task_dir / "TASK.md", f"task_id: {task_name}\nstatus: APPROVED\n")
    write_file(workspace / "tasks" / "active-task.md", f"{task_name}\n")
    write_file(workspace / "tasks" / "dropped" / f"{task_name}.md", f"{task_name}\n")
    return task_dir


def build_invalid_transition_brief_to_active(workspace: Path, task_name: str) -> Path:
    task_dir = build_task_base(workspace, task_name)
    write_file(task_dir / "TASK.md", f"task_id: {task_name}\nstatus: DRAFT\n")
    return task_dir


BUILDERS = {
    "build_active_without_approval": build_active_without_approval,
    "build_contract_without_trace": build_contract_without_trace,
    "build_review_ready_without_task": build_review_ready_without_task,
    "build_completed_and_active_conflict": build_completed_and_active_conflict,
    "build_dropped_and_active_conflict": build_dropped_and_active_conflict,
    "build_invalid_transition_brief_to_active": build_invalid_transition_brief_to_active,
}


def run_script(script_name: str, task_dir: Path, extra_args: list[str]) -> subprocess.CompletedProcess[str]:
    script_path = SCRIPTS_DIR / script_name
    return subprocess.run(
        [sys.executable, str(script_path), str(task_dir), *extra_args],
        cwd=str(task_dir.parent.parent),
        capture_output=True,
        text=True,
    )


def case_passed(result: subprocess.CompletedProcess[str], expected_exit: int) -> bool:
    return result.returncode == expected_exit


def main() -> int:
    if len(sys.argv) != 1:
        usage()
        return 2

    print("STATE FIXTURES TEST")
    print()

    all_passed = True

    for case in CASES:
        with tempfile.TemporaryDirectory(prefix=f"agentos-{case['name']}-") as tmp:
            workspace = Path(tmp)
            builder = BUILDERS[case["build"]]
            task_dir = builder(workspace, case["name"])
            result = run_script(case["script"], task_dir, case["args"])
            passed = case_passed(result, case["expected_exit"])
            all_passed &= passed
            print(f"{case['name']}: {'PASS' if passed else 'FAIL'}")
            if not passed:
                print(f"  expected exit: {case['expected_exit']}")
                print(f"  actual exit: {result.returncode}")
                stdout = result.stdout.strip()
                stderr = result.stderr.strip()
                if stdout:
                    print("  stdout:")
                    for line in stdout.splitlines():
                        print(f"    {line}")
                if stderr:
                    print("  stderr:")
                    for line in stderr.splitlines():
                        print(f"    {line}")

    print()
    print(f"Result: {'PASS' if all_passed else 'FAIL'}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
