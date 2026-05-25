---
type: cli-doc
milestone: M56
task: 56.6
title: Task Execution Readiness CLI
status: draft
authority: cli-documentation
created_for: M56
source_policy: docs/TASK-EXECUTION-READINESS-POLICY.md
source_output_contract: docs/TASK-EXECUTION-READINESS-OUTPUT-CONTRACT.md
execution_readiness_authorized: false
execution_authorized: false
execution_started: false
approval_created: false
lifecycle_mutation_authorized: false
m57_authorized: false
m57_started: false
---

## 1. Purpose
This document defines the M56 execution readiness CLI.
The CLI checks readiness signals only; it does not authorize execution.

## 2. Command
```bash
python3 scripts/check-execution-readiness.py --input PATH --preconditions PATH --active-task PATH --json
python3 scripts/check-execution-readiness.py --explain
```

## 3. Inputs
The CLI may inspect an active-task file only when --active-task is explicitly provided.
The CLI must not implicitly inspect tasks/active-task.md.

## 4. Read-Only Boundary
The CLI is read-only.
The CLI must not modify tasks/active-task.md.
The CLI must not modify tasks/queue/.
The CLI must not modify approvals/.
The CLI must not modify generated/.
The CLI must not create M57 artifacts.

## 5. Input Status Handling
EXECUTION_READINESS_INPUT_READY may allow readiness evaluation to continue.
EXECUTION_READINESS_INPUT_READY_WITH_LIMITATIONS may allow confirmed with limitations if no blockers exist.
EXECUTION_READINESS_INPUT_NOT_READY must return EXECUTION_READINESS_NOT_CONFIRMED.
EXECUTION_READINESS_INPUT_BLOCKED must return EXECUTION_READINESS_BLOCKED.
Unknown input status must return EXECUTION_READINESS_BLOCKED.
EXECUTION_READINESS_INPUT_READY_WITH_LIMITATIONS does not bypass active-task checks.
EXECUTION_READINESS_INPUT_READY_WITH_LIMITATIONS does not bypass preconditions checks.
Input limitations may contribute to EXECUTION_READINESS_CONFIRMED_WITH_LIMITATIONS only after active-task and preconditions checks pass without blockers.

## 6. Decision Priority
BLOCKED outranks NOT_CONFIRMED.
NOT_CONFIRMED outranks CONFIRMED_WITH_LIMITATIONS.
CONFIRMED_WITH_LIMITATIONS outranks CONFIRMED.

## 7. Decision Rules
Missing, malformed, unknown, contradictory, unsafe, or unverifiable state must return EXECUTION_READINESS_BLOCKED.
Empty required_traceability objects must be treated as missing traceability.
Empty required_boundaries objects must be treated as missing boundary markers.
Empty non_authority_markers arrays must be treated as missing boundary markers.
Active-task structural gaps must return EXECUTION_READINESS_NOT_CONFIRMED.
Warnings without blockers may return EXECUTION_READINESS_CONFIRMED_WITH_LIMITATIONS.
Clean readiness may return EXECUTION_READINESS_CONFIRMED.
Unknown keys must not improve result classification.
No CLI result authorizes execution.

## 8. Result Values
EXECUTION_READINESS_CONFIRMED
EXECUTION_READINESS_CONFIRMED_WITH_LIMITATIONS
EXECUTION_READINESS_NOT_CONFIRMED
EXECUTION_READINESS_BLOCKED

EXECUTION_READINESS_CONFIRMED does not authorize execution.

## 9. Exit Codes
0 -> readiness confirmed or confirmed with limitations
1 -> readiness not confirmed
2 -> readiness blocked

Exit code 0 is not execution authorization.

## 10. JSON Output
JSON output must use execution_readiness_result as the root object.
JSON output must preserve non-authority markers.

## 11. Output Type Contract
CLI JSON output must preserve required keys and basic JSON types.
Result fields must use string values.
Exit code must use an integer value.
Readiness flags must use boolean values.
Findings, warnings, blockers, and non-authority markers must use arrays of strings.
Unknown keys must not improve result classification.

## 12. Human Output
Human output is explanatory and does not authorize execution.

## 13. Explain Mode
Explain mode does not read task, input, or preconditions files.

## 14. Forbidden Behavior
The CLI must not execute the active task.
The CLI must not run validation commands.
The CLI must not create approval records.
The CLI must not authorize execution.
The CLI must not authorize lifecycle mutation.
The CLI must not authorize M57.
The CLI must not start M57.
The CLI must not include fixture mode.

## 15. Relationship to Policy
The CLI implements the M56 execution readiness policy read-only.

## 16. Relationship to Integration
Integration may call this CLI, but integration must not convert CLI success into execution authorization.

## 17. Relationship to M57
M57 must independently control any future execution attempt.
M56 CLI does not authorize M57.
M56 CLI does not start M57.
M56 CLI does not create M57 artifacts.

## 18. Summary
M56 execution readiness CLI checks readiness only.
It does not execute the active task.
It does not authorize execution.
It does not authorize lifecycle mutation.
It does not authorize M57.
