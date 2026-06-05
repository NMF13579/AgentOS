# M61 Checker Hardening Plan

## 1. Purpose
Сформировать план усиления текущих проверок M60, чтобы убрать риски ложного PASS (ложный PASS = система показывает «всё хорошо», хотя факты этого не подтверждают), не меняя смысл старых правил M56-M60.

## 2. Inputs Reviewed
- `reports/m61-m60-completion-intake.md`
- `docs/POST-M60-HARDENING-ARCHITECTURE.md`
- `reports/m61-false-pass-risk-map.md`
- `reports/m60-completion-review.md`
- `reports/m60-cleanup-action-review.json`
- `reports/m60-cleanup-evidence-report.md`
- `reports/m60-cleanup-integration-summary.md`
- `scripts/check-execution-verification-registry.py`
- `scripts/check-execution-verification-chain.py`
- `scripts/check-execution-verification-regression.py`
- `docs/EXECUTION-VERIFICATION-REGISTRY.md`
- `docs/EXECUTION-VERIFICATION-REUSABLE-CHECKS.md`
- `docs/EXECUTION-VERIFICATION-REGRESSION-RUNNER.md`

## 3. Dependency Status
- 61.0 intake: present, `M61_INTAKE_READY_WITH_WARNINGS`
- 61.1 architecture: present, `M61_HARDENING_ARCHITECTURE_DEFINED`
- 61.2 risk map: present, `M61_FALSE_PASS_RISK_MAP_COMPLETE_WITH_WARNINGS`
- M60 checker components: present
- Dependency blockers: none
- Dependency warnings: upstream M60/M61 statuses contain warnings

## 4. Components Reviewed
1. `scripts/check-execution-verification-registry.py`
2. `scripts/check-execution-verification-chain.py`
3. `scripts/check-execution-verification-regression.py`
4. `docs/EXECUTION-VERIFICATION-REGISTRY.md`
5. `docs/EXECUTION-VERIFICATION-REUSABLE-CHECKS.md`
6. `docs/EXECUTION-VERIFICATION-REGRESSION-RUNNER.md`
7. `reports/m60-completion-review.md`
8. `reports/m60-cleanup-action-review.json`
9. `reports/m60-cleanup-evidence-report.md`
10. `reports/m60-cleanup-integration-summary.md`
11. `reports/m61-false-pass-risk-map.md`

## 5. Hardening Classification Model
- `apply-now`: безопасное усиление в рамках текущих M60 форматов и смыслов.
- `defer-to-M62`: отложить до M62, потому что нужен более широкий контур.
- `defer-to-M63`: отложить до M63, если затрагивает более глубокую модель приёмки.
- `manual-review-required`: нужен ручной выбор человека перед изменением.
- `unsafe-to-change`: риск поломать M56-M60 смыслы слишком высокий.

## 6. Hardening Items
### Item 1
- item_id: M61-CHP-001
- component: `scripts/check-execution-verification-regression.py`
- related_risk_id: M61-FP-002
- current_behavior: часть malformed JSON блокируется.
- weakness: не все ветки ошибок входа описаны одинаково строго.
- false_pass_risk: malformed JSON but PASS
- recommended_change: унифицировать fail-closed (ошибка входа всегда BLOCKED) для всех требуемых JSON входов.
- fix_classification: apply-now
- safe_to_change_now: true
- fixture_needed: true
- validation_needed: `python3 scripts/check-execution-verification-regression.py --json` + негативный malformed JSON запуск
- target_task: 61.5
- target_milestone: M61
- notes: без изменения PASS/PASS_WITH_WARNINGS/BLOCKED семантики

### Item 2
- item_id: M61-CHP-002
- component: `scripts/check-execution-verification-chain.py`
- related_risk_id: M61-FP-001
- current_behavior: проверка наличия обязательных артефактов есть.
- weakness: возможны края (edge-cases) при фазовых переходах.
- false_pass_risk: missing required artifact detection
- recommended_change: усилить проверку обязательных артефактов с явной блокировкой при пропуске.
- fix_classification: apply-now
- safe_to_change_now: true
- fixture_needed: true
- validation_needed: `python3 scripts/check-execution-verification-chain.py --json`
- target_task: 61.5
- target_milestone: M61
- notes: использовать только существующие M60 пути и форматы

