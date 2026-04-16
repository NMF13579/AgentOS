# 🏗️ Архитектура фреймворка Vibe-coding-docs

---

## Схема слоёв и уровней

```text
Пользовательские уровни зрелости

Level 0  -> Быстрый старт (минимум документов)
Level 1  -> Стандартный MVP (структурированный процесс)
Level 2  -> Production MVP (расширенный контроль рисков)
Level 3  -> Поддержка и масштабирование

Слои документации

LAYER-1  -> Правила, протоколы, безопасность, поведение агента
LAYER-2  -> Продуктовые материалы: discovery, UX, specs, QA
LAYER-3  -> Память проекта: статус, уроки, инциденты, фиксы
```

---

## Поток данных и решений

```text
Задача
  ->
Интервью и уточнение контекста
  ->
Контракт и границы (scope/risk)
  ->
Работа агента
  ->
Проверка (self-verification + audit)
  ->
Результат и фиксация контекста
```

---

## Таблица компонентов

| Файл | Назначение | Для кого | Связь с другими |
|---|---|---|---|
| `README.md` | Главная навигация по системе | Все роли | Ведёт в quick start, карту документов и ключевые модули |
| `ONBOARDING-WIZARD.md` | Пошаговый старт без терминала | Новичок/врач | Использует `QUICK-START.md`, `ROLLBACK.md`, `error-handling.md` |
| `QUICK-START.md` | Короткий GUI-старт | Новичок | Ссылается на onboarding и advanced setup |
| `ADVANCED-SETUP.md` | Глубокая настройка среды и интеграций | Продвинутый пользователь | Связан с `CLAUDE.md`, `.cursor/rules/` |
| `LAYER-1/system-prompt.md` | Базовое поведение агента | Архитектор/лид | Опирается на контракт, scope и security |
| `LAYER-1/agent-contract.md` | Правила ответственности и границ | Архитектор/лид | Связан с `scope-guard.md`, `task-protocol.md` |
| `LAYER-1/task-protocol.md` | Формат задач и уровни риска | Команда разработки | Получает риск-теги из интервью и решений |
| `LAYER-1/scope-guard.md` | Контроль границ задачи | Все роли | При нарушении отправляет в `ROLLBACK.md` |
| `LAYER-1/self-verification.md` | Превентивная проверка до выполнения | Агент/ревьюер | Дополняет `error-handling.md` |
| `LAYER-1/error-handling.md` | Реакция после ошибки | Агент/ревьюер | При неудаче активирует `ROLLBACK.md` |
| `LAYER-1/ROLLBACK.md` | Безопасный откат | Все роли | Связан с аудитом и инцидентами |
| `LEARNING-LOOP.md` | Обучение на инцидентах | Лид/команда | Использует `incidents/` и `audit-checklist.md` |
| `incidents/incident-template.md` | Структурированная запись инцидента | Лид/ревьюер | Влияет на обновление правил и чеклистов |
| `LAYER-3/project-status.md` | Текущее состояние проекта | Все роли | Читается на старте каждой сессии |
| `HANDOFF.md` | Передача контекста между сессиями | Все роли | Обязателен при завершении задачи |

---

## Ключевые документы по слоям

### LAYER-1 (правила и контроль)
- [`workflow.md`](./LAYER-1/workflow.md)
- [`agent-contract.md`](./LAYER-1/agent-contract.md)
- [`scope-guard.md`](./LAYER-1/scope-guard.md)
- [`security.md`](./LAYER-1/security.md)
- [`self-verification.md`](./LAYER-1/self-verification.md)

### LAYER-2 (продукт и UX)
- [`project-interview.md`](./LAYER-2/discovery/project-interview.md)
- [`roadmap.md`](./LAYER-2/specs/roadmap.md)
- [`validation.md`](./LAYER-2/specs/validation.md)
- [`UX-DESIGN-GUIDE.md`](./LAYER-2/ux/UX-DESIGN-GUIDE.md)

### LAYER-3 (память и улучшения)
- [`project-status.md`](./LAYER-3/project-status.md)
- [`lessons.md`](./LAYER-3/lessons.md)
- [`fixes.md`](./LAYER-3/fixes.md)
