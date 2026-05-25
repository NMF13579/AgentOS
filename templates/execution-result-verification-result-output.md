# Execution Result Verification Result / Output

## Metadata

- `verification_result_id`: <!-- string: e.g. execution-result-verification-output-<task_id>-<timestamp> -->
- `task_id`: <!-- string -->
- `verification_input_id`: <!-- string -->
- `preconditions_id`: <!-- string -->
- `diff_scope_verification_id`: <!-- string -->
- `validation_evidence_id`: <!-- string -->
- `verification_result_status`: <!-- string: EXECUTION_RESULT_VERIFIED | EXECUTION_RESULT_VERIFIED_WITH_WARNINGS | EXECUTION_RESULT_NOT_VERIFIED | EXECUTION_RESULT_BLOCKED -->
- `created_at`: <!-- string: timestamp -->
- `created_by`: <!-- string -->

## Source References

- `m59_intake_report_path`: `reports/m59-m58-completion-intake.md`
- `m59_architecture_path`: `docs/EXECUTION-RESULT-VERIFICATION-ARCHITECTURE.md`
- `input_contract_path`: `docs/EXECUTION-RESULT-VERIFICATION-INPUT-CONTRACT.md`
- `preconditions_contract_path`: `docs/EXECUTION-RESULT-VERIFICATION-PRECONDITIONS-CONTRACT.md`
- `diff_scope_contract_path`: `docs/GIT-DIFF-SCOPE-VERIFICATION-CONTRACT.md`
- `validation_evidence_contract_path`: `docs/VALIDATION-EVIDENCE-CONTRACT.md`
- `verification_input_path`: <!-- string: path to input file -->
- `verification_preconditions_path`: <!-- string: path to preconditions file -->
- `diff_scope_verification_path`: <!-- string: path to diff scope verification file -->
- `validation_evidence_path`: <!-- string: path to validation evidence file -->
- `source_task_path`: <!-- string -->
- `execution_session_record_path`: <!-- string -->

## Preconditions Summary

- `preconditions_status`: <!-- string -->
- `handoff_to_git_diff_scope_verification`: <!-- boolean -->
- `handoff_to_validation_evidence_verification`: <!-- boolean -->
- `warnings_count`: <!-- integer -->
- `blockers_count`: <!-- integer -->
- `preconditions_result`: <!-- string: PRECONDITIONS_ACCEPTED | PRECONDITIONS_ACCEPTED_WITH_WARNINGS | PRECONDITIONS_NOT_ACCEPTED | PRECONDITIONS_BLOCKED -->

## Diff / Scope Summary

- `diff_scope_status`: <!-- string -->
- `changed_files_count`: <!-- integer -->
- `out_of_scope_changes_detected`: <!-- boolean -->
- `forbidden_scope_touched`: <!-- boolean -->
- `protected_paths_touched`: <!-- boolean -->
- `scope_expansion_detected`: <!-- boolean -->
- `warnings_count`: <!-- integer -->
- `blockers_count`: <!-- integer -->
- `diff_scope_result`: <!-- string: DIFF_SCOPE_ACCEPTED | DIFF_SCOPE_ACCEPTED_WITH_WARNINGS | DIFF_SCOPE_NOT_ACCEPTED | DIFF_SCOPE_BLOCKED -->

## Validation Evidence Summary

- `validation_evidence_status`: <!-- string -->
- `validation_confirmed`: <!-- boolean -->
- `tests_confirmed`: <!-- boolean -->
- `missing_evidence_detected`: <!-- boolean -->
- `stale_evidence_detected`: <!-- boolean -->
- `wrong_validation_detected`: <!-- boolean -->
- `failed_validation_detected`: <!-- boolean -->
- `warnings_count`: <!-- integer -->
- `blockers_count`: <!-- integer -->
- `validation_evidence_result`: <!-- string: VALIDATION_EVIDENCE_ACCEPTED | VALIDATION_EVIDENCE_ACCEPTED_WITH_WARNINGS | VALIDATION_EVIDENCE_NOT_ACCEPTED | VALIDATION_EVIDENCE_BLOCKED -->

