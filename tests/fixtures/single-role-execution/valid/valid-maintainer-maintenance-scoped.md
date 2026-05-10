---
execution_role:
  role: maintainer
  mode: maintenance_scoped
  allowed_write_paths:
    - docs/ARCHITECTURE.md
    - scripts/utils.py
  forbidden_write_paths:
    - approvals/
  may_modify_files: true
  may_approve: false
  may_change_task_state: true
  may_create_handoff: true
---
