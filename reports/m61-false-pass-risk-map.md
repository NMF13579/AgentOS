# M61 False PASS Risk Map

## 1. Purpose
Зафиксировать риски ложного PASS в фундаменте M60 и определить, какие риски безопасно усиливать в M61, а какие нужно перенести в M62-M67.

## 2. Inputs Reviewed
- `reports/m61-m60-completion-intake.md`
- `docs/POST-M60-HARDENING-ARCHITECTURE.md`
- `reports/m60-completion-review.md`
- `reports/m60-cleanup-evidence-report.md`
- `reports/m60-cleanup-action-review.json`
- `reports/m60-cleanup-integration-summary.md`
- `docs/EXECUTION-VERIFICATION-REGISTRY.md` (checker-specific context)
- `docs/EXECUTION-VERIFICATION-REUSABLE-CHECKS.md` (checker-specific context)
- `docs/EXECUTION-VERIFICATION-REGRESSION-RUNNER.md` (checker-specific context)
- `scripts/check-execution-verification-registry.py` (checker-specific context)
- `scripts/check-execution-verification-chain.py` (checker-specific context)
- `scripts/check-execution-verification-regression.py` (checker-specific context)

## 3. Dependency Status
- `reports/m61-m60-completion-intake.md`: present, `M61_INTAKE_READY_WITH_WARNINGS`
- `docs/POST-M60-HARDENING-ARCHITECTURE.md`: present, `M61_HARDENING_ARCHITECTURE_DEFINED`
- required M60 inputs: present and usable
- `reports/m60-cleanup-action-review.json`: JSON parseable
- dependency blocker for risk mapping: not found

## 4. False PASS Definition
A false PASS occurs when AgentOS reports, preserves, or allows a PASS-like result even though required evidence is missing, malformed, stale, contradicted, unsafe, unauthorized, or insufficient.

Warnings must not be silently converted into PASS.
Blockers must not be downgraded to warnings without explicit policy.
Unknown status must not be treated as PASS.
Missing evidence must not be treated as PASS.
Evidence is not approval.
PASS is not approval.
Human review remains required.

## 5. Risk Severity Model
- LOW — false confidence possible but limited to documentation clarity or local warning quality.
- MEDIUM — false confidence may affect M61 hardening decisions but does not directly authorize task completion.
- HIGH — false confidence may allow unsafe transition into M62 or hide broken M60 foundation.
- CRITICAL — false confidence may imply approval, hide blocker state, bypass human review, or authorize lifecycle / merge / push / release semantics.

## 6. Risk Map
### Risk 1 — missing artifact but PASS
- risk_id: M61-FP-001
- title: missing artifact but PASS
- description: обязательный файл отсутствует, но итог остаётся PASS-подобным.
- affected_component: completion/integration evidence chain
- false_pass_mechanism: отсутствие жёсткой проверки наличия всех обязательных входов
- example_failure_mode: удалён mandatory report, но агрегатор принимает старое состояние как валидное
- current_detection: частично есть в M60 checkers
- severity: CRITICAL
- recommended_action: усилить fail-closed проверку обязательных файлов
- target_milestone: M61
- m61_action: SAFE_REPAIR_CANDIDATE

### Risk 2 — malformed JSON but PASS
- risk_id: M61-FP-002
- title: malformed JSON but PASS
- description: JSON повреждён, но обрабатывается как допустимый.
- affected_component: action/integration/evidence parsing
- false_pass_mechanism: парсинг ошибки не приводит к блокировке
- example_failure_mode: `json.loads` ошибается, но итог не становится BLOCKED
- current_detection: есть в части проверок
- severity: CRITICAL
- recommended_action: унифицированная блокировка при ошибке парсинга
- target_milestone: M61
- m61_action: SAFE_REPAIR_CANDIDATE

### Risk 3 — warning hidden as PASS
- risk_id: M61-FP-003
- title: warning hidden as PASS
- description: предупреждения есть, но итог ошибочно PASS.
- affected_component: status mapping
- false_pass_mechanism: некорректная агрегация warnings
- example_failure_mode: warnings есть в runtime checker output, а final status = PASS
- current_detection: частично
- severity: HIGH
- recommended_action: закрепить правило PASS_WITH_WARNINGS при наличии warnings
- target_milestone: M61
- m61_action: SAFE_REPAIR_CANDIDATE

### Risk 4 — blocker downgraded to warning
- risk_id: M61-FP-004
- title: blocker downgraded to warning
- description: блокер снижен до warning без политики.
- affected_component: status mapping
- false_pass_mechanism: ручная/нестрогая нормализация статусов
- example_failure_mode: blocker list непустой, но final status с warning
- current_detection: частично
- severity: CRITICAL
- recommended_action: жёсткое правило blocker => BLOCKED
- target_milestone: M61
- m61_action: SAFE_REPAIR_CANDIDATE

