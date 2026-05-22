---
type: ux-planning-readiness-report
milestone: M48
status: draft
authority: readiness-review
decision: UX_PLANNING_BLOCKED
created: YYYY-MM-DD
reviewed_by: <reviewer-name-or-role>
reviewed_at: YYYY-MM-DD
---

# UX Planning Readiness Report

## Title
UX Planning Readiness Report for `<ux-contract-id>`

## Source References
- Product Spec: `<path-to-product-spec>`
- UX Contract: `<path-to-ux-contract>`
- M47 Evidence Report: `<path-to-m47-evidence-report>`
- M47 Completion Review: `<path-to-m47-completion-review>`
- M48 Architecture: `docs/UX-PLANNING-READINESS-ARCHITECTURE.md`
- M48 Criteria: `docs/UX-PLANNING-READINESS-CRITERIA.md`
- M48 Gap Policy: `docs/UX-GAP-CLASSIFICATION-POLICY.md`

## Validation Inputs
- UX Contract validation_result must be one of:
  `UX_CONTRACT_VALIDATION_OK|UX_CONTRACT_VALIDATION_FAILED|UX_CONTRACT_VALIDATION_BLOCKED`
- UX_CONTRACT_VALIDATION_OK is required for UX Planning Readiness.
- Missing source Product Spec blocks UX Planning Readiness.
- Missing source UX Contract blocks UX Planning Readiness.
- Missing UX Contract validation result blocks UX Planning Readiness.
- Skipped validation is not passed validation.
- UX Contract validator PASS is not approval.
- UX Contract validator PASS does not authorize task generation.
- Failed validation is UX_GAP_BLOCKING.
- Blocked validation is UX_GAP_BLOCKING.

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
Allowed values:
- UX_PLANNING_READY
- UX_PLANNING_READY_WITH_LIMITATIONS
- UX_PLANNING_NOT_READY
- UX_PLANNING_BLOCKED

Decision meaning:
- UX_PLANNING_READY means the UX Contract is structurally ready to inform future task planning.
- UX_PLANNING_READY_WITH_LIMITATIONS means the UX Contract may inform future planning, but limitations must be carried forward.
- UX_PLANNING_NOT_READY means the UX Contract has readiness gaps that must be resolved before future planning.
- UX_PLANNING_BLOCKED means readiness cannot be reviewed because required sources, validation results, or evidence are missing.

Required authority boundary:
- UX_PLANNING_READY does not authorize task generation.
- UX_PLANNING_READY does not authorize implementation.
- UX_PLANNING_READY does not authorize execution.

## Criteria Review
Required criteria fields:
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

State coverage terms to review:
- normal
- loading
- empty
- error
- blocked
- needs_clarification
- approval_required
- execution_not_authorized

Coverage boundary rules:
- Happy-path-only UX is not planning-ready.
- Screens without traceability are not planning-ready.
- Flows without exit states are not planning-ready.
- Actions without owner are not planning-ready.
- Approval point without human owner is UX_GAP_BLOCKING.
- Risk point without user-visible risk communication is not planning-ready.

Traceability rules:
- source_sections must be plural.
- source_sections must be a list.
- source_section must not be used.
- Traceability is not approval.
- Traceability is not execution authorization.

## Blocking Gaps
Use only gaps with class `UX_GAP_BLOCKING`.
Blocking gaps prevent UX_PLANNING_READY.

## Major Gaps
Use only gaps with class `UX_GAP_MAJOR`.
Major gaps prevent clean UX_PLANNING_READY.

## Minor Gaps
Use only gaps with class `UX_GAP_MINOR`.

## Accepted Limitations
Use only gaps with class `UX_GAP_ACCEPTED_LIMITATION`.
Accepted limitations must not hide blocking gaps.
Accepted limitations must be carried forward into future planning.
Accepted limitations are not approval.
Accepted limitations do not authorize implementation.
Accepted limitation owner is required.
Accepted limitation downstream risk is required.
carry_forward_required must be true for accepted limitations.

Accepted limitation record format:

accepted_limitation:
  limitation: <description>
  gap_class: UX_GAP_ACCEPTED_LIMITATION
  rationale: <why-this-is-accepted>
  downstream_risk: <risk-to-future-planning-or-implementation>
  owner: <owner>
  carry_forward_required: true

## Not Applicable Items
Use only items with class `UX_GAP_NOT_APPLICABLE` when justified.
NOT_APPLICABLE requires rationale.
NOT_APPLICABLE must not be used to hide missing required evidence.
NOT_APPLICABLE must not bypass authority boundaries.

not_applicable_item:
  criterion: <criterion-name>
  rationale: <why-not-applicable>
  owner: <owner>

## Open Questions
List unresolved questions and classify each as:
- UX_GAP_BLOCKING
- UX_GAP_MAJOR
- UX_GAP_MINOR
- UX_GAP_ACCEPTED_LIMITATION
- UX_GAP_NOT_APPLICABLE

## Downstream Limits
Required downstream limits:
- No task generation authorized.
- No implementation authorized.
- No execution planning authorized.
- No commit, push, merge, deploy, or release authorized.
- Future UX-to-task decomposition requires a separate authorized task contract.
- Future frontend implementation requires separate authorized task contracts.

Missing downstream limits blocks UX Planning Readiness.

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

## Review Notes
Use placeholders only. Do not use concrete example values.

## Summary
UX Planning Readiness Report does not judge visual design quality.

```yaml
ux_planning_readiness:
  source_product_spec:
    spec_id: <spec-id>
    spec_version: <spec-version>
    product_spec_path: <path-to-product-spec>
  source_ux_contract:
    ux_contract_id: <ux-contract-id>
    ux_contract_version: <ux-contract-version-or-lifecycle-status>
    ux_contract_path: <path-to-ux-contract>
    validation_result: <UX_CONTRACT_VALIDATION_OK|UX_CONTRACT_VALIDATION_FAILED|UX_CONTRACT_VALIDATION_BLOCKED>
  source_preview:
    preview_required: <true-or-false>
    preview_path: <path-to-preview-or-NOT_APPLICABLE>
  source_visual_snapshot:
    snapshot_required: <true-or-false>
    snapshot_path: <path-to-snapshot-or-NOT_APPLICABLE>
    decision: <UX_VISUAL_DIRECTION_APPROVED|UX_VISUAL_DIRECTION_NEEDS_CHANGES|UX_VISUAL_DIRECTION_REJECTED|UX_VISUAL_SNAPSHOT_BLOCKED|NOT_APPLICABLE>
  readiness_decision: <UX_PLANNING_READY|UX_PLANNING_READY_WITH_LIMITATIONS|UX_PLANNING_NOT_READY|UX_PLANNING_BLOCKED>
  criteria_review:
    source_readiness:
    validation_readiness:
    screen_coverage:
    state_coverage:
    flow_coverage:
    user_action_coverage:
    risk_and_approval_coverage:
    traceability_coverage:
    accessibility_coverage:
    open_question_handling:
    downstream_limits:
    non_authority_boundary:
  blocking_gaps:
    -
  major_gaps:
    -
  minor_gaps:
    -
  accepted_limitations:
    -
  not_applicable_items:
    -
  open_questions:
    -
  downstream_limits:
    -
  reviewed_by: <reviewer-name-or-role>
  reviewed_at: YYYY-MM-DD
```

Gap classes used in this template:
- UX_GAP_BLOCKING
- UX_GAP_MAJOR
- UX_GAP_MINOR
- UX_GAP_ACCEPTED_LIMITATION
- UX_GAP_NOT_APPLICABLE
