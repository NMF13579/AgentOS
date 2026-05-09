# M33 Status Layer Inspection

## Summary

Проведён read-only осмотр слоя статусов.
Цель: определить точные файлы, где нужно делать fail-closed (блокирующее поведение при сомнении) в задаче 33.2.1.
В этой задаче изменений логики не выполнялось.

## Preconditions

Проверки перед осмотром:
- `test -f reports/m33-p0-stabilization-findings-intake.md` -> passed
- `grep -q "M33_P0_FINDINGS_INTAKE_COMPLETE" reports/m33-p0-stabilization-findings-intake.md` -> passed

## Files Inspected

Ключевые файлы по результатам поиска:
- `scripts/check-context-pipeline.py`
- `scripts/agentos-status.py`
- `scripts/agentos-view-model.py`
- `scripts/agentos-explain.py`
- `scripts/agentos-next-step.py`
- `scripts/agentos-tui.py`
- `scripts/renderers/plain_status_renderer.py`
- `scripts/renderers/rich_status_renderer.py`
- `scripts/check-required-context-pack.py`
- `scripts/check-required-context-compliance.py`
- `docs/AGENTOS-STATUS.md`
- `docs/STATUS-VIEW-MODEL.md`
- `docs/EXPLANATION-VOCABULARY.md`
- `schemas/status-view-model.schema.json`
- `schemas/tutor-explanation.schema.json`
- `schemas/next-safe-step.schema.json`
- `tests/fixtures/context-pipeline-check/context-pack-invalid/expected-result.txt`
- `tests/fixtures/required-context-pack-gate/context-pack-claims-approval/fixture-notes.md`
- `reports/context-pipeline.json`
- `reports/context-pack.md`
- `reports/context-selection-record.md`

## Status Flow Found

Найден текущий поток:
1. `scripts/check-context-pipeline.py` формирует результат конвейера контекста.
2. Результат сохраняется/читается через `reports/context-pipeline.json`.
3. `scripts/agentos-status.py` читает `reports/context-pipeline.json` и строит общий статус.
4. `scripts/agentos-view-model.py` вызывает `agentos-status.py --json` и готовит модель для отображения.
5. `scripts/agentos-explain.py` и `scripts/agentos-next-step.py` делают пользовательские тексты.
6. `scripts/agentos-tui.py` + `scripts/renderers/*` показывают итог пользователю.

## Context Pipeline Result Sources

Источник результата `CONTEXT_PIPELINE_INVALID`:
- `scripts/check-context-pipeline.py` содержит константу `INVALID = "CONTEXT_PIPELINE_INVALID"`.
- `reports/context-pipeline.json` содержит `"result": "CONTEXT_PIPELINE_INVALID"`.
- Фикстура: `tests/fixtures/context-pipeline-check/context-pack-invalid/expected-result.txt` ожидает `CONTEXT_PIPELINE_INVALID`.

Связанные источники проверки контекста:
- `scripts/check-required-context-pack.py`
- `scripts/check-required-context-compliance.py`
- `scripts/check-context-required.py`

## Status Mapping Files

Файлы, где найдено сопоставление/обработка статусов:
- `scripts/agentos-status.py`
- `scripts/agentos-view-model.py`
- `scripts/agentos-explain.py`
- `scripts/agentos-next-step.py`
- `docs/EXPLANATION-VOCABULARY.md`
- `schemas/status-view-model.schema.json`
- `schemas/tutor-explanation.schema.json`
- `schemas/next-safe-step.schema.json`

Наблюдение:
- При повреждённом источнике статуса используются `AGENTOS_STATUS_UNKNOWN` и `STATUS_SOURCE_DAMAGED` (обнаружено в `agentos-status.py`, `agentos-view-model.py`, `agentos-explain.py`, `agentos-next-step.py`, `agentos-tui.py`, `plain_status_renderer.py`).

## TUI / User-Facing Rendering Files

Точный набор файлов отображения:
- `scripts/agentos-tui.py`
- `scripts/renderers/plain_status_renderer.py`
- `scripts/renderers/rich_status_renderer.py`
- `scripts/agentos-explain.py`
- `scripts/agentos-next-step.py`

## Tests / Fixtures Found