### Item 3
- item_id: M61-CHP-003
- component: `scripts/check-execution-verification-chain.py`
- related_risk_id: M61-FP-013
- current_behavior: unknown status обычно приводит к проблеме.
- weakness: нужна единая политика на всех ветках обработки статусов.
- false_pass_risk: unknown status handling
- recommended_change: единое правило «неизвестный статус => BLOCKED».
- fix_classification: apply-now
- safe_to_change_now: true
- fixture_needed: true
- validation_needed: `python3 scripts/check-execution-verification-chain.py --check final-status --json`
- target_task: 61.5
- target_milestone: M61
- notes: без добавления новых статусов

### Item 4
- item_id: M61-CHP-004
- component: `scripts/check-execution-verification-regression.py`
- related_risk_id: M61-FP-014
- current_behavior: FINAL_STATUS часто проверяется.
- weakness: не везде жёстко проверяется отсутствие/дублирование FINAL_STATUS.
- false_pass_risk: missing final status handling
- recommended_change: требовать ровно один валидный FINAL_STATUS там, где это обязательно.
- fix_classification: apply-now
- safe_to_change_now: true
- fixture_needed: true
- validation_needed: `python3 scripts/check-execution-verification-regression.py --check final-status --json`
- target_task: 61.5
- target_milestone: M61
- notes: ориентироваться на текущие M60 форматы отчётов

### Item 5
- item_id: M61-CHP-005
- component: `scripts/check-execution-verification-regression.py`
- related_risk_id: M61-FP-003
- current_behavior: warnings обычно переводят статус в PASS_WITH_WARNINGS.
- weakness: требуется контроль, что warning не теряется при агрегации.
- false_pass_risk: warning/blocker status mapping
- recommended_change: усилить тестируемую ветку «есть warnings => не PASS».
- fix_classification: apply-now
- safe_to_change_now: true
- fixture_needed: true
- validation_needed: `python3 scripts/check-execution-verification-regression.py --json`
- target_task: 61.5
- target_milestone: M61
- notes: не менять значения финальных статусов

### Item 6
- item_id: M61-CHP-006
- component: `scripts/check-execution-verification-regression.py`
- related_risk_id: M61-FP-009
- current_behavior: non-authority строки проверяются.
- weakness: возможна неполная проверка во всех режимах запуска.
- false_pass_risk: non_authority boundary detection
- recommended_change: одинаково строгая проверка обязательных non-authority строк в plain/json путях.
- fix_classification: apply-now
- safe_to_change_now: true
- fixture_needed: true
- validation_needed: `python3 scripts/check-execution-verification-regression.py --check non-authority --json`
- target_task: 61.5
- target_milestone: M61
- notes: сохранить текущие точные формулировки

### Item 7
- item_id: M61-CHP-007
- component: `reports/*` + checker logic
- related_risk_id: M61-FP-010
- current_behavior: human review фразы присутствуют в текущих отчётах.
- weakness: контроль этого правила не полностью унифицирован по всем отчётам.
- false_pass_risk: human_review_required enforcement
- recommended_change: определить единое минимальное правило проверки на обязательную фразу.
- fix_classification: manual-review-required
- safe_to_change_now: false
- fixture_needed: false
- validation_needed: manual confirmation of exact phrase policy before automation
- target_task: 61.4
- target_milestone: M61
- notes: сначала решение человека по объёму enforcement

### Item 8
- item_id: M61-CHP-008
- component: `scripts/check-execution-verification-chain.py`
- related_risk_id: M61-FP-008
- current_behavior: protected path проверки уже есть.
- weakness: важно не пропустить изменение существующих M60 артефактов.
- false_pass_risk: protected path detection against existing M60 artifacts
- recommended_change: усилить покрытие существующих M60 путей в protected checks.
- fix_classification: apply-now
- safe_to_change_now: true
- fixture_needed: true
- validation_needed: `python3 scripts/check-execution-verification-chain.py --json`
- target_task: 61.5
- target_milestone: M61
- notes: без расширения на M62 acceptance

