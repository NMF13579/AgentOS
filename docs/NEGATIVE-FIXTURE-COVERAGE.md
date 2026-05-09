# Negative Fixture Coverage Map (M32.4)

## Purpose

M32.4 фиксирует карту покрытия negative fixtures (негативные тестовые сценарии) до hardening в M33.

Цель: показать, какие guard/validator/boundary уже проверяются на плохих данных, а где покрытие отсутствует или неочевидно.

## Negative Fixture Principle

- Happy-path тесты доказывают только, что валидный ввод может пройти.
- Negative fixtures доказывают, что плохой/опасный ввод блокируется.
- Каждому guard нужен минимум один positive и один negative сценарий.
- Критичным guard нужны несколько negative сценариев.
- Состояния unknown/stale/malformed/fake/forbidden/unsafe должны fail-closed (при сомнении блокировать).

Обязательное правило: **No Negative Fixtures → No Guard Confidence.**

## Coverage Inventory

| Guard / Validator / Boundary | Exists? | Positive Fixtures? | Negative Fixtures? | Runner? | Expected Failure Result | Current Confidence | Gap | Follow-up |
|---|---|---|---|---|---|---|---|---|
| task contract validation (`validate-task.py`) | FOUND | FOUND | FOUND (`test-active-task-fixtures`, negative task fixtures) | FOUND | `FAIL` + non-zero | Medium | Нужна унификация expected-result контрактов | M33 |
| verification report validation (`validate-verification.py`) | FOUND | UNKNOWN | UNKNOWN | FOUND | `FAIL` + non-zero | Low | Нет явной карты негативных фикстур в одном месте | M33 |
| risk guard (`check-risk.py`) | FOUND | UNKNOWN | UNKNOWN | UNKNOWN | `FAIL/BLOCKED` | Low | Покрытие неочевидно | M33 |
| dangerous command guard (`check-dangerous-commands.py`) | FOUND | FOUND | FOUND | FOUND | `FAIL` | Medium | Нужны сценарии обхода через raw shell patterns | M33 |
| commit message validator (`validate-commit-msg.py`) | FOUND | UNKNOWN | UNKNOWN | FOUND | `FAIL` | Low | Не видно явной матрицы негативных кейсов | M33 |
| template integrity checker (`check-template-integrity.py`) | FOUND | FOUND | FOUND (`test-template-integrity-fixtures`) | FOUND | `FAIL` / strict non-zero | Medium | Нужен P0 профиль для критичных missing-core | M33 |
| context pack requirement (`check-required-context-pack.py`) | FOUND | FOUND | FOUND (`context-pipeline-check/*`) | FOUND | `NEEDS_REVIEW/BLOCKED/FAIL` | Medium | Нет единой критической матрицы no-context execution | M33 |
| context compliance check (`check-context-compliance.py`) | FOUND | UNKNOWN | UNKNOWN | FOUND | `FAIL/NEEDS_REVIEW` | Low | Сложно понять полноту negative coverage | M33 |
| status aggregation (`agentos-status.py`) | FOUND | FOUND | PARTIAL | FOUND | `UNKNOWN/BLOCKED/NEEDS_REVIEW` + non-zero path in consumers | Medium | Нужны фикстуры для false green (`UNKNOWN -> PASS`) | M33 |
| next safe action (`agentos-next-step.py`) | FOUND | FOUND | PARTIAL | FOUND | `NEXT_STEP_SAFETY_FAIL` + exit 1 | Medium | Нужны сценарии “next became execute” | M33 |
| audit runner (`audit-agentos.py`) | FOUND | FOUND | PARTIAL | FOUND | `FAIL` | Medium | Нет негативных фикстур "audit mutates files" | M33 |
| review gate (`validate-review.py`) | FOUND | FOUND (`review-validator/valid`) | FOUND (`review-validator/invalid`) | FOUND | `FAIL` | High | Нужны кейсы stale review связки с evidence | M33 |
| completion review (`check-completion-readiness.py`) | FOUND | UNKNOWN | PARTIAL | FOUND | `FAIL/PARTIAL` | Medium | Нужны негативные кейсы stale evidence blocking | M33 |
| human approval boundary (`validate-human-approval.py`, `agentos-human-gate.py`) | FOUND | FOUND | FOUND (`human-approval`, `human-gate`) | FOUND | `BLOCKED/INVALID/NEEDS_REVIEW` | High | Нужна связка с commit/push/release boundaries | M33 |
| fake approval detection | FOUND | FOUND | FOUND | FOUND | `BLOCKED/INVALID` | High | Нужны unified P0 fixtures across all gates | M33 |
| evidence freshness | FOUND (частично через context/index checks) | FOUND | PARTIAL | FOUND | `NEEDS_REVIEW/FAIL` | Medium | Нет единого fixture набора stale verification/audit/completion | M33 |
| evidence immutability | FOUND (pre-merge-scope evidence-tampering) | FOUND | FOUND | FOUND | `FAIL/BLOCKED` | Medium | Нужны кейсы post-completion edits | M33 |
| protected file write (`agentos-write-guard.py`) | FOUND | FOUND (`m27-write-guard`) | FOUND | FOUND | `WRITE_BLOCKED/WRITE_NEEDS_REVIEW` | High | Нужны cross-guard consistency fixtures | M33 |
| runtime command guard (`agentos-command-guard.py`) | FOUND | FOUND | FOUND | FOUND | `COMMAND_NEEDS_REVIEW/PERMISSION_BLOCKED` | High | Нужны unknown command + bypass pattern fixture standards | M33 |
| runtime write guard (`agentos-write-guard.py`) | FOUND | FOUND | FOUND | FOUND | `WRITE_BLOCKED/WRITE_NEEDS_REVIEW` | High | Нужна общая result-лексика с другими guard | M33 |
| runtime git guard (`agentos-git-guard.py`) | FOUND | FOUND | FOUND | FOUND | `GIT_BLOCKED/GIT_NEEDS_REVIEW` | High | Нужны прямые кейсы force push + protected branch matrix | M33 |
| token exposure check | NOT FOUND (явный отдельный guard) | NOT FOUND | NOT FOUND | NOT FOUND | `BLOCKED/FAIL` | None | Нет явного guard/fixtures | M33 |
| role separation (status/explain/next/render) | FOUND (через архитектуру) | UNKNOWN | MISSING | NOT FOUND (единый runner) | `FAIL` при смешении ролей | Low | Нет негативных drift fixtures как класса | M33 |
| dry-run requirement | UNKNOWN | UNKNOWN | MISSING | UNKNOWN | `BLOCKED/NEEDS_REVIEW` | Low | Нужны явные fixtures на обязательный dry-run | M33 |
| state transition guard | FOUND (`check-transition.py`, `validate-lifecycle-apply.py`) | FOUND | FOUND (`test-apply-transition-fixtures`) | FOUND | `FAIL/BLOCKED` | Medium | Нужны stale/ambiguous transition fixtures | M33 |
| renderer safety | FOUND (`renderers/*`, `audit-m31-tui-tutor.py`) | FOUND | PARTIAL | FOUND | `FAIL/NEEDS_REVIEW` | Medium | Нужны явные negative fixtures на softening BLOCKED | M33 |
| tutor / decision card authority boundary | PARTIAL (`agentos-tui.py`, `audit-m31-tui-tutor.py`) | FOUND | PARTIAL | FOUND | `FAIL/NEEDS_REVIEW` | Medium | decision-card artifact NOT FOUND; boundary fixtures неполные | M33 |
| CLI wrapper fail-closed behavior (`agentos.py`) | FOUND | UNKNOWN | MISSING | NOT FOUND (спец. runner) | `non-zero` for unsafe/unknown | Low | Нет явной negative fixture матрицы wrapper behavior | M33 |