Точные файлы/наборы, связанные с этой темой:
- `tests/fixtures/context-pipeline-check/context-pack-invalid/expected-result.txt`
- `tests/fixtures/context-pipeline-check/context-pack-invalid/fixture-notes.md`
- `tests/fixtures/required-context-pack-gate/context-pack-claims-approval/fixture-notes.md`
- `tests/fixtures/required-context-pack-gate/missing-context-pack/fixture-notes.md`
- `tests/fixtures/required-context-pack-gate/malformed-context-pack/fixture-notes.md`
- `tests/fixtures/context-compliance/stale-context-pack/context-pack.md`
- `tests/fixtures/negative/README.md`

## Gaps

- Нет явного жёсткого правила в пользовательском слое, что `CONTEXT_PIPELINE_INVALID` всегда должен показываться как блокировка.
- `agentos-status.py` и производные слои используют fallback к `UNKNOWN/STATUS_SOURCE_DAMAGED`; нужен запрет на трактовку как готовность.
- Нужны более явные негативные фикстуры на цепочку: invalid context -> status mapping -> TUI.

## Recommended Implementation Scope for 33.2.1

Изменять только слой fail-closed сопоставления статусов и его проверки:
- источник статуса конвейера;
- агрегация статуса;
- view-model;
- пользовательское объяснение;
- TUI/рендер;
- целевые негативные фикстуры.

## Files Allowed for 33.2.1

- `scripts/check-context-pipeline.py`
- `scripts/agentos-status.py`
- `scripts/agentos-view-model.py`
- `scripts/agentos-explain.py`
- `scripts/agentos-next-step.py`
- `scripts/agentos-tui.py`
- `scripts/renderers/plain_status_renderer.py`
- `scripts/renderers/rich_status_renderer.py`
- `docs/EXPLANATION-VOCABULARY.md`
- `schemas/status-view-model.schema.json`
- `schemas/tutor-explanation.schema.json`
- `schemas/next-safe-step.schema.json`
- `tests/fixtures/context-pipeline-check/context-pack-invalid/expected-result.txt`
- `tests/fixtures/context-pipeline-check/context-pack-invalid/fixture-notes.md`
- `tests/fixtures/required-context-pack-gate/missing-context-pack/fixture-notes.md`
- `tests/fixtures/required-context-pack-gate/malformed-context-pack/fixture-notes.md`
- `tests/fixtures/required-context-pack-gate/context-pack-claims-approval/fixture-notes.md`

## Files Forbidden for 33.2.1

- `tasks/active-task.md`
- `data/context-index.json`
- `reports/context-pack.md`
- `reports/context-selection-record.md`
- `reports/context-pipeline.json`
- `reports/m33-p0-stabilization-findings-intake.md`
- `reports/m33-status-layer-inspection.md`

## Validation Evidence

Выполненные команды осмотра:
- `grep -R "CONTEXT_PIPELINE_INVALID" -n scripts docs reports tests templates schemas || true`
- `grep -R "STATUS_SOURCE_DAMAGED" -n scripts docs reports tests templates schemas || true`
- `grep -R "UNKNOWN" -n scripts docs reports tests templates schemas || true`
- `grep -R "BLOCKED" -n scripts docs reports tests templates schemas || true`
- `grep -R "NEEDS_REVIEW" -n scripts docs reports tests templates schemas || true`
- `grep -R "READY" -n scripts docs reports tests templates schemas || true`
- `grep -R "PASS" -n scripts docs reports tests templates schemas || true`
- `grep -R "OK" -n scripts docs reports tests templates schemas || true`
- `grep -R "agentos-status" -n scripts docs reports tests templates schemas || true`
- `grep -R "context-pipeline" -n scripts docs reports tests templates schemas || true`
- `grep -R "context-pack" -n scripts docs reports tests templates schemas || true`
- `find scripts -maxdepth 2 -type f | sort`
- `find tests -maxdepth 3 -type f | sort`
- `python3 scripts/agentos-status.py || true`
- `python3 scripts/check-context-pipeline.py || true`

Фактическое поведение команд:
- `python3 scripts/agentos-status.py` -> `AGENTOS_STATUS_UNKNOWN`, причина `STATUS_SOURCE_DAMAGED`.
- `python3 scripts/check-context-pipeline.py` -> `RESULT: CONTEXT_PIPELINE_INVALID`.

## Final Status

M33_STATUS_LAYER_INSPECTION_COMPLETE
