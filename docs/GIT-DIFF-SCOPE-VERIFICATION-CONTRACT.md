# Git Diff and Scope Verification Contract

## Purpose

This contract defines the structure and rules for the Git Diff and Scope verification process in milestone M59. It specifies how actual repository changes, git diff summaries, and scope constraints are checked to ensure no unauthorized changes occurred.

## Preconditions

All preconditions for establishing this contract are verified:
- `reports/m59-m58-completion-intake.md` exists and contains `MAY_PROCEED_TO_M59_VERIFICATION_PLANNING: true`.
- `docs/EXECUTION-RESULT-VERIFICATION-ARCHITECTURE.md` exists and contains `FINAL_STATUS: M59_ARCHITECTURE_DEFINED`.
- `docs/EXECUTION-RESULT-VERIFICATION-INPUT-CONTRACT.md` exists and contains `FINAL_STATUS: M59_EXECUTION_RESULT_VERIFICATION_INPUT_CONTRACT_DEFINED`.
- `docs/EXECUTION-RESULT-VERIFICATION-PRECONDITIONS-CONTRACT.md` exists and contains `FINAL_STATUS: M59_EXECUTION_RESULT_VERIFICATION_PRECONDITIONS_CONTRACT_DEFINED`.
- JSON schemas and templates for inputs and preconditions exist and are correct.
- `reports/m58-completion-review.md` exists.
- The approved task map has not been expanded beyond 59.14.

## Position in M59

Git Diff and Scope Verification (59.4) is executed immediately after preconditions (59.3) pass. It receives the handoff from preconditions and evaluates the actual physical changes in the workspace. Its output feeds into validation evidence verification (59.5) and verification result/output (59.6).

## Diff / Scope Artifact Role

The Git Diff and Scope verification artifact documents the physical changes detected in the git repository and checks them against allowed features, folders, and protected directories. It determines whether the changes are legally within the task's scope.

## Required Fields

Every git diff and scope verification result must include the following properties:
- `diff_scope_verification_id`
- `task_id`
- `verification_input_id`
- `preconditions_id`
- `diff_scope_status`
- `checked_at`
- `checked_by`
- `source_references`
- `git_state_source`
- `actual_changed_files_check`
- `git_diff_summary_check`
- `declared_changes_comparison`
- `allowed_scope_check`
- `forbidden_scope_check`
- `protected_path_check`
- `out_of_scope_change_check`
- `deletion_check`
- `generated_artifact_check`
- `scope_expansion_check`
- `authority_claim_check`
- `warnings`
- `blockers`
- `handoff_to_validation_evidence_verification`
- `handoff_to_result_output`
- `non_authority_acknowledgement`

## Field Semantics

- **`diff_scope_verification_id`**: A unique string identifying the result artifact.
- **`task_id`**: Identifies the target task. Must match values in input and preconditions.
- **`verification_input_id`**: The ID of the input being analyzed.
- **`preconditions_id`**: The ID of the precondition checks being referenced.
- **`diff_scope_status`**: Final readiness status of the scope check.
- **`checked_at`**: Audit execution timestamp.
- **`checked_by`**: Agent descriptor (metadata).
- **`source_references`**: Collection of exact artifact paths checked.
- **`git_state_source`**: Source description of git status/diff data.
- **`actual_changed_files_check`**: Discovered list of changed, created, deleted, and renamed files.
- **`git_diff_summary_check`**: Git summary statistics (files changed, additions, deletions).
- **`declared_changes_comparison`**: Comparison between declared changes and actual git diff files.
- **`allowed_scope_check`**: Conformance score against allowed file paths.
- **`forbidden_scope_check`**: Compliance score against prohibited file paths.
- **`protected_path_check`**: Evaluation of changes touching protected files/folders.
- **`out_of_scope_change_check`**: Checks for files outside allowed scopes.
- **`deletion_check`**: Checks for file deletions and whether they were declared.
- **`generated_artifact_check`**: Audits for created artifacts, ensuring no approval/M60 cleanup files exist.
- **`scope_expansion_check`**: Verifies that any scope expansion is covered by human checkpoints.
- **`authority_claim_check`**: Scans changed files/commit logs for illegal authority assertions.
- **`warnings`**: Minor non-blocking concerns.
- **`blockers`**: Major blocking violations.
- **`handoff_to_validation_evidence_verification`**: Boolean indicator to proceed to 59.5.
- **`handoff_to_result_output`**: Boolean indicator to proceed to 59.6.
- **`non_authority_acknowledgement`**: Acknowledges structural limitations.

## Allowed Diff / Scope Statuses

