# M33 Context Hardening Negative Fixtures

## Summary
Добавлены точечные негативные фикстуры для M33, чтобы явно покрыть два недостающих сценария: `CONTEXT_REQUIRED_INVALID` и `CONTEXT_REQUIRED_MISSING`.

## Preconditions
Проверки перед изменениями выполнены успешно:
- `reports/m33-p0-stabilization-findings-intake.md` содержит `M33_P0_FINDINGS_INTAKE_COMPLETE`
- `reports/m33-context-status-mapping.md` содержит `M33_CONTEXT_STATUS_MAPPING_COMPLETE`
- `reports/m33-context-required-gate-implementation.md` содержит `M33_CONTEXT_REQUIRED_GATE_IMPLEMENTATION_COMPLETE`
- `reports/m33-tui-blocked-rendering-implementation.md` содержит `M33_TUI_BLOCKED_RENDERING_IMPLEMENTATION_COMPLETE`
- `reports/m33-negative-fixture-coverage-inspection.md` содержит `M33_NEGATIVE_FIXTURE_COVERAGE_INSPECTION_COMPLETE`
- `reports/m33-negative-fixture-coverage-inspection.md` содержит `Files Allowed for 33.6.1`

## Inspection Report Used
- `reports/m33-negative-fixture-coverage-inspection.md`

## Files Allowed by 33.6.0
- `scripts/test-gate-regression-fixtures.py`
- `scripts/test-unified-gate-smoke.py`
- `scripts/test-guard-failures.py`
- `tests/fixtures/context-pipeline-check/context-pack-invalid/expected-result.txt`
- `tests/fixtures/context-pipeline-check/context-pack-missing/expected-result.txt`
- `tests/fixtures/required-context-pack-gate/missing-context-pack/expected-result.txt`
- `tests/fixtures/required-context-pack-gate/empty-required-context-without-justification/expected-result.txt`
- `tests/fixtures/required-context-pack-gate/missing-required-context-section/expected-result.txt`
- `tests/fixtures/context-required/invalid-status/expected-result.txt`
- `tests/fixtures/context-required/missing-context-pack/expected-result.txt`

## Fixture Files Created
- `tests/fixtures/context-required/invalid-status/expected-result.txt`
- `tests/fixtures/context-required/missing-context-pack/expected-result.txt`

## Fixture Files Updated
- none

## Scenario Coverage
Покрыто в рамках новых файлов:
- `context-required-invalid` -> `CONTEXT_REQUIRED_INVALID`
- `context-required-missing` -> `CONTEXT_REQUIRED_MISSING`

Уже существующее покрытие (без изменений в этой задаче):
- `context-pipeline-invalid`
- `missing-context-pack`
- `empty-context-pack` (частично)
- `valid-context-control`

## Expected Blocked Results
Для плохих состояний ожидаются блокирующие результаты (запрещающие продолжение):
- `CONTEXT_REQUIRED_INVALID`
- `CONTEXT_REQUIRED_MISSING`
- также в существующих наборах: `CONTEXT_PIPELINE_INVALID`, `CONTEXT_PACK_MISSING`, `CONTEXT_PACK_NEEDS_REVIEW`, `CONTEXT_PACK_INVALID`

## Forbidden Success Results
Для плохих состояний запрещены результаты:
- `READY`
- `PASS`
- `OK`
- `SUCCESS`
- `APPROVED`
- `EXECUTION_ALLOWED`

## Valid Context Control
Контроль «валидный контекст не должен ломаться от негативной логики» остаётся в существующих фикстурах (например, `valid-context-pack` в `required-context-pack-gate` и `context-pipeline-check/ready-pipeline`). В этой задаче эти сценарии не менялись.

## Tests / Runner Changes
- Изменения раннеров не выполнялись.
- Production-логика не менялась.
- Runner wiring (подключение новых кейсов в запуск) оставлен без изменений.

## Validation Evidence
Команды до изменений:
- `test -f reports/m33-negative-fixture-coverage-inspection.md`
- `grep -q "M33_NEGATIVE_FIXTURE_COVERAGE_INSPECTION_COMPLETE" reports/m33-negative-fixture-coverage-inspection.md`
- `grep -q "Files Allowed for 33.6.1" reports/m33-negative-fixture-coverage-inspection.md`

Команды после изменений:
- `test -f reports/m33-context-hardening-negative-fixtures.md`
- `grep -q "M33_CONTEXT_HARDENING_NEGATIVE_FIXTURES_COMPLETE" reports/m33-context-hardening-negative-fixtures.md`
- `grep -q "Scenario Coverage" reports/m33-context-hardening-negative-fixtures.md`
- `grep -q "Forbidden Success Results" reports/m33-context-hardening-negative-fixtures.md`
- `grep -q "Valid Context Control" reports/m33-context-hardening-negative-fixtures.md`
- `grep -q "Known Gaps" reports/m33-context-hardening-negative-fixtures.md`
- `git diff --check`
- `git status --short`

Дополнительно:
- `bash scripts/test-negative-fixtures.sh || true` -> файл отсутствует
- `python3 scripts/test-negative-fixtures.py || true` -> PASS
- `python3 scripts/test-guard-failures.py || true` -> PASS_WITH_WARNINGS
- `python3 scripts/check-context-pipeline.py || true` -> `CONTEXT_PIPELINE_VIOLATION`
- `python3 scripts/agentos-status.py || true` -> BLOCKED
- `bash scripts/run-all.sh || true` -> валидация task failed из-за формата `tasks/active-task.md`

## Known Gaps
- Новые файлы `expected-result.txt` добавлены, но отдельное подключение к конкретному раннеру не расширялось в этой задаче.
- Нет новых отдельный фикстур для `STATUS_SOURCE_DAMAGED` и `UNKNOWN context state` в рамках разрешённых путей 33.6.0.
- Нет отдельного нового кейса для `Required Context: none` в рамках разрешённых путей 33.6.0.

## Final Status
`M33_CONTEXT_HARDENING_NEGATIVE_FIXTURES_COMPLETE`
