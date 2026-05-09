# M33 Negative Fixture Coverage Inspection

## Summary
Проведена read-only проверка покрытия негативных фикстур (негативных тестовых сценариев) для M33 hardening. Базовая инфраструктура фикстур и раннеров есть, но для части критичных M33-сценариев покрытие неполное или отсутствует.

## Preconditions
Проверки выполнены успешно:
- `reports/m33-p0-stabilization-findings-intake.md` содержит `M33_P0_FINDINGS_INTAKE_COMPLETE`
- `reports/m33-context-status-mapping.md` содержит `M33_CONTEXT_STATUS_MAPPING_COMPLETE`
- `reports/m33-context-pipeline-revalidation.md` содержит `M33_CONTEXT_PIPELINE_REVALIDATION_COMPLETE`
- `reports/m33-context-required-gate-implementation.md` содержит `M33_CONTEXT_REQUIRED_GATE_IMPLEMENTATION_COMPLETE`
- `reports/m33-tui-blocked-rendering-implementation.md` содержит `M33_TUI_BLOCKED_RENDERING_IMPLEMENTATION_COMPLETE`

## Inspection Method
- Выполнены только read-only команды `find`, `grep`, `rg`.
- Выполнен запуск существующих тест-раннеров без изменения файлов:
  - `python3 scripts/test-negative-fixtures.py`
  - `python3 scripts/test-guard-failures.py`
- Попытка запуска `bash scripts/test-negative-fixtures.sh` зафиксирована как отсутствующий файл.

## Files Inspected
Ключевые просмотренные области:
- `tests/fixtures/context-pipeline-check/*`
- `tests/fixtures/required-context-pack-gate/*`
- `tests/fixtures/context-required/*`
- `tests/fixtures/context-compliance-required-gate/*`
- `tests/fixtures/m29-m28-context-bypass/*`
- `tests/fixtures/negative/*`
- `scripts/test-negative-fixtures.py`
- `scripts/test-guard-failures.py`
- `scripts/agentos-status.py`
- `scripts/agentos-tui.py`
- `scripts/renderers/plain_status_renderer.py`
- `scripts/renderers/rich_status_renderer.py`

## Existing Negative Fixture Structure
Найдены устойчивые группы негативных фикстур:
- `tests/fixtures/negative/`
- `tests/fixtures/context-pipeline-check/`
- `tests/fixtures/required-context-pack-gate/`
- `tests/fixtures/context-required/`
- `tests/fixtures/context-compliance-required-gate/`
- `tests/fixtures/m29-m28-context-bypass/`

## Existing Test Runners
Найдены и/или выполнены:
- `scripts/test-negative-fixtures.py` (PASS)
- `scripts/test-guard-failures.py` (PASS_WITH_WARNINGS)
- `scripts/test-gate-regression-fixtures.py` (обнаружен, в рамках этой задачи не запускался)
- `scripts/test-unified-gate-smoke.py` (обнаружен, в рамках этой задачи не запускался)

Дополнительно:
- `scripts/test-negative-fixtures.sh` отсутствует.

## Context Pipeline Negative Coverage
Найдены прямые негативные сценарии:
- `tests/fixtures/context-pipeline-check/context-pack-invalid/expected-result.txt` (`CONTEXT_PIPELINE_INVALID`)
- `tests/fixtures/context-pipeline-check/context-pack-missing/expected-result.txt`
- `tests/fixtures/context-pipeline-check/context-pack-blocked/expected-result.txt`
- `tests/fixtures/context-pipeline-check/index-missing/expected-result.txt`
- `tests/fixtures/context-pipeline-check/gate-script-missing/expected-result.txt`

Оценка: базовое покрытие есть.

## Context Required Gate Negative Coverage
Найдены негативные сценарии gate (блокирующей проверки контекста):
- `tests/fixtures/required-context-pack-gate/missing-context-pack/expected-result.txt`
- `tests/fixtures/required-context-pack-gate/malformed-context-pack/expected-result.txt`
- `tests/fixtures/required-context-pack-gate/missing-required-context-section/expected-result.txt`
- `tests/fixtures/required-context-pack-gate/empty-required-context-without-justification/expected-result.txt`
- `tests/fixtures/required-context-pack-gate/context-pack-claims-approval/expected-result.txt`

Оценка: покрытие хорошее по базовым блокировкам, но не полное по M33-терминам состояний.

## TUI / Status Rendering Negative Coverage
Поиск показал, что production-рендеринг блокировки реализован в:
- `scripts/agentos-status.py`
- `scripts/agentos-tui.py`
- `scripts/renderers/plain_status_renderer.py`
- `scripts/renderers/rich_status_renderer.py`

Отдельные fixture-сценарии, которые явно доказывают M33-пары (`UNKNOWN`/`STATUS_SOURCE_DAMAGED` -> `BLOCKED`/`NEEDS_REVIEW`) как отдельный negative набор, не обнаружены.

## False Success Prevention Coverage
Частичное покрытие обнаружено:
- bypass/required-context наборы проверяют, что плохие контексты не проходят как allowed.
- прямых M33-фикстур на запрет ложных `READY/PASS/OK` для каждого плохого состояния в одном едином наборе нет.

