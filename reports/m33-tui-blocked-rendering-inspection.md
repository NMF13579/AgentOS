# M33 TUI Blocked Status Rendering Inspection

## Summary
Проведён только read-only осмотр (только чтение). Найдены конкретные файлы, где формируется пользовательский статус и где может появляться риск ложной уверенности при `UNKNOWN`/`STATUS_SOURCE_DAMAGED`.

## Preconditions
- `reports/m33-p0-stabilization-findings-intake.md` + `M33_P0_FINDINGS_INTAKE_COMPLETE`: PASS
- `reports/m33-context-status-mapping.md` + `M33_CONTEXT_STATUS_MAPPING_COMPLETE`: PASS
- `reports/m33-context-required-gate-implementation.md` + `M33_CONTEXT_REQUIRED_GATE_IMPLEMENTATION_COMPLETE`: PASS

## Inspection Method
- Поиск по ключевым словам (`STATUS_SOURCE_DAMAGED`, `UNKNOWN`, `BLOCKED`, `NEEDS_REVIEW`, `agentos-status`, `TUI`, `Context Pack`, `No Context Pack`, `Next safe action`).
- Точечное чтение status/TUI цепочки:
  - `scripts/agentos-status.py`
  - `scripts/agentos-view-model.py`
  - `scripts/agentos-explain.py`
  - `scripts/agentos-next-step.py`
  - `scripts/agentos-tui.py`
  - `scripts/renderers/plain_status_renderer.py`
  - `scripts/renderers/rich_status_renderer.py`
- Запуск read-only команд для фактического вывода.

## Files Inspected
- scripts/agentos-status.py
- scripts/agentos-view-model.py
- scripts/agentos-explain.py
- scripts/agentos-next-step.py
- scripts/agentos-tui.py
- scripts/renderers/plain_status_renderer.py
- scripts/renderers/rich_status_renderer.py
- scripts/agentos.py
- scripts/audit-m31-tui-tutor.py
- docs/AGENTOS-TUI.md
- docs/STATUS-VIEW-MODEL.md
- docs/NEXT-SAFE-STEP.md
- docs/EXPLANATION-VOCABULARY.md

## Status Rendering Entry Points Found
- `scripts/agentos-status.py` — агрегирует технический статус (агрегация = сбор из источников в один итог).
- `scripts/agentos-view-model.py` — строит единый объект для UI/TUI (view model = подготовленная модель показа).
- `scripts/agentos-explain.py` — строит человекочитаемое объяснение.
- `scripts/agentos-next-step.py` — строит безопасный следующий шаг.
- `scripts/agentos-tui.py` — собирает экран и печатает итог пользователю.
- `scripts/agentos.py` — CLI-роутинг к `agentos-status.py`/`agentos-tui.py`.

## TUI Rendering Files Found
- `scripts/agentos-tui.py`
- `scripts/renderers/plain_status_renderer.py`
- `scripts/renderers/rich_status_renderer.py`

## Status Value to Display Mapping Found
- В `scripts/agentos-status.py` найдено явное сопоставление технических кодов в пользовательские статусы:
  - `CONTEXT_PIPELINE_INVALID`/`STATUS_SOURCE_DAMAGED` -> `AGENTOS_STATUS_BLOCKED`
  - `UNKNOWN` -> `AGENTOS_STATUS_NEEDS_REVIEW` (с `SYSTEM_BLOCKED`)
- В `scripts/agentos-tui.py` и `scripts/renderers/plain_status_renderer.py` найден вывод полей:
  - `Status: ...`
  - `Reason: ...`
  - `Next safe step: ...`

## BLOCKED / NEEDS_REVIEW Display Path
Цепочка показа блокировки:
1. `scripts/agentos-status.py` (вычисляет `AGENTOS_STATUS_BLOCKED` / `AGENTOS_STATUS_NEEDS_REVIEW`).
2. `scripts/agentos-view-model.py` (нормализует поля `severity`, `blocked_actions`, `title`, `summary`).
3. `scripts/agentos-tui.py` + renderer (показывают человеку статус/причину/шаг).

## UNKNOWN / STATUS_SOURCE_DAMAGED Display Risk
Риск подтверждён:
- fallback-значения всё ещё присутствуют в нескольких местах (`AGENTOS_STATUS_UNKNOWN`, `STATUS_SOURCE_DAMAGED` по умолчанию), особенно при повреждённом источнике.
- если текст объяснения недостаточно явный, пользователь может не понять, что это именно блокировка, а не "обычное предупреждение".

## User-Facing Explanation Gaps
- Нет единой, всегда одинаковой фразы "Execution blocked" во всех точках вывода.
- Причина иногда остаётся технической (`STATUS_SOURCE_DAMAGED`) без простого текста причины для непрофильного пользователя.
- Нет обязательной унифицированной фразы, что вывод статуса не является approval (approval = человеческое разрешение).

