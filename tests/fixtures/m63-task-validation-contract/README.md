# M63 Task Validation Contract Fixtures

## 1. Purpose
Набор контролируемых примеров для проверки валидатора M63.

## 2. Fixture Scope
Покрываются только контрактные проверки структуры и границ ответственности.

## 3. Fixture List
- valid-minimal-package-and-result
- valid-package-result-with-warnings
- missing-package-field
- missing-result-field
- malformed-package-json
- malformed-result-json
- unsupported-contract-version
- task-id-mismatch
- unknown-result-value
- unknown-subresult-value
- human-review-disabled
- numeric-boolean-human-review
- wrong-required-field-type
- package-valid-contradiction
- approval-claim-present
- missing-non-authority-boundary
- missing-required-boundary-statement
- m64-m67-scope-absorption

## 4. Expected Validator Results
Ожидаемые результаты заданы в каждом `expected-validator-result.txt` и в `fixture-manifest.json`.

## 5. How 63.8 Uses These Fixtures
В 63.8 эти примеры можно использовать для краткой sanity-проверки (минимальной проверки), без полного регресса.

## 6. What These Fixtures Do Not Cover
Это не полный набор M67 false PASS resistance suite и не production gate.

## 7. Human Review Boundary
Во всех позитивных примерах сохраняется требование ручной проверки человеком.

## 8. Non-Authority Boundary
M63 contract fixtures are not approval.
M63 contract fixtures do not replace human review.
M63 contract fixtures do not complete the task.
M63 contract fixtures do not validate completed agent tasks as a production gate.
M63 contract fixtures are not the M67 false PASS resistance suite.
M63 contract fixtures do not define the full task output evidence model.
M63 contract fixtures do not define acceptance criteria checking.
M63 contract fixtures do not authorize merge, push, or release.
M63 contract fixtures do not start M64.
Human review remains required.

## 9. Final Status
FINAL_STATUS: M63_CONTRACT_FIXTURES_COMPLETE
