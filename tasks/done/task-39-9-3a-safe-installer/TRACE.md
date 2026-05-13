---
task_id: task-39-9-3a-safe-installer
state: active
activated_at: 2026-05-12T10:15
activated_by: human-approved-command
approval_id: approval-task-20260426-brief-readiness-check-execution
source_task: tasks/task-39-9-3a-safe-installer/TASK.md
source_contract: tasks/drafts/task-39-9-3a-contract-draft.md
transition: approved_for_execution:active
execution_role:
  role: implementor
  mode: execution_scoped
scope_control:
  allowed_paths:
    - scripts/
    - reports/
    - tasks/
  forbidden_paths:
    - src/
    - templates/
  allow_new_files: true
  allowed_new_files:
    - scripts/install-agentos.py
    - reports/pre-m40-install-agentos-script-report.md
    - tasks/
  forbidden_new_files:
    - src/
  allow_modify_existing: true
  allow_deletes: true
  allow_renames: true
  sensitive_paths:
    - scripts/agentos-validate.py
---
# Task 39.9.3a — Existing Project Safe Installer Script
