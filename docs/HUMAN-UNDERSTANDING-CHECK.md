---
type: canonical
module: product-spec
status: draft
authority: supporting
created: 2026-05-21
last_validated: unknown
---

# Human Understanding Check

Human Understanding Check verifies that a human can understand the Product Spec before UX/task planning.

This is not approval.
This is not a readiness gate.
This does not authorize execution.
This does not generate UX or tasks.

## Purpose
This review checks whether Product Spec content is understandable to the intended human reviewer without hidden assumptions.

## When To Use
Run this check before moving into deeper UX/task planning discussions.
Run it again after major Product Spec edits.

## Review Categories
Minimum categories:
- clarity
- terminology
- assumed knowledge
- ambiguity
- missing context
- undefined actors
- undefined success criteria

### clarity
What to check:
- sentences are understandable;
- key intent is explicit.

Risk examples:
- vague statements like "make it better" without concrete meaning.

What to do:
- ask clarification and rewrite unclear language.

### terminology
What to check:
- terms are defined or easy to understand.

Risk examples:
- internal words appear without explanation.

What to do:
- add short plain-language definitions.

### assumed knowledge
What to check:
- spec does not assume hidden product, domain, or process knowledge.

Risk examples:
- reviewer must already know internal process to understand scope.

What to do:
- add missing background context.

### ambiguity
What to check:
- no conflicting or multi-meaning statements.

Risk examples:
- one section says manual approval required, another implies automatic approval.

What to do:
- resolve contradiction before downstream planning.

### missing context
What to check:
- required background for understanding goals and constraints is present.

Risk examples:
- why the feature exists is missing.

What to do:
- add problem context and user context.

### undefined actors
What to check:
- human owner, user role, and system role are clear.

Risk examples:
- approval is mentioned but decision owner is unknown.

What to do:
- add explicit actor ownership.

### undefined success criteria
What to check:
- success condition is clear enough for a human to evaluate.

Risk examples:
- success says "works well" without observable criteria.

What to do:
- add clear reviewable success criteria.

## Outcome Tokens
Allowed outcomes:
- HUMAN_UNDERSTANDING_CHECK_READY_FOR_UX
- HUMAN_UNDERSTANDING_CHECK_NEEDS_CLARIFICATION
- HUMAN_UNDERSTANDING_CHECK_NEEDS_HUMAN_REVIEW
- HUMAN_UNDERSTANDING_CHECK_BLOCKED

Definitions:
- HUMAN_UNDERSTANDING_CHECK_READY_FOR_UX: understanding is sufficient for UX discussion if other gates also allow.
- HUMAN_UNDERSTANDING_CHECK_NEEDS_CLARIFICATION: understanding gaps should be clarified first.
- HUMAN_UNDERSTANDING_CHECK_NEEDS_HUMAN_REVIEW: a human owner decision is required.
- HUMAN_UNDERSTANDING_CHECK_BLOCKED: check cannot proceed safely because source context is missing or unreadable.

## Finding Severity
severity_levels:
- BLOCKING
- MAJOR
- MINOR
- INFO

Guidance:
- BLOCKING: must be resolved before downstream UX/task planning.
- MAJOR: should be resolved or explicitly accepted by human review.
- MINOR: does not block but should be recorded.
- INFO: contextual note only.

## Boundaries
Human Understanding Check is guidance for understanding quality.
It is not approval.
It is not a readiness gate.
It does not authorize execution.
It does not generate UX or tasks.
It does not create approval records.
It does not replace validation, readiness, or human gate requirements.
Human Understanding Check does not create approval.
Understanding confirmed does not automatically move a Product Spec to APPROVED or EXECUTION_READY.
