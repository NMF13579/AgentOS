---
type: protocol
module: m26-pre-merge-corridor
status: active
task_id: 26.9.2
milestone: M26
---

# Human Approval Gate Protocol

## Purpose

Определяет точки обязательного подтверждения человеком
перед выполнением критических операций агентом.

## Gate Types

GATE-1: Pre-Merge Gate
trigger: агент готовится выполнить git merge или PR
required_action: человек проверяет pre-merge checklist
timeout: нет (агент ждёт бессрочно)
bypass: запрещён

GATE-2: Scope Expansion Gate
trigger: агент обнаружил необходимость изменить файлы вне allowlist
required_action: человек явно добавляет путь в allowlist
timeout: нет
bypass: запрещён

GATE-3: Violation Recovery Gate
trigger: зафиксировано нарушение по AGENT-VIOLATION-POLICY.md
required_action: человек выбирает санкцию и подписывает violation record
timeout: нет
bypass: запрещён

GATE-4: Retry Limit Gate
trigger: агент достиг max_attempts по BOUNDED-RETRY-POLICY.md
required_action: человек решает продолжить, изменить задачу или остановить
timeout: нет
bypass: запрещён

## Gate Activation Checklist

[ ] агент явно объявил тип gate
[ ] агент остановил выполнение
[ ] человек получил уведомление
[ ] человек подтвердил или отклонил
[ ] решение зафиксировано в evidence report

## Integration

связан с: BOUNDED-RETRY-POLICY.md (GATE-4)
связан с: AGENT-VIOLATION-POLICY.md (GATE-3)
связан с: pre-merge-checklist.md (GATE-1)
аудит в: 26.13.1
