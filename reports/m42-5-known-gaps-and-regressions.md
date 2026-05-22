## Known Gaps Preserved
Gap | Source Report | Still Present | Severity | Recommended Next Action
--- | --- | --- | --- | ---
`summary-json-conflict` fails in runner | `reports/m42-2-completion-review.md`, `reports/m42-4-completion-review.md` | Yes | `P1` | Align conflict behavior path and rerun runner in M42.6+
`warning-not-clean-pass` needs-review in runner | `reports/m42-2-completion-review.md` | Yes | `P2` | Tighten wording/placement checks or evidence extraction in M42.6+
`all --strict` remains non-zero due baseline failures | `reports/m42-1-completion-review.md`, `reports/m42-4-completion-review.md` | Yes | `P1` | Keep explicit in closure and continue remediation in later milestone

## New Regressions
No new regressions detected in M42.5 command run set.

## Expected Non-Zero Safety Behaviors
- `python3 scripts/agentos-validate.py integrity-regression --self-test-fixtures --fixture-root /tmp/agentos-missing-integrity-regression-fixtures --json`
  - Observed: non-zero with `INTEGRITY_REGRESSION_BLOCKED` and `FIXTURE_ROOT_MISSING`
  - Classification: expected safety behavior.

Expected non-zero safety behavior is not a regression.

## Deferred Items
- Final closure judgement for full M42 chain in M42.6.
- Optional stricter normalization around warning phrase checks.

## P0/P1 Summary
P0: blocks M42.6 if false approval, false authorization, recursion ambiguity, hidden regression, or broken core runner appears.
P1: does not automatically block M42.6 when explicitly documented, but must have assigned next action.
Current count:
- P0 unresolved: 0
- P1 unresolved: 2
