# Task Contract Candidate Generator Output Contract

## Purpose
Define the output record contract for the future M51 generator while preserving M50 compatibility and non-authority boundaries.

## Output Boundary
This contract defines output record structure and rules only.
This task does not implement generator behavior.
This task does not create generated conversion packages.
This task does not create task contract candidates.
This task does not create examples.
This task does not create fixtures.
This task does not create queue entries.
This task does not modify active task state.
This task does not authorize implementation.

## Relationship to M51 Architecture
This output contract follows docs/TASK-CONTRACT-CANDIDATE-GENERATOR-ARCHITECTURE.md and formalizes dry-run and write output records.

## Relationship to Generator Input Contract
This output contract is downstream of docs/TASK-CONTRACT-CANDIDATE-GENERATOR-INPUT-CONTRACT.md and preserves its carry-forward and boundary requirements.

## Required Output Record Shape
```yaml
generated_task_contract_candidate_record:
  generation_id:
  source_conversion_package:
  source_generator_input:
  generated_conversion_package_path:
  generated_candidate_path:
  output_path:
  primary_validator_target:
  would_write_to:
  generation_mode:
  dry_run:
  written:
  validation_result:
  generated_at:
  generator_version:
  carry_forward_preserved:
    accepted_limitations:
    open_questions:
    downstream_limits:
    non_authority_boundary:
  boundaries:
    generated_candidate_is_active_task: false
    generated_candidate_is_queue_entry: false
    execution_authorized: false
    active_task_write_allowed: false
    queue_write_allowed: false
    approval_record_created: false
```

## Required Fields
- generation_id
- source_conversion_package
- source_generator_input
- generated_conversion_package_path
- generated_candidate_path
- output_path
- primary_validator_target
- would_write_to
- generation_mode
- dry_run
- written
- validation_result
- generated_at
- generator_version
- carry_forward_preserved
- carry_forward_preserved.accepted_limitations
- carry_forward_preserved.open_questions
- carry_forward_preserved.downstream_limits
- carry_forward_preserved.non_authority_boundary
- boundaries
- boundaries.generated_candidate_is_active_task
- boundaries.generated_candidate_is_queue_entry
- boundaries.execution_authorized
- boundaries.active_task_write_allowed
- boundaries.queue_write_allowed
- boundaries.approval_record_created

## Field Semantics
generated_conversion_package_path may be null in dry-run mode.

generated_conversion_package_path must be a string path only after write mode creates an actual generated conversion package artifact.

In M51, generated_candidate_path must be null.

M51 primary output is the generated conversion package, not a standalone candidate-only artifact.

generated_candidate_path may become non-null only in a later explicit task that authorizes secondary candidate-only artifacts.

output_path may be null in dry-run mode.

output_path must be a string path only after write mode creates an actual generated artifact.

primary_validator_target may be null in dry-run mode.

primary_validator_target must be a string path only after write mode creates an actual generated artifact.

would_write_to is required by schema.

In dry-run mode, would_write_to must contain the predicted staging path.

In write mode, would_write_to may equal output_path or be null, but must not be omitted.

In write mode, primary_validator_target must equal output_path.

In write mode, generated_conversion_package_path must equal output_path.

In write mode, primary_validator_target must point to the generated conversion package, not a standalone candidate-only artifact.

dry-run predicts would_write_to
write creates output_path
only write creates primary_validator_target

## Output Result States
Allowed validation_result states:
- TASK_CONTRACT_CANDIDATE_GENERATION_DRY_RUN_OK
- TASK_CONTRACT_CANDIDATE_GENERATION_WRITE_OK
- TASK_CONTRACT_CANDIDATE_GENERATION_FAILED
- TASK_CONTRACT_CANDIDATE_GENERATION_BLOCKED

TASK_CONTRACT_CANDIDATE_GENERATION_DRY_RUN_OK means the generator preview was produced without writing files.

