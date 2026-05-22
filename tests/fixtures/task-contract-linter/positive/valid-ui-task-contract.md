---
contract_version: 2
task_id: valid-ui-task
task_category: app_feature_ui
source_spec: docs/spec.md
source_ux: docs/ux.md
source_ui_contract: docs/UI-CONTRACT.md
ui_contract_required: true
ui_contract_present: true
goal: Improve semantic states
expected_result: UI states clear
in_scope:
  - semantic loading/empty/error states
out_of_scope:
  - visual redesign
affected_paths:
  - src/ui/state-handler.ts
forbidden_paths:
  - tasks/active-task.md
dependencies: []
blocked_by: []
priority: normal
risk_level: MEDIUM
risk_reason: UI behavior adjustment
acceptance_criteria:
  - semantic states validated
validation_plan:
  - run lint
rollback_plan: define rollback steps
human_approval_required: false
owner_review_required: false
context_required: true
created_at: 2026-05-17T09:01:00Z
---

## UI Contract Boundary
Use semantic intent only.
