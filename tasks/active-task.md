---
task_id: none
state: idle
task:
  id: none
  goal: No active task
  expected_result: Active task is intentionally idle
  in_scope:
    - reports/
  out_of_scope:
    - .github/
  files_or_areas:
    - tasks/active-task.md
  risk_level: LOW
  risk_reason: Idle placeholder task for CI context checks.
  requires_owner_approval: false
  rollback_plan: Restore previous active task contract when a new task is approved.
  acceptance_criteria:
    - active-task state is idle
  verification_plan:
    - validate task schema
---
# No active task
