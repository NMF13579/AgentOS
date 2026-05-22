status: APPROVED
ux_id: Invalid Missing Screens
title: Approved UX Missing Screens
risk_level: MEDIUM
priority: normal
ui_contract_required: true
ui_contract_present: true
ui_contract_reference: docs/UI-SEMANTIC-COMPONENT-CONTRACT.md

## UX Goal
This should fail at structure check due to missing Screens section.

## User Flows
- Flow exists but Screens is missing.

## UX Acceptance Criteria
- Should return UX_TO_TASK_BLOCKED_INVALID_UX.