## Declared vs Actual Summary

- `declared_result_present`: <!-- boolean -->
- `declared_changes_present`: <!-- boolean -->
- `actual_changed_files_present`: <!-- boolean -->
- `undeclared_actual_changes`: <!-- boolean -->
- `declared_but_missing_changes`: <!-- boolean -->
- `declared_result_consistent_with_evidence`: <!-- boolean -->
- `declared_vs_actual_result`: <!-- string: DECLARED_VS_ACTUAL_MATCH | DECLARED_VS_ACTUAL_MATCH_WITH_WARNINGS | DECLARED_VS_ACTUAL_NOT_MATCHED | DECLARED_VS_ACTUAL_BLOCKED -->

## Scope Compliance Summary

- `allowed_scope_satisfied`: <!-- boolean -->
- `forbidden_scope_clear`: <!-- boolean -->
- `protected_paths_clear`: <!-- boolean -->
- `out_of_scope_clear`: <!-- boolean -->
- `scope_expansion_clear`: <!-- boolean -->
- `scope_compliance_result`: <!-- string: SCOPE_COMPLIANCE_CONFIRMED | SCOPE_COMPLIANCE_CONFIRMED_WITH_WARNINGS | SCOPE_COMPLIANCE_NOT_CONFIRMED | SCOPE_COMPLIANCE_BLOCKED -->

## Validation and Test Summary

- `validation_claims_supported`: <!-- boolean -->
- `test_claims_supported`: <!-- boolean -->
- `validation_exit_codes_pass`: <!-- boolean -->
- `test_exit_codes_pass`: <!-- boolean -->
- `validation_relevant`: <!-- boolean -->
- `tests_relevant`: <!-- boolean -->
- `evidence_fresh`: <!-- boolean -->
- `validation_test_result`: <!-- string: VALIDATION_TESTS_CONFIRMED | VALIDATION_TESTS_CONFIRMED_WITH_WARNINGS | VALIDATION_TESTS_NOT_CONFIRMED | VALIDATION_TESTS_BLOCKED -->

## Forbidden Change Summary

- `approval_artifacts_detected`: <!-- boolean -->
- `lifecycle_mutation_detected`: <!-- boolean -->
- `merge_push_release_detected`: <!-- boolean -->
- `human_review_replacement_detected`: <!-- boolean -->
- `m60_cleanup_artifacts_detected`: <!-- boolean -->
- `forbidden_change_result`: <!-- string: FORBIDDEN_CHANGES_CLEAR | FORBIDDEN_CHANGES_WARNING | FORBIDDEN_CHANGES_BLOCKED -->

## Authority Claim Summary

- `claims_result_verified_without_evidence`: <!-- boolean -->
- `claims_task_complete`: <!-- boolean -->
- `claims_task_approved`: <!-- boolean -->
- `claims_human_review_replaced`: <!-- boolean -->
- `claims_merge_allowed`: <!-- boolean -->
- `claims_push_allowed`: <!-- boolean -->
- `claims_release_allowed`: <!-- boolean -->
- `claims_lifecycle_mutation_allowed`: <!-- boolean -->
- `authority_claim_result`: <!-- string: AUTHORITY_CLAIMS_CLEAR | AUTHORITY_CLAIMS_BLOCKED -->

## Human Review Handoff

- `human_review_required`: true
- `handoff_ready`: <!-- boolean -->
- `handoff_reason`: <!-- string -->
- `review_notes`: <!-- string -->

## Warnings

<!-- list of strings -->

## Blockers

<!-- list of strings -->

## Non-Authority Acknowledgement

- `non_authority_acknowledgement`: |
    This verification result does not approve task completion.
    This verification result does not create approval.
    This verification result does not authorize merge, push, or release.
    This verification result does not mutate lifecycle state.
    This verification result does not replace human review.
    This verification result only records M59 execution result verification output for human review handoff.

## Final Verification Result Status

- `verification_result_status_confirmed`: <!-- string: same as verification_result_status -->
