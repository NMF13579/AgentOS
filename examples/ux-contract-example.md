---
type: ux-contract
status: draft
authority: ux-structure
execution_locked: true
ux_contract_id: UX-001
ux_contract_version: 0.1.0
spec_id: SPEC-001
spec_version: 0.1.0
product_spec_path: specs/agent-action-review.md
created: 2026-05-21
owner: human
---

# Agent Action Review

## Source Product Spec
source_product_spec:
  spec_id: SPEC-001
  spec_version: 0.1.0
  product_spec_path: specs/agent-action-review.md

## UX Goal
The user easily understands the scope, risk, and impact of a proposed agent action before authorizing it.

## Screens
### Screen: Action Proposal Summary
### Screen: Action Risk Details

## Flows
### Flow: Approve Action
### Flow: Reject Action

## States
### State: normal
### State: loading
### State: empty
### State: error
### State: blocked
### State: needs_clarification
### State: approval_required
### State: execution_not_authorized

## UX Elements
### UX Element: summary_card
### UX Element: risk_banner
### UX Element: approval_card
### UX Element: review_panel
### UX Element: non_authority_notice

## User Actions
### User Action: Click Approve
### User Action: Click Reject
### User Action: Expand Risk Details

## Risk / Approval Points
### Risk / Approval Point: Approval Action Confirmation
### Risk / Approval Point: High Risk Escalation

## Edge Cases
### Edge Case: Agent action timeouts during approval
### Edge Case: Concurrent modifications to the same file

## Accessibility Notes
Ensure high contrast for the risk_banner.
Keyboard navigation must support easy access to approval and rejection actions.

## Non-Goals
This does not handle the actual execution of the action.

## Open UX Questions
Should the user be able to modify the action before approval?

## Traceability
traceability:
  spec_id: SPEC-001
  spec_version: 0.1.0
  product_spec_path: specs/agent-action-review.md
  ux_contract_id: UX-001
  source_sections:
    - section1
    - section2

## Non-Authority Boundary
UX Contract is not Product Spec.
UX Contract is not approval.
UX Contract does not authorize task generation.
UX Contract does not authorize execution planning.
UX Contract does not authorize implementation.
UX Contract does not authorize commit, push, merge, deploy, or release.
structure_review_complete means the UX structure review has been completed.
structure_review_complete does not authorize task generation.
structure_review_complete does not authorize execution planning.
structure_review_complete does not authorize implementation.
structure_review_complete does not authorize commit, push, merge, deploy, or release.
UX Contract describes user-facing structure.
UX Contract does not implement UI.
HTML Preview is optional visual explanation only.
HTML Preview is not source of truth.
UX Visual Approval Snapshot approves visual direction only.
UX Visual Approval Snapshot is supporting evidence only.

## Review Notes
None yet.
