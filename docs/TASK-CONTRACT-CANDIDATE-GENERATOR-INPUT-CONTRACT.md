# Task Contract Candidate Generator Input Contract

## Purpose
Define the M51 input contract for future generator usage so generation stays compatible with M50 boundaries and validator shape.

## Input Boundary
Generator input contract defines structure and rules only.
It does not implement generation.
It does not create generated artifacts.
It does not create examples.
It does not create fixtures.
It does not create queue entries.
It does not modify active task state.
It does not authorize implementation.

## Relationship to M51 Architecture
This contract follows docs/TASK-CONTRACT-CANDIDATE-GENERATOR-ARCHITECTURE.md and formalizes the required input shape and boundary controls.

## Required Input Shape
```yaml
generator_input:
  input_id:
  generator_input_status:
  source_conversion_package:
  source_task_contract_proposal:
  source_authorization:
  source_candidate_template:
  source_conversion_policy:
  source_validator: scripts/validate-proposal-to-task-conversion.py
  generation_mode:
  output_target:
  primary_output_format: generated_conversion_package_with_embedded_candidate
  primary_validator_target:
  carry_forward:
    accepted_limitations:
    open_questions:
    downstream_limits:
    non_authority_boundary:
  boundaries:
    dry_run_required: true
    write_to_staging_only: true
    active_task_write_allowed: false
    queue_write_allowed: false
    execution_authorized: false
    approval_record_creation_allowed: false
```

## Required Fields
- input_id
- generator_input_status
- source_conversion_package
- source_task_contract_proposal
- source_authorization
- source_candidate_template
- source_conversion_policy
- source_validator
- generation_mode
- output_target
- primary_output_format
- primary_validator_target
- carry_forward
- carry_forward.accepted_limitations
- carry_forward.open_questions
- carry_forward.downstream_limits
- carry_forward.non_authority_boundary
- boundaries
- boundaries.dry_run_required
- boundaries.write_to_staging_only
- boundaries.active_task_write_allowed
- boundaries.queue_write_allowed
- boundaries.execution_authorized
- boundaries.approval_record_creation_allowed

## Field Semantics
primary_validator_target may be null in dry-run mode.

primary_validator_target must be a string path only after write mode creates an actual generated artifact.

In dry-run mode:
- primary_validator_target must be null
- would_write_to is the predicted staging path

In write mode:
- primary_validator_target must equal the written generated artifact path

A schema that requires primary_validator_target to be a string in all modes is invalid, because dry-run mode must allow null.

Dry-run mode must not claim that a real validator target exists before a file is written.

Write mode may claim primary_validator_target only after the generated artifact exists in the staging area.

## Generator Input Statuses
Allowed statuses:
- GENERATOR_INPUT_READY
- GENERATOR_INPUT_READY_WITH_LIMITATIONS
- GENERATOR_INPUT_BLOCKED
- GENERATOR_INPUT_INVALID

GENERATOR_INPUT_READY means all required sources, carry-forward fields, output target, format, and boundaries are present and valid.

GENERATOR_INPUT_READY_WITH_LIMITATIONS means generation may proceed only if accepted limitations, open questions, downstream limits, and non-authority boundary are preserved.

GENERATOR_INPUT_BLOCKED means generation must not proceed because required authorization, source artifact, validator, output target, or boundary condition is missing or unsafe.

GENERATOR_INPUT_INVALID means the input is malformed, unsafe, contradictory, or requests forbidden behavior.

## Source Artifact Requirements
source_conversion_package is required.
source_task_contract_proposal is required.
source_authorization is required.
source_candidate_template is required.
source_conversion_policy is required.
source_validator is required.

source_validator must reference scripts/validate-proposal-to-task-conversion.py.
M51 generator input must preserve M50 validator compatibility.
M51 generator input must not define a new validator authority.

## M50 Validator Requirement
Generated output must be compatible with:

python3 scripts/validate-proposal-to-task-conversion.py --conversion <path>

M51 generated output must preserve the M50 conversion package shape expected by the M50 validator.

M51 must not generate a standalone candidate-only artifact as the primary validator target if M50 validator requires conversion_package + embedded task_contract_candidate.

source_validator: scripts/validate-proposal-to-task-conversion.py

## Primary Output Format Requirement
The primary output format must be generated_conversion_package_with_embedded_candidate.
Standalone candidate-only artifacts are not valid primary outputs in M51.
Primary generated artifact must preserve conversion_package plus embedded task_contract_candidate shape.

## Output Target Requirement
generated/task-contract-candidates/

