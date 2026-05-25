---
type: usage-examples
milestone: M55
task: 55.9
example_for: active-task-readiness-cli
status: draft
authority: example-documentation
active_task_file_created: false
active_task_replacement_authorized: false
active_task_write_allowed: false
execution_authorized: false
approval_created: false
lifecycle_mutation_authorized: false
m56_authorized: false
m56_started: false
---

1. Purpose
These CLI examples are documentation only and must not be treated as execution authorization.
CLI examples must use sandbox paths and must not write to production tasks/queue/.
The M55 CLI is read-only and does not write tasks/active-task.md.
The M55 CLI does not create approval records.
The M55 CLI does not authorize execution or M56.

2. Explain Mode
python3 scripts/check-active-task-readiness.py --explain

3. Sandbox-Only Example Layout
python3 scripts/check-active-task-readiness.py --repo-root /tmp/m55-example-sandbox --input examples/active-task-readiness/readiness-input-example.json --proposal examples/active-task-readiness/active-task-proposal-example.json --queue-entry tasks/queue/example-ready.md --json

4. JSON Output Example
{
  "active_task_readiness_result": {
    "result": "ACTIVE_TASK_READINESS_CONFIRMED",
    "exit_code": 0,
    "readiness_confirmed": true,
    "proposal_ready_for_review": true
  }
}

5. Human Output Example
M55_ACTIVE_TASK_READINESS_RESULT:
result: ACTIVE_TASK_READINESS_CONFIRMED
exit_code: 0
readiness_confirmed: true
proposal_ready_for_review: true

6. Forbidden Usage
--write
--apply
--replace-active-task
--approve
--execute
--start-m56
--fixtures

7. Non-Authority Boundary
Fixture integration belongs to 55.8; examples do not replace fixture integration.
M56 must independently validate execution readiness.

8. Relationship to Fixtures
Examples are documentation only and do not replace fixture data.

9. Relationship to M56
M56 must independently validate execution readiness.

10. Summary
These CLI examples are safe documentation only.
