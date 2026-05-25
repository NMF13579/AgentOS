---
status: active
task_id: task-fixture-invalid
---

# Active Task: fixture-invalid

## Contract

This fixture has a scope_control block with a modify-existing violation.

```yaml
scope_control:
  allowed_paths:
    - docs/
  forbidden_paths:
    - scripts/
  allow_new_files: false
  allowed_new_files:
    - docs/
  forbidden_new_files:
    - scripts/
  allow_modify_existing: false
  allow_deletes: false
  allow_renames: false
  sensitive_paths:
    - scripts/
```
