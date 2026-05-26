# Task Validation Decision Semantics

## 1. Purpose
Определить контрактные правила сопоставления условий валидации к допустимым результатам M63.

## 2. M63 Position in the Roadmap
M63 формализует контрактный слой после M62 MVP и не создаёт production authority.

## 3. Dependency on Package and Result Schemas
Зависимости:
- `schemas/task-validation-package.schema.json`
- `schemas/task-validation-result.schema.json`

## 4. Decision Semantics Scope
Документ задаёт mapping на контрактном уровне.
Он не задаёт полный evidence model и не задаёт production acceptance.

## 5. Allowed Top-Level Result Values
Разрешены только:
- `TASK_VALIDATION_PASS`
- `TASK_VALIDATION_PASS_WITH_WARNINGS`
- `TASK_VALIDATION_BLOCKED`
- `TASK_VALIDATION_NOT_ENOUGH_EVIDENCE`

M63 reuses the M62 task validation result vocabulary.
M63 formalizes contract-level decision semantics.
M63 does not create production task acceptance authority.

## 6. Decision Priority Order
1. TASK_VALIDATION_BLOCKED
2. TASK_VALIDATION_NOT_ENOUGH_EVIDENCE
3. TASK_VALIDATION_PASS_WITH_WARNINGS
4. TASK_VALIDATION_PASS

A blocker overrides all other outcomes.
TASK_VALIDATION_NOT_ENOUGH_EVIDENCE applies only when no blocker exists.
TASK_VALIDATION_PASS_WITH_WARNINGS applies only when no blocker and no not-enough-evidence condition exists.
TASK_VALIDATION_PASS applies only when no blocker, no not-enough-evidence condition, and no warning exists.

## 7. Blocking Conditions
Следующие условия дают `TASK_VALIDATION_BLOCKED`:
- package JSON missing/malformed;
- result JSON missing/malformed;
- required package/result field missing;
- unsupported package_type/result_type/contract_version;
- unknown top-level result value;
- unknown subresult value;
- human_review_required is false/missing;
- non_authority_boundary missing/empty;
- approval claim present;
- human review bypass claim present;
- merge/push/release authorization claim present;
- lifecycle mutation claim present;
- package task_id and result task_id mismatch;
- package attempts to include M64 full evidence model;
- package attempts to include M65 acceptance criteria checker semantics;
- result claims task approval/completion/production gate readiness.

Blocking conditions must not be downgraded to warnings.

## 8. Not-Enough-Evidence Conditions
При отсутствии блокеров, `TASK_VALIDATION_NOT_ENOUGH_EVIDENCE` применяется, если:
- agent_evidence_ref слишком расплывчат;
- validation_claims_ref не даёт понятной ссылки;
- diff_reference присутствует, но неинтерпретируем на контрактном уровне;
- declared_scope/declared_forbidden_changes структурно есть, но слишком расплывчаты;
- expected_artifacts есть, но структурно не коррелируют;
- subresult = NOT_ENOUGH_EVIDENCE и блокеров нет;
- ссылки есть, но слабая корреляция.

TASK_VALIDATION_NOT_ENOUGH_EVIDENCE is not approval.
TASK_VALIDATION_NOT_ENOUGH_EVIDENCE requires human review.
TASK_VALIDATION_NOT_ENOUGH_EVIDENCE must not be treated as PASS.

## 9. Warning Conditions
При отсутствии блокеров и not-enough-evidence, `TASK_VALIDATION_PASS_WITH_WARNINGS` может применяться, если:
- optional field/reference missing;
- known limitation declared;
- validation claims present but not independently verified;
- subresult PASS_WITH_WARNINGS;
- optional subcheck NOT_RUN and explicitly visible;
- minor ambiguity with valid required fields;
- deferred M64-M67 responsibility declared.

Warnings must remain visible.
Warnings must not be silently converted into TASK_VALIDATION_PASS.
PASS_WITH_WARNINGS is not approval.
Human review remains required.

## 10. PASS Conditions
`TASK_VALIDATION_PASS` возможен только если:
- package/result JSON существуют и парсятся;
- обязательные поля существуют;
- package_type/result_type поддерживаются;
- contract_version поддерживается;
- task_id package/result совпадают;
- top-level/subresult values разрешены;
- human_review_required = true;
- non_authority_boundary присутствует;
- нет approval/lifecycle/merge/push/release claims;
- нет blocker/noe/warning условий.

TASK_VALIDATION_PASS is not approval.
TASK_VALIDATION_PASS does not complete the task.
TASK_VALIDATION_PASS does not replace human review.
TASK_VALIDATION_PASS does not authorize merge, push, or release.

## 11. Schema Failure Mapping
- package schema validation failure -> TASK_VALIDATION_BLOCKED
- result schema validation failure -> TASK_VALIDATION_BLOCKED
- missing required field -> TASK_VALIDATION_BLOCKED
- unknown required enum value -> TASK_VALIDATION_BLOCKED
- human_review_required false by schema -> TASK_VALIDATION_BLOCKED
- non_authority_boundary missing by schema -> TASK_VALIDATION_BLOCKED

