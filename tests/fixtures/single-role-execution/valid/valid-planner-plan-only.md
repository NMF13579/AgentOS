---
execution_role:
  role: planner
  mode: read_only
  allowed_write_paths:
    - tasks/new-task.md
    - plans/architecture.md
  forbidden_write_paths:
    - src/
  may_modify_files: false
  may_approve: false
  may_change_task_state: false
  may_create_handoff: true
---
