## Purpose
Read-only lint for Task Contract Markdown and Queue Entry JSON.

## Position in M44
M44 validates contracts but does not execute implementation work.

## Relationship to Task Contract v2
Проверяются обязательные поля и их типы/enum.

## Relationship to UI Task Rules
UI-задачи проверяются отдельными UI-правилами.

## Relationship to Dependency Map
Linter не заменяет dependency map.

## Relationship to Task Queue Contract
Queue lint проверяет форму и consistency правил очереди.

## Relationship to M45 Controlled Autopilot
Lint не запускает M45 и не даёт разрешение на выполнение.

## CLI Usage
- `--target <file>`
- `--kind task|queue|auto`
- `--json`

--kind auto must detect input kind only by file extension.

## Result Tokens
- TASK_LINT_PASS
- TASK_LINT_WARNING
- TASK_LINT_NEEDS_REVIEW
- TASK_LINT_FAIL
- TASK_LINT_FAILED

## Exit Semantics
Only TASK_LINT_PASS may return exit 0.
- TASK_LINT_PASS => 0
- TASK_LINT_WARNING => 1
- TASK_LINT_NEEDS_REVIEW => 1
- TASK_LINT_FAIL => 1
- TASK_LINT_FAILED => 2

TASK_LINT_WARNING is not PASS.
TASK_LINT_NEEDS_REVIEW is not PASS.
TASK_LINT_FAIL is not PASS.

## JSON Output
Ключи: result, target, kind, issues, issue_count, highest_severity, non_approval_warning.
Lint PASS is not approval and does not authorize execution.

## Minimal Frontmatter Parsing Contract
Both inline empty list syntax and block list syntax must be supported in the same Markdown frontmatter file.
- между первыми двумя `---`
- split scalar только по первому `:`
- без PyYAML

## Mandatory Lint Check Order
Задан строго для task и queue режимов.

## Task Contract Required Fields
Список полей берётся из 44.9 и сверяется с required из схемы v2.

## Schema Path Resolution Rules
The linter must resolve repository root from the script location and must not depend on the current working directory.

## Schema Alignment Rules
Schema alignment mismatch is intentionally blocking.
TASK_LINT_SCHEMA_MISMATCH_DETECTED must return TASK_LINT_FAILED.

## Task Contract Needs Review Rules
- TODO в source_spec/source_ux/source_ui_contract(UI)/affected_paths/validation_plan
- rollback_plan TODO для MEDIUM/HIGH/CRITICAL

## Forbidden Execution-Authority Fields
For Markdown task files, forbidden execution-authority fields are checked only as frontmatter keys.

## UI Task Detection Rules
For UI task detection, body means all Markdown content after the closing --- marker of the frontmatter block.
ui_contract_required is true and ui_contract_present is absent or false

## UI Task Lint Rules
Провалы: raw imports, direct library imports, hardcoded visual style, missing UI contract.

## Queue Entry Required Fields
Проверяются required поля очереди, их типы и enum.
source_dependency_map: TODO is allowed for queue entry MVP.

## Queue Entry ID Normalization Rules
Queue entry normalization is ASCII-only in this MVP.

## Queue Status Consistency Rules
Проверяется согласованность status/reason/gates/blocked_by.

## Queue Enum Values
Используются enum из task-queue-entry schema.

## Non-Approval Boundary
HumanApprovalGate remains separate from linting.
Lint PASS is not approval and does not authorize execution.

## Known Gaps
- no directory linting
- no auto-fix
- no report writing
- no writes into tasks/queue/
- no source_task_contract existence validation
- no source_ui_contract existence validation
- no source_dependency_map existence validation
- no body-level execution-authority prose detection
- no full YAML parsing
- no multi-line scalar support
- no complex YAML support
- no JSON Schema library use
- only required field alignment against task-contract-v2 schema
- no full Task Contract JSON Schema validation
- no WARNING fixture required
- no M45 execution behavior