## Required Negative Fixture Categories

### A. Structural Invalidity

Покрывается частично (`queue-validator/invalid`, `review-validator/invalid`, `human-approval/invalid`, `pre-merge-scope/invalid`).

Примеры обязательных кейсов:
- missing required field;
- malformed YAML/frontmatter;
- invalid enum;
- duplicate `task_id` (coverage: UNKNOWN);
- missing acceptance criteria;
- missing validation plan;
- unknown result value.

Статус: **PARTIAL**.

### B. False Green / False OK

Примеры:
- `UNKNOWN` treated as `PASS`;
- `WARN` treated as approval;
- stale report treated as fresh;
- damaged report accepted;
- missing evidence accepted;
- generated report treated as authority.

Статус: **MISSING/PARTIAL** (есть отдельные stale/evidence проверки, но нет единого P0 набора false-green фикстур).

### C. Scope / Context Violations

Покрытие: `pre-merge-scope/invalid`, `context-pipeline-check/*`, `context-audit/*`.

Примеры:
- out_of_scope change;
- no Context Pack;
- context pack без relevance;
- missing context compliance;
- selection contradicts scope;
- no-context execution.

Статус: **FOUND (strong)**, но с пробелом в unified no-context execution P0 наборе.

### D. Human Approval Violations

Покрытие: `human-approval/invalid*`, `human-gate/*`, `m27-violation-enforcement/*`.

