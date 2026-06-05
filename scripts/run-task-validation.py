#!/usr/bin/env python3
"""
M66 Unified Runner Script
Executes child checkers as read-only subprocesses, aggregates their results, and produces a validation signal.

No execution means no validation proof.
No validation proof means no PASS.
M66 runner is not approval.
Human review remains required.
"""

import argparse
import json
import sys
import subprocess
import time
from pathlib import Path
from typing import Dict, Any, List

# Contract Definitions
CONTRACT_VERSION = "1.0.0"
PACKAGE_TYPE = "unified_runner_input"
EXPECTED_CHECKERS_COUNT = 3

FORBIDDEN_FIELDS = {
    "approved", "task_approved", "task_complete", "task_completed",
    "completion_approved", "completion_authorized", "completion_gate_passed",
    "human_review_not_required", "skip_human_review", "merge_authorized",
    "push_authorized", "release_authorized", "production_ready",
    "ready_for_production", "m67_started_automatically", "false_pass_resistance_activated"
}

ALLOWED_CHECKER_MAPPING = {
    "task_validation_contract_checker": {
        "script_path": "scripts/check-task-validation-contract.py",
        "input_arg": "--package",
        "input_path_field": "task_validation_package_path"
    },
    "agent_task_evidence_checker": {
        "script_path": "scripts/check-agent-task-evidence.py",
        "input_arg": "--evidence",
        "input_path_field": "agent_evidence_path"
    },
    "acceptance_criteria_checker": {
        "script_path": "scripts/check-acceptance-criteria.py",
        "input_arg": "--package",
        "input_path_field": "acceptance_criteria_package_path"
    }
}

ALLOWED_RESULT_SETS = {
    "task_validation_contract_checker": {"PASS", "PASS_WITH_WARNINGS", "BLOCKED"},
    "agent_task_evidence_checker": {"M64_EVIDENCE_CHECK_PASS", "M64_EVIDENCE_CHECK_PASS_WITH_WARNINGS", "M64_EVIDENCE_CHECK_BLOCKED", "M64_EVIDENCE_CHECK_NOT_ENOUGH_EVIDENCE"},
    "acceptance_criteria_checker": {"M65_ACCEPTANCE_CHECK_PASS", "M65_ACCEPTANCE_CHECK_PASS_WITH_WARNINGS", "M65_ACCEPTANCE_CHECK_BLOCKED", "M65_ACCEPTANCE_CHECK_NOT_ENOUGH_EVIDENCE"}
}

def is_forbidden_mock_path(path: str, is_test_mode: bool) -> bool:
    mock_prefix = "tests/fixtures/m66-unified-runner/mock-execution/mock-checkers/"
    if path.startswith(mock_prefix):
        return not is_test_mode
    return False

def get_family(result: str) -> str:
    if result.endswith("PASS") or result == "PASS":
        return "PASS"
    if result.endswith("PASS_WITH_WARNINGS") or result == "PASS_WITH_WARNINGS":
        return "PASS_WITH_WARNINGS"
    if result.endswith("NOT_ENOUGH_EVIDENCE") or result == "NOT_ENOUGH_EVIDENCE":
        return "NOT_ENOUGH_EVIDENCE"
    if result.endswith("BLOCKED") or result == "BLOCKED":
        return "BLOCKED"
    return "UNKNOWN"

def check_consistency(result_family: str, exit_code: int) -> bool:
    if exit_code == 0 and result_family in {"PASS", "PASS_WITH_WARNINGS"}:
        return True
    if exit_code == 1 and result_family in {"BLOCKED", "NOT_ENOUGH_EVIDENCE"}:
        return True
    return False

def fail(message: str, code: int = 1) -> None:
    print(f"Error: {message}", file=sys.stderr)
    sys.exit(code)