The value of `diff_scope_status` must be one of:
- `SCOPE_VERIFICATION_PASS`: Changed files are within scope, all constraints satisfied.
- `SCOPE_VERIFICATION_PASS_WITH_WARNINGS`: Changed files within scope, but warnings were detected.
- `SCOPE_VERIFICATION_NOT_READY`: Missing information preventing complete scope evaluation.
- `SCOPE_VERIFICATION_BLOCKED`: Violations, unauthorized changes, or illegal authority assertions detected.

## Git State Source Rules

- `source_type` must be `provided`, `read_only_git_diff`, or `not_available`.
- Git diff/status queries run by downstream CLI tools must be read-only and must not modify index or stash states.
- If git state is unavailable, scope verification is blocked.

## Actual Changed Files Rules

- The validator compares the list of physical changed files from git status/diff against scope definitions.
- Empty list is allowed only under explicitly documented no-op or documentation-only scenarios.
- Unreadable or missing list blocks validation.

## Git Diff Summary Rules

- Git diff summaries must contain file counts, additions, and deletions.
- The summary checks for binary or unreadable modifications which require special policy overrides.

## Declared Changes Comparison Rules

- Declared files are compared against actual modified/created/deleted files.
- Undeclared actual changes generate warnings or blockers depending on policy.
- Declared changes that do not occur in git generate warnings.
- Large discrepancies block scope verification.

## Allowed Scope Rules

- All changed files must be matches within `allowed_files` or `allowed_dirs`.
- Any file modified outside allowed scope blocks verification unless manually whitelisted by an authorized human checkpoint.

## Forbidden Scope Rules

- Touching forbidden files or folders blocks scope verification.
- Prohibited file changes fail closed.

## Protected Path Rules

- Modifying files inside protected paths (e.g. M57/M58 reports, check scripts) blocks scope verification.
- Overrides are allowed only with an explicit human checkpoint.

## Out-of-Scope Change Rules

- Detects files modified outsideallowed regions.
- Out-of-scope files block scope verification.

## Deletion Rules

- File deletions must be declared.
- Unexpected deletions block scope verification.
- Deletions in protected paths block.

## Generated Artifact Rules

- Audits newly created files.
- Any generated approval artifact or lifecycle mutation metadata blocks verification.
- Any M60 cleanup/consolidation artifact created during M59 blocks.

## Scope Expansion Rules

- Scope expansion is prohibited.
- `scope_expansion_allowed` must be false. Claimed expansions without manual checkpoints block.

## Authority Claim Rules

- Changed files are scanned for illegal authority assertions.
- Any positive authority claim (e.g. claiming verified status or push authorization) blocks.

## Warning and Blocker Semantics

- **Warnings**: Recorded in `warnings`. Do not halt flow but are reported.
- **Blockers**: Recorded in `blockers`. Halt flow, set final status to `SCOPE_VERIFICATION_BLOCKED`, and set handoff flags to false.

## Handoff to 59.5 Validation Evidence Verification

- `handoff_to_validation_evidence_verification` is true if `diff_scope_status` is `SCOPE_VERIFICATION_PASS` or `SCOPE_VERIFICATION_PASS_WITH_WARNINGS`.
- Otherwise, it is false.

## Handoff to 59.6 Verification Result / Output

- `handoff_to_result_output` is true if `diff_scope_status` is `SCOPE_VERIFICATION_PASS` or `SCOPE_VERIFICATION_PASS_WITH_WARNINGS`.
- Otherwise, it is false.

## Non-Authority Rules

Every scope verification result artifact must acknowledge the following non-authority statements:
- `non_authority_acknowledgement` must contain the exact non-authority text defined in this contract.

## Malformed Diff / Scope Conditions

An artifact is malformed if required schema properties are missing, invalid JSON structures exist, or enum values are unrecognized.

## Unsafe Diff / Scope Conditions

Scope verification is unsafe and blocked if:
- Changed files are outside allowed scope.
- Forbidden scope or protected paths are touched.
- Undeclared deletions are present.
- M60 cleanup or approval artifacts exist prematurely.
- Scope expansion is declared without human reviews.
- Git actions or authority assertions are claimed.

## Relationship to 59.5 Validation Evidence Contract

Once scope verification is clean, control hands off to 59.5 to run validation evidence evaluation (test run and logs validation).

## Relationship to 59.6 Verification Result / Output Contract

Once scope verification is clean, the details are compiled into the final result output artifact for policy processing.

## Relationship to 59.7 Policy

Policy consumes the scope verification result to determine the final verification decision.

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

FINAL_STATUS: M59_GIT_DIFF_SCOPE_VERIFICATION_CONTRACT_DEFINED
