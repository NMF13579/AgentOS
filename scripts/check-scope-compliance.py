#!/usr/bin/env python3
import re
import subprocess
import json
import sys
import argparse
import os
from pathlib import Path


REQUIRED_SCOPE_FIELDS = [
    "allowed_paths",
    "forbidden_paths",
    "allow_new_files",
    "allowed_new_files",
    "forbidden_new_files",
    "allow_modify_existing",
    "allow_deletes",
    "allow_renames",
    "sensitive_paths",
]

CMD_GIT_DIFF_NAME_STATUS = "git diff --name-status"
CMD_GIT_DIFF_NAME_STATUS_CACHED = "git diff --name-status --cached"
CMD_GIT_LS_OTHERS = "git ls-files --others --exclude-standard"


class ScopeArgParser(argparse.ArgumentParser):
    def error(self, message):
        raise ValueError(message)


def parse_args(argv):
    parser = ScopeArgParser(add_help=True)
    parser.add_argument("--task", required=True)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--json", action="store_true")
    return parser.parse_args(argv)


def read_task(path):
    try:
        return Path(path).read_text(encoding="utf-8")
    except Exception:
        return None


def is_idle_state(task_text: str) -> bool:
    """Return True when active-task.md is in legitimate idle/no-active-task state."""
    text_lower = task_text.lower()
    if "no active task" in text_lower:
        return True
    if re.search(r"^status:\s*(none|idle)\s*$", task_text, re.MULTILINE):
        return True
    has_scope = "scope_control:" in task_text
    has_contract = "## Contract" in task_text or "contract:" in task_text
    if not has_scope and not has_contract:
        return True
    return False


def parse_scope_control(text):
    lines = text.splitlines()
    start_index = -1
    for idx, line in enumerate(lines):
        if re.match(r"^\s*scope_control:\s*$", line):
            start_index = idx
            break
    if start_index < 0:
        return None, "missing_scope_control"

    scope = {}
    current_list_key = None
    saw_nested = False

    for idx in range(start_index + 1, len(lines)):
        raw = lines[idx]
        if re.match(r"^\s*$", raw):
            continue
        if re.match(r"^\S", raw):
            break

        if re.match(r"^\s{2}[a-z_][a-z0-9_]*:\s*(.*)$", raw):
            m = re.match(r"^\s{2}([a-z_][a-z0-9_]*):\s*(.*)$", raw)
            key = m.group(1)
            value = m.group(2).strip()
            current_list_key = None
            saw_nested = True

            if value == "":
                scope[key] = []
                current_list_key = key
                continue

            if value.lower() == "true":
                scope[key] = True
                continue
            if value.lower() == "false":
                scope[key] = False
                continue

            return None, "parse_error"

        if re.match(r"^\s{4}-\s+.+$", raw):
            if current_list_key is None:
                return None, "parse_error"
            item = re.sub(r"^\s{4}-\s+", "", raw).strip()
            scope[current_list_key].append(item)
            saw_nested = True
            continue

        return None, "parse_error"

    if not saw_nested:
        return None, "parse_error"
    return scope, None


def match_path(pattern, path):
    if pattern.endswith("/"):
        return path == pattern[:-1] or path.startswith(pattern)
    return path == pattern


def match_any(patterns, path):
    for pattern in patterns:
        if match_path(pattern, path):
            return True
    return False


def run_git(repo_root, args):
    proc = subprocess.run(
        ["git"] + args,
        cwd=repo_root,
        text=True,
        capture_output=True,
    )
    if proc.returncode != 0:
        return None, proc.stderr.strip() or proc.stdout.strip() or "git_failed"
    return proc.stdout.splitlines(), None


def parse_name_status(lines, staged):
    records = []
    for line in lines:
        if not line.strip():
            continue
        parts = line.split("\t")
        code = parts[0]
        base = code[0]
        if base == "R":
            if len(parts) < 3:
                return None, "parse_error"
            records.append(
                {
                    "status": "R",
                    "path": parts[2],
                    "old_path": parts[1],
                    "staged": staged,
                }
            )
        elif base in ["M", "A", "D"]:
            if len(parts) < 2:
                return None, "parse_error"
            records.append(
                {
                    "status": base,
                    "path": parts[1],
                    "staged": staged,
                }
            )
    return records, None


