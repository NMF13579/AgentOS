---
type: canonical
module: product-spec
status: draft
authority: supporting
created: 2026-05-21
last_validated: unknown
---

# Semantic Spec Review

Semantic Spec Review helps agents and reviewers inspect Product Spec meaning, consistency, and downstream ambiguity.

Semantic Spec Review is not a deterministic checker.
Semantic Spec Review does not guarantee detection of every contradiction.
Semantic Spec Review is not validation.
Semantic Spec Review is not readiness.
Semantic Spec Review is not approval.
Semantic Spec Review does not authorize execution.

Semantic review is not approval.
Semantic review does not authorize task generation.
Semantic review does not authorize execution planning.
Semantic review does not authorize execution, commit, push, merge, deploy, or release.
Semantic review does not create approval records.
Semantic review does not replace validation, readiness gates, human gate requirements, task state rules, or runtime enforcement.

## Purpose
The purpose is to review whether a structurally valid Product Spec is clear enough for downstream UX/decomposition work without guesswork.

## When To Review
Use semantic review after structural validation and before downstream UX/decomposition work.
Use it again when major Product Spec changes appear.

## Source Artifacts
Semantic review may use:
- Product Spec
- Product Spec lifecycle status
- validation result
- readiness result
- clarification questions
- plain-language summary
- lineage metadata
- source interview record, if available

Semantic review must not invent missing Product Spec content.

If source information is missing, the review must record it as missing.

Unknown is better than invented.
Missing is better than guessed.

## Review Categories

### Problem / Solution Separation
What to check:
- whether the Product Spec clearly separates the underlying problem from a proposed implementation.

Examples of problems:
- solution appears before user/problem statement;
- tool choice is stated without outcome definition.

What to do:
- add clarification question;
- mark as NEEDS_CLARIFICATION when ambiguity is material.

The reviewer must check whether the Product Spec clearly separates the underlying problem from a proposed implementation.

A proposed solution must not be treated as proof that the problem is understood.

| Weak spec pattern | Issue | Review response |
|---|---|---|
| “Build a dashboard button” | Solution stated, problem unclear | Ask what user problem the button solves |
| “Use AI to automate this” | Technology choice stated before outcome | Ask what outcome must improve |
| “Make it faster” | Goal vague | Ask what action or workflow is too slow |

### User / Actor Clarity
What to check:
- primary user exists;
- secondary actors exist when relevant;
- human roles are not confused with system/agent roles.

Examples of problems:
- no explicit approval owner;
- unclear distinction between human approval and agent suggestion.

What to do:
- request clarification and owner confirmation.

If the Product Spec affects human approval, risk review, or agent behavior, the human decision owner must be explicit.

### Jobs-To-Be-Done Clarity
What to check:
- jobs are understandable and outcome-oriented.

Examples of problems:
- jobs describe implementation steps instead of user outcomes.

What to do:
- rewrite jobs as user outcomes and add Open Questions if unclear.

### Goals / Success Metrics Alignment
What to check:
- every major Goal has at least one measurable or reviewable signal;
- metrics are measurable when possible;
- metrics do not silently add scope.

Examples of problems:
- vague goals without signal;
- metric contradicts stated goal.

What to do:
- add metric candidate or Open Question.

A vague Goal is not automatically invalid, but it must produce either a measurable Success Metric candidate or an Open Question.

### Acceptance Criteria Quality
What to check:
- criteria are observable and reviewable;
- criteria are tied to Goals;
- criteria are not hidden implementation tasks.

Examples of problems:
- “works well”, “looks good”, “is user-friendly”, “uses AI”, “is fast”, “is secure” without observable detail.

What to do:
- request concrete, observable detail.

Acceptance Criteria must not authorize execution.
Acceptance Criteria must not define commits, pushes, merges, deployment, or runtime permissions.

### Non-Goals Consistency
What to check:
- Non-Goals are explicit and enforceable;
- no requirement/acceptance criterion reintroduces excluded scope.

Examples of problems:
- Non-Goal says “no UX changes” but criteria require new user flow.

What to do:
- mark as NEEDS_CLARIFICATION or NEEDS_HUMAN_REVIEW.

If Product Spec requirements conflict with Non-Goals, the review must mark the issue as NEEDS_CLARIFICATION or NEEDS_HUMAN_REVIEW.

### Constraints Clarity
What to check:
- constraints are concrete enough for downstream interpretation.

Examples of problems:
- “must be compliant” without identifying relevant boundary.

What to do:
- add clarification question and dependency note.

### Risks Clarity
What to check:
- risks are concrete and tied to impact.

Examples of problems:
- “risk is low” with no reason;
- unclear risk ownership.

What to do:
- elevate to MAJOR and request human review when needed.

### Dependencies Clarity
What to check:
- dependencies are explicit and actionable for review.

Examples of problems:
- dependency exists but owner or prerequisite is missing.

What to do:
- add dependency clarification question.

### Open Questions Impact
What to check:
- unresolved questions that affect acceptance criteria, risks, dependencies, or readiness.

Examples of problems:
- unresolved approval-owner question in high-risk flow.

What to do:
- mark blocking when downstream work would require guessing.

### Hidden Assumptions
What to check:
- assumptions about users, permissions, data, integrations, compliance, timing, effort, feasibility, user understanding, agent autonomy, approval authority.

