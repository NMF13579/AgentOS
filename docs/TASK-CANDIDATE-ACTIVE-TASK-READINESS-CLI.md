---
type: cli-doc
milestone: M55
task: 55.6
title: Task Candidate Active-Task Readiness CLI
status: draft
authority: cli-documentation
created_for: M55
source_policy: docs/TASK-CANDIDATE-ACTIVE-TASK-READINESS-POLICY.md
source_output_contract: docs/TASK-CANDIDATE-ACTIVE-TASK-READINESS-OUTPUT-CONTRACT.md
active_task_file_created: false
active_task_replacement_authorized: false
active_task_write_allowed: false
execution_authorized: false
approval_created: false
lifecycle_mutation_authorized: false
m56_authorized: false
m56_started: false
---

# 1. Purpose

This document defines the M55 active-task readiness CLI behavior.

The M55 active-task readiness CLI is read-only.

# 2. Read-Only Boundary

The CLI does not write tasks/active-task.md.

The CLI does not write tasks/queue/.

The CLI does not create approval records.

The CLI does not authorize execution or M56.

# 3. Supported Arguments

- `--explain`
- `--input <path>`
- `--proposal <path>`
- `--queue-entry <path>`
- `--repo-root <path>`
- `--json`

# 4. Forbidden Arguments

- `--write`
- `--apply`
- `--replace-active-task`
- `--approve`
- `--execute`
- `--start-m56`
- `--fixtures`

Any forbidden argument must return `ACTIVE_TASK_READINESS_BLOCKED` with exit code `2`.

# 5. Input and Proposal Parsing

The CLI accepts:

- `.json` files
- Markdown files containing exactly one fenced `json` block

Parsing failures are fail-closed (`ACTIVE_TASK_READINESS_BLOCKED`).

# 6. Queue Entry Boundary

The CLI reads only the explicit `--queue-entry` file.

The queue-entry path must be relative, under `tasks/queue/`, end with `.md`, and must not point to `tasks/active-task.md`.

The CLI must not scan `tasks/queue/`.

# 7. Result Tokens

- `ACTIVE_TASK_READINESS_CONFIRMED`
- `ACTIVE_TASK_READINESS_CONFIRMED_WITH_LIMITATIONS`
- `ACTIVE_TASK_READINESS_NOT_CONFIRMED`
- `ACTIVE_TASK_READINESS_BLOCKED`

# 8. JSON Output

With `--json`, stdout is JSON with root:

- `active_task_readiness_result`

The output always keeps non-authority and no-mutation flags as `false` for replacement, execution, approvals, and M56 start.

# 9. Human Output

Without `--json`, stdout starts with:

- `M55_ACTIVE_TASK_READINESS_RESULT:`

It includes result, exit code, readiness flags, blockers, and non-authority statements.

# 10. Safe Default

The safe default is ACTIVE_TASK_READINESS_BLOCKED.

ACTIVE_TASK_READINESS_CONFIRMED must never be returned by default.

# 11. Non-Authority Boundary

- M55 readiness output is not approval.
- M55 readiness output does not authorize execution.
- M55 readiness output does not authorize active-task replacement.
- M55 readiness output does not write tasks/active-task.md.
- M55 readiness output does not create approval records.
- M55 readiness output does not authorize M56.
- M55 readiness output does not start M56.

# 12. Relationship to Fixtures

The CLI does not include a fixture mode.

Fixture integration belongs to 55.8.

# 13. Relationship to M56

M56 must independently validate execution readiness.

# 14. Summary

The CLI reports readiness status only.

It is read-only, fail-closed, and does not mutate lifecycle state.
