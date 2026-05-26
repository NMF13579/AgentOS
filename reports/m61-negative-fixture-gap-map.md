# M61 Negative Fixture Gap Map

## 1. Purpose
Определить, каких негативных фикстур (фикстура = тестовый пример, который должен показать ошибку) не хватает для безопасного hardening M60-проверок в M61.

## 2. Inputs Reviewed
- `reports/m61-m60-completion-intake.md`
- `docs/POST-M60-HARDENING-ARCHITECTURE.md`
- `reports/m61-false-pass-risk-map.md`
- `reports/m61-checker-hardening-plan.md`
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
- выборочный обзор `tests/fixtures/`

## 3. Dependency Status
- 61.0, 61.1, 61.2, 61.3: present
- зависимые M60 отчёты и checker-компоненты: present
- блокеров для построения gap map: none
- предупреждения: upstream статусы содержат `...WITH_WARNINGS`

## 4. Fixture Gap Definition
A negative fixture gap exists when an important unsafe, malformed, incomplete, unauthorized, stale, or contradictory condition is not represented by a deterministic failing example.

A checker without negative fixture coverage can create false confidence.
Positive-only validation is insufficient for hardening.
No new checker behavior should be accepted without at least one positive or negative validation path.
M61 fixture mapping is not the full M67 false PASS suite.

## 5. Existing Fixture Coverage Summary
- В репозитории есть широкие фикстуры по предыдущим темам (approval/boundary/apply-transition и т.д.).
- По M60-specific hardening рискам покрытие есть частично и не всегда в виде узких детерминированных отрицательных кейсов.
- Для 61.5 нужны минимальные точечные repair-fixtures под конкретные изменения.

## 6. Gap Classification Model
- `repair-fixture`: нужно для конкретного исправления 61.5.
- `future-suite-fixture`: относится к большой anti-false-pass программе M67.
- `manual-review-case`: пока не безопасно формализовать как детерминированную фикстуру.
- `not-applicable`: уже покрыто детерминированной проверкой или вне M61 scope.

## 7. Negative Fixture Gap Map
### Gap 1
- gap_id: M61-NFG-001
- title: missing required artifact
- related_risk_id: M61-FP-001
- related_hardening_item_id: M61-CHP-002
- checker_or_runner: `scripts/check-execution-verification-chain.py`
- missing_negative_case: отсутствует узкий кейс с удалённым обязательным M60 артефактом
- example_failure_mode: missing required artifact but PASS-like result
- expected_result: BLOCKED/INVALID
- current_coverage: partial
- priority: P0
- target_task: 61.5
- target_milestone: M61
- fixture_type: repair-fixture
- notes: критично для fail-closed поведения

### Gap 2
- gap_id: M61-NFG-002
- title: malformed registry JSON
- related_risk_id: M61-FP-002
- related_hardening_item_id: M61-CHP-001
- checker_or_runner: `scripts/check-execution-verification-regression.py`
- missing_negative_case: единый кейс с поломанным registry JSON на уровне regression flow
- example_failure_mode: malformed registry JSON accepted
- expected_result: BLOCKED
- current_coverage: partial
- priority: P1
- target_task: 61.5
- target_milestone: M61
- fixture_type: repair-fixture
- notes: нужен минимальный malformed пример

### Gap 3
- gap_id: M61-NFG-003
- title: malformed evidence JSON
- related_risk_id: M61-FP-007
- related_hardening_item_id: M61-CHP-009
- checker_or_runner: `scripts/check-execution-verification-regression.py`
- missing_negative_case: нет узкого кейса для повреждённого JSON-блока evidence report
- example_failure_mode: malformed evidence JSON treated as usable
- expected_result: BLOCKED
- current_coverage: partial
- priority: P1
- target_task: 61.5
- target_milestone: M61
- fixture_type: repair-fixture
- notes: проверка парсинга + корреляции

### Gap 4
- gap_id: M61-NFG-004
- title: missing final status
- related_risk_id: M61-FP-014
- related_hardening_item_id: M61-CHP-004
- checker_or_runner: `scripts/check-execution-verification-regression.py`
- missing_negative_case: отчёт без FINAL_STATUS
- example_failure_mode: missing final status accepted
- expected_result: BLOCKED
- current_coverage: partial
- priority: P1
- target_task: 61.5
- target_milestone: M61
- fixture_type: repair-fixture
- notes: нужен deterministic fail кейс

### Gap 5
- gap_id: M61-NFG-005
- title: blocker hidden as warning
- related_risk_id: M61-FP-004
- related_hardening_item_id: M61-CHP-016
- checker_or_runner: status aggregation layer
- missing_negative_case: отдельный кейс с непустым blocker list и warning-like итогом
- example_failure_mode: blocker downgraded to warning
- expected_result: BLOCKED
- current_coverage: limited
- priority: P0
- target_task: M64-planning
- target_milestone: M64
- fixture_type: manual-review-case
- notes: broad mapping change unsafe for M61