Примеры:
- fake approval;
- agent-generated approval;
- checklist as approval;
- tutor explanation as approval;
- decision card creates approval (artifact NOT FOUND);
- audit PASS as approval.

Статус: **FOUND (high)**, кроме decision-card и audit-pass misuse unified fixtures.

### E. Dangerous Command / Runtime Violations

Покрытие: `check-dangerous-commands`, `agentos-command-guard`, `agentos-write-guard`, `agentos-git-guard`, `m27-write-guard` fixtures.

Примеры:
- `rm -rf`;
- direct `git push`;
- force push;
- `curl | sh`;
- unknown command;
- raw shell bypass;
- forbidden command with exit 0.

Статус: **FOUND (high)**, но нужны расширенные bypass-фикстуры.

### F. Evidence / Report Violations

Покрытие: `pre-merge-scope/invalid/evidence-tampering`, часть context-аудитов.

Примеры:
- old verification reused;
- wrong-task report;
- edited-after-completion;
- missing commit/state reference;
- completion without fresh evidence;
- amendment missing.

Статус: **PARTIAL**.

### G. Script Responsibility Violations

Примеры:
- validator mutates files;
- audit has `--fix`;
- renderer decides status;
- next-step executes;
- explain lowers risk;
- status acts as tutor;
- wrapper converts BLOCKED to OK.

Статус: **MISSING** как отдельный fixture-class.

### H. UI / Human Product Violations

Примеры:
- BLOCKED softened to warning;
- ambiguous approval wording;
- next sounds like execute;
- checklist looks like decision;
- hidden risk;
- missing consequence.

Статус: **PARTIAL** (через `audit-m31-tui-tutor.py`), но полнота unknown.

## Critical Guard Matrix

| Critical Guard | Minimum Negative Fixtures Required | Existing Coverage | Missing Fixtures | Severity If Missing | M33 Target? |
|---|---|---|---|---|---|
| `UNKNOWN` must not become `PASS` | 3 (status, view-model, completion path) | PARTIAL | false-green chain fixtures | P0 | Yes |
| fake approval must not pass | 4 (format, source, scope, transition) | FOUND | unified cross-gate fixture bundle | P0 | Yes |
| stale evidence must not complete task | 4 (verification, audit, review, completion) | PARTIAL | completion stale-evidence blocker fixtures | P0 | Yes |
| no Context Pack must block execution | 3 (missing, invalid, irrelevant) | PARTIAL | direct execution-without-context fixtures | P0 | Yes |
| dangerous command must block | 4 (rm, curl-pipe, unknown, bypass) | FOUND | advanced bypass set | P0 | Yes |
| protected write must block | 4 (forbidden path, delete, traversal, no approval) | FOUND | consistency fixtures across path classes | P0 | Yes |
| direct git push must block | 3 (protected branch, unknown target, missing approval) | FOUND | force-push explicit fixture set | P0 | Yes |
| audit must not mutate files | 2 (read-only check, mutation attempt) | MISSING | mutation-detection fixtures | P0 | Yes |
| renderer must not decide status | 2 (input fidelity, blocked visibility) | PARTIAL | renderer drift fixtures | P1 | Yes |
| next-step must not execute | 3 (command injection, action mutation, unsafe verb) | MISSING | non-execute enforcement fixtures | P0 | Yes |
| tutor must not approve | 2 (wording boundary, authority boundary) | PARTIAL | explicit tutor-authority fixtures | P1 | Yes |
| completion must require fresh evidence | 3 (old evidence, wrong task, missing references) | PARTIAL | completion freshness matrix | P0 | Yes |

