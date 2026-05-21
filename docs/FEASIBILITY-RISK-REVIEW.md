---
type: canonical
module: product-spec
status: draft
authority: supporting
created: 2026-05-21
last_validated: unknown
---

# Feasibility Risk Review

Feasibility Risk Review helps agents and reviewers identify scope, dependency, complexity, and realism risks in a Product Spec.

Feasibility Risk Review is not an effort estimator.
Feasibility Risk Review is not a timeline estimator.
Feasibility Risk Review is not a cost estimator.
Feasibility Risk Review is not validation.
Feasibility Risk Review is not readiness.
Feasibility Risk Review is not approval.
Feasibility Risk Review does not authorize execution.

Feasibility review is not approval.
Feasibility review does not authorize task generation.
Feasibility review does not authorize execution planning.
Feasibility review does not authorize execution, commit, push, merge, deploy, or release.
Feasibility review does not create approval records.
Feasibility review does not replace validation, readiness gates, semantic review, human gate requirements, task state rules, or runtime enforcement.

## Purpose
Feasibility Risk Review helps reviewers decide whether a Product Spec is realistically scoped enough to proceed toward M47 UX structure work.

## When To Review
Run feasibility review after structural validation and during readiness/quality review.
Run it again when scope, dependencies, integrations, or assumptions materially change.

## Source Artifacts
Feasibility Risk Review may use:
- Product Spec
- Product Spec lifecycle status
- validation result
- readiness result
- semantic review result
- clarification questions
- plain-language summary
- lineage metadata
- source interview record, if available

Feasibility review must not invent missing source information.

If source information is missing, the review must record it as missing.

Unknown is better than invented.
Missing is better than guessed.

## Review Categories

### Scope Size
What to check:
- whether scope is too broad for one coherent Product Spec.

Examples of feasibility risk:
- multiple unrelated user groups;
- multiple unrelated workflows;
- many unrelated features in one spec;
- unclear MVP boundary;
- “build the whole platform” language;
- acceptance criteria that describe multiple products;
- Non-Goals missing for broad product requests.

What to do:
- recommend scoping and split boundaries.

If Product Spec scope is too broad, feasibility review should recommend NEEDS_SCOPING before UX or decomposition proceeds.

### MVP Boundary
What to check:
- separation between current MVP, future expansion, Non-Goals, deferred functionality, and optional improvements.

Examples of feasibility risk:
- future features treated as current scope;
- Non-Goals conflict with current acceptance criteria.

What to do:
- request clear MVP boundary and deferment list.

A Product Spec without a clear MVP boundary may be structurally valid but not feasible for downstream UX/decomposition.

Future Expansion must not silently become current Acceptance Criteria.

### Dependency Risk
What to check:
- dependence on unavailable data, unknown APIs, external systems, legal/compliance review, third-party services, human operations, unresolved lifecycle behavior, or unavailable UX decisions.

Examples of feasibility risk:
- required dependency has no owner;
- dependency is mentioned but not available.

What to do:
- add feasibility finding and scoping question.

Unresolved dependencies that affect scope, acceptance criteria, risk, or downstream readiness must be recorded as feasibility findings.

### Integration Risk
What to check:
- integration assumptions with GitHub, external IDEs, cloud execution environments, messaging systems, payment systems, medical/clinical systems, third-party AI providers, and user identity systems.

Examples of feasibility risk:
- integration assumed available without evidence;
- integration permissions/limits are unknown.

What to do:
- escalate to human review when critical.

Integration risk review identifies uncertainty.

It must not assume an integration is easy or available without source evidence.

### Data Availability Risk
What to check:
- required data, source of data, data ownership, storage constraints, privacy/compliance constraints, freshness needs, and whether missing data blocks downstream design.

Examples of feasibility risk:
- success metric requires data that is unavailable;
- privacy constraints are unknown.

What to do:
- add risk finding and block/scoping recommendation when needed.

