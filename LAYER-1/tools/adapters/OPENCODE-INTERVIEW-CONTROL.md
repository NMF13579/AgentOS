> Trigger: интервью в OpenCode по `project-interview.md`  
> Read-time: ~3 min  
> Filled-by: agent  
> Needs-approval: no  
> Next: [`../../interview-system.md`](../../interview-system.md)

# OpenCode — дельта

Общее ядро: [**README.md**](./README.md#adapter-core).

## Когда

Интервью через OpenCode (CLI) по [`../../../LAYER-2/discovery/project-interview.md`](../../../LAYER-2/discovery/project-interview.md). Subagent «guardian» не обязателен — self-check.

## Дополнительно к ядру

- **Точка входа OpenCode:** при старте обычно читаются `AGENTS.md` в корне (если есть), затем [`CLAUDE.md`](../../../CLAUDE.md), при необходимости глобальный `~/.config/opencode/AGENTS.md`. В этом репозитории опорой остаётся **`CLAUDE.md`**.
- **CLI:** работа без GUI; при желании вынести стража в отдельного агента — `.opencode/agents/*.md` с ссылкой на [`../../interview-system.md`](../../interview-system.md).

## Журнал

[`../../../LAYER-3/interview-session.md`](../../../LAYER-3/interview-session.md) — `control-mode: opencode-self-check`.
