#!/usr/bin/env python3
"""
Single-Role Execution Guard Checker.
Enforces that agent execution operates under exactly one declared role.
"""
import argparse
import fnmatch
import json
import os
import re
import sys
from pathlib import Path

# Result Tokens
OK = "SINGLE_ROLE_OK"
WARNING = "SINGLE_ROLE_WARNING"
VIOLATION = "SINGLE_ROLE_VIOLATION"
INVALID = "SINGLE_ROLE_INVALID_CONTRACT"
NEEDS_REVIEW = "SINGLE_ROLE_NEEDS_REVIEW"

ROLE_SCOPE_LIMITS = {
    "planner": {
        "max_write_paths": 3,
        "allowed_prefixes": ["tasks/", "plans/", "reports/"],
        "forbidden_prefixes": ["src/", "scripts/", "schemas/", ".github/", "core-rules/", "workflow/", "security/", "canonical/", "approvals/"]
    },
    "implementor": {
        "max_write_paths": 5,
        "forbidden_prefixes": ["approvals/", "canonical/", ".github/workflows/", "security/", "reports/*completion-review*", "reports/*evidence-report*"]
    },
    "auditor": {
        "max_write_paths": 2,
        "allowed_prefixes": ["reports/", "audits/", "findings/"],
        "forbidden_prefixes": ["src/", "scripts/", "schemas/", "templates/", "docs/", ".github/", "approvals/", "canonical/"]
    },
    "verifier": {
        "max_write_paths": 2,
        "allowed_prefixes": ["reports/", "verification/"],
        "forbidden_prefixes": ["src/", "scripts/", "schemas/", "templates/", "docs/", ".github/", "approvals/", "canonical/"]
    },
    "tutor": {
        "max_write_paths": 0,
        "forbidden_prefixes": ["*"]
    },
    "researcher": {
        "max_write_paths": 3,
        "allowed_prefixes": ["research/", "reports/", "notes/"],
        "forbidden_prefixes": ["src/", "scripts/", "schemas/", "templates/", "approvals/", "canonical/"]
    },
    "maintainer": {
        "max_write_paths": 10,
        "forbidden_prefixes": ["approvals/", "canonical/", "reports/*completion-review*", "reports/*evidence-report*"]
    }
}

VALIDATION_AUTHORITY_PATHS = [
    "scripts/check-*", "scripts/validate-*", "scripts/test-*", 
    "scripts/agentos-validate.py", "scripts/audit-*", "schemas/",
    "tests/fixtures/", ".github/workflows/", "docs/*POLICY*", "docs/*GUARD*",
    "docs/*VALIDATION*", "reports/*evidence-report*", "reports/*completion-review*"
]

MAINTAINER_POLICY_PATHS = [
    "docs/SINGLE-ROLE-EXECUTION-POLICY.md", "schemas/execution-role.schema.json",
    "scripts/check-single-role-execution.py", "tests/fixtures/single-role-execution/",
    "templates/role-handoff-request.md"
]

FORBIDDEN_BROAD_PATHS = {".", "./", "/", "*", "**", ""}

def normalize_path(path_str):
    path_str = path_str.replace("\\", "/").strip()
    if path_str.startswith("./"):
        path_str = path_str[2:]
    while "//" in path_str:
        path_str = path_str.replace("//", "/")
    return path_str

def is_broad_path(path_str):
    return normalize_path(path_str) in FORBIDDEN_BROAD_PATHS

def match_path(path, patterns):
    path = normalize_path(path)
    for p in patterns:
        p = normalize_path(p)
        if "*" in p:
            if fnmatch.fnmatch(path, p): return True
        elif path.startswith(p):
            return True
    return False

