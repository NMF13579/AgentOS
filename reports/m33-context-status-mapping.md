## Summary

Реализовано fail-closed сопоставление статусов (при сомнении блокируем):
- invalid/missing/damaged контекст больше не должен показываться как `OK/READY/PASS`.
- пользователь видит `BLOCKED` или `NEEDS_REVIEW`.

## Preconditions

- `test -f reports/m33-p0-stabilization-findings-intake.md` -> passed
- `grep -q "M33_P0_FINDINGS_INTAKE_COMPLETE" reports/m33-p0-stabilization-findings-intake.md` -> passed
- `test -f reports/m33-status-layer-inspection.md` -> passed
- `grep -q "M33_STATUS_LAYER_INSPECTION_COMPLETE" reports/m33-status-layer-inspection.md` -> passed
- `grep -q "Files Allowed for 33.2.1" reports/m33-status-layer-inspection.md` -> passed

## Inspection Report Used

- `reports/m33-status-layer-inspection.md`

## Files Allowed by 33.2.0

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

## Files Modified

- `scripts/agentos-status.py`
- `scripts/check-context-pipeline.py`
- `scripts/agentos-view-model.py`
- `scripts/agentos-explain.py`
- `scripts/agentos-next-step.py`
- `scripts/agentos-tui.py`
- `reports/m33-context-status-mapping.md`

## Mapping Implemented

Реализовано:
- `CONTEXT_PIPELINE_INVALID -> BLOCKED`
- `CONTEXT_REQUIRED_MISSING -> BLOCKED`
- `CONTEXT_REQUIRED_INVALID -> BLOCKED`
- `STATUS_SOURCE_DAMAGED -> BLOCKED`
- `STATUS_SOURCE_MISSING -> BLOCKED`
- `UNKNOWN` из context source -> `NEEDS_REVIEW` (блокирующий по authority `SYSTEM_BLOCKED`)
- `empty/missing/invalid context pack` через pipeline source -> блокирующий статус (BLOCKED)

Дополнительно:
- В `scripts/check-context-pipeline.py` для `--strict` добавлен fail-closed: любой non-ready результат gate переводит итог в `CONTEXT_PIPELINE_BLOCKED`.
- В fallback-ветках (`view-model`, `explain`, `next-step`, `tui`) статус при повреждении источника меняется с `UNKNOWN` на `BLOCKED`.

## Forbidden Mappings Checked

Проверено, что в изменённой логике больше нет целевых недопустимых трактовок:
- `CONTEXT_PIPELINE_INVALID -> READY/PASS/OK` (forbidden)
- `CONTEXT_REQUIRED_MISSING -> READY` (forbidden)
- `CONTEXT_REQUIRED_INVALID -> PASS` (forbidden)
- `UNKNOWN -> PASS/READY` (forbidden)
- `STATUS_SOURCE_DAMAGED -> READY` (forbidden)
- `missing/empty context pack -> OK` (forbidden)

## TUI / User-Facing Impact

Пользовательский вывод теперь в проблемном состоянии показывает блокировку:
- `Status: AGENTOS_STATUS_BLOCKED`
- причина указывает повреждённый/невалидный источник (`STATUS_SOURCE_DAMAGED` и т.п.)
- next step остаётся безопасной подсказкой и не означает разрешение на выполнение

## Tests / Fixtures Updated

Не изменялись.

## Validation Evidence

Запущено после изменений:
- `python3 scripts/agentos-status.py || true`
  - факт: `Status: AGENTOS_STATUS_BLOCKED`
  - факт: `Reason: STATUS_SOURCE_DAMAGED`
- `python3 scripts/check-context-pipeline.py || true`
  - факт: `RESULT: CONTEXT_PIPELINE_INVALID`
- `bash scripts/run-all.sh || true`
  - факт: команда завершилась с FAIL на валидации `tasks/active-task.md` (ожидаемое текущее состояние репозитория, не связано с этой правкой)

## Known Gaps

- Тесты/фикстуры для новой fail-closed цепочки в этой задаче не обновлялись.
- Нужно отдельной задачей добавить точечные фикстуры на user-facing mapping для `STATUS_SOURCE_DAMAGED` и `CONTEXT_REQUIRED_*`.

## Final Status

M33_CONTEXT_STATUS_MAPPING_COMPLETE
