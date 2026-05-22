---
type: canonical
module: product-spec
status: draft
authority: supporting
created: 2026-05-21
last_validated: unknown
---

# Decomposition Quality Policy

Decomposition Quality Policy defines criteria for reviewing future Product Spec to task decomposition.

Decomposition Quality Policy does not generate tasks.
Decomposition Quality Policy does not produce task graphs.
Decomposition Quality Policy does not create task contracts.
Decomposition Quality Policy is not execution planning.
Decomposition Quality Policy is not approval.
Decomposition Quality Policy does not authorize execution.

Decomposition quality review is not approval.
Decomposition quality review does not authorize task generation.
Decomposition quality review does not authorize task graph generation.
Decomposition quality review does not authorize execution planning.
Decomposition quality review does not authorize execution, commit, push, merge, deploy, or release.
Decomposition quality review does not create approval records.
Decomposition quality review does not replace validation, readiness gates, semantic review, feasibility review, human gate requirements, task state rules, or runtime enforcement.
Decomposition quality review does not replace validation.

## Purpose
Define quality criteria for deciding whether future decomposition from Product Spec into task graph/task contracts can be clear, bounded, traceable, and safe.

## When To Review
Run this review after Product Spec validation/readiness context is known, and before future task graph work.
Run again when Product Spec scope, lineage, or acceptance criteria materially change.

## Source Artifacts
Decomposition quality review may use:
- Product Spec
- Product Spec lifecycle status
- validation result
- readiness result
- semantic review result
- feasibility risk review result
- clarification questions
- plain-language summary
- lineage metadata
- source interview record, if available

Decomposition quality review must not invent missing source information.

If source information is missing, the review must record it as missing.

Unknown is better than invented.
Missing is better than guessed.

## Review Categories

### Product Spec Traceability
What to check:
- whether future task artifacts can link to Product Spec source fields.

Examples of decomposition risk:
- task candidate has no source Product Spec reference.

What to do:
- require traceability fields before decomposition proceeds.

Minimum traceability expectations for future task artifacts:
source_product_spec:
  spec_id:
  spec_version:
  product_spec_path:
  lineage_record:

Every future task contract generated from a Product Spec must be traceable to spec_id and spec_version.

A task candidate without Product Spec traceability is not decomposition-ready.

Traceability is not approval.
Traceability is not execution authorization.

### Task Atomicity
What to check:
- whether each task candidate is bounded, reviewable, independently understandable, tied to specific Product Spec intent, and small enough to validate.

Examples of decomposition risk:
- one task candidate covers unrelated workflows and multiple approval decisions;
- vague instruction such as “build the system”.

What to do:
- split large mixed tasks into smaller bounded task candidates.

A task candidate is too large if it combines unrelated workflows, unrelated user outcomes, or multiple independent approval decisions.

### Scope Containment
What to check:
- whether task candidates stay within Product Spec scope.

Examples of decomposition risk:
- task candidate implements Non-Goals;
- task candidate silently adds future expansion or extra user flows;
- task candidate adds approval/execution authority not defined in Product Spec governance;
- task candidate assumes missing dependencies are resolved.

What to do:
- recommend clarification or human review before task contracts are created.

If a future task candidate conflicts with Product Spec Non-Goals, decomposition quality review must recommend clarification or human review before task contracts are created.

### Non-Goals Consistency
What to check:
- whether Non-Goals are preserved during decomposition.

Examples of decomposition risk:
- Non-Goals moved into implementation scope.

What to do:
- mark as MAJOR or BLOCKING depending on impact.

### Acceptance Criteria Mapping
What to check:
- whether Product Spec Acceptance Criteria map to reviewable task-level checks.

Examples of decomposition risk:
- one task claims to satisfy all Acceptance Criteria without explanation;
- criteria are not mapped to any task candidate;
- task candidate introduces new criteria not present in Product Spec;
- acceptance criteria are implementation commands disguised as outcomes.

What to do:
- require explicit mapping per task candidate.

Acceptance Criteria should map to reviewable task-level checks.

A future task contract should clearly identify which Product Spec Acceptance Criteria it supports.

Acceptance Criteria must not be converted into execution authority.

