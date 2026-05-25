---
type: fixtures-readme
milestone: M56
task: 56.7.2
title: Execution Readiness Negative Fixtures
status: draft
fixture_type: negative
authority: test-data-only
execution_authorized: false
execution_started: false
approval_created: false
lifecycle_mutation_authorized: false
m57_authorized: false
m57_started: false
---

These fixtures are negative M56 execution readiness test data only.
Negative fixtures verify fail-closed and not-confirmed behavior; they do not authorize execution.
Negative fixtures must not be used as production active-task files.

fixture_file_count: 10

- README.md
- missing-required-input-key.json
- unknown-input-status.json
- empty-traceability.json
- source-path-mismatch.json
- unsafe-authorization-claim.json
- performed-action-violation.json
- preconditions-blocked.json
- active-task-missing-validation.md
- malformed-markdown-multiple-json-blocks.md
