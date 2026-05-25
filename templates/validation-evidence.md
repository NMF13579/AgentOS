# Validation Evidence

## Metadata

- `validation_evidence_id`: <!-- string: e.g. validation-evidence-<task_id>-<timestamp> -->
- `task_id`: <!-- string -->
- `verification_input_id`: <!-- string -->
- `preconditions_id`: <!-- string -->
- `diff_scope_verification_id`: <!-- string -->
- `validation_evidence_status`: <!-- string: VALIDATION_EVIDENCE_CONFIRMED | VALIDATION_EVIDENCE_CONFIRMED_WITH_WARNINGS | VALIDATION_EVIDENCE_NOT_CONFIRMED | VALIDATION_EVIDENCE_BLOCKED -->
- `checked_at`: <!-- string: timestamp -->
- `checked_by`: <!-- string -->

## Source References

- `m59_intake_report_path`: `reports/m59-m58-completion-intake.md`
- `m59_architecture_path`: `docs/EXECUTION-RESULT-VERIFICATION-ARCHITECTURE.md`
- `input_contract_path`: `docs/EXECUTION-RESULT-VERIFICATION-INPUT-CONTRACT.md`
- `preconditions_contract_path`: `docs/EXECUTION-RESULT-VERIFICATION-PRECONDITIONS-CONTRACT.md`
- `diff_scope_contract_path`: `docs/GIT-DIFF-SCOPE-VERIFICATION-CONTRACT.md`
- `verification_input_path`: <!-- string: path to input file -->
- `verification_preconditions_path`: <!-- string: path to preconditions file -->
- `diff_scope_verification_path`: <!-- string: path to diff scope verification file -->
- `source_task_path`: <!-- string -->
- `execution_session_record_path`: <!-- string -->

## Validation Claim Check

- `claimed_validation_run`: <!-- boolean -->
- `validation_claims_present`: <!-- boolean -->
- `validation_claims_supported_by_artifacts`: <!-- boolean -->
- `unsupported_validation_claims`: <!-- array of strings -->
- `validation_claim_result`: <!-- string: VALIDATION_CLAIMS_SUPPORTED | VALIDATION_CLAIMS_SUPPORTED_WITH_WARNINGS | VALIDATION_CLAIMS_NOT_CONFIRMED | VALIDATION_CLAIMS_BLOCKED -->

## Validation Command Check

- `validation_commands_declared`: <!-- array of strings -->
- `validation_commands_executed`: <!-- array of strings -->
- `command_evidence_present`: <!-- boolean -->
- `commands_match_declared`: <!-- boolean -->
- `unexpected_validation_commands`: <!-- array of strings -->
- `validation_command_result`: <!-- string: VALIDATION_COMMANDS_CONFIRMED | VALIDATION_COMMANDS_CONFIRMED_WITH_WARNINGS | VALIDATION_COMMANDS_NOT_CONFIRMED | VALIDATION_COMMANDS_BLOCKED -->

## Validation Artifact Check

- `validation_artifacts_declared`: <!-- array of strings -->
- `validation_artifacts_present`: <!-- array of strings -->
- `validation_artifacts_readable`: <!-- boolean -->
- `validation_artifacts_match_commands`: <!-- boolean -->
- `validation_artifact_result`: <!-- string: VALIDATION_ARTIFACTS_CONFIRMED | VALIDATION_ARTIFACTS_CONFIRMED_WITH_WARNINGS | VALIDATION_ARTIFACTS_NOT_CONFIRMED | VALIDATION_ARTIFACTS_BLOCKED -->

## Validation Exit Code Check

- `exit_codes_present`: <!-- boolean -->
- `exit_codes_all_zero`: <!-- boolean -->
- `nonzero_exit_codes`: <!-- array of integers -->
- `exit_code_meaning_documented`: <!-- boolean -->
- `validation_exit_code_result`: <!-- string: VALIDATION_EXIT_CODES_PASS | VALIDATION_EXIT_CODES_PASS_WITH_WARNINGS | VALIDATION_EXIT_CODES_NOT_CONFIRMED | VALIDATION_EXIT_CODES_BLOCKED -->

## Validation Freshness Check

- `evidence_timestamp_present`: <!-- boolean -->
- `evidence_after_changes`: <!-- boolean -->
- `evidence_matches_current_diff`: <!-- boolean -->
- `stale_evidence_detected`: <!-- boolean -->
- `validation_freshness_result`: <!-- string: VALIDATION_FRESHNESS_CONFIRMED | VALIDATION_FRESHNESS_CONFIRMED_WITH_WARNINGS | VALIDATION_FRESHNESS_NOT_CONFIRMED | VALIDATION_FRESHNESS_BLOCKED -->

## Validation Relevance Check

- `validation_targets_changed_files`: <!-- boolean -->
- `validation_targets_task_scope`: <!-- boolean -->
- `unrelated_validation_detected`: <!-- boolean -->
- `validation_relevance_result`: <!-- string: VALIDATION_RELEVANCE_CONFIRMED | VALIDATION_RELEVANCE_CONFIRMED_WITH_WARNINGS | VALIDATION_RELEVANCE_NOT_CONFIRMED | VALIDATION_RELEVANCE_BLOCKED -->

## Test Claim Check

- `claimed_tests_run`: <!-- boolean -->
- `test_claims_present`: <!-- boolean -->
- `test_claims_supported_by_artifacts`: <!-- boolean -->
- `unsupported_test_claims`: <!-- array of strings -->
- `test_claim_result`: <!-- string: TEST_CLAIMS_SUPPORTED | TEST_CLAIMS_SUPPORTED_WITH_WARNINGS | TEST_CLAIMS_NOT_CONFIRMED | TEST_CLAIMS_BLOCKED -->

