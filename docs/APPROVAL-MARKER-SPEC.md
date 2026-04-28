# Approval Marker Spec

## Purpose

An approval marker is a file artifact in `approvals/` that records human approval for a specific transition.
It is evidence only.
It does not execute a transition.
It does not replace human review.

## What an approval marker is

An approval marker:
- is created by a human or by a trusted agent with explicit human authorization
- records that a specific transition has been approved
- can be used as evidence by later dry-run checks
- does not itself change task state

## File Format

```text
approvals/<task-id>-<transition>.md
```

Example:

```text
approvals/task-20260428-queue-schema-check-approved_for_execution-to-active.md
```

## Marker Content

```markdown
# Approval Marker

task_id: <task-id>
transition: <from_state> -> <to_state>
approved_by: <human or trusted agent id>
approved_at: <ISO datetime>
reason: <short justification>

## Safety Confirmation

This marker was created by a human or with explicit human authorization.
This marker is evidence only.
This marker does not execute a transition.
This marker does not replace human review.
```

## When Approval Marker Is Required

An approval marker is required for:
- `contract_drafted -> approved_for_execution`
- `approved_for_execution -> active`

For other transitions, an approval marker is optional.

## What Approval Marker Does Not Do

Approval marker does not execute a transition.
Approval marker does not modify task files.
Approval marker does not replace `tasks/active-task.md`.
Approval marker does not move queue entries.
Approval marker does not grant execution authority to scripts.

## Who Creates Approval Marker

Created by:
- human
- trusted agent with explicit human authorization

Not created by:
- `scripts/detect-task-state.py`
- `scripts/validate-task-state.py`
- `scripts/check-transition.py`
- `scripts/test-state-fixtures.py`
- `scripts/agentos-validate.py`

## How `check-transition.py` Uses Approval Marker

When `check-transition.py` checks `contract_drafted -> approved_for_execution`:
- it checks whether the marker file exists in `approvals/`
- if the marker exists, the dry-run can PASS
- if the marker is missing, the dry-run must FAIL with `approval marker required`
- it does not create the marker
- it does not execute the transition

## Milestone 10 Scope

Milestone 10 does not create approval markers.
Milestone 10 does not consume approval markers to modify files.
Milestone 10 does not validate approval marker content beyond file existence.
Approval marker content validation is scope of Milestone 10.12.1+.

## approvals/ Directory

The `approvals/` directory:
- may be created manually or by a trusted agent with human authorization
- is not created by state layer scripts
- may be absent in early development, and that does not block Milestone 10
