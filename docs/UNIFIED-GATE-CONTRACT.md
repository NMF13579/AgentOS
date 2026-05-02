# UNIFIED-GATE-CONTRACT

## Purpose
Единый контракт формата для gate-проверок (gate = контрольный этап).

## Result Vocabulary
Допустимые итоговые статусы:
- PASS
- WARN
- FAIL
- ERROR

## Required Text Markers
Каждая gate-проверка в text mode должна печатать:
- `<GATE_NAME>: run`
- `<GATE_NAME>_RESULT: <PASS|WARN|FAIL|ERROR>`
- `<GATE_NAME>_REASON: <short reason>`

## Check Line Format
Детализация проверок должна идти строками вида:
- `<GATE_NAME>_CHECK: <check_name> <status> <reason>`

Где `<status>` может быть:
- PASS
- WARN
- FAIL
- NOT_RUN
- NOT_IMPLEMENTED
- ERROR

## JSON Mode
`--json` возвращает валидный JSON с итогом и списком checks.

## Exit Code Semantics
- default: exit 0 для PASS/WARN, non-zero для FAIL/ERROR
- strict: exit 0 только для PASS

## Boundary
PASS по gate-контракту не означает готовность продукта к релизу.
