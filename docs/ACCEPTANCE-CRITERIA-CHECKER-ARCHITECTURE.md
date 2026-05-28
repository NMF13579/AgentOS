# Acceptance Criteria Checker Architecture (M65)

## 1. Purpose
M65 introduces an acceptance criteria checking layer.

M64 validates whether agent output evidence is structured, bounded, and reviewable.
M65 validates whether structured evidence appears to satisfy structured acceptance criteria.
M65 is a validation signal only.
Acceptance criteria checker is not approval.
M65 is not task completion.
Human review remains required.

## 2. Problem Statement
После M64 остаётся разрыв:
- M64 умеет проверять структуру evidence, границы claims и human review boundary.
- M64 не умеет решать, выполнены ли сами acceptance criteria задачи.

M64 не определяет:
- satisfied/failed/missing/ambiguous/manual-review-only criteria;
- соответствие expected artifacts и actual artifacts;
- соответствие changed files критериям задачи;
- достаточную корреляцию validation outputs с критериями.

## 3. M65 Position in the Validation Chain
M63 = task validation contract
M64 = agent output evidence model
M65 = acceptance criteria checker
M66 = unified runner
M67 = false PASS resistance + completion gate hardening

- M63 задаёт контрактные границы.
- M64 задаёт структуру evidence.
- M65 сравнивает structured criteria и structured evidence.
- M66 позже объединит раннеры.
- M67 позже усилит защиту от ложного PASS и completion gate.

## 4. Core Architecture Principle
M65 checker must not infer full task meaning from free-form Markdown.
M65 checker must operate on structured acceptance criteria package.

Почему:
- свободный Markdown неоднозначен для детерминированной проверки;
- checker не должен имитировать «полное понимание задачи»;
- неясные критерии должны давать warning/blocker/not-enough-evidence, а не фальшивый PASS.

## 5. What M65 Checks
Архитектурно M65 проверяет structured fields:
- required criteria / optional criteria;
- expected artifacts / actual artifacts;
- changed files;
- validation outputs;
- evidence result;
- failed/missing/ambiguous/manual-review-only criteria;
- human review boundary;
- forbidden approval/completion claims.

## 6. What M65 Does Not Check
M65 не делает:
- approval;
- task completion authority;
- completion gate integration;
- unified runner;
- false PASS resistance suite;
- merge/push/release authorization;
- automatic M66/M67 start;
- unrestricted semantic evaluation free-form Markdown;
- full project quality validation.

## 7. Inputs
Архитектурный вход M65:
- acceptance criteria check package;
- structured acceptance criteria;
- expected artifacts;
- actual artifacts;
- changed files;
- agent evidence result;
- validation outputs;
- warnings;
- blockers;
- non-authority boundary;
- human_review_required flag.

Полная JSON Schema здесь не задаётся (это 65.2).

## 8. Outputs
Ожидаемые значения результата:
- M65_ACCEPTANCE_CHECK_PASS
- M65_ACCEPTANCE_CHECK_PASS_WITH_WARNINGS
- M65_ACCEPTANCE_CHECK_BLOCKED
- M65_ACCEPTANCE_CHECK_NOT_ENOUGH_EVIDENCE

На архитектурном уровне:
- PASS: required criteria выглядят выполненными без блокеров.
- PASS_WITH_WARNINGS: required criteria выглядят выполненными, но есть warning-уровень рисков.
- BLOCKED: required criteria failed / required artifacts missing / required validation failed / human review boundary broken / forbidden claims present.
- NOT_ENOUGH_EVIDENCE: недостаточно structured evidence для надёжной оценки без ложного BLOCKED/PASS.

Подробный приоритет решений — в 65.3.

## 9. Acceptance Criteria vs Evidence
Evidence описывает, что агент утверждает, что сделал.
Acceptance criteria описывают, что требовалось сделать.
M65 сравнивает evidence и artifacts с criteria.
Evidence не является authority.
Agent self-claims не являются authority.

Поле вроде `all_acceptance_criteria_met: true` не должно считаться authority.

## 10. Acceptance Check vs Approval
Acceptance criteria appear satisfied at M65 level.
This is not approval.
This does not complete the task.
Human review remains required.

Checker result = validation signal.
Approval и completion остаются вне M65.

## 11. Manual Review Criteria
Архитектурные правила:
- manual-review-only criteria не дают clean automated PASS;
- required manual-review-only criteria должны вести к blocker или not-enough-evidence (подробно в 65.3);
- optional manual-review criteria могут давать warnings.

## 12. Forbidden Claims
M65 artifacts/checker outputs не должны утверждать:
- task approved;
- task accepted by system;
- completion approved;
- human review not required;
- merge/push/release authorized;
- production ready / ready for production;
- completion gate passed;
- M66 started automatically;
- M67 started automatically.

## 13. Failure Modes
Ключевые риски M65:
- checker превращается в «magic evaluator»;
- checker выводит скрытые требования из Markdown;
- checker доверяет self-claims агента;
- checker считает missing evidence как PASS;
- checker считает manual-review-only criteria как automated PASS;
- checker путает validation и approval;
- checker начинает поглощать scope M66/M67.

## 14. Relationship to Later M65 Tasks
- 65.2: acceptance criteria check package contract.
- 65.3: decision semantics and priority order.
- 65.4: claim boundary.
- 65.5: read-only checker implementation.
- 65.6: fixtures.
- 65.7: integration validation.
- 65.8: action review.
- 65.9: evidence report.
- 65.10: completion review.

## 15. Final Status
FINAL_STATUS: M65_ACCEPTANCE_CRITERIA_ARCHITECTURE_DEFINED_WITH_WARNINGS
