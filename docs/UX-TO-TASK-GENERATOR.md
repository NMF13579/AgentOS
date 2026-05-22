## Purpose
Документ описывает MVP-генератор UX-to-Task: он создаёт кандидат Task Contract v2 из UX-файла.

## Position in M44
Это шаг M44.5: подготовка кандидатов задач из UX без запуска выполнения.

## Relationship to Decomposition Input Contract
Генератор использует правила готовности входов из `docs/DECOMPOSITION-INPUT-CONTRACT.md`.

## Relationship to Task Contract v2
Выход генератора соответствует полям из `docs/TASK-CONTRACT-V2.md`.

## Relationship to M43.5 UI Contract
Для UX-работ нужен UI Contract dependency (зависимость от UI-контракта) в метаданных UX.

## Supported MVP UX Format
Поддерживаются поля frontmatter:
- `status`
- `ux_id`
- `title`
- `risk_level`
- `priority`
- `ui_contract_required`
- `ui_contract_present`
- `ui_contract_reference`

Поддерживаются секции:
- `UX Goal`
- `Screens`
- `User Flows`
- `State and Error Matrix`
- `UX Acceptance Criteria`
- `Accessibility Notes`
- `Responsive Behavior`
- `UX Copy`
- `UI Contract References`
- `Out of Scope`
- `Known Risks`

## Approval Detection
Only APPROVED UX input may generate candidate UX Task Contracts.

## UI Contract Detection
UX tasks requiring UI work must reference UI Contract dependency.

## UI Contract Reference Boundary
The generator trusts ui_contract_present from UX frontmatter in this MVP.
The generator does not verify that ui_contract_reference exists on disk in this MVP.
ui_contract_present: true does not prove the referenced UI Contract artifact exists.

## Mandatory Validation Order
Validation order is mandatory: approval check → UI Contract check → structure check.
First failing check determines the result token.

## Deterministic ID and Filename Rules
generated_task_id format is ux_<normalized_ux_id>_task_contract.
Write mode creates <generated_task_id>.md inside --out.

## Queue Path Boundary Rules
The generator must use resolved path common-path checks for tasks/queue boundaries.
String prefix checks are forbidden for queue boundary validation.

## Extraction Rules
- `goal` из `UX Goal` или `title`.
- `expected_result` из первой строки `UX Acceptance Criteria`.
- `in_scope` из `Screens`, `User Flows`, `State and Error Matrix`, `Accessibility Notes`, `Responsive Behavior`, `UX Copy`.
- `out_of_scope` из `Out of Scope` или `TODO`.
- `risk_reason` из `Known Risks` или дефолт.

## Timestamp Format
created_at must use UTC ISO 8601 format with Z suffix.
Use datetime.now(timezone.utc), not datetime.utcnow().

## Generated UX Task Contract Fields
Генератор заполняет поля Task Contract v2, включая:
- `task_id` = `generated_task_id`
- `source_spec` = `TODO`
- `source_ux` = путь к UX-файлу
- `source_ui_contract` = `ui_contract_reference`
- `forbidden_paths` включает `tasks/active-task.md`, `tasks/queue/`, `components/ui/*`, `@radix-ui/*`

## UI Contract Boundary
Сгенерированный контракт обязан фиксировать границы UI:
- только semantic intent (смысл UX), без прямых указаний “как красить интерфейс”
- без прямых импортов `components/ui/*` и `@radix-ui/*`
- отсутствие UI Contract блокирует готовность UI-задачи

## CLI Usage
```bash
python3 scripts/generate-tasks-from-ux.py --help
python3 scripts/generate-tasks-from-ux.py --ux <path> --dry-run
python3 scripts/generate-tasks-from-ux.py --ux <path> --out <directory> --dry-run
python3 scripts/generate-tasks-from-ux.py --ux <path> --out <directory> --write
python3 scripts/generate-tasks-from-ux.py --ux <path> --json
```

## Dry-Run Behavior
Dry-run is the default behavior.
Dry-run Markdown output must include Result: UX_TO_TASK_DRY_RUN_OK.

## Write Behavior
Write mode must be explicit.
--out is always a directory.
The generator must create --out directory if it does not exist.
If --out exists and is a file, return UX_TO_TASK_FAILED.

## Queue Write Boundary
The real task queue must not be modified by this task.
The generator must refuse --out paths inside tasks/queue/.

## JSON Output
--json without --write behaves as dry-run JSON mode.
--json without --write must not create files.
JSON включает `validation_order`, `failed_check`, `generated_task_id`, `ui_contract_reference_checked_on_disk: false`.

## Result Tokens
- UX_TO_TASK_DRY_RUN_OK
- UX_TO_TASK_WRITE_OK
- UX_TO_TASK_BLOCKED_UX_NOT_APPROVED
- UX_TO_TASK_BLOCKED_MISSING_UI_CONTRACT
- UX_TO_TASK_BLOCKED_INVALID_UX
- UX_TO_TASK_NEEDS_REVIEW
- UX_TO_TASK_FAILED

## Exit Semantics
- `UX_TO_TASK_DRY_RUN_OK` => exit 0
- `UX_TO_TASK_WRITE_OK` => exit 0
- `UX_TO_TASK_BLOCKED_UX_NOT_APPROVED` => exit 1
- `UX_TO_TASK_BLOCKED_MISSING_UI_CONTRACT` => exit 1
- `UX_TO_TASK_BLOCKED_INVALID_UX` => exit 1
- `UX_TO_TASK_NEEDS_REVIEW` => exit 1
- `UX_TO_TASK_FAILED` => exit 1

## Non-Approval Boundary
Generated UX Task Contracts are not approval.
Generated UX Task Contracts do not authorize execution.
Generated UX Task Contracts do not authorize raw styling or direct UI library use.
Generated UX task contract does not authorize commit.
Generated UX task contract does not authorize push.
Generated UX task contract does not authorize merge.
Generated UX task contract does not authorize deploy.
Generated UX Task Contracts do not replace HumanApprovalGate.
Queue placement, if performed later, does not authorize execution.
TODO source/path fields do not authorize execution.

## Known Gaps
- MVP supports one candidate task per UX artifact.
- MVP does not perform full multi-screen decomposition.
- MVP does not perform full state-by-state decomposition.
- MVP does not validate against JSON Schema using external dependencies.
- MVP does not define Spec-to-task generation.
- MVP does not define Context Pack selection.
- MVP does not write into real tasks/queue/.
- MVP trusts ui_contract_present from UX frontmatter and does not verify that ui_contract_reference exists on disk.
- Referenced UI Contract file existence must be validated later by task linting / UI task decomposition checks.
- source_spec: TODO and affected_paths: TODO may later be treated as TASK_LINT_WARNING or TASK_LINT_NEEDS_REVIEW by 44.9.
- TODO source/path fields do not authorize execution.
- UX_TO_TASK_NEEDS_REVIEW is reserved for future ambiguous UX cases.
- KNOWN_GAP: `docs/UI-SEMANTIC-COMPONENT-CONTRACT.md` is missing.
- KNOWN_GAP: `docs/DESIGN-TOKENS-POLICY.md` is missing.
- KNOWN_GAP: `docs/UI-REPLACEABILITY-POLICY.md` is missing.
