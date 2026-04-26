# Negative Fixtures

This directory contains negative test fixtures for AgentOS.

Negative fixtures are intentionally invalid or incomplete inputs used to verify that validators, checkers, and generators correctly reject bad inputs.

## Purpose

Negative fixtures document bad states that AgentOS guardrails must reject.

## Categories

- `task-brief/` - invalid Task Brief files
- `review/` - invalid Review files
- `trace/` - invalid Trace files
- `contract-generation/` - invalid contract generation inputs
- `queue/` - invalid queue entries
- `runner/` - invalid runner scenarios
- `template-integrity/` - references to existing template-integrity fixtures

## Inventory

| Category | Cases | Manual verification |
|---|---:|---|
| task-brief | 4 | validate-task-brief.py |
| review | 3 | future validator |
| trace | 2 | future validator |
| contract-generation | 4 | generate-task-contract.py |
| queue | 4 | future validator |
| runner | 3 | future guard test |
| template-integrity | reference-only | check-template-integrity.py |

## Manual Verification Overview

Cases with real commands: task-brief (validate-task-brief.py), contract-generation (generate-task-contract.py), template-integrity (check-template-integrity.py).

Cases pending future validator: review, trace, queue, runner.

Commands are documented only. No scripts were executed in this task.

## Non-goals

This inventory does not:

- create payload files
- run validators
- run runner scripts
- generate contracts
- approve execution
- implement audit runner behavior
- implement autonomous runner behavior
- modify `tasks/active-task.md`
- move queue items
- modify root-level `tasks/drafts/`

## Notes

Payload files (`TASK.md`, `REVIEW.md`, `TRACE.md`, `queue-entry.md`, `scenario.md`, etc.) are added in Task 7.1.2.

This directory contains README-only inventory.
