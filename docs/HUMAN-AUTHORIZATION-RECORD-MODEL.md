# Human Authorization Record Model

## Purpose

Define the scoped human authorization record model for M50 conversion.
This model is for conversion authorization only and prevents execution-related interpretation drift.

## Authorization Boundary

Human authorization in M50 authorizes conversion only.
Human authorization in M50 does not authorize execution.
Human authorization in M50 does not authorize queue placement.
Human authorization in M50 does not authorize active-task replacement.
Human authorization in M50 does not authorize implementation.

## Required Record Shape

```yaml
human_authorization:
  authorization_id:
  authorization_type: proposal_to_task_contract_candidate_conversion
  source_proposal:
  authorized_scope:
  not_authorized:
  authorized_by:
  authorized_at:
  authorization_status:
  expires_at:
  evidence_reference:
  boundaries:
    conversion_only: true
    execution_approval_granted: false
    queue_placement_approval_granted: false
    active_task_replacement_approval_granted: false
    implementation_approval_granted: false
    approval_record_creation_allowed: false
```

## Required Fields

- authorization_id
- authorization_type
- source_proposal
- authorized_scope
- not_authorized
- authorized_by
- authorized_at
- authorization_status
- expires_at
- evidence_reference
- boundaries

## Field Semantics

- authorization_id: unique identifier of the human authorization record.
- authorization_type: scoped authorization class allowed in M50.
- source_proposal: specific proposal reference that this authorization applies to.
- authorized_scope: exact conversion scope allowed by human authorization.
- not_authorized: explicit list of disallowed actions.
- authorized_by: human approver identity reference.
- authorized_at: authorization timestamp.
- authorization_status: current authorization validity state.
- expires_at: mandatory expiration timestamp.
- evidence_reference: reference to external evidence of the human authorization.
- boundaries: explicit fixed permission boundaries.

## Allowed Authorization Type

The only allowed authorization type for M50 is:

- proposal_to_task_contract_candidate_conversion

Generic approval is not sufficient.
M49_COMPLETE is not human authorization.
Validator PASS is not human authorization.
Conversion package readiness is not human authorization.

## Allowed Authorization Statuses

Only these statuses are allowed:

- AUTHORIZATION_VALID
- AUTHORIZATION_NEEDS_REVIEW
- AUTHORIZATION_EXPIRED
- AUTHORIZATION_REVOKED
- AUTHORIZATION_INVALID

Status semantics:

- AUTHORIZATION_VALID means the record is explicit, scoped, proposal-specific, and not expired at validator runtime.
- AUTHORIZATION_NEEDS_REVIEW means the record cannot be accepted without human review.
- AUTHORIZATION_EXPIRED means expires_at has passed.
- AUTHORIZATION_REVOKED means the authorization was explicitly withdrawn.
- AUTHORIZATION_INVALID means the record is malformed, generic, unscoped, simulated, or references the wrong proposal.

## Scope Requirements

Human authorization must be explicit.
Human authorization must be scoped.
Human authorization must reference a specific proposal.
Human authorization must define authorized_scope.
Human authorization must define not_authorized.
Human authorization must not silently expand proposal scope.
Human authorization must not authorize execution.
Human authorization must not authorize queue placement.
Human authorization must not authorize active-task replacement.
Human authorization must not authorize implementation.

authorized_scope must be limited to conversion from a specific proposal into a task contract candidate ready for placement review.

not_authorized must explicitly include:

- execution
- queue placement
- active-task replacement
- implementation
- commit
- push
- merge
- deploy
- release
- approval record creation by agent or validator

## Not Authorized Requirements

The authorization record must explicitly deny execution, queue placement, active-task replacement, implementation, and approval record creation by agent or validator.

## Expiration Rule

Human authorization is valid only if authorization_status is AUTHORIZATION_VALID
and expires_at has not passed at the moment the conversion validator runs.

If authorization expires before validator execution, conversion must be BLOCKED.

Starting conversion before expiration is not sufficient.
Validator-time validity is required.

expires_at is required.
Open-ended authorization is not allowed in M50.
Missing expires_at must result in AUTHORIZATION_INVALID or AUTHORIZATION_NEEDS_REVIEW.

## Validator-Time Validity Rule

Human authorization must be valid when the conversion validator runs.
Validity must be evaluated at validator runtime, not at conversion-start intent time.

## Generic Approval Rejection

Generic approval is not sufficient.
Any non-proposal-specific or unscoped approval must be rejected for M50 conversion authorization.

## Agent-Simulated Approval Rejection

Agent-simulated approval is not human authorization.
Self-approval is not human authorization.
Generated approval text is not human authorization.
Synthetic approval records are invalid.
Validator-created approval records are invalid.

Invalid sources:

- agent
- self
- auto
- simulated
- generated
- synthetic
- validator
- script
- system-inferred

## Template Boundary

templates/human-authorization-record.md is a template only.
It must not contain real approval data.
It must not contain real personal identity data.
It must not contain a real authorization timestamp.
It must not contain a real evidence reference.
It must not be placed under approvals/.

## Relationship to Conversion Package

The conversion package references a human authorization record.
Task 50.3 defines the model and template for that record.
Task 50.3 does not create real authorization evidence.
Task 50.3 does not modify conversion packages.
Task 50.3 does not validate conversion packages.
Task 50.6 will validate conversion package references and authorization validity.

## Non-Authority Rules

- This task does not authorize execution.
- This task does not authorize queue placement.
- This task does not authorize active-task replacement.
- This task does not authorize implementation.
- This task does not create real approval evidence.

## Blocking Conditions

- human authorization missing
- human authorization generic
- human authorization unscoped
- human authorization scope mismatch
- human authorization expired
- human authorization expires before validator execution
- human authorization references wrong proposal
- human authorization missing expires_at
- human authorization has open-ended expiration
- human authorization created by agent
- human authorization simulated by agent
- human authorization generated by validator
- human authorization treated as execution approval
- human authorization treated as queue placement approval
- human authorization treated as active-task replacement approval
- human authorization treated as implementation approval

## Explicit Non-Goals

Task 50.3 does not do:

- create real approval records
- create files under approvals/
- authorize execution
- authorize queue placement
- authorize active-task replacement
- authorize implementation
- create conversion packages
- modify conversion packages
- create task contract candidates
- validate conversion packages
- validate candidates
- create schemas
- create validators
- create fixtures
- create examples
- create evidence reports
- create completion reviews
- commit
- push
- merge
- deploy
- release