### Dependency Ordering
What to check:
- prerequisite tasks;
- blocked tasks;
- dependency direction;
- human decision dependencies;
- UX dependencies;
- validation dependencies;
- readiness dependencies;
- external integration dependencies.

Examples of decomposition risk:
- order cannot be determined without guessing.

What to do:
- recommend clarification before task graph creation.

If task ordering would require guessing, decomposition quality review must recommend clarification before task graph creation.

### Duplicate Responsibility Risk
What to check:
- overlapping ownership across task candidates.

Examples of decomposition risk:
- two candidates own same acceptance criterion;
- shared concern exists but no integration responsibility is assigned.

What to do:
- assign explicit ownership and integration boundary.

Duplicate responsibility does not automatically block decomposition, but it must be made explicit and assigned.

### Hidden Work Risk
What to check:
- hidden implementation effort implied by short phrases.

Examples:
| Product Spec phrase | Hidden work risk |
|---|---|
| “Add approval button” | permissions, audit log, denial flow, escalation, ownership |
| “Send notification” | channels, templates, retries, opt-out, failure handling |
| “Show dashboard status” | status source, refresh, stale data, permissions |
| “Automate review” | authority boundaries, human gate, logging, failure mode |

What to do:
- surface hidden work before task contracts are created.

Hidden work must be surfaced before task contracts are created.

### UX Dependency Clarity
What to check:
- whether decomposition depends on M47 UX structure for new screens/workflows/states/approval UI/dashboard/mobile/error states.

Examples of decomposition risk:
- UX structure required but not available.

What to do:
- pause decomposition or explicitly record UX dependency.

Decomposition Quality Policy does not create UX.

If UX structure is needed, downstream work should wait for M47 or explicitly document the UX dependency.

### Risk / Approval Gate Clarity
What to check:
- approval behavior, destructive actions, runtime boundary changes, human gate, escalation, audit trail, permission model, agent autonomy.

Examples of decomposition risk:
- approval-sensitive work decomposed without owner/gate clarity.

What to do:
- require human review and gate clarity before decomposition output is accepted.

Task decomposition must not turn approval-sensitive Product Spec content into executable work without explicit gate and ownership clarity.

### Testability / Reviewability
What to check:
- whether task candidate outcomes can be reviewed/validated.

Examples of decomposition risk:
- candidate outcome cannot be verified.

What to do:
- refine acceptance mapping and validation expectations.

### Downstream Invalidation Awareness
What to check:
- whether future artifacts will record spec_id/spec_version and expect STALE/SUSPENDED handling after Product Spec changes.

Examples of decomposition risk:
- no version link, no invalidation awareness.

What to do:
- require lineage-ready references before task graph work.

If Product Spec version changes after task candidates are created, downstream artifacts may become STALE or SUSPENDED.

Decomposition quality review must check whether future task artifacts are expected to record spec_id and spec_version.

Decomposition quality review does not implement invalidation automation.

### Task Size Risk
What to check:
- candidate size vs practical review and validation scope.

Examples of decomposition risk:
- entire milestone packed into one task without explicit scoping.

What to do:
- split and scope.

### Cross-Cutting Concern Handling
What to check:
- how shared concerns (security, logging, audit, permissions) are assigned across tasks.

Examples of decomposition risk:
- cross-cutting concerns duplicated inconsistently.

What to do:
- define clear ownership model.

### Execution Authority Boundary
What to check:
- that decomposition output does not claim execution authority.

Examples of decomposition risk:
- decomposition text implies automatic execution.

What to do:
- remove authority claims and escalate for human review if needed.

## Review Outcomes
Allowed outcomes:
- DECOMPOSITION_QUALITY_READY_FOR_TASK_GRAPH
- DECOMPOSITION_QUALITY_NEEDS_SPEC_REFINEMENT
- DECOMPOSITION_QUALITY_NEEDS_SCOPING
- DECOMPOSITION_QUALITY_NEEDS_HUMAN_REVIEW
- DECOMPOSITION_QUALITY_BLOCKED

