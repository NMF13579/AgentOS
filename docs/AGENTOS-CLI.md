# AgentOS CLI Wrapper (31.10)

## Что делает
`scripts/agentos.py` — тонкая обёртка для удобных команд M31.

Маршрутизация:
- `agentos` / `agentos dashboard` -> `agentos-tui.py`
- `agentos status` -> `agentos-status.py`
- `agentos why` -> `agentos-explain.py`
- `agentos next` -> `agentos-next-step.py`
- `agentos log` -> read-only summary
- `agentos help` -> help

## Что не делает
- не решает статус;
- не выполняет next step;
- не создаёт approval;
- не меняет состояние.

## Разрешённые команды
- agentos
- agentos dashboard
- agentos status
- agentos why
- agentos next
- agentos log
- agentos help

## Запрещённые команды
- fix/go/approve/ready/commit/push/merge/promote/run/execute

## Pass-through флаги
Разрешены только безопасные флаги downstream-скриптов (`--json`, `--ascii`, `--no-color`, `--details`, и т.п.).

Запрещённые флаги:
`--approve`, `--ready`, `--fix`, `--go`, `--execute`, `--commit`, `--push`, `--merge`, `--promote`, `--force`, `--write-protected`.

## Exit codes
- 0: успех/help
- 1: forbidden command/flag, missing downstream script, downstream error
- 2: unknown command

## agentos log
Ограничен корнем репозитория и папкой `reports/`.
Не сканирует произвольные файлы вне репозитория.

## Boundary
- `agentos next` — подсказка, не выполнение.
- `agentos why` — объяснение, не approval.
- `agentos dashboard` — показ, не управление.
- snapshot остаётся явным действием downstream, и это не approval.

Командные "чипы" (если показываются в UI) — только текстовые подсказки, не кнопки.
