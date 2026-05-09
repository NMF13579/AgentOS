# AgentOS TUI (M31.7)

## Что делает
`agentos-tui.py` показывает компактный dashboard из готовых M31 JSON данных:
- status view model
- tutor explanation
- next safe step

## Что не делает
- не читает raw reports напрямую;
- не решает статус;
- не придумывает объяснение;
- не выполняет команды;
- не создаёт approval.

## Рендер
- по умолчанию пытается Rich;
- если Rich недоступен/упал: fallback в plain.

## Режимы
- `--json`
- `--ascii`
- `--no-color`
- `--snapshot [path]`

## Snapshot
Snapshot только по явному `--snapshot`.
Snapshot captures composed dashboard view, not raw report recomputation.
This dashboard snapshot is not approval.

## Важные правила
- UNKNOWN is not OK.
- Human Gate display is not approval.
- Dashboard summary only: полные детали остаются в `agentos why` и `agentos next --details/--all`.
