# M69.6 — Dangerous Script / Write Operation Review

## Task Boundary

This dangerous script review is a read-only review artifact.
This dangerous script review identifies risk signals only.
This dangerous script review does not execute scripts.
This dangerous script review does not authorize script cleanup, deletion, rename, move, merge, archive, or refactor.
This dangerous script review does not modify scripts or workflows.
This dangerous script review does not decide final validation authority.
This dangerous script review does not create validators, registries, fixtures, or lifecycle mutation.
This dangerous script review does not approve M69.
Human review remains required.

## Active Task Record

- `id: task-69.6`
- `milestone: M69`
- `name: "Dangerous Script / Write Operation Review"`
- `status: active`
- `mode: "EXECUTION / READ-ONLY RISK REVIEW"`
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
- `reports/m68-anomaly-grep.txt`
- `reports/m68-inventory.json`
- `reports/m68-protected-artifacts.json`
- `scripts/`
- `.github/workflows/`
- `.github/actions/` where present
- root shell/script files where present

## M69.5 Cleanup Plan Status

M69.5 is complete with warnings.

The cleanup plan exists, but it is planning only and not cleanup authorization.

## Review Method

This review identifies risk signals only.
This review does not execute scripts.
This review does not prove runtime behavior.

The review is based on read-only text inspection and grep-style signal detection.

## Risk Severity Vocabulary

- `LOW_REVIEW` - minor risk signal, low priority for human follow-up
- `MEDIUM_REVIEW` - visible risk signal that should be reviewed before execution or cleanup
- `HIGH_REVIEW` - strong risk signal that should be reviewed before execution or cleanup
- `CRITICAL_REVIEW` - direct destructive, write-heavy, or self-mutating signal
- `NEEDS_MANUAL_REVIEW` - evidence is not enough for a safe automatic judgment
- `UNKNOWN_REVIEW` - the signal cannot be classified safely from text inspection alone

Risk severity is a review priority label, not approval and not a final safety decision.

## Write Operation Signals

- `scripts/agentos-validate.py` - writes JSON result artifacts and report files
- `scripts/repo-scan.py` - writes inventory, duplicates, owner gaps, protected, drift, prompt metrics, anomaly, and raw inventory reports
- `scripts/agentos-retry-enforce.py` - writes updated state JSON
- `scripts/agentos-violation-enforce.py` - writes updated state JSON
- `scripts/agentos-status.py` - writes snapshot output
- `scripts/task-health.py` - writes report output
- `scripts/build-task-dependency-map.py` - writes generated output files
- `scripts/generate-repo-map.py` - writes generated repo map output
- `scripts/generate-tasks-from-spec.py` - writes generated markdown

## Destructive Command Signals

- `.github/workflows/setup-repository.yml` - contains `rm -rf tests/fixtures` and `rm -rf tasks/*`
- `.github/workflows/setup-repository.yml` - contains `rm -f .github/workflows/setup-repository.yml` and `rm -f init-project.sh`
- `.github/workflows/setup-repository.yml` - contains `git push`
- `scripts/test-example-project.sh` - uses `rm -rf "$TMP_DIR"` in a trap for cleanup
- `scripts/agentos-command-guard.py` - explicitly scans for `rm`, `rm -rf`, and shell-pipe patterns

## Broad Filesystem Mutation Signals

- `scripts/repo-scan.py` - broad report generation across inventory and anomaly outputs
- `scripts/install-agentos.py` - planned `copy_tree` and `mkdir_p` operations over repository trees
- `scripts/test-apply-transition-fixtures.py` - copies files into temp sandboxes and writes many fixture files
- `scripts/check-m55-active-task-readiness-fixtures.py` - copies and creates fixture workspace files
- `scripts/generate-tasks-from-spec.py` - generates multiple task files

## Git Mutation Signals

- `.github/workflows/setup-repository.yml` - `git commit`
- `.github/workflows/setup-repository.yml` - `git push`
- `.github/workflows/init-from-template.yml` - `git commit`
- `.github/workflows/init-from-template.yml` - `git push`
- `scripts/check-context-required.py` - reads `git rev-parse HEAD` as part of repo state checks
- `scripts/check-context-compliance.py` - reads `git rev-parse HEAD`

## Workflow Self-Mutation Signals

- `.github/workflows/setup-repository.yml` - deletes and rewrites repository files during template setup
- `.github/workflows/init-from-template.yml` - auto-commits and pushes repository initialization changes
- `.github/workflows/agentos-validate.yml` - collects validation output into `reports/ci/agentos-validate.json`
- `.github/workflows/dev-only/agentos-validation.yml` - invokes `scripts/run-all.sh`

## Token / API / Push Signals

- `.github/workflows/init-from-template.yml` - uses `secrets.GITHUB_TOKEN`
- `.github/workflows/init-from-template.yml` - uses `curl` to query the GitHub API
- `.github/workflows/setup-repository.yml` - uses `git push`
- `scripts/test-m40-runtime-bypass-smoke.py` - inspects token-bearing environment variables such as `GITHUB_TOKEN`