### Risk 5 — fake validation output accepted
- risk_id: M61-FP-005
- title: fake validation output accepted
- description: поддельный output проверки принимается как настоящий.
- affected_component: runtime correlation
- false_pass_mechanism: нет строгой привязки к реальному запуску checker
- example_failure_mode: вручную подставленный JSON трактуется как runtime truth
- current_detection: ограниченно
- severity: HIGH
- recommended_action: усилить проверку источника runtime output
- target_milestone: M62
- m61_action: DEFER_TO_M62

### Risk 6 — registry stale but accepted
- risk_id: M61-FP-006
- title: registry stale but accepted
- description: устаревший registry принимается как актуальный.
- affected_component: registry checker flow
- false_pass_mechanism: недостаточный контроль актуальности связанного набора артефактов
- example_failure_mode: старый registry с PASS без проверки соответствия контексту
- current_detection: частично
- severity: HIGH
- recommended_action: усилить stale-detection без смены семантики M60
- target_milestone: M61
- m61_action: PLAN_HARDENING

### Risk 7 — evidence manually written without runtime correlation
- risk_id: M61-FP-007
- title: evidence manually written without runtime correlation
- description: evidence отчёт написан вручную и не совпадает с runtime фактами.
- affected_component: evidence/integration correlation
- false_pass_mechanism: недостаточный контроль соответствия JSON-блоков runtime output
- example_failure_mode: текст и JSON расходятся, но статус остаётся PASS-like
- current_detection: есть, но не везде симметрично
- severity: HIGH
- recommended_action: усилить корреляцию runtime/result across artifacts
- target_milestone: M61
- m61_action: SAFE_REPAIR_CANDIDATE

### Risk 8 — protected path modified but not detected
- risk_id: M61-FP-008
- title: protected path modified but not detected
- description: запрещённый путь изменён, но это не замечено.
- affected_component: protected path checks
- false_pass_mechanism: неполный список путей или неполная проверка git diff
- example_failure_mode: изменение вне scope не попало в protected_paths.modified_by_this_task
- current_detection: есть, но возможны пробелы
- severity: CRITICAL
- recommended_action: усилить детект защищённых путей для M60 форматов
- target_milestone: M61
- m61_action: SAFE_REPAIR_CANDIDATE

### Risk 9 — non-authority boundary removed
- risk_id: M61-FP-009
- title: non-authority boundary removed
- description: удалены обязательные фразы про отсутствие права одобрять.
- affected_component: non-authority boundary validation
- false_pass_mechanism: слабая проверка обязательных boundary statements
- example_failure_mode: отчёт без ключевой boundary фразы проходит
- current_detection: частично
- severity: CRITICAL
- recommended_action: усилить обязательную проверку non-authority блоков
- target_milestone: M61
- m61_action: SAFE_REPAIR_CANDIDATE

### Risk 10 — human_review_required false accepted
- risk_id: M61-FP-010
- title: human_review_required false accepted
- description: допускается состояние, где требование human review фактически снято.
- affected_component: policy boundary checks
- false_pass_mechanism: отсутствие явной проверки на сохранение human review requirement
- example_failure_mode: итоговый отчёт без "Human review remains required." трактуется как корректный
- current_detection: частично
- severity: CRITICAL
- recommended_action: добавить явный контроль этого требования во всех итоговых артефактах
- target_milestone: M61
- m61_action: PLAN_HARDENING

### Risk 11 — downstream artifact created early
- risk_id: M61-FP-011
- title: downstream artifact created early
- description: артефакт следующего этапа создан преждевременно.
- affected_component: no-premature-downstream checks
- false_pass_mechanism: фазовая логика (phase-aware) неполная
- example_failure_mode: ранний артефакт M62 не приводит к BLOCKED
- current_detection: есть, но зависимо от фазы
- severity: HIGH
- recommended_action: сохранить строгую фазовую матрицу для M61 и M62
- target_milestone: M61
- m61_action: SAFE_REPAIR_CANDIDATE

### Risk 12 — completion claimed without evidence
- risk_id: M61-FP-012
- title: completion claimed without evidence
- description: completion report заявляет завершение без валидной evidence-основы.
- affected_component: completion/evidence dependency chain
- false_pass_mechanism: отсутствие жёсткой зависимости completion от evidence/action/integration
- example_failure_mode: completion есть, evidence отсутствует/некорректен
- current_detection: частично
- severity: HIGH
- recommended_action: усилить dependency checks и корреляцию источников
- target_milestone: M61
- m61_action: SAFE_REPAIR_CANDIDATE

### Risk 13 — unknown status accepted
- risk_id: M61-FP-013
- title: unknown status accepted
- description: неизвестный статус принимается как допустимый.
- affected_component: status parser/validator
- false_pass_mechanism: не fail-closed обработка незнакомых статусных значений
- example_failure_mode: `FINAL_STATUS: SOMETHING_NEW` не блокирует процесс
- current_detection: частично
- severity: HIGH
- recommended_action: блокировать unknown status везде по умолчанию
- target_milestone: M61
- m61_action: SAFE_REPAIR_CANDIDATE

