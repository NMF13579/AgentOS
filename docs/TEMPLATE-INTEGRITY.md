# TEMPLATE-INTEGRITY

## Purpose
Документ описывает read-only проверку целостности шаблонов и формат её результатов.

Template integrity PASS does not mark AgentOS as MVP-ready.

## Template Targets
Проверяются пути:
- `templates/agentos-minimal/`
- `templates/agentos-full/`

## Minimal Template Contract
Если `templates/agentos-minimal/` существует, обязательны:
- `README.md`
- `requirements.txt`
- `scripts/run-all.sh`
- `templates/task.md`
- `templates/verification.md`

Проверяются:
- наличие обязательных путей;
- пустые обязательные файлы (это FAIL);
- содержимое `templates/task.md`: `task`, `goal`, `acceptance`;
- содержимое `templates/verification.md`: `verification`, `result`, `evidence`.

## Full Template Contract
Если `templates/agentos-full/` существует, обязательны:
- `README.md`
- `requirements.txt`
- `scripts/run-all.sh`
- `templates/task.md`
- `templates/verification.md`
- `docs/architecture.md`
- `docs/guardrails.md`
- `docs/limitations.md`
- `docs/troubleshooting.md`
- `examples/`

Проверяются:
- наличие обязательных путей;
- пустые обязательные файлы (это FAIL);
- содержимое `templates/task.md`: `task`, `goal`, `acceptance`;
- содержимое `templates/verification.md`: `verification`, `result`, `evidence`.

## Full-Only Paths
В minimal шаблоне запрещены full-only пути:
- `examples/`
- `prompts/`
- `docs/architecture.md`
- `docs/troubleshooting.md`
- `docs/limitations.md`

## Result Vocabulary
Допустимые результаты:
- PASS
- WARN
- FAIL
- NOT_IMPLEMENTED
- ERROR

NOT_IMPLEMENTED is not PASS.
WARN is not PASS.
FAIL is not PASS.
ERROR is not PASS.

## Output Markers
Текстовый режим всегда печатает:
- `TEMPLATE_INTEGRITY_CHECK: run`
- `TEMPLATE_INTEGRITY_RESULT: <PASS|WARN|FAIL|NOT_IMPLEMENTED|ERROR>`
- `TEMPLATE_INTEGRITY_CHECKS_RUN: <integer>`
- `TEMPLATE_INTEGRITY_CHECKS_PASSED: <integer>`
- `TEMPLATE_INTEGRITY_CHECKS_WARNED: <integer>`
- `TEMPLATE_INTEGRITY_CHECKS_FAILED: <integer>`
- `TEMPLATE_INTEGRITY_REASON: <short reason>`

## Exit Code Semantics
- default mode: exit 0 для PASS, WARN, NOT_IMPLEMENTED; non-zero для FAIL, ERROR.
- strict mode (`--strict`): exit 0 только для PASS; иначе non-zero.

Важно: exit 0 не равен PASS. Нужно читать `TEMPLATE_INTEGRITY_RESULT`.

## Root Selection
Опция `--root <path>` меняет только проверяемый корень.
`--root` changes only the inspected root and must not create files.

## Error Handling
Скрипт обёрнут в top-level exception handler.
Если возникает неожиданная ошибка:
- в text mode печатается `TEMPLATE_INTEGRITY_RESULT: ERROR`;
- в json mode печатается `"result": "ERROR"`;
- код выхода non-zero.

A traceback without TEMPLATE_INTEGRITY_RESULT: ERROR is invalid output.

## Read-Only Boundary
The checker is read-only.
Он не создаёт, не изменяет и не удаляет файлы.
The checker must not create missing templates.

## Relationship to Release Readiness
Проверка template integrity поддерживает release readiness, но не заменяет её.
The checker supports future install smoke but does not replace it.
Шаблонная проверка не отменяет safety gates M19/M20.

## Non-Goals
- Не создавать `templates/agentos-minimal/`.
- Не создавать `templates/agentos-full/`.
- Не внедрять install smoke.
- Не внедрять example smoke.
- Не внедрять release automation.
- Не определять завершение M20.
- Не объявлять AgentOS MVP-ready.
