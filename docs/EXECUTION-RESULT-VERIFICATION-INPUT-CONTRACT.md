# Execution Result Verification Input Contract

## Purpose

This contract defines the structure and semantics of the Verification Input artifact submitted for M59 execution result verification. The contract specifies all required properties, allowed statuses, validation rules, and boundaries to ensure that results can be checked deterministically.

## Preconditions

The preconditions for establishing this contract are met:
- `reports/m59-m58-completion-intake.md` exists and contains `MAY_PROCEED_TO_M59_VERIFICATION_PLANNING: true`.
- `docs/EXECUTION-RESULT-VERIFICATION-ARCHITECTURE.md` exists and contains `FINAL_STATUS: M59_ARCHITECTURE_DEFINED`.
- The approved task map ends at 59.14. No downstream task IDs beyond 59.14 exist.

## Position in M59

The Verification Input Contract (59.2) defines the data contract that is populated after a controlled execution session completes. The populated input is then consumed by the Verification Preconditions Contract (59.3) and downstream checking modules.

## Verification Input Artifact Role

The verification input artifact serves as a structured declaration by the developer agent of what was changed and what evidence supports those changes. It packages metadata, references, declarations, and proof files for automated policy evaluation.

## Required Fields

Every verification input artifact must contain the following fields:
- `verification_input_id`
- `task_id`
- `input_status`
- `created_at`
- `created_by`
- `source_task_path`
- `m58_completion_review_path`
- `m59_intake_report_path`
- `m59_architecture_path`
- `execution_session_record_path`
- `execution_session_record_status`
- `declared_result`
- `declared_changes`
- `expected_scope`
- `actual_changed_files`
- `git_diff_evidence`
- `validation_evidence`
- `test_evidence`
- `forbidden_change_rules`
- `protected_paths_acknowledged`
- `human_review_handoff_required`
- `non_authority_acknowledgement`

## Field Semantics

- **`verification_input_id`**: A unique string identifying the artifact (e.g. `execution-result-verification-input-<task_id>-<timestamp>`).
- **`task_id`**: The ID of the task being verified.
- **`input_status`**: The state of the input submission.
- **`created_at`**: Creation timestamp.
- **`created_by`**: Agent identifier who prepared the submission (metadata only).
- **`source_task_path`**: Path to the active task definition.
- **`m58_completion_review_path`**: Must reference `reports/m58-completion-review.md`.
- **`m59_intake_report_path`**: Must reference `reports/m59-m58-completion-intake.md`.
- **`m59_architecture_path`**: Must reference `docs/EXECUTION-RESULT-VERIFICATION-ARCHITECTURE.md`.
- **`execution_session_record_path`**: Path to the execution session record generated in M58.
- **`execution_session_record_status`**: State of the execution session record.
- **`declared_result`**: Claims about task completeness and limitations.
- **`declared_changes`**: Claims about which files were changed.
- **`expected_scope`**: Path restrictions and rules for the task.
- **`actual_changed_files`**: List of files physically modified/created.
- **`git_diff_evidence`**: References to git diff files/summaries.
- **`validation_evidence`**: Proof of validation command runs.
- **`test_evidence`**: Proof of unit/integration test runs.
- **`forbidden_change_rules`**: Structural safety constraints.
- **`protected_paths_acknowledged`**: Indication that protected directory constraints are accepted.
- **`human_review_handoff_required`**: Acknowledgement that human gates are mandatory.
- **`non_authority_acknowledgement`**: Standard non-authority text.

## Allowed Input Statuses

The value of `input_status` must be one of:
- `EXECUTION_RESULT_VERIFICATION_INPUT_DRAFT`: The submission is incomplete and must not proceed to 59.3.
- `EXECUTION_RESULT_VERIFICATION_INPUT_READY_FOR_PRECONDITIONS`: The submission is complete and may proceed to 59.3.
- `EXECUTION_RESULT_VERIFICATION_INPUT_BLOCKED`: The submission is invalid or blocked and must not proceed.

## Source Reference Rules

- All source paths must resolve cleanly within the repository root.
- The `m58_completion_review_path`, `m59_intake_report_path`, and `m59_architecture_path` must match their exact physical paths in the repo.
- Path traversal (e.g. `../`) is strictly prohibited.

## Execution Session Record Rules

