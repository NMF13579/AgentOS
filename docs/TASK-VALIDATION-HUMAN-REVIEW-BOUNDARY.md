# Task Validation Human Review Boundary

## 1. Purpose
Зафиксировать обязательную границу human review для всех результатов task validation в M63.

## 2. M63 Position in the Roadmap
M63 формализует контракт, но не выдаёт approval и не заменяет ручной обзор.

## 3. Dependency on Decision Semantics
Зависимость: `docs/TASK-VALIDATION-DECISION-SEMANTICS.md`.

## 4. Boundary Scope
Граница описывает, что можно и что нельзя интерпретировать из результатов валидации.

## 5. Human Review Invariant
- `human_review_required` must always be true.
- `human_review_required` must never be false.
- Human review cannot be disabled by package, result, evidence, validator, runner, report, completion review, or agent claim.
- Human review remains required.

Это инвариант контракта, не предупреждение.

Попытки заявить:
- `human_review_required: false`
- `human review not required`
- `human review can be skipped`
- `no human review needed`
- `automatic approval`

должны трактоваться как `TASK_VALIDATION_BLOCKED`.

## 6. Non-Approval Rules
TASK_VALIDATION_PASS is not approval.
TASK_VALIDATION_PASS does not complete the task.
TASK_VALIDATION_PASS does not replace human review.
TASK_VALIDATION_PASS does not authorize merge, push, or release.
TASK_VALIDATION_PASS_WITH_WARNINGS is not approval.
TASK_VALIDATION_PASS_WITH_WARNINGS does not complete the task.
TASK_VALIDATION_PASS_WITH_WARNINGS does not replace human review.
TASK_VALIDATION_NOT_ENOUGH_EVIDENCE is not approval.
TASK_VALIDATION_NOT_ENOUGH_EVIDENCE requires human review.
TASK_VALIDATION_BLOCKED is not approval.
Human review remains required.

## 7. Result-Specific Boundary Rules
`TASK_VALIDATION_PASS` означает только отсутствие контрактных blocker/noe/warning в границе M63.
Не означает approval/completion/merge/release/skip review/production acceptance.

`TASK_VALIDATION_PASS_WITH_WARNINGS` означает отсутствие блокера при наличии видимых предупреждений.
Не означает clean approval или human review bypass.

`TASK_VALIDATION_NOT_ENOUGH_EVIDENCE` означает недостаточность ссылочных данных при отсутствии блокера.
Не означает pass/approval/completion.

`TASK_VALIDATION_BLOCKED` означает блокирующее условие для безопасной проверки.
Не означает автоматический lifecycle mutation или окончательный отказ человеком.

## 8. Forbidden Claims
Запрещённые affirm claims:
- approved
- approval granted
- task approved
- task is approved
- task completion approved
- complete without review
- human review not required
- human_review_required: false
- human review can be skipped
- merged
- released
- pushed
- deployment authorized
- merge authorized
- push authorized
- release authorized
- lifecycle mutated
- completion gate passed
- production task acceptance gate passed
- M64 started automatically

Такие фразы допустимы только как forbidden examples, quoted policy examples или explicit non-authority boundary text.
Affirmative claims должны блокировать validation.
Ambiguous claims не могут считаться clean PASS.

## 9. Required Boundary Statements
Обязательные statements интерпретации:
- TASK_VALIDATION_PASS is not approval.
- TASK_VALIDATION_PASS does not complete the task.
- TASK_VALIDATION_PASS does not replace human review.
- TASK_VALIDATION_PASS does not authorize merge, push, or release.
- Human review remains required.

Это требования интерпретации, а не approval.

## 10. Package and Result Contract Requirements
Package requirement:
- package must require `human_review_required: true`
- package must not allow `human_review_required: false`
- package must not claim approval/merge/push/release/lifecycle mutation

Result requirement:
- result must require `human_review_required: true`
- result must include `non_authority_boundary`
- result must not claim approval/merge/push/release/lifecycle mutation

63.5 документирует требования.
63.5 must not modify package schema.
63.5 must not modify result schema.
63.6 validator will check contract compliance.

## 11. Validator Responsibility in 63.6
Будущий validator должен проверять:
- `human_review_required` is true
- `human_review_required` is not false
- `non_authority_boundary` exists
- `non_authority_boundary` is not empty
- required boundary statements are present
- forbidden approval claims are absent
- merge/push/release claims are absent
- lifecycle mutation claims are absent

63.5 defines boundary contract.
63.6 implements validator checks.
63.5 must not create or modify `scripts/check-task-validation-contract.py`.

## 12. Relation to M64-M67
M64 defines the full task output evidence model.
M65 defines the acceptance criteria checker.
M66 defines the unified agent task validation runner.
M67 defines false PASS resistance and completion gate integration.
M63 human review boundary must not absorb M64-M67 responsibilities.

## 13. What This Document Does Not Define
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

## 14. Non-Authority Boundary
M63 human review boundary contract is not approval.
M63 human review boundary contract does not replace human review.
M63 human review boundary contract does not complete the task.
M63 human review boundary contract does not validate completed agent tasks as a production gate.
M63 human review boundary contract does not define the full task output evidence model.
M63 human review boundary contract does not define acceptance criteria checking.
M63 human review boundary contract does not create the validator.
M63 human review boundary contract does not authorize merge, push, or release.
M63 human review boundary contract does not start M64.
Human review remains required.

## 15. Final Status
FINAL_STATUS: M63_HUMAN_REVIEW_BOUNDARY_CONTRACT_DEFINED