## Expected Fixture Structure

Рекомендуемая структура на будущее (не реализуется в 32.4):

```text
tests/fixtures/negative/
  task-contract/
  verification/
  context-pack/
  approval/
  evidence/
  runtime-command/
  runtime-write/
  runtime-git/
  script-responsibility/
  renderer/
  tutor/
  completion/
```

Каждая группа должна содержать:
- `README.md`
- `valid-control-case/`
- `invalid-case-001/`
- `invalid-case-002/`
- `expected-result.md` или `expected.json`

## Expected Runner Behavior

Ожидаемое поведение будущего runner (runner = скрипт запуска набора фикстур):

- negative fixture должен падать по правильной причине;
- причина падения должна быть machine-readable (читаема скриптом);
- падение должно давать non-zero exit code;
- ambiguous result должен fail-closed;
- ожидаемое падение не считается провалом теста;
- неожиданный PASS — критический провал;
- runner не должен мутировать source fixtures.

## Coverage Gap Table

| Gap ID | Area | Missing Negative Case | Why It Matters | Severity | Proposed Fixture Group | Follow-up Task |
|---|---|---|---|---|---|---|
| G-001 | False green chain | `UNKNOWN -> PASS` across status→next→completion | Ложный зелёный статус | P0 | `script-responsibility/` + `completion/` | M33 |
| G-002 | Evidence freshness | stale verification/audit accepted by completion | DONE на старых данных | P0 | `evidence/` + `completion/` | M33 |
| G-003 | Context enforcement | execution allowed without valid Context Pack | Работа вне контекста | P0 | `context-pack/` | M33 |
| G-004 | Audit neutrality | audit modifies files | Потеря доверия к audit | P0 | `script-responsibility/` | M33 |
| G-005 | Next-step boundary | next-step emits executable/unsafe action | Непреднамеренное выполнение | P0 | `script-responsibility/` | M33 |
| G-006 | Renderer safety | BLOCKED visually softened | Пользователь пропускает блокировку | P1 | `renderer/` | M33 |
| G-007 | Tutor authority | tutor wording implies approval | Ложное ощущение разрешения | P1 | `tutor/` | M33 |
| G-008 | Wrapper fail-closed | wrapper returns safe/0 on ambiguous states | Обход guard-цепочки | P1 | `runtime-command/` | M33 |
| G-009 | Token exposure | no explicit token leak guard fixtures | Риск утечки секретов | P0 | `runtime-command/` + `policy/` (future) | M33 |
| G-010 | Result semantics | inconsistent result names/exit meanings | Автоматизация делает неверные выводы | P2 | `script-responsibility/` | M33 |

## M33 Candidate Fixes

Возможные задачи M33 (без реализации в 32.4):

- добавить недостающие P0 negative fixtures;
- стандартизировать структуру negative fixture директорий;
- расширить negative fixture runner;
- добавить expected-result контракт;
- добавить stale evidence fixtures;
- добавить fake approval fixtures;
- добавить no-context execution fixtures;
- добавить script-responsibility drift fixtures;
- добавить renderer softening fixtures;
- добавить tutor authority boundary fixtures;
- подключить coverage negative fixtures в unified audit runner.

## Non-Goals

M32.4 явно не делает:

- создание фикстур;
- написание тестов;
- изменение test runners;
- изменение валидаторов;
- изменение runtime guards;
- изменение audit scripts;
- изменение CI;
- внедрение fail-closed фиксов;
- внедрение покрытия фикстурами;
- self-heal;
- recovery protocol;
- shadow branching;
- git checkpoints;
- packaging;
- UI/TUI/web UI.

## Final Boundary

M32.4 — это coverage map, а не реализация тестов.
Все отсутствующие negative fixtures относятся к M33 или позже, если отдельно не согласовано.
