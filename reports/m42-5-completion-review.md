## Final Status
M42_5_REGRESSION_EVIDENCE_CONSOLIDATED_WITH_GAPS

## Decision
- M42.4 status allows continuation.
- All required M42.5 reports were created.
- Runner evidence collected.
- Self-test fixture evidence collected.
- Official CLI wrapper evidence collected.
- Recursion-safe option evidence collected.
- `all --strict` evidence collected (with known gaps, non-zero preserved honestly).
- No new critical regression detected.
- No false approval/authorization claim introduced.

## Why WITH_GAPS
- Known gaps from M42.1–M42.4 remain unresolved (`summary-json-conflict`, `warning-not-clean-pass`, strict baseline failures).
- Gaps are explicit and non-misleading.

## M42.6 Readiness
M42.6 can start because evidence is materially consolidated and no P0 gap is open.

## Status Options
- M42_5_REGRESSION_EVIDENCE_CONSOLIDATED
- M42_5_REGRESSION_EVIDENCE_CONSOLIDATED_WITH_GAPS
- M42_5_INCOMPLETE
- M42_5_BLOCKED
