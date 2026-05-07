#!/usr/bin/env python3
import argparse
import json
import re
import subprocess
from pathlib import Path

ACTIONS = {"commit", "push", "merge", "tag", "remote-delete", "force-push", "status"}
TARGETS = {"local", "feature_branch", "dev", "main", "protected_branch", "unknown"}

UNSAFE_BRANCH_PATTERNS = [
    "..", "$(`", "$(", "`", ";", "&&", "||", ">", "<", "\n", "\r"
]


def emit(result: str, reason: str, as_json: bool = False):
    if as_json:
        print(json.dumps({"result": result, "reason": reason}, ensure_ascii=True))
    else:
        print(f"RESULT: {result}")
        print(f"REASON: {reason}")


def norm_branch(branch: str):
    if branch is None:
        return None
    return branch.strip()


def unsafe_branch(branch: str) -> bool:
    if not branch:
        return True
    for marker in UNSAFE_BRANCH_PATTERNS:
        if marker in branch:
            return True
    return False


def permission_required(action: str):
    if action == "commit":
        return "COMMIT_REQUEST"
    if action == "push":
        return "PUSH_REQUEST"
    if action == "status":
        return "READ_ONLY"
    return None


def check_permission(path: str, required: str):
    script = Path("scripts/agentos-permission-state.py")
    if not script.exists():
        return "GIT_NEEDS_REVIEW", "permission script missing"

    try:
        proc = subprocess.run(
            ["python3", "scripts/agentos-permission-state.py", "check", path, "--requires", required],
            check=False,
            capture_output=True,
            text=True,
            timeout=10,
        )
    except Exception:
        return "PERMISSION_INVALID", "permission check execution failed"

    result = None
    for line in (proc.stdout or "").splitlines():
        if line.startswith("RESULT:"):
            result = line.split(":", 1)[1].strip()
            break

    if result == "PERMISSION_OK":
        return "PERMISSION_OK", "permission check passed"
    if result == "PERMISSION_BLOCKED":
        return "PERMISSION_BLOCKED", "permission is blocked"
    if result == "PERMISSION_DENIED":
        return "PERMISSION_DENIED", "permission denied"
    if result == "NEEDS_REVIEW":
        return "GIT_NEEDS_REVIEW", "open violations require review"
    return "PERMISSION_INVALID", "permission invalid or expired"


def load_precondition(path: str):
    p = Path(path)
    if not p.exists():
        return None, "PRECONDITION_INVALID", "precondition file missing"
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return None, "PRECONDITION_INVALID", "precondition file invalid json"
    if not isinstance(data, dict):
        return None, "PRECONDITION_INVALID", "precondition must be object"
    result = data.get("result")
    if not isinstance(result, str):
        return None, "PRECONDITION_INVALID", "precondition result missing"
    return result.strip(), None, None


def check_approval(path: str):
    p = Path(path)
    if not p.exists():
        return False, "approval record missing"
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return False, "approval record invalid json"
    if not isinstance(data, dict):
        return False, "approval record must be object"
    need = ["approved", "task_id", "approved_by", "approval_scope"]
    for f in need:
        if f not in data:
            return False, f"approval record missing {f}"
    if data.get("approved") is not True:
        return False, "approval record approved must be true"
    return True, "approval record valid"


def has_task_id_in_message(msg: str) -> bool:
    return bool(re.search(r"\b\d+\.\d+\.\d+\b", msg or ""))


