#!/usr/bin/env python3
import argparse
import json
import re
import subprocess
from pathlib import Path

VALID_CATEGORIES = {
    "SAFE_READ",
    "SAFE_VALIDATE",
    "SAFE_TEST",
    "WRITE_LOCAL",
    "GIT_LOCAL",
    "GIT_REMOTE",
    "DANGEROUS",
    "FORBIDDEN",
    "UNKNOWN",
}

PERMISSION_REQUIREMENTS = {
    "SAFE_READ": "READ_ONLY",
    "SAFE_VALIDATE": "LOCAL_TEST",
    "SAFE_TEST": "LOCAL_TEST",
    "WRITE_LOCAL": "LOCAL_EDIT",
    "GIT_LOCAL": "LOCAL_EDIT",
}

TIER_1_PATTERNS = [
    re.compile(r"(^|\s)git\s+commit(\s|$)"),
    re.compile(r"(^|\s)git\s+push(\s|$)"),
    re.compile(r"(^|\s)git\s+merge(\s|$)"),
    re.compile(r"(^|\s)gh\s+pr\s+merge(\s|$)"),
    re.compile(r"(^|\s)sudo\s+rm(\s|$)"),
    re.compile(r"(^|\s)chmod\s+-R\s+777(\s|$)"),
]

APPROVAL_KEYWORDS = [
    "approval",
    "approved",
    "human-gate",
    "owner-review",
    "reviewer",
    "permission",
]

TIER_2_PATTERNS = [
    re.compile(r"(^|\s)rm\s+-[a-zA-Z]*[rf][a-zA-Z]*\s"),
    re.compile(r"(^|\s)rm\s+-rf(\s|$)"),
    re.compile(r"(^|\s)rm\s+-fr(\s|$)"),
]

REVIEW_PATTERNS = [
    re.compile(r"(^|\s)sudo(\s|$)"),
    re.compile(r"curl[^\n]*\|\s*(bash|sh)"),
    re.compile(r"wget[^\n]*\|\s*(bash|sh)"),
]


def print_result(result: str, reason: str, as_json: bool = False) -> None:
    if as_json:
        print(json.dumps({"result": result, "reason": reason}, ensure_ascii=True))
        return
    print(f"RESULT: {result}")
    print(f"REASON: {reason}")


def detect_tier_1(command: str):
    lowered = command.lower()
    for pattern in TIER_1_PATTERNS:
        if pattern.search(lowered):
            return "tier_1_command_blocker"

    if is_approval_simulation_write(lowered):
        return "approval_simulation_write"

    return None


def is_approval_simulation_write(command_lower: str) -> bool:
    read_only_starts = ("cat ", "grep ", "rg ", "sed -n ")
    if command_lower.strip().startswith(read_only_starts):
        return False

    write_markers = [">", ">>", "touch ", "tee ", "mv ", "cp ", "python", "perl", "node"]
    if not any(marker in command_lower for marker in write_markers):
        return False

    return any(keyword in command_lower for keyword in APPROVAL_KEYWORDS)


def detect_tier_2(command: str):
    lowered = command.lower()
    for pattern in TIER_2_PATTERNS:
        if pattern.search(lowered):
            return "tier_2_rm_rf"
    return None


def detect_review_pattern(command: str):
    lowered = command.lower()
    for pattern in REVIEW_PATTERNS:
        if pattern.search(lowered):
            return "review_pattern"
    return None


