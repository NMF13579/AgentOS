---
type: fixture-readme
milestone: M54
task: 54.7.2
fixture_set: task-candidate-queue-placement-negative
status: draft
authority: test-fixture
queue_placement_authorized: false
execution_authorized: false
active_task_replacement_authorized: false
approval_created: false
m55_authorized: false
---

# Negative Fixtures

Negative fixtures are not production evidence.
Negative fixtures do not authorize queue placement.
Negative fixtures do not authorize execution.
Negative fixtures do not authorize active-task replacement.
Negative fixtures do not authorize approval creation.
Negative fixtures do not authorize M55.

These fixtures are intentionally invalid or unsafe examples for future M54 fixture integration only.

These fixtures must not be copied into reports/, tasks/queue/, approvals/, generated/, or memory-bank/.

Production upstream files are read only for dependency and precondition checks; their contents are not copied into these fixtures.

## Files

- `missing-input-root.json`
- `both-input-roots-present.json`
- `unsafe-boundary-execution-authorized.json`
- `unsafe-boundary-approval-created.json`
- `unsafe-boundary-active-task-replacement.json`
- `unsafe-boundary-m55-authorized.json`
- `target-outside-queue.json`
- `target-active-task-path.json`
- `missing-source-traceability.json`
- `missing-carry-forward.json`
- `m53-placement-result-not-eligible.json`
- `m53-placement-result-materialization-authorized.json`
- `m53-placement-result-already-queued.json`
- `m54-intake-blocked.md`
- `materialization-result-claims-execution.json`
- `materialization-result-claims-m55.json`
