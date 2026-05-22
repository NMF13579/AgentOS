---
type: ux-planning-readiness-criteria
milestone: M48
status: canonical
authority: criteria
version: 1.0.0
created: 2026-05-21
owner: human
---

# UX Planning Readiness Criteria

## Purpose
UX Planning Readiness Criteria define whether a validated UX Contract is structurally ready to inform future planning.
Readiness criteria do not generate tasks.
Readiness criteria do not approve implementation.
Readiness criteria do not authorize execution.

## Role in M48
These criteria provide the decision framework for M48 readiness review before any future decomposition work.

## Relationship to UX Planning Readiness Architecture
This document operationalizes the architecture boundaries from `docs/UX-PLANNING-READINESS-ARCHITECTURE.md` and keeps the same non-authority limits.

## Relationship to UX Contract
UX Contract remains the required UX structure source.
Criteria evaluate whether its structure is ready for future planning use.

## Relationship to UX Contract Validation
Criteria require a valid UX Contract validation result before readiness can be granted.

## Relationship to Static HTML Preview
Static HTML Preview is optional supporting evidence only.

## Relationship to UX Visual Approval Snapshot
UX Visual Approval Snapshot is optional supporting evidence only.

## Criteria Model
Criteria are evaluated before future UX-to-task decomposition.
Criteria are not task contracts.
Criteria are not implementation plans.

Review categories:
- source_readiness
- validation_readiness
- screen_coverage
- state_coverage
- flow_coverage
- user_action_coverage
- risk_and_approval_coverage
- traceability_coverage
- accessibility_coverage
- open_question_handling
- downstream_limits
- non_authority_boundary

## Required Inputs
Required inputs:
- source_product_spec
- source_ux_contract
- ux_contract_validation_result
- m47_evidence_report
- m47_completion_review
- m48_architecture

Optional supporting inputs:
- optional_static_html_preview
- optional_ux_visual_approval_snapshot
- m47_lesson

Input rules:
- Static HTML Preview is optional supporting evidence only.
- UX Visual Approval Snapshot is optional supporting evidence only.
- UX Contract remains the required UX structure source.

## Source Readiness Criteria
Source readiness requires:
- Product Spec reference exists.
- Product Spec version exists.
- UX Contract reference exists.
- UX Contract version or lifecycle status exists.
- UX Contract path exists.
- UX Contract source traceability exists.
- M47 completion review exists.
- M47 evidence report exists.

Required statements:
- Missing source Product Spec blocks UX Planning Readiness.
- Missing source UX Contract blocks UX Planning Readiness.
- Missing UX Contract traceability blocks UX Planning Readiness.

## UX Contract Validation Criteria
Validation readiness requires:
- UX Contract validator exists.
- UX Contract validation result exists.
- UX Contract validation result is UX_CONTRACT_VALIDATION_OK.
- Failed UX Contract validation blocks readiness.
- Blocked UX Contract validation blocks readiness.
- Skipped UX Contract validation must not be treated as pass.

Required statements:
- UX_CONTRACT_VALIDATION_OK is required for UX Planning Readiness.
- Skipped validation is not passed validation.
- UX Contract validator PASS is not approval.
- UX Contract validator PASS does not authorize task generation.

## Screen Coverage Criteria
Screen coverage requires:
- screens are listed;
- each screen has purpose;
- each screen has states;
- each screen has UX elements;
- each screen has user actions or explicit no-action rationale;
- each screen has traceability;
- each screen has non-authority boundary where relevant.

Required statement:
- Screens without traceability are not planning-ready.

## State Coverage Criteria
State coverage requires these states or explicit NOT_APPLICABLE rationale:
- normal
- loading
- empty
- error
- blocked
- needs_clarification
- approval_required
- execution_not_authorized

Required statements:
- Happy-path-only UX is not planning-ready.
- Missing blocked state may block UX Planning Readiness.
- Missing execution_not_authorized state may block UX Planning Readiness.

## Flow Coverage Criteria
Flow coverage requires:
- actor;
- entry point;
- ordered steps;
- decision points;
- risk points;
- approval points;
- blocked states;
- exit states;
- next step;
- what is not authorized.

Required statements:
- Flows without exit states are not planning-ready.
- Flows that imply execution without approval boundary are not planning-ready.

## User Action Criteria
User action coverage requires:
- action label;
- action purpose;
- actor;
- owner;
- preconditions;
- result state;
- risk level where relevant;
- approval requirement where relevant;
- blocked condition where relevant;
- explicit statement of what action does not authorize.

Required statements:
- Actions without owner are not planning-ready.
- Approval actions without human owner are not planning-ready.

## Risk and Approval Criteria
Risk and approval readiness requires:
- risk points are identified;
- risk banners are present where risk is user-facing;
- approval points are identified;
- approval_card is present where human approval is required;
- approval owner is defined;
- approval consequences are visible;
- decline path exists where approval exists;
- approval does not imply execution unless separate authorized task contract exists.

Required statements:
- Risk point without user-visible risk communication is not planning-ready.
- Approval point without human owner is not planning-ready.
- Approval card does not authorize execution.

## Traceability Criteria
Traceability readiness requires:
- spec_id
- spec_version
- product_spec_path
- ux_contract_id
- ux_contract_path
- source_sections

