#!/usr/bin/env python3
"""
M58 Controlled Execution Session Fixture Runner.
Validates the M58 controlled execution session CLI against fixtures.

M58 fixture runner does not open an execution session.
M58 fixture runner does not authorize task completion.
M58 fixture runner does not verify execution result.
M58 fixture runner does not create approval.
M58 fixture runner does not authorize merge, push, or release.
M58 fixture runner does not mutate lifecycle state.
M58 fixture runner only validates controlled execution session fixtures against the 58.7 CLI.
"""

import argparse
import json
import pathlib
import subprocess
import sys

NON_AUTHORITY = [
    "M58 fixture runner does not open an execution session.",
    "M58 fixture runner does not authorize task completion.",
    "M58 fixture runner does not verify execution result.",
    "M58 fixture runner does not create approval.",
    "M58 fixture runner does not authorize merge, push, or release.",
    "M58 fixture runner does not mutate lifecycle state."
]

EXPECTED_POSITIVE = ["positive-clean-ready", "positive-ready-with-warnings", "positive-closed-pending-m59"]
EXPECTED_NEGATIVE = [
    "negative-request-draft-not-ready",
    "negative-request-blocked",
    "negative-preconditions-blocked",
    "negative-boundary-not-satisfied",
    "negative-boundary-blocked",
    "negative-record-blocked",
    "negative-record-aborted",
    "negative-performed-action-violation",
    "negative-m59-handoff-disabled",
    "negative-result-verification-claim",
    "negative-task-complete-claim",
    "negative-push-allowed-claim",
    "negative-id-mismatch",
    "negative-unknown-status"
]

def emit_runner_result(result, exit_code, summary, cases, explain_mode, json_mode):
    if json_mode:
        output = {
            "result": result,
            "exit_code": exit_code,
            "summary": summary,
            "cases": cases,
            "non_authority": NON_AUTHORITY
        }
        print(json.dumps(output, indent=2))
    else:
        print(f"RESULT: {result}")
        print(f"TOTAL_CASES: {summary['total_cases']}")
        print(f"PASSED_CASES: {summary['passed_cases']}")
        print(f"FAILED_CASES: {summary['failed_cases']}")
        print(f"BLOCKED_CASES: {summary['blocked_cases']}")
        print(f"STRICT_CASES_RUN: {summary['strict_cases_run']}")
        
        print("\n--- Non-Authority Statements ---")
        for statement in NON_AUTHORITY:
            print(statement)
        print("M58 fixture runner only validates controlled execution session fixtures against the 58.7 CLI.")
        
        if explain_mode:
            print("\n--- Explanation ---")
            print(f"Fixture runner finished with status: {result}")
            print(f"Discovered positive cases: {summary['positive_cases']}")
            print(f"Discovered negative cases: {summary['negative_cases']}")
            print(f"Discovered total cases: {summary['total_cases']}")
            print("- Each case was evaluated against its expected.json file acting as the oracle.")
            
            print("\nFixture cases details:")
            for c in cases:
                print(f"- [{c['group']}] {c['name']}: {c['result']} (Expected Exit: {c['expected_exit_code']}, Actual: {c['actual_exit_code']})")
                
            print("\nRoot/path containment checks passed successfully.")
            print("Why runner result is not execution approval:")
            print("- The runner is a test harness only. It does not authorize execution.")
            print("Why runner result is not task completion:")
            print("- The runner only validates fixtures. It does not complete task work.")
            print("Why runner result is not result verification:")
            print("- Verification of execution results is the responsibility of M59.")

    sys.exit(exit_code)

