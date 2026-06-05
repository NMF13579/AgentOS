# Task Validation Contract Architecture

## 1. Purpose
Определить архитектуру слоя M63 для формального контракта валидации задачи: границы, роли, ответственность и инварианты.

## 2. M63 Position in the Roadmap
M63 идёт после M62 MVP и формализует контрактный слой task validation.
M63 подготавливает основу для M64-M67, но не подменяет их.

## 3. Dependency on M62 Completion
Источник зависимости: `reports/m63-m62-completion-intake.md`.
Наблюдаемый intake-статус: `M63_INTAKE_READY_WITH_WARNINGS`.

Сценарии зависимости:
- `M62_TASK_ACCEPTANCE_MVP_COMPLETE` -> M63 может идти в обычном режиме после human review.
- `M62_TASK_ACCEPTANCE_MVP_COMPLETE_WITH_WARNINGS` -> M63 может идти с предупреждениями и переносом deferred work.
- `M62_TASK_ACCEPTANCE_MVP_BLOCKED` -> архитектура может быть описана, но downstream-задачи M63 не должны продолжаться.

## 4. Contract Layer Scope
M63 defines the task validation contract.
M63 formalizes the package/result relationship.
M63 defines schema responsibilities.
M63 defines contract-level decision semantics.
M63 defines the human review boundary as contract invariant.
M63 creates a contract validator for schema and boundary consistency.

M63 does not provide full production task acceptance.

## 5. Authority Model
M63 contract defines structure, consistency, and boundary rules.
M63 validator checks contract compliance.
M63 validation result is evidence for human review.
M63 validation result is not approval.
M63 validation result does not complete a task.
M63 validation result does not authorize merge, push, or release.

Явное разделение:
- contract compliance
- task completion approval
- production acceptance

## 6. Task Validation Package Concept
Будущий task validation package — структурированный входной пакет со ссылками на:
- task brief
- declared scope
- declared forbidden changes
- expected artifacts
- changed files
- diff reference
- agent evidence reference
- validation claims reference
- contract version
- human review requirement

Граница:
- 63.1 описывает только package concept.
- 63.2 определяет package schema.
- 63.1 не создаёт package schema.

agent_evidence_ref is a reference to evidence, not the full M64 evidence model.

## 7. Task Validation Result Concept
Будущий task validation result — структурированный выход с полями:
- result
- contract_version
- task_id
- package_valid
- schema_result
- scope_result
- evidence_ref_result
- validation_claims_result
- human_review_required
- warnings
- blockers
- non_authority_boundary

Допустимые категории результата:
- TASK_VALIDATION_PASS
- TASK_VALIDATION_PASS_WITH_WARNINGS
- TASK_VALIDATION_BLOCKED
- TASK_VALIDATION_NOT_ENOUGH_EVIDENCE

Граница:
- 63.1 может назвать категории для continuity с M62.
- 63.3 определяет result schema.
- 63.4 определяет detailed decision semantics.
- 63.1 не определяет полный result schema и детальную mapping-логику.

## 8. Schema Layer Role
M63 schema layer validates package/result structure.
M63 schema layer does not prove task correctness.
M63 schema layer does not verify full evidence sufficiency.
M63 schema layer does not evaluate full acceptance criteria.

Планируемые выходы schema layer:
- `schemas/task-validation-package.schema.json`
- `schemas/task-validation-result.schema.json`

В 63.1 эти файлы не создаются.

## 9. Validator Role
Будущий validator:
- read-only
- schema-focused
- contract-boundary-focused
- non-authority-boundary-aware
- human-review-boundary-aware
- not production task acceptance
- not completion gate
- not approval

Планируемый путь:
- `scripts/check-task-validation-contract.py`

В 63.1 validator не создаётся.

## 10. Decision Semantics Role
M63 decision semantics define contract-level mapping for malformed package, missing required fields, unsupported version, unknown result value, missing human review boundary, and non-authority violations.

M63 decision semantics do not evaluate full acceptance criteria.
M63 decision semantics do not validate full task output evidence content.
M63 decision semantics do not integrate completion gate.

## 11. Human Review Boundary
Граница ручного обзора — контрактный инвариант.

