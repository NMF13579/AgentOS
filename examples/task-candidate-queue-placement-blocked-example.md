---
type: example
milestone: M54
task: 54.8
example_id: task-candidate-queue-placement-blocked-example
status: draft
authority: example
dry_run_only: true
write_mode_allowed: false
production_materialization_authorized: false
queue_write_allowed: false
active_task_replacement_allowed: false
approval_creation_allowed: false
execution_authorized: false
m55_authorized: false
---

# Blocked Example

This example demonstrates a blocked queue placement dry-run.

A blocked example does not authorize remediation, queue placement, execution, or M55.

Expected blocker: `TARGET_QUEUE_PATH_UNSAFE`

```bash
python3 scripts/materialize-task-candidate-placement.py \
  --input tests/fixtures/task-candidate-queue-placement/negative/target-active-task-path.json \
  --target tasks/active-task.md \
  --repo-root /tmp/m54-example-sandbox \
  --dry-run \
  --json
```

