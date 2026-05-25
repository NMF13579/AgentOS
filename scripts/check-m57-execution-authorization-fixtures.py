#!/usr/bin/env python3
import argparse
import json
import subprocess
import sys
import dataclasses
import pathlib
import typing

M57_FIXTURE_RUNNER_PASS = "M57_FIXTURE_RUNNER_PASS"
M57_FIXTURE_RUNNER_FAIL = "M57_FIXTURE_RUNNER_FAIL"
M57_FIXTURE_RUNNER_BLOCKED = "M57_FIXTURE_RUNNER_BLOCKED"

CASE_PASS = "CASE_PASS"
CASE_FAIL = "CASE_FAIL"
CASE_BLOCKED = "CASE_BLOCKED"

EXIT_RUNNER_PASS = 0
EXIT_RUNNER_FAIL = 1
EXIT_RUNNER_BLOCKED = 2

TIMEOUT_SECONDS = 30

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fixtures-root", default="tests/fixtures/execution-authorization")
    parser.add_argument("--positive", action="store_true")
    parser.add_argument("--negative", action="store_true")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--explain", action="store_true")
    return parser.parse_args()

def load_manifest(path):
    p = pathlib.Path(path)
    if not p.is_file():
        raise FileNotFoundError(f"Manifest not found: {path}")
    return json.loads(p.read_text(encoding="utf-8"))

def reject_protected_path(path_str):
    p = pathlib.Path(path_str).resolve()
    for protected in ["tasks", "approvals", "generated"]:
        if p.parts[-1] == protected or any(part == protected for part in p.parts):
            raise ValueError(f"Path into protected directory: {path_str}")

def resolve_fixture_path(root, fixture_subpath):
    if pathlib.Path(fixture_subpath).is_absolute():
        raise ValueError(f"Absolute case paths not allowed: {fixture_subpath}")
    resolved = (pathlib.Path(root) / fixture_subpath).resolve()
    resolved_root = pathlib.Path(root).resolve()
    if not str(resolved).startswith(str(resolved_root)):
        raise ValueError(f"Path outside fixture root: {fixture_subpath}")
    reject_protected_path(str(resolved))
    return str(resolved)

def load_case_sets(root, positive, negative):
    cases = []
    if not positive and not negative:
        positive = True
        negative = True
    
    if positive:
        manifest_path = pathlib.Path(root) / "positive" / "case-manifest.json"
        try:
            m = load_manifest(manifest_path)
            for c in m.get("cases", []):
                c["fixture_set"] = "positive"
                cases.append(c)
        except Exception as e:
            raise ValueError(f"Malformed manifest {manifest_path}: {e}")
            
    if negative:
        manifest_path = pathlib.Path(root) / "negative" / "case-manifest.json"
        try:
            m = load_manifest(manifest_path)
            for c in m.get("cases", []):
                c["fixture_set"] = "negative"
                cases.append(c)
        except Exception as e:
            raise ValueError(f"Malformed manifest {manifest_path}: {e}")
            
    return cases

def run_cli_case(root_dir, case):
    try:
        set_dir = pathlib.Path(root_dir) / case["fixture_set"]
        
        input_path = resolve_fixture_path(str(set_dir), case["input"])
        prec_path = resolve_fixture_path(str(set_dir), case["preconditions"])
        
        m56_raw = case["m56_completion_review"]
        if "missing" in m56_raw and case["fixture_set"] == "negative":
            # Allow pointing to a non-existent file for this specific missing test
            m56_path = str((set_dir / m56_raw).resolve())
            if not str(m56_path).startswith(str(set_dir.resolve())):
                return {"timed_out": False, "case_result": CASE_BLOCKED, "message": "path outside root"}
            reject_protected_path(m56_path)
        else:
            m56_path = resolve_fixture_path(str(set_dir), m56_raw)

        cmd = [
            sys.executable,
            "scripts/check-execution-authorization.py",
            "--input", input_path,
            "--preconditions", prec_path,
            "--m56-completion-review", m56_path,
            "--json"
        ]
        
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS,
            shell=False
        )
        
        try:
            payload = json.loads(proc.stdout)
            res = payload.get("execution_authorization_result", {})
            actual_res = res.get("result")
            actual_code = res.get("exit_code", proc.returncode)
            return {
                "timed_out": False,
                "actual_result": actual_res,
                "actual_exit_code": actual_code,
                "message": proc.stderr
            }
        except json.JSONDecodeError:
            return {
                "timed_out": False,
                "actual_result": "JSON_ERROR",
                "actual_exit_code": proc.returncode,
                "message": "Invalid JSON output"
            }
            
    except subprocess.TimeoutExpired:
        return {"timed_out": True, "case_result": CASE_BLOCKED, "message": "Timeout"}
    except Exception as e:
        return {"timed_out": False, "case_result": CASE_BLOCKED, "message": str(e)}

def classify_case_result(case, run_res):
    if run_res.get("case_result") == CASE_BLOCKED:
        return CASE_BLOCKED
        
    if run_res["actual_result"] == case["expected_result"] and run_res["actual_exit_code"] == case["expected_exit_code"]:
        return CASE_PASS
    return CASE_FAIL

