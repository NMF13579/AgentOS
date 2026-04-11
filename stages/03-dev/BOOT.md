---
stage: 03-dev
reads: project/PROJECT.md (discovery, ux, specs; deploy только чтение при необходимости)
writes: project/PROJECT.md (только SECTION:specs; DECISIONS для инженерных решений)
priority: scope-guard > agent-contract > local-doc > workflow
---

# Этап 03 — Разработка (SPECS)

## Твоя задача

Уточнить и поддерживать **стек, архитектуру, реализованные компоненты** в разделе 3. SPECS, опираясь на Discovery и UX, **не переписывая** их.

## Что читать

1. `project/PROJECT.md`
2. `shared/agent-contract.md`
3. `shared/task-protocol.md`
4. При необходимости: `stages/03-dev/stack-presets.md`, `anti-patterns.md`, `testing-guide.md`

## Обязательное правило

**Plan → Review → Confirm → Execute.** Код и крупные рефакторы — только после подтверждения. **Один запрос = одна задача.**

## Правила записи

- Пиши в `SECTION:specs` и в **DECISIONS** (каждое важное решение — дата + суть + почему).
- Не меняй `SECTION:discovery` и `SECTION:ux` при `LOCKED:true` без явного указания владельца.
- Неизвестно — `❓ НЕ ОПРЕДЕЛЕНО — …`.

## После крупных изменений

- Подними `version` в YAML `PROJECT.md`, обнови `updated`, при смене фокуса — `stage`.

## Smoke-test (перед работой)

1. Среда: **Claude Code** (или фактическая).
2. Этап: **03-dev**.
3. Запреты: не ломать locked discovery/ux/deploy; не расширять скоуп без согласования.
4. Запись: только **SPECS** (+ **DECISIONS**).

## ✅ Выход из этапа

Переход к этапу 04-deploy только если:
- [ ] `SECTION:specs` заполнен, нет полей `❓ НЕ ОПРЕДЕЛЕНО`
- [ ] Все ключевые архитектурные решения зафиксированы в `DECISIONS`
- [ ] `version` и `updated` в `PROJECT.md` подняты
- [ ] Владелец подтвердил: «Спеки готовы, переходим к деплою»
