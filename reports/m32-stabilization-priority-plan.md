# M32 Stabilization Priority Plan

## 1. Purpose

32.6 консолидирует результаты M32 в единый план приоритетов для hardening в M33.

Этот отчёт — план приоритетов, а не реализация.

## 2. M32 Source Documents Reviewed

| Source Document | Exists? | Purpose | Key Findings Imported | Notes |
|---|---|---|---|---|
| `docs/AGENTOS-STABILIZATION-MAP.md` | FOUND | Базовая карта рисков стабилизации | 4 слоя рисков, shared risk register, P0-P3 рамка | Использован как исходная карта рисков |
| `docs/AGENTOS-WORKFLOW-REVIEW.md` | FOUND | Риски рабочих переходов и gate-логики | Jump risks, human checkpoints, evidence freshness gaps | Использован для P1/P0 workflow-рисков |
| `docs/SCRIPT-RESPONSIBILITY-REVIEW.md` | FOUND | Границы ролей скриптов | Drift risks, result/exit несогласованность, approval boundary | Использован для P0/P2 script-рисков |
| `docs/NEGATIVE-FIXTURE-COVERAGE.md` | FOUND | Карта покрытия негативных сценариев | Missing/PARTIAL coverage по критичным guard | Использован для очередности M33.1 |
| `docs/STABILIZATION-AUDIT-DESIGN.md` | FOUND | Дизайн будущего stabilization audit | Fail-closed, suite design, JSON/report contracts | Использован для M33.8 и release gates |

Если любой источник отсутствует, план должен иметь статус partial. В текущем контексте все 5 источников найдены.

## 3. Priority Model

- `P0` — false OK / bypass / fake approval.
- `P1` — workflow jump / stale evidence / unclear command.
- `P2` — duplicated logic / weak docs / missing examples.
- `P3` — polish / future productization.

Правила принятия решений:
- P0 должен быть закрыт до release readiness.
- P1 должен быть закрыт до MVP release readiness.
- P2 можно объединять в батчи M33.
- P3 переносится в M34+ (кроме дешёвых и безопасных улучшений).

## 4. Consolidated Findings Table

| Finding ID | Source | Area | Finding | Consequence | Severity | Recommended Fix | Suggested M33 Task | Dependencies |
|---|---|---|---|---|---|---|---|---|
| CF-001 | 32.1/32.2/32.3 | false green / fail-closed | `UNKNOWN` может стать фактически безопасным в цепочке решений | Ложный зелёный статус | P0 | Жёсткий fail-closed контракт на result-семантику | 33.2 | 33.1 |
| CF-002 | 32.2/32.5 | evidence freshness | Stale evidence может пройти в completion | DONE на старых данных | P0 | Ввести обязательные freshness-checks | 33.4 | 33.2 |
| CF-003 | 32.2/32.4 | context requirement | Возможен запуск без валидного Context Pack | Работа вне контекста | P0 | Правило No Context Pack -> No Execution | 33.6 | 33.2 |
| CF-004 | 32.3/32.5 | approval boundary | Audit/отчёт/контекст могут ошибочно считаться approval | Обход human gate | P0 | Явное отделение approval authority | 33.5 | 33.2 |
| CF-005 | 32.4 | runtime boundary | Опасные команды/прямой push/защищённые записи должны блокироваться всегда | Критичный обход безопасности | P0 | Усилить P0 negative fixtures + проверку guard-цепочки | 33.1 | none |
| CF-006 | 32.3 | script responsibility | Wrapper/renderer/tutor могут дрейфовать в authority-роль | Ложное ощущение допуска | P0 | Контракты ролей + drift fixtures | 33.7 | 33.1, 33.2 |
| CF-007 | 32.2 | workflow gates | Можно перескочить review/audit/completion gates | Неполная проверка перед DONE | P1 | Упростить маршрут и обязательные gate-переходы | 33.9 | 33.2, 33.4 |
| CF-008 | 32.2 | command clarity | Нет единой очевидной команды "check everything" | Пропуски проверок | P1 | Единый проверочный путь (без обхода gate) | 33.9 | 33.8 |
| CF-009 | 32.3 | exit codes | Неодинаковая интерпретация exit/result между скриптами | Ошибки автоматизации | P2 | Нормализовать exit/result контракты | 33.3 | 33.2 |
| CF-010 | 32.3/32.5 | JSON output | Риск расхождения JSON и Markdown статусов | Неверные выводы инструментов | P2 | Стабильный JSON контракт + валидация соответствия | 33.3 | 33.8 |
| CF-011 | 32.4 | negative fixtures | Нет полного покрытия критичных drift/false-green кейсов | Незамеченные регрессии | P1 | Достроить P0/P1 негативные фикстуры | 33.1 | none |
| CF-012 | 32.5 | audit design | Stabilization audit пока только дизайн | Нельзя проверить целостно одним прогоном | P1 | Реализовать unified stabilization audit | 33.8 | 33.1-33.7 |
| CF-013 | 32.2 | human/product clarity | `next`/warning могут звучать как разрешение | Ошибочные действия человека | P1 | Жёсткие формулировки и UX-границы | 33.9 | 33.5 |
| CF-014 | 32.3 | script ownership | Не везде закреплён "one meaning - one owner" | Дубли логики и конфликт решений | P2 | Формализовать ownership matrix в runtime-контрактах | 33.7 | 33.3 |