## Subprocess Usage Signals

shell=False:
- `scripts/check-required-context-compliance.py`
- `scripts/check-context-pipeline.py`
- `scripts/check-bypass-resistance.py`
- `scripts/agentos-command-guard.py`
- `scripts/run-task-validation.py`
- `scripts/audit-agentos.py`
- `scripts/check-execution-verification-regression.py`
- `scripts/check-context-compliance.py`

shell=True:
- `scripts/check-use-template-readiness.py`

unknown shell mode:
- `scripts/agentos.py`
- `scripts/agentos-explain.py`
- `scripts/agentos-enforce.py`
- `scripts/agentos-next-step.py`
- `scripts/audit-mvp-readiness.py`
- `scripts/check-policy-fixtures.py`
- `scripts/check-transition.py`

## Shell Invocation Signals

- `scripts/run-all.sh`
- `scripts/health-check.sh`
- `scripts/validate-architecture.sh`
- `scripts/check-llms-graph-files.sh`
- `scripts/test-example-project.sh`
- `scripts/install-agentos.py`
- `.github/workflows/agentos-validate.yml` invokes `python scripts/agentos-validate.py all`
- `.github/workflows/dev-only/agentos-validation.yml` invokes `bash scripts/run-all.sh`

## Protected Artifact Touch Signals

- `scripts/check-task-validation-contract.py`
- `scripts/check-agent-task-evidence.py`
- `scripts/check-acceptance-criteria.py`
- `scripts/run-task-validation.py`
- `scripts/check-false-pass-resistance.py`
- `schemas/task-validation-package.schema.json`
- `schemas/task-validation-result.schema.json`
- `schemas/agent-task-output-evidence.schema.json`
- `schemas/acceptance-criteria-check-package.schema.json`
- `schemas/unified-runner-input.schema.json`
- `tests/fixtures/m67-false-pass-resistance/`

## Workflow-Referenced Script Risk Signals

- `scripts/agentos-validate.py` - workflow entrypoint in `agentos-validate.yml`
- `scripts/run-all.sh` - workflow entrypoint in `dev-only/agentos-validation.yml`
- `scripts/VALIDATORS.md` - referenced by `scripts/run-all.sh`
- `scripts/validate-architecture.sh` - referenced by validator docs and workflow usage
- `scripts/validate-docs.py` - referenced by validator docs
- `scripts/check-links.py` - referenced by validator docs
- `scripts/check-llms-graph-files.sh` - referenced by validator docs

## Scripts Requiring Human Review Before Cleanup

- `scripts/agentos-validate.py`
- `scripts/run-all.sh`
- `scripts/VALIDATORS.md`
- `scripts/install-agentos.py`
- `.github/workflows/setup-repository.yml`
- `.github/workflows/init-from-template.yml`
- `scripts/repo-scan.py`
- `scripts/agentos-retry-enforce.py`
- `scripts/agentos-violation-enforce.py`
- `scripts/generate-tasks-from-spec.py`
- `scripts/build-task-dependency-map.py`

## Scripts Requiring Human Review Before Execution

- `scripts/agentos-validate.py`
- `scripts/run-all.sh`
- `scripts/install-agentos.py`
- `.github/workflows/setup-repository.yml`
- `.github/workflows/init-from-template.yml`
- `scripts/agentos-enforce.py`
- `scripts/agentos-retry-enforce.py`
- `scripts/agentos-violation-enforce.py`
- `scripts/check-context-pipeline.py`
- `scripts/check-required-context-compliance.py`

## Risk Summary

- `CRITICAL_REVIEW`: workflow self-mutation in setup/init workflows, and scripts that write or mutate repo state
- `HIGH_REVIEW`: scripts with write-heavy output or protected-artifact touches
- `MEDIUM_REVIEW`: scripts with subprocess execution, shell invocations, or token/API/push usage
- `NEEDS_MANUAL_REVIEW`: ambiguous shell mode, mixed stdout/stderr behavior, or unclear runtime scope

Any script with `HIGH_REVIEW`, `CRITICAL_REVIEW`, `DANGEROUS_REQUIRES_REVIEW`, protected touch signals, or workflow self-mutation signals must be listed as requiring human review before cleanup or execution.

## Explicit Non-Remediation Boundary

This dangerous script review is a read-only review artifact.
This dangerous script review identifies risk signals only.
This dangerous script review does not execute scripts.
This dangerous script review does not authorize script cleanup, deletion, rename, move, merge, archive, or refactor.
This dangerous script review does not modify scripts or workflows.
This dangerous script review does not decide final validation authority.
This dangerous script review does not create validators, registries, fixtures, or lifecycle mutation.
This dangerous script review does not approve M69.
Human review remains required.

## M69.7 Preparation Decision

may_prepare_m69_7: true_with_warnings

may_prepare_m69_7 is roadmap preparation only.
may_prepare_m69_7 does not start M69.7.
may_prepare_m69_7 is not approval.

## Final Status

FINAL_STATUS: M69_DANGEROUS_SCRIPT_REVIEW_COMPLETE_WITH_WARNINGS