def evaluate(args):
    action = args.action.strip().lower()
    target = args.target.strip()
    branch = norm_branch(args.branch)

    # 3. absolute policy violations
    if action == "force-push":
        return "GIT_POLICY_VIOLATION", "force-push is always blocked"
    if action == "remote-delete":
        return "GIT_POLICY_VIOLATION", "remote branch deletion is always blocked"
    if action == "merge":
        return "GIT_POLICY_VIOLATION", "merge is blocked by runtime boundary"

    # 4. validate action/target
    if action not in ACTIONS:
        return "GIT_NEEDS_REVIEW", "unknown action"
    if target not in TARGETS:
        return "GIT_NEEDS_REVIEW", "unknown target"

    # 5. branch safety
    if action == "push":
        if not branch:
            return "GIT_NEEDS_REVIEW", "push requires branch"
        if unsafe_branch(branch):
            return "GIT_POLICY_VIOLATION", "unsafe branch content"
        if target == "dev" or branch == "dev":
            return "GIT_POLICY_VIOLATION", "direct push to dev is blocked"
        if target == "main" or branch == "main":
            return "GIT_POLICY_VIOLATION", "direct push to main is blocked"
        if target == "protected_branch":
            return "GIT_BLOCKED", "push to protected branch is blocked"
        if target == "unknown":
            return "GIT_NEEDS_REVIEW", "unknown push target"

    # status/tag behavior
    if action == "tag":
        return "GIT_NEEDS_REVIEW", "tag is not enabled by this guard"

    # 6. permission
    req = permission_required(action)
    if args.permission_state and req:
        p_res, p_reason = check_permission(args.permission_state, req)
        if p_res != "PERMISSION_OK":
            return p_res, p_reason

    # 7. precondition
    if action in {"commit", "push"}:
        if not args.precondition_result:
            return "GIT_NEEDS_REVIEW", "missing precondition result"
        precond, err_res, err_reason = load_precondition(args.precondition_result)
        if err_res:
            return err_res, err_reason

        if precond == "BLOCKED":
            return "GIT_BLOCKED", "precondition blocked"
        if precond == "NEEDS_APPROVAL":
            return "GIT_NEEDS_APPROVAL", "precondition requires approval"
        if precond == "NEEDS_REVIEW":
            return "GIT_NEEDS_REVIEW", "precondition requires review"

        if action == "commit" and precond != "COMMIT_ALLOWED":
            return "PRECONDITION_INVALID", "commit requires COMMIT_ALLOWED"
        if action == "push" and precond != "PUSH_ALLOWED":
            return "PRECONDITION_INVALID", "push requires PUSH_ALLOWED"

    # 8. optional approval support evidence only
    if args.approval_record:
        ok, reason = check_approval(args.approval_record)
        if not ok:
            return "GIT_NEEDS_REVIEW", reason
        if action == "push" and (target in {"dev", "main", "protected_branch"}):
            return "GIT_POLICY_VIOLATION", "approval cannot allow protected push"

    # 9. commit message/task id
    if action == "commit":
        if not args.commit_message:
            return "GIT_NEEDS_REVIEW", "commit requires --commit-message"
        if not args.task_id and not has_task_id_in_message(args.commit_message):
            return "GIT_NEEDS_REVIEW", "commit requires --task-id or task id in message"

    # 10. final
    if action == "status":
        return "GIT_ALLOWED", "status check is allowed"
    if action == "commit":
        return "GIT_ALLOWED", "commit request passed guard checks"
    if action == "push":
        if target != "feature_branch":
            return "GIT_NEEDS_REVIEW", "push target requires review"
        return "GIT_ALLOWED", "push request passed guard checks"

    return "GIT_NEEDS_REVIEW", "action is not enabled"


def main():
    parser = argparse.ArgumentParser(description="M27 git guard")
    sub = parser.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("check")
    p.add_argument("--action", required=True)
    p.add_argument("--target", required=True)
    p.add_argument("--branch")
    p.add_argument("--permission-state")
    p.add_argument("--precondition-result")
    p.add_argument("--approval-record")
    p.add_argument("--commit-message")
    p.add_argument("--task-id")
    p.add_argument("--explain", action="store_true")
    p.add_argument("--json", action="store_true")

    args = parser.parse_args()
    if args.cmd != "check":
        emit("GIT_NEEDS_REVIEW", "unknown subcommand", args.json)
        return 1

    result, reason = evaluate(args)
    if args.explain:
        reason = f"{reason}; action={args.action}; target={args.target}; branch={args.branch or 'n/a'}"

    emit(result, reason, args.json)
    return 0 if result == "GIT_ALLOWED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
