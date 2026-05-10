# Stabilization Audit Design (M32.5)

## Purpose

M32.5 проектирует будущий stabilization audit до реализации в M33.

Этот документ — дизайн аудита, а не реализация аудита.

## Audit Principles

- audit по умолчанию read-only (только чтение);
- audit проверяет evidence, структуру, согласованность и safety boundaries;
- audit должен fail-closed на `UNKNOWN`;
- audit не должен мутировать файлы;
- audit не должен одобрять действия;
- audit не должен генерировать human approval;
- audit не должен авторизовать execution;
- audit не должен авторизовать commit/push/merge/release/deployment;
- `PASS` в audit значит только «проверки пройдены», а не «задача одобрена».

Обязательное правило: **Audit PASS is not approval.**

## Proposed Future Audit Command

Дизайн-цель (не реализуется в 32.5):

```bash
python3 scripts/audit-agentos-stabilization.py
python3 scripts/audit-agentos-stabilization.py --json
python3 scripts/audit-agentos-stabilization.py --explain
```

Опциональная интеграция в будущем (только как дизайн):

```bash
python3 scripts/audit-agentos.py stabilization
```

## Audit Input Sources

| Input Area | Example Files / Directories | Purpose | Required? | Missing Behavior |
|---|---|---|---|---|
| Stabilization map | `docs/AGENTOS-STABILIZATION-MAP.md` | Базовая карта рисков M32.1 | Yes | `NOT_FOUND`/`NEEDS_REVIEW` |
| Workflow review | `docs/AGENTOS-WORKFLOW-REVIEW.md` | Риски переходов и gate-path | Yes | `NOT_FOUND`/`NEEDS_REVIEW` |
| Script responsibility review | `docs/SCRIPT-RESPONSIBILITY-REVIEW.md` | Границы ролей скриптов | Yes | `NOT_FOUND`/`NEEDS_REVIEW` |
| Negative fixture coverage | `docs/NEGATIVE-FIXTURE-COVERAGE.md` | Карта покрытия негативных сценариев | Yes | `NOT_FOUND`/`NEEDS_REVIEW` |
| Task contracts | `tasks/active-task.md`, `tasks/*.md` | Проверка scope и допусков | Yes | `FAIL`/`UNKNOWN` |
| Context packs | `reports/context-pack.md`, `reports/context-selection-record.md` | Проверка актуальности контекста | Yes | `STALE`/`NOT_FOUND` |
| Verification reports | `reports/verification.md` | Доказательства выполнения | Conditional | `STALE`/`NEEDS_REVIEW` |
| Evidence reports | `reports/*evidence*.md` | Подтверждение шагов | Conditional | `NOT_FOUND`/`STALE` |
| Audit reports | `reports/audit.md` | Согласованность с текущим состоянием | Conditional | `STALE`/`UNKNOWN` |
| Schemas | `schemas/` | Контракт структуры | Yes | `NOT_FOUND`/`FAIL` |
| Validators | `scripts/validate-*.py` | Источник ожидаемых проверок | Yes | `NOT_FOUND`/`NEEDS_REVIEW` |
| Fixtures | `tests/fixtures/` | Источник ожидаемого тестового покрытия | Conditional | `UNKNOWN`/`NEEDS_REVIEW` |
| Negative fixtures | `tests/fixtures/negative/` + domain fixtures | Проверка fail-closed сценариев | Yes | `MISSING`/`NEEDS_REVIEW` |
| Runtime guard outputs | `agentos-*-guard` results/logs if present | Проверка границ runtime | Conditional | `UNKNOWN`/`NEEDS_REVIEW` |
| Workflow files | `workflow/MAIN.md`, `state/MAIN.md`, `quality/MAIN.md` | Проверка gate-логики и переходов | Yes | `NOT_FOUND`/`FAIL` |
| Policies | `core-rules/MAIN.md`, `security/MAIN.md`, policy docs | Нормы безопасности и authority | Yes | `NOT_FOUND`/`FAIL` |
| Human decision / approval records | `tests/fixtures/human-gate/*`, task approval markers | Граница «решение человека» | Conditional | `NEEDS_REVIEW`/`UNKNOWN` |

