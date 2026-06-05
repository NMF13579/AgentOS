# Task Validation Result Contract

## 1. Purpose
Определить структуру task validation result для M63.

## 2. M63 Position in the Roadmap
M63 формализует контрактный слой после M62 MVP.

## 3. Dependency on Package Schema
Зависимость: `schemas/task-validation-package.schema.json`.

## 4. Result Contract Scope
63.3 задаёт структуру результата и допустимые значения.
63.3 не задаёт детальную логику принятия решений.

## 5. Required Result Fields
Обязательные поля:
- `contract_version`
- `result_type`
- `task_id`
- `result`
- `package_valid`
- `schema_result`
- `scope_result`
- `evidence_ref_result`
- `validation_claims_result`
- `human_review_required`
- `warnings`
- `blockers`
- `non_authority_boundary`

## 6. Allowed Result Values
Разрешены только:
- `TASK_VALIDATION_PASS`
- `TASK_VALIDATION_PASS_WITH_WARNINGS`
- `TASK_VALIDATION_BLOCKED`
- `TASK_VALIDATION_NOT_ENOUGH_EVIDENCE`

## 7. Subresult Fields
Подрезультаты:
- `schema_result`
- `scope_result`
- `evidence_ref_result`
- `validation_claims_result`

Разрешены значения:
- `PASS`
- `PASS_WITH_WARNINGS`
- `BLOCKED`
- `NOT_ENOUGH_EVIDENCE`
- `NOT_RUN`

## 8. Field Semantics
`contract_version` — версия контракта результата.

`result_type` — должен быть `task_validation_result`.

`task_id` — идентификатор задачи.

`result` — верхнеуровневый результат.

`package_valid` — структурный флаг валидности package.
`package_valid: true` не является approval и не означает завершение задачи.

`schema_result`, `scope_result`, `evidence_ref_result`, `validation_claims_result` — структурные подрезультаты M63-уровня.
`evidence_ref_result` does not validate full M64 evidence content.
`validation_claims_result` does not prove validation commands were correctly run.

`human_review_required` — обязательно `true`.

`warnings` — массив предупреждений.

`blockers` — массив блокеров.

`non_authority_boundary` — массив non-authority утверждений.

## 9. Non-Authority Boundary Field
`non_authority_boundary` обязателен как массив.
Требуемые фразы интерпретации:
- TASK_VALIDATION_PASS is not approval.
- TASK_VALIDATION_PASS does not complete the task.
- TASK_VALIDATION_PASS does not replace human review.
- TASK_VALIDATION_PASS does not authorize merge, push, or release.
- Human review remains required.

JSON Schema не гарантирует полное смысловое соблюдение этих правил без валидатора.

## 10. Warning and Blocker Visibility
Warnings must be visible.
Warnings must not be silently converted into TASK_VALIDATION_PASS.
Blockers must be visible.
Blockers must not be downgraded to warnings without explicit decision semantics.
NOT_RUN must not be treated as PASS.
Detailed mapping belongs to 63.4.

## 11. Relation to Task Validation Package Schema
63.2 defines the task validation package schema.
63.3 defines the task validation result schema.
63.3 must not modify the package schema.
`task_id` в результате должен соответствовать `task_id` в пакете.
63.6 validator will check package/result correlation.

## 12. Relation to Decision Semantics
63.3 defines result structure and allowed values.
63.4 defines contract decision semantics.
63.3 must not define detailed decision priority or full mapping rules.

## 13. Relation to M64-M67
M64 defines the full task output evidence model.
M65 defines the acceptance criteria checker.
M66 defines the unified agent task validation runner.
M67 defines false PASS resistance and completion gate integration.
M63 result schema must not absorb M64-M67 responsibilities.

## 14. What This Schema Validates
Схема валидирует структуру, типы, обязательные поля, перечисления, границы `human_review_required` и форму массивов.

## 15. What This Schema Does Not Validate
Схема не валидирует полный контент evidence, полный diff-анализ, критерии приёмки, approval, merge/release readiness, production acceptance.

## 16. Human Review Requirement
human_review_required: true
The task validation result must not disable human review.
A result that attempts to set human_review_required to false is outside the safe M63 contract boundary.
Human review remains required.

## 17. Non-Authority Boundary
M63 task validation result schema is not approval.
M63 task validation result schema does not replace human review.
M63 task validation result schema does not complete the task.
M63 task validation result schema does not validate completed agent tasks as a production gate.
M63 task validation result schema does not define the full task output evidence model.
M63 task validation result schema does not define acceptance criteria checking.
M63 task validation result schema does not authorize merge, push, or release.
M63 task validation result schema does not start M64.
Human review remains required.

## 18. Final Status
FINAL_STATUS: M63_TASK_VALIDATION_RESULT_SCHEMA_DEFINED
