# Proposal-to-Task Conversion Input Contract

## Purpose

Define the required conversion input contract for M50 so that conversion package readiness is controlled, traceable, and bounded.
This contract prevents false interpretation from conversion input readiness to execution permission.

## Input Contract Boundary

This contract defines only the conversion input package required to prepare later candidate placement review.
Task 50.2 does not create task contract candidates.
Task 50.2 does not create approval records.

Conversion input readiness is not execution readiness.
Conversion input readiness is not queue eligibility.
Conversion input readiness is not active-task permission.
Conversion input readiness is not approval record creation.

## Required Conversion Package Shape

```yaml
conversion_package:
  conversion_id:
  conversion_input_status:
  source_task_contract_proposal:
  proposal_validation_result:
  source_ux_contract:
  source_readiness_report:
  source_boundary_policy:
  source_sections:
  accepted_limitations:
  open_questions:
  downstream_limits:
  non_authority_boundary:
  human_authorization_record:
  conversion_scope:
  candidate_output:
  boundaries:
    conversion_input_ready_is_execution_permission: false
    conversion_input_ready_is_queue_permission: false
    conversion_input_ready_is_active_task_permission: false
    approval_record_creation_allowed: false
    execution_authorization_granted: false
```

## Required Fields

- conversion_id
- conversion_input_status
- source_task_contract_proposal
- proposal_validation_result
- source_ux_contract
- source_readiness_report
- source_boundary_policy
- source_sections
- accepted_limitations
- open_questions
- downstream_limits
- non_authority_boundary
- human_authorization_record
- conversion_scope
- candidate_output
- boundaries

## Field Semantics

- conversion_id: unique conversion package identifier.
- conversion_input_status: controlled conversion readiness status.
- source_task_contract_proposal: source reference to the validated task contract proposal.
- proposal_validation_result: validation result of the proposal, required as valid for readiness.
- source_ux_contract: source reference to UX contract.
- source_readiness_report: source reference to readiness report.
- source_boundary_policy: source reference to boundary policy.
- source_sections: mapped source sections used for conversion traceability.
- accepted_limitations: accepted scope limits that must persist downstream.
- open_questions: unresolved items that must persist downstream.
- downstream_limits: downstream constraints that must persist downstream.
- non_authority_boundary: explicit non-authority restrictions that must persist downstream.
- human_authorization_record: reference to existing human authorization for conversion.
- conversion_scope: bounded conversion scope that must not expand proposal scope.
- candidate_output: bounded output reference or placeholder.
- boundaries: explicit false-permission boundary flags.

## Conversion Input Statuses

Only these statuses are allowed:

- CONVERSION_INPUT_READY
- CONVERSION_INPUT_READY_WITH_LIMITATIONS
- CONVERSION_INPUT_NEEDS_HUMAN_AUTHORIZATION
- CONVERSION_INPUT_BLOCKED
- CONVERSION_INPUT_INVALID

## Human Authorization Reference Boundary

Human authorization record is required for conversion readiness.
Human authorization record in this package is a reference, not a newly created approval record.
Task 50.2 must not create approval records.
Missing human authorization must result in CONVERSION_INPUT_NEEDS_HUMAN_AUTHORIZATION or CONVERSION_INPUT_BLOCKED.
Human authorization for conversion is not execution approval.
Human authorization for conversion is not queue placement approval.
Human authorization for conversion is not active-task replacement approval.

## Source Traceability Requirements

Source traceability must be preserved.
Every conversion package must reference its source_task_contract_proposal, source_ux_contract, source_readiness_report, source_boundary_policy, and source_sections.

## Carry-Forward Requirements

Accepted limitations must be carried forward.
Open questions must be carried forward.
Downstream limits must be carried forward.
Non-authority boundary must be carried forward.
Source traceability must be preserved.

## Conversion Scope Requirements

conversion_scope must be explicit and must remain within proposal scope.
Any expansion beyond proposal scope blocks conversion input readiness.

## Candidate Output Boundary

candidate_output in Task 50.2 is a bounded output reference or placeholder.
Task 50.2 does not create a task contract candidate.
Task 50.2 does not define the final task contract candidate model.
Task 50.4 defines the task contract candidate model.
candidate_output must not grant execution permission.
candidate_output must not grant queue permission.
candidate_output must not grant active-task permission.

## Blocking Conditions

- source_task_contract_proposal missing
- proposal_validation_result missing
- proposal_validation_result not valid
- source_ux_contract missing
- source_readiness_report missing
- source_boundary_policy missing
- source_sections missing
- accepted_limitations missing
- open_questions missing
- downstream_limits missing
- non_authority_boundary missing
- human_authorization_record missing
- conversion_scope missing
- source traceability missing
- conversion scope expands proposal scope
- conversion input claims execution permission
- conversion input claims queue permission
- conversion input claims active-task permission
- conversion input creates or simulates approval record

## Schema Contract

Schema file: `schemas/proposal-to-task-conversion-package.schema.json`.
The schema enforces required shape, status set, false-boundary flags, and unknown-property rejection.

## Non-Authority Rules

- Conversion input readiness does not authorize execution.
- Conversion input readiness does not authorize queue placement.
- Conversion input readiness does not authorize active-task replacement.
- Conversion input readiness does not authorize approval record creation.
- Human authorization for conversion is not execution approval.

## Explicit Non-Goals

- creating validators
- creating fixtures
- creating examples
- creating evidence reports
- creating completion reviews
- creating approval records
- creating task contract candidate model
- lifecycle transition
- queue placement
- active-task replacement
