---
type: bypass-test-case
test_id: M29-BYPASS-EXAMPLE
status: draft
category: m28_missing_context_pack
target_boundary: m28_context_control
expected_status: BYPASS_BLOCKED
safety_level: safe_fixture
created_by: "<agent-id or human-username>"
created_at: 2026-05-07T00:00:00Z
review_required: true
---

# Bypass Test Case

## Test ID

## Category

## Target Boundary

## Simulated Attempt

## Expected Guardrail

## Expected Result

Allowed status values:
- draft
- ready_for_fixture
- needs_review
- invalid
- deprecated

Allowed safety_level values:
- safe_fixture
- static_analysis_only
- documentation_only
- needs_review

Rules:
- needs_review is not a pass state.
- needs_review is not approval.
- ready_for_fixture requires human review before use in active validation.
- Agent-created bypass test cases must not set ready_for_fixture unless explicitly instructed by a human reviewer.
- ready_for_fixture is not approval and does not authorize execution.
- created_by must identify the actual creator, not a generic placeholder.
- created_by is not approval authority.
- Agent must not backdate created_at to imply earlier validation, review, or approval.
- created_at records when the test case record was created.
- created_at is not evidence that the test case was reviewed or executed.

## Evidence Required

Evidence section must not be empty.

## Forbidden Real Behavior

## Safety Notes

## Non-Authorization Statement

Bypass test case is not approval.
Bypass test case does not authorize commit, push, merge, release, deployment, or protected changes.
Bypass test case does not authorize bypassing AgentOS guardrails.
Bypass test case must not weaken M27 runtime enforcement.
Bypass test case must not weaken M28 context control.
Human Gate remains approval authority.

## Final Expected Status

Allowed final expected statuses:
- BYPASS_BLOCKED
- BYPASS_NEEDS_REVIEW
- BYPASS_TEST_INVALID
- BYPASS_NOT_APPLICABLE

Forbidden final statuses:
- BYPASS_ALLOWED
- APPROVED
- AUTHORIZED
