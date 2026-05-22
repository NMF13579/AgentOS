## Final Status
M42_HK1_HOUSEKEEPING_COMPLETE_WITH_GAPS

## Decision
- Repository housekeeping scope was completed.
- Workspace junk files (`.icloud`) were removed.
- Pending M42.1 and M42.2–M42.4 integrity artifacts were committed.
- `memory-bank/project-status.md` was aligned to actual M40–M42 completion reviews.
- Forbidden-modification checks for M42.1–M42.4 are clean after housekeeping.
- Runtime behavior remained honest and unchanged in meaning:
  - regression self-test stays `INTEGRITY_REGRESSION_OK`
  - `all --strict` stays non-zero (`FAIL`)

## Why WITH_GAPS
- Existing repository-level strict failures are still present outside housekeeping scope.
- Housekeeping intentionally did not fix validator/runtime logic.

## Status Options
- M42_HK1_HOUSEKEEPING_COMPLETE
- M42_HK1_HOUSEKEEPING_COMPLETE_WITH_GAPS
- M42_HK1_HOUSEKEEPING_INCOMPLETE
- M42_HK1_HOUSEKEEPING_BLOCKED
