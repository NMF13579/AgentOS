---
type: ux-gap-classification-policy
milestone: M48
status: canonical
authority: classification-policy
version: 1.0.0
created: 2026-05-21
owner: human
---

# UX Gap Classification Policy

## Purpose
UX Gap Classification Policy defines how gaps discovered during UX Planning Readiness review are classified.
Gap classification does not generate tasks.
Gap classification does not approve implementation.
Gap classification does not authorize execution.

## Role in M48
This policy standardizes gap severity and handling during M48 readiness review so that readiness decisions are consistent and auditable.

## Relationship to UX Planning Readiness Architecture
This policy follows the architecture boundary that M48 is a readiness gate between validated UX structure and future UX-to-task decomposition.

## Relationship to UX Planning Readiness Criteria
This policy maps criteria failures to explicit gap classes and defines escalation and decision impact.

## Gap Classification Model
Every identified UX readiness gap must be assigned exactly one gap class.
Gap classification must not hide blocking issues.
Gap classification must not convert missing required evidence into approval.

## Gap Classes
- UX_GAP_BLOCKING
- UX_GAP_MAJOR
- UX_GAP_MINOR
- UX_GAP_ACCEPTED_LIMITATION
- UX_GAP_NOT_APPLICABLE

## UX_GAP_BLOCKING
UX_GAP_BLOCKING means the UX Contract or readiness evidence cannot safely inform future task planning until the gap is resolved.

Blocking gaps include:
- missing source Product Spec
- missing source UX Contract
- missing UX Contract validation result
- UX Contract validation failed
- UX Contract validation blocked
- missing traceability
- missing source_sections
- missing blocked state without NOT_APPLICABLE rationale
- missing execution_not_authorized state without NOT_APPLICABLE rationale
- approval point without human owner
- risk point without user-visible risk communication
- missing downstream limits
- readiness authority claim
- implementation authority claim
- task generation authority claim
- execution authority claim

Required statements:
- Blocking gaps prevent UX_PLANNING_READY.
- Blocking gaps must not be downgraded to accepted limitations.
- Authority claims are blocking gaps.

## UX_GAP_MAJOR
UX_GAP_MAJOR means the UX Contract may be reviewable, but the gap prevents clean readiness and must be resolved or explicitly carried forward.

Major gap examples:
- incomplete edge cases
- incomplete accessibility notes
- unclear next action
- incomplete state coverage
- unclear downstream limits
- major open UX question
- incomplete approval consequences
- incomplete decline path

Required statements:
- Major gaps prevent clean UX_PLANNING_READY.
- Major gaps may allow UX_PLANNING_READY_WITH_LIMITATIONS only when explicitly carried forward.

## UX_GAP_MINOR
UX_GAP_MINOR means the gap is non-blocking and does not prevent future planning if documented.

Minor gap examples:
- wording ambiguity
- minor explanatory note missing
- minor layout recommendation issue
- non-blocking open UX question
- minor naming inconsistency

Required statement:
- Minor gaps must be recorded and must not be silently ignored.

## UX_GAP_ACCEPTED_LIMITATION
UX_GAP_ACCEPTED_LIMITATION means a non-blocking limitation is consciously accepted and must be carried forward.

Accepted limitations require:
- limitation
- rationale
- downstream_risk
- owner
- carry_forward_required

Required statements:
- Accepted limitations are not approval.
- Accepted limitations do not authorize implementation.
- Accepted limitations must not hide blocking gaps.
- Accepted limitations must be carried forward into future planning.

## UX_GAP_NOT_APPLICABLE
UX_GAP_NOT_APPLICABLE means a normally required criterion does not apply and the rationale is explicitly documented.

NOT_APPLICABLE may be used for:
- state not applicable to a specific screen
- preview not used
- visual snapshot not required
- user action intentionally absent
- accessibility condition not relevant

Required statements:
- NOT_APPLICABLE requires rationale.
- NOT_APPLICABLE must not be used to hide missing required evidence.
- NOT_APPLICABLE must not bypass authority boundaries.

## Source Gaps
Classify the following as UX_GAP_BLOCKING:
- missing source Product Spec
- missing source UX Contract
- missing Product Spec version
- missing UX Contract path
- missing UX Contract traceability
- missing M47 completion review
- missing M47 evidence report

Required statement:
- Missing required source evidence is UX_GAP_BLOCKING.

## Validation Gaps
Classify the following as UX_GAP_BLOCKING:
- missing UX Contract validation result
- UX_CONTRACT_VALIDATION_FAILED
- UX_CONTRACT_VALIDATION_BLOCKED
- skipped validation treated as pass
- validator unavailable

Required statements:
- Skipped validation is not passed validation.
- Failed validation is UX_GAP_BLOCKING.
- Blocked validation is UX_GAP_BLOCKING.

## Coverage Gaps
Coverage gaps are evaluated for:
- screens
- states
- flows
- user actions
- risk points
- approval points
- edge cases
- accessibility notes
- open UX questions

Required statements:
- Happy-path-only UX is UX_GAP_BLOCKING or UX_GAP_MAJOR depending on missing coverage.
- Missing blocked state without NOT_APPLICABLE rationale is UX_GAP_BLOCKING.
- Missing execution_not_authorized state without NOT_APPLICABLE rationale is UX_GAP_BLOCKING.

## Risk and Approval Gaps
Classify the following as UX_GAP_BLOCKING:
- risk point without user-visible risk communication
- approval point without approval_card
- approval point without human owner
- approval path without decline path
- approval action that implies execution
- visual approval treated as implementation approval

Required statements:
- Approval point without human owner is UX_GAP_BLOCKING.
- Visual approval treated as implementation approval is UX_GAP_BLOCKING.
- Approval card does not authorize execution.

