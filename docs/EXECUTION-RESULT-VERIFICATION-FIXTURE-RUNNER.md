# Execution Result Verification Fixture Runner

## Purpose

This document details the Execution Result Verification Fixture Runner for milestone M59. The runner is designed to automatically evaluate the check CLI script against all defined positive and negative fixtures to ensure policy compliance.

## Preconditions

The preconditions for executing the fixture runner are:
1. `scripts/check-execution-result-verification.py` exists
2. `docs/EXECUTION-RESULT-VERIFICATION-CLI.md` exists and contains `FINAL_STATUS: M59_EXECUTION_RESULT_VERIFICATION_CLI_DEFINED`
3. `tests/fixtures/execution-result-verification/positive` exists
4. `tests/fixtures/execution-result-verification/negative` exists

## Position in M59

The fixture runner represents task 59.10 in the M59 milestone chain. It verifies the behavioral correctness of the CLI (59.8) against positive fixtures (59.9.1) and negative fixtures (59.9.2), preparing the codebase for integration summaries (59.11).

## Runner Role

The fixture runner acts as a test validation harness.
- M59 fixture runner result is not execution result verification.
- M59 fixture runner result is not task approval.
- M59 fixture runner result does not authorize merge, push, release, or lifecycle mutation.
- M59 fixture runner result does not replace human review.
- M59 fixture runner result does not create evidence report or completion review.

## Runner Arguments

The runner supports the following arguments:
- `--root`: Specifies the repository root directory (defaults to current directory).
- `--json`: Forces JSON-only output to stdout.
- `--explain`: Prints human-readable details and exit.
- `--positive-only`: Runs only positive cases (mutually exclusive with negative-only).
- `--negative-only`: Runs only negative cases (mutually exclusive with positive-only).
- `--timeout`: Specifies execution timeout in seconds (default is 30, must be positive).

## Fixture Roots

The runner discovers cases in the following directories relative to `--root`:
- Positive root: `tests/fixtures/execution-result-verification/positive`
- Negative root: `tests/fixtures/execution-result-verification/negative`

## Expected Fixture Inventory

The runner expects exactly the following inventories:
- Positive cases (4):
  - `positive-clean-verified`
  - `positive-verified-with-warnings`
  - `positive-output-verified-with-warnings`
  - `positive-strict-preserves-non-ambiguous-warning`
- Negative cases (7):
  - `negative-upstream-blocked-output-verified`
  - `negative-upstream-not-verified-output-verified`
  - `negative-authority-claim`
  - `negative-human-review-required-false`
  - `negative-human-review-handoff-false`
  - `negative-strict-ambiguous-warning`
  - `negative-malformed-json`

Total count matches: 11 cases, resulting in 11 normal runs and 2 strict runs (total 13 CLI runs).

## Fixture File Contract

Each case directory must contain exactly:
- `input.json`
- `preconditions.json`
- `diff-scope.json`
- `validation-evidence.json`
- `result-output.json`
- `expected.json`
- `README.md`

Exception:
- `negative-malformed-json/input.json` must be intentionally malformed JSON.

All other JSON files must be syntactically valid.

## Expected Oracle Contract

Every `expected.json` file must contain:
- `policy_version`
- `expected_result`
- `expected_policy_decision`
- `expected_exit_code`
- `expected_upstream_state`
- `expected_output_state`
- `expected_strict`
- `expected_strict_upgrades_applied`
- `expected_min_warnings`
- `expected_min_blockers`
- `expected_min_not_verified_reasons`
- `expected_min_authority_claims_detected`
- `expected_warning_contains`
- `forbidden_warning_contains`

For negative fixtures, it must also contain:
- `expected_blocker_contains`
- `expected_not_verified_contains`
- `expected_authority_claim_contains`

## Policy Version

Every expected oracle file must declare `policy_version` as `"M59.1"`. Any other policy version blocks the runner.

## Normal Mode Execution

In normal mode, the runner invokes the CLI for each case using Python subprocess with the case's parameters.

## Strict Mode Execution

If the `expected.json` contains `strict_expected_result`, the runner automatically re-runs the fixture with the `--strict` argument.

## Comparison Rules

The runner compares actual CLI JSON outputs against expected oracle parameters.
- Exact matches are checked for result, policy decision, exit code, upstream state, output state, strict, and strict upgrades applied.
- Minimum count checks are performed on warnings, blockers, reasons, and claims.
- Substring inclusions and exclusions are validated on text lists.

## Diagnostic Codes

The runner implements the following diagnostic codes:
- `missing_cli`
- `missing_docs`
- `wrong_cli_status`
- `missing_fixture_root`
- `unexpected_fixture_case`
- `missing_expected_json`
- `invalid_expected_json`
- `unsupported_policy_version`
- `missing_fixture_file`
- `unexpected_fixture_file`
- `fixture_json_invalid`
- `malformed_fixture_not_malformed`
- `fixture_execution_failed`
- `fixture_timeout`
- `fixture_output_not_json`
- `fixture_expected_mismatch`
- `strict_fixture_expected_mismatch`
- `runner_internal_error`

## Runner Result Values

The runner outputs exactly one of the following result strings:
- `M59_FIXTURE_RUNNER_PASS`: Discovered all expected cases, and all runs matched their oracle parameters.
- `M59_FIXTURE_RUNNER_FAIL`: Discovered and parsed cases successfully, but at least one run mismatched its oracle parameters.
- `M59_FIXTURE_RUNNER_BLOCKED`: Setup error, invalid path safety, malformed oracle config, or runtime timeouts prevented full comparison.

## Exit Code Mapping

The runner exit codes map as follows:
- `M59_FIXTURE_RUNNER_PASS` -> exit 0
- `M59_FIXTURE_RUNNER_FAIL` -> exit 1
- `M59_FIXTURE_RUNNER_BLOCKED` -> exit 2

## JSON Output

JSON output mode returns structured JSON detailing exit codes, inventory counts, run statistics, failed/blocked diagnostics lists, and cases metadata.

## Human Output

Human-readable output summarizes cases counts, run statistics, diagnostics lists, and displays the required non-authority rules.

## Explain Output

Explain mode provides detail on fixture roots, expected/run inventory, checked oracle fields, diagnostics, and non-authority boundaries.

## Fail-Closed Behavior

Any setup error, parameter error, structural files contract mismatch, or JSON syntax failure (excluding malformed JSON input) blocks runner comparison and immediately triggers exit 2.

## Non-Authority Rules

The runner and this documentation enforce the following boundaries:
- M59 fixture runner result is not execution result verification.
- M59 fixture runner result is not task approval.
- M59 fixture runner result does not authorize merge, push, release, or lifecycle mutation.
- M59 fixture runner result does not replace human review.
- M59 fixture runner result does not create evidence report or completion review.

## Relationship to 59.8 CLI

The runner validates the policy checks implemented in the verification CLI (59.8).

## Relationship to 59.9 Fixtures

The runner automatically runs positive (59.9.1) and negative (59.9.2) fixtures.

## Relationship to 59.11 Integration Summary

The results collected by this runner are integrated and referenced by the integration summary (59.11).

## Forbidden Claims

The documentation must not claim that execution result was verified or task was approved.

## Final Runner Status

```text
FINAL_STATUS: M59_EXECUTION_RESULT_VERIFICATION_FIXTURE_RUNNER_DEFINED
```

This means only that the runner and runner documentation exist.

It does not mean execution result was verified.

It does not mean task completion was approved.

It does not mean evidence report exists.

It does not mean completion review exists.