## Next Safe Action Display Gaps
- `Next safe step` есть, но нет жёстко обязательной формулировки именно для контекстной блокировки (missing/empty/invalid/damaged/inconclusive Context Pack).
- Нужно закрепить единый безопасный текст следующего шага в TUI/Status слоях.

## Tests / Fixtures Found
- `tests/fixtures/required-context-pack-gate/missing-context-pack/expected-result.txt`
- `tests/fixtures/required-context-pack-gate/malformed-context-pack/expected-result.txt`
- `tests/fixtures/context-pipeline-check/context-pack-invalid/expected-result.txt`
- `scripts/audit-m31-tui-tutor.py` (аудит TUI-поведения)

## Recommended Implementation Scope for 33.5.1
Для 33.5.1 достаточно точечных правок только в существующей цепочке показа статуса/объяснения/next-step:
- нормализовать человекочитаемую blocked-фразу,
- нормализовать объяснение причины,
- нормализовать next safe action,
- не менять execution gate (он уже реализован в 33.4.1).

## Files Allowed for 33.5.1
- scripts/agentos-status.py
- scripts/agentos-view-model.py
- scripts/agentos-explain.py
- scripts/agentos-next-step.py
- scripts/agentos-tui.py
- scripts/renderers/plain_status_renderer.py
- scripts/renderers/rich_status_renderer.py
- scripts/audit-m31-tui-tutor.py
- tests/fixtures/required-context-pack-gate/missing-context-pack/expected-result.txt
- tests/fixtures/required-context-pack-gate/malformed-context-pack/expected-result.txt
- tests/fixtures/context-pipeline-check/context-pack-invalid/expected-result.txt

## Files Forbidden for 33.5.1
- tasks/active-task.md
- data/context-index.json
- reports/context-pack.md
- reports/context-selection-record.md
- reports/context-pipeline.json
- scripts/check-context-pipeline.py
- scripts/check-execution-readiness.py
- scripts/run-active-task.py
- scripts/run-all.sh
- любой файл вне `Files Allowed for 33.5.1`

## Required Behavior for 33.5.1
Обязательно отображать так:
- `Status: BLOCKED` или `Status: NEEDS_REVIEW`
- `Reason: Context Pack is missing, empty, invalid, damaged, or inconclusive.`
- `Next safe action: inspect context pipeline, repair frontmatter, rebuild context artifacts, or request human review in a separate scoped task.`

И обязательно не допускать:
- `UNKNOWN` как success
- `STATUS_SOURCE_DAMAGED` как success
- `READY` при invalid context
- `PASS` при missing context
- `OK` при empty Context Pack

Дополнительно: TUI/status output is not approval.

## Potential New File Requiring Human Decision
NO_EXISTING_TUI_RENDERING_FILE_FOUND

(Новая сущность не требуется: существующая цепочка файлов достаточна для 33.5.1.)

## Validation Evidence
Выполнены команды:
- `grep -R "STATUS_SOURCE_DAMAGED" -n scripts docs tests templates schemas reports || true`
- `grep -R "UNKNOWN" -n scripts docs tests templates schemas reports || true`
- `grep -R "BLOCKED" -n scripts docs tests templates schemas reports || true`
- `grep -R "NEEDS_REVIEW" -n scripts docs tests templates schemas reports || true`
- `grep -R "agentos-status" -n scripts docs tests templates schemas reports || true`
- `grep -R "TUI" -n scripts docs tests templates schemas reports || true`
- `grep -R "tui" -n scripts docs tests templates schemas reports || true`
- `grep -R "Context Pack" -n scripts docs tests templates schemas reports || true`
- `grep -R "No Context Pack" -n scripts docs tests templates schemas reports || true`
- `grep -R "Next safe action" -n scripts docs tests templates schemas reports || true`
- `find scripts -maxdepth 3 -type f | sort`
- `find tests -maxdepth 4 -type f | sort`
- `python3 scripts/agentos-status.py || true`
- `python3 scripts/check-context-pipeline.py || true`
- `bash scripts/run-all.sh || true`

Фактические наблюдения:
- `agentos-status.py` -> `AGENTOS_STATUS_BLOCKED`, `Reason: STATUS_SOURCE_DAMAGED`
- `check-context-pipeline.py` -> `CONTEXT_PIPELINE_VIOLATION`
- `run-all.sh` -> FAIL (schema mismatch в `tasks/active-task.md`) — это за пределами 33.5.0 и зафиксировано как факт.

## Known Gaps
- Нет отдельного негативного фикстурного теста именно на текстовую формулировку "Execution blocked ..." в TUI слое.
- Нужна синхронизация текста между `status`/`explain`/`next-step`/`tui`, чтобы не было расхождений формулировок.

## Final Status
M33_TUI_BLOCKED_RENDERING_INSPECTION_COMPLETE
