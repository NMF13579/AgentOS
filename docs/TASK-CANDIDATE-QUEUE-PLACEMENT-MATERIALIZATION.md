---
type: cli-doc
milestone: M54
task: 54.6
title: Task Candidate Queue Placement Materialization CLI
status: draft
authority: supporting
created_for: M54
script:
  - scripts/materialize-task-candidate-placement.py
depends_on:
  - docs/TASK-CANDIDATE-QUEUE-PLACEMENT-MATERIALIZATION-POLICY.md
  - docs/TASK-CANDIDATE-QUEUE-PLACEMENT-MATERIALIZATION-OUTPUT-CONTRACT.md
queue_write_authorized_by_doc: false
active_task_replacement_authorized: false
execution_authorized: false
approval_created: false
m55_authorized: false
---

# Task Candidate Queue Placement Materialization CLI

## Purpose

The M54 materialization CLI performs controlled queue placement materialization only after all pre-materialization checks pass.

This CLI documentation does not authorize a queue write by itself.

## Non-Authority Boundary

M54 CLI is not approval.
M54 CLI does not authorize execution.
M54 CLI does not replace active-task.md.
M54 CLI does not create approval records.
M54 CLI does not authorize M55.

## Usage

```bash
python3 scripts/materialize-task-candidate-placement.py --explain
python3 scripts/materialize-task-candidate-placement.py --input <path> --target tasks/queue/<safe-target-file>.md --dry-run
python3 scripts/materialize-task-candidate-placement.py --input <path> --target tasks/queue/<safe-target-file>.md --dry-run --json
python3 scripts/materialize-task-candidate-placement.py --input <path> --target tasks/queue/<safe-target-file>.md --repo-root <path> --dry-run --json
python3 scripts/materialize-task-candidate-placement.py --input <path> --target tasks/queue/<safe-target-file>.md --write --confirm-write QUEUE_PLACEMENT_WRITE_ALLOWED_BY_M54_POLICY
```

## Dry-Run Boundary

Dry-run mode never writes a queue artifact.

Dry-run success is not materialization.

## Write Boundary

Write mode requires the exact confirmation token QUEUE_PLACEMENT_WRITE_ALLOWED_BY_M54_POLICY.

Write mode must verify all pre-materialization checks from the M54 policy before creating any queue file.

Missing or incorrect write confirmation must block before repository evidence validation.

## Repo Root Boundary

--repo-root is used only for safe path resolution and canonical evidence lookup.

--repo-root does not authorize writes outside that root.

## Forbidden Writes

- tasks/active-task.md
- approvals/
- reports/
- generated/
- docs/
- schemas/
- templates/
- tests/
- examples/
- memory-bank/

## M55 Boundary

M54 materialization does not authorize M55.

## Summary

The M54 CLI may create a queue artifact only through explicit write mode after all pre-materialization checks pass.

It does not approve.
It does not execute.
It does not replace active-task.md.
It does not authorize M55.