Обязательные утверждения:
- human_review_required must remain true.
- TASK_VALIDATION_PASS is not approval.
- TASK_VALIDATION_PASS does not complete the task.
- TASK_VALIDATION_PASS does not replace human review.
- TASK_VALIDATION_PASS does not authorize merge, push, or release.
- Human review remains required.

M63 делает эту границу явной в:
- `docs/TASK-VALIDATION-HUMAN-REVIEW-BOUNDARY.md`
- `schemas/task-validation-result.schema.json`
- `scripts/check-task-validation-contract.py`

Эти артефакты не создаются в 63.1.

## 12. Relation to M62 MVP
M62 proved a thin task acceptance MVP path.
M63 formalizes that path into a contract layer.
M63 reuses M62 result vocabulary where appropriate.
M63 does not replace M62 smoke evidence.
M63 does not convert M62 MVP runner into a production gate.

## 13. Relation to M64-M67
M64 defines the full task output evidence model.
M65 defines the acceptance criteria checker.
M66 defines the unified agent task validation runner.
M67 defines false PASS resistance and completion gate integration.

M63 must not absorb M64-M67 responsibilities.

## 14. What M63 Can Decide
M63 может решать:
- соответствует ли package схеме M63;
- соответствует ли result схеме M63;
- коррелируют ли `task_id` в package/result;
- используются ли разрешённые result values;
- сохраняется ли `human_review_required: true`;
- присутствует ли non-authority boundary;
- есть ли contract-level blockers;
- готовы ли contract outputs к M64 формализации evidence model.

## 15. What M63 Must Not Decide
M63 must not decide:
- final task approval
- production task acceptance
- full task output evidence sufficiency
- full acceptance criteria satisfaction
- full git diff correctness
- completion gate readiness
- merge readiness
- release readiness
- whether human review can be skipped

## 16. Required Outputs of M63
Планируемые выходы M63:
- `reports/m63-m62-completion-intake.md`
- `docs/TASK-VALIDATION-CONTRACT-ARCHITECTURE.md`
- `schemas/task-validation-package.schema.json`
- `docs/TASK-VALIDATION-PACKAGE-CONTRACT.md`
- `schemas/task-validation-result.schema.json`
- `docs/TASK-VALIDATION-RESULT-CONTRACT.md`
- `docs/TASK-VALIDATION-DECISION-SEMANTICS.md`
- `docs/TASK-VALIDATION-HUMAN-REVIEW-BOUNDARY.md`
- `scripts/check-task-validation-contract.py`
- `docs/TASK-VALIDATION-CONTRACT-VALIDATOR.md`
- `tests/fixtures/m63-task-validation-contract/`
- `reports/m63-task-validation-contract-integration-summary.md`
- `reports/m63-task-validation-contract-action-review.json`
- `reports/m63-task-validation-contract-evidence-report.md`
- `reports/m63-completion-review.md`

## 17. Completion Conditions for M63
M63 может считаться завершённым только если:
- intake READY или READY_WITH_WARNINGS;
- architecture defined;
- package schema defined;
- result schema defined;
- decision semantics defined;
- human review boundary contract defined;
- contract validator exists;
- contract fixtures exist;
- integration summary PASS/PASS_WITH_WARNINGS;
- action review PASS/PASS_WITH_WARNINGS;
- evidence report COMPLETE/COMPLETE_WITH_WARNINGS;
- completion review даёт разрешённый final status;
- M64-M67 artifacts не созданы преждевременно;
- human review boundary remains required.

## 18. Non-Authority Boundary
M63 task validation contract is not approval.
M63 task validation contract does not replace human review.
M63 task validation contract does not complete the task.
M63 task validation contract does not validate completed agent tasks as a production gate.
M63 task validation contract does not define the full task output evidence model.
M63 task validation contract does not define acceptance criteria checking.
M63 task validation contract does not create the unified agent task validation runner.
M63 task validation contract does not authorize merge, push, or release.
M63 task validation contract does not start M64.
Human review remains required.

## 19. Final Status
FINAL_STATUS: M63_TASK_VALIDATION_CONTRACT_ARCHITECTURE_DEFINED
