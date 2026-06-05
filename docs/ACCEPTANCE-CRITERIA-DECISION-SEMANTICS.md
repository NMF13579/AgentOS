# Acceptance Criteria Decision Semantics

## 1. Purpose
This document defines decision semantics for the M65 Acceptance Criteria Checker.
M65 evaluates structured acceptance criteria against structured evidence and package fields.
M65 result is a validation signal.
M65 result is not approval.
M65 result is not task completion.
Human review remains required.

## 2. Scope
65.3 defines:
1. result values
2. criterion-level states
3. overall priority order
4. required versus optional criterion handling
5. manual-review-only handling
6. not-enough-evidence handling
7. warning handling
8. blocker handling
9. exit-code meaning for future checker

65.3 does not:
1. implement the checker
2. create fixtures
3. define full claim-boundary scanning
4. integrate completion gate
5. create unified runner
6. start M66
7. start M67

## 3. Architecture Boundary
M65 checker must not infer full task meaning from free-form Markdown.
M65 checker must operate on structured acceptance criteria package.

1. The checker must evaluate structured package fields.
2. The checker must not pretend to understand the whole task from `task_brief_path`.
3. The checker may reference `task_brief_path` only as a declared artifact reference.
4. Ambiguous criteria must not become fake PASS.
5. Agent self-claims must not be treated as authority.

## 4. Overall Result Values
- `M65_ACCEPTANCE_CHECK_PASS`
- `M65_ACCEPTANCE_CHECK_PASS_WITH_WARNINGS`
- `M65_ACCEPTANCE_CHECK_BLOCKED`
- `M65_ACCEPTANCE_CHECK_NOT_ENOUGH_EVIDENCE`

`M65_ACCEPTANCE_CHECK_PASS`:
Use only when all required criteria are structurally checkable, all required criteria appear satisfied, all required artifacts are present or represented, required validation outputs pass or are acceptable, human_review_required is true, no forbidden approval/completion claims are present, no blockers exist, and no warnings prevent clean PASS.

`M65_ACCEPTANCE_CHECK_PASS_WITH_WARNINGS`:
Use when all required criteria appear satisfied, but warning-level issues exist, such as optional criteria not checked, ambiguous supporting evidence that does not affect required criteria, extra non-required artifacts, validation outputs present but not correlated to optional criteria, or optional manual-review-required criteria.

`M65_ACCEPTANCE_CHECK_BLOCKED`:
Use when required task validation cannot safely proceed or required criteria are failed, missing, uncheckable, or dependent entirely on manual review. Also use when required artifacts are missing, required validation failed, human_review_required is false, forbidden approval/completion claims are present, package structure is invalid, or forbidden scope expansion is detected.

`M65_ACCEPTANCE_CHECK_NOT_ENOUGH_EVIDENCE`:
Use only when the package lacks enough structured evidence to evaluate optional, ambiguous, or non-required criteria without falsely blocking required task completion. This status is conservative and inconclusive. It is not a claim that the task failed.

## 5. Priority Order
1. `M65_ACCEPTANCE_CHECK_BLOCKED`
2. `M65_ACCEPTANCE_CHECK_NOT_ENOUGH_EVIDENCE`
3. `M65_ACCEPTANCE_CHECK_PASS_WITH_WARNINGS`
4. `M65_ACCEPTANCE_CHECK_PASS`

If any BLOCKED condition exists, the final result must be M65_ACCEPTANCE_CHECK_BLOCKED.
If no BLOCKED condition exists but NOT_ENOUGH_EVIDENCE conditions exist, the final result must be M65_ACCEPTANCE_CHECK_NOT_ENOUGH_EVIDENCE.
If no BLOCKED or NOT_ENOUGH_EVIDENCE condition exists but warnings exist, the final result must be M65_ACCEPTANCE_CHECK_PASS_WITH_WARNINGS.
Only if no blockers, no not-enough-evidence conditions, and no warnings exist may the final result be M65_ACCEPTANCE_CHECK_PASS.

## 6. Criterion-Level States
- `SATISFIED`
- `SATISFIED_WITH_WARNINGS`
- `NOT_SATISFIED`
- `NOT_ENOUGH_EVIDENCE`
- `NOT_EVALUABLE`
- `BLOCKED`

`SATISFIED`: Criterion has a supported check_method, expected evidence is represented, and package data supports satisfaction.

`SATISFIED_WITH_WARNINGS`: Criterion appears satisfied but has non-blocking ambiguity, weak correlation, extra evidence, or advisory concerns.

`NOT_SATISFIED`: Criterion is checkable and package data shows the requirement was not met.

`NOT_ENOUGH_EVIDENCE`: Criterion is optional, ambiguous, or non-required and package data is insufficient to evaluate it without blocking required task completion.

`NOT_EVALUABLE`: Criterion cannot be evaluated automatically with the provided structured package fields.

`BLOCKED`: Criterion is required and failed, missing, malformed, uncheckable, unsupported, dependent entirely on manual review, or lacks required supporting evidence.

