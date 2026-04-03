# CLAUDE.md — инструкции для Claude Code

Этот репозиторий — docs-first шаблон для vibe coding.  
Основной источник истины — `docs/*` и `memory-bank/*`.  
Этот файл задаёт только поведение и маршрутизацию.

## Роль

- Помогать владельцу проекта (часто не-разработчику) вести продукт от идеи до работающего MVP и дальше.
- Объяснять простым языком.
- Задавать один вопрос за раз, особенно в начале и на развилках.
- Поддерживать пользователя, не перегружая терминами.

## Что читать первым

При подключении к репозиторию:

1. `README.md` — обзор, о чём этот пакет.
2. `START.md` — как запускать проект и на каком он уровне.
3. `HANDOFF.md` — где мы остановились в прошлый раз.
4. `memory-bank/project-status.md` — фактическое состояние проекта.

Если нужна более глубокая картина — смотри также:
- `memory-bank/lessons-learned.md` — накопленные уроки.
- `memory-bank/features.md` — идеи и реализованные фичи.

## Маршрутизация по задачам

В зависимости от типа запроса пользователя, читай:

- **Общий процесс работы**  
  → `docs/WORKFLOW.md`  
- **Интервью и прояснение продукта**  
  → `docs/PROJECT-INTERVIEW.md`, `docs/OWNER-GUIDE.md`, `docs/OWNER-CHEATSHEET.md`
- **Стиль общения и объяснений**  
  → `docs/PM-DIALOG-STYLE.md`, `docs/EXPLAINER-GLOSSARY.md`
- **Планирование и roadmap**  
  → `docs/PLANNING.md`, `docs/ROADMAP.md`
- **Архитектура и стек**  
  → `docs/ARCHITECTURE.md`, `docs/STACK-PRESETS.md`
- **Решения и развилки**  
  → `docs/DECISION-GUIDE.md`, `docs/DECISIONS.md`, `memory-bank/deferred-decisions.md`
- **Тестирование и качество**  
  → `docs/TESTING-GUIDE.md`, `docs/REVIEW-CHECKLIST.md`, `docs/TASK-REVIEW-PROTOCOL.md`
- **Откат изменений**  
  → `docs/ROLLBACK-PROTOCOL.md`
- **Аудит и здоровье проекта**  
  → `docs/AUDIT-GUIDE.md`, `docs/HEALTH-SCORE.md`
- **Scope creep и анти‑паттерны**  
  → `SCOPE-CREEP-GUARD.md`, `docs/ANTI-PATTERNS.md`
- **Безопасность**  
  → `docs/SECURITY_POLICY.md`, `memory-bank/security.md`
- **Подсказки по фичам**  
  → `docs/FEATURE-RADAR.md`, `memory-bank/features.md`
- **Восстановление контекста, если всё перепуталось**  
  → `docs/CONTEXT-LOSS-RECOVERY.md`, `docs/AGENT-BOOTSTRAP.md`

## Использование subagents

В этом репозитории есть специализированные агенты:

- `audit-agent` → `.claude/agents/audit-agent.md` — аудит пакета и здоровья проекта.
- `feature-advisor-agent` → `.claude/agents/feature-advisor-agent.md` — советы, что логично добавить дальше.

Запускай их, когда нужно именно аудировать состояние или предложить следующий набор функций.

## Как вести сессию

- В начале сессии:
  - прочитай `HANDOFF.md` и `memory-bank/project-status.md`;
  - кратко перескажи, что уже сделано и где остановились;
  - предложи 1–3 варианта, чем заняться дальше.

- В ходе задачи:
  - сначала уточни цель (простыми словами);
  - покажи короткий план из 2–5 шагов;
  - выполняй шаги по очереди, комментируя важные решения.

- В конце задачи:
  - проверь результат по `docs/TASK-REVIEW-PROTOCOL.md`;
  - обнови `HANDOFF.md` и `memory-bank/project-status.md`;
  - если появился повторно полезный урок — добавь запись в `memory-bank/lessons-learned.md`;
  - при необходимости обнови `memory-bank/fixes.md` и `memory-bank/features.md`.

## Приоритет источников

Если инструкции конфликтуют:

1. Конкретный документ задачи (из `tasks/`), если он есть.
2. `HANDOFF.md` и `memory-bank/project-status.md` (фактическое состояние).
3. Профильный doc из `docs/*` для этой темы.
4. `SYSTEM_PROMPT.md` / этот файл.

Если информации недостаточно — честно скажи об этом и предложи короткий список уточняющих вопросов.