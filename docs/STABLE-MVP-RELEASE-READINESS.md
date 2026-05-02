# Stable MVP Release Readiness Contract

## Purpose
Этот документ определяет контракт готовности Stable MVP для AgentOS: какие обязательные условия должны быть выполнены, какие статусы допустимы и что именно блокирует готовность.

No lower gate can override a higher safety gate.

## AgentOS MVP Definition
AgentOS в рамках MVP определяется как:
- Markdown-first guardrail framework
- deterministic validation layer
- controlled lifecycle workflow
- structured guardrail system for AI-assisted coding

MVP-контракт описывает только критерии готовности, а не автоматический релиз.

## Non-Goals
- AgentOS is not an autonomous agent platform.
- AgentOS is not a backend service.
- AgentOS is not a vector database.
- AgentOS is not a RAG platform.
- AgentOS is not a model router.
- AgentOS is not a CI/CD platform.
- AgentOS is not a bug-free output guarantee.

## MVP Required Capabilities
Для статуса готовности должны быть подтверждены:
- единая модель gate-последовательности из M19;
- семантика gate-результатов (PASS/BLOCKED/WARN/ERROR/NOT_RUN/NOT_APPLICABLE);
- стабильные machine-readable маркеры (формат для парсинга скриптами);
- регрессионная защита от bypass (обхода блокировок);
- аудит и smoke-проверки gate-контракта;
- подтверждающие evidence и completion review.

## Release Readiness Gates
Ниже перечислены обязательные gate-проверки с условиями PASS/FAIL.

### DOCUMENTATION_GATE
- Проверяет наличие и согласованность базовой документации M19/M20 readiness.
- Pass condition: required docs существуют и содержат обязательные разделы/правила.
- Fail condition: отсутствует обязательный документ или критическое правило readiness не зафиксировано.

### VALIDATION_GATE
- Проверяет, что обязательные валидаторы и их проверки отрабатывают без критических сбоев.
- Pass condition: required validation commands завершаются успешно и дают ожидаемые маркеры.
- Fail condition: обязательные проверки падают, дают ERROR/BLOCKED/NOT_RUN или маркеры отсутствуют.

### POLICY_GATE
- Проверяет, что policy-границы соблюдаются и блокировки policy не обходятся.
- Pass condition: policy boundary сохранён, блокирующие policy-результаты корректно блокируют поток.
- Fail condition: policy block может быть обойдён, либо policy-сигналы трактуются как PASS при блоке.

### APPROVAL_GATE
- Проверяет, что approval применяется только в пределах policy и не подменяет её.
- Pass condition: approval используется только где допускается policy, и не расширяет полномочия.
- Fail condition: approval override policy block, missing approval трактуется как success.

### APPLY_PIPELINE_GATE
- Проверяет связку preconditions + controlled apply и обязательные gate-маркеры.
- Pass condition: пайплайн выдаёт обязательные маркеры и корректно блокирует unsafe path.
- Fail condition: отсутствуют обязательные маркеры, bypass блокировок, либо unsafe path проходит.

### REGRESSION_GATE
- Проверяет набор regression fixtures против известных bypass-сценариев.
- Pass condition: regression runner PASS, failed cases = 0.
- Fail condition: хотя бы один обязательный regression case не пройден.

### AUDIT_GATE
- Проверяет статический аудит gate-контракта.
- Pass condition: audit script PASS, критических провалов нет.
- Fail condition: audit BLOCKED/ERROR, нарушены обязательные инварианты.

### SMOKE_GATE
- Проверяет сквозной read-only smoke сценарий unified gate-flow.
- Pass condition: smoke PASS и hash guard подтверждает отсутствие мутаций protected paths.
- Fail condition: smoke BLOCKED/ERROR, hash guard изменился, либо usage/traceback принят как PASS.

### EVIDENCE_GATE
- Проверяет полноту и корректность evidence report для milestone.
- Pass condition: evidence report присутствует, содержит обязательные секции и проверяемые результаты.
- Fail condition: evidence отсутствует, неконсистентен, или не подтверждает критические safety условия.

### COMPLETION_REVIEW_GATE
- Проверяет наличие и корректность финального completion review milestone.
- Pass condition: completion review присутствует, использует допустимое финальное решение и фиксирует safety-границы.
- Fail condition: completion review отсутствует/некорректен или делает выводы без обязательных оснований.

