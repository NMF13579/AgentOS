## Final Status
M42_2_REGRESSION_RUNNER_COMPLETE_WITH_GAPS

## Decision
- M42.1 status allows continuation (`M42_1_REGRESSION_BASELINE_COMPLETE_WITH_GAPS`).
- Runner exists and executes.
- Runner help works.
- Runner JSON output is valid JSON.
- Required regression checks are implemented.
- Authority-boundary checks are implemented.
- Authority-boundary missing-file behavior is implemented.
- Unknown-token, abbreviation-safety, summary/json conflict, and shell regression checks are implemented.
- Evidence report exists.
- Completion review exists.
- No implementation files modified except runner and M42.2 reports.

## Why not COMPLETE
- Runner detected live drift/failures (notably summary/json conflict message contract), so baseline is executable but not clean.
- Additional semantic alignment work remains for M42.3.

## Known Gaps
- Existing repository baseline failures still affect strict aggregate paths.
- Warning phrase check has one needs-review path when evaluated in JSON-details context.

## Status Options
- M42_2_REGRESSION_RUNNER_COMPLETE
- M42_2_REGRESSION_RUNNER_COMPLETE_WITH_GAPS
- M42_2_INCOMPLETE
- M42_2_BLOCKED