### Risk 14 — missing final status accepted
- risk_id: M61-FP-014
- title: missing final status accepted
- description: отсутствует итоговый статус, но результат всё равно PASS-like.
- affected_component: report completeness checks
- false_pass_mechanism: неполная валидация наличия FINAL_STATUS
- example_failure_mode: отчёт без FINAL_STATUS принят как валидный
- current_detection: частично
- severity: HIGH
- recommended_action: обязательный FINAL_STATUS и строгая проверка уникальности
- target_milestone: M61
- m61_action: SAFE_REPAIR_CANDIDATE

### Risk 15 — checker skipped silently
- risk_id: M61-FP-015
- title: checker skipped silently
- description: обязательная проверка не запускалась, но это не отражено.
- affected_component: runtime execution tracking
- false_pass_mechanism: нет полного учёта обязательных запусков
- example_failure_mode: один из checker runtime outputs отсутствует, но итог не блокируется
- current_detection: ограниченно
- severity: HIGH
- recommended_action: усилить обязательность и трассировку запуска checker
- target_milestone: M62
- m61_action: DEFER_TO_M62

### Risk 16 — malformed runner output accepted
- risk_id: M61-FP-016
- title: malformed runner output accepted
- description: раннер выдаёт поломанный JSON/поля, но это принимается.
- affected_component: runner output validation
- false_pass_mechanism: слабая схема валидации runtime output
- example_failure_mode: отсутствует `exit_code`, но отчёт трактует запуск как успешный
- current_detection: частично
- severity: HIGH
- recommended_action: формализовать строгую проверку структуры runtime outputs
- target_milestone: M61
- m61_action: PLAN_HARDENING

### Risk 17 — premature M61 completion artifact accepted
- risk_id: M61-FP-017
- title: premature M61 completion artifact accepted
- description: итоговые M61 артефакты появляются раньше нужной задачи, но процесс это не блокирует.
- affected_component: M61 phase boundary checks
- false_pass_mechanism: неполный контроль по ожидаемым задачам M61
- example_failure_mode: `reports/m61-completion-review.md` создан слишком рано, но chain остаётся PASS-like
- current_detection: ограниченно
- severity: HIGH
- recommended_action: усилить проверку преждевременных M61 артефактов
- target_milestone: M61
- m61_action: SAFE_REPAIR_CANDIDATE

### Risk 18 — premature M62 artifact accepted
- risk_id: M61-FP-018
- title: premature M62 artifact accepted
- description: M62 артефакт существует слишком рано, но не фиксируется как блокер.
- affected_component: M61/M62 transition boundary checks
- false_pass_mechanism: слабый path-based контроль переходной границы
- example_failure_mode: файл с `m62` в пути есть, но итог не BLOCKED
- current_detection: частично
- severity: CRITICAL
- recommended_action: усилить строгую блокировку для M62-артефактов до разрешённого этапа
- target_milestone: M61
- m61_action: SAFE_REPAIR_CANDIDATE

## 7. M61 Safe Repair Candidates
Кандидаты на безопасный ремонт в M61 (без смены семантики M56-M60):
- M61-FP-001
- M61-FP-002
- M61-FP-003
- M61-FP-004
- M61-FP-007
- M61-FP-008
- M61-FP-009
- M61-FP-011
- M61-FP-012
- M61-FP-013
- M61-FP-014
- M61-FP-017
- M61-FP-018

## 8. Deferred Risks for M62-M67
Риски, которые лучше вести в следующих этапах:
- M61-FP-005 -> M62
- M61-FP-015 -> M62
- M61-FP-006 -> M61 (plan first, possibly continue in M62 if broader changes needed)
- M61-FP-010 -> M61 (requires policy-wide consistency pass)
- M61-FP-016 -> M61 (plan hardening, may extend to M62)

## 9. Manual Review Required
Нужен ручной контроль (manual review) по зонам:
- интерпретация тяжести warnings при выборе M61 vs M62,
- подтверждение, что усиления не меняют смысл PASS/PASS_WITH_WARNINGS/BLOCKED,
- подтверждение, что non-authority границы не ослаблены.

## 10. Non-Authority Boundary
M61 false PASS risk mapping is not approval.
M61 false PASS risk mapping does not repair checkers.
M61 false PASS risk mapping does not start M62.
M61 false PASS risk mapping does not validate completed agent tasks as a production gate.
M61 false PASS risk mapping does not mutate lifecycle state.
M61 false PASS risk mapping does not authorize merge, push, or release.
Human review remains required.

## 11. Final Status
FINAL_STATUS: M61_FALSE_PASS_RISK_MAP_COMPLETE_WITH_WARNINGS
