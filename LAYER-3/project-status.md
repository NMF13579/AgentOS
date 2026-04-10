# Project Status

> Updated: 2026-04-10 (Claude Code architecture + v0.3.0)

## Слои

- Discovery: 🟡 — артефакты в `LAYER-2/discovery/`; заполнять по интервью.
- Specs: 🟡 — `LAYER-2/specs/`; архитектура и решения ведутся по мере работы.
- UX: 🟡 — `LAYER-2/ux/` + чеклисты в `LAYER-1/ux-checklist-{core,accessibility,medical,interactions}.md`.
- QA: 🟡 — `LAYER-2/qa/` (сценарии, блокеры, post-launch).
- Deploy: 🟡 — `LAYER-1/deploy-guide.md` + `LAYER-1/tools/deploy/` + `LAYER-2/specs/deploy-config.md`.

## Текущий этап

Добавлен поток **Claude Code**: `project/PROJECT.md`, `stages/01-04` с `BOOT.md`, `shared/`, `README-NEW-ARCHITECTURE.md`, `CHECKLIST.md`. `CLAUDE.md` и `llms.txt` обновлены. CHANGELOG — **v0.3.0**. Аудит v1+v2 по-прежнему закрыт.

## Последнее действие (2026-04-10)

Архитектура Claude Code (единый PROJECT.md, этапные BOOT, shared):
- Новые каталоги: `project/`, `stages/`, `shared/`; переписан `CLAUDE.md`.
- `README.md`: ссылки на `navigation.md` заменены на `LAYER-1/tools/template-sync-index.md`.

Ранее — аудит v2 — доисправление после перепроверки:
- Исправлены 6 устаревших ссылок на `memory-bank/*` и `docs/*` в 4 файлах
- Добавлены 4 маршрута в `llms.txt` (testing-guide, decision-guide, owner, agent-bootstrap)
- Обновлён CHANGELOG.md → v0.2.1
- Исправлены ссылки `LAYER-1/navigation.md` → `LAYER-1/tools/template-sync-index.md` в agents.md

Аудит v1 (ранее):
- 8 битых ссылок в `project-interview.md`
- Удалена `docs/` (21 файл), перенесены 2 уникальных
- 5 маршрутов в `llms.txt`
- Embedded-дубли в architecture/decisions
- navigation.md → template-sync-index.md
- Удалены: SCOPE-CREEP-GUARD.md, opencode.json
- Ветка: `claude/audit-documentation-105k7`

См. также `LAYER-3/session-log.md` и `HANDOFF.md`.
