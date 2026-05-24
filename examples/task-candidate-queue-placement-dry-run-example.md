---
type: example
milestone: M54
task: 54.8
example_id: task-candidate-queue-placement-dry-run-example
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

# Dry-Run Example

This example demonstrates dry-run queue placement behavior only.

This example does not authorize queue placement.

```bash
python3 scripts/materialize-task-candidate-placement.py \
  --input tests/fixtures/task-candidate-queue-placement/positive/valid-canonical-root-input.json \
  --target tasks/queue/candidate-for-validation.md \
  --repo-root /tmp/m54-example-sandbox \
  --dry-run \
  --json
```

