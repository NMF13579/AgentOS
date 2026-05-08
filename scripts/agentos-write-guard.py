#!/usr/bin/env python3
import argparse
import json
import posixpath
import subprocess
from pathlib import Path, PurePosixPath

OPERATIONS = {"create", "modify", "append", "delete", "move", "overwrite"}
PATH_CLASSES = {
    "ALLOWED_WRITE_PATH",
    "CONDITIONAL_WRITE_PATH",
    "FORBIDDEN_WRITE_PATH",
    "PROTECTED_ZONE",
    "EVIDENCE_ARTIFACT",
    "GENERATED_ARTIFACT",
    "TEMP_ARTIFACT",
    "UNKNOWN_PATH",
}


def out(result: str, reason: str, as_json: bool = False):
    if as_json:
        print(json.dumps({"result": result, "reason": reason}, ensure_ascii=True))
    else:
        print(f"RESULT: {result}")
        print(f"REASON: {reason}")


def normalize_rel_path(raw: str):
    p = raw.strip()
    if not p:
        return None, "empty path"
    if p.startswith("/"):
        return None, "absolute paths are not allowed"
    if "\\" in p:
        p = p.replace("\\", "/")
    n = posixpath.normpath(p)
    if n == ".":
        return None, "path resolves to current directory"
    parts = PurePosixPath(n).parts
    if any(part == ".." for part in parts):
        return None, "path traversal is not allowed"
    if n.startswith("../"):
        return None, "path traversal is not allowed"
    return n, None


def is_completed_milestone_artifact(path: str):
    if path in {
        "docs/M27-TWO-LEVEL-CONTROL-ARCHITECTURE.md",
        "docs/M27-COMMAND-ENFORCEMENT-RUNTIME.md",
        "docs/PERMISSION-STATE-STORE.md",
        "scripts/agentos-permission-state.py",
        "scripts/agentos-command-guard.py",
    }:
        return True
    if path.startswith("docs/M25") or path.startswith("docs/M26"):
        return True
    return False


def valid_approval(path: str):
    f = Path(path)
    if not f.exists():
        return False, "approval record missing"
    try:
        data = json.loads(f.read_text(encoding="utf-8"))
    except Exception:
        return False, "approval record invalid json"
    if not isinstance(data, dict):
        return False, "approval record must be json object"
    if data.get("approved") is not True:
        return False, "approval record missing approved=true"
    if not data.get("task_id") or not data.get("approved_by"):
        return False, "approval record missing required fields"
    return True, "approval record valid"


def load_scope(scope_file: str):
    if not scope_file:
        return None, "scope file is missing"
    f = Path(scope_file)
    if not f.exists():
        return None, "scope file is missing"
    try:
        data = json.loads(f.read_text(encoding="utf-8"))
    except Exception:
        return None, "scope file invalid json"
    if not isinstance(data, dict):
        return None, "scope file must be object"
    paths = data.get("allowed_write_paths")
    if not isinstance(paths, list):
        return None, "scope file missing allowed_write_paths list"
    normalized = set()
    for p in paths:
        if not isinstance(p, str):
            return None, "scope path must be string"
        np, err = normalize_rel_path(p)
        if err:
            return None, f"invalid scope path: {p}"
        normalized.add(np)
    return normalized, None


def check_permission(permission_state_file: str):
    script = Path("scripts/agentos-permission-state.py")
    if not script.exists():
        return "PERMISSION_INVALID", "permission checker missing"
    try:
        run = subprocess.run(
            [
                "python3",
                "scripts/agentos-permission-state.py",
                "check",
                permission_state_file,
                "--requires",
                "LOCAL_EDIT",
            ],
            check=False,
            capture_output=True,
            text=True,
            timeout=10,
        )
    except Exception:
        return "PERMISSION_INVALID", "permission check failed"

    result = None
    for line in (run.stdout or "").splitlines():
        if line.startswith("RESULT:"):
            result = line.split(":", 1)[1].strip()
            break

    if result == "PERMISSION_OK":
        return "PERMISSION_OK", "permission check passed"
    if result == "PERMISSION_BLOCKED":
        return "PERMISSION_BLOCKED", "permission is blocked"
    if result == "PERMISSION_DENIED":
        return "PERMISSION_DENIED", "permission level is insufficient"
    if result == "NEEDS_REVIEW":
        return "WRITE_NEEDS_REVIEW", "open violations require review"
    return "PERMISSION_INVALID", "permission state invalid or expired"


