# Execution Result Verification Preconditions

## Metadata

- `preconditions_id`: <!-- string: e.g. execution-result-verification-preconditions-<task_id>-<timestamp> -->
- `task_id`: <!-- string -->
- `verification_input_id`: <!-- string -->
- `preconditions_status`: <!-- string: EXECUTION_RESULT_PRECONDITIONS_READY | EXECUTION_RESULT_PRECONDITIONS_READY_WITH_WARNINGS | EXECUTION_RESULT_PRECONDITIONS_NOT_READY | EXECUTION_RESULT_PRECONDITIONS_BLOCKED -->
- `checked_at`: <!-- string: timestamp -->
- `checked_by`: <!-- string -->

## Source References

- `m58_completion_review_path`: `reports/m58-completion-review.md`
- `m59_intake_report_path`: `reports/m59-m58-completion-intake.md`
- `m59_architecture_path`: `docs/EXECUTION-RESULT-VERIFICATION-ARCHITECTURE.md`
- `input_contract_path`: `docs/EXECUTION-RESULT-VERIFICATION-INPUT-CONTRACT.md`
- `input_schema_path`: `schemas/execution-result-verification-input.schema.json`
- `input_template_path`: `templates/execution-result-verification-input.md`
- `verification_input_path`: <!-- string: path to input file -->
- `execution_session_record_path`: <!-- string: path to record file -->

## M58 Completion Status

- `m58_completion_status`: <!-- string: M58_CONTROLLED_EXECUTION_SESSION_COMPLETE | M58_CONTROLLED_EXECUTION_SESSION_COMPLETE_WITH_WARNINGS | M58_CONTROLLED_EXECUTION_SESSION_INCOMPLETE | M58_CONTROLLED_EXECUTION_SESSION_BLOCKED | UNKNOWN | MISSING | MALFORMED -->

## M59 Intake Status

- `m59_intake_status`: <!-- string: M59_INTAKE_READY | M59_INTAKE_READY_WITH_WARNINGS | M59_INTAKE_BLOCKED | UNKNOWN | MISSING | MALFORMED -->

## M59 Architecture Status

- `m59_architecture_status`: `M59_ARCHITECTURE_DEFINED`

## Input Contract Status

- `input_contract_status`: `M59_EXECUTION_RESULT_VERIFICATION_INPUT_CONTRACT_DEFINED`

## Input Status

- `input_status`: <!-- string: EXECUTION_RESULT_VERIFICATION_INPUT_DRAFT | EXECUTION_RESULT_VERIFICATION_INPUT_READY_FOR_PRECONDITIONS | EXECUTION_RESULT_VERIFICATION_INPUT_BLOCKED -->

## Input Validity

- `input_validity`: <!-- string: VERIFICATION_INPUT_VALID | VERIFICATION_INPUT_INVALID | VERIFICATION_INPUT_MALFORMED | VERIFICATION_INPUT_MISSING | VERIFICATION_INPUT_NEEDS_REVIEW -->

## Execution Session Record Check

- `record_path_present`: <!-- boolean -->
- `record_status_detected`: <!-- string -->
- `record_closed_pending_m59`: <!-- boolean -->
- `record_blocked`: <!-- boolean -->
- `record_aborted`: <!-- boolean -->
- `record_has_m59_handoff`: <!-- boolean -->
- `record_check_result`: <!-- string: EXECUTION_SESSION_RECORD_READY | EXECUTION_SESSION_RECORD_READY_WITH_WARNINGS | EXECUTION_SESSION_RECORD_NOT_READY | EXECUTION_SESSION_RECORD_BLOCKED -->

## Declared Result Check

- `summary_present`: <!-- boolean -->
- `claimed_complete_present`: <!-- boolean -->
- `known_limitations_present`: <!-- boolean -->
- `unresolved_items_present`: <!-- boolean -->
- `declared_result_check_result`: <!-- string: DECLARED_RESULT_READY | DECLARED_RESULT_READY_WITH_WARNINGS | DECLARED_RESULT_NOT_READY | DECLARED_RESULT_BLOCKED -->

## Declared Changes Check

- `files_changed_declared`: <!-- boolean -->
- `files_created_declared`: <!-- boolean -->
- `files_deleted_declared`: <!-- boolean -->
- `behavior_changed_declared`: <!-- boolean -->
- `docs_changed_declared`: <!-- boolean -->
- `tests_changed_declared`: <!-- boolean -->
- `declared_changes_check_result`: <!-- string: DECLARED_CHANGES_READY | DECLARED_CHANGES_READY_WITH_WARNINGS | DECLARED_CHANGES_NOT_READY | DECLARED_CHANGES_BLOCKED -->

## Actual Changed Files Check

- `source`: <!-- string -->
- `files_present`: <!-- boolean -->
- `git_diff_available`: <!-- boolean -->
- `actual_changed_files_check_result`: <!-- string: ACTUAL_CHANGED_FILES_READY | ACTUAL_CHANGED_FILES_READY_WITH_WARNINGS | ACTUAL_CHANGED_FILES_NOT_READY | ACTUAL_CHANGED_FILES_BLOCKED -->

## Git Diff Evidence Check

