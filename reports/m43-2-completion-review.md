## Task
M43.2 Historical Reports Archive Plan / Safe Report Reduction

## Preconditions
- M43.1 status found: `M43_1_FOOTPRINT_AUDIT_COMPLETE_WITH_GAPS`
- Continuation allowed by precondition rules.

## Created Files
- `reports/m43-2-historical-report-archive-map.md`
- `reports/m43-2-report-retention-index.md`
- `reports/m43-2-safe-report-reduction-plan.md`
- `reports/m43-2-completion-review.md`

## Coverage
- Total discovered reports (m40/m41/m42/m43-1): 71
- Individually listed rows in archive map: 71
- M40, M41, M42, M43.1 discovered groups each have concrete rows.
- Classification model applied.
- Enumeration method recorded.
- No placeholder rows used.
- No archive/move/delete/rewrite action performed.

## Gaps
- Some rows remain `UNKNOWN_NEEDS_REVIEW` due unverifiable active dependency in current scan.
- Some `Referenced By` fields are `none_found`; these need follow-up during M43.3+ review.
- Validation contract contains one phrase conflict (`safe to delete` required in one check and forbidden in another), tracked as procedural gap.

## Final Status
M43_2_REPORT_ARCHIVE_PLAN_COMPLETE_WITH_GAPS

## Allowed Status Set
- M43_2_REPORT_ARCHIVE_PLAN_COMPLETE
- M43_2_REPORT_ARCHIVE_PLAN_COMPLETE_WITH_GAPS
- M43_2_INCOMPLETE
- M43_2_BLOCKED
