# Execution Result Verification Result / Output Contract

## Purpose

This contract defines the structure and rules for the Verification Result / Output artifact in milestone M59. The contract specifies all output summary formats, field requirements, status evaluations, and boundaries required to document verification audits for downstream review.

## Preconditions

The preconditions for establishing this contract are verified:
- `reports/m59-m58-completion-intake.md` exists and contains `MAY_PROCEED_TO_M59_VERIFICATION_PLANNING: true`.
- `docs/EXECUTION-RESULT-VERIFICATION-ARCHITECTURE.md` exists and contains `FINAL_STATUS: M59_ARCHITECTURE_DEFINED`.
- `docs/EXECUTION-RESULT-VERIFICATION-INPUT-CONTRACT.md` exists and contains `FINAL_STATUS: M59_EXECUTION_RESULT_VERIFICATION_INPUT_CONTRACT_DEFINED`.
- `docs/EXECUTION-RESULT-VERIFICATION-PRECONDITIONS-CONTRACT.md` exists and contains `FINAL_STATUS: M59_EXECUTION_RESULT_VERIFICATION_PRECONDITIONS_CONTRACT_DEFINED`.
- `docs/GIT-DIFF-SCOPE-VERIFICATION-CONTRACT.md` exists and contains `FINAL_STATUS: M59_GIT_DIFF_SCOPE_VERIFICATION_CONTRACT_DEFINED`.
- `docs/VALIDATION-EVIDENCE-CONTRACT.md` exists and contains `FINAL_STATUS: M59_VALIDATION_EVIDENCE_CONTRACT_DEFINED`.
- JSON schemas and templates for inputs, preconditions, scope checks, and validation evidence exist and are correct.
- `reports/m58-completion-review.md` exists.
- The approved task map has not been expanded beyond 59.14.

## Position in M59

Verification Result / Output Contract (59.6) consolidates all results generated during scope checks (59.4) and validation evidence audits (59.5). The output artifact represents the final verified output package that is consumed by policy validation (59.7) and verification CLI scripts (59.8).

## Result / Output Artifact Role

The Result / Output artifact records the programmatic audit conclusions. It compiles the summaries of preconditions, diff scope matching, test runner successes, and safety boundary compliance into a single structured report.

## Required Fields

Every result output artifact must contain the following fields:
- `verification_result_id`
- `task_id`
- `verification_input_id`
- `preconditions_id`
- `diff_scope_verification_id`
- `validation_evidence_id`
- `verification_result_status`
- `created_at`
- `created_by`
- `source_references`
- `preconditions_summary`
- `diff_scope_summary`
- `validation_evidence_summary`
- `declared_vs_actual_summary`
- `scope_compliance_summary`
- `validation_test_summary`
- `forbidden_change_summary`
- `authority_claim_summary`
- `human_review_handoff`
- `warnings`
- `blockers`
- `non_authority_acknowledgement`

## Field Semantics

- **`verification_result_id`**: A unique string identifying the result artifact (e.g. `execution-result-verification-output-<task_id>-<timestamp>`).
- **`task_id`**: Identifies the target task. Must match values in input, preconditions, scope, and evidence records.
- **`verification_input_id`**: Reference to input artifact.
- **`preconditions_id`**: Reference to preconditions result.
- **`diff_scope_verification_id`**: Reference to scope verification result.
- **`validation_evidence_id`**: Reference to validation evidence result.
- **`verification_result_status`**: Bounded verification decision classification.
- **`created_at`**: Creation timestamp.
- **`created_by`**: Agent descriptor (metadata).
- **`source_references`**: Collection of exact paths checked.
- **`preconditions_summary`**: Summary of precondition result checks.
- **`diff_scope_summary`**: Summary of repository change/scope checks.
- **`validation_evidence_summary`**: Summary of test run logs checks.
- **`declared_vs_actual_summary`**: Evaluation of declared vs actual workspace modifications.
- **`scope_compliance_summary`**: Compliance status of allowed and forbidden scopes.
- **`validation_test_summary`**: Summarizes test executions and exit codes.
- **`forbidden_change_summary`**: Checks for premature files and safety rule compliance.
- **`authority_claim_summary`**: Audits for authority claim violations.
- **`human_review_handoff`**: Structures data packaging for human gates.
- **`warnings`**: Minor concerns list.
- **`blockers`**: Major blocking issues list.
- **`non_authority_acknowledgement`**: Acknowledges structural limits.

## Allowed Verification Result Statuses