## Valid Context Control Coverage
Найдены контрольные позитивные сценарии (чтобы валидный контекст не блокировался):
- `tests/fixtures/context-pipeline-check/ready-pipeline/expected-result.txt`
- `tests/fixtures/required-context-pack-gate/valid-context-pack/expected-result.txt`
- `tests/fixtures/context-required/valid-context-pack/expected-result.txt`

## Missing Coverage
Недостаточно явного покрытия по M33-категориям:
- `Required Context: none` как отдельный негативный fixture (в явном виде)
- `UNKNOWN context state` как отдельный негативный fixture для статуса/рендера
- `STATUS_SOURCE_DAMAGED` как отдельный негативный fixture для статуса/рендера
- явный anti-false-success тест: плохой контекст не может отобразиться как `READY/PASS/OK`

## Coverage Classification Table
- context pipeline invalid fixture: `COVERED`
- missing context-pack fixture: `COVERED`
- empty context-pack fixture: `PARTIALLY_COVERED`
- Required Context: none fixture: `MISSING`
- UNKNOWN context state fixture: `MISSING`
- STATUS_SOURCE_DAMAGED fixture: `MISSING`
- execution blocked fixture: `PARTIALLY_COVERED`
- TUI blocked rendering fixture: `MISSING`
- false READY/PASS/OK prevention fixture: `PARTIALLY_COVERED`
- valid context still allowed fixture: `COVERED`

## Recommended Implementation Scope for 33.6.1
Для 33.6.1 нужен узкий объём: добавить/обновить только целевые негативные сценарии M33 и их проверки в существующих раннерах, без изменения production-логики.

## Files Allowed for 33.6.1
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

## Files Forbidden for 33.6.1
- `scripts/agentos-status.py`
- `scripts/agentos-tui.py`
- `scripts/check-context-pipeline.py`
- `scripts/check-required-context-pack.py`
- `scripts/check-context-required.py`
- `data/context-index.json`
- `reports/context-pack.md`
- `reports/context-selection-record.md`
- `reports/context-pipeline.json`
- `tasks/active-task.md`

## Potential New Files Requiring Human Decision
- `tests/fixtures/context-pipeline-check/context-state-unknown/expected-result.txt`
- `tests/fixtures/context-pipeline-check/context-state-unknown/fixture-notes.md`
- `tests/fixtures/context-pipeline-check/status-source-damaged/expected-result.txt`
- `tests/fixtures/context-pipeline-check/status-source-damaged/fixture-notes.md`
- `tests/fixtures/required-context-pack-gate/required-context-none/expected-result.txt`
- `tests/fixtures/required-context-pack-gate/required-context-none/fixture-notes.md`
- `tests/fixtures/tui-blocked-rendering/unknown-renders-needs-review/expected-output.txt`
- `tests/fixtures/tui-blocked-rendering/status-source-damaged-renders-blocked/expected-output.txt`

## Validation Evidence
Выполненные команды:
- precondition `test -f` + `grep -q` для пяти M33 отчётов
- `find tests -maxdepth 5 -type f | sort`
- `find tests -maxdepth 5 -type d | sort`
- `find scripts -maxdepth 3 -type f | sort`
- множественные `grep -R` по ключам: `negative`, `fixture`, `CONTEXT_PIPELINE_INVALID`, `CONTEXT_REQUIRED_MISSING`, `CONTEXT_REQUIRED_INVALID`, `CONTEXT_GATE_BLOCKED`, `STATUS_SOURCE_DAMAGED`, `UNKNOWN`, `Required Context: none`, `No Context Pack`, `READY`, `PASS`, `OK`
- `python3 scripts/test-negative-fixtures.py` -> `Result: PASS`
- `python3 scripts/test-guard-failures.py` -> `Result: PASS_WITH_WARNINGS`
- `bash scripts/test-negative-fixtures.sh || true` -> отсутствует файл

## Known Gaps
- Нет явного единого M33-набора негативных фикстур именно для user-facing статусов `UNKNOWN`/`STATUS_SOURCE_DAMAGED`.
- Нет явного M33-фикстурного доказательства для `Required Context: none` как отдельного статуса/причины блокировки.
- Есть исторические дубли файлов с суффиксом ` 3` в ряде каталогов; это повышает риск неоднозначной выборки кейсов в будущих задачах.

## Final Status
`M33_NEGATIVE_FIXTURE_COVERAGE_INSPECTION_COMPLETE`

## Required Behavior for Future 33.6.1
Будущая 33.6.1 должна доказать, что:
- missing Context Pack does not become READY
- empty Context Pack does not become PASS
- Required Context: none does not become OK
- CONTEXT_PIPELINE_INVALID blocks execution
- CONTEXT_REQUIRED_MISSING blocks execution
- CONTEXT_REQUIRED_INVALID blocks execution
- STATUS_SOURCE_DAMAGED renders BLOCKED / NEEDS_REVIEW
- UNKNOWN context state renders BLOCKED / NEEDS_REVIEW
- TUI/status output does not claim approval
- valid Context Pack is not blocked by negative-only logic

И 33.6.1 не должна:
- change production logic
- repair frontmatter
- rebuild context-index
- regenerate context-pack
- broaden execution gates
- redesign TUI
