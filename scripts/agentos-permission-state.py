#!/usr/bin/env python3
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

PERMISSION_RANK = {
    "BLOCKED": 0,
    "READ_ONLY": 1,
    "PATCH_PROPOSE": 2,
    "LOCAL_EDIT": 3,
    "LOCAL_TEST": 4,
    "COMMIT_REQUEST": 5,
    "PUSH_REQUEST": 6,
}

REQUIRED_FIELDS = [
    "schema_version",
    "active_task_id",
    "agent_id",
    "current_permission",
    "permission_record",
    "open_violations",
    "retry_count",
    "blocked_state",
    "expiration",
    "last_decision",
    "updated_at",
]


def print_result(result: str, reason: str) -> None:
    print(f"RESULT: {result}")
    print(f"REASON: {reason}")


def parse_utc_iso8601(value: str):
    if value.endswith("Z"):
        value = value[:-1] + "+00:00"
    try:
        dt = datetime.fromisoformat(value)
    except ValueError:
        return None
    if dt.tzinfo is None:
        return None
    return dt.astimezone(timezone.utc)


def load_state(path: str):
    file_path = Path(path)
    if not file_path.exists():
        return None, "NEEDS_REVIEW", "state file missing"
    try:
        content = file_path.read_text(encoding="utf-8")
        data = json.loads(content)
    except json.JSONDecodeError:
        return None, "PERMISSION_INVALID", "invalid json"
    except OSError:
        return None, "PERMISSION_INVALID", "cannot read state file"

    if not isinstance(data, dict):
        return None, "PERMISSION_INVALID", "state must be a json object"

    return data, None, None


def validate_state(data: dict):
    for field in REQUIRED_FIELDS:
        if field not in data:
            return "PERMISSION_INVALID", f"missing required field: {field}"

    current_permission = data.get("current_permission")
    if current_permission not in PERMISSION_RANK:
        return "PERMISSION_INVALID", "unknown current_permission"

    blocked_state = data.get("blocked_state")
    if not isinstance(blocked_state, bool):
        return "PERMISSION_INVALID", "blocked_state must be boolean"

    retry_count = data.get("retry_count")
    if not isinstance(retry_count, int) or retry_count < 0:
        return "PERMISSION_INVALID", "retry_count must be integer >= 0"

    open_violations = data.get("open_violations")
    if not isinstance(open_violations, list):
        return "PERMISSION_INVALID", "open_violations must be a list"

    expiration = data.get("expiration")
    if expiration is None:
        return "PERMISSION_EXPIRED", "expiration is null"
    if expiration != "never":
        if not isinstance(expiration, str):
            return "PERMISSION_INVALID", "expiration must be ISO 8601 UTC string or never"
        parsed = parse_utc_iso8601(expiration)
        if parsed is None:
            return "PERMISSION_INVALID", "invalid expiration format"
        if parsed <= datetime.now(timezone.utc):
            return "PERMISSION_EXPIRED", "permission state expired"

    if blocked_state or current_permission == "BLOCKED":
        return "PERMISSION_BLOCKED", "permission is blocked"

    return "PERMISSION_OK", "state is valid"


def run_validate(path: str) -> int:
    data, err_result, err_reason = load_state(path)
    if err_result:
        print_result(err_result, err_reason)
        return 1

    result, reason = validate_state(data)
    print_result(result, reason)
    return 0 if result == "PERMISSION_OK" else 1


def run_show(path: str) -> int:
    data, err_result, err_reason = load_state(path)
    if err_result:
        print_result(err_result, err_reason)
        return 1

    result, reason = validate_state(data)
    if result != "PERMISSION_OK":
        print_result(result, reason)
        return 1

    print(f"active_task_id: {data.get('active_task_id')}")
    print(f"agent_id: {data.get('agent_id')}")
    print(f"current_permission: {data.get('current_permission')}")
    print(f"open_violations_count: {len(data.get('open_violations', []))}")
    print(f"retry_count: {data.get('retry_count')}")
    print(f"expiration: {data.get('expiration')}")
    print_result("PERMISSION_OK", "state is valid")
    return 0


def run_check(path: str, required: str) -> int:
    data, err_result, err_reason = load_state(path)
    if err_result:
        print_result(err_result, err_reason)
        return 1

    result, reason = validate_state(data)
    if result != "PERMISSION_OK":
        print_result(result, reason)
        return 1

    if len(data.get("open_violations", [])) > 0:
        print_result("NEEDS_REVIEW", "open violations require human review")
        return 1

    current_permission = data.get("current_permission")
    if PERMISSION_RANK[current_permission] < PERMISSION_RANK[required]:
        print_result("PERMISSION_DENIED", "insufficient permission level")
        return 1

    print_result("PERMISSION_OK", "required permission level satisfied")
    return 0


def build_parser():
    parser = argparse.ArgumentParser(description="M27 permission state store checker")
    sub = parser.add_subparsers(dest="command", required=True)

    p_validate = sub.add_parser("validate")
    p_validate.add_argument("state_file")

    p_show = sub.add_parser("show")
    p_show.add_argument("state_file")

    p_check = sub.add_parser("check")
    p_check.add_argument("state_file")
    p_check.add_argument("--requires", required=True, choices=list(PERMISSION_RANK.keys()))

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "validate":
        return run_validate(args.state_file)
    if args.command == "show":
        return run_show(args.state_file)
    if args.command == "check":
        return run_check(args.state_file, args.requires)

    print_result("PERMISSION_INVALID", "unknown command")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
