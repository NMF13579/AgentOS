# Proposal-to-Task Conversion Validation

## Purpose

Define deterministic validation for proposal-to-task conversion packages and candidate boundary compliance in M50.

## Validator Boundary

Conversion validator checks whether conversion is valid.
Conversion validator does not authorize execution.
Conversion validator does not place task into queue.
Conversion validator does not create active task state.
Conversion validator does not create approval records.
Conversion validator PASS is not approval.

## CLI

- `python3 scripts/validate-proposal-to-task-conversion.py --conversion <path>`
- `python3 scripts/validate-proposal-to-task-conversion.py --fixtures`
- `python3 scripts/validate-proposal-to-task-conversion.py --explain`
- `python3 scripts/validate-proposal-to-task-conversion.py --json --conversion <path>`
- `python3 scripts/validate-proposal-to-task-conversion.py --json --fixtures`

## Result Tokens

- `PROPOSAL_TO_TASK_CONVERSION_VALIDATION_OK`
- `PROPOSAL_TO_TASK_CONVERSION_VALIDATION_FAILED`
- `PROPOSAL_TO_TASK_CONVERSION_VALIDATION_BLOCKED`

## Exit Semantics

- `PROPOSAL_TO_TASK_CONVERSION_VALIDATION_OK` => exit `0`
- `PROPOSAL_TO_TASK_CONVERSION_VALIDATION_FAILED` => exit `1`
- `PROPOSAL_TO_TASK_CONVERSION_VALIDATION_BLOCKED` => exit `2`

## Non-Authority Markers

- `VALIDATOR_CREATES_NO_APPROVAL_RECORD`
- `VALIDATOR_DOES_NOT_AUTHORIZE_EXECUTION`
- `VALIDATOR_DOES_NOT_PLACE_TASK_IN_QUEUE`
- `VALIDATOR_DOES_NOT_MODIFY_ACTIVE_TASK`
- `VALIDATOR_DOES_NOT_START_IMPLEMENTATION`

## Required Checks

- conversion package structure and required field labels
- conversion input status classification
- source proposal and proposal validation state checks
- human authorization type, status, scope, and expiration checks
- candidate mode and candidate boundary flag checks
- carry-forward preservation checks
- forbidden weakening/expansion pattern checks
- validator non-authority behavior checks

## Authorization Checks

- `authorization_type` must be `proposal_to_task_contract_candidate_conversion`
- `authorization_status` must be `AUTHORIZATION_VALID`
- `expires_at` must exist and be valid at validator runtime
- `authorized_scope` and `not_authorized` must exist
- authorization reference must match source proposal chain
- authorization provenance fields must reject agent/self/auto/simulated/generated/synthetic/validator/script/system-inferred

Deterministic fixture expiration:
- Positive fixtures use `expires_at: 2099-12-31T23:59:59Z`
- Expired negative fixtures use `expires_at: 2000-01-01T00:00:00Z`

This far-future value is only for deterministic tests, not a recommendation for real production authorization expiry policy.

## Candidate Boundary Checks

- mode must be `EXECUTION_SHAPE`
- mode must not be `EXECUTION`
- boundaries must enforce conversion true flags and execution/placement false flags
- candidate text must not claim execution approval, queue placement, active-task replacement, or implementation approval

## Carry-Forward Checks

- `accepted_limitations` must exist and be non-empty
- `open_questions` must exist and be non-empty
- `downstream_limits` must exist and be non-empty
- `non_authority_boundary` must exist and be non-empty
- source traceability must be present

## Fixture Strategy

- fixtures are markdown files under `tests/fixtures/proposal-to-task-conversion/positive` and `negative`
- each fixture includes `fixture_name`, `fixture_type`, `expected_result`
- `--fixtures` validates all fixtures and compares actual result with expected result
- fixture run returns OK only if all fixture expectations match

## JSON Output Contract

All JSON outputs include:
- `result`
- `exit_code`
- `mode`
- `checked_path`
- `findings`
- `warnings`
- `non_authority_markers`

For `--fixtures --json`, output also includes:
- `fixture_summary`
- `fixtures`

Each fixture item includes:
- `path`
- `expected_result`
- `actual_result`
- `passed`
- `findings`

## Blocking vs Failed Semantics

FAILED means the conversion package is structurally invalid, semantically invalid, or violates M50 boundaries.
BLOCKED means validation cannot proceed because required authorization, inputs, fixtures, or readable files are missing.
OK means the conversion package passes M50 validation but still does not authorize execution.

## Side-Effect Prohibition

Validator runtime is read-only.
Validator must not create, modify, infer, or simulate approval records.
Validator must not write files under `approvals/`, `tasks/active-task.md`, `tasks/queue/`, `reports/`, or `examples/`.
Patterns like `approval_record_creation_allowed: true` or validator-created approval claims are treated as validation failure.

## Explicit Non-Goals

- authorize execution
- authorize queue placement
- authorize active-task replacement
- create approval records
- create active tasks
- create queue entries
- start implementation
- create lifecycle transitions
