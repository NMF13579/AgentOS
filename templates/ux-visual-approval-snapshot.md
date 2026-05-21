---
type: ux-visual-approval-snapshot
status: draft
authority: supporting-evidence
decision: UX_VISUAL_SNAPSHOT_BLOCKED
spec_id: SPEC-...
ux_contract_id: UX-...
source_preview: <path-to-preview-or-NOT_APPLICABLE>
created: YYYY-MM-DD
reviewed_at: YYYY-MM-DD
approved_by: <reviewer-name-or-role>
---

# Title

## Source References

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
    preview_required: <true-or-false>
    preview_path: <path-to-preview-or-NOT_APPLICABLE>
  source_sections:
    -
  decision:
  approved_by: <reviewer-name-or-role>
  reviewed_at: YYYY-MM-DD
  approved_scope:
  not_approved:
  open_questions:
  downstream_limits:
```

## Visual Decision
Allowed values:
- UX_VISUAL_DIRECTION_APPROVED
- UX_VISUAL_DIRECTION_NEEDS_CHANGES
- UX_VISUAL_DIRECTION_REJECTED
- UX_VISUAL_SNAPSHOT_BLOCKED

## Approved Scope
- screen structure
- order of blocks
- visibility of risk banner
- presence of approval card
- visibility of Non-Authority Boundary
- clarity of states
- clarity of next action

## Not Approved
- production HTML
- CSS implementation
- React components
- Vue components
- Svelte components
- backend behavior
- real approval execution
- task generation
- execution planning
- implementation
- commit
- push
- merge
- deploy
- release

## Open Questions
- 

## Downstream Limits
UX_VISUAL_DIRECTION_APPROVED means a human has reviewed and accepted the visual direction.
This does not change UX Contract lifecycle status.
This does not mark UX Contract as implementation-ready.
This does not unlock task generation.
This does not authorize execution planning.
This does not authorize implementation, commit, push, merge, deploy, or release.
Downstream systems may reference the UX Visual Approval Snapshot as supporting evidence only.

## Traceability
- source_sections must be plural and must be a list.
- source_sections must use dot-path references such as `spec.requirements.risk_visibility`.

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

## Review Notes
- 
