## Task
M43.4 Docs / Spec Footprint Audit and Safe Consolidation Plan

## Preconditions
- M43.3 status found: `M43_3_FIXTURE_CONSOLIDATION_PLAN_COMPLETE_WITH_GAPS`
- Continuation allowed by precondition rules.

## Created Files
- `reports/m43-4-docs-footprint-inventory.md`
- `reports/m43-4-source-of-truth-preservation-map.md`
- `reports/m43-4-safe-docs-consolidation-plan.md`
- `reports/m43-4-completion-review.md`

## Coverage Summary
- Discovered docs: 164
- Listed inventory rows: 164
- Intentionally excluded docs: 0
- Each discovered doc has an inventory row.
- No docs were modified.

## Gaps
- Some docs remain `UNKNOWN_NEEDS_REVIEW`.
- Some references remain `none_found` and need M43.5+ follow-up.
- Concept `SQLite/cache as optional runtime cache` marked `not_found`.

## Final Status
M43_4_DOCS_CONSOLIDATION_PLAN_COMPLETE_WITH_GAPS

## Allowed Status Set
- M43_4_DOCS_CONSOLIDATION_PLAN_COMPLETE
- M43_4_DOCS_CONSOLIDATION_PLAN_COMPLETE_WITH_GAPS
- M43_4_INCOMPLETE
- M43_4_BLOCKED
