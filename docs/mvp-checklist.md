# MVP Checklist

## Purpose
Этот документ задаёт перечень проверок для итоговой оценки readiness в M20.

## Relationship to Release Checklist
`docs/release-checklist.md` описывает release-процедуру и статусы, а этот документ фиксирует M20 MVP-проверки в одном месте.

## Relationship to Stable MVP Contract
Основание: `docs/STABLE-MVP-RELEASE-READINESS.md`.

## Required M20 Artifacts
- docs/STABLE-MVP-RELEASE-READINESS.md
- VERSION
- CHANGELOG.md
- docs/release-checklist.md
- templates/release-notes.md
- scripts/check-template-integrity.py
- docs/TEMPLATE-INTEGRITY.md
- scripts/test-template-integrity-fixtures.py
- tests/fixtures/template-integrity/
- docs/architecture.md
- docs/guardrails.md
- docs/limitations.md
- docs/troubleshooting.md
- docs/mvp-checklist.md

## Required Documentation
- Архитектура и границы AgentOS
- Guardrail boundaries
- Ограничения и non-goals
- Troubleshooting для типовых сбоев

## Required Packaging Checks
- VERSION и CHANGELOG присутствуют
- release checklist и release notes template присутствуют
- template integrity checker присутствует

## Required Validation Evidence
- Результаты ключевых валидаторов и regression checks
- Подтверждение, что safety boundary не нарушен

## Required Smoke Evidence
- Результаты unified gate smoke

## Required Audit Evidence
- Результаты gate contract audit

## Allowed Readiness Labels
- MVP_READY
- MVP_READY_WITH_WARNINGS
- MVP_NOT_READY
- NEEDS_REVIEW

## Blocking Conditions
- Провал обязательного safety gate
- Отсутствие обязательного артефакта
- Попытка трактовать NOT_RUN/ERROR как PASS

## Decision Boundary
This checklist does not mark AgentOS as MVP-ready.
Final MVP readiness decision must come from the Milestone 20 completion review.
Evidence collection is not the same as completion review.
Template integrity PASS does not mark AgentOS as MVP-ready.
Release notes do not determine final readiness.
No lower gate can override a higher safety gate.

## Non-Goals
- Не объявлять M20 завершённым.
- Не подменять completion review автоматически собранным evidence.
