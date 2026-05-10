---
task_id: task-m37-1-0-task-id-sync-hardening
task_number: "37.1.0"
task_name: Task ID Sync Hardening
milestone: M37
state: completed
mode: EXECUTION
repository: AgentOS
branch: dev
task:
  id: task-m37-1-0-task-id-sync-hardening
  goal: >
    Implement three levels of task ID sync hardening: templates with {{TASK_ID}}, sync script, and CI step.
  expected_result: >
    Templates updated, script created, CI updated, and all validations pass.
  in_scope:
    - tasks/templates/task-contract.md
    - scripts/sync-task-ids.py
    - .github/workflows/agentos-validate.yml
  out_of_scope:
    - docs/
  files_or_areas:
    - tasks/templates/task-contract.md
    - scripts/sync-task-ids.py
    - .github/workflows/agentos-validate.yml
    - reports/m37-task-id-sync-hardening-report.md
  risk_level: LOW
  risk_reason: "Safe addition of sync logic and CI steps."
  requires_owner_approval: false
  rollback_plan: "Git restore modified files."
  acceptance_criteria:
    - "templates updated"
    - "script created"
    - "CI updated"
  verification_plan:
    - "python3 scripts/validate-task.py tasks/active-task.md"
    - "python3 scripts/agentos-validate.py all"
scope_control:
  allowed_paths:
    - tasks/active-task.md
    - tasks/templates/task-contract.md
    - scripts/sync-task-ids.py
    - .github/workflows/agentos-validate.yml
    - reports/
  forbidden_paths:
  allow_new_files: true
  allowed_new_files:
    - scripts/sync-task-ids.py
    - reports/m37-task-id-sync-hardening-report.md
  forbidden_new_files:
  allow_modify_existing: true
  allow_deletes: false
  allow_renames: false
  sensitive_paths:
    - .github/workflows/agentos-validate.yml
    - scripts/sync-task-ids.py
---

# Task 37.1.0 — Task ID Sync Hardening
