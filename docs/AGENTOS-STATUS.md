# AgentOS Status Aggregator (M31.2)

## Что делает
`scripts/agentos-status.py` читает готовые источники статуса и собирает единый JSON статуса AgentOS.

## Что не делает
- не рисует dashboard;
- не объясняет “почему” в режиме Tutor;
- не выполняет команды;
- не создаёт approval;
- не меняет защищённые файлы.

## Критичные источники
- `data/explanations/status-vocabulary.yml`
- статус M30 (предпочтительно `reports/context-pipeline.json`, fallback: markdown)

## Fail-Closed поведение
Если источник отсутствует/повреждён/непонятен:
- статус не может стать OK;
- `overall_status` уходит в UNKNOWN или NEEDS_REVIEW;
- `authority` становится `SYSTEM_BLOCKED` при критической неопределённости.

UNKNOWN is not OK.

## JSON контракт
Скрипт отдаёт:
- `overall_status`, `top_status_code`, `severity`, `authority`
- `is_ready`, `is_blocked`, `is_unknown`
- `sources`, `missing_sources`, `damaged_sources`, `stale_sources`
- `warnings`, `errors`, `summary`

## Source Conflict/Fallback
- machine-readable JSON источник приоритетнее markdown fallback.
- если preferred source повреждён, это не считается "OK по fallback".
- malformed markdown fallback = damaged, не missing.

## Freshness
- По умолчанию порог устаревания: 300 секунд.
- stale критичный источник не должен давать OK.

## Snapshot
`--snapshot` пишет снимок только по явному запросу.
Снимок не является approval.

## CLI
- `python3 scripts/agentos-status.py`
- `python3 scripts/agentos-status.py --json`
- `python3 scripts/agentos-status.py --strict`
- `python3 scripts/agentos-status.py --ascii`
- `python3 scripts/agentos-status.py --no-color`
- `python3 scripts/agentos-status.py --snapshot reports/status-snapshot.md`

## Границы
- Вывод статуса не равен approval.
- Скрипт агрегирует и сообщает состояние, а не разрешает действия.
- Будущий View Model builder должен читать этот JSON.
- Будущие рендереры должны читать View Model, а не внутренности агрегатора.