If Product Spec success depends on data that is unavailable, undefined, or restricted, feasibility review must mark the risk explicitly.

### Operational Complexity
What to check:
- human-in-the-loop process, manual review, escalation path, audit trail, rollback path, support workflow, owner responsibilities, and incident handling.

Examples of feasibility risk:
- “Add approve button” but no permission/audit/escalation model.

What to do:
- request explicit operational design assumptions.

Operational complexity must not be hidden behind simple UI language.

### User Workflow Complexity
What to check:
- whether user flow has too many branches, unclear decisions, or unclear handoffs.

Examples of feasibility risk:
- user flow depends on undefined decisions.

What to do:
- recommend scoping and clarification before UX work.

### Approval / Ownership Complexity
What to check:
- whether approval owner and decision boundaries are explicit.

Examples of feasibility risk:
- multiple teams implied but no final owner.

What to do:
- mark as HIGH or BLOCKING based on impact.

### Compliance / Safety Risk
What to check:
- legal/compliance/safety constraints that can block delivery.

Examples of feasibility risk:
- regulated behavior without compliance boundary definition.

What to do:
- require human review and scope constraint.

### Automation Risk
What to check:
- autonomous approval/execution assumptions, destructive actions, background actions without review, automatic task state changes, readiness bypass, runtime enforcement bypass, missing owner clarity.

Examples of feasibility risk:
- “auto-approve all high-risk actions”.

What to do:
- recommend human review or scoping before downstream work.

If automation risk conflicts with AgentOS authority boundaries, feasibility review must recommend human review or scoping before downstream work proceeds.

### External Service Risk
What to check:
- dependence on external service uptime, limits, legal terms, or unknown behavior.

Examples of feasibility risk:
- required third-party feature not confirmed.

What to do:
- add dependency risk and fallback requirement.

### Technical Unknowns
What to check:
- unknown technical constraints that may expand scope.

Examples of feasibility risk:
- required behavior depends on an unverified capability.

What to do:
- classify risk and route to human review if material.

### Timeline / Effort Claim Risk
What to check:
- unsupported claims such as “simple”, “quick”, “just add”, “only needs”, “small change”, “one day”, “easy MVP”, “fully automate”.

Examples of feasibility risk:
- timeline confidence without evidence.

What to do:
- record as risk, require evidence or scoping.

Feasibility Risk Review must not produce exact timelines, hours, story points, or cost estimates.

Unsupported effort claims should be recorded as risk findings, not converted into estimates.

Allowed output:
risk_level: LOW | MEDIUM | HIGH | BLOCKING

Forbidden output fields:
estimated_days:
estimated_hours:
story_points:
cost:

These are forbidden as output fields, not forbidden as ordinary words inside explanatory prose.

### Downstream UX Readiness Risk
What to check:
- whether unresolved feasibility risks would force UX/decomposition to guess.

Examples of feasibility risk:
- unresolved scope/ownership/integration questions required for UX structure.

What to do:
- recommend NEEDS_SCOPING or NEEDS_HUMAN_REVIEW before M47.

## Review Outcomes
Allowed outcomes:
- FEASIBILITY_REVIEW_READY_FOR_UX
- FEASIBILITY_REVIEW_NEEDS_SCOPING
- FEASIBILITY_REVIEW_NEEDS_HUMAN_REVIEW
- FEASIBILITY_REVIEW_BLOCKED

Definitions:
- FEASIBILITY_REVIEW_READY_FOR_UX: no blocking feasibility risk was found; Product Spec may proceed toward M47 UX structure work if semantic review and readiness conditions are otherwise met.
- FEASIBILITY_REVIEW_NEEDS_SCOPING: scope, dependencies, or MVP boundary must be narrowed or clarified before UX/decomposition proceeds.
- FEASIBILITY_REVIEW_NEEDS_HUMAN_REVIEW: risk requires human product/ownership/technical decision.
- FEASIBILITY_REVIEW_BLOCKED: review cannot be completed because source artifacts are missing, unreadable, structurally blocked, or insufficient for safe risk review.

