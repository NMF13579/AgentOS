# M33 Negative Fixture Runner Wiring

## Summary
Подключено выполнение M33 negative fixtures в существующий runner-контур: добавлена проверка M33 expected-result файлов в `scripts/test-gate-regression-fixtures.py` и подключение этого раннера в `scripts/test-guard-failures.py`.

## Preconditions
Проверки выполнены успешно:
- `reports/m33-negative-fixture-coverage-inspection.md` содержит `M33_NEGATIVE_FIXTURE_COVERAGE_INSPECTION_COMPLETE`
- `reports/m33-context-hardening-negative-fixtures.md` содержит `M33_CONTEXT_HARDENING_NEGATIVE_FIXTURES_COMPLETE`
- `reports/m33-context-hardening-negative-fixtures.md` содержит `Tests / Runner Changes`
- `reports/m33-context-hardening-negative-fixtures.md` содержит `Known Gaps`

## Fixture Report Used
- `reports/m33-negative-fixture-coverage-inspection.md`
- `reports/m33-context-hardening-negative-fixtures.md`

## Runner Files Allowed
- `scripts/test-gate-regression-fixtures.py`
- `scripts/test-unified-gate-smoke.py`
- `scripts/test-guard-failures.py`

## Runner Files Modified
- `scripts/test-gate-regression-fixtures.py`
- `scripts/test-guard-failures.py`

## Fixture Groups Wired
- `context-pipeline-check` expected-result fixtures
- `required-context-pack-gate` expected-result fixtures
- `context-required` expected-result fixtures
- valid-control fixture from `required-context-pack-gate/valid-context-pack`

## Scenarios Wired
- `context-pipeline-invalid`
- `missing-context-pack`
- `empty-context-pack`
- `context-required-missing`
- `context-required-invalid`
- `false-ready-prevention`
- `false-pass-prevention`
- `false-ok-prevention`
- `valid-context-control`

## Scenarios Missing
- `required-context-none`
- `status-source-damaged`
- `unknown-context-state`
- `pipeline-rebuild-failed`
- `pipeline-validation-inconclusive`
- `false-approval-prevention` (явный отдельный fixture в wired-наборе)

## Expected Negative Result Semantics
Runner считает негативный тест успешным, если observed-результат находится в блокирующих/требующих проверки значениях:
- `BLOCKED`
- `NEEDS_REVIEW`
- `CONTEXT_REQUIRED_MISSING`
- `CONTEXT_REQUIRED_INVALID`
- `CONTEXT_GATE_BLOCKED`
- `CONTEXT_PIPELINE_INVALID`
- `STATUS_SOURCE_DAMAGED`
- `CONTEXT_PIPELINE_MISSING`
- `CONTEXT_PACK_MISSING`
- `CONTEXT_PACK_INVALID`
- `CONTEXT_PACK_NEEDS_REVIEW`

## Forbidden Success Result Semantics
Runner считает тест проваленным, если observed-результат равен одному из запрещённых «ложно успешных» значений:
- `READY`
- `PASS`
- `OK`
- `SUCCESS`
- `APPROVED`
- `EXECUTION_ALLOWED`

## Valid Context Control Handling
Добавлен контрольный сценарий: `tests/fixtures/required-context-pack-gate/valid-context-pack/expected-result.txt`.
Он проходит только при безопасном «валидном» результате (например, `CONTEXT_PACK_VALID`, `CONTEXT_REQUIRED_OK`, `CONTEXT_PIPELINE_READY`) и не трактуется как автоматическое разрешение полного выполнения задачи.

## Validation Evidence
Перед изменениями:
- `test -f reports/m33-negative-fixture-coverage-inspection.md`
- `grep -q "M33_NEGATIVE_FIXTURE_COVERAGE_INSPECTION_COMPLETE" reports/m33-negative-fixture-coverage-inspection.md`
- `test -f reports/m33-context-hardening-negative-fixtures.md`
- `grep -q "M33_CONTEXT_HARDENING_NEGATIVE_FIXTURES_COMPLETE" reports/m33-context-hardening-negative-fixtures.md`

После изменений:
- `test -f reports/m33-negative-fixture-runner-wiring.md`
- `grep -q "M33_NEGATIVE_FIXTURE_RUNNER_WIRING_COMPLETE" reports/m33-negative-fixture-runner-wiring.md`
- `grep -q "Fixture Groups Wired" reports/m33-negative-fixture-runner-wiring.md`
- `grep -q "Expected Negative Result Semantics" reports/m33-negative-fixture-runner-wiring.md`
- `grep -q "Forbidden Success Result Semantics" reports/m33-negative-fixture-runner-wiring.md`
- `grep -q "Valid Context Control Handling" reports/m33-negative-fixture-runner-wiring.md`
- `git diff --check`
- `bash scripts/test-negative-fixtures.sh || true`
- `python3 scripts/test-negative-fixtures.py || true`
- `python3 scripts/test-guard-failures.py || true`
- `python3 scripts/check-context-pipeline.py || true`
- `python3 scripts/agentos-status.py || true`
- `bash scripts/run-all.sh || true`
- `git status --short`

## Known Gaps
- Часть M33 сценариев не подключена, потому что в разрешённом списке нет соответствующих fixture-путей.
- `scripts/test-negative-fixtures.sh` отсутствует.
- `bash scripts/run-all.sh` падает на валидации `tasks/active-task.md` (вне scope этой задачи).

## Final Status
`M33_NEGATIVE_FIXTURE_RUNNER_WIRING_COMPLETE`
