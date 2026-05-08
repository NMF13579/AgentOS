#!/usr/bin/env python3
import json
import subprocess
import sys
from pathlib import Path

SUBSYSTEMS = {
    "audit": "scripts/agentos-audit-log.py",
    "check-command": "scripts/agentos-command-guard.py",
    "check-write": "scripts/agentos-write-guard.py",
    "check-commit": "scripts/agentos-git-guard.py",
    "check-push": "scripts/agentos-git-guard.py",
    "human-gate": "scripts/agentos-human-gate.py",
    "violation": "scripts/agentos-violation-enforce.py",
    "retry": "scripts/agentos-retry-enforce.py",
    "permission": "scripts/agentos-permission-state.py",
}

ALLOW_RESULTS = {
    "COMMAND_ALLOWED",
    "WRITE_ALLOWED",
    "GIT_ALLOWED",
    "HUMAN_GATE_APPROVED",
    "RETRY_ALLOWED",
    "PERMISSION_OK",
    "AUDIT_OK",
    "AUDIT_APPENDED",
    "SANCTION_REQUIRED",
    "SANCTION_APPLIED",
}

BLOCK_RESULTS = {
    "COMMAND_BLOCKED",
    "WRITE_BLOCKED",
    "GIT_BLOCKED",
    "TASK_BLOCKED",
    "AGENT_BLOCKED",
    "RETRY_BLOCKED",
    "PERMISSION_BLOCKED",
    "RETRY_EXHAUSTED",
    "HUMAN_GATE_REJECTED",
}

POLICY_RESULTS = {
    "COMMAND_POLICY_VIOLATION",
    "WRITE_POLICY_VIOLATION",
    "GIT_POLICY_VIOLATION",
    "RETRY_POLICY_VIOLATION",
}

NEEDS_APPROVAL_RESULTS = {
    "COMMAND_NEEDS_APPROVAL",
    "WRITE_NEEDS_APPROVAL",
    "GIT_NEEDS_APPROVAL",
    "HUMAN_GATE_REQUIRED",
}

NEEDS_REVIEW_RESULTS = {
    "HUMAN_GATE_NEEDS_CLARIFICATION",
    "RETRY_NEEDS_HUMAN_REVIEW",
    "RETRY_NEEDS_OWNER_REVIEW",
    "NEEDS_HUMAN_REVIEW",
    "NEEDS_OWNER_REVIEW",
    "HUMAN_GATE_NEEDS_REVIEW",
    "VIOLATION_NEEDS_REVIEW",
}

INVALID_RESULTS = {
    "RETRY_INVALID",
    "VIOLATION_INVALID",
    "PERMISSION_INVALID",
    "PRECONDITION_INVALID",
    "HUMAN_GATE_INVALID",
    "AUDIT_INVALID",
}


def emit(result: str, reason: str, as_json: bool):
    if as_json:
        print(json.dumps({"result": result, "reason": reason}, ensure_ascii=True))
    else:
        print(f"RESULT: {result}")
        print(f"REASON: {reason}")


def parse_result(stdout: str):
    for line in stdout.splitlines():
        if line.startswith("RESULT:"):
            return line.split(":", 1)[1].strip()
    return None


def map_result(underlying: str):
    if underlying in ALLOW_RESULTS:
        return "ENFORCE_ALLOWED"
    if underlying in POLICY_RESULTS:
        return "ENFORCE_POLICY_VIOLATION"
    if underlying in BLOCK_RESULTS:
        return "ENFORCE_BLOCKED"
    if underlying in NEEDS_APPROVAL_RESULTS:
        return "ENFORCE_NEEDS_APPROVAL"
    if underlying in NEEDS_REVIEW_RESULTS:
        return "ENFORCE_NEEDS_REVIEW"
    if underlying in INVALID_RESULTS:
        return "ENFORCE_INVALID"
    return "ENFORCE_SUBSYSTEM_ERROR"


def route_args(cmd: str, rest: list[str]):
    if cmd == "check-command":
        return ["check", *rest]
    if cmd == "check-write":
        return ["check", *rest]
    if cmd == "check-commit":
        return ["check", "--action", "commit", *rest]
    if cmd == "check-push":
        return ["check", "--action", "push", *rest]
    return rest


def main():
    argv = sys.argv[1:]

    as_json = False
    explain = False
    filtered = []
    for a in argv:
        if a == "--json":
            as_json = True
        elif a == "--explain":
            explain = True
        else:
            filtered.append(a)

    if not filtered:
        emit("ENFORCE_INVALID", "missing subcommand", as_json)
        return 1

    subcmd, rest = filtered[0], filtered[1:]
    if subcmd not in SUBSYSTEMS:
        emit("ENFORCE_INVALID", "unsupported subcommand", as_json)
        return 1

    script = Path(SUBSYSTEMS[subcmd])
    if not script.exists():
        emit("ENFORCE_SUBSYSTEM_MISSING", f"missing subsystem script: {script}", as_json)
        return 1

    cmd_args = route_args(subcmd, rest)
    if explain:
        cmd_args.append("--explain")

    try:
        run = subprocess.run(
            ["python3", str(script), *cmd_args],
            capture_output=True,
            text=True,
            check=False,
            timeout=20,
        )
    except subprocess.TimeoutExpired:
        emit("ENFORCE_SUBSYSTEM_ERROR", "subsystem timeout", as_json)
        return 1
    except Exception as e:
        emit("ENFORCE_SUBSYSTEM_ERROR", f"subsystem crash: {e}", as_json)
        return 1

    underlying_result = parse_result(run.stdout or "")
    if underlying_result is None:
        reason = (run.stdout or run.stderr or "unknown subsystem output").strip()
        emit("ENFORCE_SUBSYSTEM_ERROR", reason, as_json)
        return 1

    top = map_result(underlying_result)
    reason = (run.stdout or run.stderr or "subsystem returned result").strip().splitlines()
    reason_text = reason[-1] if reason else "subsystem returned result"

    # consistency checks
    if top == "ENFORCE_ALLOWED" and run.returncode != 0:
        emit("ENFORCE_SUBSYSTEM_ERROR", "subsystem non-zero exit with allow result", as_json)
        return 1
    if top in {"ENFORCE_BLOCKED", "ENFORCE_NEEDS_APPROVAL", "ENFORCE_NEEDS_REVIEW", "ENFORCE_POLICY_VIOLATION", "ENFORCE_INVALID"} and run.returncode == 0:
        emit("ENFORCE_SUBSYSTEM_ERROR", "subsystem zero exit with blocked/review result", as_json)
        return 1

    emit(top, f"mapped from {underlying_result}; {reason_text}", as_json)
    return 0 if top == "ENFORCE_ALLOWED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
