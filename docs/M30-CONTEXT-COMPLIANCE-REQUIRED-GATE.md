# M30 Context Compliance Required Gate

## Purpose
- Context Compliance Required Gate validates plan/verification against selected required context.
- Silence is not compliance.
- Context Pack is not approval.
- Command success does not override context violation.
- Context Compliance Required Gate is not approval.
- Context Compliance Required Gate does not authorize protected actions.
- Context Compliance Required Gate does not replace Human Gate.
- Context Compliance Required Gate does not replace M27 runtime enforcement.
- Context Compliance Required Gate does not weaken M28 context control.
- Context Compliance Required Gate does not weaken M29 bypass resistance boundaries.
- Human Gate remains approval authority.

## CLI
- `python3 scripts/check-required-context-compliance.py`
- `python3 scripts/check-required-context-compliance.py --json`
- `python3 scripts/check-required-context-compliance.py --mode plan|verification|both`
- `python3 scripts/check-required-context-compliance.py --require-valid-context-pack`

## Result Values
- `CONTEXT_COMPLIANCE_PASS`
- `CONTEXT_COMPLIANCE_PASS_WITH_WARNINGS`
- `CONTEXT_COMPLIANCE_MISSING`
- `CONTEXT_COMPLIANCE_INVALID`
- `CONTEXT_COMPLIANCE_VIOLATION`
- `CONTEXT_COMPLIANCE_INCOMPLETE`
- `CONTEXT_COMPLIANCE_NEEDS_REVIEW`
- `CONTEXT_COMPLIANCE_BLOCKED`

## Exit semantics
- `CONTEXT_COMPLIANCE_PASS => exit 0`
- others => `exit 1`

## Modes
- plan mode
- verification mode
- both mode (default)
- Plan success does not hide verification violation.

## Optional valid Context Pack check
- Compliance requires valid Context Pack.
- Context Pack checker result mapping
- CONTEXT_PACK_STALE → CONTEXT_COMPLIANCE_INCOMPLETE
- Stale Context Pack must never map to CONTEXT_COMPLIANCE_PASS

## Required context extraction
- Required context must be machine-checkable enough to verify compliance.

## Acknowledgement definition
- A mention of the context item path alone without a coverage statement is insufficient.
- Generic claim patterns are insufficient.
- Silence about selected required context is not compliance.
- not_applicable requires explicit justification.

## Contradiction checks
- Command success does not override context violation.

## Changed files checks
- Safe read-only git diff means read-only commands only.
- Undeclared changed files must be treated as scope/context violation, not as neutral.

## Verification evidence checks
- Verification evidence is required for context compliance.
- Tests passing is not context compliance.

## Lesson checks
- Selected lessons must not be silently ignored.

## Result escalation order
- Result escalation order
- PASS_WITH_WARNINGS in one artifact cannot downgrade stricter non-pass result.
- if one artifact passes and the other required artifact is missing -> non-pass.

## JSON output
- includes result, mode, paths, findings, warnings, errors
- Finding severity mapping rules

## Fixture notes
- exit 0 without explicit CONTEXT_COMPLIANCE_PASS is downstream gate responsibility.
- downstream gate responsibility
- process exit code is 0
- explicit result value is CONTEXT_COMPLIANCE_PASS

## Semantic compliance limitation
- Semantic compliance limitation
- deterministic static checker only
- no LLM, no embeddings, no vector DB, no remote semantics

## Non-Authorization Boundary
Context Compliance Required Gate is not approval.
Context Compliance Required Gate does not authorize commit, push, merge, release, deployment, or protected changes.
Context Compliance Required Gate does not authorize bypassing AgentOS guardrails.
Context Compliance Required Gate does not replace Human Gate.
Context Compliance Required Gate does not weaken, disable, or reduce any guardrail.
Context Compliance Required Gate must not weaken M27 runtime enforcement.
Context Compliance Required Gate must not weaken M28 context control.
Context Compliance Required Gate must not weaken M29 bypass resistance boundaries.
Human Gate remains approval authority.

- if one artifact passes and the other required artifact is missing, result is non-pass.
- Context Pack checker result mapping.
- Safe read-only git diff means read-only commands only.
- exit 0 without explicit CONTEXT_COMPLIANCE_PASS is not success.
