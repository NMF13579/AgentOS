---
contract_version:
task_id:
task_category:
source_spec:
source_ux:
source_ui_contract:
ui_contract_required:
ui_contract_present:
goal:
expected_result:
in_scope:
out_of_scope:
affected_paths:
forbidden_paths:
dependencies:
blocked_by:
priority:
risk_level:
risk_reason:
acceptance_criteria:
validation_plan:
rollback_plan:
human_approval_required:
owner_review_required:
context_required:
created_at:
---

## Summary
Краткое описание UI-задачи.

## Source References
Укажите `source_spec`, `source_ux`, `source_ui_contract`.

## UI Task Category
Укажите категорию (`app_feature_ui`, `agentos_control_ui`, `ui_state_handling`, `ui_error_handling`, `ui_accessibility`, `ui_responsive_behavior`, `ui_copy`, `ui_contract_alignment`).

## UI Contract Boundary
UX prose describes user experience intent, not direct implementation authority.
Agent must describe semantic intent, not visual taste.
Missing UI Contract blocks UI task readiness.
New design tokens require review.
No silent token expansion.

## Semantic Intent
Опишите ожидаемое поведение интерфейса без указания конкретной библиотеки UI и без жёстких визуальных параметров.

## App Feature UI Boundary
Граница изменений UI функциональности приложения.

## AgentOS Control UI Boundary
Граница изменений управляющего UI AgentOS.

## State and Error Handling
Опишите empty/loading/error/success/disabled/blocked семантически.

## Accessibility Requirements
Требования доступности.

## Responsive Behavior Requirements
Требования адаптивности.

## UX Copy Requirements
Требования к текстам интерфейса.

## In Scope
Что входит в задачу.

## Out of Scope
Что не входит в задачу.

## Affected Paths
Какие пути могут меняться.

## Forbidden Paths
Какие пути менять нельзя.

## Acceptance Criteria
Проверяемые критерии.

## Validation Plan
План проверки, включая placeholder проверки соответствия UI Contract.

## Rollback Plan
План отката.

## Human Approval Boundary
Фиксируйте требования ручного одобрения для рискованных действий.

## Owner Review Boundary
Фиксируйте требования ревью владельцем.

## Non-Approval Warning
This UI Task Contract is not approval.
This UI Task Contract does not authorize execution.
This UI Task Contract does not authorize raw styling or direct UI library use.
This UI Task Contract does not authorize commit, push, merge, deploy, or release.
This UI Task Contract does not replace HumanApprovalGate.
Queue placement does not authorize execution.

## Known Gaps
task_category is UI-task-specific and is not currently defined in schemas/task-contract-v2.schema.json.
Schema extension or linter behavior for task_category is deferred to future task linting / schema alignment work.
source_ui_contract: TODO linting behavior is deferred to 44.9.
