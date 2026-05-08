#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

REQUIRED_FIELDS = [
    "schema_version",
    "repository",
    "checked_at",
    "checked_by",
    "level_2_enabled",
    "workflow_exists",
    "codeowners_exists",
    "branch_protection",
    "required_pr",
    "required_status_checks",
    "m27_enforcement_required",
    "m25_validation_required_if_present",
    "codeowners_review_required",
    "force_push_disabled",
    "branch_deletion_disabled",
    "bypass_permissions_restricted",
    "direct_push_restricted",
    "target_branches",
    "owner_admin_setup_actor",
    "evidence_source",
    "non_authorization_warning",
]

REQUIRED_BOOL_SETTINGS = [
    "branch_protection",
    "required_pr",
    "required_status_checks",
    "m27_enforcement_required",
    "codeowners_review_required",
    "force_push_disabled",
    "branch_deletion_disabled",
    "bypass_permissions_restricted",
    "direct_push_restricted",
]


def emit(result: str, reason: str, as_json: bool = False):
    if as_json:
        print(json.dumps({"result": result, "reason": reason}, ensure_ascii=True))
    else:
        print(f"RESULT: {result}")
        print(f"REASON: {reason}")


def load_state(path: str):
    p = Path(path)
    if not p.exists():
        return None, "PLATFORM_CHECK_INVALID", "platform state file missing"
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return None, "PLATFORM_CHECK_INVALID", "invalid platform state json"
    if not isinstance(data, dict):
        return None, "PLATFORM_CHECK_INVALID", "platform state must be object"
    return data, None, None


def check_artifacts_exist():
    if not Path(".github/workflows/m27-enforcement.yml").exists():
        return False, "workflow artifact missing"
    if not Path(".github/CODEOWNERS").exists():
        return False, "CODEOWNERS artifact missing"
    return True, "repo-side artifacts exist"


def evaluate_state(state: dict):
    for f in REQUIRED_FIELDS:
        if f not in state:
            return "PLATFORM_CHECK_INVALID", f"missing required field: {f}"

    if state.get("level_2_enabled") is not True:
        return "NEEDS_OWNER_ACTION", "platform state indicates level_2_enabled is not true"

    tb = state.get("target_branches")
    if not isinstance(tb, list):
        return "PLATFORM_CHECK_INVALID", "target_branches must be list"
    if "dev" not in tb or "main" not in tb:
        return "NEEDS_OWNER_ACTION", "target_branches must include dev and main"

    # Artifact consistency from provided evidence + repo files
    if not bool(state.get("workflow_exists")):
        return "PLATFORM_NOT_ENFORCED", "workflow_exists is false in platform state"
    if not bool(state.get("codeowners_exists")):
        return "PLATFORM_NOT_ENFORCED", "codeowners_exists is false in platform state"

    ok_art, art_reason = check_artifacts_exist()
    if not ok_art:
        return "PLATFORM_NOT_ENFORCED", art_reason

    for key in REQUIRED_BOOL_SETTINGS:
        val = state.get(key)
        if not isinstance(val, bool):
            return "PLATFORM_CHECK_INVALID", f"{key} must be boolean"
        if val is False:
            return "PLATFORM_PARTIAL", f"{key} is not enabled"

    # M25 validation check requirement behavior:
    # if present/configured it must be required, otherwise do not fail solely for absence.
    m25_val = state.get("m25_validation_required_if_present")
    if not isinstance(m25_val, bool):
        return "PLATFORM_CHECK_INVALID", "m25_validation_required_if_present must be boolean"

    return "PLATFORM_ENFORCED", "all required settings verified by provided evidence"


def show_requirements(as_json: bool):
    msg = {
        "required_branches": ["dev", "main"],
        "required_checks": ["M27 Enforcement", "M25 Validation (if present)"],
        "required_settings": REQUIRED_BOOL_SETTINGS,
        "status_note": "informational output only; not platform enforcement",
    }
    if as_json:
        print(json.dumps(msg, ensure_ascii=True))
    else:
        print("Required branches: dev, main")
        print("Required checks: M27 Enforcement; M25 Validation (if present)")
        print("Required settings:")
        for x in REQUIRED_BOOL_SETTINGS:
            print(f"- {x}")
    emit("NEEDS_REVIEW", "informational output only", as_json)
    return 0


def main():
    parser = argparse.ArgumentParser(description="Read-only GitHub platform enforcement checker")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--explain", action="store_true")
    sub = parser.add_subparsers(dest="cmd", required=True)

    pcheck = sub.add_parser("check")
    pcheck.add_argument("--level-2-enabled", required=True, choices=["true", "false"])
    pcheck.add_argument("--platform-state")

    sub.add_parser("show-requirements")

    args = parser.parse_args()

    if args.cmd == "show-requirements":
        return show_requirements(args.json)

    # check command
    if args.level_2_enabled == "false":
        emit("SKIPPED_LEVEL_2_NOT_ENABLED", "level 2 is disabled; valid skip status", args.json)
        return 0

    if not args.platform_state:
        emit("PLATFORM_CHECK_INVALID", "--platform-state is required when --level-2-enabled true", args.json)
        return 1

    state, er, rs = load_state(args.platform_state)
    if er:
        emit(er, rs, args.json)
        return 1

    result, reason = evaluate_state(state)
    emit(result, reason, args.json)
    return 0 if result in {"PLATFORM_ENFORCED", "SKIPPED_LEVEL_2_NOT_ENABLED"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
