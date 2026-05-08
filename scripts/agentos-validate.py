#!/usr/bin/env python3

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

PASS = "PASS"
FAIL = "FAIL"
WARN = "WARN"
ERROR = "ERROR"
NOT_RUN = "NOT_RUN"

CONTROL_READY = "CONTROL_READY"
READY_WITH_WARNINGS = "READY_WITH_WARNINGS"
NEEDS_REVIEW = "NEEDS_REVIEW"
NOT_READY = "NOT_READY"

RESULT_TO_EXIT = {
    PASS: 0,
    FAIL: 1,
    WARN: 2,
    ERROR: 3,
    NOT_RUN: 3,
}

PRIORITY = {
    PASS: 0,
    WARN: 1,
    NOT_RUN: 2,
    FAIL: 3,
    ERROR: 4,
}


def summary_tail(stdout_text, stderr_text):
    combined = f"{stdout_text}{stderr_text}"
    return combined[-500:]


def parse_cli(argv):
    parser = argparse.ArgumentParser(prog="agentos-validate.py")
    parser.add_argument("--json", action="store_true")
    parser.add_argument(
        "command",
        nargs="?",
        choices=["scope", "scope-fixtures", "execution-audit", "all"],
    )
    parser.add_argument("--task")
    args = parser.parse_args(argv)

    if args.command is None:
        args.command = "all"
    if args.command == "scope" and not args.task:
        raise ValueError("scope requires --task")
    if args.command in ["scope-fixtures", "execution-audit"] and args.task:
        raise ValueError("--task is only allowed with scope")
    if args.command == "all" and args.task:
        raise ValueError("--task is not supported with all")
    return args


def run_child(repo_root, command_name, command_list):
    child_script = command_list[1] if len(command_list) > 1 else ""
    if child_script and child_script.endswith(".py"):
        if not (repo_root / child_script).is_file():
            return {
                "name": command_name,
                "command": " ".join(command_list),
                "exit_code": 3,
                "result": ERROR,
                "output_summary": f"missing child script: {child_script}",
                "human_action_required": True,
                "ran": True,
            }

    try:
        proc = subprocess.run(
            command_list,
            cwd=str(repo_root),
            capture_output=True,
            text=True,
        )
    except Exception as exc:
        return {
            "name": command_name,
            "command": " ".join(command_list),
            "exit_code": 3,
            "result": ERROR,
            "output_summary": f"subprocess failure: {exc}",
            "human_action_required": True,
            "ran": True,
        }

    mapped_result = {
        0: PASS,
        1: FAIL,
        2: WARN,
        3: ERROR,
    }.get(proc.returncode, ERROR)

    out_sum = summary_tail(proc.stdout, proc.stderr)

    if command_name == "execution-audit":
        combined = f"{proc.stdout}\n{proc.stderr}"
        mapped_from_output = None
        if CONTROL_READY in combined:
            mapped_from_output = PASS
        elif READY_WITH_WARNINGS in combined:
            mapped_from_output = WARN
        elif NEEDS_REVIEW in combined:
            mapped_from_output = FAIL
        elif NOT_READY in combined:
            mapped_from_output = FAIL

        if mapped_from_output is not None:
            if mapped_from_output != mapped_result:
                out_sum = (out_sum + "\n" + "conflict: output mapping overrides child exit mapping")[-500:]
            mapped_result = mapped_from_output
        elif proc.returncode not in [0, 1, 2, 3]:
            mapped_result = ERROR

    return {
        "name": command_name,
        "command": " ".join(command_list),
        "exit_code": RESULT_TO_EXIT[mapped_result],
        "result": mapped_result,
        "output_summary": out_sum,
        "human_action_required": mapped_result in [FAIL, ERROR, NOT_RUN],
        "ran": True,
    }


def not_run_check(name, command_text, reason):
    return {
        "name": name,
        "command": command_text,
        "exit_code": 3,
        "result": NOT_RUN,
        "output_summary": reason,
        "human_action_required": True,
        "ran": False,
    }