### Gap 6
- gap_id: M61-NFG-006
- title: warning hidden as PASS
- related_risk_id: M61-FP-003
- related_hardening_item_id: M61-CHP-005
- checker_or_runner: `scripts/check-execution-verification-regression.py`
- missing_negative_case: есть warnings, но итог PASS
- example_failure_mode: warning hidden as PASS
- expected_result: PASS_WITH_WARNINGS
- current_coverage: partial
- priority: P1
- target_task: 61.5
- target_milestone: M61
- fixture_type: repair-fixture
- notes: нужен focused case

### Gap 7
- gap_id: M61-NFG-007
- title: forbidden path modified
- related_risk_id: M61-FP-008
- related_hardening_item_id: M61-CHP-008
- checker_or_runner: `scripts/check-execution-verification-chain.py`
- missing_negative_case: модификация protected path не детектирована
- example_failure_mode: forbidden path modified but accepted
- expected_result: BLOCKED
- current_coverage: partial
- priority: P0
- target_task: 61.5
- target_milestone: M61
- fixture_type: repair-fixture
- notes: critical boundary case

### Gap 8
- gap_id: M61-NFG-008
- title: approval claim present
- related_risk_id: M61-FP-009
- related_hardening_item_id: M61-CHP-006
- checker_or_runner: non-authority checks
- missing_negative_case: отчёт содержит approval claim
- example_failure_mode: approval claim accepted
- expected_result: BLOCKED
- current_coverage: partial via older boundary fixtures
- priority: P0
- target_task: 61.5
- target_milestone: M61
- fixture_type: repair-fixture
- notes: M60/M61 specific wording

### Gap 9
- gap_id: M61-NFG-009
- title: human review disabled
- related_risk_id: M61-FP-010
- related_hardening_item_id: M61-CHP-007
- checker_or_runner: policy boundary checks
- missing_negative_case: `Human review remains required.` отсутствует
- example_failure_mode: human review disabled accepted
- expected_result: BLOCKED
- current_coverage: partial
- priority: P0
- target_task: 61.5-manual-gate
- target_milestone: M61
- fixture_type: manual-review-case
- notes: сначала зафиксировать единый enforcement policy

### Gap 10
- gap_id: M61-NFG-010
- title: fake runtime checker output
- related_risk_id: M61-FP-005
- related_hardening_item_id: M61-CHP-015
- checker_or_runner: runtime correlation layer
- missing_negative_case: поддельный checker output подставлен в отчёт
- example_failure_mode: fake runtime checker output accepted
- expected_result: BLOCKED
- current_coverage: limited
- priority: P1
- target_task: M67-suite
- target_milestone: M67
- fixture_type: future-suite-fixture
- notes: лучше в широком anti-false-pass наборе

### Gap 11
- gap_id: M61-NFG-011
- title: stale registry entry
- related_risk_id: M61-FP-006
- related_hardening_item_id: M61-CHP-014
- checker_or_runner: `scripts/check-execution-verification-registry.py`
- missing_negative_case: устаревшая запись registry считается валидной
- example_failure_mode: stale registry accepted
- expected_result: INVALID/BLOCKED
- current_coverage: limited
- priority: P1
- target_task: M62-planning
- target_milestone: M62
- fixture_type: future-suite-fixture
- notes: требует расширения stale policy

### Gap 12
- gap_id: M61-NFG-012
- title: premature downstream artifact
- related_risk_id: M61-FP-011
- related_hardening_item_id: M61-CHP-011
- checker_or_runner: `scripts/check-execution-verification-regression.py`
- missing_negative_case: ранний downstream артефакт не блокируется
- example_failure_mode: premature downstream artifact accepted
- expected_result: BLOCKED
- current_coverage: partial
- priority: P0
- target_task: 61.5
- target_milestone: M61
- fixture_type: repair-fixture
- notes: phase-aware logic regression guard

### Gap 13
- gap_id: M61-NFG-013
- title: M61 completion artifact created early
- related_risk_id: M61-FP-017
- related_hardening_item_id: M61-CHP-010
- checker_or_runner: `scripts/check-execution-verification-regression.py`
- missing_negative_case: ранний `reports/m61-completion-review.md`
- example_failure_mode: M61 completion artifact accepted early
- expected_result: BLOCKED
- current_coverage: partial
- priority: P0
- target_task: 61.5
- target_milestone: M61
- fixture_type: repair-fixture
- notes: must fail before allowed stage

### Gap 14
- gap_id: M61-NFG-014
- title: M62 artifact created early
- related_risk_id: M61-FP-018
- related_hardening_item_id: M61-CHP-011
- checker_or_runner: `scripts/check-execution-verification-regression.py`
- missing_negative_case: путь с `m62` появляется заранее
- example_failure_mode: M62 artifact accepted early
- expected_result: BLOCKED
- current_coverage: partial
- priority: P0
- target_task: 61.5
- target_milestone: M61
- fixture_type: repair-fixture
- notes: critical non-start boundary

### Gap 15
- gap_id: M61-NFG-015
- title: unknown status accepted
- related_risk_id: M61-FP-013
- related_hardening_item_id: M61-CHP-003
- checker_or_runner: `scripts/check-execution-verification-chain.py`
- missing_negative_case: неизвестный FINAL_STATUS принимается
- example_failure_mode: unknown status accepted
- expected_result: BLOCKED
- current_coverage: partial
- priority: P1
- target_task: 61.5
- target_milestone: M61
- fixture_type: repair-fixture
- notes: one focused invalid status case

