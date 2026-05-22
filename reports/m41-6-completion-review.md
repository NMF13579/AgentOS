## Final Status
M41_6_UNIFIED_INTEGRITY_CONSOLIDATION_COMPLETE_WITH_GAPS

## Decision
- M41.5 status allows continuation (`M41_5_ALL_STRICT_INTEGRITY_COMPLETE_WITH_GAPS`).
- Required M41.1–M41.5 reports exist.
- `integrity --fixtures --json` and `integrity --strict --fixtures --json` work.
- Fixture registry exists and is valid JSON.
- `integrity --list-fixtures --json` works.
- Result UX commands work.
- `all --strict` includes integrity and executes, while retaining known non-integrity baseline failures.
- No new P0 false-authority claim found.
- No new regression beyond documented gaps found.
- No files outside M41.6 closure outputs modified.

## Known Gaps
- `all --strict` remains non-zero due known baseline failures outside M41 consolidation scope.
- `all --strict --json` is valid but remains aggregate-style and not a dedicated all-strict integrity envelope.
- Some source detail in human-readable all-strict output remains summarized.

## Status Options
- M41_6_UNIFIED_INTEGRITY_CONSOLIDATION_COMPLETE
- M41_6_UNIFIED_INTEGRITY_CONSOLIDATION_COMPLETE_WITH_GAPS
- M41_6_INCOMPLETE
- M41_6_BLOCKED
