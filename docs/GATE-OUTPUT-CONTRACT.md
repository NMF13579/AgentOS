# GATE-OUTPUT-CONTRACT

## Purpose
Единый формат вывода для gate-скриптов.

## Text Output Contract
Обязательные строки:
- `<GATE_NAME>: run`
- `<GATE_NAME>_RESULT: <PASS|WARN|FAIL|ERROR>`
- `<GATE_NAME>_REASON: <short reason>`

Рекомендуемые счётчики:
- `<GATE_NAME>_CHECKS_RUN: <integer>`
- `<GATE_NAME>_CHECKS_PASSED: <integer>`
- `<GATE_NAME>_CHECKS_WARNED: <integer>`
- `<GATE_NAME>_CHECKS_FAILED: <integer>`

## JSON Output Contract
`--json` режим:
- только JSON
- без text markers
- поля: `result`, `reason`, `checks`

## Error Handling
При непойманной ошибке итог должен быть ERROR, без «тихого падения».