The `verification_result_status` must be one of:
- `EXECUTION_RESULT_VERIFIED`: Programmatic verification passes, handoff is ready.
- `EXECUTION_RESULT_VERIFIED_WITH_WARNINGS`: Verification passes with warnings, handoff is ready.
- `EXECUTION_RESULT_NOT_VERIFIED`: Information incomplete, checks unrun, or stale evidence. Handoff is not ready.
- `EXECUTION_RESULT_BLOCKED`: Major policy blockers, scope violations, failed tests, or authority claim failures. Handoff is blocked.

Important Boundary:
`EXECUTION_RESULT_VERIFIED` is not task approval, and does not authorize push, commit, merge, or release.

## Preconditions Summary Rules

- Summarizes preconditions (59.3).
- Must resolve `preconditions_result` to `PRECONDITIONS_ACCEPTED` or `PRECONDITIONS_ACCEPTED_WITH_WARNINGS` to proceed.
- Preconditions blocked forces `EXECUTION_RESULT_BLOCKED`.

## Diff / Scope Summary Rules

- Summarizes scope checks (59.4).
- Must resolve `diff_scope_result` to `DIFF_SCOPE_ACCEPTED` or `DIFF_SCOPE_ACCEPTED_WITH_WARNINGS`.
- `SCOPE_VERIFICATION_BLOCKED` forces `EXECUTION_RESULT_BLOCKED`.

## Validation Evidence Summary Rules

- Summarizes test evidence audits (59.5).
- Must resolve `validation_evidence_result` to `VALIDATION_EVIDENCE_ACCEPTED` or `VALIDATION_EVIDENCE_ACCEPTED_WITH_WARNINGS`.
- Outdated, missing, or blocked validation logs force `EXECUTION_RESULT_BLOCKED` or `EXECUTION_RESULT_NOT_VERIFIED`.

## Declared vs Actual Summary Rules

- Compares developer agent declared changes against physical git changes.
- Mismatches in created or modified files prevent clean verification.

## Scope Compliance Summary Rules

- Asserts that no forbidden files or protected paths were touched.
- Scope compliance result must be `SCOPE_COMPLIANCE_CONFIRMED` or `SCOPE_COMPLIANCE_CONFIRMED_WITH_WARNINGS` to pass.

## Validation and Test Summary Rules

- Confirms that validation exit codes and test runner exit codes were zero.
- Confirms freshness of evidence. Any stale or irrelevant logs block.

## Forbidden Change Summary Rules

- Confirms no approval files or lifecycle mutation metadata were modified.
- Confirms no M60 cleanup files exist prematurely. Any violation blocks.

## Authority Claim Summary Rules

- Confirms no authority assertions exist in logs or comments.
- Any positive claim blocks verification.

## Human Review Handoff Rules

- `human_review_required` must be true.
- `handoff_ready` is true only if status is `EXECUTION_RESULT_VERIFIED` or `EXECUTION_RESULT_VERIFIED_WITH_WARNINGS`.
- Handoff ready is false if status is `NOT_VERIFIED` or `BLOCKED`.
- Automated results do not replace human reviewers.

## Warning and Blocker Semantics

- **Warnings**: Recorded in `warnings`. Do not halt flow but are reported.
- **Blockers**: Recorded in `blockers`. Halt flow and set final status to `EXECUTION_RESULT_BLOCKED`.

## Non-Authority Rules

Every result output artifact must acknowledge the following non-authority statements:
- `non_authority_acknowledgement` must contain the exact non-authority text defined in this contract.

## Malformed Result / Output Conditions

An artifact is malformed if required schema fields are missing, invalid JSON structures exist, or enum checks fail.

## Unsafe Result / Output Conditions

The result output is unsafe and blocked if:
- Output asserts task approval or replaces human reviewers.
- Outputs authorize push, merge, or release.
- Output bypasses blocked precondition, scope, or evidence states.
- Output marks result verified despite missing, stale, or wrong tests.

## Relationship to 59.7 Policy

Policy validates the populated verification result output against strict rules to decide the final milestone state.

## Relationship to 59.8 CLI

The verification CLI script checks inputs, preconditions, scope results, and validation evidence to write the result output artifact.

## Forbidden Claims

The contract, schemas, and templates must not assert:
- TASK_COMPLETE must not be set to true
- TASK_APPROVED must not be set to true
- PUSH_ALLOWED must not be set to true
- MERGE_ALLOWED must not be set to true
- RELEASE_ALLOWED must not be set to true
- LIFECYCLE_MUTATION_ALLOWED must not be set to true
- HUMAN_REVIEW_REPLACED must not be set to true

## Final Contract Status

FINAL_STATUS: M59_EXECUTION_RESULT_VERIFICATION_RESULT_OUTPUT_CONTRACT_DEFINED
