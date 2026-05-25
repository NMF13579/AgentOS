---
type: fixture-integration-doc
milestone: M55
task: 55.8
title: Task Candidate Active-Task Readiness Fixture Integration
status: draft
authority: fixture-integration-documentation
created_for: M55
source_cli: scripts/check-active-task-readiness.py
source_fixture_harness: scripts/check-m55-active-task-readiness-fixtures.py
source_positive_fixtures: tests/fixtures/active-task-readiness/positive/
source_negative_fixtures: tests/fixtures/active-task-readiness/negative/
active_task_file_created: false
active_task_replacement_authorized: false
active_task_write_allowed: false
execution_authorized: false
approval_created: false
lifecycle_mutation_authorized: false
m56_authorized: false
m56_started: false
---

# 1. Purpose

This document defines the M55 active-task readiness fixture integration harness.

The M55 fixture integration harness validates fixture behavior through an isolated /tmp sandbox.

# 2. Integration Boundary

The M55 fixture integration harness does not modify repository task state.

The M55 fixture integration harness does not add fixture mode to the M55 CLI.

The M55 fixture integration harness does not create reports.

The M55 fixture integration harness does not authorize active-task replacement.

The M55 fixture integration harness does not authorize execution.

The M55 fixture integration harness does not authorize M56.

# 3. Sandbox Model

The harness uses a sandbox rooted at `/tmp/m55-active-task-readiness-fixture-integration/`.

The harness copies required upstream files and fixture files into that sandbox.

# 4. Positive Fixture Scenarios

The harness runs these positive scenarios:

- `positive-confirmed-json`
- `positive-confirmed-with-limitations-json`
- `positive-markdown-input`
- `positive-markdown-proposal`

# 5. Negative Fixture Scenarios

The harness runs these negative scenarios:

- `missing-input-root`
- `missing-proposal-root`
- `malformed-readiness-input`
- `readiness-input-queue-entry-mismatch`
- `readiness-input-target-invalid`
- `readiness-input-authority-escalation`
- `readiness-input-missing-traceability`
- `readiness-input-missing-carry-forward`
- `readiness-input-missing-non-authority-markers`
- `proposal-draft-not-confirmed`
- `proposal-blocked-not-confirmed`
- `proposal-human-review-false`
- `proposal-authority-escalation`
- `queue-entry-missing-boundary-markers`
- `queue-entry-authority-escalation`

# 6. Static Result Contradiction Scenario

The harness validates `result-contradictory-authority.json` as a static contradiction case.

# 7. JSON Output

The harness emits JSON with root `m55_active_task_readiness_fixture_integration` when `--json` is provided.

# 8. Human Output

The harness emits a compact human summary when `--json` is not provided.

# 9. Non-Authority Boundary

The harness does not mutate repository files.

The harness does not create approval records.

The harness does not authorize execution.

The harness does not authorize active-task replacement.

The harness does not authorize M56.

# 10. Relationship to 55.9

55.9 may create usage examples, but 55.8 does not create examples.

# 11. Relationship to M56

M56 must independently validate execution readiness.

# 12. Summary

The fixture integration harness is sandbox-only, read-only toward the repository, and fail-closed.
