---
stage: 04-deploy
reads: project/PROJECT.md (specs + deploy минимум; discovery/ux по необходимости, без правок)
writes: project/PROJECT.md (только SECTION:deploy; DECISIONS для деплой-решений)
priority: scope-guard > agent-contract > local-doc > workflow
---

# Этап 04 — Деплой

## Твоя задача

Зафиксировать **окружение, домены, сервисы, процедуры выката** в разделе 4. DEPLOY, без изменения продуктовых и UX-решений в закрытых секциях.

## Что читать

1. `project/PROJECT.md`
2. `shared/agent-contract.md`
3. `shared/scope-guard.md`
4. `stages/04-deploy/deploy-guide.md`, `security.md`
5. Перед релизом: корневой [`../../CHECKLIST.md`](../../CHECKLIST.md)

## Обязательное правило

**Plan → Review → Confirm → Execute.** Особенно перед продакшеном — явное подтверждение плана и чеклиста.

## Правила записи

- Только `SECTION:deploy` и **DECISIONS**.
- Не правь discovery/ux/specs с `LOCKED:true` без решения владельца.
- Секреты в репозиторий не коммитить; указывать имена переменных и где хранить — см. `security.md`.

## Smoke-test (перед работой)

1. Среда: **Claude Code** (или фактическая).
2. Этап: **04-deploy**.
3. Запреты: не менять продуктовую спецификацию и UX; не раскрывать секреты.
4. Запись: только **DEPLOY** (+ **DECISIONS**).
