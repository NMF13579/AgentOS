## Purpose
Task queue contract defines queue metadata.
Task queue contract does not approve work.
Task queue contract does not authorize execution.

## Position in M44
M44 формирует контракты и очередность, но не запускает выполнение.

## Relationship to Task Contract v2
Queue entry ссылается на task contract как источник данных.

## Relationship to Dependency Map
Task queue contract does not override dependency map.

## Relationship to Task Queue
Queue placement does not authorize execution.

## Relationship to HumanApprovalGate
HumanApprovalGate remains separate.

## Queue Status Enum
- candidate
- blocked
- ready_for_review
- queued
- rejected

ready_for_review is not approval.
queued is not execution authorization.

## Queue Reason Enum
- created_from_candidate_task
- dependency_satisfied
- blocked_by_dependency
- blocked_by_approval
- blocked_by_owner_review
- blocked_by_context
- blocked_by_ui_contract
- blocked_by_lint
- invalid_contract
- rejected_by_owner
- manual_queue_hold

## Gate Status Fields
- dependency_status: satisfied | blocked | invalid | not_checked
- lint_status: pass | warning | fail | not_run
- context_status: present | missing | stale | not_required | not_checked
- ui_contract_status: present | missing | not_required | not_checked
- approval_status: approved | required_missing | not_required | not_checked
- owner_review_status: approved | required_missing | not_required | not_checked

## Queue Entry Fields
- queue_entry_version
- queue_entry_id
- task_id
- source_task_contract
- source_dependency_map
- queue_status
- queue_reason
- dependency_status
- lint_status
- context_status
- ui_contract_status
- approval_status
- owner_review_status
- depends_on
- blocked_by
- priority
- risk_level
- human_approval_required
- owner_review_required
- created_at
- non_approval_warning

Queue entry must not include execution-authority fields.

## Queue Entry ID Rules
queue_entry_id format is queue_<normalized_task_id>.

Нормализация:
- lowercase
- non-alphanumeric -> underscore
- trim edge underscores
- collapse repeated underscores
- пустой результат => invalid

Strict queue_entry_id normalization validation is deferred to 44.9 linting.

## Timestamp Rules
created_at must use UTC ISO 8601 format with Z suffix.
Формат: YYYY-MM-DDTHH:MM:SSZ
Strict timestamp validation is deferred to 44.9 linting.

## Source Reference Boundary
source_task_contract placeholder does not prove the referenced task contract exists.
Future 44.9 linting must validate source_task_contract existence.
source_dependency_map может быть TODO в MVP.

## Status Consistency Rules
- queue_status: ready_for_review must not have non-empty blocked_by.
- queue_status: ready_for_review must not have dependency_status: blocked.
- queue_status: ready_for_review must not have lint_status: fail.
- queue_status: ready_for_review must not have lint_status: not_run.
- queue_status: ready_for_review must not have context_status: missing.
- queue_status: ready_for_review must not have context_status: stale.
- queue_status: ready_for_review must not have ui_contract_status: missing when UI Contract is required.
- queue_status: ready_for_review must not have approval_status: required_missing.
- queue_status: ready_for_review must not have owner_review_status: required_missing.
- queue_status: queued must not have dependency_status: blocked.
- queue_status: queued must not have lint_status: fail.
- queue_status: queued must not have context_status: missing.
- queue_status: queued must not have context_status: stale.
- queue_status: queued must not have ui_contract_status: missing when UI Contract is required.
- queue_status: queued must not have approval_status: required_missing.
- queue_status: queued must not have owner_review_status: required_missing.
- queue_status: queued still does not authorize execution.
- queue_status: blocked must include a blocking queue_reason.
- queue_status: rejected must include rejected_by_owner or manual_queue_hold.
- priority must not convert blocked into ready_for_review.
- priority must not convert blocked into queued.

Priority must not override queue blockers.
Dependency satisfaction must not override approval requirements.
Future 44.9 linting must validate queue status consistency.

## Forbidden Execution-Authority Fields
Запрещены в schema/template/positive fixtures:
- execution_approved
- execution_authorized
- ready_for_execution
- push_allowed
- merge_allowed
- deploy_allowed
- release_allowed
- approval_granted

## JSON Schema Contract
Схема описывает структуру и enum-поля, но не реализует полную cross-field проверку.

## Template Contract
Шаблон — это образец метаданных queue entry, не разрешение на выполнение.

## Fixture Semantics
Позитивные фикстуры: корректная структура и допустимые значения.
Негативные фикстуры: валидный JSON с намеренно плохой семантикой для будущего lint.

## Future 44.9 Linting Expectations
- проверка существования source_task_contract
- проверка существования source_dependency_map
- проверка consistency-правил queue_status/gates
- строгая проверка normalized queue_entry_id
- строгая проверка timestamp

## Non-Approval Boundary
Task queue contract does not override HumanApprovalGate.
Queue entry is not approval.
Queue entry does not authorize execution.
Queue entry does not authorize commit.
Queue entry does not authorize push.
Queue entry does not authorize merge.
Queue entry does not authorize deploy.
queue_status: queued still does not authorize execution.

## Known Gaps
- This task does not create real queue entries.
- This task does not write into tasks/queue/.
- This task does not implement task queue validation.
- This task does not implement queue state transitions.
- This task does not modify Task Contract v2 schema.
- This task does not fully validate cross-field consistency in JSON Schema.
- Cross-field consistency is deferred to 44.9 linting.
- Strict queue_entry_id normalization validation is deferred to 44.9 linting.
- Strict timestamp validation is deferred to 44.9 linting.
- source_task_contract existence validation is deferred to 44.9 linting.
- Negative fixtures intentionally contain invalid queue patterns for future linting.