def run_checker(checker_info: Dict[str, Any], resolved_path: str, strict: bool, timeout: int) -> Dict[str, Any]:
    cmd = ["python3", checker_info["script_path"], checker_info["input_arg"], resolved_path, "--json"]
    if strict:
        cmd.append("--strict")

    start_time = time.time()
    try:
        proc = subprocess.run(
            cmd,
            shell=False,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        duration_ms = int((time.time() - start_time) * 1000)
        exit_code = proc.returncode
        stdout = proc.stdout
        stderr = proc.stderr
    except FileNotFoundError:
        return {
            "checker_id": checker_info["checker_id"],
            "executed": False,
            "error": "FileNotFoundError",
            "blockers": ["FileNotFoundError"]
        }
    except subprocess.TimeoutExpired:
        return {
            "checker_id": checker_info["checker_id"],
            "executed": False,
            "error": "TimeoutExpired",
            "blockers": ["TimeoutExpired"]
        }

    res_record = {
        "checker_id": checker_info["checker_id"],
        "script_path": checker_info["script_path"],
        "input_arg": checker_info["input_arg"],
        "input_path_field": checker_info["input_path_field"],
        "resolved_input_path": resolved_path,
        "executed": True,
        "exit_code": exit_code,
        "stdout": stdout,
        "stderr": stderr,
        "duration_ms": duration_ms,
        "blockers": []
    }

    if exit_code == 2:
        res_record["blockers"].append("checker exits 2")
        return res_record

    try:
        parsed_json = json.loads(stdout)
        res_record["stdout_json_valid"] = True
        res_record["parsed_json"] = parsed_json
    except json.JSONDecodeError:
        res_record["stdout_json_valid"] = False
        res_record["blockers"].append("stdout invalid JSON")
        return res_record

    result_val = parsed_json.get("result")
    if not isinstance(result_val, str):
        res_record["blockers"].append("result missing or non-string")
        return res_record

    res_record["result"] = result_val

    allowed_set = ALLOWED_RESULT_SETS.get(checker_info["checker_id"], set())
    if result_val not in allowed_set:
        res_record["blockers"].append(f"unknown result value for checker: {result_val}")
        return res_record

    family = get_family(result_val)
    consistent = check_consistency(family, exit_code)
    res_record["exit_code_consistent_with_result"] = consistent

    if not consistent:
        res_record["blockers"].append("exit-code/result mismatch")

    return res_record

def main():
    parser = argparse.ArgumentParser(description="M66 Unified Runner")
    parser.add_argument("--input", required=True, help="Path to unified-runner-input JSON")
    parser.add_argument("--json", action="store_true", help="Machine-readable JSON output")
    parser.add_argument("--strict", action="store_true", help="Enable strict mode (forwarded)")
    parser.add_argument("--no-execute", action="store_true", help="Force no_execute mode")
    parser.add_argument("--fixture-mode", help="Test mode (e.g., mock-execution)")
    
    args = parser.parse_args()

    if not args.json:
        fail("Missing --json flag is CLI misuse", 2)

    is_test_mode = args.fixture_mode == "mock-execution"

    try:
        input_data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    except Exception as e:
        print(json.dumps({"result": "M66_UNIFIED_RUN_BLOCKED", "blockers": [f"Input load failed: {e}"]}))
        sys.exit(1)

    blockers = []
    warnings = []

    # 5. Required top-level fields
    required_keys = [
        "contract_version", "package_type", "task_id", "task_brief_path",
        "task_validation_package_path", "agent_evidence_path", "acceptance_criteria_package_path",
        "expected_checkers", "runner_options", "human_review_required", "non_authority_boundary"
    ]
    
    for k in required_keys:
        if k not in input_data:
            blockers.append(f"Missing required field: {k}")
    
    if blockers:
        print(json.dumps({"result": "M66_UNIFIED_RUN_BLOCKED", "blockers": blockers}))
        sys.exit(1)

    # 6. Contract constants
    if input_data["contract_version"] != CONTRACT_VERSION:
        blockers.append("Invalid contract_version")
    if input_data["package_type"] != PACKAGE_TYPE:
        blockers.append("Invalid package_type")
    if input_data["human_review_required"] is not True:
        blockers.append("human_review_required must be true")
    if not isinstance(input_data["non_authority_boundary"], list) or len(input_data["non_authority_boundary"]) == 0:
        blockers.append("non_authority_boundary must be non-empty array")

    # 7. Forbidden fields
    for k in input_data.keys():
        if k in FORBIDDEN_FIELDS:
            blockers.append(f"Forbidden operational field present: {k}")

    # 8. runner_options
    ro = input_data["runner_options"]
    if not isinstance(ro.get("strict"), bool):
        blockers.append("runner_options.strict must be bool")
    if not isinstance(ro.get("json"), bool):
        blockers.append("runner_options.json must be bool")
    
    if ro.get("json") is False and args.json:
        warnings.append("RUNNER_OPTIONS_JSON_FALSE_IGNORED")
        
    timeout = ro.get("timeout_seconds")
    if not isinstance(timeout, int) or not (1 <= timeout <= 300):
        blockers.append("invalid timeout_seconds")
        timeout = 30 # safe fallback for error reporting
        
    exec_mode = ro.get("execution_mode")
    if exec_mode not in ("execute", "no_execute"):
        blockers.append("invalid execution_mode")

    # 9. Effective execution mode
    effective_exec_mode = "no_execute" if args.no_execute else exec_mode

    # 11. Checker validation
    checkers = input_data["expected_checkers"]
    if not isinstance(checkers, list) or len(checkers) < EXPECTED_CHECKERS_COUNT:
        blockers.append("Invalid expected_checkers list")
    
    for c in checkers:
        cid = c.get("checker_id")
        if cid not in ALLOWED_CHECKER_MAPPING:
            blockers.append(f"Unknown checker_id: {cid}")
            continue
            
        expected = ALLOWED_CHECKER_MAPPING[cid]
        if c.get("script_path") != expected["script_path"]:
            if is_forbidden_mock_path(c.get("script_path", ""), is_test_mode):
                blockers.append(f"Mock checker path rejected in production mode: {c.get('script_path')}")
            elif not is_test_mode:
                blockers.append(f"Invalid script_path for {cid}: {c.get('script_path')}")
        if c.get("input_arg") != expected["input_arg"]:
            blockers.append(f"Invalid input_arg for {cid}")
        if c.get("input_path_field") != expected["input_path_field"]:
            blockers.append(f"Invalid input_path_field for {cid}")
            
        # 13. input_path_field resolution
        field_name = c.get("input_path_field")
        resolved = input_data.get(field_name)
        if not isinstance(resolved, str) or not resolved:
            blockers.append(f"Missing or invalid resolved path for {field_name}")

    if blockers:
        print(json.dumps({
            "result": "M66_UNIFIED_RUN_BLOCKED",
            "execution_mode": exec_mode,
            "effective_execution_mode": effective_exec_mode,
            "human_review_required": True,
            "non_authority_boundary": input_data.get("non_authority_boundary", []),
            "blockers": blockers,
            "warnings": warnings,
            "exit_code": 1
        }))
        sys.exit(1)

    # 10. no_execute behavior
    if effective_exec_mode == "no_execute":
        out = {
            "result": "M66_UNIFIED_RUN_NOT_ENOUGH_EVIDENCE",
            "task_id": input_data["task_id"],
            "execution_mode": exec_mode,
            "effective_execution_mode": effective_exec_mode,
            "human_review_required": True,
            "checker_results": [],
            "aggregation": {"reason": "No execution means no validation proof. No validation proof means no PASS."},
            "blockers": [],
            "warnings": warnings,
            "not_enough_evidence": ["no_execute"],
            "non_authority_boundary": input_data["non_authority_boundary"],
            "exit_code": 1
        }
        print(json.dumps(out))
        sys.exit(1)

    # Execution
    checker_results = []
    child_blockers = False
    child_not_enough = False
    child_warnings = False
    
    strict_flag = args.strict or ro.get("strict", False)

    for c in checkers:
        field_name = c["input_path_field"]
        resolved_path = input_data[field_name]
        
        # Quick pre-check for existence
        if not Path(resolved_path).exists():
            blockers.append(f"Resolved path does not exist: {resolved_path}")
            child_blockers = True
            continue

        res = run_checker(c, resolved_path, strict=strict_flag, timeout=timeout)
        checker_results.append(res)
        
        if res.get("blockers"):
            child_blockers = True
        
        res_val = res.get("result", "")
        family = get_family(res_val)
        
        if family == "BLOCKED" or not res.get("executed"):
            child_blockers = True
        elif family == "NOT_ENOUGH_EVIDENCE":
            child_not_enough = True
        elif family == "PASS_WITH_WARNINGS":
            child_warnings = True

    # Aggregation
    if blockers or child_blockers:
        final_result = "M66_UNIFIED_RUN_BLOCKED"
        exit_code = 1
    elif child_not_enough:
        final_result = "M66_UNIFIED_RUN_NOT_ENOUGH_EVIDENCE"
        exit_code = 1
    elif child_warnings:
        final_result = "M66_UNIFIED_RUN_PASS_WITH_WARNINGS"
        exit_code = 0
    else:
        final_result = "M66_UNIFIED_RUN_PASS"
        exit_code = 0

    out = {
        "result": final_result,
        "task_id": input_data["task_id"],
        "execution_mode": exec_mode,
        "effective_execution_mode": effective_exec_mode,
        "human_review_required": True,
        "checker_results": checker_results,
        "aggregation": {
            "child_blockers": child_blockers,
            "child_not_enough": child_not_enough,
            "child_warnings": child_warnings
        },
        "findings": [],
        "blockers": blockers,
        "warnings": warnings,
        "non_authority_boundary": input_data["non_authority_boundary"],
        "exit_code": exit_code
    }
    
    print(json.dumps(out))
    sys.exit(exit_code)

if __name__ == "__main__":
    main()
