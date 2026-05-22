---
type: canonical
module: product-spec
status: canonical
authority: canonical
created: unknown
last_validated: unknown
---

# Product Spec Architecture

## Purpose
Product Spec is the canonical source-of-truth artifact for product intent in AgentOS.
It defines what should be built, why it should exist, who it serves, constraints, risks, and acceptance boundaries.

Product Spec defines:
- WHAT should be built
- WHY it should exist
- WHO it serves
- constraints, risks, and acceptance boundaries

Product Spec does NOT define:
- implementation details
- commits
- runtime authority
- approvals
- deployment authority
- UX layouts
- visual components
- autonomous task execution

## Architecture Position
Flow:

Problem Interview
↓
Product Spec
↓
UX structure / task decomposition / execution planning

Relationship map:
- M45 Problem Interview: provides source interview evidence; interview completeness is not execution authority.
- FEAT/TASK systems: may consume Product Spec as input but are not overridden by Product Spec.
- Task State Machine: remains authoritative for task lifecycle; Product Spec does not replace it.
- Spec-to-Task Generator: may generate candidate contracts only when policy conditions are satisfied.
- Future M47 UX layer: consumes interaction intent; owns visual realization.
- Execution layer: remains operational and human-gated; Product Spec does not grant runtime permissions.

## Product Lifecycle vs Frontmatter Boundary
Product lifecycle statuses such as DRAFT, REVIEW, APPROVED, and EXECUTION_READY belong to Product Spec body/schema fields.
They must not be confused with the standard frontmatter status field from docs/FRONTMATTER-STANDARD.md.
The frontmatter status field must use existing lowercase FRONTMATTER-STANDARD.md values such as draft, active, canonical, archived, deprecated, or unknown.

## Core Policies
APPROVED is a product-level human decision.

EXECUTION_READY is an operational validation state.

APPROVED does not automatically authorize execution.

## Canonical Sections
### Required Sections
1. Problem
- Purpose: define the core problem and context.
- Expected content: current pain, affected scenario, why this matters now.
- Minimal acceptable completeness: 2-5 clear sentences with concrete user pain.
- Required: yes.

2. Users
- Purpose: define who the spec serves.
- Expected content: primary users, secondary users, relevant roles.
- Minimal acceptable completeness: at least one named primary user group.
- Required: yes.

3. Jobs-To-Be-Done
- Purpose: describe key user jobs and intended outcomes.
- Expected content: job statements in user language.
- Minimal acceptable completeness: at least one core job statement.
- Required: yes.

4. Goals
- Purpose: define desired product outcomes and direction.
- Expected content: outcome-oriented goals, can be qualitative.
- Minimal acceptable completeness: at least one clear product outcome.
- Required: yes.

5. Non-Goals
- Purpose: define explicit exclusions from current scope.
- Expected content: what will not be built now.
- Minimal acceptable completeness: at least one explicit exclusion or explicit "none" with rationale.
- Required: yes.

6. Constraints
- Purpose: define limiting conditions.
- Expected content: time, policy, technical, legal, organizational boundaries.
- Minimal acceptable completeness: at least one real constraint or explicit "none".
- Required: yes.

7. Risks
- Purpose: define known product and delivery risks.
- Expected content: risk statements and impact.
- Minimal acceptable completeness: at least one risk or explicit "none".
- Required: yes.

8. Success Metrics
- Purpose: define measurable indicators for goal achievement.
- Expected content: measurable metrics with thresholds.
- Minimal acceptable completeness: at least one measurable metric.
- Required: yes.

9. Acceptance Criteria
- Purpose: define boundaries for acceptable product behavior/outcomes.
- Expected content: testable acceptance statements.
- Minimal acceptable completeness: at least one testable criterion.
- Required: yes.

10. Dependencies
- Purpose: define external/internal dependencies.
- Expected content: required inputs, teams, systems, approvals.
- Minimal acceptable completeness: at least one dependency or explicit "none".
- Required: yes.

11. Open Questions
- Purpose: keep unresolved uncertainty explicit.
- Expected content: unresolved questions or explicit "none" or "resolved".
- Minimal acceptable completeness: explicit list OR explicit "none"/"resolved".
- Required: yes.

### Optional Sections
1. UX Notes
- Purpose: capture interaction intent hints.
- Expected content: actors, choices, response expectations.
- Minimal acceptable completeness: optional free-form notes.
- Required: no.

2. Rollout Notes
- Purpose: rollout context and sequencing considerations.
- Expected content: staged rollout notes, stakeholder alignment notes.
- Minimal acceptable completeness: optional free-form notes.
- Required: no.

3. Compliance Notes
- Purpose: compliance reminders and constraints.
- Expected content: regulated context notes, controls to verify later.
- Minimal acceptable completeness: optional free-form notes.
- Required: no.

4. Future Expansion
- Purpose: explicitly defer future direction.
- Expected content: post-scope areas for later milestones.
- Minimal acceptable completeness: optional free-form notes.
- Required: no.

## Goals vs Success Metrics
Goals define desired product outcomes and direction.

Success Metrics define measurable indicators used to evaluate whether the goals were achieved.

Goals may be qualitative.
Success Metrics must be measurable.

Example:
goal:
  "Reduce onboarding confusion for non-technical users"

success_metrics:
  - "onboarding completion rate > 80%"
  - "support questions reduced by 40%"

