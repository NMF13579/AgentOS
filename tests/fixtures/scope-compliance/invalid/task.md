---
status: active
task_id: task-fixture-invalid
---

# Active Task: fixture-invalid

## Contract

This fixture has a scope_control block with a broad forbidden path violation.

```yaml
scope_control:
  allowed_write_paths:
    - .
  forbidden_write_paths: []
```
