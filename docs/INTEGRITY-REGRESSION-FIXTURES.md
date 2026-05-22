# Integrity Regression Fixtures

## Purpose
Define static negative fixtures used by regression-runner self-test mode.

Negative fixtures test the regression runner. They must not change Honest PASS semantics.
Regression fixtures are static test data, not policy authority.
Regression runner result is validation evidence, not approval.
Known gaps are not clean regression PASS.
Human approval remains above every PASS.

## Fixture Format
Each fixture is a directory under `tests/fixtures/integrity-regression/` with `fixture.json` plus referenced input files.

Required manifest fields:
- `id`
- `description`
- `kind`
- `expected_check_status`
- `expected_failure_class`
- `expected_runner_result_floor`
- `input_files`

## Positive vs Negative Fixture Semantics
- These fixtures are primarily negative/control fixtures.
- A fixture test is considered PASS when the runner detects the expected failure or needs-review outcome.

## Self-Test Mode
- `python3 scripts/test-integrity-regression.py --self-test-fixtures`
- `python3 scripts/test-integrity-regression.py --self-test-fixtures --json`
- `python3 scripts/test-integrity-regression.py --self-test-fixtures --fixture-root tests/fixtures/integrity-regression --json`

## Fixture Root
Default root: `tests/fixtures/integrity-regression`

If root is missing:
- result must be blocked
- failure class: `FIXTURE_ROOT_MISSING`

## Expected Failure Class and Runner Result Floor
Each fixture defines:
- expected check status (`FAIL`, `NEEDS_REVIEW`, etc.)
- expected failure class
- expected minimum runner-result floor

## Known Gap Handling
Known-gap fixtures must not produce clean regression OK.

## Authority-Boundary Fixture Behavior
Authority-boundary fixtures can model:
- no files available -> needs review
- false approval phrase present -> fail

## Command-Behavior Fixture Input Format
For `kind: command-behavior`, input file format:

```json
{
  "simulated_exit_code": 0,
  "simulated_stdout": "",
  "simulated_stderr": "error: unrecognized arguments"
}
```

Self-test mode consumes this simulated output and does not execute real fixture-provided commands.

## Missing Fixture-Root Behavior
Missing root must return blocked result with missing-path detail; runner must not create directories.

## Non-Approval Boundary
M42.3 does not modify agentos-validate.py.
M42.3 does not create new Honest PASS behavior.
M42.3 does not create approval records.
