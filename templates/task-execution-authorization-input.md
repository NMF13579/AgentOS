---
type: execution-authorization-input
milestone: M57
template: task-execution-authorization-input
schema: schemas/task-execution-authorization-input.schema.json
status: draft
authorization_input_only: true
execution_authorized: false
execution_started: false
approval_created: false
lifecycle_mutation_authorized: false
m58_authorized: false
m58_started: false
---

# M57 Execution Authorization Input Template

```json
{
  "execution_authorization_input": {
    "schema_version": "1.0.0",
    "input_id": "example-input-id",
    "source_m56_completion_review": "reports/m56-completion-review.md",
    "source_m56_evidence_report": "reports/m56-execution-readiness-evidence-report.md",
    "source_active_task": "tasks/active-task.md",
    "authorization_request_status": "EXECUTION_AUTHORIZATION_INPUT_READY",
    "requested_execution_mode": "M58_PLANNING_ONLY",
    "expected_execution_session_type": "CONTROLLED_EXECUTION_SESSION",
    "required_traceability": {
      "m57_intake_report": "reports/m57-m56-completion-intake.md"
    },
    "required_boundaries": {
      "non_authority_preservation": true
    },
    "boundary_flags": {
      "authorization_input_only": true,
      "execution_authorized": false,
      "execution_started": false,
      "approval_created": false,
      "lifecycle_mutation_authorized": false,
      "m58_authorized": false,
      "m58_started": false
    },
    "carry_forward_limitations": [
      "Timeout handling was contractually required but not directly exercised by the Task 56.8 fixture matrix."
    ],
    "warnings": [],
    "blockers": [],
    "non_authority_markers": [
      "M57 authorization input is not authorization.",
      "M57 authorization input does not authorize execution.",
      "M57 authorization input does not start execution.",
      "M57 authorization input does not create approval records.",
      "M57 authorization input does not authorize lifecycle mutation.",
      "M57 authorization input does not authorize M58.",
      "M57 authorization input does not start M58.",
      "M57 authorization input does not modify tasks/active-task.md.",
      "M58 must independently validate M57 completion before any M58 planning work."
    ]
  }
}
```

## 1. Purpose

This template captures M57 execution authorization input only.

## 2. Usage

Use this template as a reference to construct valid input files conforming to the JSON schema.

## 3. Non-Authority Boundary

This template captures M57 execution authorization input only.
This template does not authorize execution.
This template does not start M58.
This template does not create approval records.
This template does not modify tasks/active-task.md.

## 5. Relationship to M58

M58 must independently validate M57 completion before any M58 planning work.

## 4. Relationship to M56

This template references M56 completion status to construct the input state for M57.