def collect_evidence(repo_root):
    unstaged_lines, err = run_git(repo_root, CMD_GIT_DIFF_NAME_STATUS.split()[1:])
    if err is not None:
        return None, err
    staged_lines, err = run_git(repo_root, CMD_GIT_DIFF_NAME_STATUS_CACHED.split()[1:])
    if err is not None:
        return None, err
    untracked_lines, err = run_git(repo_root, CMD_GIT_LS_OTHERS.split()[1:])
    if err is not None:
        return None, err

    unstaged_records, err = parse_name_status(unstaged_lines, staged=False)
    if err is not None:
        return None, err
    staged_records, err = parse_name_status(staged_lines, staged=True)
    if err is not None:
        return None, err

    records = unstaged_records + staged_records
    for line in untracked_lines:
        p = line.strip()
        if p:
            records.append({"status": "A", "path": p, "staged": False, "untracked": True})

    dedup = {}
    for record in records:
        key = (
            record.get("status"),
            record.get("old_path", ""),
            record.get("path"),
            record.get("staged", False),
            record.get("untracked", False),
        )
        dedup[key] = record
    records = list(dedup.values())

    changed_paths = {}
    for record in records:
        changed_paths[record["path"]] = True
    changed_files = sorted(changed_paths.keys())
    return {"records": records, "changed_files": changed_files}, None


def validate_scope_fields(scope):
    missing = []
    for field in REQUIRED_SCOPE_FIELDS:
        if field not in scope:
            missing.append(field)
    return missing


def check_compliance(scope, evidence):
    violations = []
    warnings = []
    failed_paths = {}

    allowed_paths = scope["allowed_paths"]
    forbidden_paths = scope["forbidden_paths"]
    allow_new_files = scope["allow_new_files"]
    allowed_new_files = scope["allowed_new_files"]
    forbidden_new_files = scope["forbidden_new_files"]
    allow_modify_existing = scope["allow_modify_existing"]
    allow_deletes = scope["allow_deletes"]
    allow_renames = scope["allow_renames"]
    sensitive_paths = scope["sensitive_paths"]

    for name in ["allowed_paths", "forbidden_paths", "allowed_new_files", "forbidden_new_files", "sensitive_paths"]:
        if not isinstance(scope[name], list):
            return None, None, "parse_error"
    for name in ["allow_new_files", "allow_modify_existing", "allow_deletes", "allow_renames"]:
        if not isinstance(scope[name], bool):
            return None, None, "parse_error"

    for rec in evidence["records"]:
        status = rec["status"]
        path = rec["path"]

        if match_any(forbidden_paths, path):
            violations.append(f"forbidden path changed: {path}")
            failed_paths[path] = True

        if status == "R":
            if not allow_renames:
                violations.append(f"rename not allowed: {path}")
                failed_paths[path] = True
            if not match_any(allowed_paths, path):
                violations.append(f"changed file outside allowed_paths: {path}")
                failed_paths[path] = True
        elif status == "M":
            if not allow_modify_existing:
                violations.append(f"modify not allowed: {path}")
                failed_paths[path] = True
            if not match_any(allowed_paths, path):
                violations.append(f"changed file outside allowed_paths: {path}")
                failed_paths[path] = True
        elif status == "D":
            if not allow_deletes:
                violations.append(f"delete not allowed: {path}")
                failed_paths[path] = True
            if not match_any(allowed_paths, path):
                violations.append(f"changed file outside allowed_paths: {path}")
                failed_paths[path] = True
        elif status == "A":
            if not allow_new_files:
                violations.append(f"new file not allowed: {path}")
                failed_paths[path] = True
            if not match_any(allowed_new_files, path):
                violations.append(f"new file outside allowed_new_files: {path}")
                failed_paths[path] = True
            if match_any(forbidden_new_files, path):
                violations.append(f"new file matches forbidden_new_files: {path}")
                failed_paths[path] = True
        else:
            violations.append(f"unknown status evidence: {status} {path}")
            failed_paths[path] = True

    for path in evidence["changed_files"]:
        if match_any(sensitive_paths, path) and path not in failed_paths:
            warnings.append(f"sensitive path changed: {path}")

    return violations, warnings, None


