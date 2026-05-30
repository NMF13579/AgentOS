# M74.11 — Regression Evidence Report

## Purpose
This report is a read-only evidence consolidation for milestone M74.11. It aggregates and cross-checks evidence from M74.8 (runner), M74.9 (execution), M74.10 (action review), and M74.12 (completion review). No regression was re-executed. No statuses, approvals, or lifecycle state were changed.

## Input Inventory
input_m73_completion_review_exists: true
input_m74_runner_report_exists: true
input_m74_execution_report_exists: true
input_m74_action_review_exists: true
input_m74_completion_review_exists: true
input_policy_doc_exists: true
input_fixture_schema_exists: true
input_fixtures_root_exists: true

All mandatory inputs for M74.11 were found and are readable. No inputs are missing.

## Runner Evidence Summary (M74.8)
Source: reports/m74-regression-runner-report.md

runner_report_readable: true
runner_created: true
runner_python_syntax_valid: true
runner_validate_only_supported: true
runner_execute_supported: true
runner_unknown_args_rejected: true
runner_cli_misuse_exit_2_supported: true

Additional runner safety properties confirmed:
runner_uses_shell_true: false
runner_uses_subprocess_argument_list: true
runner_refuses_output_outside_reports_m74: true
runner_refuses_fixture_path_escape: true
runner_refuses_mock_child_path_escape: true
runner_refuses_mock_child_under_scripts: true
runner_modifies_dispatcher: false
runner_modifies_wrappers: false
runner_modifies_production_validators: false
runner_creates_approval: false
runner_mutates_lifecycle: false

Validate-only execution result (M74.8):
validate_only_exit_code: 0
validate_only_runner_result: M74_REGRESSION_VALIDATE_PASS
fixtures_discovered_by_validate_only: 35
fixtures_valid_by_validate_only: 35
fixtures_invalid_by_validate_only: 0

M74.8 final status: M74_REGRESSION_RUNNER_COMPLETE_WITH_WARNINGS

## Execution Evidence Summary (M74.9)
Source: reports/m74-dispatcher-regression-execution-report.md

execution_report_readable: true
execution_runner_command_run: true
execution_runner_exit_code: 1
execution_runner_result: M74_REGRESSION_EXECUTION_BLOCKED
execution_fixtures_discovered_count: 35
execution_fixtures_run_count: 35
execution_fixtures_passed_count: 2
execution_fixtures_failed_count: 33
execution_essential_fixtures_failed_count: 25

Category-level execution breakdown:
execution_exit_code_category_seen: true
execution_child_validator_failures_category_seen: true
execution_false_pass_resistance_category_seen: true
execution_warning_visibility_category_seen: true
execution_wrapper_category_seen: true
execution_supporting_boundary_category_seen: false

Essential fixture breakdown:
execution_essential_fixtures_discovered_count: 27
execution_essential_fixtures_run_count: 27
execution_essential_fixtures_passed_count: 2
execution_essential_fixtures_blocked_count: 0
execution_essential_fixtures_not_run_count: 0

Conditional (wrapper) fixture breakdown:
execution_wrapper_fixtures_discovered_count: 8
execution_wrapper_fixtures_run_count: 8
execution_wrapper_fixtures_failed_count: 8
execution_wrapper_regression_applicability: applicable

Failure summary by category:
execution_exit_code_failures: 5
execution_child_validator_failures: 6
execution_false_pass_failures: 7
execution_warning_visibility_failures: 7
execution_wrapper_failures: 8

M74.9 final status: M74_DISPATCHER_REGRESSION_EXECUTION_COMPLETE_WITH_WARNINGS

## Action Review Evidence Summary (M74.10)
Source: reports/m74-regression-action-review.md

action_review_report_readable: true
failed_fixtures_classified: true
blocked_fixtures_classified: true
not_run_fixtures_classified: true
gap_closed_by_fixture_count: 2
gap_requires_fix_task_count: 9
gap_not_applicable_with_evidence_count: 0
gap_open_count: 0
gap_blocked_count: 0

Action decision from M74.10: FIX_TASKS_REQUIRED

Gap status table (from M74.10):
| gap_id | gap_status | action_required |
| :--- | :--- | :--- |
| exit_2_semantics | REQUIRES_FIX_TASK | true |
| pass_with_warnings_exit_0 | REQUIRES_FIX_TASK | true |
| missing_child_validator | REQUIRES_FIX_TASK | true |
| malformed_child_output | REQUIRES_FIX_TASK | true |
| child_failure_propagation | REQUIRES_FIX_TASK | true |
| unknown_not_pass_requires_m74_regression_fixture | REQUIRES_FIX_TASK | true |
| not_run_not_pass_requires_m74_regression_fixture | REQUIRES_FIX_TASK | true |
| warning_visibility | REQUIRES_FIX_TASK | true |
| wrapper_gaps | REQUIRES_FIX_TASK | true |
| runner-safety | CLOSED_BY_FIXTURE | false |
| controlled-execution | CLOSED_BY_FIXTURE | false |

M74.10 final status: M74_REGRESSION_ACTION_REVIEW_COMPLETE_WITH_WARNINGS

## Completion Review Reflection (M74.12)
Source: reports/m74-completion-review.md

completion_review_report_readable: true
m74_final_status: M74_DISPATCHER_REGRESSION_BLOCKED
ready_for_m75: false
human_review_required_before_m75: true

Reason for BLOCKED status as stated in M74.12:
M74.12 completion review was blocked because reports/m74-regression-evidence-report.md (this report) was missing at the time of M74.12 creation. The current report (M74.11) is the artifact that resolves this missing input. M74.12 should be re-evaluated once this report is committed.

