# Execution Result Verification Input

## Metadata

- `verification_input_id`: <!-- string: e.g. execution-result-verification-input-<task_id>-<YYYYMMDDHHMMSS> -->
- `task_id`: <!-- string -->
- `input_status`: <!-- string: EXECUTION_RESULT_VERIFICATION_INPUT_DRAFT | EXECUTION_RESULT_VERIFICATION_INPUT_READY_FOR_PRECONDITIONS | EXECUTION_RESULT_VERIFICATION_INPUT_BLOCKED -->
- `created_at`: <!-- string: timestamp -->
- `created_by`: <!-- string -->

## Source References

- `source_task_path`: <!-- string: path to task file -->
- `m58_completion_review_path`: `reports/m58-completion-review.md`
- `m59_intake_report_path`: `reports/m59-m58-completion-intake.md`
- `m59_architecture_path`: `docs/EXECUTION-RESULT-VERIFICATION-ARCHITECTURE.md`

## Execution Session Record Reference

- `execution_session_record_path`: <!-- string: path to record file -->
- `execution_session_record_status`: <!-- string: EXECUTION_SESSION_RECORD_READY_FOR_POLICY | EXECUTION_SESSION_RECORD_CLOSED_PENDING_M59_VERIFICATION | EXECUTION_SESSION_RECORD_BLOCKED | EXECUTION_SESSION_RECORD_ABORTED | UNKNOWN | MISSING -->

## Declared Result

- `summary`: <!-- string: summary of results -->
- `claimed_complete`: <!-- boolean: true/false -->
- `known_limitations`: <!-- array of strings -->
- `unresolved_items`: <!-- array of strings -->

## Declared Changes

- `files_changed`: <!-- array of strings -->
- `files_created`: <!-- array of strings -->
- `files_deleted`: <!-- array of strings -->
- `behavior_changed`: <!-- string -->
- `docs_changed`: <!-- array of strings -->
- `tests_changed`: <!-- array of strings -->

## Expected Scope

- `allowed_files`: <!-- array of strings -->
- `allowed_dirs`: <!-- array of strings -->
- `forbidden_files`: <!-- array of strings -->
- `forbidden_dirs`: <!-- array of strings -->
- `protected_paths`: <!-- array of strings -->
- `out_of_scope`: <!-- array of strings -->
- `scope_expansion_allowed`: false

## Actual Changed Files

- `source`: <!-- string: provided | git_diff | not_available -->
- `files`: <!-- array of strings -->
- `git_diff_available`: <!-- boolean: true/false -->

## Git Diff Evidence

- `diff_available`: <!-- boolean: true/false -->
- `diff_source`: <!-- string -->
- `diff_summary`: <!-- string -->
- `diff_artifact_path`: <!-- string -->

## Validation Evidence

- `claimed_validation_run`: <!-- boolean: true/false -->
- `validation_commands`: <!-- array of strings -->
- `validation_artifacts`: <!-- array of strings -->
- `validation_exit_codes`: <!-- array of integers -->
- `validation_summary`: <!-- string -->
- `validation_missing_reason`: <!-- string -->

## Test Evidence

- `claimed_tests_run`: <!-- boolean: true/false -->
- `test_commands`: <!-- array of strings -->
- `test_artifacts`: <!-- array of strings -->
- `test_exit_codes`: <!-- array of integers -->
- `test_summary`: <!-- string -->
- `tests_missing_reason`: <!-- string -->

## Forbidden Change Rules

- `no_approval_artifacts`: true
- `no_lifecycle_mutation`: true
- `no_merge_push_release`: true
- `no_human_review_replacement`: true
- `no_m60_cleanup_artifacts`: true

## Human Review Handoff

- `human_review_handoff_required`: true

## Non-Authority Acknowledgement

- `protected_paths_acknowledged`: true
- `non_authority_acknowledgement`: |
    This verification input does not verify execution result.
    This verification input does not approve task completion.
    This verification input does not create approval.
    This verification input does not authorize merge, push, or release.
    This verification input does not mutate lifecycle state.
    This verification input does not replace human review.
    This verification input only provides structured input for M59 verification precondition checks.

## Final Input Status

- `input_status_confirmed`: <!-- string: same as input_status -->