Принцип для missing: по умолчанию `MISSING`/`UNKNOWN`/`NEEDS_REVIEW`, не `PASS`.

## Audit Suite Design

### A. Stabilization Map Suite

Проверяет:
- существует stabilization map;
- есть 4 слоя;
- есть shared risk register;
- есть определения `P0/P1/P2/P3`;
- есть follow-up map.

### B. Workflow Review Suite

Проверяет:
- есть workflow path;
- есть gate analysis;
- есть human checkpoint review;
- есть evidence freshness review;
- есть command clarity review;
- есть jump risks.

### C. Script Responsibility Suite

Проверяет:
- есть script inventory;
- есть responsibility boundaries;
- есть result semantics;
- есть exit code semantics;
- есть mutation boundary;
- есть approval authority boundary.

### D. Negative Coverage Suite

Проверяет:
- есть coverage inventory;
- есть critical guard matrix;
- есть expected fixture structure;
- есть expected runner behavior;
- есть coverage gaps.

### E. False Green / Fail-Closed Suite

Должен выявлять:
- `UNKNOWN` treated as `PASS`;
- `STALE` treated as `PASS`;
- missing report treated as `PASS`;
- damaged report accepted;
- warning treated as approval;
- blocked subsystem downgraded to `OK`.

### F. Evidence Freshness Suite

Должен выявлять:
- report относится к другой задаче;
- report без `task_id`;
- report без commit/state reference (если требуется);
- report старее текущего task state;
- completion review без ссылки на свежие evidence;
- evidence изменены после completion без amendment.

### G. Approval Boundary Suite

Должен выявлять:
- fake approval accepted;
- agent-generated approval accepted;
- checklist treated as approval;
- tutor explanation treated as approval;
- audit `PASS` treated as approval;
- context pack treated as approval;
- evidence report treated as approval.

### H. Runtime Boundary Suite

Должен выявлять:
- forbidden command allowed;
- dangerous command allowed;
- direct git push allowed;
- protected write allowed;
- unknown command allowed;
- runtime guard ambiguous status;
- wrapper converts `BLOCKED` to allowed.

### I. Human/Product Safety Suite

Должен выявлять:
- `BLOCKED` softened into warning;
- next safe action sounds like execute;
- decision card lacks consequence;
- risk is hidden;
- tutor lowers risk;
- user-facing text creates false control.

## Result Semantics

Машинные результаты:
- `PASS`
- `PASS_WITH_WARNINGS`
- `WARN`
- `FAIL`
- `BLOCKED`
- `UNKNOWN`
- `STALE`
- `NOT_FOUND`
- `NEEDS_REVIEW`

Смысл:
- `PASS` = машинная проверка пройдена;
- `PASS_WITH_WARNINGS` = только неблокирующие предупреждения;
- `WARN` сам по себе не авторизует переход;
- `FAIL` блокирует;
- `BLOCKED` блокирует;
- `UNKNOWN` блокирует;
- `STALE` блокирует completion;
- `NOT_FOUND` блокирует, если артефакт обязателен;
- `NEEDS_REVIEW` требует human review.

Обязательное правило: `UNKNOWN`, `STALE`, `BLOCKED`, `NOT_FOUND`, `NEEDS_REVIEW` никогда не становятся `PASS`.

## Exit Code Semantics

Будущая семантика exit-кодов:
- `exit 0` только для `PASS` или `PASS_WITH_WARNINGS`;
- `exit 1` для `FAIL`, `BLOCKED`, `UNKNOWN`, `STALE`, required `NOT_FOUND`, `NEEDS_REVIEW`, invalid state.

Правило: неоднозначный safety-result не может завершаться с `exit 0`.

## JSON Output Contract

