## M42.3 status inspected
- Source: `reports/m42-3-completion-review.md`
- Found: `M42_3_NEGATIVE_REGRESSION_FIXTURES_COMPLETE_WITH_GAPS`
- Preconditions satisfied.

## Dependency precondition results
- `python3 scripts/test-integrity-regression.py --help` -> exit 0.
- `python3 scripts/test-integrity-regression.py --json` -> exit 1 (usable, expected baseline failures).
- `python3 scripts/test-integrity-regression.py --self-test-fixtures --json` -> exit 0.
- `python3 scripts/agentos-validate.py all --help` -> exit 0.

## existing integrity-regression subcommand handling
- Before M42.4: no `integrity-regression` subcommand was present in `scripts/agentos-validate.py`.
- M42.4 adds a single wrapper subcommand (no duplication).

## Files changed
- Updated `scripts/agentos-validate.py`
- Updated `scripts/test-integrity-regression.py`
- Added `docs/INTEGRITY-REGRESSION-CLI-INTEGRATION.md`

## Runner changes made
- Added `--skip-all-strict-check` to `scripts/test-integrity-regression.py`.
- Standalone behavior preserved: without flag runner still checks `all --strict`.
- With skip flag, only `all-strict` internal check is skipped.
- Skip detail recorded: `Skipped to prevent all --strict recursion.`

## AgentOS CLI changes made
- Added wrapper command:
  - `python3 scripts/agentos-validate.py integrity-regression`
  - `python3 scripts/agentos-validate.py integrity-regression --json`
  - `python3 scripts/agentos-validate.py integrity-regression --json --skip-all-strict-check`
  - `python3 scripts/agentos-validate.py integrity-regression --self-test-fixtures --json`
  - `python3 scripts/agentos-validate.py integrity-regression --self-test-fixtures --fixture-root tests/fixtures/integrity-regression --json`

## JSON preservation result
- Wrapper JSON mode preserves runner JSON when valid.
- `integrity-regression --json` output validated with `python3 -m json.tool`.
- Wrapper exit code matches runner exit code.

## invalid runner JSON handling
- Implemented safe fallback payload with:
  - `result: INTEGRITY_REGRESSION_BLOCKED`
  - `failure_class: INVALID_RUNNER_JSON`
  - `error: invalid_runner_json`
- Behavior documented in integration doc.

## Wrapper --skip-all-strict-check forwarding result
- Wrapper forwards flag to runner.
- Command run:
  - `python3 scripts/agentos-validate.py integrity-regression --json --skip-all-strict-check`
- JSON output valid; skip marker preserved in check details.

## Self-test fixture forwarding result
- `python3 scripts/agentos-validate.py integrity-regression --self-test-fixtures --json` -> exit 0, valid JSON.
- Explicit root forwarding:
  - `python3 scripts/agentos-validate.py integrity-regression --self-test-fixtures --fixture-root tests/fixtures/integrity-regression --json` -> exit 0, valid JSON.

## all --strict integration result or gap
- Integrated into strict path with recursion-safe mode.
- `all --strict` now includes two integrity checks:
  - `integrity-strict-fixtures`
  - `integrity-regression-strict`
- Verification from `all --strict --json` confirms presence of `integrity-regression-strict`.
- Overall `all --strict` remains non-zero due existing baseline failures; this is preserved honestly.

## Exit semantics result
- Wrapper command returns runner exit codes.
- `INTEGRITY_REGRESSION_OK` -> 0
- `INTEGRITY_REGRESSION_FAILED` -> non-zero
- `INTEGRITY_REGRESSION_NEEDS_REVIEW` -> non-zero
- `INTEGRITY_REGRESSION_BLOCKED` -> non-zero

## backward compatibility result
- Existing runner commands still work:
  - `--help`
  - `--json`
  - `--self-test-fixtures --json`
  - `--self-test-fixtures --fixture-root tests/fixtures/integrity-regression --json`
- New flag does not change default behavior when absent.

## Commands run
- `python3 -m py_compile scripts/agentos-validate.py scripts/test-integrity-regression.py`
- `python3 scripts/agentos-validate.py integrity-regression --help`
- `python3 scripts/agentos-validate.py integrity-regression --json`
- `python3 scripts/agentos-validate.py integrity-regression --json --skip-all-strict-check`
- `python3 scripts/agentos-validate.py integrity-regression --self-test-fixtures --json`
- `python3 scripts/agentos-validate.py integrity-regression --self-test-fixtures --fixture-root tests/fixtures/integrity-regression --json`
- `python3 scripts/test-integrity-regression.py --json --skip-all-strict-check`
- `python3 scripts/agentos-validate.py all --strict`
- `python3 scripts/agentos-validate.py all --strict --json`

## Known gaps
- Runner baseline still contains known fail/needs-review checks from earlier milestones.
- Repository has unrelated pre-existing working tree noise outside M42.4 scope, which may affect strict forbidden-path cleanliness checks.

## Required boundary statements
- M42.4 integrates the integrity regression runner into the official AgentOS CLI surface.
- M42.4 does not create new Honest PASS behavior.
- M42.4 does not create new validators.
- M42.4 does not change INTEGRITY_REGRESSION top-level result semantics.
- Regression CLI integration detects drift; it does not grant approval.
- Regression runner result is validation evidence, not approval.
- all --strict must not call a regression mode that calls all --strict again.
- Known gaps are not clean regression PASS.
- Human approval remains above every PASS.

## Recommended M42.5 action
- Stabilize remaining regression failures to move from COMPLETE_WITH_GAPS to COMPLETE.
- Add explicit regression-wrapper test for invalid runner JSON branch in controlled test harness.
