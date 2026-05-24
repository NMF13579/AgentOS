---
type: example
milestone: M54
task: 54.8
example_id: task-candidate-queue-placement-with-limitations-example
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

# Carry-Forward Limitations Example

This example demonstrates carry-forward limitations in M54 dry-run context.

Carry-forward limitations are not approval.

Reference fixture:

`tests/fixtures/task-candidate-queue-placement/positive/valid-input-with-limitations.json`

```bash
python3 scripts/materialize-task-candidate-placement.py \
  --input tests/fixtures/task-candidate-queue-placement/positive/valid-input-with-limitations.json \
  --target tasks/queue/candidate-for-validation.md \
  --repo-root /tmp/m54-example-sandbox \
  --dry-run \
  --json
```

