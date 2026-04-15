# AGENTS.md — точка входа для OpenCode

Этот файл читается OpenCode автоматически при старте сессии.

## Агент, читай в таком порядке

1. [`CLAUDE.md`](CLAUDE.md) — основной контракт сессии (правила, стиль, ограничения).
2. [`llms.txt`](llms.txt) — карта репозитория, навигация по файлам.
3. [`LAYER-1/tools/adapters/OPENCODE-INTERVIEW-CONTROL.md`](LAYER-1/tools/adapters/OPENCODE-INTERVIEW-CONTROL.md) — адаптер интервью-протокола.

## Быстрый старт

Скажи агенту **«Начнём»** — он прочтёт `CLAUDE.md` и запустит интервью по [`LAYER-2/discovery/project-interview.md`](LAYER-2/discovery/project-interview.md).
