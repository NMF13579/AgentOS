---
task:
  risk_level: LOW
execution_role:
  role: implementor
  mode: scoped_write
  allowed_write_paths:
    - src/app.py
    - reports/evidence.md
    - scripts/agentos-validate.py
  forbidden_write_paths:
    - approvals/
  may_modify_files: true
  may_approve: false
  may_change_task_state: true
  may_create_handoff: true
---