### Item 9
- item_id: M61-CHP-009
- component: `reports/m60-cleanup-integration-summary.md` correlation logic
- related_risk_id: M61-FP-007
- current_behavior: runtime correlation присутствует.
- weakness: нужно усилить защиту от ручной подмены без runtime совпадения.
- false_pass_risk: runtime correlation checks for existing M60 report formats
- recommended_change: добавить stricter cross-check полей result/exit_code по всем связкам.
- fix_classification: apply-now
- safe_to_change_now: true
- fixture_needed: true
- validation_needed: `python3 scripts/check-execution-verification-regression.py --json`
- target_task: 61.5
- target_milestone: M61
- notes: использовать только текущие M60 JSON-блоки

### Item 10
- item_id: M61-CHP-010
- component: `scripts/check-execution-verification-regression.py`
- related_risk_id: M61-FP-017
- current_behavior: ранние M61 артефакты частично контролируются.
- weakness: возможны gaps в списке «что запрещено до нужного шага».
- false_pass_risk: premature M61 completion artifact detection
- recommended_change: уточнить фазовую проверку для раннего `reports/m61-completion-review.md`.
- fix_classification: apply-now
- safe_to_change_now: true
- fixture_needed: true
- validation_needed: `python3 scripts/check-execution-verification-regression.py --check no-premature-downstream --json`
- target_task: 61.5
- target_milestone: M61
- notes: не затрагивать M62 контракты

### Item 11
- item_id: M61-CHP-011
- component: `scripts/check-execution-verification-regression.py`
- related_risk_id: M61-FP-018
- current_behavior: M62 пути блокируются.
- weakness: критично сохранить строгую path-based блокировку.
- false_pass_risk: premature M62 artifact detection
- recommended_change: укрепить и протестировать блокировку M62 путей без ложных пропусков.
- fix_classification: apply-now
- safe_to_change_now: true
- fixture_needed: true
- validation_needed: `python3 scripts/check-execution-verification-regression.py --check no-premature-downstream --json`
- target_task: 61.5
- target_milestone: M61
- notes: не считать сторонние файлы M62, если в пути нет m62

### Item 12
- item_id: M61-CHP-012
- component: `scripts/check-execution-verification-regression.py`
- related_risk_id: M61-FP-016
- current_behavior: strict mode есть.
- weakness: возможна неоднородность между strict/non-strict в редких ветках.
- false_pass_risk: strict mode behavior
- recommended_change: уточнить правило эскалации warning->blocker только по допустимым сценариям.
- fix_classification: apply-now
- safe_to_change_now: true
- fixture_needed: true
- validation_needed: `python3 scripts/check-execution-verification-regression.py --strict --json`
- target_task: 61.5
- target_milestone: M61
- notes: не допускать downgrade blocker

### Item 13
- item_id: M61-CHP-013
- component: `scripts/check-execution-verification-regression.py`
- related_risk_id: M61-FP-016
- current_behavior: parsing runner outputs выполняется.
- weakness: нужно жёстко валидировать обязательные поля результата.
- false_pass_risk: runner output parsing
- recommended_change: fail-closed при отсутствии `result` или `exit_code`.
- fix_classification: apply-now
- safe_to_change_now: true
- fixture_needed: true
- validation_needed: `python3 scripts/check-execution-verification-regression.py --json`
- target_task: 61.5
- target_milestone: M61
- notes: без изменения JSON-контракта

### Item 14
- item_id: M61-CHP-014
- component: `scripts/check-execution-verification-registry.py`
- related_risk_id: M61-FP-006
- current_behavior: registry валидируется по текущим правилам.
- weakness: stale state detection частично ограничен.
- false_pass_risk: registry staleness detection
- recommended_change: расширить stale-проверки можно только после отдельного дизайна.
- fix_classification: defer-to-M62
- safe_to_change_now: false
- fixture_needed: true
- validation_needed: manual confirmation + `python3 scripts/check-execution-verification-registry.py --json`
- target_task: M62-planning
- target_milestone: M62
- notes: риск задеть базовую семантику M60

