# Task Output Evidence Model Architecture

## 1. Purpose
Определить архитектуру слоя M64 для evidence (доказательства/подтверждающие данные) после выполнения задачи агентом: что это за объект, как его проверять на уровне архитектуры, где границы доверия и что остаётся на ручной проверке человеком.

architecture_scope: task_output_evidence_model
defines_evidence_schema: false
defines_evidence_checker: false
defines_acceptance_criteria_checker: false
defines_unified_runner: false
defines_false_pass_suite: false
integrates_completion_gate: false
approves_task_completion: false
human_review_required: true

## 2. M64 Position in the Roadmap
M63 validates the task validation contract.
M64 defines and checks agent task output evidence.
M65 checks acceptance criteria.
M66 combines checks into a unified runner.
M67 hardens the pipeline against false PASS and connects it to completion gate readiness.

M64 не заменяет M63 и не забирает ответственность M65/M66/M67.

## 3. Dependency on 64.0 Intake
Источник зависимости: `reports/m64-m63-completion-intake.md`.
Входной статус intake: `FINAL_STATUS: M64_INTAKE_READY_WITH_WARNINGS`.

Сценарии:
- `M64_INTAKE_READY` -> архитектура может идти в обычном режиме.
- `M64_INTAKE_READY_WITH_WARNINGS` -> архитектура может идти, предупреждения обязательно переносятся дальше.
- `M64_INTAKE_BLOCKED` -> архитектура может быть задокументирована, но downstream-задачи M64 не должны продолжаться.

intake_dependency_status: READY_WITH_WARNINGS
downstream_m64_tasks_should_proceed: true
warnings_carried_forward_from_intake: true

## 4. Relationship to M63 Contract Layer
M63 defines:
- task validation package contract
- task validation result contract
- decision semantics
- human review boundary
- contract validator

M64 строится поверх M63 и определяет evidence object (объект доказательств), который потом может ссылаться на потоки package/result из M63.

Required formula:
Agent evidence is required for validation.
Agent evidence is not approval.
Agent evidence must be checked, not trusted.
Human review remains required.

## 5. Relationship to M65 Acceptance Criteria Checker
M64 does not check whether acceptance criteria were satisfied.
M64 only checks whether the agent provided evidence that can later be used by acceptance checking.
M65 will define acceptance criteria checking.

M64 может определить только категории evidence, а не логику принятия по критериям.

## 6. Relationship to M66 Unified Runner
M64 does not create a unified agent task validation runner.
M64 evidence checker is one future input to M66.
M66 will combine M63 contract validation, M64 evidence checking, M65 acceptance checking, and scope/diff validation.

## 7. Relationship to M67 False PASS Resistance
M64 does not create the M67 false PASS resistance suite.
M64 may identify evidence-level false PASS risks.
M67 will test full pipeline false PASS resistance.

Примеры рисков на уровне evidence:
- агент заявил, что команда запускалась, но нет проверяемого следа результата;
- агент заявил, что валидация прошла, но нет результата;
- блокер скрыт как предупреждение;
- заявлено approval;
- отключена ручная проверка;
- заявлен автоматический старт downstream-этапа.

## 8. Evidence Object Lifecycle
Evidence lifecycle states:
- evidence_declared
- evidence_submitted
- evidence_checked
- evidence_passed
- evidence_passed_with_warnings
- evidence_blocked
- evidence_not_enough
- evidence_ready_for_human_review

Это состояния только слоя evidence.
`evidence_passed` does not mean task approved.
`evidence_passed` does not mean task completed.
`evidence_ready_for_human_review` does not mean human review completed.

## 9. Evidence Authority Model
Agent-written evidence is claim.
Evidence checker result is validation.
Validation is not approval.
Human review remains required.

Evidence checker may block bad evidence.
Evidence checker may warn on incomplete evidence.
Evidence checker may report not enough evidence.
Evidence checker may pass structurally valid evidence.
Evidence checker may not approve task completion.

## 10. Evidence Categories
Только архитектурные категории (без финальной схемы JSON):
- identity evidence
- task reference evidence
- file change evidence
- artifact evidence
- command evidence
- validation evidence
- limitation evidence
- warning evidence
- blocker evidence
- forbidden action evidence
- human review evidence
- non-authority boundary evidence

Exact JSON fields and field constraints belong to 64.2.

## 11. Evidence Integrity Categories
Категории целостности (integrity):
- missing evidence
- malformed evidence
- unsupported evidence version
- wrong evidence type
- missing identity
- task mismatch
- missing required fields
- wrong field types
- empty evidence
- contradictory evidence
- stale evidence
- hidden blocker
- forbidden claim
- human review bypass
- downstream scope absorption

