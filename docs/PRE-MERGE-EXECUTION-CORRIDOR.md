---
type: corridor-index
module: m26-pre-merge-corridor
status: CORRIDOR_READY
task_id: 26.1.2
milestone: M26
---

# Pre-Merge Execution Corridor

## Purpose
Index-документ pre-merge corridor M26.
Определяет границы автономного выполнения агента
перед операциями merge/push.

## Safety Statements
CI PASS is not approval.
Evidence report is not approval.
Auto-merge is forbidden.
Automatic approval is forbidden.

## Corridor Components
| Документ | Назначение |
|----------|------------|
| AGENT-PERMISSION-MODEL.md | уровни разрешений агента |
| COMMAND-ALLOWLIST-POLICY.md | разрешённые команды |
| WRITE-ALLOWLIST-POLICY.md | разрешённые пути записи |
| NO-DIRECT-PUSH-POLICY.md | запрет прямого push |
| AGENT-VIOLATION-POLICY.md | нарушения и санкции |
| BOUNDED-RETRY-POLICY.md | ограничение повторов |
| HUMAN-APPROVAL-GATE.md | gates подтверждения |
| KNOWN-LIMITATIONS-M26.md | известные ограничения |

## Corridor Status
status: CORRIDOR_READY
enforcement: declarative (runtime в M27)
supersedes: M25-execution-controls
approved_by: owner-review-required
