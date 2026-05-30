# M69.7 — Validation Authority Drift Review

## Task Boundary

This validation authority drift review is a read-only review artifact.
This validation authority drift review identifies authority drift signals only.
This validation authority drift review does not decide final validation authority.
This validation authority drift review does not modify scripts or workflows.
This validation authority drift review does not create validators, registries, fixtures, or lifecycle mutation.
This validation authority drift review does not approve M69.
Human review remains required.

## Active Task Record

- `id: task-69.7`
- `milestone: M69`
- `name: "Validation Authority Drift Review"`
- `status: active`
- `mode: "EXECUTION / READ-ONLY VALIDATION AUTHORITY REVIEW"`
- `branch: dev`
- `started_at: "2026-05-28"`

## Inputs Reviewed

- `reports/m69-m68-completion-intake.md`
- `reports/m69-script-inventory-intake.md`
- `docs/SCRIPT-RESPONSIBILITY-MAP.md`
- `docs/SCRIPT-LIFECYCLE-POLICY.md`
- `docs/SCRIPT-OUTPUT-CONTRACT.md`
- `docs/SCRIPT-EXIT-CODE-STANDARD.md`
- `docs/ACTIVE-TREE-CLEANUP-PLAN.md`
- `reports/m69-dangerous-script-review.md`
- `reports/m68-docs-to-code-drift.json`
- `reports/m68-anomaly-grep.txt`
- `scripts/agentos-validate.py`
- `scripts/run-all.sh`
- `scripts/VALIDATORS.md`
- `.github/workflows/`
- `scripts/`

## M69.6 Risk Review Status

M69.6 is complete with warnings.

The dangerous script review exists, but it does not settle validation authority.

## Review Method

This is a read-only review based on observed file contents, references, and M68/M69 evidence.

This review identifies validation authority drift signals only.
This review does not decide final validation authority.
This review does not modify validation behavior.

## Observed Validation Entrypoints

- `scripts/agentos-validate.py`
- `scripts/run-all.sh`
- `scripts/validate-task.py`
- `scripts/validate-verification.py`
- `scripts/check-pr-quality.py`
- `scripts/check-dangerous-commands.py`
- `scripts/check-risk.py`
- `scripts/check-scope-compliance.py`
- `scripts/check-single-role-execution.py`
- `scripts/check-template-integrity.py`
- `scripts/check-template-cleanliness.py`
- `scripts/validate-architecture.sh`
- `scripts/check-links.py`
- `scripts/check-llms-graph-files.sh`
- other `run-*`, `validate-*`, and `check-*` scripts present in `scripts/`

## Observed CI Validation Calls

- `.github/workflows/agentos-validate.yml` calls `python scripts/agentos-validate.py all`
- `.github/workflows/agentos-validate.yml` calls `python scripts/agentos-validate.py all --json > reports/ci/agentos-validate.json`
- `.github/workflows/dev-only/agentos-validation.yml` calls `python3 scripts/validate-task.py tasks/active-task.md`
- `.github/workflows/dev-only/agentos-validation.yml` calls `python3 scripts/validate-verification.py reports/verification.md`
- `.github/workflows/dev-only/agentos-validation.yml` calls `python3 scripts/check-pr-quality.py`
- `.github/workflows/dev-only/agentos-validation.yml` calls `python3 scripts/check-dangerous-commands.py`
- `.github/workflows/dev-only/agentos-validation.yml` calls `python3 scripts/check-risk.py tasks/active-task.md`
- `.github/workflows/dev-only/agentos-validation.yml` calls `bash scripts/run-all.sh`

## Observed Child Validators

- `scripts/check-scope-compliance.py`
- `scripts/test-scope-compliance-fixtures.py`
- `scripts/audit-execution-control.py`
- `scripts/check-readiness-assertions.py`
- `scripts/check-single-role-execution.py`
- `scripts/check-process-trace.py`
- `scripts/check-evidence-binding.py`
- `scripts/check-private-evaluator-consistency.py`
- `scripts/check-canary-integrity.py`
- `scripts/check-validator-authority-boundary.py`
- `scripts/check-role-separation.py`
- `scripts/check-evidence-immutability.py`
- `scripts/check-evidence-amendments.py`
- `scripts/test-honest-pass-fixtures.py`
- `scripts/test-integrity-regression.py`

## Observed Legacy Validation References

- `scripts/run-all.sh` explicitly labels itself a legacy script and points to `python3 scripts/agentos-validate.py all` as the current validator
- `scripts/VALIDATORS.md` still frames canonical checks as being used by `scripts/run-all.sh`
- `.github/workflows/dev-only/agentos-validation.yml` still invokes `scripts/run-all.sh`
- older task/verification style validation remains visible in workflow calls and legacy run-all references

## Observed Validator Documentation References

- `scripts/VALIDATORS.md`
- `scripts/run-all.sh`
- `docs/SCRIPT-OUTPUT-CONTRACT.md`
- `docs/SCRIPT-EXIT-CODE-STANDARD.md`
- `reports/m68-docs-to-code-drift.json`
- `reports/m68-anomaly-grep.txt`

## Observed JSON Output Expectations