Exact integrity mapping belongs to 64.3.

## 12. Evidence Decision Result Categories
Категории результатов проверки evidence:
- M64_EVIDENCE_CHECK_PASS
- M64_EVIDENCE_CHECK_PASS_WITH_WARNINGS
- M64_EVIDENCE_CHECK_BLOCKED
- M64_EVIDENCE_CHECK_NOT_ENOUGH_EVIDENCE

Значения:
- PASS — evidence структурно корректен и без предупреждений/блокеров.
- PASS_WITH_WARNINGS — evidence пригоден, но есть явные неблокирующие предупреждения.
- BLOCKED — evidence некорректен, небезопасен, противоречив или нарушает границы.
- NOT_ENOUGH_EVIDENCE — данных недостаточно для проверяемого вывода.

Exact mapping belongs to 64.3.

## 13. Forbidden Evidence Claims
Evidence must never claim:
- approval granted
- task approved
- task completion approved
- complete without review
- human review not required
- merged
- released
- pushed
- merge authorized
- push authorized
- release authorized
- lifecycle mutated
- completion gate passed
- production task acceptance gate passed
- M65 started automatically
- M66 started automatically
- M67 started automatically

Exact forbidden claim boundary belongs to 64.4.

## 14. Hidden Blocker Concept
Hidden blocker: блокирующее условие замаскировано как warning/limitation/neutral note.
Примеры:
- warning говорит "required check failed";
- warning говорит "cannot proceed";
- warning говорит "critical issue remains";
- warning говорит "unsafe to continue".

Правило архитектуры:
- Hidden blockers must not produce clean PASS.
- High-confidence hidden blockers should block.
- Ambiguous hidden blockers should at least warn.

Exact detection logic belongs to 64.3 and 64.5.

## 15. Stale and Contradictory Evidence
Stale evidence: evidence больше не соответствует текущему результату задачи.
Примеры:
- ссылка на старый `task_id`;
- ссылка на устаревший путь артефакта;
- результат проверки из предыдущего запуска;
- ссылки на файлы, которых нет в текущем diff (список изменений).

Contradictory evidence: внутренние противоречия evidence.
Примеры:
- blockers пуст, но warning описывает блокер;
- forbidden_actions_performed=false, но в тексте есть факт запрещённого действия;
- validation_results=PASS, но notes говорят failed;
- created_artifacts содержит файл без объяснения, которого нет в files_changed.

Exact handling belongs to 64.3 and 64.5.

## 16. What Evidence Can Prove
Evidence может доказать только проверяемые факты уровня данных:
- агент предоставил структурированный пакет заявлений;
- данные можно машинно проверить на форму и согласованность;
- заявлены warnings/blockers/limitations;
- соблюдены non-authority и human review границы на уровне claims.

## 17. What Evidence Cannot Prove
Evidence сам по себе не доказывает:
- approval;
- task completion;
- выполнение acceptance criteria;
- готовность к merge/push/release;
- прохождение completion gate;
- завершение human review.

## 18. Deferred Work
Перенос ответственности:
- 64.2: финальная evidence schema.
- 64.3: integrity and decision semantics mapping.
- 64.4: строгая claim boundary для запрещённых утверждений.
- 64.5: evidence checker implementation.
- M65: acceptance criteria checker.
- M66: unified runner.
- M67: false PASS resistance + completion gate readiness coupling.

## 19. Human Review Boundary
M64 не отменяет ручную проверку.
Даже при `M64_EVIDENCE_CHECK_PASS` итоговое решение остаётся за человеком.
Human review remains required.

## 20. Non-Authority Boundary
M64 evidence model architecture is not approval.
M64 evidence model architecture does not replace human review.
M64 evidence model architecture does not complete M64.
M64 evidence model architecture does not start M65.
M64 evidence model architecture does not create the evidence schema.
M64 evidence model architecture does not create the evidence checker.
M64 evidence model architecture does not define acceptance criteria checking.
M64 evidence model architecture does not create the unified agent task validation runner.
M64 evidence model architecture does not create the false PASS resistance suite.
M64 evidence model architecture does not integrate the completion gate.
M64 evidence model architecture does not validate completed agent tasks as a production gate.
M64 evidence model architecture does not approve any agent task result.
M64 evidence model architecture does not authorize merge, push, or release.
Human review remains required.

## 21. Final Status
FINAL_STATUS: M64_EVIDENCE_MODEL_ARCHITECTURE_DEFINED_WITH_WARNINGS
