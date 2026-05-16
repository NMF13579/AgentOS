status: DRAFT
ux_id: Draft Appointment Flow
title: Draft UX Should Be Blocked
risk_level: MEDIUM
priority: normal
ui_contract_required: true
ui_contract_present: true
ui_contract_reference: docs/UI-SEMANTIC-COMPONENT-CONTRACT.md

## UX Goal
This should fail because status is not APPROVED.

## Screens
- Draft screen listed, but approval check must fail first.

## UX Acceptance Criteria
- Should never generate task contract.
