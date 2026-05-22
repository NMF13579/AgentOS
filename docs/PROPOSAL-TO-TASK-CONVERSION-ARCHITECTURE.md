# Proposal-to-Task Candidate Conversion Architecture

## Purpose

Define the controlled transition from a validated task contract proposal to a task contract candidate ready for placement review.
This architecture sets the authority boundary for M50 and prevents interpretation drift from "valid proposal" to "execution allowed".

## M50 Boundary Summary

M50 is limited to conversion architecture for candidate preparation.
M50 does not create an active task, does not place anything into queue, and does not authorize execution.
M50 does not start implementation.

## Core Flow

validated task contract proposal
↓
scoped human authorization for conversion
↓
conversion package
↓
task contract candidate ready for placement review
↓
later lifecycle / placement gate

The final step is outside M50.

## Definitions

- task contract proposal: a proposed task contract draft that describes intended task scope, constraints, and expected verification, but is not yet eligible for execution.
- validated task contract proposal: a task contract proposal that passed conversion-relevant validation checks, while still remaining non-executable.
- human authorization for conversion: explicit scoped approval by a human owner to run proposal-to-candidate conversion only.
- conversion package: the bounded conversion output set that transforms validated proposal content into a candidate-form contract package for placement review.
- task contract candidate ready for placement review: a candidate contract artifact prepared for placement decision, still outside active task and queue states.
- EXECUTION_SHAPE: candidate semantics meaning the artifact has executable contract structure only.
- placement review: a later gate where humans decide whether and where a candidate may be placed in lifecycle flow.
- active task: the currently authorized task state represented by `tasks/active-task.md`.
- queue entry: a task item placed into `tasks/queue/` for later lifecycle processing.
- execution authorization: explicit human permission that allows implementation/execution actions.

## Required Inputs

- validated task contract proposal
- scoped human authorization for conversion

## Allowed Outputs

- conversion package
- task contract candidate ready for placement review

## Proposal vs Task Contract Candidate

A proposal is an upstream contract idea that may be valid but is not a placement-ready candidate.
A task contract candidate is a converted artifact that is ready only for placement review, not for execution.

Validated proposal is not execution permission.

## Human Authorization Boundary

Human authorization for conversion is required.
Human authorization for conversion is not execution approval.
Human authorization must be valid when the conversion validator runs.
M49_COMPLETE is not human authorization.

## Conversion Package Boundary

Conversion is not execution.
The conversion package exists only to move from validated proposal to candidate-for-placement-review state.
M50 must not use conversion to authorize implementation, task activation, or queue placement.

## Task Contract Candidate Boundary

Task contract candidate is not active task state.
Task contract candidate is not queue entry.
Task contract candidate must not be copied into tasks/active-task.md by M50.
Task contract candidate must not be placed into tasks/queue/ by M50.

## Validator Boundary

Validator PASS is not human authorization.
Validator PASS is not execution authorization.
Validator must not create approval records.

## Non-Authority Rules

- This architecture defines conversion boundary, not execution boundary.
- Conversion readiness does not grant lifecycle placement rights.
- Placement rights are decided later in placement review.
- M50 uses EXECUTION_SHAPE, not EXECUTION.

## Forbidden Interpretations

- "Validated proposal means execution is allowed" is forbidden.
- "Conversion output can be treated as active task" is forbidden.
- "Conversion output can be placed into queue automatically" is forbidden.
- "Validator PASS is equivalent to approval" is forbidden.

## Downstream Handoff to M51+

M50 hands off only candidate artifacts that are ready for placement review.
Any placement decision, activation decision, queue decision, or execution decision belongs to later lifecycle and is outside M50.

## Explicit Non-Goals

M50 does not do:

- mass task generation
- automatic task generator
- task graph generation
- placement into tasks/active-task.md
- placement into tasks/queue/
- active task replacement
- approval record creation
- agent execution
- implementation
- autopilot
- commit
- push
- merge
- deploy
- release

EXECUTION_SHAPE means the candidate has the structure of an executable task contract.
EXECUTION_SHAPE does not mean execution is authorized.
EXECUTION_SHAPE does not allow queue placement.
EXECUTION_SHAPE does not allow active-task replacement.
EXECUTION_SHAPE does not allow implementation.

```yaml
boundaries:
  conversion_validated: true
  executable_contract_shape: true
  candidate_ready_for_placement_review: true
  placement_review_required: true
  execution_authorized: false
  execution_permission_granted: false
  active_task_allowed: false
  task_queue_allowed: false
```

In M50:
- execution_authorized must always be false.
- execution_permission_granted must always be false.
- active_task_allowed must always be false.
- task_queue_allowed must always be false.
