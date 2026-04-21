<!-- ROLE: REFERENCE -->
<!-- AUTHORITY: SECONDARY -->
<!-- STATUS: ACTIVE -->
<!-- UPDATED_BY: owner -->
<!-- SOURCE_OF_TRUTH: no -->
<!-- MUST_NOT_CONTAIN: runtime state, policy rules, routing logic -->

# DECISIONS

Этот файл фиксирует архитектурные решения системы.
Цель: предотвратить повторные обсуждения закрытых вопросов.
Агент должен проверять этот файл перед предложением изменений,
если изменения затрагивают архитектуру или governance.

---

## Формат записи

## Decision: [короткое имя]
Date: YYYY-MM-DD
Status: active | deprecated
### Context
Почему возникла задача
### Decision
Что выбрали и почему
### Alternatives rejected
Что отвергли и почему
### Consequences
Что это меняет в системе
### Links
Связанные файлы

---

## Success metrics
- DECISIONS.md используется как справочник прошлых решений
- повторных предложений по закрытым решениям без проверки DECISIONS.md: 0
- архитектурные изменения при необходимости фиксируются здесь

---

## Recorded decisions

## ADR-001 — Canonical bootstrap: llms.txt как единственный entrypoint
**Дата:** see HANDOFF.md
**Решение:** единственная точка входа — llms.txt; все адаптеры только redirect
**Причина:** исключить competing entry surfaces и platform drift
**Статус:** ACTIVE
## ADR-002 — State authority: STATE.md = formal state canon
**Дата:** see HANDOFF.md
**Решение:** STATE.md — единственный canonical source of truth для состояния; HANDOFF.md — вторичный session context
**Причина:** предотвратить state scatter по файлам
**Статус:** ACTIVE
## ADR-003 — Adapter model: dumb adapters, no logic
**Дата:** see HANDOFF.md
**Решение:** адаптеры содержат только redirect к llms.txt, без правил и логики
**Причина:** логика в адаптерах = неуправляемое и непроверяемое поведение
**Статус:** ACTIVE
## ADR-004 — Bootstrap limit ≤ 7 файлов
**Дата:** see HANDOFF.md
**Решение:** required at every start = STATE.md, HANDOFF.md, agent-rules.md + task file (conditional); итого ≤ 7
**Причина:** предотвратить context overload при старте агента
**Статус:** ACTIVE
## ADR-005 — Doc-integrity CI layer
**Дата:** 2026-04-20
**Решение:** автоматическая проверка структуры через .github/workflows/doc-integrity.yml
**Причина:** drift нельзя надёжно поймать вручную
**Статус:** ACTIVE