Examples of problems:
- assumes data exists without source;
- assumes approval can be fully automatic.

What to do:
- surface assumption as finding and link to impacted section.

Hidden assumptions that affect Goals, Risks, Acceptance Criteria, Dependencies, or readiness must be surfaced as review findings.

### Internal Contradictions
What to check:
- conflicting statements within the same Product Spec.

Examples of problems:
- anonymous user experience + personalized recommendations;
- no data storage + history-dependent behavior;
- human approval required + fully automatic approval;
- no UX changes + new user-facing workflow;
- no task generation + generated task contracts expected;
- low-risk classification + destructive action capability.

What to do:
- mark as MAJOR or BLOCKING based on impact.

Semantic review can flag likely contradictions, but it does not guarantee complete contradiction detection.

### Downstream Ambiguity
What to check:
- unresolved ambiguity that would force UX/decomposition guessing.

Examples of problems:
- unclear actor, flow, acceptance criteria, risk, Non-Goal, dependency, Open Question, or lifecycle/readiness mismatch.

What to do:
- recommend clarification before M47/decomposition.

If downstream UX or task decomposition would require guessing, semantic review must recommend clarification before M47 or decomposition work proceeds.

### Scope Expansion Risk
What to check:
- whether proposed outcomes silently expand scope.

Examples of problems:
- new criteria introduce unrelated feature area.

What to do:
- classify as MAJOR and request human scope decision.

## Review Outcomes
Allowed outcomes:
- SEMANTIC_REVIEW_READY_FOR_UX
- SEMANTIC_REVIEW_NEEDS_CLARIFICATION
- SEMANTIC_REVIEW_NEEDS_HUMAN_REVIEW
- SEMANTIC_REVIEW_BLOCKED

Definitions:
- SEMANTIC_REVIEW_READY_FOR_UX: no blocking semantic ambiguity was found; Product Spec may proceed toward M47 UX structure review if readiness conditions are otherwise met.
- SEMANTIC_REVIEW_NEEDS_CLARIFICATION: unclear or missing information should be resolved before downstream UX/decomposition.
- SEMANTIC_REVIEW_NEEDS_HUMAN_REVIEW: issue requires human product/ownership decision.
- SEMANTIC_REVIEW_BLOCKED: review cannot be completed because source artifacts are missing, unreadable, contradictory at foundation level, or insufficient for safe review.

Examples of SEMANTIC_REVIEW_BLOCKED:
- source Product Spec is missing or unreadable
- validation result is PRODUCT_SPEC_VALIDATION_BLOCKED
- Product Spec contains mutually exclusive lifecycle statuses
- required source artifacts are unavailable and reviewer cannot safely assess meaning
- Product Spec is so structurally inconsistent that semantic review would require guessing

SEMANTIC_REVIEW_READY_FOR_UX is not approval.
SEMANTIC_REVIEW_READY_FOR_UX is not validation PASS.
SEMANTIC_REVIEW_READY_FOR_UX is not readiness READY.
SEMANTIC_REVIEW_READY_FOR_UX does not authorize execution.

## Finding Severity
semantic_finding_severity:
  BLOCKING:
    meaning: "Must be resolved before UX/decomposition proceeds"
  MAJOR:
    meaning: "Should be resolved or explicitly accepted by human review"
  MINOR:
    meaning: "Does not block downstream work but should be recorded"
  INFO:
    meaning: "Contextual observation only"

| Highest finding severity | Typical outcome |
|---|---|
| BLOCKING | SEMANTIC_REVIEW_NEEDS_CLARIFICATION or SEMANTIC_REVIEW_BLOCKED |
| MAJOR | SEMANTIC_REVIEW_NEEDS_HUMAN_REVIEW |
| MINOR | SEMANTIC_REVIEW_READY_FOR_UX with notes |
| INFO | SEMANTIC_REVIEW_READY_FOR_UX with notes |

If multiple findings exist, reviewers should consider the highest finding severity first.
However, semantic review outcome is reviewer judgment, not deterministic computation.
The severity-to-outcome table provides default guidance, not an automatic rule.
Reviewer must explain any deviation from the typical outcome mapping.

## Relationship To Validation And Readiness
Validation checks deterministic structure.
Readiness checks target-specific downstream eligibility.
Semantic review checks meaning, ambiguity, and likely contradictions.

Semantic review does not replace validation or readiness.
Semantic review must not downgrade validation failures into semantic notes.
Semantic review must not upgrade readiness failures into downstream permission.

If validation failed, semantic review may be blocked or limited.
If readiness failed, semantic review may still provide useful findings, but must not claim the Product Spec can proceed.

## Relationship To Clarification Policy
Semantic review findings may produce clarification questions.
Clarification questions should use CLARIFICATION-QUESTION-POLICY.md and templates/clarification-question.md.
Semantic review must not mark clarification questions resolved unless source artifacts explicitly show resolution.

## Relationship To M47 UX
Semantic review prepares Product Specs for M47 UX structure work.
It does not create UX layouts, wireframes, visual hierarchy, components, or prototypes.
If UX work would require guessing, semantic review should recommend clarification.

## Relationship To M48 Feasibility
Semantic review may identify feasibility concerns as review findings.
It must not estimate effort, cost, timeline, or implementation complexity.
Feasibility risk review belongs to 46.5.3 and M48.