## Required Evidence
Для readiness оценки требуются как минимум:
- подтверждение существования M19 source-of-truth артефактов;
- результаты gate contract validator;
- результаты regression runner;
- результаты unified gate audit;
- результаты unified gate smoke;
- evidence report milestone;
- completion review milestone.

Evidence должен быть проверяемым, а не декларативным.

## MVP Readiness Labels
Допустимые readiness labels:
- MVP_READY
- MVP_READY_WITH_WARNINGS
- MVP_NOT_READY
- NEEDS_REVIEW

### Label meanings
- MVP_READY: required docs и required gates проходят; критических safety gap нет; ограничения задокументированы.
- MVP_READY_WITH_WARNINGS: core safety gates проходят, но остаются некритичные gaps; warnings должны быть явно перечислены в evidence/review; warnings не могут ослаблять safety gates.
- MVP_NOT_READY: один или более обязательных gates не проходят, либо safety-контракт нарушен/обходится.
- NEEDS_REVIEW: доказательства неполные, конфликтуют, или требуется ручное решение.

### Label Precedence
Label Precedence, descending priority:
- MVP_NOT_READY
- NEEDS_REVIEW
- MVP_READY_WITH_WARNINGS
- MVP_READY

MVP_NOT_READY > NEEDS_REVIEW > MVP_READY_WITH_WARNINGS > MVP_READY

When multiple label conditions are satisfied simultaneously, the highest-priority label always overrides all lower labels.

No lower label may be assigned if a higher-priority condition is true.

## Gate Result to Label Mapping
| Gate Result | MVP Readiness Label | Notes |
|---|---|---|
| PASS | MVP_READY candidate | All required gates must pass for MVP_READY |
| WARN | MVP_READY_WITH_WARNINGS | Only allowed for non-critical readiness gaps; no safety gate may use WARN to bypass a block |
| BLOCKED | MVP_NOT_READY | Immediate block, no override |
| ERROR | MVP_NOT_READY | Technical failure is not PASS |
| NOT_RUN | MVP_NOT_READY | NOT_RUN is never treated as PASS |
| NOT_APPLICABLE | NEEDS_REVIEW | Allowed only if explicitly justified for this MVP version |

Gate result NOT_RUN maps to MVP_NOT_READY, not NEEDS_REVIEW.

NOT_RUN is a technical block, not an ambiguous result.

Gate result ERROR maps to MVP_NOT_READY, not NEEDS_REVIEW.

ERROR is a failed gate execution, not a successful enforcement result.

## Blocking Conditions
MVP readiness must be blocked when any of the following is true:
- missing M19 gate contract docs;
- missing gate result semantics;
- missing gate output contract;
- failed gate regression runner;
- failed unified gate smoke;
- failed gate audit;
- missing or invalid evidence report;
- unsupported safety boundary;
- any required gate marked NOT_RUN and treated as PASS;
- any gate ERROR treated as PASS;
- any generic traceback or usage error treated as enforcement PASS.

## Relationship to M19 Gate Contract
M20 readiness contract опирается на M19 как на source-of-truth для:
- порядка ворот;
- семантики результатов;
- output markers;
- non-bypass инвариантов;
- regression/audit/smoke доказательств.

MVP readiness cannot override policy blocks.

MVP readiness cannot override missing approval.

MVP readiness cannot override failed preconditions.

MVP readiness cannot treat NOT_RUN validation as PASS.

MVP readiness cannot treat ERROR validation as PASS.

MVP readiness cannot treat missing evidence as success.

MVP readiness cannot legalize unsafe operation after the fact.

## Stable MVP Boundary
Stable MVP boundary фиксирует, что readiness-оценка:
- не создаёт новую safety-layer поверх M19;
- не отменяет и не ослабляет existing gate blocks;
- не переводит BLOCKED/ERROR/NOT_RUN в PASS;
- не разрешает unsafe operation ретроспективно.

## Future Work Explicitly Out of Scope
- implementation release process;
- release scripts;
- package metadata;
- install smoke;
- example project smoke;
- template integrity checker;
- declaration that M20 is complete in this task.