Examples of FEASIBILITY_REVIEW_BLOCKED:
- source Product Spec is missing or unreadable
- validation result is PRODUCT_SPEC_VALIDATION_BLOCKED
- readiness gate is blocked and feasibility cannot be assessed safely
- Product Spec lacks enough scope information to distinguish MVP from future expansion
- required source artifacts are unavailable and reviewer would need to guess

FEASIBILITY_REVIEW_READY_FOR_UX is not approval.
FEASIBILITY_REVIEW_READY_FOR_UX is not validation PASS.
FEASIBILITY_REVIEW_READY_FOR_UX is not readiness READY.
FEASIBILITY_REVIEW_READY_FOR_UX does not authorize execution.

## Risk Levels
feasibility_risk_level:

LOW:
meaning: "No material feasibility concern identified"

MEDIUM:
meaning: "Feasibility concern exists but can likely proceed with notes"

HIGH:
meaning: "Feasibility concern should be resolved or reviewed before downstream work"

BLOCKING:
meaning: "Downstream UX/decomposition should not proceed until resolved"

Relationship to outcomes:

| Highest risk level | Typical outcome |
|---|---|
| BLOCKING | FEASIBILITY_REVIEW_NEEDS_SCOPING or FEASIBILITY_REVIEW_BLOCKED |
| HIGH | FEASIBILITY_REVIEW_NEEDS_HUMAN_REVIEW or FEASIBILITY_REVIEW_NEEDS_SCOPING |
| MEDIUM | FEASIBILITY_REVIEW_READY_FOR_UX with notes or FEASIBILITY_REVIEW_NEEDS_SCOPING |
| LOW | FEASIBILITY_REVIEW_READY_FOR_UX |

If multiple risks exist, reviewers should consider the highest risk level first.
However, feasibility review outcome is reviewer judgment, not deterministic computation.
The risk-to-outcome table provides default guidance, not an automatic rule.
Reviewer must explain any deviation from the typical outcome mapping.
Outcome deviation must include a written rationale.

## Relationship To Semantic Review
Semantic review checks meaning, ambiguity, and likely contradictions.

Feasibility review checks scope, dependency, complexity, and realism risk.

Feasibility review does not replace semantic review.
Semantic review does not replace feasibility review.
If semantic review found blocking ambiguity, feasibility review may be blocked or limited.
If feasibility review identifies scope risk, it may recommend clarification or scoping even if semantic review was otherwise acceptable.

## Relationship To Validation And Readiness
Validation checks deterministic structure.

Readiness checks target-specific downstream eligibility.

Feasibility review checks whether the Product Spec appears realistically scoped enough for downstream UX/decomposition.

Feasibility review must not downgrade validation failures into notes.

Feasibility review must not upgrade readiness failures into downstream permission.
If validation failed, feasibility review may be blocked or limited.
If readiness failed, feasibility review may still provide useful findings, but must not claim the Product Spec can proceed.

Feasibility review does not replace validation.

## Relationship To M47 UX
Feasibility review prepares Product Specs for M47 UX structure work by identifying scope and dependency risks.

It does not create UX layouts, wireframes, visual hierarchy, components, or prototypes.

If UX work would require designing around unresolved feasibility risks, feasibility review should recommend scoping or human review.

## Relationship To M48 Execution Planning
Feasibility Risk Review is not execution planning.

It does not produce task graphs.
It does not estimate effort.
It does not assign work.
It does not calculate schedules.
It does not calculate cost.

Detailed execution planning and realism analysis belongs to M48.

## Non-Authority Boundary
This document defines feasibility risk review policy.
It does not authorize execution, commit, push, merge, deploy, or release.
It does not create approval records.
It does not replace human gate requirements.
It does not override runtime enforcement.