- `execution_session_record_path` must reference a valid, existing execution session record.
- If `execution_session_record_status` is not `EXECUTION_SESSION_RECORD_CLOSED_PENDING_M59_VERIFICATION`, the verification check must fail closed.
- Status values like `EXECUTION_SESSION_RECORD_BLOCKED`, `EXECUTION_SESSION_RECORD_ABORTED`, `UNKNOWN`, or `MISSING` block verification.

## Declared Result Rules

- The `declared_result` contains the developer agent's claims.
- `claimed_complete: true` is treated as a claim only, and does not constitute verification.
- Summary must not be empty. Known limitations and unresolved items must be declared.

## Declared Changes Rules

- Developer agents must explicitly declare all added, modified, or deleted files.
- The declared list is compared against actual git changes in downstream validation steps.
- Missing declarations prevent successful verification.

## Expected Scope Rules

- Defines `allowed_files` and `allowed_dirs`.
- Requires `forbidden_files`, `forbidden_dirs`, `protected_paths`, and `out_of_scope` to be declared.
- `scope_expansion_allowed` must be `false`. Scope expansion is prohibited without manual human review overrides.

## Actual Changed Files Rules

- `source` must be `provided`, `git_diff`, or `not_available`.
- If `source` is `git_diff`, downstream CLI tools will compute the changed files using standard, read-only git commands.
- If `source` is `not_available`, verification is blocked.

## Git Diff Evidence Rules

- `diff_available` must be `true` for a clean PASS.
- The diff artifact must reside in a valid path inside the repository root.
- Diff evidence is not an authorization to proceed.

## Validation Evidence Rules

- Developer agents must reference validation logs and files.
- `claimed_validation_run: true` alone is not proof; logs must be parsed.
- Stale or missing validation evidence results in a fail-closed decision.

## Test Evidence Rules

- Developer agents must reference test runner output logs.
- Wrong or unexecuted tests result in a fail-closed decision.
- Freshness checks must align timestamps of tests with the latest commit.

## Forbidden Change Rules

The contract enforces these static safety checks:
- `no_approval_artifacts`: true (no approval files may be created/modified by the task)
- `no_lifecycle_mutation`: true (no lifecycle state changes may be performed)
- `no_merge_push_release`: true (no merges, pushes, or releases may be performed)
- `no_human_review_replacement`: true (cannot claim human review is replaced)
- `no_m60_cleanup_artifacts`: true (no M60 cleanup files may be created)

Any disabled rules (set to false) block verification.

## Human Review Handoff Rules

- `human_review_handoff_required` must be `true`.
- Automated result verification does not replace human review.

## Non-Authority Rules

Every verification input artifact must acknowledge the following non-authority statements:
- `protected_paths_acknowledged`: true
- The `non_authority_acknowledgement` must contain the exact non-authority text defined in this contract.

## Malformed Input Conditions

An input is classified as malformed if:
- Any required top-level or nested properties are missing.
- Schema validation fails (e.g. invalid type, extra fields).
- Values do not match allowed enums.

## Unsafe Input Conditions

An input is classified as unsafe if:
- It claims verification is already complete.
- It asserts task completion or approvals.
- It attempts to authorize pushes, merges, or releases.
- It sets `human_review_handoff_required: false`.
- It sets `protected_paths_acknowledged: false`.
- It attempts to set `scope_expansion_allowed: true` without an authorized human checkpoint.

## Relationship to 59.3 Preconditions

The 59.3 Preconditions Contract consumes the populated verification input. Preconditions check the physical existence and formatting of all referenced artifacts prior to running git diff and test log validations.

## Forbidden Claims

The contract, schemas, and templates must not assert:
- EXECUTION_RESULT_VERIFIED must not be set to true
- RESULT_VERIFIED must not be set to true
- TASK_COMPLETE must not be set to true
- TASK_APPROVED must not be set to true
- PUSH_ALLOWED must not be set to true
- MERGE_ALLOWED must not be set to true
- RELEASE_ALLOWED must not be set to true
- LIFECYCLE_MUTATION_ALLOWED must not be set to true
- HUMAN_REVIEW_REPLACED must not be set to true

## Final Contract Status

FINAL_STATUS: M59_EXECUTION_RESULT_VERIFICATION_INPUT_CONTRACT_DEFINED
