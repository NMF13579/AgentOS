# Task Validation Package Contract

## 1. Purpose
Определить структуру task validation package для M63 как формальный вход в контрактную валидацию.

## 2. M63 Position in the Roadmap
M63 формализует контракт валидации задачи после M62 MVP.
M63 задаёт структуру пакета, но не закрывает production-проверку задачи.

## 3. Dependency on Contract Architecture
Зависимость: `docs/TASK-VALIDATION-CONTRACT-ARCHITECTURE.md`.
Наблюдаемый статус архитектуры: `FINAL_STATUS: M63_TASK_VALIDATION_CONTRACT_ARCHITECTURE_DEFINED`.

## 4. Package Contract Scope
63.2 определяет только package schema (структуру входа).
Контракт не определяет result schema и не определяет detailed decision mapping.

## 5. Required Package Fields
Обязательные поля:
- `contract_version`
- `package_type`
- `task_id`
- `task_brief_path`
- `declared_scope`
- `declared_forbidden_changes`
- `expected_artifacts`
- `changed_files`
- `diff_reference`
- `agent_evidence_ref`
- `validation_claims_ref`
- `human_review_required`

Ограничения:
- `package_type` = `task_validation_package`
- `human_review_required` = `true`
- `contract_version` в стабильном формате, например `m63.task_validation_package.v1`

## 6. Field Semantics
`contract_version` — стабильная версия контракта M63; не означает одобрение задачи.

`package_type` — идентификатор типа пакета: `task_validation_package`.

`task_id` — стабильный идентификатор задачи.

`task_brief_path` — путь к task brief внутри репозитория.

`declared_scope` — структура допустимой области изменения (например `allowed_paths`, `allowed_reports`, `allowed_docs`, `allowed_scripts`, `notes`).

`declared_forbidden_changes` — структура запретов (например `forbidden_paths`, `forbidden_claims`, `forbidden_operations`, `notes`).

`expected_artifacts` — декларативный список ожидаемых артефактов задачи.

`changed_files` — декларативный список изменённых файлов (repository-relative).

`diff_reference` — метаданные о diff-базе (например `HEAD~1`, `main...HEAD`, `manual_changed_files_input`).

`agent_evidence_ref` — ссылка на evidence.

`validation_claims_ref` — ссылка на claims валидации.

`human_review_required` — всегда `true`.

Иллюстративный пример (не approval):
```json
{
  "contract_version": "m63.task_validation_package.v1",
  "package_type": "task_validation_package",
  "task_id": "63.6",
  "task_brief_path": "tasks/active-task.md",
  "declared_scope": {
    "allowed_paths": [
      "scripts/check-task-validation-contract.py",
      "docs/TASK-VALIDATION-CONTRACT-VALIDATOR.md"
    ],
    "notes": []
  },
  "declared_forbidden_changes": {
    "forbidden_paths": [
      "schemas/agent-evidence.schema.json",
      "docs/ACCEPTANCE-CRITERIA-CHECKER.md"
    ],
    "forbidden_claims": [
      "approved",
      "human review not required",
      "merge authorized"
    ],
    "forbidden_operations": [
      "merge",
      "push",
      "release",
      "lifecycle mutation"
    ],
    "notes": []
  },
  "expected_artifacts": [
    "scripts/check-task-validation-contract.py",
    "docs/TASK-VALIDATION-CONTRACT-VALIDATOR.md"
  ],
  "changed_files": [
    "scripts/check-task-validation-contract.py",
    "docs/TASK-VALIDATION-CONTRACT-VALIDATOR.md"
  ],
  "diff_reference": "manual_changed_files_input",
  "agent_evidence_ref": {
    "path": "reports/task-evidence.json",
    "kind": "reference_only"
  },
  "validation_claims_ref": {
    "path": "reports/task-validation-output.json",
    "kind": "reference_only"
  },
  "human_review_required": true
}
```

## 7. Path Safety Rules
Все пути в task_validation_package должны быть repository-relative.
Absolute paths are forbidden.
Path traversal is forbidden.
Paths resolving outside repository root are forbidden.

В schema используются консервативные строковые ограничения для отсева очевидно опасных путей.
JSON Schema сама по себе не гарантирует полную path safety; runtime resolution относится к validator/runner.

## 8. Evidence Reference Boundary
agent_evidence_ref is a reference to evidence, not the full M64 evidence model.

M63 package schema does not define full evidence content.
M64 defines the full task output evidence model.

## 9. Validation Claims Reference Boundary
validation_claims_ref is a reference to claimed validation output.
M63 package schema does not prove validation commands were correctly run.
M65 and M66 may later strengthen validation command checking.

## 10. Relation to Task Validation Result Schema
63.2 defines the task validation package schema.
63.3 defines the task validation result schema.
63.2 must not define the result schema.
63.2 must not define detailed decision mapping.

## 11. Relation to M64-M67
M64 defines the full task output evidence model.
M65 defines the acceptance criteria checker.
M66 defines the unified agent task validation runner.
M67 defines false PASS resistance and completion gate integration.

M63 package schema must not absorb M64-M67 responsibilities.

## 12. What This Schema Validates
Схема валидирует:
- обязательные поля;
- базовые типы;
- `package_type` const;
- `human_review_required` const true;
- структуру массивов/объектов;
- базовые path string constraints.

## 13. What This Schema Does Not Validate
Схема не валидирует:
- полную корректность evidence content;
- выполнение acceptance criteria;
- фактическую корректность git diff;
- runtime file existence;
- approval/completion/release readiness.

## 14. Human Review Requirement
human_review_required: true

The task validation package must not disable human review.
A package that attempts to set human_review_required to false is outside the safe M63 contract boundary.
Human review remains required.

## 15. Non-Authority Boundary
M63 task validation package schema is not approval.
M63 task validation package schema does not replace human review.
M63 task validation package schema does not complete the task.
M63 task validation package schema does not validate completed agent tasks as a production gate.
M63 task validation package schema does not define the full task output evidence model.
M63 task validation package schema does not define acceptance criteria checking.
M63 task validation package schema does not authorize merge, push, or release.
M63 task validation package schema does not start M64.
Human review remains required.

## 16. Final Status
FINAL_STATUS: M63_TASK_VALIDATION_PACKAGE_SCHEMA_DEFINED
