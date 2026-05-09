# Next Safe Step (M31.5)

## Что делает
`agentos-next-step.py` показывает следующий безопасный шаг по данным View Model.

## Что не делает
- не запускает этот шаг;
- не создаёт approval;
- не меняет статус;
- не меняет файлы.

## Приоритет данных
- primary: `next_safe_steps` из View Model;
- fallback: `next_safe_step`.

Если поля расходятся: warning `NEXT_STEP_FIELD_MISMATCH`.

## selected_step vs all_steps
- `selected_step`: первый безопасный шаг;
- `all_steps`: полный список безопасных шагов.

`safe_to_execute_by_m31` всегда `false`.

## does_not_authorize
Всегда непустой список, минимум:
- approval
- mark ready
- commit
- push
- merge
- protected write
- state change
- Human Gate approval
- owner approval

## Safety
Запрещённые глаголы/типы шага приводят к fail-closed (`UNSAFE_NEXT_STEP`).

## UNKNOWN
UNKNOWN is not OK.
При UNKNOWN нормальное продолжение не показывается как безопасное.

## validate-safety
- `--validate-safety` выполняет только статические проверки.
- По умолчанию печатает одну строку результата.
- С `--json` отдаёт JSON с `result/warnings/errors`.

## Boundary
Next safe step is guidance, not execution.
Human Gate display is not approval.
