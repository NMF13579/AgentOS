status: APPROVED
ux_id: Missing UI Contract Example
title: Approved UX Missing UI Contract Presence
risk_level: MEDIUM
priority: normal
ui_contract_required: true
ui_contract_present: false
ui_contract_reference: docs/UI-SEMANTIC-COMPONENT-CONTRACT.md

## UX Goal
This should fail because UI contract presence is false.

## Screens
- Screen exists but UI contract check must fail before structure check.

## UX Acceptance Criteria
- Should return blocked missing UI contract token.