## 5. P0 Findings

### P0-1: `UNKNOWN` becoming `PASS`
- Почему опасно: создаёт ложное разрешение на продолжение.
- Как детектировать: негативные цепочки status->next->completion с `UNKNOWN`.
- Что реализовать в M33: fail-closed трактовка result + запрет конверсии `UNKNOWN` в `PASS`.
- Что пока не делать: автоматический self-heal/автоисправления.

### P0-2: Fake approval accepted
- Почему опасно: обход человеческого контроля.
- Как детектировать: фикстуры fake/agent-generated approval, scope mismatch, expired approval.
- Что реализовать в M33: строгая проверка источника/области/срока approval.
- Что пока не делать: новые approval workflow-продукты.

### P0-3: Audit PASS treated as approval
- Почему опасно: проверка подменяет решение человека.
- Как детектировать: кейс "audit PASS + no human decision" должен оставаться BLOCKED/NEEDS_REVIEW.
- Что реализовать в M33: явная non-authorization семантика audit.
- Что пока не делать: автозавершение задач по audit.

### P0-4: Stale evidence allows completion
- Почему опасно: задача закрывается по устаревшим данным.
- Как детектировать: completion при старом `verification/audit/evidence`.
- Что реализовать в M33: freshness gates в completion checks.
- Что пока не делать: автоматический rewrite evidence.

### P0-5: No Context Pack but execution allowed
- Почему опасно: выполнение вне проверенного контекста.
- Как детектировать: запуск с отсутствующим/невалидным context pack.
- Что реализовать в M33: mandatory context gate.
- Что пока не делать: автогенерация context pack в обход review.

### P0-6: Direct git push / dangerous command / protected write allowed
- Почему опасно: немедленный риск безопасности/потери контроля.
- Как детектировать: negative fixtures на push/force-push/rm/path traversal.
- Что реализовать в M33: унификация блокировок runtime guards.
- Что пока не делать: новые команды автоматизации git.

### P0-7: Wrapper downgrades BLOCKED to OK / tutor(decision card) creates approval / renderer hides BLOCKED
- Почему опасно: визуальный/маршрутизационный слой искажает риск.
- Как детектировать: drift fixtures на wrapper/renderer/tutor.
- Что реализовать в M33: границы ответственности и fail-closed визуализация.
- Что пока не делать: UI/TUI продуктовые расширения.

## 6. P1 Findings

- Неясная первая команда и отсутствие единого "check-everything" пути.
  - Влияние на пользователя: повышает вероятность пропуска шага.
  - Влияние на агента: разные траектории, больше ошибок последовательности.
  - Шаг hardening: единый проверочный маршрут с прозрачными gate.
  - Зависимость: после P0 fail-closed и approval boundary.

