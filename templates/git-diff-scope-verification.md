# Git Diff and Scope Verification

## Metadata

- `diff_scope_verification_id`: <!-- string: e.g. git-diff-scope-verification-<task_id>-<timestamp> -->
- `task_id`: <!-- string -->
- `verification_input_id`: <!-- string -->
- `preconditions_id`: <!-- string -->
- `diff_scope_status`: <!-- string: SCOPE_VERIFICATION_PASS | SCOPE_VERIFICATION_PASS_WITH_WARNINGS | SCOPE_VERIFICATION_NOT_READY | SCOPE_VERIFICATION_BLOCKED -->
- `checked_at`: <!-- string: timestamp -->
- `checked_by`: <!-- string -->

## Source References

- `m59_intake_report_path`: `reports/m59-m58-completion-intake.md`
- `m59_architecture_path`: `docs/EXECUTION-RESULT-VERIFICATION-ARCHITECTURE.md`
- `input_contract_path`: `docs/EXECUTION-RESULT-VERIFICATION-INPUT-CONTRACT.md`
- `preconditions_contract_path`: `docs/EXECUTION-RESULT-VERIFICATION-PRECONDITIONS-CONTRACT.md`
- `verification_input_path`: <!-- string: path to input file -->
- `verification_preconditions_path`: <!-- string: path to preconditions file -->
- `source_task_path`: <!-- string -->
- `execution_session_record_path`: <!-- string -->

## Git State Source

- `source_type`: <!-- string: provided | read_only_git_diff | not_available -->
- `git_diff_available`: <!-- boolean -->
- `git_status_available`: <!-- boolean -->
- `diff_source_description`: <!-- string -->
- `generated_at`: <!-- string -->

## Actual Changed Files Check

- `changed_files_present`: <!-- boolean -->
- `changed_files`: <!-- array of strings -->
- `created_files`: <!-- array of strings -->
- `modified_files`: <!-- array of strings -->
- `deleted_files`: <!-- array of strings -->
- `renamed_files`: <!-- array of strings -->
- `actual_changed_files_result`: <!-- string: ACTUAL_CHANGED_FILES_MATCH_INPUT | ACTUAL_CHANGED_FILES_MATCH_WITH_WARNINGS | ACTUAL_CHANGED_FILES_NOT_READY | ACTUAL_CHANGED_FILES_BLOCKED -->

## Git Diff Summary Check

- `diff_summary_present`: <!-- boolean -->
- `files_changed_count`: <!-- integer -->
- `additions_present`: <!-- boolean -->
- `deletions_present`: <!-- boolean -->
- `binary_or_unreadable_changes_present`: <!-- boolean -->
- `git_diff_summary_result`: <!-- string: GIT_DIFF_SUMMARY_READY | GIT_DIFF_SUMMARY_READY_WITH_WARNINGS | GIT_DIFF_SUMMARY_NOT_READY | GIT_DIFF_SUMMARY_BLOCKED -->

## Declared Changes Comparison

- `declared_files_changed`: <!-- array of strings -->
- `actual_files_changed`: <!-- array of strings -->
- `undeclared_actual_changes`: <!-- array of strings -->
- `declared_but_missing_changes`: <!-- array of strings -->
- `declared_vs_actual_result`: <!-- string: DECLARED_CHANGES_MATCH_ACTUAL | DECLARED_CHANGES_MATCH_WITH_WARNINGS | DECLARED_CHANGES_DO_NOT_MATCH | DECLARED_CHANGES_COMPARISON_NOT_READY | DECLARED_CHANGES_COMPARISON_BLOCKED -->

## Allowed Scope Check

- `allowed_files`: <!-- array of strings -->
- `allowed_dirs`: <!-- array of strings -->
- `files_within_allowed_scope`: <!-- boolean -->
- `files_outside_allowed_scope`: <!-- array of strings -->
- `allowed_scope_result`: <!-- string: ALLOWED_SCOPE_PASS | ALLOWED_SCOPE_PASS_WITH_WARNINGS | ALLOWED_SCOPE_NOT_READY | ALLOWED_SCOPE_BLOCKED -->

