---
type: ux-visual-approval-snapshot-policy
status: canonical
authority: supporting-evidence
version: 1.0.0
created: 2026-05-21
owner: human
---

# UX Visual Approval Snapshot

## Purpose
Определить каноническую политику фиксации человеческого review визуального направления UX.

## Role in M47
UX Visual Approval Snapshot фиксирует supporting evidence по визуальному направлению, не заменяя UX Contract.

## Relationship to UX Contract
- UX Visual Approval Snapshot may reference UX Contract.
- UX Visual Approval Snapshot does not replace UX Contract.

## Relationship to Static HTML Preview
- UX Visual Approval Snapshot may reference Static HTML Preview.
- Static HTML Preview остается опциональным и производным артефактом.

## Relationship to Human Approval
Snapshot фиксирует только review визуального направления человеком и не является real approval execution.

## Snapshot Definition
- UX Visual Approval Snapshot records visual direction review.
- UX Visual Approval Snapshot is supporting evidence only.
- UX Visual Approval Snapshot may reference Static HTML Preview.
- UX Visual Approval Snapshot may reference UX Contract.
- UX Visual Approval Snapshot does not replace UX Contract.
- UX Visual Approval Snapshot does not approve production UI.
- UX Visual Approval Snapshot does not authorize implementation.
- UX Visual Approval Snapshot does not authorize task generation.
- UX Visual Approval Snapshot does not authorize execution.

## Snapshot Decision Values
- UX_VISUAL_DIRECTION_APPROVED
- UX_VISUAL_DIRECTION_NEEDS_CHANGES
- UX_VISUAL_DIRECTION_REJECTED
- UX_VISUAL_SNAPSHOT_BLOCKED

Decision semantics:
- UX_VISUAL_DIRECTION_APPROVED means a human accepted visual direction only.
- UX_VISUAL_DIRECTION_NEEDS_CHANGES means visual direction needs revision.
- UX_VISUAL_DIRECTION_REJECTED means visual direction should not be used as supporting evidence.
- UX_VISUAL_SNAPSHOT_BLOCKED means snapshot cannot be completed because required sources, reviewer information, timestamp, scope, downstream limits, or non-authority boundary are missing.

## Snapshot Record Format
```yaml
ux_visual_decision:
  source_product_spec:
    spec_id:
    spec_version:
    product_spec_path:
  source_ux_contract:
    ux_contract_id:
    ux_contract_path:
  source_preview:
    preview_required:
    preview_path:
  source_sections:
    -
  decision:
  approved_by:
  reviewed_at:
  approved_scope:
  not_approved:
  open_questions:
  downstream_limits:
```

## Review Timestamp Requirements
- reviewed_at is required for every UX Visual Approval Snapshot.
- reviewed_at records when the visual direction review was made.
- reviewed_at must use YYYY-MM-DD format.
- Snapshot freshness depends on reviewed_at, spec_version, and referenced UX Contract version.
- A snapshot without reviewed_at must be blocked.
- reviewed_at is not approval authority.
- reviewed_at does not make stale UX artifacts current.

reviewed_at must use YYYY-MM-DD format.

## Preview Optionality Rules
- Static HTML Preview is optional in M47.
- source_preview must exist as a record container.
- source_preview.preview_required must be either true or false.
- If preview_required is true, source_preview.preview_path must be present and must point to the referenced preview artifact.
- If preview_required is false, source_preview.preview_path must be NOT_APPLICABLE.
- If preview_required is false and preview_path is missing, empty, null, or not NOT_APPLICABLE, the snapshot must be blocked.
- NOT_APPLICABLE is the required sentinel value for snapshots that do not reference Static HTML Preview.
- Snapshot must not be created from raw HTML Preview alone.
- UX Contract remains required even when preview is referenced.
- Future pages must not be generated from raw HTML Preview alone.

NOT_APPLICABLE is the required preview_path value when preview_required is false.

Preview used example:
```yaml
source_preview:
  preview_required: true
  preview_path: examples/ux-preview/agent-action-review-preview.html
```

No preview example:
```yaml
source_preview:
  preview_required: false
  preview_path: NOT_APPLICABLE
```

## Source Sections Format
- source_sections must use stable dot-path references.
- source_sections must use this format:
<source_type>.<section_key>
- Allowed source_type values:
spec
ux_contract
preview
- Allowed examples:
spec.requirements.risk_visibility
spec.requirements.human_approval_boundary
ux_contract.screens.agent_action_review
ux_contract.flows.agent_action_review_flow
preview.sections.approval_card

Rules:
- source_sections must be plural.
- source_sections must be a list.
- source_sections must not use free-form prose.
- source_sections must not use source_section.
- source_sections must not be empty.
- source_sections must identify Product Spec, UX Contract, or preview sections that justify the reviewed visual direction.

## What Can Be Reviewed
UX Visual Approval Snapshot may cover only:
- screen structure
- order of blocks
- visibility of risk banner
- presence of approval card
- visibility of Non-Authority Boundary
- clarity of states
- clarity of next action