## Traceability Gaps
Classify the following as UX_GAP_BLOCKING:
- missing spec_id
- missing spec_version
- missing product_spec_path
- missing ux_contract_id
- missing ux_contract_path
- missing source_sections
- source_section used instead of source_sections

Required statements:
- Missing source_sections is UX_GAP_BLOCKING.
- source_section must not be used.
- Traceability gaps must not be treated as approval gaps.
- Traceability is not approval.
- Traceability is not execution authorization.

## Accessibility Gaps
Accessibility gaps are classified as UX_GAP_MAJOR or UX_GAP_BLOCKING depending on severity.

Examples:
- missing accessibility notes
- risk state hidden visually
- approval state hidden visually
- blocked state lacks user-readable explanation
- error state lacks user-readable explanation
- visual-only cue is the only communication method

Required statements:
- Missing accessibility notes may be UX_GAP_MAJOR.
- Hidden approval or risk state may be UX_GAP_BLOCKING.

## Open Question Gaps
Classify open questions as:
- blocking
- major
- minor
- accepted_limitation
- not_applicable

Rules:
- Blocking open UX questions are UX_GAP_BLOCKING.
- Major open UX questions prevent clean UX_PLANNING_READY.
- Minor open UX questions may be carried forward.
- Accepted open UX limitations require rationale, downstream risk, and owner.

## Authority Gaps
Authority gaps are always UX_GAP_BLOCKING.

Authority gaps include claims that readiness, criteria, validation, preview, snapshot, or evidence authorize:
- task generation
- task contract creation
- implementation planning
- frontend implementation
- backend implementation
- execution planning
- commit
- push
- merge
- deploy
- release

Required statements:
- Authority claims are UX_GAP_BLOCKING.
- UX Planning Readiness does not authorize task generation.
- UX Planning Readiness does not authorize implementation.
- UX Planning Readiness does not authorize execution.
- UX_PLANNING_READY does not authorize task generation.
- UX_PLANNING_READY does not authorize implementation.
- UX_PLANNING_READY does not authorize execution.

## Downstream Limit Gaps
Missing downstream limits are UX_GAP_BLOCKING.

Required downstream limits:
- No task generation authorized.
- No implementation authorized.
- No execution planning authorized.
- No commit, push, merge, deploy, or release authorized.
- Future UX-to-task decomposition requires a separate authorized task contract.
- Future frontend implementation requires separate authorized task contracts.

Required statement:
- Missing downstream limits is UX_GAP_BLOCKING.

## Accepted Limitation Record
Record format:

accepted_limitation:
  limitation:
  gap_class: UX_GAP_ACCEPTED_LIMITATION
  rationale:
  downstream_risk:
  owner:
  carry_forward_required:

Rules:
- carry_forward_required must be true for accepted limitations.
- Accepted limitation owner is required.
- Accepted limitation downstream risk is required.

## Escalation Rules
Escalation rules:
- minor gap becomes major if repeated across multiple screens;
- major gap becomes blocking if it affects approval, risk, traceability, or execution boundary;
- accepted limitation becomes blocking if it hides missing required evidence;
- any authority claim escalates to blocking;
- any missing source or validation evidence escalates to blocking.

Required statements:
- Any authority claim escalates to UX_GAP_BLOCKING.
- Any missing required source evidence escalates to UX_GAP_BLOCKING.
- Accepted limitation that hides a blocking gap escalates to UX_GAP_BLOCKING.

## Decision Impact
Gap class impact on readiness decisions:
- UX_GAP_BLOCKING -> UX_PLANNING_NOT_READY or UX_PLANNING_BLOCKED
- UX_GAP_MAJOR -> UX_PLANNING_READY_WITH_LIMITATIONS or UX_PLANNING_NOT_READY
- UX_GAP_MINOR -> may allow UX_PLANNING_READY_WITH_LIMITATIONS
- UX_GAP_ACCEPTED_LIMITATION -> may allow UX_PLANNING_READY_WITH_LIMITATIONS
- UX_GAP_NOT_APPLICABLE -> does not block if rationale exists

Required statements:
- UX_GAP_BLOCKING prevents UX_PLANNING_READY.
- UX_GAP_MAJOR prevents clean UX_PLANNING_READY.
- UX_GAP_ACCEPTED_LIMITATION must be carried forward.

## What Gap Classification Does Not Decide
Gap classification does not decide:
- visual design quality
- production UI quality
- frontend framework choice
- component architecture
- backend behavior
- task generation permission
- implementation permission
- execution permission
- deployment readiness

Required statement:
- UX Gap Classification Policy does not judge visual design quality.

## Non-Authority Boundary
UX Gap Classification Policy is not task generation.
UX Gap Classification Policy is not implementation approval.
UX Gap Classification Policy does not authorize task generation.
UX Gap Classification Policy does not authorize implementation.
UX Gap Classification Policy does not authorize execution planning.
UX Gap Classification Policy does not authorize commit, push, merge, deploy, or release.
UX Gap Classification Policy may inform future planning only.
Future task generation requires a separate authorized task contract.
Future implementation requires separate authorized task contracts.

## Future Validator Notes
- Future validator may check gap classes.
- Future validator may check accepted limitation fields.
- Future validator may check no blocking gap is marked accepted limitation.
- Future validator may check downstream limits.
- Future validator may check no forbidden authority claims exist.
- Future validator must not judge visual design quality.
- Future validator must not authorize task generation.
- Future validator must not authorize implementation.

Required statement:
- Future validator must not judge visual design quality.

## Summary
This policy ensures that UX readiness gaps are classified consistently, blocking risks are not hidden, authority boundaries are preserved, and readiness decisions remain non-authorizing inputs for future planning only.