Будущая форма JSON:

```json
{
  "result": "PASS|PASS_WITH_WARNINGS|FAIL|BLOCKED|UNKNOWN|STALE|NEEDS_REVIEW",
  "suites": [
    {
      "name": "workflow-review",
      "result": "PASS",
      "findings": []
    }
  ],
  "summary": {
    "p0": 0,
    "p1": 0,
    "p2": 0,
    "p3": 0
  }
}
```

Правила:
- JSON для автоматизации;
- Markdown для человека;
- JSON не source of truth;
- JSON не должен противоречить Markdown;
- JSON не должен содержать секреты;
- ключи JSON должны быть стабильными.

## Markdown Report Contract

Будущий путь отчёта:
- `reports/m33-stabilization-audit-report.md`
- или `reports/stabilization-audit-report.md`

Отчёт должен включать:
- timestamp;
- repo/branch (если доступны);
- список suites;
- сводку pass/fail;
- находки `P0/P1/P2/P3`;
- missing artifacts;
- stale evidence;
- unknown states;
- recommended next actions;
- non-authorization warning.

Обязательное предупреждение:

**This report is not approval for execution, commit, push, merge, release, or deployment.**

## Severity Model

- `P0` — false OK / bypass / fake approval.
  Example: `UNKNOWN` превращён в `PASS`.
- `P1` — workflow jump / stale evidence / unclear command.
  Example: completion без свежих evidence.
- `P2` — duplicated logic / weak docs / missing examples.
  Example: разные скрипты используют разные result-имена.
- `P3` — polish / future productization.
  Example: неединообразный текст подсказок без прямой угрозы безопасности.

## Fail-Closed Rules

- missing required artifact → `NOT_FOUND` или `FAIL`;
- unreadable required artifact → `UNKNOWN` или `FAIL`;
- malformed required artifact → `FAIL`;
- stale evidence → `STALE`;
- ambiguous status → `UNKNOWN`;
- unknown result value → `UNKNOWN`;
- unexpected script output → `UNKNOWN`;
- inconsistent Markdown/JSON status → `NEEDS_REVIEW` или `FAIL`;
- audit internal error → `UNKNOWN` или `FAIL`.

Обязательное правило: **audit должен предпочитать false red вместо false green** (лучше лишний блок, чем ложный «всё хорошо»).

## Mutation Boundary

Stabilization audit должен быть read-only.

Он не должен:
- редактировать docs;
- редактировать reports;
- редактировать tasks;
- редактировать schemas;
- редактировать templates;
- редактировать fixtures;
- чинить frontmatter;
- генерировать approval;
- создавать commits;
- перемещать задачи;
- помечать задачи done;
- обновлять `tasks/active-task.md`;
- переписывать evidence.

Если в будущем будут repair tools, они должны быть отдельны от audit и требовать явного approval.

## Recommended M33 Implementation Plan

Возможные задачи M33 (без реализации здесь):
- реализовать stabilization audit runner;
- добавить JSON output;
- добавить Markdown report output;
- связать существующие M32 docs с audit;
- добавить fail-closed обработку результатов;
- добавить evidence freshness checks;
- добавить approval boundary checks;
- добавить script responsibility checks;
- добавить negative coverage checks;
- добавить audit smoke fixtures;
- добавить audit negative fixtures.

## Non-Goals

M32.5 не делает:
- реализацию audit runner;
- создание скриптов;
- создание фикстур;
- изменение тестов;
- изменение валидаторов;
- изменение runtime guards;
- изменение CI;
- внедрение repair behavior;
- внедрение self-heal;
- внедрение recovery protocol;
- внедрение shadow branching;
- внедрение git checkpoints;
- внедрение packaging;
- внедрение UI/TUI/web UI.

## Final Boundary

M32.5 проектирует stabilization audit.
Он не запускает, не реализует и не вводит audit-принуждение.
Реализация аудита относится к M33+ при отдельном согласовании.
