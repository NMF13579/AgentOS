# M33 TUI Blocked Status Rendering Implementation

## Summary
Выполнены точечные изменения пользовательского вывода статуса, чтобы при проблемном контексте показывался явный блокирующий смысл (блокировка = продолжать нельзя) без изменения execution gate (механизм допуска к запуску) и без изменения context pipeline logic (логика проверки контекста).

## Preconditions
- `reports/m33-p0-stabilization-findings-intake.md`: PASS
- `reports/m33-context-status-mapping.md`: PASS
- `reports/m33-context-required-gate-implementation.md`: PASS
- `reports/m33-tui-blocked-rendering-inspection.md`: PASS
- `Files Allowed for 33.5.1` present: PASS
- `NO_EXISTING_TUI_RENDERING_FILE_FOUND` не содержится в секции `Files Allowed for 33.5.1`: PASS

## Inspection Report Used
- `reports/m33-tui-blocked-rendering-inspection.md`

## Files Allowed by 33.5.0
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

## Files Modified
- scripts/agentos-status.py
- scripts/renderers/plain_status_renderer.py
- scripts/renderers/rich_status_renderer.py

## Rendering Behavior Implemented
Добавлено явное человекочитаемое поведение для blocked/review статусов:
- выводится понятная причина, что Context Pack (контекстный пакет) отсутствует/пустой/невалидный/повреждён/неопределён;
- выводится явная блокировка выполнения;
- выводится безопасный следующий шаг;
- выводится явная граница: это объяснение, не approval (человеческое разрешение).

## Blocked States Rendered
Покрыт смысл для проблемных состояний:
- CONTEXT_PIPELINE_INVALID
- CONTEXT_REQUIRED_MISSING
- CONTEXT_REQUIRED_INVALID
- CONTEXT_GATE_BLOCKED
- STATUS_SOURCE_DAMAGED
- UNKNOWN
- missing Context Pack
- empty Context Pack
- Required Context: none
- CONTEXT_PIPELINE_REBUILD_FAILED
- CONTEXT_PIPELINE_VALIDATION_INCONCLUSIVE

## Forbidden Renderings Checked
Проверено, что пользовательский вывод не трактует проблемный контекст как success:
- UNKNOWN как success: запрещено
- STATUS_SOURCE_DAMAGED как success: запрещено
- READY/PASS/OK при invalid/missing/empty context: запрещено
- "execution allowed" при блокировке: запрещено

## User-Facing Text Added
Добавлены фразы в слой вывода:
- `Execution is blocked.`
- `Reason: Context Pack is missing, empty, invalid, damaged, or inconclusive.`
- `Next safe action: inspect or repair context pipeline in a separate scoped task.`
- для review-сценария: `Execution must not continue until context evidence is reviewed.`
- пояснение границы: `Status output explains only. It does not approve or authorize execution.`
- пояснение границы в TUI-renderer: `TUI explains. TUI does not approve or authorize execution.`

## Tutor / Human Explanation Boundary
- TUI explains.
- TUI does not approve.
- TUI does not authorize execution.
- TUI does not replace human gate.

## Tests / Fixtures Updated
- Не обновлялись в этой задаче.

## Validation Evidence
Запущено:
- `python3 scripts/agentos-status.py || true`
- `python3 scripts/check-context-pipeline.py || true`
- `bash scripts/run-all.sh || true`

Наблюдения:
- `agentos-status.py` показывает `AGENTOS_STATUS_BLOCKED` и новый ясный текст блокировки/причины/next safe action.
- `check-context-pipeline.py` -> `CONTEXT_PIPELINE_VIOLATION` (ожидаемо fail-closed).
- `run-all.sh` упал на несоответствии схемы `tasks/active-task.md` (вне области 33.5.1, не изменялось здесь).

## Known Gaps
- Не добавлены/не изменены негативные фикстуры по тексту рендеринга в рамках 33.5.1.
- Рекомендуется отдельная задача на фикстуры для текстовых гарантий (`BLOCKED/NEEDS_REVIEW` формулировки).

## Final Status
M33_TUI_BLOCKED_RENDERING_IMPLEMENTATION_COMPLETE
