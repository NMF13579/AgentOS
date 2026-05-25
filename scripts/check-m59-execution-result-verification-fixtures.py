#!/usr/bin/env python3
"""
M59 Execution Result Verification Fixture Runner

This script automates running the Execution Result Verification CLI against
predefined positive and negative fixtures to ensure policy compliance.

M59 fixture runner result is not execution result verification.
M59 fixture runner result is not task approval.
M59 fixture runner result does not authorize merge, push, release, or lifecycle mutation.
M59 fixture runner result does not replace human review.
M59 fixture runner result does not create evidence report or completion review.
"""

import sys
import json
import argparse
import subprocess
from pathlib import Path

# Required non-authority statements
NON_AUTHORITY_STATEMENTS = [
    "M59 fixture runner result is not execution result verification.",
    "M59 fixture runner result is not task approval.",
    "M59 fixture runner result does not authorize merge, push, release, or lifecycle mutation.",
    "M59 fixture runner result does not replace human review.",
    "M59 fixture runner result does not create evidence report or completion review."
]

# Canonical inventories
EXPECTED_POSITIVE = {
    "positive-clean-verified",
    "positive-verified-with-warnings",
    "positive-output-verified-with-warnings",
    "positive-strict-preserves-non-ambiguous-warning"
}

EXPECTED_NEGATIVE = {
    "negative-upstream-blocked-output-verified",
    "negative-upstream-not-verified-output-verified",
    "negative-authority-claim",
    "negative-human-review-required-false",
    "negative-human-review-handoff-false",
    "negative-strict-ambiguous-warning",
    "negative-malformed-json"
}


