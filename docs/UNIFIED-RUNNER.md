# M66 Unified Runner

## 1. Purpose

This document describes the M66 runner.

M66 runner is a read-only subprocess orchestrator for M63/M64/M65 checkers.
M66 runner executes known validators.
M66 runner captures stdout/stderr/exit codes.
M66 runner parses JSON outputs.
M66 runner enforces exit-code/result consistency.
M66 runner aggregates validation signals.
M66 runner is not approval.
Human review remains required.

## 2. CLI

`python3 scripts/run-task-validation.py --input <unified-runner-input-json> --json`

Optional:
`--strict`
`--no-execute`
`--fixture-mode mock-execution`

State clearly whether `--fixture-mode mock-execution` exists or is deferred. It is implemented to allow mock paths explicitly in test scopes only.

## 3. Input Contract

Reference:
- `schemas/unified-runner-input.schema.json`
- `docs/UNIFIED-RUNNER-INPUT-CONTRACT.md`

`input_path_field` is a top-level package field name, not a file path.

## 4. Production Checker Allowlist

task_validation_contract_checker → scripts/check-task-validation-contract.py → --package → task_validation_package_path
agent_task_evidence_checker → scripts/check-agent-task-evidence.py → --evidence → agent_evidence_path
acceptance_criteria_checker → scripts/check-acceptance-criteria.py → --package → acceptance_criteria_package_path

## 5. Mock Checker Boundary

Production runner inputs must not execute mock checkers.
Mock checker paths are rejected outside explicit test-only mock-execution mode.
Mock-execution fixtures validate runner mechanics only.
Mock-execution fixtures do not replace real execution fixtures.

## 6. Subprocess Policy

subprocess.run
shell=False
capture_output=True
text=True
timeout required
Python subprocess execution environment

This does not permit shell=True.

## 7. Read-Only Boundary

Runner writes no files.
Runner creates no reports.
Runner modifies no input files.
Runner only emits JSON to stdout.

## 8. no_execute Behavior

No execution means no validation proof.
No validation proof means no PASS.

--no-execute and execution_mode no_execute cannot produce M66_UNIFIED_RUN_PASS.
--no-execute and execution_mode no_execute cannot produce M66_UNIFIED_RUN_PASS_WITH_WARNINGS.
Valid no_execute structure returns M66_UNIFIED_RUN_NOT_ENOUGH_EVIDENCE.
Invalid no_execute structure returns M66_UNIFIED_RUN_BLOCKED.

## 9. runner_options.json Boundary

runner_options.json is advisory only.
CLI --json controls output.
runner_options.json false with CLI --json produces warning RUNNER_OPTIONS_JSON_FALSE_IGNORED.
Missing CLI --json is CLI misuse and exits 2.

## 10. Result Values and Exit Codes

M66_UNIFIED_RUN_PASS → exit 0
M66_UNIFIED_RUN_PASS_WITH_WARNINGS → exit 0
M66_UNIFIED_RUN_BLOCKED → exit 1
M66_UNIFIED_RUN_NOT_ENOUGH_EVIDENCE → exit 1
CLI misuse / internal runner error → exit 2

## 11. Exit-Code / Result Consistency

Child checker exit code must match child checker result.
Mismatch blocks.
Invalid JSON blocks.
Unknown result blocks.
M63 has no NOT_ENOUGH_EVIDENCE unless explicitly added by M63 contract.

## 12. Aggregation

1. M66_UNIFIED_RUN_BLOCKED
2. M66_UNIFIED_RUN_NOT_ENOUGH_EVIDENCE
3. M66_UNIFIED_RUN_PASS_WITH_WARNINGS
4. M66_UNIFIED_RUN_PASS

## 13. JSON Output Shape

Top-level fields include:
- result
- task_id
- execution_mode
- effective_execution_mode
- human_review_required
- checker_results
- aggregation
- findings
- non_authority_boundary
- exit_code

## 14. Non-Authority Boundary

M66 runner result is a validation signal.
M66 runner result is not approval.
M66 runner result does not complete the task.
M66 runner result does not authorize merge, push, release, or production deployment.
M66 runner result does not create completion gate.
M66 runner result does not start M67.
Human review remains required.

## 15. Relationship to Later Tasks

66.6 creates fixtures.
66.7 validates integration.
66.8 reviews actions.
66.9 collects evidence.
66.10 closes M66.

## 16. Final Status

FINAL_STATUS: M66_UNIFIED_RUNNER_DEFINED_WITH_WARNINGS
