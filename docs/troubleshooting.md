# Troubleshooting

## Purpose
Руководство по безопасной интерпретации типовых сбоев и неоднозначных результатов.

## How to Read Gate Failures
Сначала смотрите gate-маркеры и их результат, потом причину, затем доказательства.

## Missing Required Marker
symptom: missing GATE_RESULT
likely cause: скрипт вывел неполный набор обязательных маркеров
correct interpretation: проверка не может считаться PASS
safe next step: повторить запуск и проверить полный marker output

symptom: missing TEMPLATE_INTEGRITY_RESULT
likely cause: неполный/некорректный вывод checker-а
correct interpretation: template integrity не подтверждён
safe next step: запустить checker заново и получить parseable output

## NOT_RUN Result
symptom: NOT_RUN treated as PASS
likely cause: результат интерпретирован как «не критично»
correct interpretation: обязательный этап не пройден
safe next step: выполнить обязательный этап и зафиксировать результат

## ERROR Result
symptom: ERROR treated as PASS
likely cause: технический сбой ошибочно принят за успешный контроль
correct interpretation: проверка провалена
safe next step: устранить ошибку выполнения и повторить проверку

## BLOCKED Result
symptom: BLOCKED результат на критическом gate
likely cause: policy/preconditions/approval boundary сработал корректно
correct interpretation: это защитная блокировка, не успешное прохождение
safe next step: устранить причину блокировки, не обходя gate

## Template Integrity Failure
symptom: one template exists but the other does not
likely cause: неполный набор template targets
correct interpretation: integrity FAIL
safe next step: выровнять структуру или явно оставить NOT_IMPLEMENTED

symptom: minimal template contains full-only path
likely cause: minimal/full контракты смешаны
correct interpretation: integrity FAIL
safe next step: убрать full-only path из minimal

## Release Checklist Failure
symptom: release checklist has NOT_IMPLEMENTED items
likely cause: часть scope ещё не реализована
correct interpretation: NOT_IMPLEMENTED не равен PASS
safe next step: зафиксировать ограничения и не повышать статус автоматически

## Optional Validation Missing
symptom: optional M19 smoke or audit unavailable
likely cause: отсутствуют артефакты или среда запуска
correct interpretation: optional check не подтверждён
safe next step: отметить ограничение и эскалировать в review при влиянии на решение

## Traceback or Usage Error
symptom: usage error treated as enforcement PASS
likely cause: общий CLI-сбой принят как валидный результат
correct interpretation: это не подтверждённый PASS
safe next step: исправить вызов команды и получить валидные маркеры

A traceback is not a valid gate result.
A usage error is not a valid enforcement PASS.
Missing markers are not PASS.

## When to Use NEEDS_REVIEW
symptom: противоречивые или неполные результаты readiness
likely cause: доказательства неполные или конфликтуют между собой
correct interpretation: автоматического вывода недостаточно
safe next step: safe next step for unclear readiness is NEEDS_REVIEW

## Non-Goals
- Не объявлять итоговую готовность MVP.
- Не заменять completion review промежуточными выводами.
