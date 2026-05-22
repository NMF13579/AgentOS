# M41.5 All Strict Integrity Evidence Report

## M41.4 status inspected
- Source: `reports/m41-4-completion-review.md`
- Status found: `M41_4_RESULT_UX_COMPLETE_WITH_GAPS`

## Summary
M41.5 integrates unified integrity checks into all --strict.
M41.5 does not create new validators.
M41.5 does not create new security policy.
M41.5 does not change source-token semantics.
all --strict may include integrity checks, but it must not turn validation PASS into human approval.
all --strict must not parse human-readable summary output.
Unified status is navigation metadata, not replacement for source token.
INTEGRITY_WARNING is not clean PASS.
Human approval remains above every PASS.

## dependency precondition results
- `python3 scripts/agentos-validate.py integrity --help` -> exit 0
- `python3 scripts/agentos-validate.py integrity --strict --fixtures --json` -> exit 0
- `python3 scripts/agentos-validate.py integrity --strict --fixtures --summary` -> exit 0
- `python3 scripts/agentos-validate.py all --help` -> exit 0

## docs created
- `docs/ALL-STRICT-INTEGRITY-INTEGRATION.md`

## CLI changes made
- Modified `scripts/agentos-validate.py`.
- In `all --strict`, integrity stage now calls machine-readable command:
  - `python3 scripts/agentos-validate.py integrity --strict --fixtures --json`
- No summary parsing was introduced in `all --strict`.

## all --strict integration approach
- Existing `all --strict` checks are preserved.
- Integrity stage is appended safely as `integrity-strict-fixtures` check.
- Integrity JSON is parsed and mapped to existing PASS/WARN/FAIL aggregator contract.

## whether existing all --strict behavior was preserved
- Preserved: existing checks still run.
- Preserved: overall aggregate output shape (`result`, `checks`, counters).

## integrity command used internally
- Internal command is exactly `integrity --strict --fixtures --json`.

## source token preservation summary
- Integrity stage summary now includes:
  - integrity result
  - source tokens (when present)
  - warning/violation/needs-review/blocked counts
  - next safe action
- Minimum required fields are preserved:
  - integrity command run
  - integrity result
  - exit code

## optional source field handling
- Optional fields are accessed with `.get()` and defaults.
- Missing optional fields do not raise `KeyError` and do not crash `all --strict`.

## warning behavior summary
- `INTEGRITY_WARNING` maps to `WARN` in all-strict aggregator and keeps non-blocking exit behavior.
- `INTEGRITY_WARNING is not clean PASS.` remains explicitly documented.

## blocking semantics review for INTEGRITY_VIOLATION, INTEGRITY_BLOCKED, and INTEGRITY_NEEDS_REVIEW
- `INTEGRITY_VIOLATION` -> non-zero / exit 1 path via FAIL mapping.
- `INTEGRITY_BLOCKED` -> non-zero / exit 1 path via FAIL mapping.
- `INTEGRITY_NEEDS_REVIEW` -> non-zero / exit 1 path via FAIL mapping.

## JSON behavior if available
- `all --strict --json` runs and returns valid JSON.
- Integrity subcheck is present in `checks` array with command and summary details.

## all --strict result
- Command executed: `python3 scripts/agentos-validate.py all --strict`
- Exit code: 1
- Result is non-zero due existing baseline failures outside M41.5 scope.
- Integrity stage executed and returned warning-level mapped check (`WARN`).

## all --strict --json result or gap
- Command executed: `python3 scripts/agentos-validate.py all --strict --json`
- JSON output valid.
- Exit code: 1 (same baseline failures).
- No JSON integration gap observed for this repository state.

## commands run
- M41.5 dependency checks from task
- `python3 scripts/agentos-validate.py all --strict`
- `python3 scripts/agentos-validate.py all --strict --json`
- Required grep and negative grep checks from task

## validation gaps
- Global strict baseline failures remain and are outside M41.5 integration scope.

## known limitations
- all-strict top-level output remains aggregate-style; deep per-subcheck source payload is summarized.
- Human-readable `all --strict` output does not print full nested integrity source JSON.

## recommended M41.6 action
- Add optional structured `integrity` section at top level for `all --strict --json` while preserving existing compatibility.
- Add clearer, dedicated strict-summary guidance line for baseline failures vs integrity findings.