### Item 15
- item_id: M61-CHP-015
- component: orchestration across checkers
- related_risk_id: M61-FP-015
- current_behavior: факты запусков отражаются, но не как отдельный унифицированный трассинг.
- weakness: checker skipped silently
- false_pass_risk: checker skipped silently
- recommended_change: добавить общий слой трассировки запусков чекеров.
- fix_classification: defer-to-M63
- safe_to_change_now: false
- fixture_needed: true
- validation_needed: manual confirmation of design scope
- target_task: M63-planning
- target_milestone: M63
- notes: это уже выходит в новую инфраструктуру

### Item 16
- item_id: M61-CHP-016
- component: global policy semantics
- related_risk_id: M61-FP-004
- current_behavior: blocker mapping в целом строгий.
- weakness: глобальный рефакторинг mapping может случайно изменить смысл M56-M60.
- false_pass_risk: warning/blocker status mapping
- recommended_change: не менять глобально в M61, ограничиться локальным hardening.
- fix_classification: unsafe-to-change
- safe_to_change_now: false
- fixture_needed: false
- validation_needed: manual review required before any broad refactor
- target_task: none
- target_milestone: M64
- notes: высокий риск нарушить старые гарантии

## 7. Apply-Now Candidates
- M61-CHP-001
- M61-CHP-002
- M61-CHP-003
- M61-CHP-004
- M61-CHP-005
- M61-CHP-006
- M61-CHP-008
- M61-CHP-009
- M61-CHP-010
- M61-CHP-011
- M61-CHP-012
- M61-CHP-013

## 8. Deferred to M62
- M61-CHP-014

## 9. Deferred to M63
- M61-CHP-015

## 10. Manual Review Required
- M61-CHP-007

## 11. Unsafe to Change
- M61-CHP-016

## 12. Fixture Requirements for 61.5
Если 61.5 меняет поведение checker, нужно добавить/обновить минимальные точечные fixtures (фикстуры = тестовые примеры) ровно для исправляемого поведения.
Это repair fixtures, а не полный M67 false PASS suite.
Нельзя менять поведение checker без хотя бы одного positive/negative validation path (путь проверки «должно пройти» / «должно блокироваться»).

Apply-now items requiring fixtures:
- M61-CHP-001, 002, 003, 004, 005, 006, 008, 009, 010, 011, 012, 013

## 13. Validation Requirements for 61.5
Плановые команды после ремонта (по item-ам):
- `python3 scripts/check-execution-verification-registry.py --help`
- `python3 scripts/check-execution-verification-registry.py --json`
- `python3 scripts/check-execution-verification-chain.py --json`
- `python3 scripts/check-execution-verification-regression.py --json`
- `python3 scripts/check-execution-verification-regression.py --strict --json`
- `python3 scripts/check-execution-verification-regression.py --check no-premature-downstream --json`
- `python3 scripts/check-execution-verification-regression.py --check non-authority --json`
- `python3 -m json.tool reports/m60-cleanup-action-review.json >/dev/null`

Команды, которые зависят от нового дизайна (manual confirmation):
- трассировка checker skipped silently (M61-CHP-015)
- расширенный stale-detection policy (M61-CHP-014)

## 14. Non-Authority Boundary
M61 checker hardening plan is not approval.
M61 checker hardening plan does not repair checkers.
M61 checker hardening plan does not start M62.
M61 checker hardening plan does not validate completed agent tasks as a production gate.
M61 checker hardening plan does not mutate lifecycle state.
M61 checker hardening plan does not authorize merge, push, or release.
Human review remains required.

## 15. Final Status
FINAL_STATUS: M61_CHECKER_HARDENING_PLAN_COMPLETE_WITH_WARNINGS