TASK_CONTRACT_CANDIDATE_GENERATION_WRITE_OK means the generated conversion package was written to the allowed staging area.

TASK_CONTRACT_CANDIDATE_GENERATION_FAILED means generation completed with validation or semantic failure and must not be treated as successful output.

TASK_CONTRACT_CANDIDATE_GENERATION_BLOCKED means generation must not proceed because a required source, boundary, path, validator, or safety condition is missing or unsafe.

## M50 Validator Compatibility Requirement
Generated output must be compatible with:

python3 scripts/validate-proposal-to-task-conversion.py --conversion <path>

M51 generated output must preserve the M50 conversion package shape expected by the M50 validator.

M51 must not generate a standalone candidate-only artifact as the primary validator target if M50 validator requires conversion_package + embedded task_contract_candidate.

primary_validator_target must point to a generated conversion package with embedded task_contract_candidate.

primary_validator_target must not point to a standalone candidate-only artifact.

Generated conversion package must still pass M50 validator.

## Primary Generated Artifact Requirement
Primary generated artifact format:

generated/task-contract-candidates/<candidate-id>.generated-conversion-package.md

The primary generated artifact must be a generated conversion package with embedded task_contract_candidate.

Standalone candidate-only artifacts are not valid primary outputs in M51.

Optional secondary candidate-only artifacts are out of scope for Task 51.3 and require a future explicit task if ever introduced.

## Dry-Run Output Semantics
In dry-run mode:
- dry_run must be true
- written must be false
- output_path must be null
- generated_conversion_package_path must be null
- generated_candidate_path must be null
- primary_validator_target must be null
- would_write_to must contain the predicted staging path that would be written if --write were used

Dry-run predicted output path is not a written artifact.
Dry-run does not create lifecycle state.
Dry-run does not create primary_validator_target.
Dry-run does not create generated_conversion_package_path.

## Write Output Semantics
In write mode:
- dry_run must be false
- written must be true
- output_path must contain the actual generated artifact path
- generated_conversion_package_path must equal output_path
- generated_candidate_path must remain null in M51
- primary_validator_target must equal output_path
- would_write_to may equal output_path or be null if output_path is present
- would_write_to must not be omitted because the schema requires the field

Write to staging does not create lifecycle state.
Write to staging does not authorize execution.
Write to staging does not authorize queue placement.
Write to staging does not authorize active-task replacement.

## Path Semantics
Only allowed output target family:

generated/task-contract-candidates/

output_path must resolve inside generated/task-contract-candidates/.
generated_conversion_package_path must resolve inside generated/task-contract-candidates/.
primary_validator_target must resolve inside generated/task-contract-candidates/.
would_write_to must resolve inside generated/task-contract-candidates/.
output_path must not resolve to tasks/active-task.md.
output_path must not resolve inside tasks/queue/.
output_path must not resolve inside approvals/.
output_path must not use path traversal.

Task 51.3 defines the output record contract only.
Task 51.3 does not create generated/.
Task 51.3 does not write generated artifacts.

## Carry-Forward Preservation
Accepted limitations must be preserved in generated output records.
Open questions must be preserved in generated output records.
Downstream limits must be preserved in generated output records.
Non-authority boundary must be preserved in generated output records.
Source traceability must be preserved in generated output records.

Carry-forward preservation prevents the generator output record from silently erasing limitations, open questions, downstream limits, or non-authority boundaries inherited from M50 and 51.2 input.

## Boundary Flags
```yaml
boundaries:
  generated_candidate_is_active_task: false
  generated_candidate_is_queue_entry: false
  execution_authorized: false
  active_task_write_allowed: false
  queue_write_allowed: false
  approval_record_created: false
```

generated_candidate_is_active_task must remain false.
generated_candidate_is_queue_entry must remain false.
execution_authorized must remain false.
active_task_write_allowed must remain false.
queue_write_allowed must remain false.
approval_record_created must remain false.

