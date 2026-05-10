#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "scripts" / "check-single-role-execution.py"
FIXTURES_DIR = ROOT / "tests" / "fixtures" / "single-role-execution"

def run_test(task_file, changed_files=None, strict=False):
    cmd = [sys.executable, str(CHECKER), str(task_file)]
    if changed_files:
        cmd.extend(["--changed-files", str(changed_files)])
    if strict:
        cmd.append("--strict")
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode, result.stdout.strip()

def main():
    tests = [
        # Valid fixtures (Exit 0)
        {"file": "valid/valid-auditor-readonly-report-only.md", "expected_code": 0, "expected_token": "SINGLE_ROLE_OK"},
        {"file": "valid/valid-implementor-scoped-write.md", "expected_code": 0, "expected_token": "SINGLE_ROLE_OK"},
        {"file": "valid/valid-planner-plan-only.md", "expected_code": 0, "expected_token": "SINGLE_ROLE_OK"},
        
        # Invalid fixtures (Exit 1)
        {"file": "invalid/invalid-missing-execution-role.md", "expected_code": 1, "expected_token": "SINGLE_ROLE_INVALID_CONTRACT"},
        {"file": "invalid/invalid-unknown-role.md", "expected_code": 1, "expected_token": "SINGLE_ROLE_VIOLATION"},
        {"file": "invalid/invalid-auditor-with-scoped-write.md", "expected_code": 1, "expected_token": "SINGLE_ROLE_VIOLATION"},
        {"file": "invalid/invalid-broad-write-path-root.md", "expected_code": 1, "expected_token": "SINGLE_ROLE_VIOLATION"},
        {"file": "invalid/invalid-role-scope-too-many-paths.md", "expected_code": 1, "expected_token": "SINGLE_ROLE_VIOLATION"},
        {"file": "invalid/invalid-maintainer-self-policy-edit.md", "expected_code": 1, "expected_token": "SINGLE_ROLE_VIOLATION"},

        # Runtime Changed Files scenarios
        {"file": "valid/valid-auditor-readonly-report-only.md", "changed": "changed-files/auditor-report-only-pass.txt", "expected_code": 0, "expected_token": "SINGLE_ROLE_OK"},
        {"file": "valid/valid-auditor-readonly-report-only.md", "changed": "changed-files/auditor-modifies-src-fail.txt", "expected_code": 1, "expected_token": "SINGLE_ROLE_VIOLATION"},
        {"file": "valid/valid-implementor-scoped-write.md", "changed": "changed-files/implementor-in-scope-pass.txt", "expected_code": 0, "expected_token": "SINGLE_ROLE_OK"},
        {"file": "valid/valid-implementor-scoped-write.md", "changed": "changed-files/implementor-modifies-validator-needs-review.txt", "expected_code": 1, "expected_token": "SINGLE_ROLE_NEEDS_REVIEW"},
        {"file": "valid/valid-maintainer-maintenance-scoped.md", "changed": "changed-files/maintainer-self-policy-edit-fail.txt", "expected_code": 1, "expected_token": "SINGLE_ROLE_VIOLATION"},
        {"file": "valid/valid-maintainer-maintenance-scoped.md", "changed": "changed-files/maintainer-normal-doc-pass.txt", "expected_code": 0, "expected_token": "SINGLE_ROLE_OK"},
    ]

    failed = 0
    for t in tests:
        task_path = FIXTURES_DIR / t["file"]
        changed_path = FIXTURES_DIR / t["changed"] if "changed" in t else None
        
        code, output = run_test(task_path, changed_path)
        token = output.split(":")[0] if ":" in output else output
        
        if code == t["expected_code"] and token == t["expected_token"]:
            print(f"[PASS] {t['file']} (changed: {t.get('changed', 'NONE')})")
        else:
            print(f"[FAIL] {t['file']} (changed: {t.get('changed', 'NONE')})")
            print(f"  Expected: {t['expected_token']} (code {t['expected_code']})")
            print(f"  Actual:   {token} (code {code})")
            print(f"  Output:   {output}")
            failed += 1

    if failed > 0:
        print(f"\nResult: {failed} tests failed.")
        sys.exit(1)
    else:
        print("\nResult: All single-role execution fixture tests passed.")
        sys.exit(0)

if __name__ == "__main__":
    main()
