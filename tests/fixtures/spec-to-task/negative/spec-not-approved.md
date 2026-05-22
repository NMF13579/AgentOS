status: DRAFT
spec_id: SPEC-44-4-DRAFT
title: Draft Spec Fixture Should Be Blocked
risk_level: MEDIUM
priority: normal

## Goal
This fixture should fail only because status is not APPROVED.

## Functional Requirements
- The structure is valid enough except approval state.

## Acceptance Criteria
- Generator must block due to non-approved status.

## Validation Plan
- Run generator and expect SPEC_TO_TASK_BLOCKED_SPEC_NOT_APPROVED.

## Out of Scope
- Any write mode verification.

## Known Risks
- None for fixture purpose.
