---
contract_version: 2
task_id: valid-task
source_spec: docs/spec.md
source_ux: docs/ux.md
source_ui_contract: TODO
goal: Deliver stable behavior
expected_result: Criteria pass
in_scope:
  - update parser
out_of_scope:
  - ui redesign
affected_paths:
  - src/parser.py
forbidden_paths:
  - tasks/active-task.md
dependencies: []
blocked_by: []
priority: normal
risk_level: LOW
risk_reason: low-risk change
acceptance_criteria:
  - parser handles mixed lists
validation_plan:
  - run lint
rollback_plan: TODO
human_approval_required: false
owner_review_required: false
context_required: true
created_at: 2026-05-17T09:00:00Z
---

Body text.
