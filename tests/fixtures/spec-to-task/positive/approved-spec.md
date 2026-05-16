status: APPROVED
spec_id: SPEC-44-4-APPROVED
title: Approved Spec Fixture for Spec-to-Task Generator
risk_level: MEDIUM
priority: normal

## Goal
Generate a candidate task contract from approved spec input.

## Functional Requirements
- Parse approved spec metadata and required sections.
- Produce candidate Task Contract v2 markdown.

## Acceptance Criteria
- Dry-run returns SPEC_TO_TASK_DRY_RUN_OK.
- Generated content includes non-approval warning.

## Validation Plan
- Run generator in dry-run mode and check output tokens.
- Run generator in JSON mode and validate JSON format.

## Out of Scope
- Real task queue write.
- Task execution.

## Known Risks
- TODO source fields require follow-up linting.
