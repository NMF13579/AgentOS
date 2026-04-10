# HANDOFF — где мы остановились

> Этот файл нужен, чтобы следующая сессия (и человек, и AI) быстро поняли контекст.

## Что мы делали в последний раз (2026-04-10)

**Архитектура Claude Code (docs-first, один `PROJECT.md`):**

- Добавлены `project/PROJECT.md` (шаблон с секциями discovery / ux / specs / deploy / decisions, `LOCKED`, `❓ НЕ ОПРЕДЕЛЕНО`), `project/archive/`.
- Добавлены `stages/01-interview` … `04-deploy` с `BOOT.md` (reads/writes/priority/smoke-test) и тонкими указателями на `LAYER-*`.
- Добавлены `shared/` (README + agent-contract, scope-guard, task-protocol, workflow — сжато со ссылками на LAYER-1).
- Переписан `CLAUDE.md` под этот поток; `llms.txt` и `README.md` обновлены (маршруты + исправлены ссылки navigation → template-sync-index).
- Новые файлы: `README-NEW-ARCHITECTURE.md`, `CHECKLIST.md`. CHANGELOG → **v0.3.0**. Ветка: `cursor/claude-code-architecture-218a`.

**Ранее — полный аудит v2 — доисправление оставшихся проблем:**

- **Устаревшие ссылки (6 штук):** `memory-bank/*` и `docs/*` → актуальные пути LAYER-*/
  - `SYSTEM_PROMPT.md`: `memory-bank/project-status.md` → `LAYER-3/project-status.md`
  - `tasks/RELEASE-CHECKLIST.md`: `docs/user-flows.md` → `LAYER-2/ux/USER-FLOWS.md`, `memory-bank/project-status.md` → `LAYER-3/project-status.md`, `docs/ROADMAP.md` → `LAYER-2/specs/roadmap.md`
  - `LAYER-1/tools/deploy/ROLLBACK-PROTOCOL.md`: `memory-bank/fixes.md` → `LAYER-3/fixes.md`
  - `LAYER-1/agents.md`: `LAYER-1/navigation.md` → `LAYER-1/tools/template-sync-index.md` (все 6 вхождений)
- **llms.txt:** добавлены ещё 4 маршрута: `testing-guide`, `decision-guide`, `owner`, `agent-bootstrap`.
- **CHANGELOG.md:** добавлена запись v0.2.1 с полным списком изменений аудита.

**Ранее в этой сессии (аудит v1):**

- Исправлены 8 UPPERCASE-ссылок в `project-interview.md`.
- Удалена директория `docs/` (21 legacy-файл), перенесены 2 уникальных.
- Добавлены 5 маршрутов в `llms.txt`.
- Убраны embedded-дубли в `architecture.md` / `decisions.md`.
- Переименован `navigation.md` → `tools/template-sync-index.md`.
- Удалены: `SCOPE-CREEP-GUARD.md`, `opencode.json`.
- Добавлен платформенный контекст в `START.md` и `SYSTEM_PROMPT.md`.

## Что уже работает

- **Claude Code:** `CLAUDE.md` → `project/PROJECT.md` + `stages/*/BOOT.md` + `shared/`; обзор — `README-NEW-ARCHITECTURE.md`.
- Маршрут агента: `llms.txt` → `HANDOFF.md` → маршруты LAYER-1/LAYER-2 или этапы `stages/`.
- Интервью и страж: `LAYER-1/interview-system.md`, `LAYER-2/discovery/project-interview.md`, адаптеры в `LAYER-1/tools/adapters/`.

## Где мы остановились

Внедрена целевая структура под Claude Code (v0.3.0 в CHANGELOG). Шаблон LAYER-* сохранён; `shared/` и `stages/*` указывают на полные гайды.

## Следующий лучший шаг

1. **Прогон в Claude Code:** «Прочитай `stages/01-interview/BOOT.md`» на чистом форке шаблона.
2. **Опционально (этап C):** link-checker для markdown, шаблон weekly-summary, политика архива в `project/archive/`.
3. **START.md** — по-прежнему legacy для Lovable/Bolt; при желании синхронизировать первую строку с `README-NEW-ARCHITECTURE.md`.

## Риски и вопросы

- Внешние ссылки на старые пути `docs/*` / `memory-bank/*` вне репозитория могут отвалиться — при миграции проектов обновить ссылки вручную.
- `START.md` сохранён как legacy-файл для Lovable/Bolt — при желании можно удалить или перенести в LAYER-1/tools/.

## Применимые уроки

- Перед началом сессии: `LAYER-3/project-status.md`, `LAYER-3/lessons.md`, `LAYER-3/session-log.md`.
