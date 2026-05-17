## Purpose
End-to-end smoke for M44 decomposition pipeline.

## Position in M44
Финальная smoke-проверка совместимости компонентов M44.

## Smoke Scope
Проверяется связка: spec generator, ux generator, dependency map builder, linter.

## Risk Reason
Risk Reason: MEDIUM because orchestration touches multiple tools, but remains read-only.

## Required Upstream Artifacts
Обязательны upstream скрипты, схемы и docs из 44.4/44.5/44.7/44.9.

## Required 44.9 Fixture Artifacts
Обязателен полный набор позитивных и негативных фикстур лентера 44.9.

## CLI Compatibility Preconditions
CLI compatibility checks are normative for M44.10.
Если CLI несовместим, вернуть PRECONDITION_FAILED_M44_10_CLI_INCOMPATIBLE.

## Normative CLI Contract
Проверяются флаги help для:
- generate-tasks-from-spec
- generate-tasks-from-ux
- build-task-dependency-map
- lint-task-contract

## Canonical Lint Token Vocabulary
44.10 must use the canonical lint result tokens defined by 44.9.
- TASK_LINT_PASS
- TASK_LINT_WARNING
- TASK_LINT_NEEDS_REVIEW
- TASK_LINT_FAIL
- TASK_LINT_FAILED
TASK_LINT_FAILED is linter infrastructure failure, not behavior failure.
TASK_LINT_FAILED is not an acceptable substitute for TASK_LINT_FAIL.

## Python Runtime Requirement
Python runtime below 3.10 is M44_SMOKE_FAILED.

## Temporary Output Boundary
Temporary smoke output is not task queue state.
Temporary JSON output must be written under the smoke temporary directory.
M44 smoke must not write into tasks/queue/.

## Smoke JSON Output Contract
Smoke JSON output must include result, exit_code, steps, issue_count, failed_steps, infrastructure_failures, non_approval_warning, and timestamp.
--json output must be written to stdout.
timestamp must not include microseconds or sub-second precision.
steps must contain at least one step entry.

## Fixture Kind Mapping
Expected-token validation must use explicit --kind values.
- .md => --kind task
- .json => --kind queue

## Relationship to Spec Generator
Dry-run smoke for spec generator only.

## Relationship to UX Generator
Dry-run smoke for UX generator only.

## Relationship to Dependency Map
Dependency map smoke runs via temp output directory.

## Relationship to Task Contract / Queue Linter
Позитивные/негативные фикстуры 44.9 валидируются по expected token map.

## Positive Fixture Expected-Token Map
Positive fixtures must return expected lint tokens.

## Negative Fixture Expected-Token Map
Negative fixtures must return expected lint tokens.
Unexpected PASS on a negative fixture is M44_SMOKE_FAIL.
Malformed JSON output is M44_SMOKE_FAILED.

## Forbidden Repository Path Mutation Boundary
The definitive changed-file scope check is external validation, not a smoke script responsibility.
Smoke script itself must not call git.

## Result Tokens
- M44_SMOKE_PASS
- M44_SMOKE_FAIL
- M44_SMOKE_FAILED

## Exit Codes
- 0 = M44_SMOKE_PASS
- 1 = M44_SMOKE_FAIL
- 2 = M44_SMOKE_FAILED

## FAIL vs FAILED Semantics
M44_SMOKE_FAIL means behavior checks failed.
M44_SMOKE_FAILED means smoke infrastructure could not run safely.

## Non-Approval Boundary
M44 smoke validation does not approve execution.
Smoke PASS is not approval and does not authorize execution.
Smoke PASS does not authorize queue mutation.
M44 smoke must not start M45 autopilot.

## Known Gaps
- This smoke does not validate real external specs.
- This smoke does not create real task queue entries.
- This smoke does not approve generated tasks.
- This smoke does not test M45 autopilot.
- This smoke does not replace HumanApprovalGate.
- This smoke does not perform full integration with GitHub branch protection.
- This smoke uses fixtures and temporary directories only.
- This smoke depends on 44.4, 44.5, 44.7, and 44.9 CLI compatibility.
- This smoke depends on 44.9 linter fixture paths.
- This smoke intentionally fails closed on incompatible upstream CLI contracts.
- This smoke intentionally fails closed on canonical lint token vocabulary mismatch.
- This smoke intentionally fails closed if required 44.9 fixtures are missing.
- The smoke script does not call git; changed-file scope is verified by external validation.
- PRECONDITION_FAILED_M44_10_CLI_INCOMPATIBLE
- PRECONDITION_FAILED_M44_10_LINT_TOKEN_INCOMPATIBLE
- PRECONDITION_FAILED_M44_10_44_9_FIXTURES_MISSING