Coverage requirements:
- every screen must preserve traceability;
- every flow must preserve traceability;
- every UX element must preserve traceability;
- every risk point must preserve traceability;
- every approval point must preserve traceability;
- source_sections must be plural;
- source_sections must be a list;
- source_section must not be used.

Required statements:
- source_sections must be plural.
- source_sections must be a list.
- source_section must not be used.
- Traceability is not approval.
- Traceability is not execution authorization.

## Accessibility Criteria
Accessibility readiness requires:
- accessibility notes exist;
- keyboard-relevant interactions are identified where applicable;
- disabled controls in preview are identified as preview-only;
- error and blocked states have user-readable explanation;
- approval and risk states are not hidden;
- visual-only cues are not the only communication method.

Required statement:
- Missing accessibility notes may make UX Planning Readiness incomplete.

## Open UX Questions Criteria
Open questions must be classified as:
- blocking
- major
- minor
- accepted_limitation
- not_applicable

Rules:
- blocking open questions prevent UX_PLANNING_READY;
- unresolved major questions prevent clean readiness;
- minor questions may be carried forward;
- accepted limitations require rationale;
- accepted limitations require downstream risk;
- accepted limitations require owner.

Required statements:
- Blocking open UX questions block UX Planning Readiness.
- Accepted limitations must include rationale, downstream risk, and owner.

## Downstream Limits Criteria
Required downstream limits:
- No task generation authorized.
- No implementation authorized.
- No execution planning authorized.
- No commit, push, merge, deploy, or release authorized.
- Future UX-to-task decomposition requires a separate authorized task contract.
- Future frontend implementation requires separate authorized task contracts.

Required statement:
- Missing downstream limits blocks UX Planning Readiness.

## Non-Authority Criteria
Readiness criteria require absence of claims that readiness authorizes:
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
- UX Planning Readiness does not authorize task generation.
- UX Planning Readiness does not authorize implementation.
- UX Planning Readiness does not authorize execution.
- UX_PLANNING_READY does not authorize task generation.
- UX_PLANNING_READY does not authorize implementation.
- UX_PLANNING_READY does not authorize execution.

## Readiness Decision Criteria
Decision values:
- UX_PLANNING_READY
- UX_PLANNING_READY_WITH_LIMITATIONS
- UX_PLANNING_NOT_READY
- UX_PLANNING_BLOCKED

Decision requirements:

UX_PLANNING_READY
Allowed only when:
- all required sources exist;
- UX Contract validation passed;
- no blocking gaps exist;
- no unresolved major gaps exist;
- required states are covered or have explicit NOT_APPLICABLE rationale;
- risk and approval points are covered;
- traceability exists;
- downstream limits exist;
- no authority violations exist.

UX_PLANNING_READY_WITH_LIMITATIONS
Allowed when:
- required sources exist;
- UX Contract validation passed;
- no blocking gaps exist;
- limitations are explicit;
- limitations have rationale;
- limitations have owner;
- limitations have downstream risk;
- limitations are carried forward.

UX_PLANNING_NOT_READY
Required when:
- required sources exist;
- review can run;
- one or more blocking readiness gaps exist;
- major gaps prevent safe future planning;
- readiness evidence is insufficient but not blocked by missing sources.

UX_PLANNING_BLOCKED
Required when:
- source Product Spec is missing;
- source UX Contract is missing;
- UX Contract validation result is missing;
- UX Contract validation is blocked;
- M47 evidence or completion review is missing;
- readiness review cannot be performed.

Required statement:
- UX_PLANNING_READY_WITH_LIMITATIONS must carry limitations forward.

## Blocking Conditions
Blocking conditions:
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
- Blocking conditions prevent UX_PLANNING_READY.
- Authority claims block UX Planning Readiness.

## Limitations Handling
Limitation record format:

accepted_limitation:
  limitation:
  rationale:
  downstream_risk:
  owner:
  carry_forward_required:

Rules:
- accepted limitations are not approval;
- accepted limitations do not authorize implementation;
- accepted limitations must be carried forward into future planning;
- accepted limitations must not hide blocking gaps.

Required statement:
- Accepted limitations must not hide blocking gaps.

## What Criteria Do Not Decide
Readiness criteria do not decide:
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
- UX Planning Readiness Criteria do not judge visual design quality.

## Non-Authority Boundary
UX Planning Readiness Criteria are not task generation.
UX Planning Readiness Criteria are not implementation approval.
UX Planning Readiness Criteria do not authorize task generation.
UX Planning Readiness Criteria do not authorize implementation.
UX Planning Readiness Criteria do not authorize execution planning.
UX Planning Readiness Criteria do not authorize commit, push, merge, deploy, or release.
UX Planning Readiness Criteria may inform future planning only.
Future task generation requires a separate authorized task contract.
Future implementation requires separate authorized task contracts.

## Future Validator Notes
- Future validator may check readiness report structure.
- Future validator may check decision values.
- Future validator may check required downstream limits.
- Future validator may check no forbidden authority claims exist.
- Future validator must not judge visual design quality.
- Future validator must not authorize task generation.
- Future validator must not authorize implementation.

Required statement:
- Future validator must not judge visual design quality.

## Summary
The criteria define when validated UX structure is planning-ready, while preserving strict boundaries: no task generation, no implementation approval, and no execution authorization.
