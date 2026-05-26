# M62 Task Acceptance MVP Fixtures

## 1. Purpose
Набор контролируемых примеров для тонкого runner из M62, чтобы проверить базовые исходы без production-семантики.

## 2. Fixture Scope
Покрываются только MVP-сценарии: PASS, PASS_WITH_WARNINGS, BLOCKED, NOT_ENOUGH_EVIDENCE.
Это не полный набор ложного PASS и не production gate.

## 3. Fixture List
- valid-minimal-task-result
- valid-with-warning
- missing-evidence
- missing-expected-artifact
- forbidden-path-changed
- human-review-disabled
- approval-claim-present
- malformed-changed-files-json
- not-enough-evidence

## 4. Expected Results
- valid-minimal-task-result -> TASK_VALIDATION_PASS
- valid-with-warning -> TASK_VALIDATION_PASS_WITH_WARNINGS
- missing-evidence -> TASK_VALIDATION_BLOCKED
- missing-expected-artifact -> TASK_VALIDATION_BLOCKED
- forbidden-path-changed -> TASK_VALIDATION_BLOCKED
- human-review-disabled -> TASK_VALIDATION_BLOCKED
- approval-claim-present -> TASK_VALIDATION_BLOCKED
- malformed-changed-files-json -> TASK_VALIDATION_BLOCKED
- not-enough-evidence -> TASK_VALIDATION_NOT_ENOUGH_EVIDENCE

## 5. How 62.6 Uses These Fixtures
В 62.6 runner запускается на каждом примере и сравнивается фактический результат с `expected-result.txt`.

## 6. What These Fixtures Do Not Cover
- полный M67 false PASS resistance suite
- полный контракт M63
- полная модель evidence M64
- полный acceptance checker M65
- unified runner M66

## 7. Non-Authority Boundary
M62 controlled trial fixtures are not approval.
M62 controlled trial fixtures do not replace human review.
M62 controlled trial fixtures do not validate completed agent tasks as a production gate.
M62 controlled trial fixtures are not the M67 false PASS resistance suite.
M62 controlled trial fixtures do not authorize merge, push, or release.
M62 controlled trial fixtures do not start M63.
Human review remains required.

## 8. Final Status
FINAL_STATUS: M62_MVP_CONTROLLED_TRIAL_FIXTURES_COMPLETE
