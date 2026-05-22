## Task
M43.3 Fixture Footprint Audit / Safe Regression Fixture Consolidation Plan

## Preconditions
- M43.2 status found: `M43_2_REPORT_ARCHIVE_PLAN_COMPLETE_WITH_GAPS`
- Continuation allowed by precondition rules.

## Created Files
- `reports/m43-3-fixture-footprint-inventory.md`
- `reports/m43-3-fixture-coverage-preservation-map.md`
- `reports/m43-3-safe-fixture-consolidation-plan.md`
- `reports/m43-3-completion-review.md`

## Coverage Summary
- Discovered fixture files: 2891
- Listed inventory rows: 2891
- Intentionally excluded fixture files: 0
- Fixture roots reviewed: 75
- Each discovered fixture file has an inventory row.
- No fixture modifications were performed.

## Gaps
- Some fixture references remain `none_found` and require M43.4+ review.
- Some fixture classes are `UNKNOWN_NEEDS_REVIEW` due limited active-reference evidence in current scan.
- Failure classes `TOKEN_CONTRACT_REGRESSION` and `FIXTURE_ROOT_MISSING` are marked `not_found` in direct fixture-name scan.

## Final Status
M43_3_FIXTURE_CONSOLIDATION_PLAN_COMPLETE_WITH_GAPS

## Allowed Status Set
- M43_3_FIXTURE_CONSOLIDATION_PLAN_COMPLETE
- M43_3_FIXTURE_CONSOLIDATION_PLAN_COMPLETE_WITH_GAPS
- M43_3_INCOMPLETE
- M43_3_BLOCKED