## 7. Required Criteria Semantics
1. Required criterion failed must produce M65_ACCEPTANCE_CHECK_BLOCKED.
2. Required artifact missing must produce M65_ACCEPTANCE_CHECK_BLOCKED.
3. Required validation failed must produce M65_ACCEPTANCE_CHECK_BLOCKED.
4. Required criterion cannot be checked must produce M65_ACCEPTANCE_CHECK_BLOCKED.
5. Required criterion with unsupported check_method must produce M65_ACCEPTANCE_CHECK_BLOCKED.
6. Required criterion with missing expected_evidence when the check method needs evidence must produce M65_ACCEPTANCE_CHECK_BLOCKED.
7. Required criterion that depends entirely on manual review must produce M65_ACCEPTANCE_CHECK_BLOCKED.
8. Required criterion that is only supported by an agent self-claim must not produce PASS.

Required criterion that cannot be checked must map to M65_ACCEPTANCE_CHECK_BLOCKED, not M65_ACCEPTANCE_CHECK_NOT_ENOUGH_EVIDENCE.

## 8. Optional Criteria Semantics
1. Optional criterion satisfied may contribute to PASS if no warnings or blockers exist.
2. Optional criterion satisfied with ambiguity may contribute to PASS_WITH_WARNINGS.
3. Optional criterion not checked may contribute to PASS_WITH_WARNINGS or NOT_ENOUGH_EVIDENCE.
4. Optional criterion uncheckable may produce M65_ACCEPTANCE_CHECK_NOT_ENOUGH_EVIDENCE if the package lacks enough structured evidence to evaluate it.
5. Optional manual-review-required criterion may produce PASS_WITH_WARNINGS if all required criteria are otherwise satisfied.
6. Optional criteria must not override failed required criteria.
7. Optional criteria must not create clean PASS when warnings remain.

## 9. Manual-Review-Only Criteria Semantics
1. manual_review_required is a valid check_method.
2. manual_review_required criteria cannot produce clean automated PASS by structure alone.
3. Required manual_review_required criterion must produce M65_ACCEPTANCE_CHECK_BLOCKED unless the package explicitly defines that the criterion is non-required or advisory.
4. Optional manual_review_required criterion may produce M65_ACCEPTANCE_CHECK_PASS_WITH_WARNINGS if all required criteria are otherwise satisfied.
5. Automated acceptance is insufficient when satisfaction requires human judgment.
6. If all criteria in the package have check_method: manual_review_required and at least one criterion is required, the checker must return M65_ACCEPTANCE_CHECK_BLOCKED.

If all criteria in the package have check_method: manual_review_required and at least one criterion is required, the checker must return M65_ACCEPTANCE_CHECK_BLOCKED.
A package where all criteria require manual review is a valid input structure, but it cannot produce automated PASS or PASS_WITH_WARNINGS when required criteria depend entirely on manual review.

## 10. NOT_ENOUGH_EVIDENCE Semantics
M65_ACCEPTANCE_CHECK_NOT_ENOUGH_EVIDENCE is reserved for cases where the package lacks enough structured evidence to evaluate optional, ambiguous, or non-required criteria without falsely blocking required task completion.

M65_ACCEPTANCE_CHECK_NOT_ENOUGH_EVIDENCE must not be used for required criteria that cannot be checked.
M65_ACCEPTANCE_CHECK_NOT_ENOUGH_EVIDENCE must not allow pipeline continuation as if PASS occurred.
M65_ACCEPTANCE_CHECK_NOT_ENOUGH_EVIDENCE is conservative and inconclusive.
M65_ACCEPTANCE_CHECK_NOT_ENOUGH_EVIDENCE is not approval.
M65_ACCEPTANCE_CHECK_NOT_ENOUGH_EVIDENCE is not task failure.
Human review remains required.

## 11. Warning Semantics
Warning conditions include:
1. optional criterion not checked
2. ambiguous supporting evidence for optional criterion
3. extra artifact not required
4. validation output present but not correlated to optional criterion
5. optional manual-review-required criterion
6. M64 evidence result PASS_WITH_WARNINGS when required criteria are still satisfied
7. known limitations that do not block required criteria
8. advisory warnings carried from prior M65 tasks

Warnings prevent clean PASS.
Warnings may produce M65_ACCEPTANCE_CHECK_PASS_WITH_WARNINGS only if no blockers or not-enough-evidence conditions exist.

## 12. Blocker Semantics
Blocker conditions include:
1. package invalid
2. required top-level field missing
3. wrong field type
4. empty acceptance_criteria
5. human_review_required false
6. required criterion missing
7. required criterion malformed
8. required criterion failed
9. required criterion uncheckable
10. required artifact missing
11. required validation failed
12. required manual-review-only criterion
13. forbidden approval or completion claim
14. protected prior-layer artifact modified
15. forbidden M66/M67 artifact found
16. checker scope expansion
17. unsupported check_method on required criterion

Any blocker condition must produce M65_ACCEPTANCE_CHECK_BLOCKED.