def check_permission_state(permission_file: str, required_level: str):
    permission_script = Path("scripts/agentos-permission-state.py")
    if not permission_script.exists():
        return "COMMAND_NEEDS_REVIEW", "permission script missing"

    try:
        proc = subprocess.run(
            [
                "python3",
                "scripts/agentos-permission-state.py",
                "check",
                permission_file,
                "--requires",
                required_level,
            ],
            check=False,
            capture_output=True,
            text=True,
            timeout=10,
        )
    except (subprocess.TimeoutExpired, OSError):
        return "PERMISSION_INVALID", "permission check failed"

    result_line = None
    for line in (proc.stdout or "").splitlines():
        if line.startswith("RESULT:"):
            result_line = line.split(":", 1)[1].strip()
            break

    if not result_line:
        return "PERMISSION_INVALID", "unknown permission result"

    if result_line == "PERMISSION_OK":
        return "PERMISSION_OK", "permission ok"
    if result_line == "PERMISSION_BLOCKED":
        return "PERMISSION_BLOCKED", "permission blocked"
    if result_line == "PERMISSION_DENIED":
        return "PERMISSION_DENIED", "permission denied"
    if result_line in {"PERMISSION_EXPIRED", "PERMISSION_INVALID"}:
        return "PERMISSION_INVALID", "permission invalid or expired"
    if result_line == "NEEDS_REVIEW":
        return "COMMAND_NEEDS_REVIEW", "permission needs review"

    return "PERMISSION_INVALID", "unknown permission result"


def load_approval_record(path: str):
    file_path = Path(path)
    if not file_path.exists():
        return False, "approval record missing"
    try:
        data = json.loads(file_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return False, "invalid approval record json"

    if not isinstance(data, dict):
        return False, "approval record must be object"
    if data.get("approved") is not True:
        return False, "approval record missing approved=true"
    if not data.get("task_id") or not data.get("approved_by"):
        return False, "approval record missing required fields"

    return True, "approval record is valid"


def evaluate(category: str, command: str, permission_state: str, approval_record: str):
    if category not in VALID_CATEGORIES:
        return "COMMAND_NEEDS_REVIEW", "unknown category"

    tier_1 = detect_tier_1(command)
    if tier_1:
        return "COMMAND_POLICY_VIOLATION", f"tier 1 blocker: {tier_1}"

    if category == "FORBIDDEN":
        return "COMMAND_POLICY_VIOLATION", "forbidden category"
    if category == "UNKNOWN":
        return "COMMAND_NEEDS_REVIEW", "unknown category requires review"
    if category == "GIT_REMOTE":
        return "COMMAND_POLICY_VIOLATION", "git remote operations are blocked"

    tier_2 = detect_tier_2(command)
    if tier_2 and category != "DANGEROUS":
        return "COMMAND_POLICY_VIOLATION", f"tier 2 blocker: {tier_2}"

    review_match = detect_review_pattern(command)
    if review_match:
        return "COMMAND_NEEDS_REVIEW", "command requires review"

    if category == "WRITE_LOCAL" and not permission_state:
        return "COMMAND_NEEDS_REVIEW", "write_local requires permission state"

    if category == "DANGEROUS":
        if not approval_record:
            return "COMMAND_NEEDS_APPROVAL", "dangerous command requires approval record"
        ok, reason = load_approval_record(approval_record)
        if not ok:
            return "COMMAND_NEEDS_APPROVAL", reason

    required_level = PERMISSION_REQUIREMENTS.get(category)
    if permission_state and required_level:
        perm_result, perm_reason = check_permission_state(permission_state, required_level)
        if perm_result != "PERMISSION_OK":
            return perm_result, perm_reason

    if permission_state and not required_level:
        perm_result, perm_reason = check_permission_state(permission_state, "READ_ONLY")
        if perm_result != "PERMISSION_OK":
            return perm_result, perm_reason

    return "COMMAND_ALLOWED", "command passed guard checks"


def main() -> int:
    parser = argparse.ArgumentParser(description="M27 command guard")
    sub = parser.add_subparsers(dest="command_name", required=True)

    p_check = sub.add_parser("check")
    p_check.add_argument("--category", required=True)
    p_check.add_argument("--command", required=True)
    p_check.add_argument("--permission-state")
    p_check.add_argument("--approval-record")
    p_check.add_argument("--explain", action="store_true")
    p_check.add_argument("--json", action="store_true")

    args = parser.parse_args()

    if args.command_name != "check":
        print_result("COMMAND_NEEDS_REVIEW", "unknown subcommand", args.json)
        return 1

    category = args.category.strip()
    result, reason = evaluate(category, args.command, args.permission_state, args.approval_record)
    if args.explain:
        reason = f"{reason}; declared_category={category}"

    print_result(result, reason, args.json)
    return 0 if result == "COMMAND_ALLOWED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
