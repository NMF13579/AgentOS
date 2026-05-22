---
type: task-contract-proposal
proposal_id: PROPOSAL-UX-agent-action-review-001
proposal_status: PROPOSED_ONLY
source_draft_id: DRAFT-UX-agent-action-review-001
source_task_draft_path: docs/drafts/agent-action-review-draft.md
source_ux_contract: examples/ux-contract-example.md
source_readiness_report: examples/ux-planning-readiness-report-example.md
source_boundary_policy: docs/UX-TO-TASK-BOUNDARY-POLICY.md
execution_authorized: false
implementation_authorized: false
human_authorization_required: true
created: 2026-05-21
owner: human
---

## Purpose
Task contract proposal is not executable.
Task contract proposal does not authorize implementation.
Task contract proposal does not authorize execution.
Task contract proposal must not be copied into tasks/active-task.md.
Task contract proposal must not be copied into tasks/queue/.

## Source Traceability
source_sections: ["ux.contract.screen.review", "ux.flow.agent_action_review"]

## Proposed Task Contract Summary
Proposal summary for non-executable review.

## Proposed Goal
Define review panel behavior proposal.

## Proposed Scope
Non-executable proposal scope only.

## Proposed Allowed Changes
- docs

## Proposed Forbidden Changes
- tasks/active-task.md
- tasks/queue/

## Proposed Validation
- validator checks only

## Proposed Risk Notes
No execution authorization in this artifact.

## Carry-Forward Requirements
Carry forward limitations, questions, and limits.

## Human Authorization Requirement
Separate human authorization is required.

## Non-Executable Boundary
This proposal is non-executable.

## Summary
Valid proposal fixture.

```yaml
task_contract_proposal:
  proposal_id: PROPOSAL-UX-agent-action-review-001
  proposal_status: PROPOSED_ONLY
  source_draft:
    source_draft_id: DRAFT-UX-agent-action-review-001
    source_task_draft_path: docs/drafts/agent-action-review-draft.md
    draft_status: DRAFT_READY_FOR_PROPOSAL
  source_product_spec:
    spec_id: SPEC-agent-action-review
    spec_version: 1.0.0
    product_spec_path: examples/ux-contract-example.md
  source_ux_contract:
    ux_contract_id: UX-agent-action-review
    ux_contract_version: 1.0.0
    ux_contract_path: examples/ux-contract-example.md
    ux_contract_validation_result: UX_CONTRACT_VALIDATION_OK
  source_readiness_report:
    readiness_report_path: examples/ux-planning-readiness-report-example.md
    readiness_validation_result: UX_PLANNING_READINESS_VALIDATION_OK
    readiness_decision: UX_PLANNING_READY_WITH_LIMITATIONS
  source_boundary_policy:
    boundary_policy_path: docs/UX-TO-TASK-BOUNDARY-POLICY.md
  source_sections:
    - ux.contract.screen.review
  proposed_contract:
    proposed_task_id: TASK-agent-action-review-001
    proposed_task_name: Agent Action Review UI Behavior
    proposed_mode: EXECUTION
    proposed_goal: Define candidate behavior for later authorized implementation.
    proposed_scope: Proposal-level scope only.
    proposed_allowed_changes: ["docs"]
    proposed_forbidden_changes: ["tasks/active-task.md", "tasks/queue/"]
    proposed_validation: ["validator"]
    proposed_expected_final_report: Proposal validation summary.
  carry_forward:
    accepted_limitations:
      - limitation: Static preview is non-production.
    open_questions:
      - question: framework choice
    downstream_limits:
      - No implementation authorized.
    non_authority_boundary:
      - Proposal is not execution authorization.
  authorization:
    human_authorization_required: true
    authorization_reference: AUTH-M49-001
    authorized_by: human-owner
    authorized_at: 2026-05-21
  boundaries:
    execution_authorized: false
    implementation_authorized: false
    active_task_allowed: false
    task_queue_allowed: false
  review:
    reviewed_by: validator
    reviewed_at: 2026-05-21
```
