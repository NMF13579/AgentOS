---
type: canonical
module: product-spec
status: draft
authority: supporting
created: 2026-05-21
last_validated: unknown
---

# Product Spec Lifecycle

## Purpose
This document defines lifecycle policy for Product Spec artifacts in AgentOS.
This document defines lifecycle policy.
It does not authorize execution, commit, push, merge, deploy, or release.
It does not create approval records.
It does not replace human gate requirements.
It does not override runtime enforcement.

## Core Boundary
APPROVED is a product-level human decision.

EXECUTION_READY is an operational validation state.

APPROVED does not automatically authorize execution.

No Product Spec in APPROVED state means no downstream task generation.

No Product Spec in EXECUTION_READY state means no execution planning.

## Lifecycle States

### DRAFT
- meaning: initial product spec drafting.
- entry condition: a new spec record is created.
- exit condition: enough interview context exists to continue into structured synthesis.
- downstream task generation allowed: no.
- execution planning allowed: no.
- human confirmation required: no.
- AI may recommend transition: yes.
- AI may apply transition: no.

### INTERVIEWING
- meaning: product intent is being structured from interview evidence.
- entry condition: draft was promoted for evidence-backed synthesis.
- exit condition: either key gaps are detected (move to NEEDS_CLARIFICATION) or evidence is sufficient for REVIEW.
- downstream task generation allowed: no.
- execution planning allowed: no.
- human confirmation required: no.
- AI may recommend transition: yes.
- AI may apply transition: no.

### NEEDS_CLARIFICATION
- meaning: material ambiguity or missing product intent blocks reliable review.
- entry condition: unresolved ambiguity detected during interviewing/review.
- exit condition: clarifications are captured and review can resume.
- downstream task generation allowed: no.
- execution planning allowed: no.
- human confirmation required: yes.
- AI may recommend transition: yes.
- AI may apply transition: no.

### REVIEW
- meaning: spec is under product-level quality and scope review.
- entry condition: required lifecycle content is present for review.
- exit condition: spec is either APPROVED, sent back for clarification, or ARCHIVED.
- downstream task generation allowed: no.
- execution planning allowed: no.
- human confirmation required: yes.
- AI may recommend transition: yes.
- AI may apply transition: no.

### APPROVED
- meaning: human decision confirms product intent and scope.
- entry condition: review completed with explicit human confirmation.
- exit condition: operational readiness checks pass (EXECUTION_READY), re-review is needed (REVIEW), or archival is chosen.
- downstream task generation allowed: yes.
- execution planning allowed: no.
- human confirmation required: yes.
- AI may recommend transition: yes.
- AI may apply transition: no.

### EXECUTION_READY
- meaning: approved product intent has passed required operational readiness checks for downstream execution planning.
- entry condition: APPROVED plus required validation and explicit human confirmation.
- exit condition: review is reopened or spec is archived.
- downstream task generation allowed: yes.
- execution planning allowed: yes.
- human confirmation required: yes.
- AI may recommend transition: yes.
- AI may apply transition: no.

### ARCHIVED
- meaning: spec is retired from active planning usage.
- entry condition: explicit decision to archive from an allowed source state.
- exit condition: none.
- downstream task generation allowed: no.
- execution planning allowed: no.
- human confirmation required: yes.
- AI may recommend transition: yes.
- AI may apply transition: no.

## Relationship to Task Lifecycle
Product Spec lifecycle governs product intent artifacts.
Task lifecycle governs executable task artifacts.
Product Spec state does not directly mutate task state.
Task state changes require existing task transition rules.

This relationship is aligned with:
- `docs/TASK-STATE-MACHINE.md`
- `docs/TASK-TRANSITION-RULES.md`

## Non-Authority Boundary
This lifecycle policy is documentation-only governance.
It must not be interpreted as automation authority.
It does not grant runtime permission escalation.

## Cross Reference
- Lineage policy: `docs/SPEC-TO-TASK-LINEAGE.md`

- Validation policy: 

- Validation policy: docs/PRODUCT-SPEC-VALIDATION.md

- Readiness gate policy: docs/PRODUCT-SPEC-READINESS-GATE.md
