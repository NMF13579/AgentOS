#!/usr/bin/env python3
import sys
import os
import json
import argparse
import subprocess
import shlex
from pathlib import Path

# Enforce category/class pairing rules
PAIRINGS = {
    "exit-code": "ESSENTIAL",
    "child-validator-failures": "ESSENTIAL",
    "false-pass-resistance": "ESSENTIAL",
    "warning-visibility": "ESSENTIAL",
    "wrapper": "CONDITIONAL",
    "supporting-boundary": "SUPPORTING"
}

ALLOWED_RESULTS = {
    "DISPATCHER_PASS",
    "DISPATCHER_PASS_WITH_WARNINGS",
    "DISPATCHER_BLOCKED",
    "DISPATCHER_NOT_RUN",
    "DISPATCHER_UNKNOWN",
    "DISPATCHER_ERROR",
}

ALLOWED_BEHAVIORS = {
    "none",
    "missing_child",
    "malformed_output",
    "exit_result_mismatch",
    "child_failure",
    "stderr_output",
    "timeout",
    "unknown_result",
    "not_run_result",
    "pass_with_warnings",
}

def fail_exit(msg, code=2):
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(code)

def validate_paths(fixture_dir, schema_file, output_file, repo_root):
    # Enforce fixture root path safety
    try:
        f_dir = Path(fixture_dir).resolve()
        expected_root = (repo_root / "fixtures/m74-dispatcher-regression").resolve()
        if not str(f_dir).startswith(str(expected_root)):
            fail_exit("Fixture directory must be within fixtures/m74-dispatcher-regression/", 1)
    except Exception as e:
        fail_exit(f"Invalid fixture directory: {e}", 1)

    # Output file safety check
    if output_file:
        try:
            out_path = Path(output_file).resolve()
            reports_dir = (repo_root / "reports").resolve()
            if not str(out_path).startswith(str(reports_dir)) or not out_path.name.startswith("m74-"):
                fail_exit("Output path must be within reports/m74-*", 1)
        except Exception as e:
            fail_exit(f"Invalid output path: {e}", 1)

def validate_fixture(data, path, repo_root):
    # 1. Required fields presence
    required_fields = [
        "fixture_id", "fixture_name", "category", "category_class",
        "gap_id", "gap_status", "input_mode", "dispatcher_command",
        "mock_child_behavior", "mock_child_path", "expected_dispatcher_result",
        "expected_exit_code", "expected_stdout_contains", "expected_stderr_contains",
        "must_not_contain", "expected_report_fields", "approval_created_expected",
        "lifecycle_mutation_expected", "m74_scope"
    ]
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"

    # 2. Forbid empty fixture_id, fixture_name, category, category_class, gap_status, dispatcher_command, m74_scope
    for field in ["fixture_id", "fixture_name", "category", "category_class", "gap_status", "dispatcher_command", "m74_scope"]:
        if not str(data[field]).strip():
            return False, f"Field cannot be empty: {field}"

    # 3. Category/class pairing validation
    cat = data["category"]
    cat_class = data["category_class"]
    if cat not in PAIRINGS:
        return False, f"Invalid category: {cat}"
    if PAIRINGS[cat] != cat_class:
        return False, f"Invalid category/class pairing: {cat} -> {cat_class} (expected {PAIRINGS[cat]})"

    # 4. Expected exit code and dispatcher result
    if data["expected_exit_code"] not in [0, 1, 2]:
        return False, f"Invalid expected_exit_code: {data['expected_exit_code']}"
    if data["expected_dispatcher_result"] not in ALLOWED_RESULTS:
        return False, f"Invalid expected_dispatcher_result: {data['expected_dispatcher_result']}"

    # 5. Safety expectations
    if data["approval_created_expected"] is not False:
        return False, "approval_created_expected must be false"
    if data["lifecycle_mutation_expected"] is not False:
        return False, "lifecycle_mutation_expected must be false"

    # 6. Mock child behavior and path isolation
    behavior = data["mock_child_behavior"]
    if behavior not in ALLOWED_BEHAVIORS:
        return False, f"Invalid mock_child_behavior: {behavior}"

    m_path = data["mock_child_path"]
    if behavior == "none":
        if m_path not in ["none", ""]:
            return False, f"mock_child_path must be 'none' or empty when behavior is 'none'"
    else:
        # Validate path isolation for mock validator
        if ".." in m_path or m_path.startswith("/") or os.path.isabs(m_path):
            return False, f"mock_child_path uses path traversal or absolute path: {m_path}"
        try:
            child_resolved = (repo_root / m_path).resolve()
            mock_root = (repo_root / "fixtures/m74-dispatcher-regression/mock-child-validators").resolve()
            if not str(child_resolved).startswith(str(mock_root)):
                return False, f"mock_child_path escapes mock validator directory: {m_path}"
            
            # Check script and production validator directory rules
            rel_path = child_resolved.relative_to(repo_root)
            if str(rel_path).startswith("scripts/") or str(rel_path).startswith("validators/"):
                return False, f"mock_child_path points to scripts or production validators: {m_path}"
        except Exception as e:
            return False, f"Invalid mock_child_path resolution: {e}"

    return True, ""