### Gap 16
- gap_id: M61-NFG-016
- title: checker skipped silently
- related_risk_id: M61-FP-015
- related_hardening_item_id: M61-CHP-015
- checker_or_runner: checker orchestration
- missing_negative_case: обязательный checker не запускался
- example_failure_mode: checker skipped silently accepted
- expected_result: BLOCKED
- current_coverage: weak
- priority: P1
- target_task: M63-planning
- target_milestone: M63
- fixture_type: future-suite-fixture
- notes: needs orchestration layer first

### Gap 17
- gap_id: M61-NFG-017
- title: malformed runner output accepted
- related_risk_id: M61-FP-016
- related_hardening_item_id: M61-CHP-013
- checker_or_runner: `scripts/check-execution-verification-regression.py`
- missing_negative_case: runner JSON без `result` или `exit_code`
- example_failure_mode: malformed runner output accepted
- expected_result: BLOCKED
- current_coverage: partial
- priority: P1
- target_task: 61.5
- target_milestone: M61
- fixture_type: repair-fixture
- notes: strict parsing coverage

### Gap 18
- gap_id: M61-NFG-018
- title: missing non-authority boundary
- related_risk_id: M61-FP-009
- related_hardening_item_id: M61-CHP-006
- checker_or_runner: non-authority checks
- missing_negative_case: удалена обязательная non-authority фраза
- example_failure_mode: missing non-authority boundary accepted
- expected_result: BLOCKED
- current_coverage: partial
- priority: P0
- target_task: 61.5
- target_milestone: M61
- fixture_type: repair-fixture
- notes: exact-string based deterministic case

### Gap 19
- gap_id: M61-NFG-019
- title: completion claimed without evidence
- related_risk_id: M61-FP-012
- related_hardening_item_id: M61-CHP-009
- checker_or_runner: completion/evidence correlation
- missing_negative_case: completion есть, evidence link сломан
- example_failure_mode: completion claimed without evidence
- expected_result: BLOCKED
- current_coverage: partial
- priority: P0
- target_task: 61.5
- target_milestone: M61
- fixture_type: repair-fixture
- notes: deterministic broken-link case

### Gap 20
- gap_id: M61-NFG-020
- title: merge/push/release authorization claimed
- related_risk_id: M61-FP-009
- related_hardening_item_id: M61-CHP-006
- checker_or_runner: non-authority checks
- missing_negative_case: текст с авторизацией merge/push/release
- example_failure_mode: authorization claim accepted
- expected_result: BLOCKED
- current_coverage: partial
- priority: P0
- target_task: 61.5
- target_milestone: M61
- fixture_type: repair-fixture
- notes: explicit forbidden-claim case

## 8. P0 Fixture Gaps
- M61-NFG-001
- M61-NFG-005
- M61-NFG-007
- M61-NFG-008
- M61-NFG-009
- M61-NFG-012
- M61-NFG-013
- M61-NFG-014
- M61-NFG-018
- M61-NFG-019
- M61-NFG-020

## 9. P1 Fixture Gaps
- M61-NFG-002
- M61-NFG-003
- M61-NFG-004
- M61-NFG-006
- M61-NFG-010
- M61-NFG-011
- M61-NFG-015
- M61-NFG-016
- M61-NFG-017

## 10. P2 Fixture Gaps
- none currently mapped as P2 in this hardening pass

## 11. Repair Fixtures Required for 61.5
If 61.5 changes checker behavior, it must add or update minimal focused fixtures for that exact repaired behavior.
These are repair fixtures, not the full M67 false PASS suite.
No checker behavior change without at least one positive or negative validation path.
61.4 must not create those fixtures. It only maps them.

Repair-fixture candidates for 61.5:
- M61-NFG-001, 002, 003, 004, 006, 007, 008, 012, 013, 014, 015, 017, 018, 019, 020

## 12. Deferred Fixture Suite for M67
M67 owns the full false PASS resistance fixture suite.
M61 only identifies fixture gaps and allows minimal repair fixtures when 61.5 changes existing M60 checker behavior.

Deferred as future-suite-fixture:
- M61-NFG-010
- M61-NFG-011
- M61-NFG-016

## 13. Manual Review Cases
- M61-NFG-005 (broad blocker/warning mapping refactor)
- M61-NFG-009 (policy confirmation for human review enforcement wording)

## 14. Non-Authority Boundary
M61 negative fixture gap mapping is not approval.
M61 negative fixture gap mapping does not create fixtures.
M61 negative fixture gap mapping does not repair checkers.
M61 negative fixture gap mapping does not start M62.
M61 negative fixture gap mapping does not validate completed agent tasks as a production gate.
M61 negative fixture gap mapping does not mutate lifecycle state.
M61 negative fixture gap mapping does not authorize merge, push, or release.
Human review remains required.

## 15. Final Status
FINAL_STATUS: M61_NEGATIVE_FIXTURE_GAP_MAP_COMPLETE_WITH_WARNINGS
