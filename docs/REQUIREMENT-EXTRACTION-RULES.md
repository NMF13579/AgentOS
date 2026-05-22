---
type: canonical
module: product-spec
status: draft
authority: supporting
created: 2026-05-21
last_validated: unknown
---

# Requirement Extraction Rules

Requirement extraction rules guide agents and reviewers.

They are not executable logic.
They are not a deterministic interview engine.
They do not guarantee semantic correctness.
They do not authorize lifecycle transitions.
They do not replace human review.

This document provides agent-facing guidance.
It does not authorize execution, commit, push, merge, deploy, or release.
It does not create approval records.
It does not replace human gate requirements.
It does not override runtime enforcement.
It does not implement an interview engine.

## Extraction Coverage
Extract and classify:
- Problem
- Users
- Jobs-To-Be-Done
- Goals
- Non-Goals
- Constraints
- Risks
- Success Metrics
- Acceptance Criteria
- Dependencies
- Open Questions
- Assumptions
- Out-of-scope items

## Problem vs Solution
Problem describes the user/business pain or need.
Solution describes one possible way to address it.

Agents must not treat a proposed solution as proof that the underlying problem is understood.

| Raw input | Problem | Proposed solution |
|---|---|---|
| “Add a dashboard button so users stop asking support” | Users cannot find needed status/action information | Add dashboard button |
| “Make onboarding shorter” | Onboarding may be creating friction or abandonment | Reduce onboarding steps |

If the problem is unclear, the agent must ask clarification before finalizing Product Spec Goals or Acceptance Criteria.

## MUST vs NICE-TO-HAVE
requirement_priority:
  MUST:
    meaning: "Required for the current Product Spec to be considered successful"
  SHOULD:
    meaning: "Important but may be deferred with human confirmation"
  NICE_TO_HAVE:
    meaning: "Useful but not required for current scope"
  OUT_OF_SCOPE:
    meaning: "Explicitly excluded from current scope"

NICE_TO_HAVE items must not silently become Acceptance Criteria.

OUT_OF_SCOPE items must be reflected in Non-Goals when relevant.

MUST requirements should be traceable to Goals or Acceptance Criteria.

## Goals vs Success Metrics
Goals define desired product outcomes and direction.
Success Metrics define measurable indicators used to evaluate whether the goals were achieved.

goal:
  "Reduce onboarding confusion for non-technical users"

success_metrics:
  - "onboarding completion rate > 80%"
  - "support questions about onboarding reduced by 40%"

If a metric is qualitative and not measurable, classify it as a Goal candidate, not a Success Metric.

If a Goal has no measurable signal, record an Open Question or propose a measurable Success Metric for human review.

## Non-Goals
Non-Goals are explicit exclusions from current scope.
Non-Goals are not future feature wishlists.

When raw input contains requests that are too broad, risky, unrelated, or future-facing, the agent must propose them as Non-Goals or Future Expansion candidates.

If a proposed downstream task conflicts with Non-Goals, human clarification is required before task contracts may be created.

## Acceptance Criteria
Acceptance Criteria describe observable conditions that show the Product Spec goal is satisfied.

Acceptance Criteria should be:
- specific
- testable or reviewable
- tied to Product Spec Goals
- not implementation-specific unless implementation is part of the product requirement
- not hidden task instructions

Acceptance Criteria must not authorize execution.
Acceptance Criteria must not define commits, pushes, merges, deployment, or runtime permissions.

## Assumptions
Common assumption categories:
- user identity assumptions
- workflow assumptions
- permission assumptions
- data availability assumptions
- technical capability assumptions
- legal/compliance assumptions
- timing/effort assumptions
- integration assumptions

Assumptions that affect Goals, Risks, Acceptance Criteria, Dependencies, or Open Questions must be recorded explicitly.

If assumption is unresolved and material, agent must recommend:
lifecycle_status: NEEDS_CLARIFICATION

But must not apply the transition automatically.

## Risks
Product risk categories:
- user harm
- privacy/security
- compliance/legal
- incorrect automation
- destructive action
- misunderstanding by non-technical users
- operational complexity
- dependency risk
- scope expansion risk

Risk extraction is a product reasoning aid.
It is not a security audit.
It is not feasibility estimation.
It is not approval.

High-risk or unclear-risk items should produce clarification questions or human review recommendations.

## Dependencies
Dependency categories:
- internal product dependencies
- existing AgentOS policy dependencies
- external service dependencies
- data dependencies
- user workflow dependencies
- legal/compliance dependencies
- task/decomposition dependencies

Dependencies must be recorded as Product Spec content, not silently converted into tasks.

## Open Questions
Create Open Questions when there is:
- unclear actor
- unclear success condition
- unclear risk
- unclear constraint
- conflicting requirement
- missing acceptance criteria
- unclear dependency
- unclear Non-Goal
- unclear lifecycle target

Open Questions are not failure by themselves.

Open Questions become blocking when they affect Acceptance Criteria, Risks, Dependencies, lifecycle readiness, or downstream task generation.

Use existing markers when relevant:
- open_questions_acknowledged_by_human: true
- open_questions_block_execution_ready: true

## Relationship to Lifecycle, Validation, and Readiness
This policy may recommend clarifications and lifecycle direction.
It must not apply lifecycle transitions.

Extraction policy happens before or during Product Spec drafting.
Validation checks deterministic structure.
Readiness gate checks target-specific downstream eligibility.

Extraction policy does not replace validation.
Clarification policy does not replace readiness gate.
A well-written clarification response does not authorize task generation or execution planning.