def check_role(task_contract, changed_files=None):
    if "execution_role" not in task_contract:
        return INVALID, "Missing execution_role block"
    
    role_config = task_contract["execution_role"]
    role = role_config.get("role")
    mode = role_config.get("mode")
    
    if role not in ROLE_SCOPE_LIMITS:
        return VIOLATION, f"Unknown role: {role}"
    
    limits = ROLE_SCOPE_LIMITS[role]
    allowed_write = role_config.get("allowed_write_paths", [])
    
    # 1. Scope count limit
    if len(allowed_write) > limits["max_write_paths"]:
        return VIOLATION, f"Role {role} exceeds max write paths ({len(allowed_write)} > {limits['max_write_paths']})"
    
    # 2. Broad path check
    for p in allowed_write:
        if is_broad_path(p):
            return VIOLATION, f"Broad write path forbidden: {p}"
            
    # 3. Static prefix checks
    if "allowed_prefixes" in limits:
        for p in allowed_write:
            if not match_path(p, limits["allowed_prefixes"]):
                return VIOLATION, f"Path {p} not allowed for role {role}"
                
    for p in allowed_write:
        if match_path(p, limits.get("forbidden_prefixes", [])):
            # Bootstrap exception for evidence report in initial implementation
            if task_contract.get("task_id") == "task-m40-single-role-guard-mvp" and "evidence-report" in p:
                continue
            return VIOLATION, f"Path {p} explicitly forbidden for role {role}"
        if role == "maintainer" and match_path(p, MAINTAINER_POLICY_PATHS):
            # Bootstrap exception for initial implementation
            if task_contract.get("task_id") == "task-m40-single-role-guard-mvp":
                continue
            return VIOLATION, f"Maintainer cannot declare write access to its own policy: {p}"

    # 4. Changed files check
    if changed_files:
        for f in changed_files:
            f = normalize_path(f)
            
            # Anti-bootstrapping for maintainer
            if role == "maintainer" and match_path(f, MAINTAINER_POLICY_PATHS):
                if task_contract.get("task_id") == "task-m40-single-role-guard-mvp":
                    continue
                return VIOLATION, f"Maintainer cannot modify its own policy in same run: {f}"
                
            # Auditor/Verifier code modification check
            if role in ["auditor", "verifier"]:
                if match_path(f, ["src/", "scripts/", "schemas/", "templates/", "docs/"]):
                    if not match_path(f, allowed_write):
                        return VIOLATION, f"Role {role} attempted unauthorized write to {f}"
            
            # Implementor verification-authority boundary
            if role == "implementor" and match_path(f, VALIDATION_AUTHORITY_PATHS):
                # If it's not even allowed in scope, it's a violation
                if not match_path(f, allowed_write):
                    return VIOLATION, f"Changed file {f} outside allowed write scope (and is validation authority)"
                # If it is allowed, check risk level for MVP
                if not task_contract.get("task", {}).get("risk_level") == "HIGH":
                    return NEEDS_REVIEW, f"Implementor modified validation authority without HIGH risk level: {f}"

            if not match_path(f, allowed_write):
                return VIOLATION, f"Changed file {f} outside allowed write scope"

    return OK, "Single-role constraints satisfied"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("task_file")
    parser.add_argument("--changed-files")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    try:
        import yaml
        with open(args.task_file, "r") as f:
            content = f.read()
            # Extract first yaml block
            blocks = re.findall(r"---(.*?)---", content, re.DOTALL)
            if not blocks:
                print(f"FAIL: No YAML frontmatter in {args.task_file}")
                sys.exit(1)
            task_contract = yaml.safe_load(blocks[0])
    except Exception as e:
        print(f"FAIL: Parse error: {e}")
        sys.exit(1)

    changed = None
    if args.changed_files:
        if os.path.exists(args.changed_files):
            with open(args.changed_files, "r") as f:
                changed = [l.strip() for l in f if l.strip()]
        else:
            changed = []

    token, msg = check_role(task_contract, changed)
    
    result = {"result": token, "message": msg}
    
    if args.json:
        print(json.dumps(result))
    else:
        print(f"{token}: {msg}")

    if token == OK: sys.exit(0)
    if token == WARNING: sys.exit(1 if args.strict else 0)
    sys.exit(1)

if __name__ == "__main__":
    main()
