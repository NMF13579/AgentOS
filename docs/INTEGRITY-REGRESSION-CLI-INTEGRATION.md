## Purpose
This document describes how integrity regression checks are exposed through `scripts/agentos-validate.py`.

Regression CLI integration detects drift; it does not grant approval.

## Wrapper Behavior
- New command: `python3 scripts/agentos-validate.py integrity-regression`
- Wrapper delegates to `python3 scripts/test-integrity-regression.py`.
- Human-readable mode passes through runner text output.
- JSON mode passes through runner JSON output when valid.

## Runner Relationship
- `agentos-validate.py` is a command gateway.
- `test-integrity-regression.py` is the executable regression checker.
- Wrapper exit code must match runner exit code.

## JSON Preservation
- `integrity-regression --json` runs runner in JSON mode.
- If runner JSON is valid, wrapper preserves runner `result` and payload.
- If runner JSON is invalid, wrapper returns blocked safe JSON:
  - `suite: integrity-regression-wrapper`
  - `result: INTEGRITY_REGRESSION_BLOCKED`
  - `failure_class: INVALID_RUNNER_JSON`

## Self-Test Fixture Forwarding
- `--self-test-fixtures` is forwarded to runner.
- `--fixture-root <path>` is forwarded unchanged.
- Missing fixture root from runner (for example `FIXTURE_ROOT_MISSING`) is preserved by wrapper output.

## Strict Path Integration
- `all --strict` includes regression check in recursion-safe mode.
- Integrated command path uses machine JSON:
  - `python3 scripts/agentos-validate.py integrity-regression --json --skip-all-strict-check`

## Recursion Boundary
all --strict must not call a regression mode that calls all --strict again.

- Standalone runner still checks `all --strict` by default.
- Integration-safe strict path uses `--skip-all-strict-check` only to prevent recursion loops.
- Skip marker must be visible in details: `Skipped to prevent all --strict recursion.`

## Known Gaps
- Known gaps are not clean regression PASS.
- Existing repository baseline failures may still keep `all --strict` non-zero.
- This integration does not reinterpret failures as approvals.

## Invalid Runner JSON Handling
- In JSON wrapper mode, invalid runner JSON is converted to safe blocked JSON summary.
- Raw output is not dumped in full.

## Non-Approval Boundary
Regression runner result is validation evidence, not approval.

Human approval remains above every PASS.

## Explicit Non-Changes
- M42.4 does not create new Honest PASS behavior.
- M42.4 does not create new validators.
- M42.4 does not change INTEGRITY_REGRESSION top-level result semantics.