- Возможность skip review/audit в потоке.
  - Влияние на пользователя: DONE без достаточной проверки.
  - Влияние на агента: сложнее доказать корректность завершения.
  - Шаг hardening: обязательные блокеры на review/audit перед completion.
  - Зависимость: P0 freshness + semantics.

- Нечёткая свежесть evidence / completion не всегда связан с audit result.
  - Влияние на пользователя: доверие к устаревшей информации.
  - Влияние на агента: ложное PASS при старых отчётах.
  - Шаг hardening: формализованные freshness-checks.
  - Зависимость: P0 stale-evidence prevention.

- Retry без review причины сбоя.
  - Влияние на пользователя: циклические повторения без прогресса.
  - Влияние на агента: рост шума и неопределённости.
  - Шаг hardening: pre-retry check с обязательным reason.
  - Зависимость: может идти параллельно с P1 workflow hardening.

- `next safe action` звучит как исполняемая команда; warning воспринимается как pass.
  - Влияние на пользователя: неправильные действия.
  - Влияние на агента: смешение guidance и authorization.
  - Шаг hardening: текстовые и семантические ограничения для next/warn.
  - Зависимость: P0 approval boundary.

## 7. P2 Findings

- дубли и расхождение result names;
- непоследовательные exit code conventions;
- нехватка примеров expected-result для части fixture-наборов;
- слабые/разрозненные справочные описания команд;
- неявная ownership-граница некоторых скриптов;
- риск Markdown/JSON mismatch.

Рекомендация: объединить эти работы в 1-2 M33 батча после закрытия P0/P1.

## 8. P3 Findings

К M34+ или позже:
- product polish;
- пользовательские режимы/расширенный tutor language;
- packaging;
- UI/TUI/web UI;
- self-heal;
- recovery protocol;
- shadow branching;
- git checkpoints.

Эти элементы не должны отвлекать M33 от hardening.

## 9. Recommended M33 Structure

### 33.1 - P0 Negative Fixtures
- Purpose: закрыть критичные негативные сценарии P0.
- Expected artifact: расширенный набор `tests/fixtures/negative/*` + runner coverage.
- Priority: P0.
- Dependencies: none.
- Non-goals: без изменения UX/упаковки.

### 33.2 - Fail-Closed Result Semantics
- Purpose: унифицировать блокирующую трактовку `UNKNOWN/STALE/BLOCKED/NOT_FOUND/NEEDS_REVIEW`.
- Expected artifact: контракт result-семантики + enforcement в проверках.
- Priority: P0.
- Dependencies: 33.1.
- Non-goals: без новых CLI-команд.

### 33.3 - Exit Code and JSON Consistency
- Purpose: согласовать exit-коды и JSON ключи между проверками.
- Expected artifact: единый exit/json contract + проверки соответствия.
- Priority: P2 (с опорой на P0).
- Dependencies: 33.2.
- Non-goals: без продуктовых UI-изменений.

### 33.4 - Evidence Freshness Checks
- Purpose: блокировать completion на stale evidence.
- Expected artifact: freshness-gates и негативные кейсы stale evidence.
- Priority: P0/P1.
- Dependencies: 33.2.
- Non-goals: без автоперезаписи отчётов.

### 33.5 - Approval Boundary Hardening
- Purpose: исключить подмену approval audit/report/tutor-результатами.
- Expected artifact: approval-boundary checks + fixtures.
- Priority: P0.
- Dependencies: 33.2.
- Non-goals: без нового approval workflow-продукта.

### 33.6 - Context Requirement Hardening
- Purpose: enforce правило no-context-no-execution.
- Expected artifact: context-gate checks + negative fixtures.
- Priority: P0.
- Dependencies: 33.2.
- Non-goals: без автогенерации context pack.

### 33.7 - Script Responsibility Fixes
- Purpose: устранить drift ролей status/explain/next/renderer/wrapper.
- Expected artifact: ответственность скриптов закреплена тестами и контрактами.
- Priority: P1/P2.
- Dependencies: 33.1, 33.2, 33.3.
- Non-goals: без расширения UI.

