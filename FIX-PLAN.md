---
# FIX-PLAN.md — Журнал исправлений по аудиту 2026-04

> Аудит проведён: 2026-04-17
> Источник: перекрёстный аудит (AI-архитект + внешний документ)
> Итоговая оценка до исправлений: 6.7/10

## ✅ Группа 1 — Критические (выполнено)
- [x] Удалён дубль `.cursor/rules/31-stage-routing.mdc`
- [x] Удалён дубль `.cursor/rules/32-document-priority.mdc`
- [x] Удалён дубль `.cursor/rules/33-scope-guard.mdc`
- [x] Обновлён `.cursor/rules/00-core.mdc` — добавлены канонические ссылки

## ✅ Группа 2 — Важные (выполнено)
- [x] Исправлена ссылка `shared/scope-guard.md` → `LAYER-1/scope-guard.md` в `CLAUDE.md`
- [x] Добавлена таблица выбора старта в `README.md`
- [x] Добавлена таблица поддерживаемых IDE в `README.md`
- [x] Добавлены 3 AI-специфичных анти-паттерна в `LAYER-1/anti-patterns.md`

## 🔲 Группа 3 — Желательные (в процессе)
- [x] Создан этот файл `FIX-PLAN.md`
- [ ] Синхронизированы названия этапов в stages/ и .cursor/rules/
- [ ] Расширен медицинский раздел в `LAYER-1/ux-checklist-core.md` (`# UX-CHECKLIST-MEDICAL.md`): офлайн-режим, HL7 FHIR, тайм-аут сессии

## 📋 Оставшиеся задачи (следующая итерация)
- Добавить Conflict Resolution Protocol в `LAYER-1/decision-guide.md`
- Добавить Rollback Plan в `LAYER-1/workflow.md`
- Углубить медицинскую специфику в `LAYER-1/interview-system.md`
---
