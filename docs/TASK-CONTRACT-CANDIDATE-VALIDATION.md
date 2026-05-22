# Task Contract Candidate Validation CLI (M52)

## CLI Purpose

M52 candidate validator checks whether a generated conversion package with an embedded `task_contract_candidate` is valid for future M53 review input.

Candidate validator CLI is read-only.
Candidate validator CLI does not authorize execution.
Candidate validator CLI does not authorize queue placement.
Candidate validator CLI does not authorize active-task replacement.
Candidate validator CLI does not create lifecycle state.
Candidate validator CLI does not authorize M53 placement.

## CLI Modes

- `--candidate <path>`
- `--input <path>`
- `--fixtures`
- `--explain`
- `--json`

--candidate validates a generated conversion package artifact containing an embedded task_contract_candidate.
--input validates a candidate_validation_input package.
--candidate and --input are mutually exclusive.

## --candidate Behavior

- validates generated conversion package wrapper as primary artifact
- requires embedded `task_contract_candidate`
- rejects standalone candidate-only file as primary source when expected shape is `generated_conversion_package_with_embedded_candidate`
- validates required sections, carry-forward fields, non-authority boundary, and authority flags

## --input Behavior

- validates `candidate_validation_input` structure
- enforces `source_candidate_origin: M51_GENERATED_STAGING_ARTIFACT`
- enforces `validation_mode: M52_CANDIDATE_READINESS_VALIDATION`
- enforces `expected_candidate_shape: generated_conversion_package_with_embedded_candidate`
- enforces `downstream_target: M53_PLACEMENT_REVIEW`
- enforces `m51_origin.required: true` for M51 origin
- enforces boundary flags/authority fields as non-authorizing

## --fixtures Behavior

- checks internal fixture directory presence
- may return BLOCKED in Task 52.5 when fixture directory is absent

## --explain Behavior

- prints usage
- prints result token semantics
- prints read-only boundary
- prints non-authority markers

## --json Behavior

Validator JSON output goes to stdout only.
Any reports JSON file must be created by caller shell redirection.
The validator must not open, create, or modify reports/*.json directly.

## Result Tokens

- TASK_CONTRACT_CANDIDATE_VALIDATION_OK
- TASK_CONTRACT_CANDIDATE_VALIDATION_OK_WITH_LIMITATIONS
- TASK_CONTRACT_CANDIDATE_VALIDATION_FAILED
- TASK_CONTRACT_CANDIDATE_VALIDATION_BLOCKED

## Exit Code Semantics

- OK / OK_WITH_LIMITATIONS => exit 0
- FAILED => exit 1
- BLOCKED => exit 2

## Non-Authority Markers

Every result includes non-authority markers including:
- CANDIDATE_VALIDATION_IS_NOT_APPROVAL
- CANDIDATE_VALIDATION_DOES_NOT_AUTHORIZE_EXECUTION
- CANDIDATE_VALIDATION_DOES_NOT_AUTHORIZE_QUEUE_PLACEMENT
- CANDIDATE_VALIDATION_DOES_NOT_AUTHORIZE_ACTIVE_TASK_REPLACEMENT
- CANDIDATE_VALIDATION_DOES_NOT_CREATE_LIFECYCLE_STATE
- CANDIDATE_VALIDATION_REQUIRES_M53_PLACEMENT_REVIEW

## Authority Fields

These fields must always remain false:
- placement_authorized
- execution_authorized
- queue_write_allowed
- active_task_write_allowed
- approval_record_creation_allowed

## Candidate Wrapper Requirement

For M52 MVP, primary source must be generated conversion package wrapper with embedded candidate.
Standalone candidate-only primary artifact is rejected as BLOCKED.

## Input Package Requirements

`candidate_validation_input` must include required origin, mode, shape, downstream target, `m51_origin`, and non-authority boundary flags.

## Result Classification Rules

- OK / OK_WITH_LIMITATIONS: structurally valid and non-authority boundaries preserved
- FAILED: parseable candidate/input with rule violations
- BLOCKED: safety/lineage/shape ambiguity or unsupported invocation

## Known Limitations

- MVP parser uses deterministic marker checks.
- No fixture creation in 52.5.
- Missing `source_generated_artifact` fixture coverage belongs to 52.6.
- No real integration run against M51 artifact in 52.5.

## Allowed Command Examples

```bash
python3 scripts/validate-task-contract-candidate.py --candidate generated/task-contract-candidates/agent-action-review.generated-conversion-package.md
python3 scripts/validate-task-contract-candidate.py --input templates/task-contract-candidate-validation-input.md
python3 scripts/validate-task-contract-candidate.py --candidate generated/task-contract-candidates/agent-action-review.generated-conversion-package.md --json > reports/m52-candidate-validation-result-agent-action-review.json
python3 scripts/validate-task-contract-candidate.py --explain
```

## Forbidden Behavior Examples

- passing both `--candidate` and `--input`
- treating standalone candidate-only file as primary source
- treating `m53_review_input_candidate: true` as placement approval
- expecting validator to write any report file directly

## Non-Authority for OK

TASK_CONTRACT_CANDIDATE_VALIDATION_OK is not approval.
TASK_CONTRACT_CANDIDATE_VALIDATION_OK is not execution permission.
TASK_CONTRACT_CANDIDATE_VALIDATION_OK is not queue placement.
TASK_CONTRACT_CANDIDATE_VALIDATION_OK is not active-task replacement.
TASK_CONTRACT_CANDIDATE_VALIDATION_OK is not M53 placement authorization.
