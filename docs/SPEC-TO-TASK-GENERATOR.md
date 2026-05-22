## Purpose
Документ описывает MVP-генератор, который делает кандидат Task Contract v2 из Spec-файла.

## Position in M44
Это шаг M44.4: подготовка кандидата задачи, без выполнения самой задачи.

## Relationship to Decomposition Input Contract
Генератор опирается на готовность входов из `docs/DECOMPOSITION-INPUT-CONTRACT.md`.

## Relationship to Task Contract v2
Генератор выпускает контент в формате `docs/TASK-CONTRACT-V2.md`.

## Supported MVP Spec Format
Поддерживается простой Markdown формат:
- фронтматтер (поля в начале файла): `status`, `spec_id`, `title`, `risk_level`, `priority`
- секции: `Goal`, `Functional Requirements`, `Non-Functional Requirements`, `Acceptance Criteria`, `Constraints`, `Validation Plan`, `Out of Scope`, `Known Risks`

## Approval Detection
Only APPROVED Spec input may generate candidate Task Contracts.
Если `status` не равен `APPROVED`, генератор блокирует выпуск кандидата.

## Extraction Rules
- `goal` берётся из секции `Goal`, иначе из `title`.
- `expected_result` берётся из первой строки `Functional Requirements`.
- `in_scope` берётся из `Functional Requirements`.
- `out_of_scope` берётся из `Out of Scope`, иначе `TODO`.
- `acceptance_criteria` берётся из `Acceptance Criteria`.
- `validation_plan` берётся из `Validation Plan`, иначе `TODO`.
- `risk_reason` берётся из `Known Risks`, иначе стандартный текст.
- `source_ux` и `source_ui_contract` в MVP ставятся как `TODO`.

## Timestamp Format
created_at must use UTC ISO 8601 format with Z suffix.
Use datetime.now(timezone.utc), not datetime.utcnow().

## Generated Task Contract Fields
Генератор заполняет обязательные поля Task Contract v2:
- `contract_version`
- `task_id`
- `source_spec`
- `source_ux`
- `source_ui_contract`
- `goal`
- `expected_result`
- `in_scope`
- `out_of_scope`
- `affected_paths`
- `forbidden_paths`
- `dependencies`
- `blocked_by`
- `priority`
- `risk_level`
- `risk_reason`
- `acceptance_criteria`
- `validation_plan`
- `rollback_plan`
- `human_approval_required`
- `owner_review_required`
- `context_required`
- `created_at`

## CLI Usage
```bash
python3 scripts/generate-tasks-from-spec.py --help
python3 scripts/generate-tasks-from-spec.py --spec <path> --out <path> --dry-run
python3 scripts/generate-tasks-from-spec.py --spec <path> --out <path> --write
python3 scripts/generate-tasks-from-spec.py --spec <path> --json
```

## Dry-Run Behavior
Dry-run is the default behavior.
Без `--write` генератор печатает кандидат-контракт в stdout (вывод в терминал), файлы не создаёт.

## Write Behavior
Write mode must be explicit.
- `--write` обязателен для записи
- `--out` обязателен с `--write`
- без `--out` генератор возвращает `SPEC_TO_TASK_FAILED`
- существующий файл не перезаписывается

## Queue Write Boundary
The real task queue must not be modified by this task.
The generator must refuse --out paths inside tasks/queue/.

## JSON Output
Режим `--json` печатает корректный JSON и включает:
- `result`
- `spec_path`
- `would_write` или `written_path` (по ситуации)
- `generated_task_id` (когда возможно)
- `warnings`
- `non_approval_warning`

## Result Tokens
- SPEC_TO_TASK_DRY_RUN_OK
- SPEC_TO_TASK_WRITE_OK
- SPEC_TO_TASK_BLOCKED_SPEC_NOT_APPROVED
- SPEC_TO_TASK_BLOCKED_INVALID_SPEC
- SPEC_TO_TASK_NEEDS_REVIEW
- SPEC_TO_TASK_FAILED

## Exit Semantics
- `SPEC_TO_TASK_DRY_RUN_OK` => exit 0
- `SPEC_TO_TASK_WRITE_OK` => exit 0
- `SPEC_TO_TASK_BLOCKED_SPEC_NOT_APPROVED` => exit 1
- `SPEC_TO_TASK_BLOCKED_INVALID_SPEC` => exit 1
- `SPEC_TO_TASK_NEEDS_REVIEW` => exit 1
- `SPEC_TO_TASK_FAILED` => exit 1

## Non-Approval Boundary
Generated Task Contracts are not approval.
Generated Task Contracts do not authorize execution.
Generated task contract does not authorize commit.
Generated task contract does not authorize push.
Generated task contract does not authorize merge.
Generated task contract does not authorize deploy.
Generated Task Contracts do not replace HumanApprovalGate.
Queue placement, if performed later, does not authorize execution.
TODO source fields do not authorize execution.

## Known Gaps
- MVP supports one candidate task per Spec.
- MVP does not perform full multi-task decomposition.
- MVP does not validate against JSON Schema using external dependencies.
- MVP does not define UX-to-task generation.
- MVP does not define Context Pack selection.
- MVP does not write into real tasks/queue/.
- source_ux: TODO and source_ui_contract: TODO may later be treated as TASK_LINT_WARNING or TASK_LINT_NEEDS_REVIEW by 44.9.
- TODO source fields do not authorize execution.
- KNOWN_GAP: `docs/UI-SEMANTIC-COMPONENT-CONTRACT.md` is missing.
- KNOWN_GAP: `docs/DESIGN-TOKENS-POLICY.md` is missing.
- KNOWN_GAP: `docs/UI-REPLACEABILITY-POLICY.md` is missing.
