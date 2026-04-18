> Trigger: первый заход в репозиторий, быстрые команды в чате  
> Read-time: ~3 min  
> Filled-by: agent  
> Needs-approval: no  
> Next: `START.md`, `llms.txt`, `LAYER-1/agent-rules.md`

# Рекомендуемый порядок чтения и триггеры по фразам

## Рекомендуемая цепочка при старте (ориентир)

1. `README.md` или `START.md` — в зависимости от того, что указано в карте для вашей среды.
2. `llms.txt` — маршруты.
3. `HANDOFF.md` и `LAYER-3/project-status.md` — контекст и статус.

Детали bootstrap и уровней — в `LAYER-1/agent-rules.md` и `LAYER-1/workflow.md`.

Перед реализацией: границы задачи — `LAYER-1/scope-guard.md`.  
Перед завершением задачи: `LAYER-1/self-verification.md`.

## Триггеры по фразам (намерение → документ)

| Намерение пользователя | Открыть / выполнить |
|------------------------|----------------------|
| Проверка перед отдачей ответа с кодом | `LAYER-1/self-verification.md` |
| Откат, ошибка после действий | `LAYER-1/error-handling.md`, раздел «Процедура отката» |
| Проверка выхода за скоуп | `LAYER-1/scope-guard.md` |
| Аудит документации / готовности | `LAYER-1/audit.md` (протокол и «Чеклист аудита») |

Основное поведение и контракт: `LAYER-1/system-prompt.md`, `LAYER-1/agent-rules.md`.  
При конфликте инструкций: `LAYER-1/instruction-priority.md` и `shared/priority-order.md`.

## Маршрут по типу задачи (ориентир)

- Старт проекта (новый или существующий код) → `llms.txt`, `LAYER-1/workflow.md` (этап 0), `LAYER-1/agent-rules.md`
- Продуктовое интервью → `LAYER-2/discovery/project-interview.md`, `LAYER-1/interview-system.md`, дельта среды в `LAYER-1/tools/adapters/README.md`
- Стиль общения → `LAYER-1/dialog-style.md`, `LAYER-1/glossary.md`
- Планирование → `LAYER-2/specs/planning.md`, `LAYER-2/specs/roadmap.md`
- Архитектура продукта → `LAYER-2/specs/architecture.md`, `LAYER-1/stack-presets.md`
- Ревью задачи → `LAYER-1/task-protocol.md`
- Аудит → `LAYER-1/audit.md` (протокол и раздел «Чеклист аудита»)
- Безопасность → `LAYER-1/security.md`, при необходимости `LAYER-3/security.md`
- Идеи продукт → `LAYER-1/feature-radar.md`, `LAYER-3/features.md`
- Путаница, потеря контекста → `LAYER-1/context-recovery.md`