## Non-Goals Policy
Non-Goals are explicit exclusions from current scope.
Non-Goals are not future feature wishlists.

Non-Goal conflict policy:
If proposed decomposition, task generation, or execution planning conflicts with Product Spec Non-Goals, human clarification is required before task contracts may be created.

## Progressive Specification Depth
Specification depth must scale with product complexity.

small_change:
  expected_depth: minimal
  example: "Small copy change, isolated UI adjustment, simple documentation improvement"

medium_feature:
  expected_depth: structured
  example: "New onboarding flow, dashboard section, user-facing workflow"

large_or_high_risk_system:
  expected_depth: full
  example: "Medical workflow, payment system, security-sensitive feature, multi-role product area"

Forbidden:
- enterprise-style overdocumentation for simple changes
- forcing massive specs for low-risk work
- treating missing unnecessary sections as failure when progressive depth says they are not required

## Product Spec vs UX Boundary
Product Spec may define:
- actors
- user intent
- interaction goals
- flow-level requirements
- edge cases
- required user choices
- required system responses

Product Spec must not define:
- screen layouts
- wireframes
- visual hierarchy
- component placement
- pixel-level design
- UI implementation

| Layer | Example |
|---|---|
| Product Spec | User must be able to cancel onboarding at any step. |
| UX Layer | Cancel button is placed in the top-right corner of every onboarding screen. |
| Product Spec | User must review risk before approving a high-risk agent action. |
| UX Layer | Risk card appears above the primary approval button with warning styling. |

Product Spec defines interaction intent.
UX Layer defines visual realization.

## Lifecycle States
### DRAFT
- Meaning: initial draft under creation.
- Allowed use: early structuring.
- Downstream work allowed: no.
- Human confirmation required: no.

### INTERVIEWING
- Meaning: spec is being derived from interview evidence.
- Allowed use: synthesis and clarification capture.
- Downstream work allowed: no.
- Human confirmation required: no.

### NEEDS_CLARIFICATION
- Meaning: unresolved ambiguity blocks review quality.
- Allowed use: clarify with humans.
- Downstream work allowed: no.
- Human confirmation required: yes for closure decisions.

### REVIEW
- Meaning: prepared for product review.
- Allowed use: evaluate readiness and quality.
- Downstream work allowed: no.
- Human confirmation required: yes for approval outcome.

### APPROVED
- Meaning: product intent accepted at product level.
- Allowed use: product agreement checkpoint.
- Downstream work allowed: limited preparation only, not execution planning.
- Human confirmation required: yes.

### EXECUTION_READY
- Meaning: operational checks for downstream planning readiness are satisfied.
- Allowed use: controlled downstream planning input.
- Downstream work allowed: yes, execution planning can proceed under existing gates.
- Human confirmation required: yes.

### ARCHIVED
- Meaning: inactive historical specification.
- Allowed use: reference only.
- Downstream work allowed: no.
- Human confirmation required: yes.

No Product Spec in APPROVED state means no downstream task generation.

No Product Spec in EXECUTION_READY state means no execution planning.

## Transition Policy
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

This is a policy definition only.
Do not implement task suspension logic in this task.

## Open Questions Policy
Open Questions section is mandatory.
It may contain:
- unresolved questions
- explicit "none"
- explicit "resolved"

APPROVED Product Specs with unresolved Open Questions require explicit human acknowledgement.

EXECUTION_READY is blocked if unresolved Open Questions affect acceptance criteria, risks, dependencies, or implementation feasibility.

## Schema vs Validator Responsibility
product-spec.schema.json validates structure only.

Semantic completeness, contradiction detection, feasibility, realism, and quality review are outside schema responsibility.

| Layer | Responsibility |
|---|---|
| JSON Schema | fields, types, required sections, allowed lifecycle status values |
| Future validator | completeness, contradictions, weak criteria, Non-Goal conflicts |
| Future semantic review | realism, hidden assumptions, quality of reasoning |

M46.1.1 must not implement semantic validation.

## Authority Boundaries
Product Spec:
- is source-of-truth for product intent
- is not execution authority
- is not approval by itself
- is not deployment authorization
- does not bypass human gate
- does not override canonical rules
- does not override task state machine
- does not override runtime enforcement
- does not authorize commit, push, merge, deploy, or release

Forbidden:
- autonomous execution authorization
- implicit execution approval
- runtime permission escalation
- hidden planning authority
- direct task creation without readiness checks

## Frontmatter Compatibility
This document follows docs/FRONTMATTER-STANDARD.md minimum fields and uses lowercase frontmatter status.
No deviation is required for M46.1.1.

## Cross References
- Lifecycle policy: `docs/PRODUCT-SPEC-LIFECYCLE.md`
- Transition policy: `docs/PRODUCT-SPEC-TRANSITION-POLICY.md`
- Lineage policy: `docs/SPEC-TO-TASK-LINEAGE.md`
- Validation policy: `docs/PRODUCT-SPEC-VALIDATION.md`
- Readiness gate policy: `docs/PRODUCT-SPEC-READINESS-GATE.md`
- Requirement extraction rules: `docs/REQUIREMENT-EXTRACTION-RULES.md`
- Clarification policy: `docs/CLARIFICATION-QUESTION-POLICY.md`
- Product summary policy: `docs/PRODUCT-SUMMARY-POLICY.md`
- M46 evidence report: `reports/m46-product-spec-layer-evidence-report.md`
- M46 completion review: `reports/m46-completion-review.md`