- `diff_available`: <!-- boolean -->
- `diff_source`: <!-- boolean -->
- `diff_summary_present`: <!-- boolean -->
- `diff_artifact_path_present`: <!-- boolean -->
- `git_diff_evidence_check_result`: <!-- string: GIT_DIFF_EVIDENCE_READY | GIT_DIFF_EVIDENCE_READY_WITH_WARNINGS | GIT_DIFF_EVIDENCE_NOT_READY | GIT_DIFF_EVIDENCE_BLOCKED -->

## Scope Input Check

- `allowed_files_or_dirs_present`: <!-- boolean -->
- `forbidden_files_present`: <!-- boolean -->
- `forbidden_dirs_present`: <!-- boolean -->
- `protected_paths_present`: <!-- boolean -->
- `out_of_scope_present`: <!-- boolean -->
- `scope_expansion_allowed`: <!-- boolean -->
- `scope_input_check_result`: <!-- string: SCOPE_INPUT_READY | SCOPE_INPUT_READY_WITH_WARNINGS | SCOPE_INPUT_NOT_READY | SCOPE_INPUT_BLOCKED -->

## Validation Evidence Check

- `claimed_validation_run`: <!-- boolean -->
- `validation_commands_present`: <!-- boolean -->
- `validation_artifacts_present`: <!-- boolean -->
- `validation_exit_codes_present`: <!-- boolean -->
- `validation_summary_present`: <!-- boolean -->
- `validation_missing_reason_present`: <!-- boolean -->
- `validation_evidence_check_result`: <!-- string: VALIDATION_EVIDENCE_INPUT_READY | VALIDATION_EVIDENCE_INPUT_READY_WITH_WARNINGS | VALIDATION_EVIDENCE_INPUT_NOT_READY | VALIDATION_EVIDENCE_INPUT_BLOCKED -->

## Test Evidence Check

- `claimed_tests_run`: <!-- boolean -->
- `test_commands_present`: <!-- boolean -->
- `test_artifacts_present`: <!-- boolean -->
- `test_exit_codes_present`: <!-- boolean -->
- `test_summary_present`: <!-- boolean -->
- `tests_missing_reason_present`: <!-- boolean -->
- `test_evidence_check_result`: <!-- string: TEST_EVIDENCE_INPUT_READY | TEST_EVIDENCE_INPUT_READY_WITH_WARNINGS | TEST_EVIDENCE_INPUT_NOT_READY | TEST_EVIDENCE_INPUT_BLOCKED -->

## Forbidden Change Rule Checks

- `no_approval_artifacts`: <!-- boolean -->
- `no_lifecycle_mutation`: <!-- boolean -->
- `no_merge_push_release`: <!-- boolean -->
- `no_human_review_replacement`: <!-- boolean -->
- `no_m60_cleanup_artifacts`: <!-- boolean -->
- `forbidden_change_rules_result`: <!-- string: FORBIDDEN_CHANGE_RULES_OK | FORBIDDEN_CHANGE_RULES_WARNING | FORBIDDEN_CHANGE_RULES_BLOCKED -->

## Human Review Handoff Check

- `human_review_handoff_required`: <!-- boolean -->
- `human_review_replacement_claim_absent`: <!-- boolean -->
- `human_review_handoff_result`: <!-- string: HUMAN_REVIEW_HANDOFF_OK | HUMAN_REVIEW_HANDOFF_WARNING | HUMAN_REVIEW_HANDOFF_BLOCKED -->

## Forbidden Action Checks

- `result_already_verified`: false
- `task_marked_complete`: false
- `approval_record_created`: false
- `lifecycle_mutation_performed`: false
- `commit_created`: false
- `push_performed`: false
- `merge_performed`: false
- `release_performed`: false
- `m60_cleanup_started`: false

## Premature Downstream Artifact Checks

- `m59_diff_scope_contract_created`: <!-- boolean -->
- `m59_validation_evidence_contract_created`: <!-- boolean -->
- `m59_result_output_contract_created`: <!-- boolean -->
- `m59_policy_created`: <!-- boolean -->
- `m59_cli_created`: <!-- boolean -->
- `m59_fixtures_created`: <!-- boolean -->
- `m59_fixture_runner_created`: <!-- boolean -->
- `m59_integration_summary_created`: <!-- boolean -->
- `m59_action_review_created`: <!-- boolean -->
- `m59_evidence_report_created`: <!-- boolean -->
- `m59_completion_review_created`: <!-- boolean -->
- `m60_cleanup_artifact_created`: <!-- boolean -->

## Warnings

<!-- list of strings -->

## Blockers

<!-- list of strings -->

## Handoff to 59.4 Git Diff and Scope Verification

- `handoff_to_git_diff_scope_verification`: <!-- boolean -->

## Handoff to 59.5 Validation Evidence Verification

- `handoff_to_validation_evidence_verification`: <!-- boolean -->

## Non-Authority Acknowledgement

- `non_authority_acknowledgement`: |
    This verification preconditions result does not verify execution result.
    This verification preconditions result does not approve task completion.
    This verification preconditions result does not create approval.
    This verification preconditions result does not authorize merge, push, or release.
    This verification preconditions result does not mutate lifecycle state.
    This verification preconditions result does not replace human review.
    This verification preconditions result only determines whether input may proceed to M59 verification checks.

## Final Preconditions Status

- `preconditions_status_confirmed`: <!-- string: same as preconditions_status -->