## Fixture and Gap Evidence
Fixture root: fixtures/m74-dispatcher-regression/
Fixture directories present: exit-code, child-validator-failures, false-pass-resistance, warning-visibility, wrapper, mock-child-validators
Total fixture JSON files confirmed: 35

Fixture counts by category:
fixture_exit_code_count: 7
fixture_child_validator_failures_count: 6
fixture_false_pass_resistance_count: 7
fixture_warning_visibility_count: 7
fixture_wrapper_count: 8
fixture_total_count: 35

All 35 fixtures are confirmed present and passed schema validation in M74.8 validate-only run.

Gap lifecycle evidence summary:
gap_lifecycle_closed_by_fixture_count: 2
gap_lifecycle_requires_fix_task_count: 9
gap_lifecycle_not_applicable_with_evidence_count: 0
gap_lifecycle_open_count: 0
gap_lifecycle_blocked_count: 0
gap_lifecycle_invalid_count: 0

## False PASS Resistance Evidence
Source: reports/m74-dispatcher-regression-execution-report.md

unknown_became_pass: false
not_run_became_pass: false
missing_result_became_pass: false
unparseable_result_became_pass: false
empty_output_became_pass: false
partial_output_became_pass: false
smoke_not_run_became_pass: false

The runner correctly failed closed on all false PASS resistance scenarios. UNKNOWN and NOT_RUN results were not promoted to PASS. These are fixture-level failures (gaps remain open and require fix tasks) — they are not runner safety failures.

## Warning Visibility Evidence
Source: reports/m74-dispatcher-regression-execution-report.md

pass_with_warnings_exit_0_observed: false
warnings_visible_in_stdout: false
warnings_visible_in_report_or_runner_output: false
warnings_hidden_by_exit_0: false
ci_green_treated_as_approval: false

Warning visibility fixture failures were classified as REQUIRES_FIX_TASK in M74.10. This is a dispatcher gap — the dispatcher does not yet surface warnings visibly. The runner itself correctly detected and reported these failures.

## Safety Boundary Evidence
Source: reports/m74-dispatcher-regression-execution-report.md, reports/m74-regression-action-review.md, reports/m74-completion-review.md

controlled_execution_mode_used: true
production_dispatcher_modified: false
production_wrappers_modified: false
production_validators_modified: false
fixtures_modified: false
schema_modified: false
runner_modified: false
shell_true_used_in_runner: false
mock_child_validators_escaped_fixture_dir: false

## Lifecycle / Approval Evidence
approval_claim_created: false
human_approval_created: false
lifecycle_mutation_occurred: false
repair_authorized: false
m75_started: false
m75_artifacts_created: false

Safety semantics confirmed:
PASS is not approval.
Evidence is not approval.
Regression PASS is not approval.
UNKNOWN is not OK.
NOT_RUN is not PASS.
Fixture NOT_RUN is not PASS.
CI green is not approval.
Human approval cannot be simulated.
Human review remains required.

## Evidence Reliability Review
evidence_complete: true
evidence_consistent: true
evidence_based_on_actual_execution: true
evidence_runner_execution_reused_from_m74_9: true
evidence_missing_m74_11_specific_run: true
evidence_missing_reports: none

Cross-check consistency note:
All four input reports (M74.8 runner, M74.9 execution, M74.10 action review, M74.12 completion review) are internally consistent on key counts:
- fixtures_discovered: 35 across all sources
- fixtures_run: 35 across M74.9 and M74.10
- fixtures_passed: 2 across M74.9, M74.10, and M74.12
- fixtures_failed: 33 across M74.9, M74.10, and M74.12
- essential_fixtures_failed: 25 across M74.9, M74.10, and M74.12
- gap_closed_by_fixture: 2 across M74.10 and M74.12
- gap_requires_fix_task: 9 in M74.10

No inconsistencies detected. Evidence is reliable and consistent.

## Evidence Limitations
This report does not re-execute regression. The evidence is entirely derived from M74.9 controlled execution output. The following limitations apply:

- M74.11 does not run scripts/check-m74-dispatcher-regression.py with --execute.
- M74.11 does not run the dispatcher in any mode.
- M74.11 does not modify fixture files or runner.
- Fixture-level FAIL outcomes (33 failures) reflect open dispatcher gaps, not evidence collection failures.
- evidence_missing_m74_11_specific_run is always true; M74.9 execution is the authoritative execution record.

## Readiness Evidence for M75
ready_for_m75_evidence_only: true
ready_for_m75_is_approval: false
ready_for_m75_starts_m75: false

Evidence indicates that M74 is currently blocked due to 33 fixture failures, 9 gaps requiring fix tasks, and the absence of this evidence report at time of M74.12 creation. This evidence report resolves the missing-input blocker in M74.12, but does not resolve the fix-task gaps. Those gaps (listed in M74.10 gap status table) require separate fix tasks before M74 can be declared complete. Human review remains required before M75 execution.

## Boundary Statement
M74.11 created the regression evidence report. M74.11 did not execute the regression runner with --execute. M74.11 did not execute the dispatcher. M74.11 did not modify any fixture files. M74.11 did not modify the runner script. M74.11 did not modify any other M73 or M74 reports. M74.11 did not create M75 artifacts. M74.11 did not create approval claims. M74.11 did not create human approvals. M74.11 did not authorize repair. M74.11 did not mutate lifecycle. Evidence is not approval. ready_for_m75_evidence_only is evidence readiness only and is not approval. ready_for_m75_evidence_only does not start M75. Human review remains required before M75 execution.

## Final Status
FINAL_STATUS: M74_REGRESSION_EVIDENCE_COMPLETE_WITH_WARNINGS
may_prepare_m74_12: true_with_warnings
