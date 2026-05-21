---
type: ux-contract
status: review
authority: ux-structure
execution_locked: true
ux_contract_id: UX-agent-action-review
ux_contract_version: 0.1.0
spec_id: SPEC-agent-action-review
spec_version: 0.1.0
product_spec_path: specs/agent-action-review.md
created: 2026-05-21
owner: human
---

# Agent Action Review

## Source Product Spec
source_product_spec:
  spec_id: SPEC-agent-action-review
  spec_version: 0.1.0
  product_spec_path: specs/agent-action-review.md

## UX Goal
Safe review before risky action.

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

- summary_card
- risk_banner
- approval_card
- review_panel
- non_authority_notice

action_summary: review proposed action
risk_level: high
human_owner: product_owner
consequences: possible destructive changes
approve_label: Approve conceptually
decline_label: Decline conceptually
non_authority_notice: This is not execution permission
risk_reason: affects production files
affected_scope: repo files and workflows

## User Actions
### User Action: Click Approve
### User Action: Click Reject

## Risk / Approval Points
### Risk / Approval Point: Approval Action Confirmation

## Edge Cases
### Edge Case: concurrent edit

## Accessibility Notes
Use high contrast.

## Non-Goals
No execution.

## Open UX Questions
Who is the final approval owner?

## Traceability
traceability:
  spec_id: SPEC-agent-action-review
  spec_version: 0.1.0
  product_spec_path: specs/agent-action-review.md
  ux_contract_id: UX-agent-action-review
  source_sections:
    - goals.agent_action_review

## Non-Authority Boundary
UX Contract is not Product Spec.
UX Contract is not approval.
UX Contract does not authorize task generation.
UX Contract does not authorize execution planning.
UX Contract does not authorize implementation.
UX Contract does not authorize commit, push, merge, deploy, or release.
UX Contract describes user-facing structure.
UX Contract does not implement UI.
HTML Preview is optional visual explanation only.
HTML Preview is not source of truth.
UX Visual Approval Snapshot approves visual direction only.
UX Visual Approval Snapshot is supporting evidence only.