def aggregate(checks):
    overall = PASS
    for item in checks:
        if PRIORITY[item["result"]] > PRIORITY[overall]:
            overall = item["result"]

    if checks and all(item["result"] == NOT_RUN for item in checks):
        overall = NOT_RUN

    commands_run = sum(1 for item in checks if item.get("ran", False))
    commands_not_run = sum(1 for item in checks if item["result"] == NOT_RUN)
    commands_passed = sum(1 for item in checks if item["result"] == PASS)
    commands_warned = sum(1 for item in checks if item["result"] == WARN)
    commands_failed = sum(1 for item in checks if item["result"] in [FAIL, ERROR])

    any_blocking = any(item["result"] in [FAIL, ERROR, NOT_RUN] for item in checks)
    if overall == WARN and not any_blocking:
        human_action_required = False
    elif overall == PASS:
        human_action_required = False
    else:
        human_action_required = any_blocking

    return {
        "result": overall,
        "commands_run": commands_run,
        "commands_passed": commands_passed,
        "commands_failed": commands_failed,
        "commands_warned": commands_warned,
        "commands_not_run": commands_not_run,
        "human_action_required": human_action_required,
        "checks": [
            {
                "name": item["name"],
                "command": item["command"],
                "exit_code": item["exit_code"],
                "result": item["result"],
                "output_summary": item["output_summary"],
                "human_action_required": item["human_action_required"],
            }
            for item in checks
        ],
    }


def run_scope(repo_root, task_path):
    cmd = [sys.executable, "scripts/check-scope-compliance.py", "--task", task_path]
    return [run_child(repo_root, "scope", cmd)]


def run_scope_fixtures(repo_root):
    cmd = [sys.executable, "scripts/test-scope-compliance-fixtures.py"]
    return [run_child(repo_root, "scope-fixtures", cmd)]


def run_execution_audit(repo_root):
    cmd = [sys.executable, "scripts/audit-execution-control.py"]
    return [run_child(repo_root, "execution-audit", cmd)]


def run_all(repo_root):
    checks = []
    default_task = repo_root / "tasks/active-task.md"

    if default_task.is_file():
        checks.extend(run_scope(repo_root, "tasks/active-task.md"))
    else:
        checks.append(
            not_run_check(
                "scope",
                f"{sys.executable} scripts/check-scope-compliance.py --task tasks/active-task.md",
                "default task file is missing",
            )
        )

    checks.extend(run_scope_fixtures(repo_root))
    checks.extend(run_execution_audit(repo_root))
    return checks


def print_human(summary):
    failed_names = [c["name"] for c in summary["checks"] if c["result"] in [FAIL, ERROR]]
    warn_names = [c["name"] for c in summary["checks"] if c["result"] == WARN]
    not_run_names = [c["name"] for c in summary["checks"] if c["result"] == NOT_RUN]

    print(f"Overall result: {summary['result']}")
    print(f"Checks run: {summary['commands_run']}")
    print(f"Failed checks: {len(failed_names)}")
    print(f"Warnings: {len(warn_names)}")
    print(f"Not run checks: {len(not_run_names)}")
    print(f"Human action required: {'YES' if summary['human_action_required'] else 'NO'}")

    if summary["result"] == PASS:
        print("Next step: continue normal review")
    elif summary["result"] == WARN:
        print("Next step: review warning details")
    elif summary["result"] == NOT_RUN:
        print("Next step: run missing checks")
    elif summary["result"] == FAIL:
        print("Next step: fix failing checks and rerun")
    else:
        print("Next step: investigate execution errors")


def emit_json(payload):
    text = json.dumps(payload, indent=2)
    print(text)


def main(argv):
    try:
        args = parse_cli(argv)
    except Exception as exc:
        payload = {
            "result": ERROR,
            "commands_run": 0,
            "commands_passed": 0,
            "commands_failed": 1,
            "commands_warned": 0,
            "commands_not_run": 0,
            "human_action_required": True,
            "checks": [
                {
                    "name": "argument-error",
                    "command": "agentos-validate",
                    "exit_code": 3,
                    "result": ERROR,
                    "output_summary": str(exc),
                    "human_action_required": True,
                }
            ],
        }
        if "--json" in argv:
            emit_json(payload)
        else:
            print_human(payload)
        return 3

    repo_root = Path(os.getcwd()).resolve()

    if args.command == "scope":
        checks = run_scope(repo_root, args.task)
    elif args.command == "scope-fixtures":
        checks = run_scope_fixtures(repo_root)
    elif args.command == "execution-audit":
        checks = run_execution_audit(repo_root)
    else:
        checks = run_all(repo_root)

    summary = aggregate(checks)

    if args.json:
        emit_json(summary)
    else:
        print_human(summary)

    return RESULT_TO_EXIT[summary["result"]]


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