def evaluate(args):
    if args.operation not in OPERATIONS:
        return "WRITE_NEEDS_REVIEW", "unknown operation"
    if args.path_class not in PATH_CLASSES:
        return "WRITE_NEEDS_REVIEW", "unknown path class"

    norm, err = normalize_rel_path(args.path)
    if err:
        if "absolute" in err:
            return "WRITE_NEEDS_REVIEW", err
        return "WRITE_POLICY_VIOLATION", err

    if args.path_class == "FORBIDDEN_WRITE_PATH":
        return "WRITE_BLOCKED", "forbidden write path"

    if args.path_class == "EVIDENCE_ARTIFACT":
        if args.operation in {"modify", "delete", "overwrite"}:
            return "WRITE_POLICY_VIOLATION", "evidence artifact tampering is forbidden"
        if args.operation == "append":
            return "WRITE_NEEDS_APPROVAL", "evidence append requires audit mechanism"

    if args.path_class == "PROTECTED_ZONE":
        if not args.approval_record:
            return "WRITE_NEEDS_APPROVAL", "protected zone requires approval"
        ok, reason = valid_approval(args.approval_record)
        if not ok:
            return "WRITE_NEEDS_APPROVAL", reason
        return "WRITE_NEEDS_REVIEW", "protected zone approval requires human review path"

    if is_completed_milestone_artifact(norm) and args.operation != "create":
        return "WRITE_BLOCKED", "completed milestone artifact modification is blocked"

    if args.path_class == "UNKNOWN_PATH":
        return "WRITE_NEEDS_REVIEW", "unknown path class fails closed"

    if args.path_class == "GENERATED_ARTIFACT" and args.operation not in {"create", "overwrite", "modify"}:
        return "WRITE_BLOCKED", "generated artifact operation is not allowed"

    if args.path_class == "TEMP_ARTIFACT":
        if not (norm.startswith("tmp/") or norm.startswith("temp/") or norm.startswith(".tmp/")):
            return "WRITE_BLOCKED", "temp artifact must be under temp path"

    if args.operation in {"delete", "move"}:
        if not args.approval_record:
            return "WRITE_NEEDS_APPROVAL", "delete/move requires explicit approval"
        ok, reason = valid_approval(args.approval_record)
        if not ok:
            return "WRITE_NEEDS_APPROVAL", reason
        return "WRITE_NEEDS_REVIEW", "approved delete/move still requires human review path"

    if args.path_class == "CONDITIONAL_WRITE_PATH":
        if not args.scope_file:
            return "WRITE_NEEDS_REVIEW", "conditional path requires scope file"

    if args.path_class in {"CONDITIONAL_WRITE_PATH", "UNKNOWN_PATH"} or args.scope_file:
        allowed_paths, scope_err = load_scope(args.scope_file)
        if scope_err:
            return "WRITE_NEEDS_REVIEW", scope_err
        if norm not in allowed_paths:
            return "WRITE_BLOCKED", "path is out of declared scope"

    if args.permission_state:
        p_res, p_reason = check_permission(args.permission_state)
        if p_res != "PERMISSION_OK":
            return p_res, p_reason

    return "WRITE_ALLOWED", "write request passed guard checks"


def main():
    parser = argparse.ArgumentParser(description="M27 write guard")
    sub = parser.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("check")
    p.add_argument("--path", required=True)
    p.add_argument("--operation", required=True)
    p.add_argument("--path-class", required=True)
    p.add_argument("--permission-state")
    p.add_argument("--scope-file")
    p.add_argument("--approval-record")
    p.add_argument("--explain", action="store_true")
    p.add_argument("--json", action="store_true")

    args = parser.parse_args()
    if args.cmd != "check":
        out("WRITE_NEEDS_REVIEW", "unknown subcommand", args.json)
        return 1

    result, reason = evaluate(args)
    if args.explain:
        reason = f"{reason}; normalized_path={normalize_rel_path(args.path)[0] if normalize_rel_path(args.path)[0] else 'n/a'}"
    out(result, reason, args.json)
    return 0 if result == "WRITE_ALLOWED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
