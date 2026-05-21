---
type: canonical
module: product-spec
status: draft
authority: supporting
created: 2026-05-21
last_validated: unknown
---

# Product Summary Policy

Plain-language Product Summary helps users understand Product Spec intent, scope, risks, and readiness.

Plain-language Product Summary is not approval.
Plain-language Product Summary is not validation.
Plain-language Product Summary is not readiness.
Plain-language Product Summary is not execution authorization.
Plain-language Product Summary does not replace human gate requirements.

This document provides human-facing explanation.
It does not authorize execution, commit, push, merge, deploy, or release.
It does not create approval records.
It does not replace human gate requirements.
It does not override runtime enforcement.
It does not replace validation or readiness gates.

## Relationship To Human-Readable Summary Standard
HUMAN-READABLE-SUMMARY-STANDARD.md is the parent standard for concise human-readable summaries.

Product Summary is a Product Spec-specific specialization of the general Human-Readable Summary Standard.

This policy inherits non-authority boundaries, plain-language focus, and evidence-first behavior from HUMAN-READABLE-SUMMARY-STANDARD.md.

## Purpose
The summary translates Product Spec content into plain language for non-technical review.

It should help the user understand what they are being asked to review, not pressure them to approve.

The summary should answer:
- What are we building?
- Who is it for?
- Why does it matter?
- What is included?
- What is explicitly excluded?
- What risks or uncertainties exist?
- What questions remain?
- What does the current lifecycle status mean?
- What should a non-technical user do next?
- What downstream step may happen next?
- What does the summary not authorize?

Approval requires a separate human decision.
Summary does not create or imply approval.

## When To Use
Use the summary before review, approval, and downstream decisions to support human understanding.
Use it again when lifecycle status, risks, or open questions change.

## Source Artifacts
Summary may use:
- Product Spec
- Product Spec lifecycle status
- Product Spec validation result
- Product Spec readiness result
- clarification questions
- Product Spec lineage metadata

The summary must not invent missing Product Spec content.

If source information is missing, the summary must say it is missing.

Unknown is better than invented.
Missing is better than guessed.

## Required Sections
Required sections:
- Source Product Spec
- What Is Being Built
- Who It Is For
- Why It Matters
- What Is Included
- What Is Not Included
- Success Criteria In Plain Language
- Main Risks
- Open Questions
- Current Status
- What Can Happen Next
- What This Summary Does Not Authorize

Section intent:
- Source Product Spec: identifies spec path, spec_id, and spec_version.
- What Is Being Built: plain explanation of product change.
- Who It Is For: user and actor summary.
- Why It Matters: user/business pain and expected outcome.
- What Is Included: current in-scope content.
- What Is Not Included: explicit Non-Goals, clearly visible.
- Success Criteria In Plain Language: readable translation of metrics and acceptance criteria.
- Main Risks: risks, impact, and review need.
- Open Questions: unresolved/acknowledged/blocking/unknown state.
- Current Status: lifecycle, validation status, readiness status, and Suggested next action.
- What Can Happen Next: possible next step without authorization language.
- What This Summary Does Not Authorize: explicit non-authority boundary.

## Plain-Language Style Rules
Use short sentences.
Avoid jargon where possible.
Explain necessary terms.
Do not hide risk behind optimistic language.
Do not overstate certainty.
Do not convert unknowns into assumptions.
Do not use implementation details unless needed for user understanding.
Do not include raw technical logs unless summarized.
Do not pressure the user toward approval.

The summary should be clear, neutral, and decision-supporting.

The summary must not be persuasive marketing copy.

## Product Scope Summary
| Product Spec Concept | Plain-Language Summary |
|---|---|
| Goals | What outcome the product should create |
| Non-Goals | What is intentionally not included |
| Acceptance Criteria | What must be true for the result to count as acceptable |
| Constraints | What limits or rules the product must respect |
| Dependencies | What the product depends on |
| Risks | What could go wrong or require caution |

Non-Goals must be summarized clearly.

Non-Goals must not be hidden in a minor note.

## Lifecycle Status With Next Action
Every lifecycle status explanation must include a plain-language next action.

| lifecycle_status | Plain meaning | Suggested next action |
|---|---|---|
| DRAFT | The Product Spec is still being written | Continue drafting or answer missing questions |
| INTERVIEWING | More input is being collected | Provide more context or answer interview questions |
| NEEDS_CLARIFICATION | Important questions must be answered | Review blocking questions before approval |
| REVIEW | The Product Spec is ready for review | Read the summary and decide whether changes are needed |
| APPROVED | A human has approved product direction/scope | Product may proceed toward task-generation readiness checks |
| EXECUTION_READY | Required readiness conditions for downstream execution planning are met | Downstream planning may be considered, but task-level gates still apply |
| ARCHIVED | The Product Spec is no longer active | Do not use for new downstream work unless reopened through policy |

APPROVED does not mean execution is authorized.

EXECUTION_READY does not mean tasks may execute without task-level gates.

## Validation And Readiness Explanation
Validation means the Product Spec passed structural checks.

Readiness means the Product Spec may proceed to a specific downstream stage.

Neither validation nor readiness is approval.

If validation/readiness status is unknown, the summary must say:
- Validation status: unknown.
- Readiness status: unknown.

Summary must not infer validation PASS.

Summary must not infer readiness READY.

Summary must not convert APPROVED into EXECUTION_READY.

## Open Questions Summary
Open Questions must be shown clearly and labeled as:
- no open questions
- open questions exist but are acknowledged
- open questions block readiness
- open questions are unknown / not reviewed

Open Questions are not automatically a failure.

Open Questions become blocking when they affect Acceptance Criteria, Risks, Dependencies, lifecycle readiness, or downstream task generation.

Use existing markers when present:
- open_questions_acknowledged_by_human: true
- open_questions_block_execution_ready: true

## Risk Summary
Risk summary must include:
- what the risk is
- why it matters
- what decision or review may be needed
- whether risk affects downstream readiness

Risk summary is not a security audit.
Risk summary is not feasibility estimation.
Risk summary is not approval.

## Relationship To Clarification Policy
If a summary reveals missing information, the next step should be clarification, not silent approval.

The summary may refer to clarification questions, but must not mark them resolved unless source artifacts say they are resolved.

## Relationship To Human Understanding Check
Plain-Language Product Summary is an explanatory artifact.

Human Understanding Check is a later decision checkpoint.

Summary may support understanding, but it does not prove understanding.

This task does not implement a Human Understanding Check gate.
Future M46.5 work may use this summary as input.

## Relationship To Validation And Readiness Systems
Summary can report validation/readiness results only if they are provided by source artifacts or command outputs.

Summary must not infer validation PASS.
Summary must not infer readiness READY.
Summary must not convert APPROVED into EXECUTION_READY.
