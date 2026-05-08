# M27 Audit

## Purpose
Этот документ описывает полный аудит M27.
Он объединяет:
- проверку готовности Level 1 (обязательная часть),
- smoke-проверку Level 1 (быстрые контрольные проверки),
- проверку Level 2 (опциональная часть GitHub Platform Control).

## Two-Level Relationship
- Level 1 обязателен для завершения M27.
- Level 2 опционален и включается только владельцем/администратором репозитория.
- Если Level 2 выключен, валидный статус: `SKIPPED_LEVEL_2_NOT_ENABLED`.
- Выключенный Level 2 не должен ломать Level 1.

## Related Components
- `27.14.1`: `scripts/audit-m27-level1.py`
- `27.15.1`: `scripts/test-m27-level1-fixtures.py`
- `27.13.1`: `scripts/check-github-platform-enforcement.py`

## Script
- `scripts/audit-m27.py`

### CLI
```bash
python3 scripts/audit-m27.py
python3 scripts/audit-m27.py --root <repo-root>
python3 scripts/audit-m27.py --level-2-enabled false
python3 scripts/audit-m27.py --level-2-enabled true --platform-state <state-file>
python3 scripts/audit-m27.py --json
python3 scripts/audit-m27.py --explain
```

## Result Values
- `M27_LEVEL_1_READY_PLATFORM_OPTIONAL`
- `M27_LEVEL_2_PLATFORM_ENFORCED`
- `M27_LEVEL_1_NOT_READY`
- `M27_LEVEL_2_NEEDS_OWNER_ACTION`
- `M27_NEEDS_REVIEW`
- `M27_AUDIT_INVALID`

## Exit Semantics
- `M27_LEVEL_1_READY_PLATFORM_OPTIONAL` => exit `0`
- `M27_LEVEL_2_PLATFORM_ENFORCED` => exit `0`
- `M27_LEVEL_1_NOT_READY` => exit `1`
- `M27_LEVEL_2_NEEDS_OWNER_ACTION` => exit `1`
- `M27_NEEDS_REVIEW` => exit `1`
- `M27_AUDIT_INVALID` => exit `1`

## Evaluation Order
1. Разбор аргументов.
2. Определение корня репозитория.
3. Запуск `scripts/audit-m27-level1.py`.
4. Запуск `scripts/test-m27-level1-fixtures.py`.
5. Если любой из шагов Level 1 не пройден, итог: `M27_LEVEL_1_NOT_READY` или `M27_NEEDS_REVIEW`.
6. Проверка флага `--level-2-enabled`.
7. Если `false`, фиксируется `SKIPPED_LEVEL_2_NOT_ENABLED`.
8. Если `true`, запуск `scripts/check-github-platform-enforcement.py`.
9. Классификация статуса Level 2.
10. Выдача финального `M27_*` результата.

## Level 1 Behavior
- Отсутствует `scripts/audit-m27-level1.py` => `M27_LEVEL_1_NOT_READY`.
- Отсутствует `scripts/test-m27-level1-fixtures.py` => `M27_LEVEL_1_NOT_READY`.
- `LEVEL_1_NOT_READY` => `M27_LEVEL_1_NOT_READY`.
- `NEEDS_REVIEW` от Level 1 audit => `M27_NEEDS_REVIEW`.
- `LEVEL_1_SMOKE_FAIL` => `M27_LEVEL_1_NOT_READY`.
- `LEVEL_1_SMOKE_NEEDS_REVIEW` => `M27_NEEDS_REVIEW`.
- `...WITH_WARNINGS` допустимы для итогового готового статуса Level 1.

## Level 2 Behavior
- `--level-2-enabled false` => `SKIPPED_LEVEL_2_NOT_ENABLED`, и Level 1 может считаться готовым.
- `PLATFORM_ENFORCED` (при готовом Level 1) => `M27_LEVEL_2_PLATFORM_ENFORCED`.
- `PLATFORM_PARTIAL` / `NEEDS_OWNER_ACTION` / `PLATFORM_NOT_ENFORCED` => `M27_LEVEL_2_NEEDS_OWNER_ACTION`.
- `PLATFORM_CHECK_INVALID` => `M27_AUDIT_INVALID`.

## SKIPPED_LEVEL_2_NOT_ENABLED
- Это валидный статус для опционального Level 2.
- Он не означает platform enforced.
- Он не должен ломать Level 1 результат.

## Output Example
```text
RESULT: M27_LEVEL_1_READY_PLATFORM_OPTIONAL
REASON: Level 1 ready; Level 2 skipped
```

```text
RESULT: M27_LEVEL_2_NEEDS_OWNER_ACTION
REASON: Level 2 needs owner/admin action (PLATFORM_PARTIAL)
```

## Non-Authorization Clauses
- This audit is not approval.
- This audit does not authorize commit.
- This audit does not authorize push.
- This audit does not authorize merge.
- This audit does not authorize release.
- This audit does not override M25.
- This audit does not override M26.
- This audit does not override M27 runtime guards.
