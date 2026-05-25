---
type: cli-doc
milestone: M56
task: 56.8
title: Execution Readiness Fixture Runner
status: draft
authority: fixture-runner-documentation
fixture_runner_only: true
execution_authorized: false
execution_started: false
approval_created: false
lifecycle_mutation_authorized: false
m57_authorized: false
m57_started: false
---

## 1. Purpose
This document defines the M56 execution readiness fixture runner.
The fixture runner validates positive and negative readiness fixtures only.
The fixture runner may invoke the M56 readiness CLI against fixtures only.
Task 56.8 assumes fixture sets from 56.7.1 and 56.7.2 are complete, stable, and expected to produce the declared CLI outcomes.

## 2. Command
The fixture runner is `scripts/check-m56-execution-readiness-fixtures.py`.
It supports `--json`, `--strict`, `--explain`, `--fixtures-root`, and `--readiness-cli`.

## 3. Fixture Scope
The fixture runner reads only the positive and negative execution readiness fixture sets.
It does not inspect production `tasks/active-task.md`.
It does not inspect production queue entries.
It does not inspect approvals.
It does not inspect generated artifacts.

## 4. Case Matrix
The fixture runner evaluates these case ids:
positive_clean_confirmed
positive_input_limitations
positive_markdown_input_with_warning_preconditions
negative_missing_required_input_key
negative_unknown_input_status
negative_empty_traceability
negative_source_path_mismatch
negative_unsafe_authorization_claim
negative_performed_action_violation
negative_preconditions_blocked
negative_active_task_missing_validation
negative_malformed_markdown_multiple_json_blocks

## 5. Runner Result Values
Allowed values are `M56_FIXTURE_RUNNER_PASS`, `M56_FIXTURE_RUNNER_FAIL`, and `M56_FIXTURE_RUNNER_BLOCKED`.

## 6. Runner Exit Codes
`M56_FIXTURE_RUNNER_PASS` maps to exit code `0`.
`M56_FIXTURE_RUNNER_FAIL` maps to exit code `1`.
`M56_FIXTURE_RUNNER_BLOCKED` maps to exit code `2`.

## 7. JSON Output
When `--json` is used, the runner emits machine-readable JSON only.
The JSON output preserves the non-authority boundary and the case results.

## 8. Human Output
Without `--json`, the runner emits a concise human-readable summary.
M56 fixture runner is test harness only.

## 9. Explain Mode
`--explain` prints the runner purpose, timeout rule, strict-mode rule, and non-authority boundary.

## 10. Subprocess Boundary
Subprocess use is limited to invoking `scripts/check-execution-readiness.py` with explicit fixture paths.
The fixture runner may invoke the M56 readiness CLI against fixtures only.

## 11. Timeout Handling
The fixture runner uses TIMEOUT_SECONDS=30 for each CLI invocation.
The fixture runner treats subprocess.TimeoutExpired as CASE_BLOCKED.
Timeout handling is contractually required but not directly exercised by the fixture matrix in Task 56.8 validation.

## 12. Strict Mode
Default mode executes all configured cases and reports all mismatches.
Strict mode stops on the first CASE_FAIL or CASE_BLOCKED.
In strict mode, the cases array contains only executed cases up to and including the first CASE_FAIL or CASE_BLOCKED.

## 13. Forbidden Path Rejection
The fixture runner must reject any case path that resolves outside the fixture root.
The fixture runner must reject paths that point to tasks/, approvals/, or generated/.

## 14. Forbidden Behavior
The fixture runner does not execute active tasks.
The fixture runner does not run validation commands from active-task files.
The fixture runner does not authorize execution.
The fixture runner does not authorize lifecycle mutation.
The fixture runner does not authorize M57.
The fixture runner does not start M57.

## 15. Relationship to CLI
The fixture runner checks the M56 readiness CLI against known fixture inputs.
It does not change the CLI and it does not broaden CLI authority.

## 16. Relationship to Evidence
Fixture runner PASS is not execution authorization.
Fixture runner PASS is not evidence approval.
Fixture runner PASS does not start M57.

## 17. Relationship to M57
The fixture runner is not M57 authorization.
The fixture runner does not start M57.

## 18. Summary
M56 fixture runner is test harness only.
It does not execute active tasks.
It does not authorize execution.
It does not authorize lifecycle mutation.
It does not authorize M57.
