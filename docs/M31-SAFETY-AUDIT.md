# M31 Safety Audit (31.8)

## Что проверяет аудит
`audit-m31-tui-tutor.py` проверяет:
- наличие обязательных M31 файлов;
- языковую безопасность простого текста;
- границы рендеров;
- границы dashboard;
- fail-closed поведение.

## Что не проверяет
- не даёт approval;
- не доказывает production security;
- не запускает dangerous действия.

## Результаты
- `M31_SAFETY_PASS`
- `M31_SAFETY_PASS_WITH_WARNINGS`
- `M31_SAFETY_FAIL`
- `M31_SAFETY_NEEDS_REVIEW`

## Exit codes
- PASS / PASS_WITH_WARNINGS => 0
- FAIL / NEEDS_REVIEW => 1
- usage error => 2
- `--strict`: только PASS => 0

## JSON контракт
Возвращает:
- `result`
- `sections[]`
- `warnings[]`
- `errors[]`

## Safety boundary
Audit is not approval.
Passing audit is not proof of production security.