Definitions:
- DECOMPOSITION_QUALITY_READY_FOR_TASK_GRAPH: no blocking decomposition quality issue was found; Product Spec may proceed toward future task graph work if semantic, feasibility, readiness, and lifecycle conditions are otherwise met.
- DECOMPOSITION_QUALITY_NEEDS_SPEC_REFINEMENT: Product Spec needs clarification or refinement before quality decomposition is possible.
- DECOMPOSITION_QUALITY_NEEDS_SCOPING: Product Spec scope must be narrowed before task graph/decomposition work.
- DECOMPOSITION_QUALITY_NEEDS_HUMAN_REVIEW: issue requires human product/ownership/technical decision.
- DECOMPOSITION_QUALITY_BLOCKED: review cannot be completed because source artifacts are missing, unreadable, structurally blocked, or insufficient for safe decomposition review.

Examples of DECOMPOSITION_QUALITY_BLOCKED:
- source Product Spec is missing or unreadable
- validation result is PRODUCT_SPEC_VALIDATION_BLOCKED
- readiness gate is blocked and decomposition eligibility cannot be assessed safely
- semantic review is blocked due to unresolved contradictions
- feasibility review is blocked due to missing scope boundary
- required source artifacts are unavailable and reviewer would need to guess

DECOMPOSITION_QUALITY_READY_FOR_TASK_GRAPH is not approval.
DECOMPOSITION_QUALITY_READY_FOR_TASK_GRAPH is not task generation.
DECOMPOSITION_QUALITY_READY_FOR_TASK_GRAPH is not execution planning.
DECOMPOSITION_QUALITY_READY_FOR_TASK_GRAPH does not authorize execution.

## Finding Severities
decomposition_quality_severity:
  BLOCKING:
    meaning: "Must be resolved before task graph/decomposition proceeds"
  MAJOR:
    meaning: "Should be resolved or explicitly accepted by human review"
  MINOR:
    meaning: "Does not block downstream work but should be recorded"
  INFO:
    meaning: "Contextual observation only"

Relationship to outcomes:

| Highest finding severity | Typical outcome |
|---|---|
| BLOCKING | DECOMPOSITION_QUALITY_NEEDS_SPEC_REFINEMENT, DECOMPOSITION_QUALITY_NEEDS_SCOPING, or DECOMPOSITION_QUALITY_BLOCKED |
| MAJOR | DECOMPOSITION_QUALITY_NEEDS_HUMAN_REVIEW |
| MINOR | DECOMPOSITION_QUALITY_READY_FOR_TASK_GRAPH with notes |
| INFO | DECOMPOSITION_QUALITY_READY_FOR_TASK_GRAPH with notes |

If multiple findings exist, reviewers should consider the highest finding severity first.
However, decomposition quality outcome is reviewer judgment, not deterministic computation.
The severity-to-outcome table provides default guidance, not an automatic rule.
Reviewer must explain any deviation from the typical outcome mapping.
Outcome deviation must include a written rationale.

## Relationship To Product Spec Lineage
This policy aligns with lineage requirements in docs/SPEC-TO-TASK-LINEAGE.md.
It checks whether future decomposition artifacts can preserve source traceability and invalidation awareness.

## Relationship To Semantic Review
Semantic review checks meaning, ambiguity, and likely contradictions.

Decomposition quality review checks whether future task decomposition can be clear, bounded, traceable, and safe.

Decomposition quality review does not replace semantic review.
Semantic review does not replace decomposition quality review.
If semantic review found blocking ambiguity, decomposition quality review may be blocked or limited.

## Relationship To Feasibility Review
Feasibility review checks scope, dependency, complexity, and realism risk.

Decomposition quality review checks whether Product Spec content can be decomposed into bounded future task artifacts.

Decomposition quality review does not estimate effort, timeline, story points, or cost.
If feasibility review found blocking scope risk, decomposition quality review may be blocked or limited.

## Relationship To M47 UX
M47 defines composable UX structure.

Decomposition quality review may identify that UX structure is needed before task graph work.

Decomposition quality review does not create layouts, wireframes, visual hierarchy, components, or prototypes.

## Relationship To M48 Execution Planning
M48 performs execution planning and realism analysis.

Decomposition Quality Policy defines quality criteria that M48 should consider.

This policy does not create task graphs, task contracts, schedules, assignments, or execution plans.

## Non-Authority Boundary
This document defines decomposition quality policy.
It does not authorize execution, commit, push, merge, deploy, or release.
It does not create approval records.
It does not replace human gate requirements.
It does not override runtime enforcement.
