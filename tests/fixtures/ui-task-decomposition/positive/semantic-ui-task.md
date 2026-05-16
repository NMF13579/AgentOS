---
contract_version: 2
task_id: ux_appointment_form_task_contract
task_category: app_feature_ui
source_spec: TODO
source_ux: tests/fixtures/ux-to-task/positive/approved-ux-with-ui-contract.md
source_ui_contract: docs/UI-SEMANTIC-COMPONENT-CONTRACT.md
ui_contract_required: true
ui_contract_present: true
goal: Improve semantic UI behavior for appointment form
expected_result: Empty/loading/error/success states are clear and accessible
in_scope:
  - Define semantic empty/loading/error/success states
  - Add accessibility acceptance criteria for labels and keyboard flow
  - Add responsive behavior acceptance criteria
out_of_scope:
  - Expand token set without review
  - Replace design system authority
affected_paths:
  - TODO
forbidden_paths:
  - tasks/active-task.md
  - tasks/queue/
dependencies: []
blocked_by: []
priority: normal
risk_level: MEDIUM
risk_reason: UI contract artifacts are not fully present in repo
acceptance_criteria:
  - Semantic states are defined and testable
  - Accessibility labels and keyboard behavior are testable
  - Responsive behavior expectations are explicit
validation_plan:
  - TODO
  - UI Contract compliance placeholder
rollback_plan: TODO
human_approval_required: false
owner_review_required: false
context_required: true
created_at: 2026-05-16T13:30:00Z
---

## Non-Approval Warning
This UI Task Contract is not approval.
This UI Task Contract does not authorize execution.
This UI Task Contract does not authorize raw styling or direct UI library use.
This UI Task Contract does not authorize commit, push, merge, deploy, or release.
This UI Task Contract does not replace HumanApprovalGate.
Queue placement does not authorize execution.