## What Cannot Be Approved
UX Visual Approval Snapshot must not approve:
- production HTML
- CSS implementation
- React components
- Vue components
- Svelte components
- backend behavior
- real approval execution
- task generation
- execution planning
- commit
- push
- merge
- deploy
- release

## Approved Scope and Not Approved Rules
- approved_scope must contain at least one reviewed visual-direction item.
- not_approved must contain at least one explicit excluded scope item.
- not_approved must include task generation, execution planning, implementation, commit, push, merge, deploy, and release.
- approved_scope must not include implementation, task generation, execution planning, commit, push, merge, deploy, or release.
- If approved_scope is empty, snapshot must be blocked.
- If not_approved is empty, snapshot must be blocked.
- If excluded implementation/execution scopes are missing from not_approved, snapshot must be blocked.

## Downstream Effect
UX_VISUAL_DIRECTION_APPROVED means a human has reviewed and accepted the visual direction.
This does not change UX Contract lifecycle status.
This does not mark UX Contract as implementation-ready.
This does not unlock task generation.
This does not authorize execution planning.
This does not authorize implementation, commit, push, merge, deploy, or release.
Downstream systems may reference the UX Visual Approval Snapshot as supporting evidence only.

## Source Requirements
- Snapshot must reference a Product Spec source.
- Snapshot must reference a UX Contract source.
- Snapshot may reference Static HTML Preview.
- Snapshot must not be created from raw HTML Preview alone.
- Future pages must not be generated from raw HTML Preview alone.
- Approved UX Snapshot may support future page generation only as supporting evidence.
- Future page generation requires separate authorized task contracts.

Approved UX Snapshot may support future page generation.
Approved UX Snapshot does not authorize implementation.
Future pages must not be generated from raw HTML Preview alone.

## Traceability Requirements
Every UX Visual Approval Snapshot must preserve traceability to:
- spec_id
- spec_version
- product_spec_path
- ux_contract_id
- ux_contract_path
- preview_required
- preview_path
- source_sections
- reviewed_at

- Traceability is not approval.
- Traceability is not execution authorization.
- Snapshot traceability must not make stale UX artifacts current.
- If UX Contract changes, related UX Visual Approval Snapshot may become stale.
- If Static HTML Preview changes, related UX Visual Approval Snapshot may become stale.
- If Product Spec changes, related UX Visual Approval Snapshot may become stale.
- source_sections must identify the Product Spec, UX Contract, or preview sections that justify the reviewed visual direction.
- source_sections must be plural.
- source_sections must be a list.

## Open Questions
Open questions remain evidence items only and must not be silently converted into implementation assumptions.

## Snapshot Blocking Rules
Snapshot must be blocked if:
- source Product Spec is missing;
- source UX Contract is missing;
- source_preview record container is missing;
- source preview is missing when preview_required: true;
- preview_path is missing when preview_required: false;
- preview_path is empty when preview_required: false;
- preview_path is null when preview_required: false;
- preview_path is not NOT_APPLICABLE when preview_required: false;
- source sections are missing;
- decision value is invalid;
- approved_by is missing;
- reviewed_at is missing;
- reviewed_at does not use YYYY-MM-DD;
- approved_scope is empty;
- not_approved is missing;
- not_approved does not include downstream excluded scopes;
- downstream limits are missing;
- non-authority boundary is missing.

Missing reviewer identity blocks UX Visual Approval Snapshot.
Missing reviewed_at blocks UX Visual Approval Snapshot.
Missing downstream limits blocks UX Visual Approval Snapshot.
Missing non-authority boundary blocks UX Visual Approval Snapshot.
Missing source_sections blocks UX Visual Approval Snapshot.

## Non-Authority Boundary
UX Visual Approval Snapshot approves visual direction only.
UX Visual Approval Snapshot is supporting evidence only.
UX Visual Approval Snapshot does not approve Product Spec.
UX Visual Approval Snapshot does not approve UX Contract lifecycle status.
UX Visual Approval Snapshot does not approve production HTML.
UX Visual Approval Snapshot does not approve implementation.
UX Visual Approval Snapshot does not authorize task generation.
UX Visual Approval Snapshot does not authorize execution planning.
UX Visual Approval Snapshot does not authorize commit, push, merge, deploy, or release.
UX Visual Approval Snapshot must not be created from raw HTML Preview alone.

## Future Use Notes
- Future systems may reference UX Visual Approval Snapshot as supporting evidence only.
- Future systems must not treat UX Visual Approval Snapshot as approval for implementation.
- Future systems must not generate pages from raw HTML Preview alone.
- Future page generation requires separate authorized task contracts.
- M47.11 must verify cross-file consistency of the UX Visual Approval Snapshot non-authority boundary across policy, template, and example.

## Summary
Политика фиксирует безопасный формат UX Visual Approval Snapshot как supporting evidence, без полномочий на реализацию, генерацию задач и исполнение.
