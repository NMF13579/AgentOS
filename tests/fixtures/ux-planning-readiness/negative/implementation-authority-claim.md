---
type: ux-planning-readiness-report
milestone: M48
status: draft
authority: readiness-review
decision: UX_PLANNING_READY_WITH_LIMITATIONS
created: YYYY-MM-DD
reviewed_by: <reviewer-name-or-role>
reviewed_at: YYYY-MM-DD
---

# UX Planning Readiness Report

## Source References
- Product Spec: <path-to-product-spec>
- UX Contract: <path-to-ux-contract>

## Validation Inputs
- UX_CONTRACT_VALIDATION_OK is required for UX Planning Readiness.
- Skipped validation is not passed validation.
- UX Contract validator PASS is not approval.
- UX Contract validator PASS does not authorize task generation.
- Failed validation is UX_GAP_BLOCKING.
- Blocked validation is UX_GAP_BLOCKING.
- Missing source Product Spec blocks UX Planning Readiness.
- Missing source UX Contract blocks UX Planning Readiness.
- Missing UX Contract validation result blocks UX Planning Readiness.

## Supporting Evidence
- Static HTML Preview is optional supporting evidence only.
- UX Visual Approval Snapshot is optional supporting evidence only.
- UX Contract remains the required UX structure source.
- HTML Preview is not source of truth.
- UX Visual Approval Snapshot is not implementation approval.
- If preview_required is false, preview_path must be NOT_APPLICABLE.
- If snapshot_required is false, snapshot_path must be NOT_APPLICABLE.
- NOT_APPLICABLE is the required sentinel when optional evidence is not used.

## Readiness Decision
- UX_PLANNING_READY
- UX_PLANNING_READY_WITH_LIMITATIONS
- UX_PLANNING_NOT_READY
- UX_PLANNING_BLOCKED
- UX_PLANNING_READY does not authorize task generation.
- UX_PLANNING_READY does not authorize implementation.
- UX_PLANNING_READY does not authorize execution.

## Criteria Review
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
- normal
- loading
- empty
- error
- blocked
- needs_clarification
- approval_required
- execution_not_authorized
- Happy-path-only UX is not planning-ready.
- Screens without traceability are not planning-ready.
- Flows without exit states are not planning-ready.
- Actions without owner are not planning-ready.
- Approval point without human owner is UX_GAP_BLOCKING.
- Risk point without user-visible risk communication is not planning-ready.
- source_sections must be plural.
- source_sections must be a list.
- source_section must not be used.
- Traceability is not approval.
- Traceability is not execution authorization.

## Blocking Gaps

## Major Gaps

## Minor Gaps
- UX_GAP_MINOR: minor wording ambiguity.

## Accepted Limitations
- UX_GAP_ACCEPTED_LIMITATION: legacy wording retained for compatibility.
- Accepted limitations are not approval.
- Accepted limitations do not authorize implementation.
- Accepted limitation owner is required.
- Accepted limitation downstream risk is required.
- carry_forward_required must be true for accepted limitations.
- Accepted limitations must not hide blocking gaps.
- Accepted limitations must be carried forward into future planning.

accepted_limitation:
  limitation: legacy wording retained for compatibility
  gap_class: UX_GAP_ACCEPTED_LIMITATION
  rationale: migration in progress
  downstream_risk: medium risk of interpretation drift
  owner: ux-governance-owner
  carry_forward_required: true

## Not Applicable Items
- UX_GAP_NOT_APPLICABLE
- NOT_APPLICABLE requires rationale.
- NOT_APPLICABLE must not be used to hide missing required evidence.
- NOT_APPLICABLE must not bypass authority boundaries.

not_applicable_item:
  criterion: visual snapshot
  rationale: not required in this report
  owner: ux-governance-owner

## Open Questions
- UX_GAP_MAJOR: clarify one edge-case handoff.

## Downstream Limits
- No task generation authorized.
- No implementation authorized.
- No execution planning authorized.
- No commit, push, merge, deploy, or release authorized.
- Future UX-to-task decomposition requires a separate authorized task contract.
- Future frontend implementation requires separate authorized task contracts.
- Missing downstream limits blocks UX Planning Readiness.

## Non-Authority Boundary
UX Planning Readiness Report is not task generation.
UX Planning Readiness Report is not implementation approval.
UX Planning Readiness Report does not authorize task generation.
UX Planning Readiness Report does not authorize implementation.
UX Planning Readiness Report does not authorize execution planning.
UX Planning Readiness Report does not authorize commit, push, merge, deploy, or release.
UX Planning Readiness Report may inform future planning only.
Future task generation requires a separate authorized task contract.
Future implementation requires separate authorized task contracts.

ux_planning_readiness:
  source_product_spec:
    spec_id: <spec-id>
    spec_version: <spec-version>
    product_spec_path: <path-to-product-spec>
  source_ux_contract:
    ux_contract_id: <ux-contract-id>
    ux_contract_version: <ux-contract-version-or-lifecycle-status>
    ux_contract_path: <path-to-ux-contract>
    validation_result: UX_CONTRACT_VALIDATION_OK
  source_preview:
    preview_required: false
    preview_path: NOT_APPLICABLE
  source_visual_snapshot:
    snapshot_required: false
    snapshot_path: NOT_APPLICABLE
    decision: NOT_APPLICABLE
  readiness_decision: UX_PLANNING_READY_WITH_LIMITATIONS
  criteria_review:
    source_readiness: pass
    validation_readiness: pass
    screen_coverage: pass
    state_coverage: pass
    flow_coverage: pass
    user_action_coverage: pass
    risk_and_approval_coverage: pass
    traceability_coverage: pass
    accessibility_coverage: limitations
    open_question_handling: limitations
    downstream_limits: pass
    non_authority_boundary: pass
  blocking_gaps:
  major_gaps:
  minor_gaps:
    - UX_GAP_MINOR: minor wording ambiguity.
  accepted_limitations:
    - UX_GAP_ACCEPTED_LIMITATION: legacy wording retained for compatibility.
  not_applicable_items:
    - UX_GAP_NOT_APPLICABLE: visual snapshot not required.
  open_questions:
    - UX_GAP_MAJOR: clarify one edge-case handoff.
  downstream_limits:
    - No task generation authorized.
    - No implementation authorized.
    - No execution planning authorized.
    - No commit, push, merge, deploy, or release authorized.
    - Future UX-to-task decomposition requires a separate authorized task contract.
    - Future frontend implementation requires separate authorized task contracts.
  reviewed_by: <reviewer-name-or-role>
  reviewed_at: YYYY-MM-DD

UX Planning Readiness Report authorizes implementation
