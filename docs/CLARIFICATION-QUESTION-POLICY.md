---
type: canonical
module: product-spec
status: draft
authority: supporting
created: 2026-05-21
last_validated: unknown
---

# Clarification Question Policy

Clarification Question Policy defines agent-facing guidance.

It is not executable logic.
It is not a chat runtime.
It is not a deterministic interview engine.
It does not create lifecycle transitions.
It does not create approval records.
It does not replace human review.

This document provides agent-facing guidance.
It does not authorize execution, commit, push, merge, deploy, or release.
It does not create approval records.
It does not replace human gate requirements.
It does not override runtime enforcement.
It does not implement an interview engine.

## When Clarification Is Required
Use clarification questions when:
- the problem is unclear
- user/actor is undefined
- goals and metrics are mixed
- acceptance criteria are absent or vague
- Non-Goals are missing for broad scope
- risks are unclear
- dependencies are unknown
- requirements conflict
- implementation is requested before product intent is clear
- downstream readiness would be unsafe without more information

## Clarification Levels
clarification_level:
  BLOCKING:
    meaning: "Cannot produce APPROVED/EXECUTION_READY Product Spec safely without answer"
  IMPORTANT:
    meaning: "Can draft Product Spec, but should not mark ready without review"
  OPTIONAL:
    meaning: "Useful detail, but not blocking for current Product Spec depth"

BLOCKING clarification should recommend lifecycle_status: NEEDS_CLARIFICATION.

IMPORTANT clarification should be recorded as Open Questions.

OPTIONAL clarification may be recorded in Future Expansion or UX Notes.

AI may recommend these classifications but must not approve lifecycle transitions on its own.

## Clarification Question Quality Rules
Clarification questions must be:
- specific
- answerable
- tied to a Product Spec section
- limited in number
- non-leading
- written in plain language
- clear about why the answer matters

Avoid:
- long interrogation lists
- vague “please clarify everything”
- technical jargon when user is non-technical
- mixing multiple unrelated issues in one question
- pushing implementation choices before intent is clear

Ask no more than 5 clarification questions in one pass unless the user explicitly requests a full review.

## Clarification Output Format
clarification_question:
  id:
  level:
  product_spec_section:
  question:
  why_it_matters:
  possible_answers:
  blocks:

Where:
- id is a stable local question ID
- level is BLOCKING, IMPORTANT, or OPTIONAL
- product_spec_section points to the affected Product Spec section
- question is the user-facing question
- why_it_matters explains the impact
- possible_answers may provide examples, not forced choices
- blocks identifies affected downstream step, if any

## Section 16 — Relationship To Lifecycle
This section consolidates lifecycle-related clarification boundaries already introduced above.
Section 12 defines operational clarification severity.
Section 16 defines the lifecycle authority boundary.

Clarification policy may recommend lifecycle states.

Clarification policy must not apply lifecycle transitions.

BLOCKING clarification may recommend NEEDS_CLARIFICATION.

Only Product Spec lifecycle/transition policy controls allowed transitions.

AI may recommend transitions.
AI must not autonomously approve Product Specs.
AI must not autonomously mark Product Specs as EXECUTION_READY.

## Relationship To Validation And Readiness
Requirement extraction and clarification policy happen before or during Product Spec drafting.

Validation checks deterministic structure.

Readiness gate checks target-specific downstream eligibility.

Extraction policy does not replace validation.

Clarification policy does not replace readiness gate.

A well-written clarification response does not authorize task generation or execution planning.
