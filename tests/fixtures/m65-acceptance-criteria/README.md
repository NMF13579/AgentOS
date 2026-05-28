# M65 Acceptance Criteria Fixtures

## 1. Purpose
These fixtures validate the M65 acceptance criteria checker.

## 2. Scope
65.6 creates fixtures only.
65.6 does not modify checker.
65.6 does not create integration summary.
65.6 does not create action review.
65.6 does not create evidence report.
65.6 does not complete M65.

## 3. Architecture Boundary
M65 checker must not infer full task meaning from free-form Markdown.
M65 checker must operate on structured acceptance criteria package.
Human review remains required.

## 4. Fixture Categories
- `positive/` expects `M65_ACCEPTANCE_CHECK_PASS`
- `warning/` expects `M65_ACCEPTANCE_CHECK_PASS_WITH_WARNINGS`
- `not-enough/` expects `M65_ACCEPTANCE_CHECK_NOT_ENOUGH_EVIDENCE`
- `negative/` expects `M65_ACCEPTANCE_CHECK_BLOCKED`
- `malformed/` expects `M65_ACCEPTANCE_CHECK_BLOCKED`

## 5. Exit Code Expectations
- `positive/` expected exit code: `0`
- `warning/` expected exit code: `0`
- `not-enough/` expected exit code: `1`
- `negative/` expected exit code: `1`
- `malformed/` expected exit code: `1`

M65_ACCEPTANCE_CHECK_NOT_ENOUGH_EVIDENCE maps to exit 1 because automated evaluation is inconclusive and must not allow the pipeline to proceed without human review.
This is a conservative fail-closed mapping, not a claim that the task failed.

## 6. Fixture List
- `positive/valid-required-criteria-satisfied.json` -> PASS
- `positive/valid-multiple-required-criteria-satisfied.json` -> PASS
- `warning/optional-criterion-not-checked.json` -> PASS_WITH_WARNINGS
- `warning/ambiguous-supporting-evidence.json` -> PASS_WITH_WARNINGS
- `warning/extra-artifact-not-required.json` -> PASS_WITH_WARNINGS
- `warning/validation-output-present-but-not-correlated.json` -> PASS_WITH_WARNINGS
- `warning/manual-review-required-optional-criterion.json` -> PASS_WITH_WARNINGS
- `not-enough/not-enough-evidence.json` -> NOT_ENOUGH_EVIDENCE
- `not-enough/optional-criterion-uncheckable.json` -> NOT_ENOUGH_EVIDENCE
- `not-enough/ambiguous-criteria-package.json` -> NOT_ENOUGH_EVIDENCE
- `negative/no-acceptance-criteria.json` -> BLOCKED
- `negative/missing-required-criterion.json` -> BLOCKED
- `negative/required-artifact-missing.json` -> BLOCKED
- `negative/required-validation-failed.json` -> BLOCKED
- `negative/required-criterion-uncheckable.json` -> BLOCKED
- `negative/manual-review-required-required-criterion.json` -> BLOCKED
- `negative/human-review-disabled.json` -> BLOCKED
- `negative/approval-claim-present.json` -> BLOCKED
- `negative/production-ready-claim.json` -> BLOCKED
- `negative/completion-gate-passed-claim.json` -> BLOCKED
- `negative/wrong-required-field-type.json` -> BLOCKED
- `malformed/malformed-package-json.json` -> BLOCKED

## 7. Execution Instructions
Run checker with:

```bash
python3 scripts/check-acceptance-criteria.py --package <fixture-path> --json
```

## 8. Boundary Statement
Fixtures are not approval.
Fixtures do not complete M65.
Fixtures do not authorize M66 or M67.
Human review remains required.

## 9. Final Status
FINAL_STATUS: M65_ACCEPTANCE_FIXTURES_COMPLETE_WITH_WARNINGS
