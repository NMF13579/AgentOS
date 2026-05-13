---
task_id: task-39-10-1-add-agentos-flow
state: active
activated_at: 2026-05-12T10:00
activated_by: human-approved-command
approval_id: approval-task-20260426-brief-readiness-check-execution
source_task: tasks/task-39-10-1-add-agentos-flow/TASK.md
source_contract: tasks/drafts/task-39-10-1-contract-draft.md
transition: approved_for_execution:active
execution_role:
  role: implementor
  mode: execution_scoped
scope_control:
  allowed_paths:
    - docs/
    - scripts/
    - README.md
    - tasks/
  forbidden_paths:
    - src/
  allow_new_files: true
  allowed_new_files:
    - docs/ADD-AGENTOS.md
    - scripts/install-agentos.py
    - tasks/
  forbidden_new_files:
    - src/
  allow_modify_existing: true
  allow_deletes: true
  allow_renames: true
  sensitive_paths:
    - scripts/agentos-validate.py
---
# Task 39.10.1 — Add AgentOS to Existing Project Flow
