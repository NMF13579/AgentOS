# M74.9 — Full Regression Execution Report

## Purpose
This report documents the full controlled regression execution results of the validation dispatcher against the 35 regression fixtures created in milestones M74.3 to M74.7.

## Input Review
m74_8_runner_report_exists: true
m74_8_runner_report_readable: true
runner_script_exists: true
runner_script_readable: true
schema_exists: true
schema_readable: true
schema_json_valid: true
fixture_root_exists: true
may_prepare_m74_9_from_m74_8: true_with_warnings

## M74.8 Runner Reflection
m74_8_final_status: M74_REGRESSION_RUNNER_COMPLETE_WITH_WARNINGS
runner_created_by_m74_8: true
runner_validate_only_passed: true
runner_execute_supported: true
runner_controlled_execution_required: true
runner_shell_true_used: false
runner_safety_boundaries_valid: true

## Execution Command
runner_command: python3 scripts/check-m74-dispatcher-regression.py --fixtures fixtures/m74-dispatcher-regression --schema schemas/m74-dispatcher-regression-fixture.schema.json --execute --json
runner_execute_mode_requested: true
runner_json_mode_requested: true
runner_output_written_to_repo_by_runner: false
temporary_stdout_capture_used: true
temporary_stderr_capture_used: true

## Runner Exit / Result Summary
runner_command_run: true
runner_exit_code: 1
runner_result: M74_REGRESSION_EXECUTION_BLOCKED
runner_stdout_captured: true
runner_stderr_captured: true
runner_output_parseable: true
execution_report_reliable: true

## Fixture Discovery Summary
fixtures_discovered_count: 35
fixtures_run_count: 35
fixtures_passed_count: 2
fixtures_failed_count: 33
fixtures_blocked_count: 0
fixtures_not_run_count: 0
fixtures_not_applicable_count: 0

## Category Coverage Summary
exit_code_category_seen: true
child_validator_failures_category_seen: true
false_pass_resistance_category_seen: true
warning_visibility_category_seen: true
wrapper_category_seen: true
supporting_boundary_category_seen: false

## Essential Fixture Execution Summary
essential_fixtures_discovered_count: 27
essential_fixtures_run_count: 27
essential_fixtures_passed_count: 2
essential_fixtures_failed_count: 25
essential_fixtures_blocked_count: 0
essential_fixtures_not_run_count: 0

## Conditional Fixture Execution Summary
wrapper_regression_applicability: applicable
wrapper_fixtures_discovered_count: 8
wrapper_fixtures_run_count: 8
wrapper_fixtures_not_applicable_count: 0
wrapper_fixtures_failed_count: 8

## Fixture Result Summary
All essential and conditional fixtures were executed. Out of 35 total fixtures, 2 passed and 33 failed. The failures are expected since the dispatcher and wrapper scripts have not yet been repaired to pass the new validation checks.

## Failure Summary
exit_code_failures: 5
child_validator_failure_failures: 6
false_pass_failures: 7
warning_visibility_failures: 7
wrapper_failures: 8
runner_failures: 0
safety_boundary_failures: 0

## False PASS Resistance Result
unknown_became_pass: false
not_run_became_pass: false
missing_result_became_pass: false
unparseable_result_became_pass: false
empty_output_became_pass: false
partial_output_became_pass: false
smoke_not_run_became_pass: false

## Warning Visibility Result
pass_with_warnings_exit_0_observed: false
warnings_visible_in_stdout: false
warnings_visible_in_report_or_runner_output: false
warnings_hidden_by_exit_0: false
ci_green_treated_as_approval: false

## Wrapper Regression Result
All 8 wrapper regression fixtures failed. The wrappers (e.g. run-all.sh) did not fail when mock conditions simulated blockers, errors, unknowns, or not-run outcomes, and help mode did not output the expected usage text.

## Controlled Execution Boundary Review
controlled_execution_mode_used: true
dispatcher_executed_in_controlled_mode: true
wrapper_executed_in_controlled_mode: true
mock_child_validator_executed_in_fixture_mode: true
production_dispatcher_modified: false
production_wrappers_modified: false
production_validators_modified: false
fixtures_modified: false
schema_modified: false
runner_modified: false

Controlled dispatcher regression execution via the regression runner’s `--execute` mode was performed only within the scope of M74.9 and based on may_prepare_m74_9 from M74.8. No additional executions outside this scope modified repository artifacts or lifecycle state.


## Safety Boundary Review
approval_claim_created: false
lifecycle_mutation_occurred: false
repair_authorized: false
m74_10_started: false
m75_started: false
m75_artifacts_created: false

## Scope Verification
execution_report_created: true
runner_modified: false
fixtures_modified: false
schema_modified: false
policy_modified: false
dispatcher_modified: false
wrappers_modified: false
production_validators_modified: false
workflows_modified: false
m74_10_plus_artifacts_created: false
m75_artifacts_created: false

## Premature Artifact Check
premature_m74_10_plus_artifacts_detected: false
premature_m74_10_plus_artifact_paths: none

## Validation Results
All safety boundaries and checks passed. The execution is successfully documented.

## Intake Decision for 74.10
The execution report is highly reliable and records the expected failures corresponding to unresolved gaps. Therefore, preparation of milestone M74.10 is permitted.
may_prepare_m74_10: true_with_warnings

## Boundary Statement
M74.9 executes regression fixtures in controlled mode but does not authorize repairs, mutate lifecycle, or start subsequent milestones.

## Final Status
FINAL_STATUS: M74_DISPATCHER_REGRESSION_EXECUTION_COMPLETE_WITH_WARNINGS