- `docs/SCRIPT-OUTPUT-CONTRACT.md` asks for stable JSON fields such as `tool`, `version`, `result`, `status`, `warnings`, `errors`, `inputs`, `outputs`, `evidence`, `manual_review_required`, and `non_approval_boundary`
- `scripts/agentos-validate.py` emits JSON for `--json` mode and for subcommands such as `honest-pass`, `integrity`, and `integrity-regression`
- `.github/workflows/agentos-validate.yml` expects `reports/ci/agentos-validate.json`
- workflow enforcement reads the JSON `result` field and blocks on `WARN`, `FAIL`, `ERROR`, `NOT_RUN`, and `INCOMPLETE`
- current code still preserves mixed summary/result behavior, so JSON evidence and exit-code meaning must be reconciled later

## Observed Exit-Code Expectations

- `docs/SCRIPT-EXIT-CODE-STANDARD.md` proposes `exit 0`, `exit 1`, and `exit 2` only
- `scripts/agentos-validate.py` currently maps `PASS=0`, `FAIL=1`, `WARN=2`, `ERROR=3`, `NOT_RUN=3`
- `scripts/agentos-validate.py` also uses `exit_code=0` for some integrity warnings, which differs from the future standard
- `.github/workflows/agentos-validate.yml` treats `WARN`, `FAIL`, `ERROR`, `NOT_RUN`, and `INCOMPLETE` as blocking merge conditions
- `scripts/run-all.sh` does not express the same JSON/exit-code model as the consolidated validator

## Validation Authority Drift Signals

- CLI entrypoint signal: `scripts/agentos-validate.py` is presented in docs and workflows as the current validator
- legacy entrypoint signal: `scripts/run-all.sh` still exists and is still referenced by docs/workflows
- docs reference signal: `scripts/VALIDATORS.md` frames canonical checks through `run-all.sh`
- CI signal: one workflow uses the unified validator, another still calls the older task/verification stack plus `run-all.sh`
- child validator signal: validation authority is distributed across many child checks rather than one clear dispatcher boundary
- JSON/exit-code signal: `PASS`/`WARN`/`FAIL`/`ERROR`/`NOT_RUN` are not handled by one single exit-code convention across all surfaces

## Conflicting Or Ambiguous Authority Areas

- `scripts/agentos-validate.py` vs `scripts/run-all.sh`
- `scripts/VALIDATORS.md` describing canonical checks while workflow still calls legacy validation paths
- `agentos-validate.yml` using merged JSON enforcement while `dev-only/agentos-validation.yml` uses legacy task/verification plus run-all
- `scripts/agentos-validate.py` child validator behavior vs top-level workflow blocking rules
- `PASS`/`WARN`/`NOT_RUN` meanings across JSON, text, and exit code

## Protected Validator Constraints

- `scripts/check-task-validation-contract.py` - protected
- `scripts/check-agent-task-evidence.py` - protected
- `scripts/check-acceptance-criteria.py` - protected
- `scripts/run-task-validation.py` - protected
- `scripts/check-false-pass-resistance.py` - protected
- `schemas/task-validation-package.schema.json` - protected
- `schemas/task-validation-result.schema.json` - protected
- `schemas/agent-task-output-evidence.schema.json` - protected
- `schemas/acceptance-criteria-check-package.schema.json` - protected
- `schemas/unified-runner-input.schema.json` - protected
- `tests/fixtures/m67-false-pass-resistance/` - protected

These protected artifacts are constrained by separate human checkpoint rules and are not authority candidates for cleanup or rewrite in this task.

## Carry-Forward Items For M71

- validation authority drift check
- JSON/exit-code consistency check
- known entrypoint reference check
- stale validator doc check

## Carry-Forward Items For M72

- validator registry candidate
- owner coverage for validators
- protected validator registry entries

## Carry-Forward Items For M73

- thin dispatcher boundary
- child validator routing
- no reinterpretation of child results
- no downgrade of BLOCKED to WARNING
- no NOT_RUN to PASS conversion

## Carry-Forward Items For M74

- conflicting validator authority fixture
- stale VALIDATORS.md fixture
- child checker invalid JSON fixture
- exit-code/result mismatch fixture

## Carry-Forward Items For M75

- validators with JSON contract %
- validators with exit-code contract %
- validation authority drift count
- child validator registry coverage

## Human Review Requirements

- Any unresolved authority drift remains human-review material
- Any protected validator path remains human-review material
- Any workflow that still splits validation authority across multiple surfaces requires human review before cleanup or routing changes

## Explicit Non-Authority-Decision Boundary

This validation authority drift review is a read-only review artifact.
This validation authority drift review identifies authority drift signals only.
This validation authority drift review does not decide final validation authority.
This validation authority drift review does not modify scripts or workflows.
This validation authority drift review does not create validators, registries, fixtures, or lifecycle mutation.
This validation authority drift review does not approve M69.
Human review remains required.

## M69.8 Preparation Decision

may_prepare_m69_8: true_with_warnings

may_prepare_m69_8 is roadmap preparation only.
may_prepare_m69_8 does not start M69.8.
may_prepare_m69_8 is not approval.

## Final Status

FINAL_STATUS: M69_VALIDATION_AUTHORITY_DRIFT_REVIEW_COMPLETE_WITH_WARNINGS
