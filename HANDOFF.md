<!-- ROLE: SESSION_CONTEXT -->
<!-- AUTHORITY: SECONDARY -->
<!-- STATUS: ACTIVE -->
<!-- UPDATED_BY: agent -->
<!-- SOURCE_OF_TRUTH: no -->
<!-- MUST_NOT_CONTAIN: formal state как canonical (см. LAYER-3/STATE.md), полная история сессий -->

# HANDOFF.md — Session Handoff Contract
<!-- Terminal Snapshot: перезаписывается агентом при каждом завершении сессии. -->
<!-- Session History: см. LAYER-3/session-log.md -->
<!-- Persistent Context: меняется редко, только при изменении архитектуры. -->
<!-- Историческое → CHANGELOG.md | Формальное состояние → LAYER-3/STATE.md -->

---

## Terminal Snapshot
<!-- Агент ПЕРЕЗАПИСЫВАЕТ этот блок при завершении каждой сессии -->

> ⚠️ HANDOFF.md не является источником состояния.
> Перед началом работы следуй **полному** перечню файлов из `llms.txt` (корень репозитория); там заданы `LAYER-3/STATE.md` (**PRIMARY**), этот файл (**SECONDARY** для контекста сессии) и остальное.

> **State (canonical):** см. `LAYER-3/STATE.md` — Project / Session / Task, `next_allowed_actions`, `forbidden`, `blockers`.

Last event (reference, не canonical): ITERATION_3_COMPLETED
Last transition (reference, не canonical): DEVELOPMENT → MAINTENANCE (2026-04-19)

Что сделано в последней сессии:
- Этап 5 (слепой проход): убраны конкурирующие списки bootstrap из `.cursor/rules/*.mdc`, `.cursor/CLAUDE-WORKFLOW.md`, `.github/copilot-instructions.md`, `.claude/agents/*.md` — единая отсылка к `llms.txt`; в `FAQ.md` добавлены кликабельные ссылки для цепочки восстановления контекста; адаптеры `AGENTS.md` / `CLAUDE.md` / `GEMINI.md` / `00-core.mdc` / `.windsurfrules` — единый metadata-блок.
- Этап 4 (стабилизация): в `ARCHITECTURE.md` — таблица папок и исправления State Control Plane; в `CHECKLIST.md` — Merge Gate; правки `CHANGELOG.md` (пометки [replaced by] / [deprecated]); аудит ссылок приоритета 1; единый путь к мед. UX — `LAYER-1/ux-checklist-medical.md` (регистр имён на диске).
- Этап 3 (Medical Safety): созданы `LAYER-1/MEDICAL-SAFETY.md`, полный UX в `LAYER-1/ux-checklist-medical.md`, `MEDICAL-ROLES-AND-PERMISSIONS.md`, `MEDICAL-DASHBOARDS.md`; обновлены `LEGAL-152FZ.md`, `security.md`, перекрёстные ссылки (`ux-checklist-core.md`, `START.md`, `agents.md`, LAYER-2 UX).
- Этап 2 (онбординг человека): в `README.md` Quick Start сведён к одной CTA на `START.md`, добавлены medical disclaimer и install policy (main vs dev); в `QUICK-START-NOVICE.md`, `QUICK-START.md`, `ONBOARDING-WIZARD.md` — вводные блоки «для кого»; таблица ролей и Docs Map в README ведут через `START.md`; шаблон промпта в `ONBOARDING-WIZARD.md` выровнен под `llms.txt`.
- Этап 1 (маршруты агента): канонический порядок чтения только в `llms.txt`; адаптеры (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.cursor/rules/00-core.mdc`, `.windsurfrules`) указывают на `llms.txt`, поведение — `LAYER-1/agent-rules.md`; `START.md`, `FAQ.md`, `LAYER-1/agents.md`, `LAYER-1/agent-rules.md` и `LAYER-1/tools/template-sync-index.md` согласованы; узкий аудит в `LAYER-1/audit.md` — точка входа `llms.txt` вместо `CLAUDE.md`.
- Миграция фаз 2–4: разведены STATE / HANDOFF / project-status; session-log append; state-aware + document governance audit в `audit.md`; `document-governance.md`; единый bootstrap в `agent-rules.md`.
- В `dev` влита ветка `cursor/handoff-three-zone-restructure-e7fa`: разрешены конфликты в
  `HANDOFF.md`, `LAYER-3/STATE.md`, `LAYER-3/project-status.md`, `memory-bank/project-status.md`.
- Сохранён формальный `LAYER-3/STATE.md` (MAINTENANCE, guards, Transition Log).
- История шаблона до state layer — в [`CHANGELOG.md`](./CHANGELOG.md) (`## [2026-04-19] Pre-state-layer history` и связанные секции).

Что должен сделать следующий агент первым шагом:
1. Прочитать `llms.txt` и выполнить шаги из `LAYER-1/agent-rules.md` (# SESSION LOAD) после загрузки файлов из списка.
2. Далее — по `LAYER-3/roadmap.md` и команде владельца (следующие этапы док-коррекции или TASK-001, если актуально).

Blockers (reference, не canonical): нет

---

## Session History
> Полный лог сессий: `LAYER-3/session-log.md`

---

## Persistent Context
<!-- Меняется только при изменении архитектуры или стека -->

Тип проекта: документационный фреймворк для AI-агентов (vibe coding)
Стек: Markdown, GitHub, агентные среды (Cursor, Claude Code, OpenCode)
Ключевые решения: LAYER-3/atomic-decisions.md
Архитектура: ARCHITECTURE.md
Критические зависимости: LAYER-1/ (28 файлов), LAYER-3/
Принцип: agent/IDE files — adapters only, вся логика — в LAYER-1/