## 13. Evidence Result Semantics
1. M64_EVIDENCE_CHECK_PASS can support M65 evaluation but does not guarantee acceptance criteria satisfaction.
2. M64_EVIDENCE_CHECK_PASS_WITH_WARNINGS can support M65 evaluation but should usually contribute warning-level findings unless the warning affects required criteria.
3. M64_EVIDENCE_CHECK_BLOCKED must produce M65_ACCEPTANCE_CHECK_BLOCKED.
4. M64_EVIDENCE_CHECK_NOT_ENOUGH_EVIDENCE should produce M65_ACCEPTANCE_CHECK_NOT_ENOUGH_EVIDENCE or BLOCKED depending on whether required criteria depend on the missing evidence.
5. UNKNOWN evidence result must not produce clean PASS.

Evidence result is not authority that acceptance criteria are satisfied.
Agent evidence remains claim-bound.
M65 must compare structured evidence and package fields against structured criteria.

## 14. Artifact Semantics
1. artifact_presence checks expected_artifacts against actual_artifacts and/or changed_files.
2. Required expected artifact missing from actual_artifacts and changed_files must produce BLOCKED.
3. Optional expected artifact missing may produce PASS_WITH_WARNINGS or NOT_ENOUGH_EVIDENCE.
4. Extra actual artifact not required should produce warning unless it violates scope.
5. Scope-violating artifact must produce BLOCKED.

## 15. Validation Output Semantics
1. validation_output checks criteria against validation_outputs.
2. Required validation result FAIL must produce BLOCKED.
3. Required validation result BLOCKED must produce BLOCKED.
4. Required validation result NOT_RUN must produce BLOCKED if required criteria depend on it.
5. Required validation result UNKNOWN must produce BLOCKED or NOT_ENOUGH_EVIDENCE only if the criterion is not required.
6. Optional validation output missing or UNKNOWN may produce PASS_WITH_WARNINGS or NOT_ENOUGH_EVIDENCE.
7. Validation output not correlated to any criterion should produce warning.

## 16. Declared Change Semantics
1. declared_change checks criteria against changed_files and actual_artifacts.
2. Required declared change missing must produce BLOCKED.
3. Optional declared change missing may produce warning or NOT_ENOUGH_EVIDENCE.
4. Changed file alone is not proof that criterion is satisfied unless it correlates with expected evidence.
5. Agent self-claim alone is not sufficient.

## 17. Forbidden Claim Semantics
Detailed forbidden claim boundary belongs to 65.4. Decision mapping requirement:

Forbidden approval, completion, merge, push, release, production-ready, completion-gate, M66 auto-start, or M67 auto-start claims must map to M65_ACCEPTANCE_CHECK_BLOCKED.

Acceptance criteria appear satisfied at M65 level.
This is not approval.
This does not complete the task.
Human review remains required.

## 18. Exit Code Semantics for Future Checker
- exit 0 — M65_ACCEPTANCE_CHECK_PASS
- exit 0 — M65_ACCEPTANCE_CHECK_PASS_WITH_WARNINGS
- exit 1 — M65_ACCEPTANCE_CHECK_BLOCKED or M65_ACCEPTANCE_CHECK_NOT_ENOUGH_EVIDENCE
- exit 2 — CLI misuse / internal checker error

M65_ACCEPTANCE_CHECK_NOT_ENOUGH_EVIDENCE maps to exit 1 because automated evaluation is inconclusive and must not allow the pipeline to proceed without human review.
This is a conservative fail-closed mapping, not a claim that the task failed.

## 19. Decision Examples
1. All required criteria satisfied, no warnings: Final result: M65_ACCEPTANCE_CHECK_PASS.
2. Required criteria satisfied, optional criterion not checked: Final result: M65_ACCEPTANCE_CHECK_PASS_WITH_WARNINGS.
3. Required artifact missing: Final result: M65_ACCEPTANCE_CHECK_BLOCKED.
4. Required validation failed: Final result: M65_ACCEPTANCE_CHECK_BLOCKED.
5. Required criterion cannot be checked: Final result: M65_ACCEPTANCE_CHECK_BLOCKED.
6. Optional criterion lacks enough evidence: Final result: M65_ACCEPTANCE_CHECK_NOT_ENOUGH_EVIDENCE or M65_ACCEPTANCE_CHECK_PASS_WITH_WARNINGS depending on severity and package completeness.
7. Required manual-review-only criterion: Final result: M65_ACCEPTANCE_CHECK_BLOCKED.
8. All criteria manual-review-required and at least one required: Final result: M65_ACCEPTANCE_CHECK_BLOCKED.
9. Forbidden production-ready claim present: Final result: M65_ACCEPTANCE_CHECK_BLOCKED.
10. M64 evidence result UNKNOWN with required criteria depending on it: Final result: M65_ACCEPTANCE_CHECK_BLOCKED.

## 20. Relationship to Later Tasks
65.4 defines the acceptance criteria claim boundary.
65.5 implements the read-only checker.
65.6 creates fixtures for these semantics.
65.7 validates integration.
65.8 reviews actions.
65.9 collects evidence.
65.10 closes M65.

## 21. Final Status
FINAL_STATUS: M65_ACCEPTANCE_DECISION_SEMANTICS_DEFINED_WITH_WARNINGS
