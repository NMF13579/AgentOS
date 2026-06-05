# numeric-boolean-human-review

## Purpose
Проверка одного контролируемого сценария для контрактного валидатора M63.

## Expected Validator Result
M63_CONTRACT_VALIDATION_BLOCKED

## Intentional Condition
human_review_required указан как число 1 вместо boolean true.

## Files
- package.json
- result.json
- expected-validator-result.txt

## Boundary Notes
This fixture is not approval.
Human review remains required.
