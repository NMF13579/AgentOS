# RELEASE-READINESS-AUDIT

## Purpose
Документ описывает read-only аудит готовности релиза для M20 и формат его результатов.

## Audit Scope
Аудит проверяет покрытие артефактов, запуск ключевых проверок и прозрачность статусов.

## Required Artifact Groups
- M20 contract/release artifacts
- M20 template integrity artifacts
- M20 documentation hardening artifacts
- M20 scenario artifacts
- M20 prompt pack artifacts
- M19 gate contract dependency artifacts

## Required Command Checks
- `python3 -m py_compile scripts/check-template-integrity.py`
- `python3 -m py_compile scripts/test-template-integrity-fixtures.py`
- `python3 scripts/check-template-integrity.py`
- `python3 scripts/test-template-integrity-fixtures.py`

## Optional M19 Checks
- `python3 scripts/test-unified-gate-smoke.py`
- `python3 scripts/audit-gate-contract.py`

## Result Vocabulary
Audit results:
- PASS
- WARN
- FAIL
- ERROR

Check statuses:
- PASS
- WARN
- FAIL
- NOT_RUN
- NOT_IMPLEMENTED
- ERROR

NOT_RUN is not PASS.
NOT_IMPLEMENTED is not PASS.
ERROR is not PASS.

## Output Markers
Text mode markers:
- `RELEASE_READINESS_AUDIT: run`
- `RELEASE_READINESS_AUDIT_RESULT: <PASS|WARN|FAIL|ERROR>`
- `RELEASE_READINESS_AUDIT_CHECKS_RUN: <integer>`
- `RELEASE_READINESS_AUDIT_CHECKS_PASSED: <integer>`
- `RELEASE_READINESS_AUDIT_CHECKS_WARNED: <integer>`
- `RELEASE_READINESS_AUDIT_CHECKS_FAILED: <integer>`
- `RELEASE_READINESS_AUDIT_CHECKS_NOT_RUN: <integer>`
- `RELEASE_READINESS_AUDIT_CHECKS_NOT_IMPLEMENTED: <integer>`
- `RELEASE_READINESS_AUDIT_REASON: <short reason>`
- `RELEASE_READINESS_AUDIT_CHECK: <check_name> <status> <reason>`

Boundary statements use RELEASE_READINESS_AUDIT_BOUNDARY.
RELEASE_READINESS_AUDIT_RESULT must appear exactly once in text output.

## JSON Output
`--json` mode возвращает валидный JSON с агрегатами и списком checks.
JSON mode не печатает text markers и boundary lines.

## Exit Code Semantics
- default mode: exit 0 only for PASS and WARN; non-zero for FAIL and ERROR
- strict mode: exit 0 only for PASS; non-zero for WARN, FAIL, ERROR

## Read-Only Boundary
The audit runner is read-only.
Runner пишет только в stdout и не изменяет файлы репозитория.

## Relationship to Stable MVP Contract
Аудит опирается на `docs/STABLE-MVP-RELEASE-READINESS.md`, но не заменяет контракт решения.
Release readiness audit PASS does not mark AgentOS as MVP-ready.
Release readiness audit WARN does not mark AgentOS as MVP-ready.

## Relationship to Release Checklist
Аудит использует release checklist как источник обязательных артефактов и проверок, но не подменяет completion review.

## Relationship to Completion Review
Final MVP readiness decision must come from Milestone 20 completion review.

## Non-Goals
- Не создавать release evidence report.
- Не создавать completion review.
- Не реализовывать install/example smoke.
- Не публиковать пакет.
- Не создавать git tags.
- Не объявлять AgentOS как MVP-ready.

A traceback is not valid audit output.
