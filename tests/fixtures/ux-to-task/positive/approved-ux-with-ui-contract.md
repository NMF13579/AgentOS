status: APPROVED
ux_id: Appointment Form
title: Appointment Intake UX
risk_level: MEDIUM
priority: normal
ui_contract_required: true
ui_contract_present: true
ui_contract_reference: docs/UI-SEMANTIC-COMPONENT-CONTRACT.md

## UX Goal
Enable users to submit appointment request in one pass.

## Screens
- Appointment Form Screen
- Submission Confirmation Screen

## User Flows
- Open form, fill required fields, submit request.

## State and Error Matrix
- Loading state while submit is in progress.
- Inline error state for invalid required fields.

## UX Acceptance Criteria
- User can submit valid form and see confirmation.
- User sees clear error when required fields are missing.

## Accessibility Notes
- Keyboard navigation for all inputs and actions.

## Responsive Behavior
- Layout remains usable on mobile and desktop widths.

## UX Copy
- Submit button label: Send Request.

## Out of Scope
- Admin dashboard.

## Known Risks
- Missing upstream UI contract artifact file in repository.
