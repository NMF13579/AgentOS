---
stage: 01-interview
reads: project/PROJECT.md (все секции; фокус — discovery)
writes: project/PROJECT.md (только SECTION:discovery; DECISIONS при решениях)
priority: scope-guard > agent-contract > local-doc > workflow
---

# Этап 01 — Интервью (Discovery)

## Твоя задача

Собрать и зафиксировать продуктовый контекст в **разделе 1. DISCOVERY** в `project/PROJECT.md`, не ломая закрытые секции.

## Что читать

1. `project/PROJECT.md`
2. `shared/agent-contract.md`
3. `shared/scope-guard.md`
4. `stages/01-interview/interview-system.md` (маршрут к полным гайдам)

## Обязательное правило

**Plan → Review → Confirm → Execute:** сначала короткий план на русском языке. Жди подтверждения владельца. Только потом меняй файлы или пиши код.

## Правила записи

- Пиши **только** между `<!-- SECTION:discovery -->` и `<!-- END:discovery -->` и в **DECISIONS** при явных решениях.
- Не трогай секции с **`LOCKED:true`**.
- Если данных не хватает — оставляй или добавляй строку: `❓ НЕ ОПРЕДЕЛЕНО — что нужно уточнить` (не придумывай).

## После завершения этапа (по согласованию с владельцем)

- Установи в секции discovery: `LOCKED:true` (в комментарии `SECTION:discovery`).
- Обнови YAML в шапке `PROJECT.md`: `version`, `updated`, `stage: ux` (или оставь `interview`, пока UX не начат).

## Smoke-test (перед работой)

Перед первым изменением **явно назови** (в ответе владельцу):

1. Среду: **Claude Code** (или какая фактически открыта).
2. Текущий этап: **01-interview**.
3. Что нельзя: менять UX/SPECS/DEPLOY и `LOCKED:true`; не начинать без подтверждения плана.
4. Куда писать: только **DISCOVERY** в `project/PROJECT.md` (+ DECISIONS при необходимости).

Если файл или секция не найдены — скажи явно, не продолжай вслепую.

## ✅ Выход из этапа

Переход к этапу 02-ux только если:
- [ ] `SECTION:discovery` заполнен, нет полей `❓ НЕ ОПРЕДЕЛЕНО`
- [ ] Все ключевые решения зафиксированы в `DECISIONS`
- [ ] `version` и `updated` в `PROJECT.md` подняты
- [ ] Владелец подтвердил: «Дискавери готово, переходим к UX»