def write_mock_child(repo_root, mock_child_path, behavior):
    path = (repo_root / mock_child_path).resolve()
    path.parent.mkdir(parents=True, exist_ok=True)
    
    content = "#!/usr/bin/env python3\nimport sys\nimport json\n"
    if behavior == "malformed_output":
        content += "print('this is malformed non-json output')\nsys.exit(0)\n"
    elif behavior == "exit_result_mismatch":
        content += "print(json.dumps({'result': 'PASS'}))\nsys.exit(1)\n"
    elif behavior == "child_failure":
        content += "print(json.dumps({'result': 'FAIL'}))\nsys.exit(1)\n"
    elif behavior == "stderr_output":
        content += "print('mock child error to stderr', file=sys.stderr)\nsys.exit(1)\n"
    elif behavior == "timeout":
        content += "import time\ntime.sleep(2)\nsys.exit(0)\n"
    elif behavior == "unknown_result":
        content += "print(json.dumps({'result': 'UNKNOWN_TOKEN'}))\nsys.exit(1)\n"
    elif behavior == "not_run_result":
        content += "print(json.dumps({'result': 'NOT_RUN'}))\nsys.exit(1)\n"
    elif behavior == "pass_with_warnings":
        content += "print(json.dumps({'result': 'WARN', 'warnings': ['mock warning']}))\nsys.exit(0)\n"
    else:
        content += "sys.exit(0)\n"
        
    with open(path, "w") as f:
        f.write(content)
    path.chmod(0o755)

def determine_actual_result(exit_code, stdout, stderr):
    # Try parsing stdout as JSON
    try:
        data = json.loads(stdout.strip())
        if isinstance(data, dict) and "result" in data:
            res = data["result"]
            if res == "PASS":
                return "DISPATCHER_PASS"
            elif res == "WARN":
                return "DISPATCHER_PASS_WITH_WARNINGS"
            elif res == "FAIL":
                return "DISPATCHER_BLOCKED"
            elif res == "NOT_RUN":
                return "DISPATCHER_NOT_RUN"
            elif res == "ERROR":
                return "DISPATCHER_ERROR"
    except Exception:
        pass

    # Check for Overall result prefix
    for line in stdout.splitlines():
        if line.startswith("Overall result:"):
            res = line.split(":", 1)[1].strip()
            if res == "PASS":
                # Check for warnings in exit code 0
                if "warning" in stdout.lower() or "warning" in stderr.lower():
                    return "DISPATCHER_PASS_WITH_WARNINGS"
                return "DISPATCHER_PASS"
            elif res == "WARN":
                return "DISPATCHER_PASS_WITH_WARNINGS"
            elif res == "FAIL":
                return "DISPATCHER_BLOCKED"
            elif res == "NOT_RUN":
                return "DISPATCHER_NOT_RUN"
            elif res == "ERROR":
                return "DISPATCHER_ERROR"

    # Fallback to exit codes and keywords
    if exit_code == 2:
        return "DISPATCHER_ERROR"
    elif exit_code == 0:
        if "warning" in stdout.lower() or "warning" in stderr.lower():
            return "DISPATCHER_PASS_WITH_WARNINGS"
        return "DISPATCHER_PASS"
    elif exit_code == 1:
        if "not_run" in stdout.lower() or "not run" in stdout.lower():
            return "DISPATCHER_NOT_RUN"
        if "unknown" in stdout.lower():
            return "DISPATCHER_UNKNOWN"
        return "DISPATCHER_BLOCKED"
        
    return "DISPATCHER_ERROR"

