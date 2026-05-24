---
type: fixture-readme
milestone: M55
task: 55.7.2
fixture_set: active-task-readiness-negative
status: draft
authority: fixture-documentation
negative_fixture_count: 17
active_task_file_created: false
active_task_replacement_authorized: false
active_task_write_allowed: false
execution_authorized: false
approval_created: false
lifecycle_mutation_authorized: false
m56_authorized: false
m56_started: false
---

These are negative fixtures for the M55 active-task readiness checker.
Negative fixtures are static test data only.
Negative fixtures must fail closed.
Negative fixtures do not authorize active-task replacement.
Negative fixtures do not write tasks/active-task.md.
Negative fixtures do not create approval records.
Negative fixtures do not authorize execution.
Negative fixtures do not authorize lifecycle mutation.
Negative fixtures do not authorize M56.
Fixture integration belongs to 55.8.
Positive fixtures belong to 55.7.1.

- missing-input-root.json
- missing-proposal-root.json
- malformed-readiness-input.json
- readiness-input-queue-entry-mismatch.json
- readiness-input-target-invalid.json
- readiness-input-authority-escalation.json
- readiness-input-missing-traceability.json
- readiness-input-missing-carry-forward.json
- readiness-input-missing-non-authority-markers.json
- proposal-draft-not-confirmed.json
- proposal-blocked-not-confirmed.json
- proposal-human-review-false.json
- proposal-authority-escalation.json
- queue-entry-missing-boundary-markers.md
- queue-entry-authority-escalation.md
- result-contradictory-authority.json
