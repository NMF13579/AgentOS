#!/usr/bin/env python3
from pathlib import Path
import argparse
import sys
from typing import List, Sequence, Tuple


Section = Tuple[str, Sequence[str], Sequence[str]]


SECTIONS = [
    (
        "Core files",
        [
            "core-rules/MAIN.md",
            "workflow/MAIN.md",
            "llms.txt",
            "repo-map.md",
        ],
        [],
    ),
    (
        "Input layer",
        [
            "INIT.md",
            "project/PROJECT.md",
            "stages/01-interview/BOOT.md",
            "stages/spec-wizard/BOOT.md",
        ],
        [
            "project/",
            "tasks/drafts/",
        ],
    ),
    (
        "Task brief validation",
        [
            "schemas/task-brief.schema.json",
            "scripts/validate-task-brief.py",
        ],
        [],
    ),
    (
        "Review / Trace",
        [
            "tools/task-review/REVIEW-TASK-BRIEF.md",
            "templates/task-brief-review.md",
            "tools/interview-archive/WRITE-TRACE.md",
            "templates/task-decision-trace.md",
        ],
        [],
    ),
    (
        "Contract generation",
        [
            "tools/task-contract-builder/BUILD-TASK-CONTRACT.md",
            "templates/task-contract-from-brief.md",
            "scripts/generate-task-contract.py",
        ],
        [],
    ),
    (
        "Queue lifecycle",
        [
            "templates/queue-entry.md",
            "tools/task-queue/MANAGE-QUEUE.md",
        ],
        [
            "tasks/queue/",
            "tasks/done/",
            "tasks/dropped/",
        ],
    ),
    (
        "Runner protocol",
        [
            "tools/agent-runner/RUNNER-PROTOCOL.md",
            "scripts/agent-next.py",
            "scripts/agent-complete.py",
            "scripts/agent-fail.py",
        ],
        [],
    ),
    (
        "Task health metrics",
        [
            "scripts/task-health.py",
            "tools/task-health/TASK-HEALTH.md",
        ],
        [],
    ),
]

FORBIDDEN_FILES = [
    "PROJECT-v2.md",
    "auto-flow.py",
    "scripts/auto-flow.py",
    "scripts/auto-runner.py",
    "scripts/run-agent.py",
    "scripts/agent-runner.py",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check AgentOS template structure integrity."
    )
    parser.add_argument(
        "--root",
        default=".",
        help="Root directory to check.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Reserved for 7.0.2; accepted but does not change behavior.",
    )
    return parser.parse_args()


def check_section(root: Path, files: Sequence[str], dirs: Sequence[str]) -> List[str]:
    errors = []
    for rel_path in files:
        if not (root / rel_path).is_file():
            errors.append("Missing file: {0}".format(rel_path))
    for rel_path in dirs:
        if not (root / rel_path).is_dir():
            errors.append("Missing directory: {0}".format(rel_path))
    return errors


def check_gitignore(root: Path) -> List[str]:
    gitignore_path = root / ".gitignore"
    if not gitignore_path.is_file():
        return ["Missing file: .gitignore"]

    try:
        lines = gitignore_path.read_text().splitlines()
    except UnicodeDecodeError:
        return ["Unable to read file: .gitignore"]

    for line in lines:
        if line.strip() == "tasks/drafts/":
            return []
    return ["Missing .gitignore entry: tasks/drafts/"]


def check_forbidden_files(root: Path) -> List[str]:
    errors = []
    for rel_path in FORBIDDEN_FILES:
        if (root / rel_path).is_file():
            errors.append("Found forbidden file: {0}".format(rel_path))
    return errors


def print_section(name: str, errors: Sequence[str]) -> None:
    if errors:
        print("{0}: FAIL".format(name))
        for error in errors:
            print("- {0}".format(error))
    else:
        print("{0}: PASS".format(name))


def main() -> int:
    args = parse_args()
    root = Path(args.root)

    print("AgentOS Template Integrity Report")

    if not root.is_dir():
        print(
            "Root: FAIL - Root path does not exist or is not a directory: {0}".format(
                args.root
            )
        )
        print("Result: FAIL")
        return 1

    has_errors = False

    for name, files, dirs in SECTIONS:
        errors = check_section(root, files, dirs)
        print_section(name, errors)
        if errors:
            has_errors = True

    runtime_errors = check_gitignore(root)
    print_section("Runtime artifacts", runtime_errors)
    if runtime_errors:
        has_errors = True

    forbidden_errors = check_forbidden_files(root)
    print_section("Forbidden files", forbidden_errors)
    if forbidden_errors:
        has_errors = True

    if has_errors:
        print("Result: FAIL")
        return 1

    print("Result: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
