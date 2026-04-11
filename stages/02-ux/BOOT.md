---
stage: 02-ux
reads: project/PROJECT.md (discovery + ux; остальное только для контекста, без правок)
writes: project/PROJECT.md (только SECTION:ux; DECISIONS при UX-решениях)
priority: scope-guard > agent-contract > local-doc > workflow
---

# Этап 02 — UX

## Твоя задача

Заполнить **раздел 2. UX** в `project/PROJECT.md` на основе зафиксированного Discovery, не переписывая Discovery.

## Что читать

1. `project/PROJECT.md` (секции 1–2 минимум)
2. `shared/agent-contract.md`
3. `stages/02-ux/ux-checklist-core.md` и при необходимости остальные чеклисты в этой папке

## Обязательное правило

**Plan → Review → Confirm → Execute:** план на русском → подтверждение → правки.

## Правила записи

- Пиши **только** в `SECTION:ux` и при необходимости в **DECISIONS**.
- **Не редактируй** `SECTION:discovery`, если там `LOCKED:true`, без явного решения владельца.
- Пробелы — только через `❓ НЕ ОПРЕДЕЛЕНО — …`.

## После завершения этапа

- По согласованию: `LOCKED:true` для `SECTION:ux`.
- Обнови YAML: `version`, `updated`, `stage: dev` (когда готовы к разработке).

## Smoke-test (перед работой)

1. Среда: **Claude Code** (или фактическая).
2. Этап: **02-ux**.
3. Запреты: не менять discovery/specs/deploy; не трогать `LOCKED:true`.
4. Запись: только **UX** в `project/PROJECT.md`.

Если discovery пустой или противоречивый — скажи явно; не заполняй UX «от себя».

## ✅ Выход из этапа

Переход к этапу 03-dev только если:
- [ ] `SECTION:ux` заполнен, нет полей `❓ НЕ ОПРЕДЕЛЕНО`
- [ ] UX-решения подтверждены владельцем и зафиксированы в `DECISIONS`
- [ ] `version` и `updated` в `PROJECT.md` подняты
- [ ] Владелец подтвердил: «UX готов, переходим к разработке»