def main():
    parser = argparse.ArgumentParser(
        description="M58 Controlled Execution Session Fixture Runner. "
                    "M58 fixture runner only validates controlled execution session fixtures against the 58.7 CLI."
    )
    parser.add_argument("--json", action="store_true", help="Emit output in JSON format")
    parser.add_argument("--explain", action="store_true", help="Explain test runner execution and mapping")
    parser.add_argument("--positive-only", action="store_true", help="Only execute positive fixtures")
    parser.add_argument("--negative-only", action="store_true", help="Only execute negative fixtures")
    parser.add_argument("--root", help="Repository root path")
    
    args = parser.parse_args()
    
    # Check mutually exclusive modes
    if args.positive_only and args.negative_only:
        # positive-only and negative-only together must fail closed as BLOCKED
        emit_runner_result(
            "M58_FIXTURE_RUNNER_BLOCKED", 2,
            {"positive_cases": 0, "negative_cases": 0, "total_cases": 0, "passed_cases": 0, "failed_cases": 0, "blocked_cases": 1, "strict_cases_run": 0},
            [{"name": "args_check", "group": "validation", "result": "BLOCKED", "error": "Mutually exclusive arguments --positive-only and --negative-only provided together."}],
            args.explain, args.json
        )
        
    # 1. Path Safety & Containment
    try:
        resolved_root = pathlib.Path(args.root or ".").resolve(strict=True)
    except Exception:
        # Root doesn't exist or resolves invalid
        emit_runner_result(
            "M58_FIXTURE_RUNNER_BLOCKED", 2,
            {"positive_cases": 0, "negative_cases": 0, "total_cases": 0, "passed_cases": 0, "failed_cases": 0, "blocked_cases": 1, "strict_cases_run": 0},
            [{"name": "root_path", "group": "validation", "result": "BLOCKED", "error": "Repository root path does not exist or is invalid."}],
            args.explain, args.json
        )
        
    cli_path = resolved_root / "scripts" / "check-controlled-execution-session.py"
    pos_dir = resolved_root / "tests" / "fixtures" / "controlled-execution-session" / "positive"
    neg_dir = resolved_root / "tests" / "fixtures" / "controlled-execution-session" / "negative"
    
    # Verify CLI and directories are resolved and contained under root
    for path_to_check, desc in [(cli_path, "CLI path"), (pos_dir, "positive fixtures path"), (neg_dir, "negative fixtures path")]:
        try:
            resolved_path = path_to_check.resolve()
        except Exception as e:
            emit_runner_result(
                "M58_FIXTURE_RUNNER_BLOCKED", 2,
                {"positive_cases": 0, "negative_cases": 0, "total_cases": 0, "passed_cases": 0, "failed_cases": 0, "blocked_cases": 1, "strict_cases_run": 0},
                [{"name": desc, "group": "validation", "result": "BLOCKED", "error": f"Failed resolving path for {desc}: {str(e)}"}],
                args.explain, args.json
            )
            
        # Containment check: resolved_path == resolved_root or resolved_root in resolved_path.parents
        is_contained = (resolved_path == resolved_root) or (resolved_root in resolved_path.parents)
        if not is_contained:
            emit_runner_result(
                "M58_FIXTURE_RUNNER_BLOCKED", 2,
                {"positive_cases": 0, "negative_cases": 0, "total_cases": 0, "passed_cases": 0, "failed_cases": 0, "blocked_cases": 1, "strict_cases_run": 0},
                [{"name": desc, "group": "validation", "result": "BLOCKED", "error": f"{desc} resolves outside repo root."}],
                args.explain, args.json
            )
            
    if not cli_path.exists():
        emit_runner_result(
            "M58_FIXTURE_RUNNER_BLOCKED", 2,
            {"positive_cases": 0, "negative_cases": 0, "total_cases": 0, "passed_cases": 0, "failed_cases": 0, "blocked_cases": 1, "strict_cases_run": 0},
            [{"name": "cli_existence", "group": "validation", "result": "BLOCKED", "error": "check-controlled-execution-session.py CLI script not found."}],
            args.explain, args.json
        )

    # 2. Discover fixture cases and enforce exact counts
    discovered_pos = []
    discovered_neg = []
    
    if pos_dir.exists():
        for item in pos_dir.iterdir():
            if item.is_dir() and not item.name.startswith("."):
                discovered_pos.append(item.name)
                
    if neg_dir.exists():
        for item in neg_dir.iterdir():
            if item.is_dir() and not item.name.startswith("."):
                discovered_neg.append(item.name)
                
    discovered_pos.sort()
    discovered_neg.sort()
    
    # Enforce expected counts
    # Missing expected fixture cases must produce runner failure or blocked status.
    # Extra cases are not allowed and must produce runner failure.
    if set(discovered_pos) != set(EXPECTED_POSITIVE) or set(discovered_neg) != set(EXPECTED_NEGATIVE):
        emit_runner_result(
            "M58_FIXTURE_RUNNER_BLOCKED", 2,
            {"positive_cases": len(discovered_pos), "negative_cases": len(discovered_neg), "total_cases": len(discovered_pos) + len(discovered_neg), "passed_cases": 0, "failed_cases": 0, "blocked_cases": 1, "strict_cases_run": 0},
            [{"name": "fixture_discovery", "group": "validation", "result": "BLOCKED", "error": f"Fixture discovery counts mismatch. Discovered positive: {discovered_pos}, Discovered negative: {discovered_neg}."}],
            args.explain, args.json
        )

    # Filter according to arguments
    target_pos = discovered_pos if not args.negative_only else []
    target_neg = discovered_neg if not args.positive_only else []
    
    cases_run = []
    passed_count = 0
    failed_count = 0
    blocked_count = 0
    strict_run_count = 0
    
    # Helper to validate a case directory
    def run_case(case_name, group, base_dir):
        nonlocal passed_count, failed_count, blocked_count, strict_run_count
        case_path = base_dir / case_name
        
        # Verify case dir resolves under root
        try:
            resolved_case_path = case_path.resolve()
        except Exception:
            blocked_count += 1
            cases_run.append({"name": case_name, "group": group, "result": "BLOCKED", "error": "Failed resolving case directory."})
            return
            
        if not (resolved_case_path == resolved_root or resolved_root in resolved_case_path.parents):
            blocked_count += 1
            cases_run.append({"name": case_name, "group": group, "result": "BLOCKED", "error": "Case directory resolves outside repo root."})
            return
            
        req_file = case_path / "request.json"
        prec_file = case_path / "preconditions.json"
        bound_file = case_path / "boundary.json"
        rec_file = case_path / "record.json"
        exp_file = case_path / "expected.json"
        
        # Validate existence of files
        for f in [req_file, prec_file, bound_file, rec_file, exp_file]:
            if not f.exists():
                blocked_count += 1
                cases_run.append({"name": case_name, "group": group, "result": "BLOCKED", "error": f"Missing required fixture file: {f.name}"})
                return
                
        # Parse expected.json oracle
        try:
            expected_data = json.loads(exp_file.read_text(encoding="utf-8"))
        except Exception as e:
            blocked_count += 1
            cases_run.append({"name": case_name, "group": group, "result": "BLOCKED", "error": f"Failed parsing expected.json: {str(e)}"})
            return
            
        # Check oracle required fields
        required_oracle = ["expected_result", "expected_policy_decision", "expected_exit_code", "non_authority_required"]
        if group == "negative":
            required_oracle.append("negative_reason")
        for key in required_oracle:
            if key not in expected_data:
                blocked_count += 1
                cases_run.append({"name": case_name, "group": group, "result": "BLOCKED", "error": f"expected.json missing required oracle field: {key}"})
                return

        # Invoke CLI script as subprocess
        cmd = [
            sys.executable,
            str(cli_path),
            "--request", str(req_file),
            "--preconditions", str(prec_file),
            "--boundary", str(bound_file),
            "--record", str(rec_file),
            "--json"
        ]
        
        try:
            proc = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=30,
                check=False
            )
        except subprocess.TimeoutExpired:
            failed_count += 1
            cases_run.append({"name": case_name, "group": group, "result": "FAIL", "error": "CLI execution timed out (30 seconds limit)."})
            return
        except Exception as e:
            blocked_count += 1
            cases_run.append({"name": case_name, "group": group, "result": "BLOCKED", "error": f"CLI execution failed to start: {str(e)}"})
            return

        # Parse output JSON
        try:
            actual_data = json.loads(proc.stdout)
        except Exception as e:
            failed_count += 1
            cases_run.append({
                "name": case_name,
                "group": group,
                "result": "FAIL",
                "expected_result": expected_data["expected_result"],
                "actual_result": "MALFORMED_JSON_OUTPUT",
                "expected_exit_code": expected_data["expected_exit_code"],
                "actual_exit_code": proc.returncode,
                "error": f"Failed parsing CLI stdout JSON: {str(e)}"
            })
            return

        # Compare outputs
        mismatch = False
        mismatch_desc = []
        if actual_data.get("result") != expected_data["expected_result"]:
            mismatch = True
            mismatch_desc.append(f"Result mismatch: expected '{expected_data['expected_result']}', got '{actual_data.get('result')}'")
        if actual_data.get("policy_decision") != expected_data["expected_policy_decision"]:
            mismatch = True
            mismatch_desc.append(f"Policy decision mismatch: expected '{expected_data['expected_policy_decision']}', got '{actual_data.get('policy_decision')}'")
        if actual_data.get("exit_code") != expected_data["expected_exit_code"]:
            mismatch = True
            mismatch_desc.append(f"Exit code in JSON mismatch: expected {expected_data['expected_exit_code']}, got {actual_data.get('exit_code')}")
        if proc.returncode != expected_data["expected_exit_code"]:
            mismatch = True
            mismatch_desc.append(f"CLI exit status mismatch: expected {expected_data['expected_exit_code']}, got {proc.returncode}")

        # Check non_authority if required
        if expected_data.get("non_authority_required") is True:
            non_authority_list = actual_data.get("non_authority", [])
            for statement in ["M58 CLI does not open an execution session.", "M58 CLI does not authorize task completion.", "M58 CLI does not verify execution result."]:
                if statement not in non_authority_list:
                    mismatch = True
                    mismatch_desc.append(f"Non-authority list missing statement: '{statement}'")

        if mismatch:
            failed_count += 1
            cases_run.append({
                "name": case_name,
                "group": group,
                "result": "FAIL",
                "expected_result": expected_data["expected_result"],
                "actual_result": actual_data.get("result"),
                "expected_exit_code": expected_data["expected_exit_code"],
                "actual_exit_code": proc.returncode,
                "error": "; ".join(mismatch_desc)
            })
            return

        # Perform strict-mode run if strict fields are non-null
        strict_result = expected_data.get("strict_expected_result")
        if strict_result is not None:
            strict_run_count += 1
            strict_decision = expected_data.get("strict_expected_policy_decision")
            strict_exit = expected_data.get("strict_expected_exit_code")
            
            strict_cmd = cmd + ["--strict"]
            try:
                strict_proc = subprocess.run(
                    strict_cmd,
                    capture_output=True,
                    text=True,
                    timeout=30,
                    check=False
                )
            except subprocess.TimeoutExpired:
                failed_count += 1
                cases_run.append({"name": case_name, "group": group, "result": "FAIL", "error": "CLI strict-mode execution timed out (30 seconds limit)."})
                return
            except Exception as e:
                blocked_count += 1
                cases_run.append({"name": case_name, "group": group, "result": "BLOCKED", "error": f"CLI strict-mode execution failed to start: {str(e)}"})
                return
                
            try:
                strict_actual = json.loads(strict_proc.stdout)
            except Exception as e:
                failed_count += 1
                cases_run.append({
                    "name": case_name,
                    "group": group,
                    "result": "FAIL",
                    "expected_result": strict_result,
                    "actual_result": "MALFORMED_JSON_OUTPUT",
                    "expected_exit_code": strict_exit,
                    "actual_exit_code": strict_proc.returncode,
                    "error": f"Failed parsing CLI strict-mode stdout JSON: {str(e)}"
                })
                return
                
            strict_mismatch = False
            strict_desc = []
            if strict_actual.get("result") != strict_result:
                strict_mismatch = True
                strict_desc.append(f"Strict result mismatch: expected '{strict_result}', got '{strict_actual.get('result')}'")
            if strict_actual.get("policy_decision") != strict_decision:
                strict_mismatch = True
                strict_desc.append(f"Strict policy decision mismatch: expected '{strict_decision}', got '{strict_actual.get('policy_decision')}'")
            if strict_actual.get("exit_code") != strict_exit:
                strict_mismatch = True
                strict_desc.append(f"Strict exit code in JSON mismatch: expected {strict_exit}, got {strict_actual.get('exit_code')}")
            if strict_proc.returncode != strict_exit:
                strict_mismatch = True
                strict_desc.append(f"Strict CLI exit status mismatch: expected {strict_exit}, got {strict_proc.returncode}")
                
            if strict_mismatch:
                failed_count += 1
                cases_run.append({
                    "name": case_name,
                    "group": group,
                    "result": "FAIL",
                    "expected_result": strict_result,
                    "actual_result": strict_actual.get("result"),
                    "expected_exit_code": strict_exit,
                    "actual_exit_code": strict_proc.returncode,
                    "error": "; ".join(strict_desc)
                })
                return

        passed_count += 1
        cases_run.append({
            "name": case_name,
            "group": group,
            "result": "PASS",
            "expected_result": expected_data["expected_result"],
            "actual_result": actual_data.get("result"),
            "expected_exit_code": expected_data["expected_exit_code"],
            "actual_exit_code": proc.returncode
        })

    # Run positive cases
    for case in target_pos:
        run_case(case, "positive", pos_dir)
        
    # Run negative cases
    for case in target_neg:
        run_case(case, "negative", neg_dir)

    # Determine final runner status and exit code
    total_cases_run = len(target_pos) + len(target_neg)
    summary = {
        "positive_cases": len(target_pos),
        "negative_cases": len(target_neg),
        "total_cases": total_cases_run,
        "passed_cases": passed_count,
        "failed_cases": failed_count,
        "blocked_cases": blocked_count,
        "strict_cases_run": strict_run_count
    }
    
    if blocked_count > 0:
        final_result = "M58_FIXTURE_RUNNER_BLOCKED"
        final_exit = 2
    elif failed_count > 0:
        final_result = "M58_FIXTURE_RUNNER_FAIL"
        final_exit = 1
    else:
        final_result = "M58_FIXTURE_RUNNER_PASS"
        final_exit = 0
        
    emit_runner_result(final_result, final_exit, summary, cases_run, args.explain, args.json)

if __name__ == "__main__":
    main()
