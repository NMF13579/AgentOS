---
execution_role:
  role: auditor
  mode: read_only
  allowed_write_paths:
    - reports/a.md
    - reports/b.md
    - reports/c.md
  forbidden_write_paths: []
  may_modify_files: false
  may_approve: false
  may_change_task_state: false
  may_create_handoff: true
---