def main():
    parser = argparse.ArgumentParser(
        description="M59 Execution Result Verification Fixture Runner",
        add_help=True
    )
    parser.add_argument("--root", default=".", help="Repository root directory")
    parser.add_argument("--json", action="store_true", help="Output JSON only to stdout")
    parser.add_argument("--explain", action="store_true", help="Print explain details and exit")
    parser.add_argument("--positive-only", action="store_true", help="Run only positive fixtures")
    parser.add_argument("--negative-only", action="store_true", help="Run only negative fixtures")
    parser.add_argument("--timeout", type=int, default=30, help="CLI run timeout in seconds")

    args = parser.parse_args()

    # Explain Mode
    if args.explain:
        explanation = """M59 Execution Result Verification Fixture Runner - Explain Mode

This runner evaluates the Execution Result Verification CLI against standard test fixtures.

Discovered Fixture Roots:
- Positive fixtures under tests/fixtures/execution-result-verification/positive
- Negative fixtures under tests/fixtures/execution-result-verification/negative

Expected Fixtures to Run:
- Positive cases: 4
- Negative cases: 7
- Total cases: 11
- Strict mode runs: 2

Comparison Rules:
- Reads and validates expected.json configuration for each case.
- Verifies exact matches for result, policy_decision, exit_code, upstream_state, output_state, strict, and strict_upgrades_applied.
- Checks minimum counts of warnings, blockers, not-verified reasons, and authority claims.
- Validates warning/blocker/not_verified/authority claim substring inclusions and exclusions.

Non-Authority Boundary:
- The runner result is not approval.
- M59 fixture runner result is not execution result verification.
- M59 fixture runner result is not task approval.
- M59 fixture runner result does not authorize merge, push, release, or lifecycle mutation.
- M59 fixture runner result does not replace human review.
- M59 fixture runner result does not create evidence report or completion review.
"""
        print(explanation)
        sys.exit(0)

    # Initialize results
    runner_result = "M59_FIXTURE_RUNNER_PASS"
    exit_code = 0
    blocked_diagnostics = []
    failed_diagnostics = []
    cases_run_metadata = []

    positive_fixture_cases_count = 0
    negative_fixture_cases_count = 0
    normal_cli_runs_count = 0
    strict_cli_runs_count = 0
    total_cli_runs_count = 0
    passed_runs_count = 0
    failed_runs_count = 0

    try:
        # Validate timeout
        if args.timeout <= 0:
            blocked_diagnostics.append("runner_internal_error: Timeout must be positive.")
            runner_result = "M59_FIXTURE_RUNNER_BLOCKED"
            exit_code = 2

        # Validate mutual exclusion
        if args.positive_only and args.negative_only:
            blocked_diagnostics.append("runner_internal_error: --positive-only and --negative-only are mutually exclusive.")
            runner_result = "M59_FIXTURE_RUNNER_BLOCKED"
            exit_code = 2

        # Resolve paths
        root_path = Path(args.root).resolve()
        cli_script = root_path / "scripts" / "check-execution-result-verification.py"
        cli_doc = root_path / "docs" / "EXECUTION-RESULT-VERIFICATION-CLI.md"
        pos_root = root_path / "tests" / "fixtures" / "execution-result-verification" / "positive"
        neg_root = root_path / "tests" / "fixtures" / "execution-result-verification" / "negative"

        # Check Preconditions
        if runner_result != "M59_FIXTURE_RUNNER_BLOCKED":
            if not cli_script.is_file():
                blocked_diagnostics.append("missing_cli: check-execution-result-verification.py not found.")
                runner_result = "M59_FIXTURE_RUNNER_BLOCKED"
                exit_code = 2

            if not cli_doc.is_file():
                blocked_diagnostics.append("missing_docs: EXECUTION-RESULT-VERIFICATION-CLI.md not found.")
                runner_result = "M59_FIXTURE_RUNNER_BLOCKED"
                exit_code = 2
            else:
                doc_content = cli_doc.read_text(encoding="utf-8")
                if "FINAL_STATUS: M59_EXECUTION_RESULT_VERIFICATION_CLI_DEFINED" not in doc_content:
                    blocked_diagnostics.append("wrong_cli_status: FINAL_STATUS wrong or missing in CLI docs.")
                    runner_result = "M59_FIXTURE_RUNNER_BLOCKED"
                    exit_code = 2

            if not pos_root.is_dir() or not neg_root.is_dir():
                blocked_diagnostics.append("missing_fixture_root: Positive or negative fixture root directory not found.")
                runner_result = "M59_FIXTURE_RUNNER_BLOCKED"
                exit_code = 2

        # Discovered cases
        pos_cases = []
        neg_cases = []

        if runner_result != "M59_FIXTURE_RUNNER_BLOCKED":
            # Discover Positive cases
            if not args.negative_only:
                for path in sorted(pos_root.iterdir()):
                    if path.is_dir():
                        pos_cases.append(path)
                        if path.name not in EXPECTED_POSITIVE:
                            blocked_diagnostics.append(f"unexpected_fixture_case: Unexpected positive case {path.name}.")
                            runner_result = "M59_FIXTURE_RUNNER_BLOCKED"
                            exit_code = 2

            # Discover Negative cases
            if not args.positive_only:
                for path in sorted(neg_root.iterdir()):
                    if path.is_dir():
                        neg_cases.append(path)
                        if path.name not in EXPECTED_NEGATIVE:
                            blocked_diagnostics.append(f"unexpected_fixture_case: Unexpected negative case {path.name}.")
                            runner_result = "M59_FIXTURE_RUNNER_BLOCKED"
                            exit_code = 2

        # Verify cases count
        if runner_result != "M59_FIXTURE_RUNNER_BLOCKED":
            positive_fixture_cases_count = len(pos_cases)
            negative_fixture_cases_count = len(neg_cases)

        # Run cases
        if runner_result != "M59_FIXTURE_RUNNER_BLOCKED":
            all_cases = []
            for p in pos_cases:
                all_cases.append((p, True))
            for n in neg_cases:
                all_cases.append((n, False))

            for case_path, is_positive in all_cases:
                case_name = case_path.name
                required_files = {
                    "input.json", "preconditions.json", "diff-scope.json",
                    "validation-evidence.json", "result-output.json",
                    "expected.json", "README.md"
                }
                
                # Check file structural contract
                existing_files = set()
                extra_files = False
                for f in case_path.iterdir():
                    if f.is_file():
                        existing_files.add(f.name)
                    else:
                        extra_files = True

                missing_files = required_files - existing_files
                unexpected_files = existing_files - required_files

                if missing_files:
                    blocked_diagnostics.append(f"missing_fixture_file: Case {case_name} missing {sorted(list(missing_files))}.")
                    runner_result = "M59_FIXTURE_RUNNER_BLOCKED"
                    exit_code = 2
                    continue

                if unexpected_files or extra_files:
                    blocked_diagnostics.append(f"unexpected_fixture_file: Case {case_name} has extra files or subdirectories.")
                    runner_result = "M59_FIXTURE_RUNNER_BLOCKED"
                    exit_code = 2
                    continue

                # Load and validate expected.json
                expected_file = case_path / "expected.json"
                try:
                    expected_data = json.loads(expected_file.read_text(encoding="utf-8"))
                except Exception as e:
                    blocked_diagnostics.append(f"invalid_expected_json: Case {case_name} expected.json is malformed: {str(e)}.")
                    runner_result = "M59_FIXTURE_RUNNER_BLOCKED"
                    exit_code = 2
                    continue

                # Check policy version
                if expected_data.get("policy_version") != "M59.1":
                    blocked_diagnostics.append(f"unsupported_policy_version: Case {case_name} uses wrong policy version {expected_data.get('policy_version')}.")
                    runner_result = "M59_FIXTURE_RUNNER_BLOCKED"
                    exit_code = 2
                    continue

                # Check required keys in expected.json
                required_oracle_keys = [
                    "policy_version", "expected_result", "expected_policy_decision",
                    "expected_exit_code", "expected_upstream_state", "expected_output_state",
                    "expected_strict", "expected_strict_upgrades_applied", "expected_min_warnings",
                    "expected_min_blockers", "expected_min_not_verified_reasons",
                    "expected_min_authority_claims_detected", "expected_warning_contains",
                    "forbidden_warning_contains"
                ]
                if not is_positive:
                    required_oracle_keys.extend([
                        "expected_blocker_contains", "expected_not_verified_contains",
                        "expected_authority_claim_contains"
                    ])

                missing_keys = set(required_oracle_keys) - set(expected_data.keys())
                if missing_keys:
                    blocked_diagnostics.append(f"invalid_expected_json: Case {case_name} expected.json missing keys: {sorted(list(missing_keys))}.")
                    runner_result = "M59_FIXTURE_RUNNER_BLOCKED"
                    exit_code = 2
                    continue

                # Validate other JSON file syntax
                malformed_case_name = "negative-malformed-json"
                json_parse_error = False

                for f_name in ["input.json", "preconditions.json", "diff-scope.json", "validation-evidence.json", "result-output.json"]:
                    f_path = case_path / f_name
                    if case_name == malformed_case_name and f_name == "input.json":
                        # Must be malformed
                        try:
                            json.loads(f_path.read_text(encoding="utf-8"))
                            blocked_diagnostics.append(f"malformed_fixture_not_malformed: Case {case_name} input.json is valid JSON but should be malformed.")
                            runner_result = "M59_FIXTURE_RUNNER_BLOCKED"
                            exit_code = 2
                            json_parse_error = True
                        except json.JSONDecodeError:
                            pass
                    else:
                        # Must be valid JSON
                        try:
                            json.loads(f_path.read_text(encoding="utf-8"))
                        except Exception as e:
                            blocked_diagnostics.append(f"fixture_json_invalid: Case {case_name} file {f_name} is malformed: {str(e)}.")
                            runner_result = "M59_FIXTURE_RUNNER_BLOCKED"
                            exit_code = 2
                            json_parse_error = True

                if json_parse_error or runner_result == "M59_FIXTURE_RUNNER_BLOCKED":
                    continue

                # Execute Normal Mode Run
                normal_cli_runs_count += 1
                total_cli_runs_count += 1

                cmd = [
                    sys.executable, str(cli_script),
                    "--input", str(case_path / "input.json"),
                    "--preconditions", str(case_path / "preconditions.json"),
                    "--diff-scope", str(case_path / "diff-scope.json"),
                    "--validation-evidence", str(case_path / "validation-evidence.json"),
                    "--result-output", str(case_path / "result-output.json"),
                    "--json"
                ]

                try:
                    completed = subprocess.run(
                        cmd,
                        capture_output=True,
                        text=True,
                        timeout=args.timeout,
                        check=False
                    )
                except subprocess.TimeoutExpired:
                    blocked_diagnostics.append(f"fixture_timeout: Case {case_name} execution timed out.")
                    runner_result = "M59_FIXTURE_RUNNER_BLOCKED"
                    exit_code = 2
                    continue
                except Exception as e:
                    blocked_diagnostics.append(f"fixture_execution_failed: Case {case_name} execution failed: {str(e)}.")
                    runner_result = "M59_FIXTURE_RUNNER_BLOCKED"
                    exit_code = 2
                    continue

                # Parse output
                try:
                    actual = json.loads(completed.stdout)
                except Exception:
                    blocked_diagnostics.append(f"fixture_output_not_json: Case {case_name} CLI did not emit JSON on stdout.")
                    runner_result = "M59_FIXTURE_RUNNER_BLOCKED"
                    exit_code = 2
                    continue

                # Compare actual vs expected
                mismatch_reasons = []

                if actual.get("result") != expected_data["expected_result"]:
                    mismatch_reasons.append(f"result mismatch: got '{actual.get('result')}', expected '{expected_data['expected_result']}'")
                if actual.get("policy_decision") != expected_data["expected_policy_decision"]:
                    mismatch_reasons.append(f"policy_decision mismatch: got '{actual.get('policy_decision')}', expected '{expected_data['expected_policy_decision']}'")
                if actual.get("exit_code") != expected_data["expected_exit_code"]:
                    mismatch_reasons.append(f"exit_code mismatch: got {actual.get('exit_code')}, expected {expected_data['expected_exit_code']}")
                if completed.returncode != expected_data["expected_exit_code"]:
                    mismatch_reasons.append(f"process returncode mismatch: got {completed.returncode}, expected {expected_data['expected_exit_code']}")
                if actual.get("upstream_state") != expected_data["expected_upstream_state"]:
                    mismatch_reasons.append(f"upstream_state mismatch: got '{actual.get('upstream_state')}', expected '{expected_data['expected_upstream_state']}'")
                if actual.get("output_state") != expected_data["expected_output_state"]:
                    mismatch_reasons.append(f"output_state mismatch: got '{actual.get('output_state')}', expected '{expected_data['expected_output_state']}'")
                if actual.get("strict") != expected_data["expected_strict"]:
                    mismatch_reasons.append(f"strict mode mismatch: got {actual.get('strict')}, expected {expected_data['expected_strict']}")
                if actual.get("strict_upgrades_applied") != expected_data["expected_strict_upgrades_applied"]:
                    mismatch_reasons.append(f"strict_upgrades_applied mismatch: got {actual.get('strict_upgrades_applied')}, expected {expected_data['expected_strict_upgrades_applied']}")

                # Check lengths
                if len(actual.get("warnings", [])) < expected_data["expected_min_warnings"]:
                    mismatch_reasons.append(f"warnings count too low: got {len(actual.get('warnings', []))}, expected at least {expected_data['expected_min_warnings']}")
                if len(actual.get("blockers", [])) < expected_data["expected_min_blockers"]:
                    mismatch_reasons.append(f"blockers count too low: got {len(actual.get('blockers', []))}, expected at least {expected_data['expected_min_blockers']}")
                if len(actual.get("not_verified_reasons", [])) < expected_data["expected_min_not_verified_reasons"]:
                    mismatch_reasons.append(f"not_verified_reasons count too low: got {len(actual.get('not_verified_reasons', []))}, expected at least {expected_data['expected_min_not_verified_reasons']}")
                if len(actual.get("authority_claims_detected", [])) < expected_data["expected_min_authority_claims_detected"]:
                    mismatch_reasons.append(f"authority_claims count too low: got {len(actual.get('authority_claims_detected', []))}, expected at least {expected_data['expected_min_authority_claims_detected']}")

                # Text checks
                warnings_text = "\n".join(str(w) for w in actual.get("warnings", []))
                blockers_text = "\n".join(str(b) for b in actual.get("blockers", []))
                not_verified_text = "\n".join(str(r) for r in actual.get("not_verified_reasons", []))
                authority_text = "\n".join(str(c) for c in actual.get("authority_claims_detected", []))

                for item in expected_data.get("expected_warning_contains", []):
                    if item.lower() not in warnings_text.lower():
                        mismatch_reasons.append(f"warnings text missing: '{item}'")
                for item in expected_data.get("forbidden_warning_contains", []):
                    if item.lower() in warnings_text.lower():
                        mismatch_reasons.append(f"warnings text contains forbidden: '{item}'")
                for item in expected_data.get("expected_blocker_contains", []):
                    if item.lower() not in blockers_text.lower():
                        mismatch_reasons.append(f"blockers text missing: '{item}'")
                for item in expected_data.get("expected_not_verified_contains", []):
                    if item.lower() not in not_verified_text.lower():
                        mismatch_reasons.append(f"not_verified_reasons text missing: '{item}'")
                for item in expected_data.get("expected_authority_claim_contains", []):
                    if item.lower() not in authority_text.lower():
                        mismatch_reasons.append(f"authority claims text missing: '{item}'")

                normal_passed = len(mismatch_reasons) == 0

                if not normal_passed:
                    failed_diagnostics.append(f"fixture_expected_mismatch: Case {case_name} normal mode mismatches: {mismatch_reasons}.")
                    if runner_result != "M59_FIXTURE_RUNNER_BLOCKED":
                        runner_result = "M59_FIXTURE_RUNNER_FAIL"
                        exit_code = 1
                    failed_runs_count += 1
                else:
                    passed_runs_count += 1

                # Execute Strict Mode Run if required
                strict_passed = True
                if "strict_expected_result" in expected_data:
                    strict_cli_runs_count += 1
                    total_cli_runs_count += 1

                    strict_cmd = cmd + ["--strict"]
                    try:
                        completed_strict = subprocess.run(
                            strict_cmd,
                            capture_output=True,
                            text=True,
                            timeout=args.timeout,
                            check=False
                        )
                    except subprocess.TimeoutExpired:
                        blocked_diagnostics.append(f"fixture_timeout: Case {case_name} strict mode timed out.")
                        runner_result = "M59_FIXTURE_RUNNER_BLOCKED"
                        exit_code = 2
                        continue
                    except Exception as e:
                        blocked_diagnostics.append(f"fixture_execution_failed: Case {case_name} strict execution failed: {str(e)}.")
                        runner_result = "M59_FIXTURE_RUNNER_BLOCKED"
                        exit_code = 2
                        continue

                    try:
                        actual_strict = json.loads(completed_strict.stdout)
                    except Exception:
                        blocked_diagnostics.append(f"fixture_output_not_json: Case {case_name} strict CLI did not emit JSON.")
                        runner_result = "M59_FIXTURE_RUNNER_BLOCKED"
                        exit_code = 2
                        continue

                    strict_mismatches = []
                    if actual_strict.get("result") != expected_data["strict_expected_result"]:
                        strict_mismatches.append(f"result mismatch: got '{actual_strict.get('result')}', expected '{expected_data['strict_expected_result']}'")
                    if actual_strict.get("policy_decision") != expected_data["strict_expected_policy_decision"]:
                        strict_mismatches.append(f"policy_decision mismatch: got '{actual_strict.get('policy_decision')}', expected '{expected_data['strict_expected_policy_decision']}'")
                    if actual_strict.get("exit_code") != expected_data["strict_expected_exit_code"]:
                        strict_mismatches.append(f"exit_code mismatch: got {actual_strict.get('exit_code')}, expected {expected_data['strict_expected_exit_code']}")
                    if completed_strict.returncode != expected_data["strict_expected_exit_code"]:
                        strict_mismatches.append(f"process returncode mismatch: got {completed_strict.returncode}, expected {expected_data['strict_expected_exit_code']}")
                    if actual_strict.get("strict") is not True:
                        strict_mismatches.append(f"strict mode not set to true: got {actual_strict.get('strict')}")

                    # Min checks
                    if len(actual_strict.get("warnings", [])) < expected_data["strict_expected_min_warnings"]:
                        strict_mismatches.append(f"warnings count too low: got {len(actual_strict.get('warnings', []))}, expected at least {expected_data['strict_expected_min_warnings']}")
                    if len(actual_strict.get("blockers", [])) < expected_data["strict_expected_min_blockers"]:
                        strict_mismatches.append(f"blockers count too low: got {len(actual_strict.get('blockers', []))}, expected at least {expected_data['strict_expected_min_blockers']}")

                    # Optional strict checks
                    if "strict_expected_min_not_verified_reasons" in expected_data:
                        if len(actual_strict.get("not_verified_reasons", [])) < expected_data["strict_expected_min_not_verified_reasons"]:
                            strict_mismatches.append(f"not_verified_reasons count too low: got {len(actual_strict.get('not_verified_reasons', []))}, expected at least {expected_data['strict_expected_min_not_verified_reasons']}")

                    strict_warnings_text = "\n".join(str(w) for w in actual_strict.get("warnings", []))
                    strict_blockers_text = "\n".join(str(b) for b in actual_strict.get("blockers", []))

                    for item in expected_data.get("strict_expected_warning_contains", []):
                        if item.lower() not in strict_warnings_text.lower():
                            strict_mismatches.append(f"warnings text missing: '{item}'")
                    for item in expected_data.get("strict_forbidden_warning_contains", []):
                        if item.lower() in strict_warnings_text.lower():
                            strict_mismatches.append(f"warnings text contains forbidden: '{item}'")
                    for item in expected_data.get("strict_expected_blocker_contains", []):
                        if item.lower() not in strict_blockers_text.lower():
                            strict_mismatches.append(f"blockers text missing: '{item}'")

                    strict_passed = len(strict_mismatches) == 0
                    if not strict_passed:
                        failed_diagnostics.append(f"strict_fixture_expected_mismatch: Case {case_name} strict mode mismatches: {strict_mismatches}.")
                        if runner_result != "M59_FIXTURE_RUNNER_BLOCKED":
                            runner_result = "M59_FIXTURE_RUNNER_FAIL"
                            exit_code = 1
                        failed_runs_count += 1
                    else:
                        passed_runs_count += 1

                cases_run_metadata.append({
                    "case": case_name,
                    "is_positive": is_positive,
                    "normal_mode_passed": normal_passed,
                    "strict_mode_passed": strict_passed
                })

    except Exception as e:
        blocked_diagnostics.append(f"runner_internal_error: Runner execution aborted due to unhandled error: {str(e)}.")
        runner_result = "M59_FIXTURE_RUNNER_BLOCKED"
        exit_code = 2

    # Prepare output data
    output_data = {
        "runner_result": runner_result,
        "exit_code": exit_code,
        "policy_version": "M59.1",
        "positive_fixture_cases": positive_fixture_cases_count,
        "negative_fixture_cases": negative_fixture_cases_count,
        "total_fixture_cases": positive_fixture_cases_count + negative_fixture_cases_count,
        "normal_cli_runs": normal_cli_runs_count,
        "strict_cli_runs": strict_cli_runs_count,
        "total_cli_runs": total_cli_runs_count,
        "passed_runs": passed_runs_count,
        "failed_runs": failed_runs_count,
        "blocked_diagnostics": blocked_diagnostics,
        "failed_diagnostics": failed_diagnostics,
        "cases": cases_run_metadata,
        "non_authority": NON_AUTHORITY_STATEMENTS
    }

    if args.json:
        print(json.dumps(output_data, indent=2))
    else:
        print(f"RUNNER_RESULT: {output_data['runner_result']}")
        print(f"EXIT_CODE: {output_data['exit_code']}")
        print(f"POLICY_VERSION: {output_data['policy_version']}")
        print(f"POSITIVE_FIXTURE_CASES: {output_data['positive_fixture_cases']}")
        print(f"NEGATIVE_FIXTURE_CASES: {output_data['negative_fixture_cases']}")
        print(f"TOTAL_FIXTURE_CASES: {output_data['total_fixture_cases']}")
        print(f"NORMAL_CLI_RUNS: {output_data['normal_cli_runs']}")
        print(f"STRICT_CLI_RUNS: {output_data['strict_cli_runs']}")
        print(f"TOTAL_CLI_RUNS: {output_data['total_cli_runs']}")
        print(f"PASSED_RUNS: {output_data['passed_runs']}")
        print(f"FAILED_RUNS: {output_data['failed_runs']}")
        print(f"BLOCKED_DIAGNOSTICS: {output_data['blocked_diagnostics']}")
        print(f"FAILED_DIAGNOSTICS: {output_data['failed_diagnostics']}")
        for statement in NON_AUTHORITY_STATEMENTS:
            print(statement)

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
