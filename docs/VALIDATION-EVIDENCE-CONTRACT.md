# Validation Evidence Contract

## Purpose

This contract defines the structure and evaluation rules for validation and test evidence in milestone M59. It outlines how validation artifacts, test logs, freshness parameters, relevance checks, and false PASS hazards are evaluated to confirm code correctness without assuming completion authority.

## Preconditions

The preconditions for establishing this contract are verified:
- `reports/m59-m58-completion-intake.md` exists and contains `MAY_PROCEED_TO_M59_VERIFICATION_PLANNING: true`.
- `docs/EXECUTION-RESULT-VERIFICATION-ARCHITECTURE.md` exists and contains `FINAL_STATUS: M59_ARCHITECTURE_DEFINED`.
- `docs/EXECUTION-RESULT-VERIFICATION-INPUT-CONTRACT.md` exists and contains `FINAL_STATUS: M59_EXECUTION_RESULT_VERIFICATION_INPUT_CONTRACT_DEFINED`.
- `docs/EXECUTION-RESULT-VERIFICATION-PRECONDITIONS-CONTRACT.md` exists and contains `FINAL_STATUS: M59_EXECUTION_RESULT_VERIFICATION_PRECONDITIONS_CONTRACT_DEFINED`.
- `docs/GIT-DIFF-SCOPE-VERIFICATION-CONTRACT.md` exists and contains `FINAL_STATUS: M59_GIT_DIFF_SCOPE_VERIFICATION_CONTRACT_DEFINED`.
- JSON schemas and templates for inputs, preconditions, and diff scope verification exist and are correct.
- `reports/m58-completion-review.md` exists.
- The approved task map ends at 59.14. No downstream task IDs beyond 59.14 exist.

## Position in M59

Validation Evidence Verification (59.5) runs in parallel or immediately after Git Diff and Scope Verification (59.4). It receives the handoff from preconditions (59.3) and processes the validation and testing logs. Its output is combined with the diff scope verification result in 59.6.

## Validation Evidence Artifact Role

The validation evidence artifact documents the analysis of actual logs, commands, and outputs from test runners and checkers. It confirms whether the checks actually executed, succeeded, and are relevant to the physical file changes.

## Required Fields

Every validation evidence result artifact must include the following properties:
- `validation_evidence_id`
- `task_id`
- `verification_input_id`
- `preconditions_id`
- `diff_scope_verification_id`
- `validation_evidence_status`
- `checked_at`
- `checked_by`
- `source_references`
- `validation_claim_check`
- `validation_command_check`
- `validation_artifact_check`
- `validation_exit_code_check`
- `validation_freshness_check`
- `validation_relevance_check`
- `test_claim_check`
- `test_command_check`
- `test_artifact_check`
- `test_exit_code_check`
- `test_freshness_check`
- `test_relevance_check`
- `missing_evidence_check`
- `stale_evidence_check`
- `wrong_validation_check`
- `authority_claim_check`
- `warnings`
- `blockers`
- `handoff_to_result_output`
- `non_authority_acknowledgement`

## Field Semantics

- **`validation_evidence_id`**: A unique string identifying the result artifact.
- **`task_id`**: Identifies the target task. Must match values in input, preconditions, and diff/scope results.
- **`verification_input_id`**: The ID of the input being analyzed.
- **`preconditions_id`**: The ID of the precondition checks being referenced.
- **`diff_scope_verification_id`**: The ID of the diff scope verification being referenced.
- **`validation_evidence_status`**: Final validation status.
- **`checked_at`**: Audit execution timestamp.
- **`checked_by`**: Agent descriptor (metadata).
- **`source_references`**: Collection of exact artifact paths checked.
- **`validation_claim_check`**: Analysis of claimed validation runs.
- **`validation_command_check`**: Checks validation commands executed.
- **`validation_artifact_check`**: Checks validation files and readability.
- **`validation_exit_code_check`**: Checks exit codes returned by validation.
- **`validation_freshness_check`**: Compares timestamps of validation logs with git changes.
- **`validation_relevance_check`**: Verifies if validation covers modified code.
- **`test_claim_check`**: Analysis of claimed test runs.
- **`test_command_check`**: Checks test commands executed.
- **`test_artifact_check`**: Checks test logs and readability.
- **`test_exit_code_check`**: Checks test runner exit codes.
- **`test_freshness_check`**: Compares timestamps of test logs with git changes.
- **`test_relevance_check`**: Verifies if tests target changed code.
- **`missing_evidence_check`**: Identifies and categorizes missing files.
- **`stale_evidence_check`**: Evaluates outdated check files.
- **`wrong_validation_check`**: Scans for wrong validations or wrong test commands.
- **`authority_claim_check`**: Scans files for illegal authority assertions.
- **`warnings`**: Minor non-blocking concerns.
- **`blockers`**: Major blocking violations.
- **`handoff_to_result_output`**: Boolean indicator to proceed to 59.6.
- **`non_authority_acknowledgement`**: Acknowledges structural limitations.

