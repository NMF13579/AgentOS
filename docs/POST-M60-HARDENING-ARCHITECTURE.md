# Post-M60 Hardening Architecture

## 1. Purpose
Определить безопасную архитектуру M61 hardening (этап усиления и доработки), которая укрепляет фундамент M60 без изменения базового смысла проверок и без перехода в M62 pipeline (конвейер приёмки задач).

## 2. M61 Position in the Roadmap
M61 идёт после завершения M60 и до M62.
M61 фокусируется на проверке и укреплении качества существующей базы M60.
M61 не запускает M62 автоматически.
Текущий intake из 61.0: `FINAL_STATUS: M61_INTAKE_READY_WITH_WARNINGS`.

## 3. Source Foundation from M60
Основа M61:
- `reports/m60-completion-review.md`
- `reports/m60-cleanup-evidence-report.md`
- `reports/m60-cleanup-action-review.json`
- `reports/m60-cleanup-integration-summary.md`
- M60 registry/reusable/regression foundation (реестр/повторно используемые проверки/регрессионный раннер) как существующая база для усиления.

## 4. Hardening Scope
M61 may inspect and harden:
- M60 completion review chain
- M60 cleanup evidence report
- M60 cleanup action review
- M60 cleanup integration summary
- M60 execution verification registry
- M60 reusable checks
- M60 regression runner
- M60 checker output semantics
- M60 warning/blocker/final-status mapping
- known false PASS risks related to M60 foundation

## 5. Protected M56–M60 Semantics
M61 must not change the meaning of:
- PASS
- PASS_WITH_WARNINGS
- BLOCKED
- Evidence is not approval
- Completion review is not approval
- Human review remains required
- No automatic lifecycle mutation
- No merge/push/release authorization

## 6. False PASS Risk Categories
Минимальный список категорий рисков ложного PASS:
- missing artifact but PASS
- malformed JSON but PASS
- warning hidden as PASS
- blocker downgraded to warning
- fake validation output accepted
- registry stale but accepted
- evidence manually written without runtime correlation
- protected path modified but not detected
- non-authority boundary removed
- human_review_required false accepted
- downstream artifact created early
- completion claimed without evidence
- unknown status accepted
- checker skipped silently

## 7. Registry / Reusable / Regression Hardening Model
Модель hardening:
- Проверки усиливаются только внутри текущей M60-модели, без смены базовых статусов.
- Усиление направлено на более строгую фиксацию ошибок входа, статусов и корреляции runtime-результатов.
- Любое усиление должно сохранять совместимость с действующими артефактами M60.

## 8. Allowed Fixes
Разрешены только безопасные улучшения, которые:
- strengthen malformed input blocking
- strengthen unknown status handling
- strengthen warning/blocker mapping
- strengthen non-authority boundary detection
- strengthen protected path detection against existing M60 artifacts
- strengthen runtime correlation checks for existing M60 report formats
- clarify strict mode behavior for existing M60 checkers

Эти изменения должны сохранять existing M56–M60 semantics.

## 9. Forbidden Fixes
M61 must not:
- create task acceptance pipeline
- create task result schema
- create agent evidence schema
- create acceptance criteria checker
- create production task validation gate
- create unified agent task validation runner
- create completion gate integration
- approve task completion
- start M62 automatically
- mutate lifecycle state
- authorize merge, push, or release
- mass-clean documentation or scripts
- archive M56–M60 artifacts
- delete M56–M60 artifacts

## 10. M61 vs M62 Responsibility Split
- M61 reviews and hardens the M60 foundation.
- M61 does not validate completed agent tasks as a production gate.
- M61 does not define the task result contract.
- M61 does not define the agent evidence schema.
- M61 does not define acceptance criteria semantics.
- M61 does not create the unified agent task validation runner.
- M62 begins the thin task acceptance MVP after M61 completion review allows it.

## 11. Non-Authority Boundary
M61 hardening is not approval.
M61 hardening does not start M62.
M61 hardening does not validate completed agent tasks as a production gate.
M61 hardening does not replace human review.
M61 hardening does not mutate lifecycle state.
M61 hardening does not authorize merge, push, or release.
Human review remains required.

## 12. Required Outputs of M61
Архитектура M61 требует только профильные hardening-артефакты этапа M61 (risk map/plan/repair/integration/action/evidence/completion) в пределах задач M61.
M61 не создаёт M62 артефакты.

## 13. Completion Conditions for M61
M61 может считаться завершённым только если:
- риски ложного PASS явно покрыты и проверяемы,
- усиления не ломают semantics M56–M60,
- non-authority границы (границы «без права одобрения») сохранены,
- решение о переходе дальше подтверждено человеком.

## 14. Final Status
FINAL_STATUS: M61_HARDENING_ARCHITECTURE_DEFINED