def main():
    parser = argparse.ArgumentParser(description="M74 Dispatcher Regression Runner and Fixture Validator")
    parser.add_argument("--fixtures", required=True, help="Path to fixtures directory")
    parser.add_argument("--schema", required=True, help="Path to JSON Schema")
    parser.add_argument("--output", help="Path to save execution/validation report")
    parser.add_argument("--json", action="store_true", help="Print summary in JSON format")
    parser.add_argument("--validate-only", action="store_true", help="Run validation checks only")
    parser.add_argument("--execute", action="store_true", help="Run controlled regression tests")
    parser.add_argument("--category", help="Filter by fixture category")
    parser.add_argument("--fail-on-warning", action="store_true", help="Fail on warning status")

    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent

    # Validate output and input directories safety
    validate_paths(args.fixtures, args.schema, args.output, repo_root)

    # Load schema
    try:
        with open(args.schema, 'r') as f:
            schema = json.load(f)
    except Exception as e:
        fail_exit(f"Failed to load schema: {e}", 2)

    # Discover and validate fixture files
    discovered_fixtures = []
    fixtures_dir = Path(args.fixtures)
    for root, _, files in os.walk(fixtures_dir):
        for file in files:
            if file.endswith(".json"):
                discovered_fixtures.append(Path(root) / file)

    valid_count = 0
    invalid_count = 0
    invalid_fixtures = []
    categories_seen = set()
    essential_categories_seen = set()
    conditional_categories_seen = set()
    supporting_categories_seen = set()
    fixtures_data = []

    for f_path in discovered_fixtures:
        try:
            with open(f_path, 'r') as f:
                data = json.load(f)
        except Exception as e:
            invalid_count += 1
            invalid_fixtures.append((f_path, f"JSON load error: {e}"))
            continue

        is_valid, err_msg = validate_fixture(data, f_path, repo_root)
        if not is_valid:
            invalid_count += 1
            invalid_fixtures.append((f_path, err_msg))
            continue

        # Check filter
        if args.category and data["category"] != args.category:
            continue

        valid_count += 1
        fixtures_data.append((f_path, data))
        
        cat = data["category"]
        categories_seen.add(cat)
        cat_class = data["category_class"]
        if cat_class == "ESSENTIAL":
            essential_categories_seen.add(cat)
        elif cat_class == "CONDITIONAL":
            conditional_categories_seen.add(cat)
        elif cat_class == "SUPPORTING":
            supporting_categories_seen.add(cat)

    # Determine validation-mode results
    if invalid_count > 0:
        val_result = "M74_REGRESSION_VALIDATE_BLOCKED"
        exit_code = 1
    else:
        val_result = "M74_REGRESSION_VALIDATE_PASS"
        exit_code = 0

    # Initialize execution metrics
    execute_mode = bool(args.execute)
    run_count = 0
    passed_count = 0
    failed_count = 0
    blocked_count = 0
    approval_created = False
    lifecycle_mutation_occurred = False
    dispatcher_executed = False
    wrapper_executed = False
    runner_result = val_result

    if execute_mode:
        if invalid_count > 0:
            runner_result = "M74_REGRESSION_EXECUTION_BLOCKED"
            exit_code = 1
        else:
            # Run the controlled executions
            for f_path, data in fixtures_data:
                run_count += 1
                mock_child_created = False
                mock_child_path = data["mock_child_path"]
                behavior = data["mock_child_behavior"]
                
                try:
                    if behavior != "none" and mock_child_path != "none" and mock_child_path:
                        write_mock_child(repo_root, mock_child_path, behavior)
                        mock_child_created = True
                        
                    # Track what's being executed
                    input_mode = data["input_mode"]
                    if input_mode == "wrapper_cli":
                        wrapper_executed = True
                    elif input_mode in ["dispatcher_cli", "dispatcher_cli_with_mock_child"]:
                        dispatcher_executed = True
                        
                    # Parse command safely
                    cmd_list = shlex.split(data["dispatcher_command"])
                    
                    # Run subprocess (never shell=True)
                    proc = subprocess.run(
                        cmd_list,
                        cwd=str(repo_root),
                        capture_output=True,
                        text=True,
                        check=False
                    )
                    
                    actual_exit_code = proc.returncode
                    actual_stdout = proc.stdout
                    actual_stderr = proc.stderr
                    
                    actual_result = determine_actual_result(actual_exit_code, actual_stdout, actual_stderr)
                    
                    # Comparisons
                    expected_exit_code = data["expected_exit_code"]
                    expected_result = data["expected_dispatcher_result"]
                    
                    fixture_pass = True
                    
                    if actual_exit_code != expected_exit_code:
                        fixture_pass = False
                    if actual_result != expected_result:
                        fixture_pass = False
                        
                    # Check contains
                    for term in data["expected_stdout_contains"]:
                        if term not in actual_stdout:
                            fixture_pass = False
                    for term in data["expected_stderr_contains"]:
                        if term not in actual_stderr:
                            fixture_pass = False
                    for term in data["must_not_contain"]:
                        if term in actual_stdout or term in actual_stderr:
                            fixture_pass = False
                            
                    # Fail closed checks on actual result
                    if actual_result not in ALLOWED_RESULTS:
                        fixture_pass = False
                    if actual_result == "DISPATCHER_NOT_RUN" and expected_result != "DISPATCHER_NOT_RUN":
                        fixture_pass = False
                    if actual_result == "DISPATCHER_UNKNOWN" and expected_result != "DISPATCHER_UNKNOWN":
                        fixture_pass = False
                        
                    # Verify no approval/lifecycle mutation occurred (safety enforcement)
                    if "approval created" in actual_stdout.lower() or "approval" in actual_stdout.lower() and "created" in actual_stdout.lower():
                        approval_created = True
                    if "lifecycle mutated" in actual_stdout.lower() or "lifecycle_mutation_occurred" in actual_stdout.lower():
                        lifecycle_mutation_occurred = True
                        
                    if fixture_pass:
                        passed_count += 1
                    else:
                        failed_count += 1
                        
                except Exception as e:
                    failed_count += 1
                    blocked_count += 1
                finally:
                    # Clean up mock child validator
                    if mock_child_created:
                        try:
                            p = (repo_root / mock_child_path).resolve()
                            if p.is_file():
                                p.unlink()
                        except Exception:
                            pass
            
            # Determine overall execution result
            if failed_count > 0:
                runner_result = "M74_REGRESSION_EXECUTION_BLOCKED"
                exit_code = 1
            else:
                if args.fail_on_warning and (passed_count == 0 or any("warning" in str(f) for f, _ in fixtures_data)):
                    # Fail on warning logic
                    runner_result = "M74_REGRESSION_EXECUTION_BLOCKED"
                    exit_code = 1
                else:
                    runner_result = "M74_REGRESSION_EXECUTION_PASS"
                    exit_code = 0

    summary = {
        "runner_mode": "execute" if execute_mode else "validate-only",
        "fixtures_discovered_count": len(discovered_fixtures),
        "fixtures_valid_count": valid_count,
        "fixtures_invalid_count": invalid_count,
        "fixtures_run_count": run_count,
        "fixtures_passed_count": passed_count,
        "fixtures_failed_count": failed_count,
        "fixtures_blocked_count": blocked_count,
        "fixtures_not_run_count": len(discovered_fixtures) - run_count,
        "categories_seen": sorted(list(categories_seen)),
        "essential_categories_seen": sorted(list(essential_categories_seen)),
        "conditional_categories_seen": sorted(list(conditional_categories_seen)),
        "supporting_categories_seen": sorted(list(supporting_categories_seen)),
        "approval_created": approval_created,
        "lifecycle_mutation_occurred": lifecycle_mutation_occurred,
        "dispatcher_executed": dispatcher_executed,
        "wrapper_executed": wrapper_executed,
        "runner_result": runner_result
    }

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(f"Runner result: {runner_result}")
        print(f"Discovered {len(discovered_fixtures)} fixtures: {valid_count} valid, {invalid_count} invalid.")
        if execute_mode:
            print(f"Executed {run_count} fixtures: {passed_count} passed, {failed_count} failed.")
        if invalid_count > 0:
            print("Blocker validation errors:", file=sys.stderr)
            for f_path, err in invalid_fixtures:
                print(f"  - {f_path}: {err}", file=sys.stderr)

    if args.output:
        try:
            with open(args.output, 'w') as f:
                json.dump(summary, f, indent=2)
        except Exception as e:
            fail_exit(f"Failed to write output report: {e}", 2)

    sys.exit(exit_code)

if __name__ == "__main__":
    main()
