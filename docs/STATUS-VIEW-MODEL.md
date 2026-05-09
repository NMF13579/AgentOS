# Status View Model (M31.3)

## Что делает
`scripts/agentos-view-model.py` берёт:
- машинный статус из `agentos-status.py --json`;
- смысл/тексты из `data/explanations/status-vocabulary.yml`.

И собирает единый JSON для отображения.

## Что не делает
- не решает статус вместо агрегатора;
- не выполняет команды;
- не создаёт approval;
- не меняет файлы.

## Ключевое правило
Machine-state берётся из агрегатора.
Display-meaning берётся из vocabulary.

## Mapping
- `title` ← `simple_ru.title`
- `summary` ← `simple_ru.what_happened`
- `why` ← `simple_ru.why_it_matters`
- `next_safe_steps` ← vocabulary
- `next_safe_step` ← первый элемент `next_safe_steps`
- `blocked_actions` ← vocabulary
- `rendering` ← renderer_hints

## Fail-Closed
Если что-то критично отсутствует:
- UNKNOWN
- SYSTEM_BLOCKED
- `is_ready = false`

UNKNOWN is not OK.

## Консистентность
Если severity/authority в словаре и агрегаторе расходятся:
- агрегатор выигрывает для текущего запуска;
- добавляется warning `VOCABULARY_STATUS_MISMATCH`.

## CLI
- `python3 scripts/agentos-view-model.py`
- `python3 scripts/agentos-view-model.py --json`
- `python3 scripts/agentos-view-model.py --status CONTEXT_PIPELINE_NEEDS_REVIEW`
- `python3 scripts/agentos-view-model.py --from-status-json <path>`
- `python3 scripts/agentos-view-model.py --validate-only`

## Boundary
View Model is not approval.
View Model is not proof by itself.
Renderer must consume View Model, not raw reports.