def aggregate_results(cases):
    if not cases:
        return M57_FIXTURE_RUNNER_PASS, EXIT_RUNNER_PASS
        
    has_blocked = any(c["case_result"] == CASE_BLOCKED for c in cases)
    has_fail = any(c["case_result"] == CASE_FAIL for c in cases)
    
    if has_blocked:
        return M57_FIXTURE_RUNNER_BLOCKED, EXIT_RUNNER_BLOCKED
    if has_fail:
        return M57_FIXTURE_RUNNER_FAIL, EXIT_RUNNER_FAIL
        
    return M57_FIXTURE_RUNNER_PASS, EXIT_RUNNER_PASS

def build_runner_payload(runner_res, exit_code, strict, fixtures_root, selected, cases):
    pos_count = sum(1 for c in cases if c["fixture_set"] == "positive")
    neg_count = sum(1 for c in cases if c["fixture_set"] == "negative")
    pass_count = sum(1 for c in cases if c["case_result"] == CASE_PASS)
    fail_count = sum(1 for c in cases if c["case_result"] == CASE_FAIL)
    block_count = sum(1 for c in cases if c["case_result"] == CASE_BLOCKED)
    timeout_count = sum(1 for c in cases if c.get("timed_out"))
    
    return {
        "execution_authorization_fixture_runner_result": {
            "schema_version": "1.0.0",
            "runner": "scripts/check-m57-execution-authorization-fixtures.py",
            "result": runner_res,
            "exit_code": exit_code,
            "strict": strict,
            "fixtures_root": fixtures_root,
            "selected_sets": selected,
            "total_cases": len(cases),
            "passed_cases": pass_count,
            "failed_cases": fail_count,
            "blocked_cases": block_count,
            "timed_out_cases": timeout_count,
            "positive_cases": pos_count,
            "negative_cases": neg_count,
            "cases": cases,
            "warnings": [],
            "blockers": [],
            "non_authority_markers": [
                "M57 fixture runner result is not execution authorization.",
                "M57 fixture runner result does not authorize execution.",
                "M57 fixture runner result does not start execution.",
                "M57 fixture runner result does not create approval records.",
                "M57 fixture runner result does not authorize lifecycle mutation.",
                "M57 fixture runner result does not authorize M58.",
                "M57 fixture runner result does not start M58.",
                "M57 fixture runner result does not modify tasks/active-task.md."
            ]
        }
    }

def emit_json(payload):
    print(json.dumps(payload, indent=2))

def emit_human(payload):
    res = payload["execution_authorization_fixture_runner_result"]
    print("=== M57 Fixture Runner Result ===")
    print(f"RUNNER_RESULT: {res['result']}")
    print(f"EXIT_CODE: {res['exit_code']}")
    print(f"TOTAL_CASES: {res['total_cases']}")
    print(f"PASSED_CASES: {res['passed_cases']}")
    print("NON_AUTHORITY:")
    for marker in res["non_authority_markers"]:
        print(f"  - {marker}")
    print("M57 fixture runner does not start M58.")

def emit_explain():
    print("M57 fixture runner is a test harness only.")
    print("M57 fixture runner result is not execution authorization.")
    print("M57 fixture runner does not start M58.")
    print("M57 fixture runner does not create approval records.")
    print("M57 fixture runner does not mutate lifecycle state.")
    print("M57 fixture runner does not modify tasks/active-task.md.")
    print("Exit code 0 is not execution.")
    print("Exit code 0 does not start M58.")

def main():
    args = parse_args()
    if args.explain:
        emit_explain()
        sys.exit(0)
        
    try:
        if not pathlib.Path("scripts/check-execution-authorization.py").is_file():
            raise FileNotFoundError("missing CLI")
            
        cases = load_case_sets(args.fixtures_root, args.positive, args.negative)
        selected = []
        if args.positive or (not args.positive and not args.negative): selected.append("positive")
        if args.negative or (not args.positive and not args.negative): selected.append("negative")
        
        executed_cases = []
        for c in cases:
            run_res = run_cli_case(args.fixtures_root, c)
            c["timed_out"] = run_res.get("timed_out", False)
            c["actual_result"] = run_res.get("actual_result", "")
            c["actual_exit_code"] = run_res.get("actual_exit_code", -1)
            c["message"] = run_res.get("message", "")
            c["case_result"] = classify_case_result(c, run_res)
            
            executed_cases.append(c)
            if args.strict and c["case_result"] in (CASE_FAIL, CASE_BLOCKED):
                break
                
        res, code = aggregate_results(executed_cases)
        payload = build_runner_payload(res, code, args.strict, args.fixtures_root, selected, executed_cases)
        
        if args.json:
            emit_json(payload)
        else:
            emit_human(payload)
        sys.exit(code)
        
    except Exception as e:
        payload = build_runner_payload(M57_FIXTURE_RUNNER_BLOCKED, EXIT_RUNNER_BLOCKED, args.strict, args.fixtures_root, [], [])
        payload["execution_authorization_fixture_runner_result"]["blockers"].append(str(e))
        if args.json:
            emit_json(payload)
        else:
            emit_human(payload)
        sys.exit(EXIT_RUNNER_BLOCKED)

if __name__ == "__main__":
    main()
