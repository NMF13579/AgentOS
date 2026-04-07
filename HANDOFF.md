# HANDOFF — где мы остановились

> Этот файл нужен, чтобы следующая сессия (и человек, и AI) быстро поняли контекст.

## Что мы делали в последний раз

- **Кросс-IDE контроль интервью (план Cross IDE Interview Guard):** единый `INTERVIEW-GUARDIAN.md` + обязательный self-check в Cursor/Copilot/Claude/Gemini через `docs/adapters/*`; stop-block при ❌; обновлены `INTERVIEWER.md`, `START.md`, `docs/PROJECT-INTERVIEW.md`, `.cursor/rules/10-communication.mdc`, `.github/copilot-instructions.md`, `CLAUDE.md`, `GEMINI.md`, `docs/DOCS-MAP.md`, `README-PLACEMENT.md`, шаблон `interview-session.md` (поле `control-mode`).
- **Выравнивание interview-документов (план Interview docs alignment):** единый канонический лог `memory-bank/interview-session.md`; `project-context-draft.md` — редирект; синхронизированы `docs/PROJECT-INTERVIEW.md` и `START.md` (журнал, этап 0 vs служебный лог, этапы 4–5 Level 1, пути VISION); уточнены `INTERVIEWER.md` / `INTERVIEW-GUARDIAN.md` (START как вход, резюме+«Правильно понимаю?», ссылка на «Команды-модули»); в `opencode.json` в prompt интервьюера добавлен `START.md`; обновлены `README-PLACEMENT.md`, `docs/DOCS-MAP.md`, `memory-bank/index-memory-bank.md`.
- Добавлен `README-PLACEMENT.md` в корень: зафиксирована структура размещения файлов интервью-агентов, связи между ними, правила для `opencode.json`, порядок запуска и рекомендации по модели guardian.
- Настроили инфраструктуру интервью-агентов для OpenCode:
  - добавлен `opencode.json` с секцией `agent.interviewer` и `agent.guardian`;
  - создан `INTERVIEWER.md` (протокол интервью + вызов `@guardian`);
  - создан `INTERVIEW-GUARDIAN.md` (inline-чеклист + вердикты ✅/⚠️/❌);
  - добавлен `memory-bank/interview-session.md` как файл накопления ответов.
- Привязки в prompts настроены к: `docs/PROJECT-INTERVIEW.md`, `AGENT-CONTRACT.md`, `HANDOFF.md`, `SCOPE-CREEP-GUARD.md`.

## Что уже работает

- В `docs/DEPLOY.md` есть явный выбор платформы деплоя (Timeweb Cloud / Vercel).
- В `docs/DEPLOY.md` убрана устаревшая пометка про «Vercel — в разработке».
- В `docs/DOCS-MAP.md` в разделе «Связь с Vibe-coding-docs» платформы оформлены таблицей (Timeweb Cloud / Vercel).
- В `docs/standards/UX-CHECKLIST-INDEX.md` добавлены три новые точки навигации: STARTER-FLOW, ONBOARDING, PERMISSIONS-AND-ACCESS.
- В `docs/AGENT-BOOTSTRAP.md` в чеклист добавлены `ANTI-PATTERNS.md` и `PM-DIALOG-STYLE.md`.
- В `docs/AGENTS.md` добавлено правило синхронизации с `docs/DOCS-MAP.md` и обновлена зона ответственности `Docs Agent`.

## Где мы остановились

- Базовая конфигурация готова; следующий шаг — тестовый запуск команды «@interviewer начни интервью» в OpenCode.

## Следующий лучший шаг

- Проверить живой прогон: 1-2 шага интервью и убедиться, что `@guardian` реально вызывается после каждого шага.
- Если всё ок — согласовать формат итоговой сводки интервью перед переносом в продуктовые документы.

## Риски и вопросы

- Риск №1: OpenCode может требовать дополнительный синтаксис для автоматического вызова subagent; при необходимости уточнить в локальной документации OpenCode.

## Применимые уроки

- Перед началом следующей сессии стоит посмотреть:
  - `memory-bank/project-status.md`
  - `memory-bank/lessons-learned.md`
  - `memory-bank/fixes.md` (если правили баги)
  - `memory-bank/features.md` (если проектировали функции)

## Заметки агента

- Все правки выполнялись в режиме «одно изменение → одно подтверждение».