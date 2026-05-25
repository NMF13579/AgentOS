# Task Contract Candidate Validation Input Contract (M52)

## Purpose

This contract defines the exact input package required before M52 can validate an M51-generated staging artifact as a task contract candidate for future M53 review.

## Task Execution Context Boundary

Task 52.2 execution mode is bounded to creating only the three Task 52.2 input-contract artifacts.
Task 52.2 execution mode does not authorize commit, push, merge, deployment, release, queue placement, active-task replacement, approval creation, generated candidate execution, validator implementation, or M53 placement review.
Task execution mode and generated candidate mode are different concepts.
Generated task contract candidate mode must remain EXECUTION_SHAPE, not EXECUTION.

## Input Package Definition

The input package is a structured object named `candidate_validation_input` used as validator input only.
It includes source traceability, source proposal reference, source authorization provenance, source conversion package reference, M51-origin evidence, carry-forward fields, and non-authority boundaries.

## What The Input Package Is Not

Candidate validation input is not approval.
Candidate validation input is not execution permission.
Candidate validation input is not queue placement.
Candidate validation input is not active-task replacement.
Candidate validation input does not create lifecycle state.
Candidate validation input does not authorize M53 placement.

M52 input readiness is not candidate validation success.
M52 input readiness only means the input package may be used by the M52 validator.

## M52 MVP Source Origin Rule

For M52 MVP, the only accepted `source_candidate_origin` is `M51_GENERATED_STAGING_ARTIFACT`.
m51_origin fields are required only when source_candidate_origin is M51_GENERATED_STAGING_ARTIFACT.
For M52 MVP, because source_candidate_origin is intentionally M51-specific, m51_origin is effectively required for all valid MVP inputs.
M52 MVP must not silently accept missing M51 evidence for M51-origin candidates.

## Validation Mode Rule

validation_mode must be M52_CANDIDATE_READINESS_VALIDATION for M52 MVP.
validation_mode is not execution mode, approval mode, or placement mode.
validation_mode does not authorize queue write.
validation_mode does not authorize active-task replacement.

## Required Traceability Semantics

`required_traceability` contains:
- source_proposal
- source_authorization
- source_conversion_package
- source_generated_artifact
- source_candidate_origin
- m50_traceability
- m51_generator_evidence

required_traceability must be an object, not a free-form string.

`source_authorization` means provenance authorization for source conversion / candidate generation only.
source_authorization is not approval.
source_authorization is not execution authorization.
source_authorization is not placement authorization.

## Required Carry-Forward Semantics

`required_carry_forward` contains:
- accepted_limitations
- open_questions
- downstream_limits
- non_authority_boundary

required_carry_forward must be an object, not a free-form string.

Carry-forward preservation rule:
accepted_limitations, open_questions, downstream_limits, and non_authority_boundary must be carried forward from the source conversion package without deletion.
Additional stricter limitations, open questions, and downstream limits may be added.
Existing items must not be removed, softened, renamed into weaker meaning, or converted into resolved/approved state by M52.

## Required Boundary Values

The input package must preserve these exact values:
- validation_only: true
- queue_write_allowed: false
- active_task_write_allowed: false
- execution_authorized: false
- approval_record_creation_allowed: false
- placement_authorized: false

Candidate validation input is valid only if traceability, carry-forward fields, and non-authority boundary are preserved.

## Input Status Tokens

- CANDIDATE_VALIDATION_INPUT_READY
- CANDIDATE_VALIDATION_INPUT_READY_WITH_LIMITATIONS
- CANDIDATE_VALIDATION_INPUT_BLOCKED
- CANDIDATE_VALIDATION_INPUT_INVALID

Semantics:
- READY: structure complete, traceability exists, carry-forward exists, M51 evidence exists, boundaries preserved.
- READY_WITH_LIMITATIONS: structurally complete, no boundary weakening, limitations/open questions must be carried into validation result and M53 review.
- BLOCKED: unsafe to validate due to missing source/wrapper/M51 evidence or unknown carry-forward baseline.
- INVALID: malformed input, missing required fields, boundary contradiction, unsupported origin, or unsupported validation_mode.

## m51_origin Required Semantics

The m51_origin.required field is a data field inside the input package and must have value true for M51-origin candidates.
The JSON Schema must also require the m51_origin object itself when source_candidate_origin is M51_GENERATED_STAGING_ARTIFACT.

## Schema Layout Limitations For Task 52.2

Task 52.2 checks that Task 52.1 architecture document exists, but does not revalidate full 52.1 semantic validity.
Task 52.2 schema must use direct top-level properties and must not place candidate_validation_input only under $defs.
m51_origin must be declared in candidate_validation_input.properties, not only in then.required.
candidate_validation_input.properties and candidate_validation_input.allOf must be declared on the same schema object.

## Why This Input Does Not Grant Authority

The input package defines validator prerequisites only.
It does not authorize validation result success by itself.
It does not authorize M53 placement.
It does not authorize queue placement.
It does not authorize active-task replacement.
It does not authorize execution.