## Allowed Validation Evidence Statuses

The value of `validation_evidence_status` must be one of:
- `VALIDATION_EVIDENCE_CONFIRMED`: All checks are verified, relevant, fresh, and passing.
- `VALIDATION_EVIDENCE_CONFIRMED_WITH_WARNINGS`: Checks are verified, but non-blocking warnings are present.
- `VALIDATION_EVIDENCE_NOT_CONFIRMED`: Incomplete or missing evidence without active safety violations.
- `VALIDATION_EVIDENCE_BLOCKED`: Violations, failed tests, stale evidence, or authority claims detected.

## Validation Claim Rules

- Claimed validation must match physical logs.
- Falsely claiming validation passed without log files blocks verification.
- Contradictory claims block.

## Validation Command Rules

- Validation commands must be declared and match executed commands.
- Dangerous or unrelated shell commands block or warn depending on severity.

## Validation Artifact Rules

- Missing validation artifacts do not result in a PASS.
- Unreadable files block verification.
- References to non-existent files block.

## Validation Exit Code Rules

- All validation exit codes must be checked.
- Non-zero exit codes block verification unless explicitly whitelisted as non-blocking.
- Exit code 0 is an input value, never a final task completion approval.

## Validation Freshness Rules

- Timestamps of validation artifacts are compared to git diff modification times.
- Logs generated before the latest modifications are classified as stale and block.

## Validation Relevance Rules

- Validation commands must target the changed files.
- Unrelated validations do not count as proof.

## Test Claim Rules

- Claims of test execution must be backed by readable log artifacts.
- Test claim mismatches block verification.

## Test Command Rules

- Executed test commands must match declared commands.
- Running wrong or unrelated tests blocks clean verification.

## Test Artifact Rules

- Test logs must exist and be readable.
- Non-existent test log references block.

## Test Exit Code Rules

- Non-zero test runner exit codes block verification.
- Exit code 0 is required for a PASS, but does not constitute task approval.

## Test Freshness Rules

- Timestamps of test logs must be after the last git file modification.
- Stale logs block.

## Test Relevance Rules

- Tests must exercise the changed files or task scope.
- Unrelated test runs block.

## Missing Evidence Rules

- Missing evidence is never a PASS.
- Missing evidence with an explanation may yield `NOT_CONFIRMED` but never `CONFIRMED`.
- Falsely representing missing files as passing blocks.

## Stale Evidence Rules

- Outdated validation or test logs are rejected.
- Stale evidence affecting changed files blocks.

## Wrong Validation and Wrong Test Rules

- Executing incorrect commands or validating wrong scopes is treated as failure.
- Unrelated commands block.

## Authority Claim Rules

- Files, commits, and logs are scanned for authority claims.
- Claims of completed tasks, approved status, or merge authorization block.

## Warning and Blocker Semantics

- **Warnings**: Recorded in `warnings`. Do not halt flow but are reported.
- **Blockers**: Recorded in `blockers`. Halt flow, set final status to `VALIDATION_EVIDENCE_BLOCKED`, and set handoff flags to false.

## Handoff to 59.6 Verification Result / Output

- `handoff_to_result_output` is true if status is `CONFIRMED` or `CONFIRMED_WITH_WARNINGS`.
- Otherwise, it is false.

## Non-Authority Rules

Every validation evidence result artifact must acknowledge the following non-authority statements:
- `non_authority_acknowledgement` must contain the exact non-authority text defined in this contract.

## Malformed Validation Evidence Conditions

An artifact is malformed if required schema properties are missing, invalid JSON structures exist, or enum values are unrecognized.

## Unsafe Validation Evidence Conditions

Verification is unsafe and blocked if:
- Validation/tests claimed passed without actual evidence.
- Logs are stale or unexecuted.
- Non-zero exit codes exist.
- Unrelated or wrong tests were run.
- Authority assertions or git push/merge permissions are claimed.

## Relationship to 59.6 Verification Result / Output Contract

Once validation evidence checks pass, the outcomes are compiled into the final result output artifact for policy processing.

## Relationship to 59.7 Policy

Policy consumes the validation evidence result to determine the final verification decision.

## Forbidden Claims

The contract, schema, and template must not assert:
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

FINAL_STATUS: M59_VALIDATION_EVIDENCE_CONTRACT_DEFINED
