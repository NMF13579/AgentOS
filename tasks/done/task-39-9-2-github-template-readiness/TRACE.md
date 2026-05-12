---
task_id: task-39-9-2-github-template-readiness
state: active
activated_at: 2026-05-12T09:30
activated_by: human-approved-command
approval_id: approval-task-20260426-brief-readiness-check-execution
source_task: tasks/task-39-9-2-github-template-readiness/TASK.md
source_contract: tasks/drafts/task-39-9-2-contract-draft.md
transition: approved_for_execution:active
execution_role:
  role: implementor
  mode: execution_scoped
scope_control:
  allowed_paths:
    - docs/
    - templates/
    - scripts/
    - reports/
    - tasks/
  forbidden_paths:
    - src/
  allow_new_files: true
  allowed_new_files:
    - templates/agentos-clean/
    - scripts/check-use-template-readiness.py
    - reports/pre-m40-use-template-readiness-report.md
    - tasks/
  forbidden_new_files:
    - src/
  allow_modify_existing: true
  allow_deletes: true
  allow_renames: true
  sensitive_paths:
    - scripts/agentos-validate.py
---
# Task 39.9.2 — GitHub Template Bootstrap / Use Template Readiness