### 33.8 - Unified Stabilization Audit Runner
- Purpose: реализовать дизайн M32.5 в единый аудит.
- Expected artifact: `scripts/audit-agentos-stabilization.py` + JSON/Markdown output.
- Priority: P1.
- Dependencies: 33.1-33.7.
- Non-goals: без auto-fix.

### 33.9 - Workflow Simplification / Check-Everything Path
- Purpose: убрать двусмысленность команд и перескоки между gate.
- Expected artifact: единый безопасный маршрут проверок.
- Priority: P1.
- Dependencies: 33.5, 33.8.
- Non-goals: без новых продуктовых интерфейсов.

### 33.10 - M33 Evidence Report and Completion Review
- Purpose: финальная доказательная сборка M33 и проверка готовности.
- Expected artifact: evidence report + completion review с открытыми рисками.
- Priority: P1/P2.
- Dependencies: 33.4, 33.8, 33.9.
- Non-goals: без релизного автодеплоя.

## 10. Implementation Order

| Step | M33 Task | Why First | Blocks | Validation Needed |
|---|---|---|---|---|
| 1 | 33.1 P0 Negative Fixtures | Даёт базу для проверки критичных рисков | Все последующие проверки | Negative fixture runner pass/fail correctness |
| 2 | 33.2 Fail-Closed Result Semantics | Закрывает false green ядро | 33.3, 33.4, 33.5, 33.6 | Contract tests for UNKNOWN/STALE/BLOCKED |
| 3 | 33.5 Approval Boundary Hardening | Убирает критичный bypass | 33.9, 33.10 | Fake approval fixtures + human-gate checks |
| 4 | 33.4 Evidence Freshness Checks | Блокирует stale completion | 33.10 | Freshness fixtures + completion gates |
| 5 | 33.6 Context Requirement Hardening | Гарантирует no-context-no-execution | 33.9 | Context missing/invalid fixtures |
| 6 | 33.3 Exit Code and JSON Consistency | Делает автоматизацию надёжной | 33.8 | Exit matrix + JSON schema checks |
| 7 | 33.7 Script Responsibility Fixes | Убирает drift и дубли ролей | 33.8, 33.9 | Responsibility drift fixtures |
| 8 | 33.8 Unified Stabilization Audit Runner | Собирает всё в единый аудит | 33.9, 33.10 | Suite-level pass/fail + report parity |
| 9 | 33.9 Workflow Simplification | Снижает ошибки человека/агента | 33.10 | End-to-end gate route checks |
| 10 | 33.10 Evidence Report and Completion Review | Финальная верификация M33 | M34 start gate | Completion readiness + risk register closure |

## 11. Release Readiness Gate

M34 может стартовать только если:
- нет открытых P0 stabilization findings;
- P1 либо исправлены, либо явно приняты с обоснованием;
- дизайн stabilization audit имеет реализованный путь;
- критичные negative fixtures существуют или включены как blocking M33 tasks;
- exit/result semantics достаточно согласованы для аудита;
- есть определённая проверка freshness evidence;
- approval boundary не двусмысленна.

## 12. Risk Acceptance Rules

- P0 нельзя тихо откладывать.
- P1 требует документированного обоснования.
- P2 можно батчить.
- P3 можно переносить в M34+.
- Любой отложенный риск должен иметь owner, reason, revisit trigger.

## 13. M32 Completion Assessment

**Status: `M32_PRIORITY_PLAN_COMPLETE`**

Обоснование:
- все 5 документов M32.1-M32.5 найдены и использованы;
- консолидированный P0/P1/P2/P3 план сформирован;
- предложен порядок реализации M33;
- границы "план, не реализация" соблюдены.

## 14. Non-Goals

32.6 не делает:
- реализацию M33;
- создание scripts;
- создание fixtures;
- модификацию validators;
- модификацию runtime guards;
- модификацию CI;
- исправление workflow gaps в коде;
- добавление approval flow;
- self-heal;
- recovery protocol;
- shadow branches;
- git checkpoints;
- packaging;
- UI/TUI/web UI.

## 15. Final Boundary

32.6 приоритизирует stabilization-работу.
32.6 не реализует stabilization-работу.
M33 начинается только после существования M32 priority plan.
