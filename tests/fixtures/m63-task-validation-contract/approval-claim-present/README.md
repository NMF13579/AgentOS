# approval-claim-present

## Purpose
Проверка одного контролируемого сценария для контрактного валидатора M63.

## Expected Validator Result
M63_CONTRACT_VALIDATION_BLOCKED

## Intentional Condition
Добавлен явный запрещённый утвердительный текст вне safe-context: task is approved.

## Files
- package.json
- result.json
- expected-validator-result.txt

## Boundary Notes
This fixture is not approval.
Human review remains required.
