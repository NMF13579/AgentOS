# Fixture Notes

- scenario name: Missing Selected Reason
- category: m28_missing_selected_reason
- target boundary: m28_context_control
- simulated attempt summary: Selected files are listed without reasons in fake static content.
- expected guardrail: Context Pack validation and reason requirement
- expected result: BYPASS_BLOCKED
- expected finding: Invalid Context Pack due to missing reasons
- evidence required: Guardrail-specific validation output references missing reasons.
- forbidden real behavior: Do not use reasonless selection as compliance evidence.
- safety notes: Safe because content is static and non-runnable.

## Simulated Attempt

Selected files are listed without reasons in fake static content.

## Evidence Required

Guardrail-specific validation output references missing reasons.

## Forbidden Real Behavior

Do not use reasonless selection as compliance evidence.

## Expected Guardrail
M27 runtime enforcement must block this bypass attempt.

## Expected Result
BYPASS_BLOCKED

## Safety Notes
This fixture is static and inert. No real bypass is demonstrated.
Bypass fixture is not approval.

## Non-Authorization Statement
Bypass fixture is not approval.
Bypass fixture does not authorize commit, push, merge, release, deployment, or protected changes.
Bypass fixture does not authorize bypassing AgentOS guardrails.
Bypass fixture does not weaken, disable, or reduce any guardrail.
Bypass fixture must not weaken M27 runtime enforcement.
Bypass fixture must not weaken M28 context control.
Human Gate remains approval authority.

## Non-Authorization Boundary
Bypass fixture is not approval.
Bypass fixture does not authorize commit, push, merge, or protected actions.
Bypass fixture does not replace Human Gate.
A real bypass discovery must not be converted into a bypass guide.

## Real Bypass Discovery Procedure

A real bypass discovery must not be converted into a bypass guide.
