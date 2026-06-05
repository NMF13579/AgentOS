# Acceptance Criteria Checker

## 1. Purpose
This document describes the M65 read-only checker.

## 2. Scope
65.5 implements the checker.
65.5 does not create fixtures.
65.5 does not create integration summary.
65.5 does not create action review.
65.5 does not create evidence report.
65.5 does not complete M65.

## 3. Architecture Boundary
M65 checker must not infer full task meaning from free-form Markdown.
M65 checker must operate on structured acceptance criteria package.

## 4. CLI
```bash
python3 scripts/check-acceptance-criteria.py \
  --package <acceptance-criteria-check-package-json> \
  --json
```
Optional:
```bash
--strict
```

## 5. Inputs
The checker reads one acceptance criteria check package JSON.

## 6. Outputs
When `--json` is passed, the checker prints deterministic JSON with:
- `result`
- package identity fields
- criteria summary
- per-criterion states
- blockers / warnings / not-enough-evidence findings
- forbidden fields and forbidden claims findings
- final decision reason
- exit code

## 7. Result Values
- `M65_ACCEPTANCE_CHECK_PASS`
- `M65_ACCEPTANCE_CHECK_PASS_WITH_WARNINGS`
- `M65_ACCEPTANCE_CHECK_BLOCKED`
- `M65_ACCEPTANCE_CHECK_NOT_ENOUGH_EVIDENCE`

## 8. Exit Codes
- exit 0 — `M65_ACCEPTANCE_CHECK_PASS`
- exit 0 — `M65_ACCEPTANCE_CHECK_PASS_WITH_WARNINGS`
- exit 1 — `M65_ACCEPTANCE_CHECK_BLOCKED`
- exit 1 — `M65_ACCEPTANCE_CHECK_NOT_ENOUGH_EVIDENCE`
- exit 2 — CLI misuse / internal checker error

M65_ACCEPTANCE_CHECK_NOT_ENOUGH_EVIDENCE maps to exit 1 because automated evaluation is inconclusive and must not allow the pipeline to proceed without human review.
This is a conservative fail-closed mapping, not a claim that the task failed.

## 9. Check Methods
- `artifact_presence`
- `validation_output`
- `declared_change`
- `manual_review_required`

## 10. Required Criteria Handling
Required criterion that cannot be checked must map to M65_ACCEPTANCE_CHECK_BLOCKED, not M65_ACCEPTANCE_CHECK_NOT_ENOUGH_EVIDENCE.

Also blocked:
- required criterion failed
- required artifact missing
- required validation failed or unavailable
- required malformed criterion
- required unsupported check_method
- required `manual_review_required` criterion

## 11. Optional Criteria Handling
Optional criteria can produce:
- warning-level outcomes (`M65_ACCEPTANCE_CHECK_PASS_WITH_WARNINGS`)
- not-enough-evidence outcomes (`M65_ACCEPTANCE_CHECK_NOT_ENOUGH_EVIDENCE`)

Optional criteria never override failed required criteria.

## 12. Manual Review Criteria
If all criteria in the package have check_method: manual_review_required and at least one criterion is required, the checker must return M65_ACCEPTANCE_CHECK_BLOCKED.

## 13. Forbidden Claims
The checker blocks operative forbidden claims and forbidden operative field names related to:
- approval
- completion
- human review bypass
- merge/push/release authorization
- production readiness
- completion gate pass
- automatic M66/M67 start

## 14. Human Review Boundary
Human review remains required.
M65 checker result is not approval.
M65 checker result does not complete the task.

## 15. Limitations
The checker performs deterministic structured validation.
The checker does not understand full task meaning.
The checker does not semantically analyze free-form Markdown.
The checker does not prove business correctness.
The checker does not replace human review.

## 16. Relationship to Later Tasks
65.6 creates fixtures for the checker.
65.7 validates integration.
65.8 reviews actions.
65.9 collects evidence.
65.10 closes M65.

## 17. Final Status
FINAL_STATUS: M65_ACCEPTANCE_CHECKER_DEFINED_WITH_WARNINGS