Schema PASS is not task approval.
Schema PASS does not prove task completion.

## 12. Malformed Package and Result Mapping
- missing package file -> TASK_VALIDATION_BLOCKED
- malformed package JSON -> TASK_VALIDATION_BLOCKED
- missing result file -> TASK_VALIDATION_BLOCKED
- malformed result JSON -> TASK_VALIDATION_BLOCKED
- unreadable package/result file -> TASK_VALIDATION_BLOCKED

Internal validator error behavior реализуется в 63.6.

## 13. Missing Field Mapping
- missing required package field -> TASK_VALIDATION_BLOCKED
- missing required result field -> TASK_VALIDATION_BLOCKED
- missing optional field -> warning if no blocker
- missing required reference field -> TASK_VALIDATION_BLOCKED

Required fields are defined by schemas.

## 14. Unsupported Version Mapping
- unsupported contract_version -> TASK_VALIDATION_BLOCKED
- missing contract_version -> TASK_VALIDATION_BLOCKED
- unknown package_type -> TASK_VALIDATION_BLOCKED
- unknown result_type -> TASK_VALIDATION_BLOCKED

M63 fails closed on unsupported versions.

## 15. Unknown Result Value Mapping
- unknown top-level result value -> TASK_VALIDATION_BLOCKED
- unknown subresult value -> TASK_VALIDATION_BLOCKED
- NOT_RUN top-level result -> TASK_VALIDATION_BLOCKED
- NOT_RUN subresult -> warning or blocker depending on requiredness

UNKNOWN must not be treated as PASS.
NOT_RUN must not be treated as PASS.

## 16. Human Review Boundary Mapping
- human_review_required: true -> invariant preserved
- human_review_required: false -> TASK_VALIDATION_BLOCKED
- human_review_required missing -> TASK_VALIDATION_BLOCKED
- claim "human review not required" -> TASK_VALIDATION_BLOCKED
- claim "human review can be skipped" -> TASK_VALIDATION_BLOCKED

Human review boundary is a contract invariant.

## 17. Non-Authority Boundary Mapping
- non_authority_boundary present and non-empty -> invariant present
- non_authority_boundary missing -> TASK_VALIDATION_BLOCKED
- non_authority_boundary empty -> TASK_VALIDATION_BLOCKED
- approval claim contradicting boundary -> TASK_VALIDATION_BLOCKED
- merge/push/release claim contradicting boundary -> TASK_VALIDATION_BLOCKED

The non-authority boundary is required evidence of safe interpretation.
The non-authority boundary does not approve the task.

## 18. Subresult Mapping
Allowed subresult values:
- PASS
- PASS_WITH_WARNINGS
- BLOCKED
- NOT_ENOUGH_EVIDENCE
- NOT_RUN

Mapping:
- any required subresult BLOCKED -> TASK_VALIDATION_BLOCKED
- any required subresult NOT_ENOUGH_EVIDENCE with no blockers -> TASK_VALIDATION_NOT_ENOUGH_EVIDENCE
- any required subresult NOT_RUN -> TASK_VALIDATION_BLOCKED
- any optional subresult NOT_RUN -> TASK_VALIDATION_PASS_WITH_WARNINGS if no blocker exists
- any subresult PASS_WITH_WARNINGS with no blockers/noe -> TASK_VALIDATION_PASS_WITH_WARNINGS
- all required subresults PASS and no warnings/blockers -> TASK_VALIDATION_PASS

Required subresults in M63:
- schema_result
- scope_result
- evidence_ref_result
- validation_claims_result

## 19. Relation to M64-M67
M64 defines the full task output evidence model.
M65 defines the acceptance criteria checker.
M66 defines the unified agent task validation runner.
M67 defines false PASS resistance and completion gate integration.
M63 decision semantics must not absorb M64-M67 responsibilities.

## 20. What This Document Does Not Define
Не определяет:
- full task output evidence model
- acceptance criteria checking
- full git diff correctness
- unified runner behavior
- false PASS resistance suite
- completion gate integration
- human approval procedure
- merge/release readiness
- production task acceptance

## 21. Non-Authority Boundary
M63 contract decision semantics are not approval.
M63 contract decision semantics do not replace human review.
M63 contract decision semantics do not complete the task.
M63 contract decision semantics do not validate completed agent tasks as a production gate.
M63 contract decision semantics do not define the full task output evidence model.
M63 contract decision semantics do not define acceptance criteria checking.
M63 contract decision semantics do not authorize merge, push, or release.
M63 contract decision semantics do not start M64.
Human review remains required.

## 22. Final Status
FINAL_STATUS: M63_CONTRACT_DECISION_SEMANTICS_DEFINED