## Test Command Check

- `test_commands_declared`: <!-- array of strings -->
- `test_commands_executed`: <!-- array of strings -->
- `command_evidence_present`: <!-- boolean -->
- `commands_match_declared`: <!-- boolean -->
- `unexpected_test_commands`: <!-- array of strings -->
- `test_command_result`: <!-- string: TEST_COMMANDS_CONFIRMED | TEST_COMMANDS_CONFIRMED_WITH_WARNINGS | TEST_COMMANDS_NOT_CONFIRMED | TEST_COMMANDS_BLOCKED -->

## Test Artifact Check

- `test_artifacts_declared`: <!-- array of strings -->
- `test_artifacts_present`: <!-- array of strings -->
- `test_artifacts_readable`: <!-- boolean -->
- `test_artifacts_match_commands`: <!-- boolean -->
- `test_artifact_result`: <!-- string: TEST_ARTIFACTS_CONFIRMED | TEST_ARTIFACTS_CONFIRMED_WITH_WARNINGS | TEST_ARTIFACTS_NOT_CONFIRMED | TEST_ARTIFACTS_BLOCKED -->

## Test Exit Code Check

- `exit_codes_present`: <!-- boolean -->
- `exit_codes_all_zero`: <!-- boolean -->
- `nonzero_exit_codes`: <!-- array of integers -->
- `exit_code_meaning_documented`: <!-- boolean -->
- `test_exit_code_result`: <!-- string: TEST_EXIT_CODES_PASS | TEST_EXIT_CODES_PASS_WITH_WARNINGS | TEST_EXIT_CODES_NOT_CONFIRMED | TEST_EXIT_CODES_BLOCKED -->

## Test Freshness Check

- `evidence_timestamp_present`: <!-- boolean -->
- `evidence_after_changes`: <!-- boolean -->
- `evidence_matches_current_diff`: <!-- boolean -->
- `stale_evidence_detected`: <!-- boolean -->
- `test_freshness_result`: <!-- string: TEST_FRESHNESS_CONFIRMED | TEST_FRESHNESS_CONFIRMED_WITH_WARNINGS | TEST_FRESHNESS_NOT_CONFIRMED | TEST_FRESHNESS_BLOCKED -->

## Test Relevance Check

- `tests_target_changed_files`: <!-- boolean -->
- `tests_target_task_scope`: <!-- boolean -->
- `unrelated_tests_detected`: <!-- boolean -->
- `test_relevance_result`: <!-- string: TEST_RELEVANCE_CONFIRMED | TEST_RELEVANCE_CONFIRMED_WITH_WARNINGS | TEST_RELEVANCE_NOT_CONFIRMED | TEST_RELEVANCE_BLOCKED -->

## Missing Evidence Check

- `validation_evidence_missing`: <!-- boolean -->
- `validation_missing_reason_present`: <!-- boolean -->
- `test_evidence_missing`: <!-- boolean -->
- `test_missing_reason_present`: <!-- boolean -->
- `missing_evidence_result`: <!-- string: NO_REQUIRED_EVIDENCE_MISSING | MISSING_EVIDENCE_WITH_EXPLANATION | MISSING_EVIDENCE_NOT_CONFIRMED | MISSING_EVIDENCE_BLOCKED -->

## Stale Evidence Check

- `stale_validation_evidence_detected`: <!-- boolean -->
- `stale_test_evidence_detected`: <!-- boolean -->
- `stale_evidence_affects_changed_files`: <!-- boolean -->
- `stale_evidence_result`: <!-- string: NO_STALE_EVIDENCE | STALE_EVIDENCE_WARNING | STALE_EVIDENCE_NOT_CONFIRMED | STALE_EVIDENCE_BLOCKED -->

## Wrong Validation Check

- `wrong_validation_detected`: <!-- boolean -->
- `wrong_tests_detected`: <!-- boolean -->
- `unrelated_commands_detected`: <!-- boolean -->
- `wrong_validation_result`: <!-- string: NO_WRONG_VALIDATION_DETECTED | WRONG_VALIDATION_WARNING | WRONG_VALIDATION_NOT_CONFIRMED | WRONG_VALIDATION_BLOCKED -->

## Authority Claim Check

- `claims_result_verified`: <!-- boolean -->
- `claims_task_complete`: <!-- boolean -->
- `claims_task_approved`: <!-- boolean -->
- `claims_human_review_replaced`: <!-- boolean -->
- `claims_merge_allowed`: <!-- boolean -->
- `claims_push_allowed`: <!-- boolean -->
- `claims_release_allowed`: <!-- boolean -->
- `claims_lifecycle_mutation_allowed`: <!-- boolean -->
- `authority_claim_result`: <!-- string: AUTHORITY_CLAIMS_CLEAR | AUTHORITY_CLAIMS_BLOCKED -->

## Warnings

<!-- list of strings -->

## Blockers

<!-- list of strings -->

## Handoff to 59.6 Verification Result / Output

- `handoff_to_result_output`: <!-- boolean -->

## Non-Authority Acknowledgement

- `non_authority_acknowledgement`: |
    This validation evidence result does not verify execution result.
    This validation evidence result does not approve task completion.
    This validation evidence result does not create approval.
    This validation evidence result does not authorize merge, push, or release.
    This validation evidence result does not mutate lifecycle state.
    This validation evidence result does not replace human review.
    This validation evidence result only checks validation and test evidence for later M59 result verification.

## Final Validation Evidence Status

- `validation_evidence_status_confirmed`: <!-- string: same as validation_evidence_status -->