## Blocking Conditions
- source conversion package missing
- source generator input missing
- source generator input invalid
- source validator missing
- source validator does not reference M50 validator
- primary output format not M50-compatible
- standalone candidate-only artifact used as primary validator target
- generated conversion package path outside staging area
- output_path outside staging area
- primary_validator_target outside staging area
- would_write_to outside staging area
- path traversal requested
- active-task target requested
- queue target requested
- approvals target requested
- dry-run output_path non-null
- dry-run generated_conversion_package_path non-null
- dry-run primary_validator_target non-null
- dry-run written set to true
- write output_path missing
- write generated_conversion_package_path missing
- write primary_validator_target missing
- write primary_validator_target mismatches output_path
- write generated_conversion_package_path mismatches output_path
- write would_write_to omitted despite required schema field
- generated_candidate_path non-null without explicit future authorization
- generated_candidate_is_active_task set to true
- generated_candidate_is_queue_entry set to true
- execution_authorized set to true
- active_task_write_allowed set to true
- queue_write_allowed set to true
- approval_record_created set to true
- carry-forward preservation missing
- accepted limitations preservation missing
- open questions preservation missing
- downstream limits preservation missing
- non-authority boundary preservation missing

## Template Boundary
templates/generated-task-contract-candidate-record.md must be a template only.
It must not contain a real generated conversion package path as if written by this task.
It must not contain a real output path as if written by this task.
It must not contain a real primary validator target as if created by this task.
It must not contain a real approval record.
It must not contain real approval evidence.

## Schema Contract
Schema file: schemas/generated-task-contract-candidate-record.schema.json

## Primitive Field Type Requirements
Primitive field types:

```yaml
dry_run:
  type: boolean

written:
  type: boolean

generated_at:
  type: string

generator_version:
  type: string
```

generated_at must be a string timestamp.

generator_version must be a string.

generated_at should use ISO 8601 / RFC 3339 timestamp format when generated by future implementation.

Task 51.3 schema may define generated_at as string without enforcing date-time format.

Date-time validity is a semantic generator rule for later implementation and fixtures.

## Schema vs Semantic Validation Boundary
JSON Schema in Task 51.3 is structural, not a full semantic validator.

The schema allows output path fields to be either string or null because both values are valid in different modes.

The schema does not have to enforce that output_path is null specifically when generation_mode is dry_run.

The schema does not have to enforce that primary_validator_target is null specifically when generation_mode is dry_run.

The schema does not have to enforce that primary_validator_target equals output_path specifically when generation_mode is write.

Those mode-specific constraints are semantic generator rules and must be enforced later by the generator implementation and fixtures.

Task 51.3 must document these constraints, but must not implement generator behavior.

Schema checks shape.
Generator later checks mode-specific output semantics.

dry_run + output_path: null is a semantic rule.
dry_run + primary_validator_target: null is a semantic rule.
write + primary_validator_target equals output_path is a semantic rule.
write + would_write_to equals output_path or null is a semantic rule.
generated_candidate_path null in M51 is a semantic rule.

The schema may allow string or null for future compatibility, but Task 51.3 requires M51 implementations to keep generated_candidate_path null unless a later explicit task authorizes otherwise.

## Non-Authority Rules
Generated task contract candidate record is not approval.
Generated task contract candidate record does not authorize execution.
Generated task contract candidate record does not authorize queue placement.
Generated task contract candidate record does not authorize active-task replacement.
Generated task contract candidate record does not authorize implementation.
Generated task contract candidate record does not create active task state.
Generated task contract candidate record does not create queue entry.

Task 51.3 does not implement generator behavior.
Task 51.3 does not validate actual generation.
Task 51.3 does not create generated outputs.
Task 51.3 does not create examples.
Task 51.3 does not create fixtures.

## Explicit Non-Goals
Task 51.3 does not do:
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
