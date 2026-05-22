---
type: canonical
module: product-spec
status: draft
authority: supporting
created: 2026-05-21
last_validated: unknown
---

# Product Spec Transition Policy

## Purpose
This document defines allowed Product Spec state transitions and governance controls.
This document defines lifecycle policy.
It does not authorize execution, commit, push, merge, deploy, or release.
It does not create approval records.
It does not replace human gate requirements.
It does not override runtime enforcement.

## Approval and Readiness Boundary
| State | Meaning |
|---|---|
| APPROVED | Human agrees with product intent and scope |
| EXECUTION_READY | Spec passed required readiness checks for downstream execution planning |

APPROVED is necessary but not sufficient for EXECUTION_READY.
EXECUTION_READY must not be inferred from APPROVED alone.

## Allowed Transition Matrix
allowed_transitions:

  DRAFT:
    - INTERVIEWING
    - ARCHIVED

  INTERVIEWING:
    - NEEDS_CLARIFICATION
    - REVIEW
    - ARCHIVED

  NEEDS_CLARIFICATION:
    - INTERVIEWING
    - REVIEW
    - ARCHIVED

  REVIEW:
    - APPROVED
    - NEEDS_CLARIFICATION
    - ARCHIVED

  APPROVED:
    - EXECUTION_READY
    - REVIEW
    - ARCHIVED

  EXECUTION_READY:
    - REVIEW
    - ARCHIVED

  ARCHIVED: []

## Transition Authority
transition_authority:

  REVIEW_to_APPROVED:
    requires_human_confirmation: true
    ai_may_recommend: true
    ai_may_apply: false

  APPROVED_to_EXECUTION_READY:
    requires_validation: true
    requires_human_confirmation: true
    ai_may_recommend: true
    ai_may_apply: false

  any_to_ARCHIVED:
    requires_human_confirmation: true
    ai_may_recommend: true
    ai_may_apply: false

AI may recommend transitions.
AI must not autonomously approve Product Specs.
AI must not autonomously mark Product Specs as EXECUTION_READY.
AI must not archive Product Specs without human confirmation.

## Post-Approval Modification Policy
post_approval_modification_policy:

  material_changes:
    reset_state_to: REVIEW
    requires_revalidation: true

  non_material_changes:
    allowed_without_reset: true
    must_be_recorded: true

Material changes include changes to:
- Problem
- Goals
- Non-Goals
- Acceptance Criteria
- Constraints
- Risks
- Dependencies
- Open Questions
- Success Metrics
- lifecycle status

Material changes after APPROVED invalidate previous execution readiness.

## Downstream Invalidation Policy
downstream_invalidation_policy:

  leaving_execution_ready:
    generated_task_contracts:
      status: SUSPENDED
      requires_revalidation: true

    generated_task_graphs:
      status: STALE
      requires_regeneration_or_review: true

If a Product Spec leaves EXECUTION_READY due to material changes, downstream generated task contracts must not continue as if the spec were still valid.
This is policy only.
Do not implement task suspension logic.

## Relationship to Task Lifecycle
Product Spec lifecycle governs product intent artifacts.
Task lifecycle governs executable task artifacts.
Product Spec state does not directly mutate task state.
Task state changes require existing task transition rules.

This policy references existing task governance documents and does not override them.

## Cross Reference
- Lineage policy: `docs/SPEC-TO-TASK-LINEAGE.md`

- Validation policy: 

- Validation policy: docs/PRODUCT-SPEC-VALIDATION.md

- Readiness gate policy: docs/PRODUCT-SPEC-READINESS-GATE.md