def make_result(result, evidence, violations, warnings, reason):
    human_action_required = result in ["FAIL", "WARN", "ERROR"]
    payload = {
        "result": result,
        "changed_files_count": len(evidence["changed_files"]),
        "violations_count": len(violations),
        "warnings_count": len(warnings),
        "human_action_required": human_action_required,
        "changed_files": evidence["records"],
        "violations": violations,
        "warnings": warnings,
        "reason": reason,
    }
    return payload


def print_human(payload):
    print(f"Scope Compliance: {payload['result']}")
    print(f"Changed files: {payload['changed_files_count']}")
    print(f"Violations: {payload['violations_count']}")
    print(f"Warnings: {payload['warnings_count']}")
    print(f"Human action required: {'YES' if payload['human_action_required'] else 'NO'}")
    print(f"Reason: {payload['reason']}")
    if payload["violations"]:
        print("Violation details:")
        for item in payload["violations"]:
            print(f"- {item}")
    if payload["warnings"]:
        print("Warning details:")
        for item in payload["warnings"]:
            print(f"- {item}")


def main(argv):
    try:
        args = parse_args(argv)
    except Exception:
        payload = make_result("ERROR", {"changed_files": [], "records": []}, [], [], "invalid CLI arguments")
        print_human(payload)
        return 3

    repo_root = Path(args.repo_root).resolve()
    if not repo_root.exists() or not repo_root.is_dir():
        payload = make_result("ERROR", {"changed_files": [], "records": []}, [], [], "invalid repository root")
        if args.json:
            print(json.dumps(payload, indent=2))
        else:
            print_human(payload)
        return 3

    task_text = read_task(args.task)
    if task_text is None:
        payload = make_result("ERROR", {"changed_files": [], "records": []}, [], [], "task file cannot be read")
        if args.json:
            print(json.dumps(payload, indent=2))
        else:
            print_human(payload)
        return 3

    scope, parse_state = parse_scope_control(task_text)
    if parse_state == "missing_scope_control":
        if is_idle_state(task_text):
            payload = make_result("PASS", {"changed_files": [], "records": []}, [], [], "idle state - no active task")
            if args.json:
                print(json.dumps(payload, indent=2))
            else:
                print_human(payload)
            return 0
        payload = make_result("FAIL", {"changed_files": [], "records": []}, ["scope_control is missing"], [], "scope block missing")
        if args.json:
            print(json.dumps(payload, indent=2))
        else:
            print_human(payload)
        return 1
    if parse_state is not None:
        payload = make_result("ERROR", {"changed_files": [], "records": []}, [], [], "scope block parse failed")
        if args.json:
            print(json.dumps(payload, indent=2))
        else:
            print_human(payload)
        return 3

    missing_fields = validate_scope_fields(scope)
    if missing_fields:
        payload = make_result(
            "FAIL",
            {"changed_files": [], "records": []},
            [f"missing required scope field: {name}" for name in missing_fields],
            [],
            "scope block missing required fields",
        )
        if args.json:
            print(json.dumps(payload, indent=2))
        else:
            print_human(payload)
        return 1

    evidence, err = collect_evidence(str(repo_root))
    if err is not None:
        payload = make_result("ERROR", {"changed_files": [], "records": []}, [], [], "git evidence collection failed")
        if args.json:
            print(json.dumps(payload, indent=2))
        else:
            print_human(payload)
        return 3

    violations, warnings, err = check_compliance(scope, evidence)
    if err is not None:
        payload = make_result("ERROR", evidence, [], [], "scope values are invalid")
        if args.json:
            print(json.dumps(payload, indent=2))
        else:
            print_human(payload)
        return 3

    if violations:
        payload = make_result("FAIL", evidence, violations, warnings, "scope violations detected")
        code = 1
    elif warnings:
        payload = make_result("WARN", evidence, violations, warnings, "sensitive path changes detected")
        code = 2
    else:
        payload = make_result("PASS", evidence, violations, warnings, "no scope issues detected")
        code = 0

    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print_human(payload)
    return code


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except Exception:
        payload = {
            "result": "ERROR",
            "changed_files_count": 0,
            "violations_count": 0,
            "warnings_count": 0,
            "human_action_required": True,
            "changed_files": [],
            "violations": [],
            "warnings": [],
            "reason": "unexpected exception",
        }
        print_human(payload)
        sys.exit(3)
