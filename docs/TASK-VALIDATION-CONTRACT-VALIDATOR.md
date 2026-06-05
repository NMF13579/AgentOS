# Task Validation Contract Validator

## 1. Purpose
Описать read-only валидатор M63 для проверки package/result контракта.

## 2. M63 Position in the Roadmap
M63 формализует контракт, но не создаёт production gate.

## 3. Validator Role
Валидатор проверяет структуру package/result, корреляцию task_id, human review invariant, non-authority boundary и запретные claims.

## 4. CLI
```bash
python3 scripts/check-task-validation-contract.py --package <file> --result <file> --json
python3 scripts/check-task-validation-contract.py --help
```

## 5. Strict Mode
`--strict` поддерживается и фиксируется в JSON как `"strict": true`.
В 63.6 strict не меняет mapping результатов.

## 6. Inputs
- package JSON
- result JSON

## 7. Package Checks
Проверяются required поля, types, `package_type`, `contract_version`, `human_review_required: true`.

## 8. Result Checks
Проверяются required поля, types, `result_type`, `contract_version`, top-level result enum и subresult enum.

## 9. Required Field Type Checks
Включены строгие type checks.
Boolean поля (`human_review_required`, `package_valid`) принимаются только как JSON boolean, не как `0/1`.

## 10. Package / Result Correlation
Проверяется `package.task_id == result.task_id`.

## 11. Human Review Boundary Checks
Проверяется `human_review_required: true` в package и result.
Попытки отключить human review блокируются.

## 12. Non-Authority Boundary Checks
Проверяется наличие `non_authority_boundary`, непустой массив строк и обязательные boundary statements.

## 13. Forbidden Claim Detection
Реализован рекурсивный просмотр строковых значений JSON.
Safe-context исключения:
- `declared_forbidden_changes`
- `declared_forbidden_changes.forbidden_claims`
- `declared_forbidden_changes.forbidden_operations`
- `non_authority_boundary`

## 14. M64-M67 Boundary Checks
Проверяются признаки попытки поглощения зон M64-M67.

## 15. Validator Result Values
- `M63_CONTRACT_VALIDATION_PASS`
- `M63_CONTRACT_VALIDATION_PASS_WITH_WARNINGS`
- `M63_CONTRACT_VALIDATION_BLOCKED`

## 16. Exit Codes
- `0` = PASS/PASS_WITH_WARNINGS
- `1` = BLOCKED
- `2` = internal error/cli misuse

## 17. JSON Output Contract
Выход содержит структурные флаги проверок, итог `result`, `warnings`, `blockers`, и обязательное поле `human_review_required: true`.

## 18. Validator Findings vs Input Warnings
Output warnings/blockers — это findings валидатора, не blind passthrough входного `warnings`/`blockers`.

## 19. Implementation Boundaries
Не используются внешние зависимости.
Не меняются файлы репозитория.
Нет сети.

## 20. Limitations
Валидатор M63 проверяет контрактный слой и не заменяет M64/M65/M66/M67.

## 21. Non-Authority Boundary
M63 contract validator is not approval.
M63 contract validator does not replace human review.
M63 contract validator does not complete the task.
M63 contract validator does not validate completed agent tasks as a production gate.
M63 contract validator does not define the full task output evidence model.
M63 contract validator does not define acceptance criteria checking.
M63 contract validator does not create the unified agent task validation runner.
M63 contract validator does not authorize merge, push, or release.
M63 contract validator does not start M64.
Human review remains required.

## 22. Final Status
FINAL_STATUS: M63_CONTRACT_VALIDATOR_DEFINED
