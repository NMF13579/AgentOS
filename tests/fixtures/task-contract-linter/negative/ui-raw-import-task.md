---
contract_version: 2
task_id: ui-raw-import
task_category: app_feature_ui
source_spec: docs/spec.md
source_ux: docs/ux.md
source_ui_contract: docs/UI-CONTRACT.md
ui_contract_required: true
ui_contract_present: true
goal: detect raw import
expected_result: fail
in_scope:
  - ui update
out_of_scope: []
affected_paths:
  - src/ui/file.ts
forbidden_paths: []
dependencies: []
blocked_by: []
priority: normal
risk_level: MEDIUM
risk_reason: ui rule
acceptance_criteria: []
validation_plan: []
rollback_plan: defined
human_approval_required: false
owner_review_required: false
context_required: true
created_at: 2026-05-17T09:05:00Z
---

Body contains forbidden import: components/ui/button