## Forbidden Scope Check

- `forbidden_files`: <!-- array of strings -->
- `forbidden_dirs`: <!-- array of strings -->
- `forbidden_files_touched`: <!-- array of strings -->
- `forbidden_dirs_touched`: <!-- array of strings -->
- `forbidden_scope_result`: <!-- string: FORBIDDEN_SCOPE_CLEAR | FORBIDDEN_SCOPE_WARNING | FORBIDDEN_SCOPE_BLOCKED | FORBIDDEN_SCOPE_NOT_READY -->

## Protected Path Check

- `protected_paths`: <!-- array of strings -->
- `protected_paths_touched`: <!-- array of strings -->
- `protected_path_override_present`: <!-- boolean -->
- `protected_path_human_checkpoint_present`: <!-- boolean -->
- `protected_path_result`: <!-- string: PROTECTED_PATHS_CLEAR | PROTECTED_PATHS_WARNING | PROTECTED_PATHS_BLOCKED | PROTECTED_PATHS_NOT_READY -->

## Out-of-Scope Change Check

- `out_of_scope_rules_present`: <!-- boolean -->
- `out_of_scope_files_detected`: <!-- array of strings -->
- `out_of_scope_change_result`: <!-- string: OUT_OF_SCOPE_CLEAR | OUT_OF_SCOPE_WARNING | OUT_OF_SCOPE_BLOCKED | OUT_OF_SCOPE_NOT_READY -->

## Deletion Check

- `deleted_files`: <!-- array of strings -->
- `deleted_files_declared`: <!-- array of strings -->
- `unexpected_deletions`: <!-- array of strings -->
- `deletion_check_result`: <!-- string: DELETIONS_CLEAR | DELETIONS_WARNING | DELETIONS_BLOCKED | DELETIONS_NOT_READY -->

## Generated Artifact Check

- `generated_files`: <!-- array of strings -->
- `expected_generated_files`: <!-- array of strings -->
- `unexpected_generated_files`: <!-- array of strings -->
- `m60_cleanup_artifacts_detected`: <!-- boolean -->
- `approval_artifacts_detected`: <!-- boolean -->
- `lifecycle_artifacts_detected`: <!-- boolean -->
- `generated_artifact_result`: <!-- string: GENERATED_ARTIFACTS_CLEAR | GENERATED_ARTIFACTS_WARNING | GENERATED_ARTIFACTS_BLOCKED | GENERATED_ARTIFACTS_NOT_READY -->

## Scope Expansion Check

- `scope_expansion_claimed`: <!-- boolean -->
- `scope_expansion_allowed`: <!-- boolean -->
- `human_checkpoint_present`: <!-- boolean -->
- `scope_expansion_result`: <!-- string: SCOPE_EXPANSION_CLEAR | SCOPE_EXPANSION_WARNING | SCOPE_EXPANSION_BLOCKED | SCOPE_EXPANSION_NOT_READY -->

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

## Handoff to 59.5 Validation Evidence Verification

- `handoff_to_validation_evidence_verification`: <!-- boolean -->

## Handoff to 59.6 Verification Result / Output

- `handoff_to_result_output`: <!-- boolean -->

## Non-Authority Acknowledgement

- `non_authority_acknowledgement`: |
    This git diff and scope verification result does not approve task completion.
    This git diff and scope verification result does not verify validation or test evidence.
    This git diff and scope verification result does not create approval.
    This git diff and scope verification result does not authorize merge, push, or release.
    This git diff and scope verification result does not mutate lifecycle state.
    This git diff and scope verification result does not replace human review.
    This git diff and scope verification result only checks repository diff and scope evidence for later M59 result verification.

## Final Diff / Scope Status

- `diff_scope_status_confirmed`: <!-- string: same as diff_scope_status -->
