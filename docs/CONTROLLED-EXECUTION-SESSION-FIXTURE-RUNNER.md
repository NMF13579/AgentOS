# Controlled Execution Session Fixture Runner

## Purpose

This document defines the interface, behaviors, validation logic, and design constraints of the M58 Controlled Execution Session Fixture Runner.

The fixture runner discovers, validates, and runs all M58 positive and negative test fixtures against the 58.7 CLI. It compares actual stdout results and exit codes against the expected oracle metadata. It does not open execution sessions. It does not authorize execution. It does not approve task completion. It does not verify execution results. It does not mutate lifecycle state.

## Preconditions

Before executing the runner, the following conditions must be met:
- The M58 CLI script `scripts/check-controlled-execution-session.py` exists and is parseable.
- Positive fixtures exist under `tests/fixtures/controlled-execution-session/positive/`.
- Negative fixtures exist under `tests/fixtures/controlled-execution-session/negative/`.
- All required M58 contract and policy files are defined.

## Position in M58

This is task 58.9. It follows 58.8.1 and 58.8.2 (positive and negative fixtures) and precedes 58.10 (Integration Summary). It serves as the test validation harness for the M58 readiness CLI.

## Runner Inputs

The runner accepts discovered test fixtures containing:
- `request.json`
- `preconditions.json`
- `boundary.json`
- `record.json`
- `expected.json` (oracle file)

## Runner Arguments

The runner supports the following command-line arguments:
- `--json`: Emit validation results as valid JSON only.
- `--explain`: Print human-readable explanations of the validation runs.
- `--positive-only`: Run only the discovered positive test cases.
- `--negative-only`: Run only the discovered negative test cases.
- `--root <path>`: Override the repository root for path resolving.
- `--help`: Print the help message and exit.

## Fixture Discovery

The runner discovers cases by listing positive and negative subdirectories under the resolved fixtures path. It ensures that the exact discovered folder list matches the expected set of positive and negative cases.

## Root and Path Safety

The runner implements rigorous path normalization:
- All discovered fixture directories and file paths are resolved.
- Discovered paths, CLI paths, and temporary directories are validated to reside strictly within the resolved repository root directory.
- symlink traversal or directory escape attempts fail closed, returning `M58_FIXTURE_RUNNER_BLOCKED` and exit code 2.

## Expected Fixture Counts

The runner expects exactly:
- Positive cases: 3
- Negative cases: 14
- Total cases: 17
Missing or extra cases fail closed.

## Expected JSON as Oracle

Each fixture directory includes an `expected.json` containing the oracle fields:
- `expected_result`
- `expected_policy_decision`
- `expected_exit_code`
- `non_authority_required`
For positive cases, it may also define strict expectations. The runner compares CLI outputs against these fields.

## Positive Fixture Handling

Positive fixtures are executed to ensure that valid, clean readiness states or warning states (in non-strict mode) succeed (exit 0).

## Negative Fixture Handling

Negative fixtures are executed to ensure that draft, blocked, malformed, unsafe, contradictory, or traversal states are correctly blocked (exit 1 or 2). Non-zero exit codes from the CLI are verified to match the oracle exit codes.

## Strict Expectation Handling

If strict oracle fields are present in a fixture's expected.json (e.g. for `positive-ready-with-warnings`), the runner performs a second execution of the CLI with the `--strict` option and asserts that it matches the strict exit code and status expectations.

## Result Values

The runner emits exactly one of:
- `M58_FIXTURE_RUNNER_PASS`
- `M58_FIXTURE_RUNNER_FAIL`
- `M58_FIXTURE_RUNNER_BLOCKED`

## Exit Code Mapping

- `M58_FIXTURE_RUNNER_PASS` -> exit 0
- `M58_FIXTURE_RUNNER_FAIL` -> exit 1
- `M58_FIXTURE_RUNNER_BLOCKED` -> exit 2

Runner exit 0 does not authorize execution. Runner exit 0 does not approve task completion. Runner exit 0 does not verify result.

## JSON Output

In `--json` mode, output is valid JSON only:
```json
{
  "result": "M58_FIXTURE_RUNNER_PASS",
  "exit_code": 0,
  "summary": {
    "positive_cases": 3,
    "negative_cases": 14,
    "total_cases": 17,
    "passed_cases": 17,
    "failed_cases": 0,
    "blocked_cases": 0,
    "strict_cases_run": 1
  },
  "cases": [
    {
      "name": "positive-clean-ready",
      "group": "positive",
      "result": "PASS",
      "expected_result": "CONTROLLED_EXECUTION_SESSION_READY",
      "actual_result": "CONTROLLED_EXECUTION_SESSION_READY",
      "expected_exit_code": 0,
      "actual_exit_code": 0
    }
  ],
  "non_authority": [
    "M58 fixture runner does not open an execution session.",
    "M58 fixture runner does not authorize task completion.",
    "M58 fixture runner does not verify execution result.",
    "M58 fixture runner does not create approval.",
    "M58 fixture runner does not authorize merge, push, or release.",
    "M58 fixture runner does not mutate lifecycle state."
  ]
}
```

## Human Output

By default, the runner prints human-readable outputs:
- `RESULT: <runner result>`
- `TOTAL_CASES: <count>`
- `PASSED_CASES: <count>`
- `FAILED_CASES: <count>`
- `BLOCKED_CASES: <count>`
- `STRICT_CASES_RUN: <count>`
Along with the required non-authority statements.

## Explain Output

When running in `--explain` mode, the runner prints detailed reports on:
- Discovered fixtures.
- Oracle expected results.
- Passed, failed, or blocked cases.
- Strict expectations evaluated.
- Path containment results.
- Why the result is not execution approval, task completion, or result verification.

## Timeout Behavior

Individual CLI runs are executed with a timeout limit of 30 seconds. If any case exceeds this, the test is failed.

## Fail-Closed Behavior

Any malformed files, missing expectations, CLI crash, path escape, or argument parsing errors immediately block the runner.

## Non-Authority Rules

- M58 fixture runner does not open an execution session.
- M58 fixture runner does not authorize task completion.
- M58 fixture runner does not verify execution result.
- M58 fixture runner does not create approval.
- M58 fixture runner does not authorize merge, push, or release.
- M58 fixture runner does not mutate lifecycle state.
- M58 fixture runner only validates controlled execution session fixtures against the 58.7 CLI.

## Relationship to 58.7 CLI

The runner acts as the test execution harness for the M58 CLI, asserting that it implements M58 policy correctly.

## Relationship to 58.10 Integration Summary

The integration summary will consume the test execution statistics from the runner as verification evidence.

## Relationship to M59 Verification

The runner ensures that the M58 layer is structurally ready and tested before handing off execution evidence to M59 verification.

## Forbidden Claims

The runner and docs do not claim:
- execution session is open
- execution is authorized
- task is complete
- result is verified
- task is approved
- human review is replaced
- M59 verification is optional
- commit is allowed
- push is allowed
- merge is allowed
- release is allowed
- lifecycle state may be mutated

## Final Runner Status

FINAL_STATUS: M58_CONTROLLED_EXECUTION_SESSION_FIXTURE_RUNNER_DEFINED

This status means only that the fixture runner and runner documentation exist.
It does not mean execution was authorized.
It does not mean execution session was opened.
It does not mean result was verified.