output_target must resolve inside generated/task-contract-candidates/.
output_target must not resolve to tasks/active-task.md.
output_target must not resolve inside tasks/queue/.
output_target must not resolve inside approvals/.
output_target must not use path traversal.

Task 51.2 defines the output target contract only.
Task 51.2 does not create generated/.
Task 51.2 does not write generated artifacts.

## Dry-Run and Write Input Semantics
dry-run predicts would_write_to
write creates output_path
only write creates primary_validator_target

generation_mode values:
- dry_run
- write

dry_run is the default safe mode for the future generator.
write mode requires explicit --write and explicit --out in later CLI behavior.
Task 51.2 defines input semantics only and does not implement CLI behavior.

primary_validator_target must allow null for dry-run mode.
primary_validator_target must allow string path for write mode.

## Carry-Forward Requirements
Accepted limitations must be carried forward.
Open questions must be carried forward.
Downstream limits must be carried forward.
Non-authority boundary must be carried forward.
Source traceability must be preserved.

Carry-forward fields are required because generator behavior must not silently erase limitations, open questions, downstream limits, or non-authority boundaries inherited from M50.

## Boundary Flags
```yaml
boundaries:
  dry_run_required: true
  write_to_staging_only: true
  active_task_write_allowed: false
  queue_write_allowed: false
  execution_authorized: false
  approval_record_creation_allowed: false
```

dry_run_required must remain true.
write_to_staging_only must remain true.
active_task_write_allowed must remain false.
queue_write_allowed must remain false.
execution_authorized must remain false.
approval_record_creation_allowed must remain false.

## Blocking Conditions
- conversion package missing
- conversion package not validated
- source task contract proposal missing
- source authorization missing
- source candidate template missing
- source conversion policy missing
- source validator missing
- source validator does not reference M50 validator
- primary output format missing
- primary output format not M50-compatible
- standalone candidate-only artifact requested as primary output
- carry-forward fields missing
- accepted limitations missing
- open questions missing
- downstream limits missing
- non-authority boundary missing
- output target outside staging area
- active-task target requested
- queue target requested
- approvals target requested
- path traversal requested
- execution authorization claimed
- approval creation requested
- dry_run_required set to false
- write_to_staging_only set to false
- active_task_write_allowed set to true
- queue_write_allowed set to true
- execution_authorized set to true
- approval_record_creation_allowed set to true
- primary_validator_target forced to string-only schema
- primary_validator_target non-null in dry-run mode
- primary_validator_target missing or mismatched in write mode

## Template Boundary
templates/task-contract-candidate-generator-input.md must be a template only.
It must not contain a real conversion package reference as if created by this task.
It must not contain a real authorization record.
It must not contain a real generated artifact path as if written by this task.
It must not contain real approval evidence.

## Schema Contract
Schema file: schemas/task-contract-candidate-generator-input.schema.json

## Schema vs Semantic Validation Boundary
JSON Schema in Task 51.2 is structural, not a full semantic validator.

The schema allows primary_validator_target to be either string or null because both values are valid in different modes.

The schema does not have to enforce that primary_validator_target is null specifically when generation_mode is dry_run.

The schema does not have to enforce that primary_validator_target is a string specifically when generation_mode is write.

Those mode-specific constraints are semantic generator rules and must be enforced later by the generator implementation and fixtures.

Task 51.2 must document these constraints, but must not implement generator behavior.

Schema checks shape.
Generator later checks mode-specific semantics.

dry_run + primary_validator_target: null is a semantic rule.
write + primary_validator_target: string path is a semantic rule.

## Non-Authority Rules
Generator input readiness is not approval.
Generator input readiness does not authorize execution.
Generator input readiness does not authorize queue placement.
Generator input readiness does not authorize active-task replacement.
Generator input readiness does not authorize implementation.
Generator input readiness does not create generated artifacts.

Task 51.2 does not implement generator behavior.
Task 51.2 does not validate actual generation.
Task 51.2 does not create generated outputs.
Task 51.2 does not create examples.
Task 51.2 does not create fixtures.

## Explicit Non-Goals
Task 51.2 does not do:
- create generator output contract
- create generator policy
- create generator CLI
- create generator behavior
- create fixtures
- create examples
- create generated artifacts
- create queue entries
- modify tasks/active-task.md
- modify tasks/queue/
- create real approval records
- create files under approvals/
- authorize execution
- authorize queue placement
- authorize active-task replacement
- authorize implementation
- create evidence reports
- create lessons entries
- create completion reviews
- commit
- push
- merge
- deploy
- release
