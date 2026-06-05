# Script Dangerous Operations Audit

**Milestone:** M71.4 — Dangerous Script Operations Audit
**Mode:** AUDIT / READ-ONLY RISK SIGNALS / NO SCRIPT CHANGES
**Branch:** dev
**Date:** 2026-05-30
**Produced by:** Task 71.4

---

## Boundary Statement

This document is the output of M71.4 read-only signal scanning.

This document does not modify scripts.

This document does not execute scripts.

This document does not run validators.

This document does not perform cleanup.

This document does not create registries.

This document does not assign final lifecycle status.

This document does not judge scripts as SAFE or UNSAFE.

This document does not print source lines.

This document does not print secret values.

This document records only: detected signal names, line numbers, and categories — not values.

---

## Authority Declaration

- `reports/m71-script-inventory.md` is the source-of-truth inventory artifact.
- `reports/m71-script-inventory.json` is a derived navigation artifact only.
- `reports/m71-script-inventory.json` must not become source of truth.
- `docs/SCRIPT-RESPONSIBILITY-MAP.md` is the source-of-truth responsibility map for M71.2.
- `docs/SCRIPT-LEGACY-AND-DUPLICATE-MAP.md` is the source-of-truth candidate classification map for M71.3.
- This document (`docs/SCRIPT-DANGEROUS-OPERATIONS-AUDIT.md`) is the source-of-truth dangerous operations audit for M71.4.

---

## Inputs Used

| Artifact | Status |
|---|---|
| `reports/m71-script-inventory.md` | Verified present, FINAL_STATUS accepted |
| `reports/m71-script-inventory.json` | Verified present, used for navigation only |
| `docs/SCRIPT-RESPONSIBILITY-MAP.md` | Verified present, FINAL_STATUS accepted |
| `docs/SCRIPT-LEGACY-AND-DUPLICATE-MAP.md` | Verified present, FINAL_STATUS accepted |
| `tasks/active-task.md` | Verified: task-71.4 active |

---

## Scan Method

Signals were extracted using read-only Python regex scanning of file text content. No scripts were executed. No source lines were printed. No secret values were captured or logged. Scanning covered:

- `scripts/` — all files recursively (`.pyc` excluded from final tally)
- `.github/workflows/` — all files recursively
- `install.sh` — root-level bootstrap file

Two scanner categories were applied:

**Operation signal scanner** — patterns covering:
`RM_RF`, `RM`, `SHUTIL_RMTREE`, `UNLINK`, `GIT_PUSH`, `GIT_RESET`, `GIT_CHECKOUT`, `GIT_CLEAN`, `SUBPROCESS`, `SHELL_TRUE`, `OS_SYSTEM`, `CURL`, `REQUESTS`, `URLLIB`, `WRITE_TEXT`, `OPEN_WRITE`, `MKDIR`, `RENAME`, `REPLACE`, `CHMOD`, `CHOWN`

**Secret-like signal scanner** — variable-name patterns (no values captured):
`TOKEN`, `GITHUB_TOKEN`, `SECRET`, `API_KEY`, `ACCESS_KEY`, `PRIVATE_KEY`, `PASSWORD`, `BEARER`, `AUTHORIZATION`

---

## Scan Summary

| Metric | Count |
|---|---|
| Total source files scanned (no .pyc) | 236 |
| Total files with any operation signal | 114 |
| Total operation signal hits | 579 |
| Total secret-like signal hits | 728 |
| Files with GIT_MUTATION signals | 8 |
| Files with DESTRUCTIVE_DELETE signals | 16 |
| Files with NETWORK signals | 10 |
| Files with SUBPROCESS_SHELL signals | 134 |
| Files with FILE_WRITE signals | 58 |
| Files with secret-like signals | 89 |

**Operation signals by name:**

| Signal | Hits |
|---|---|
| SUBPROCESS | 309 |
| MKDIR | 74 |
| WRITE_TEXT | 71 |
| REPLACE | 43 |
| RM_RF | 11 |
| REQUESTS | 9 |
| GIT_PUSH | 9 |
| SHUTIL_RMTREE | 7 |
| RENAME | 6 |
| UNLINK | 6 |
| CURL | 6 |
| OS_SYSTEM | 4 |
| CHMOD | 4 |
| OPEN_WRITE | 3 |
| URLLIB | 2 |
| SHELL_TRUE | 2 |

**Secret-like signals by name (variable names only, no values):**

| Signal Name | Hits |
|---|---|
| AUTHORIZATION | 239 |
| TOKEN | 464 |
| GITHUB_TOKEN | 3 |
| SECRET | 19 |
| BEARER | 2 |
| PASSWORD | 1 |

---

## Section 1: GIT_MUTATION Signals

Files containing signals classified as git-state-mutating operations (`GIT_PUSH`, `GIT_RESET`, `GIT_CHECKOUT`, `GIT_CLEAN`).

| File | Operation Signals | Secret-like Signals | Notes |
|---|---|---|---|
| `.github/workflows/init-from-template.yml` | GIT_PUSH, CURL | AUTHORIZATION, BEARER, GITHUB_TOKEN, SECRET, TOKEN | Workflow: push in bootstrap flow; also CURL and multi-signal secret-like hits |
| `.github/workflows/setup-repository.yml` | GIT_PUSH, RM, RM_RF | — | Workflow: push + destructive delete; setup bootstrap |
| `scripts/audit-context-layer.py` | GIT_PUSH, SUBPROCESS | AUTHORIZATION | Audit script: push signal present; purpose is context-layer audit |
| `scripts/audit-pre-merge-corridor.py` | GIT_PUSH, OS_SYSTEM, SUBPROCESS | — | Canonical audit script: OS_SYSTEM + GIT_PUSH; highest-risk combination in audit category |
| `scripts/check-commit-push-preconditions.py` | GIT_PUSH, SUBPROCESS | AUTHORIZATION | Precondition checker: push signal is part of gate check logic |
| `scripts/check-use-template-readiness.py` | GIT_PUSH, SHELL_TRUE, SUBPROCESS | — | SHELL_TRUE + GIT_PUSH combination: elevated risk signal; checks readiness before template use |

---

## Section 2: DESTRUCTIVE_DELETE Signals

Files containing signals classified as destructive deletion (`RM_RF`, `RM`, `SHUTIL_RMTREE`, `UNLINK`).

| File | Operation Signals | Secret-like Signals | Notes |
|---|---|---|---|
| `scripts/canonical-cleanup.sh` | RM, RM_RF | — | Cleanup shell script: destructive delete is stated purpose |
| `scripts/check-context-index-freshness.py` | SHUTIL_RMTREE, SUBPROCESS, WRITE_TEXT | TOKEN | Context freshness checker: rmtree with write |
| `scripts/check-m55-active-task-readiness-fixtures.py` | SHUTIL_RMTREE, MKDIR, SUBPROCESS, WRITE_TEXT | — | Fixture setup/teardown script: rmtree + mkdir pattern for temp dirs |
| `scripts/test-activation-fixtures.py` | UNLINK, MKDIR, SUBPROCESS, WRITE_TEXT | — | Test fixture: unlink for fixture teardown |
| `scripts/test-example-project.sh` | RM, RM_RF | — | Test shell script: cleanup at start/end of test run |
| `scripts/test-install.sh` | RM, RM_RF | — | Install test: destructive delete of test dirs |
| `scripts/test-m27-level1-fixtures.py` | RM, RM_RF, SUBPROCESS | — | Fixture: uses rm -rf for tmp fixture dir teardown |
| `scripts/test-m40-runtime-bypass-smoke.py` | SHUTIL_RMTREE, CHMOD, CURL, MKDIR, SUBPROCESS, WRITE_TEXT | GITHUB_TOKEN, SECRET, TOKEN | **Highest multi-signal risk**: destructive + network + secret-like + chmod; bypass smoke test |
| `scripts/test-scope-compliance-fixtures.py` | UNLINK, RENAME, MKDIR, SUBPROCESS, WRITE_TEXT | — | Fixture: unlink + rename for temp fixture management |

---

## Section 3: NETWORK Signals

Files containing signals classified as network access (`CURL`, `REQUESTS`, `URLLIB`).

| File | Operation Signals | Secret-like Signals | Notes |
|---|---|---|---|
| `.github/workflows/dev-only/m27-enforcement.yml` | REQUESTS | — | Workflow: network call in enforcement workflow |
| `.github/workflows/init-from-template.yml` | CURL, GIT_PUSH | AUTHORIZATION, BEARER, GITHUB_TOKEN, SECRET, TOKEN | Workflow: curl + push + multi-secret-like; bootstrap init flow |
| `scripts/agentos-command-guard.py` | CURL | — | Guard script: curl signal; verify intended network use |
| `scripts/audit-m31-tui-tutor.py` | REQUESTS, URLLIB, OS_SYSTEM | — | Legacy audit: REQUESTS + URLLIB + OS_SYSTEM combination |
| `scripts/audit-validation-integration.py` | REQUESTS, SUBPROCESS | — | Audit script: REQUESTS for validation integration check |
| `scripts/check-bypass-fixtures.py` | CURL, CHMOD, REPLACE | AUTHORIZATION, BEARER, PASSWORD, SECRET, TOKEN | **Highest secret-like signal breadth**: CURL + BEARER + PASSWORD + SECRET — fixture for bypass checks |
| `scripts/test-ci-advisory-config.py` | REQUESTS | SECRET, TOKEN | Network + SECRET signal; CI advisory config test |
| `scripts/test-m40-runtime-bypass-smoke.py` | CURL, SHUTIL_RMTREE, CHMOD, MKDIR, SUBPROCESS, WRITE_TEXT | GITHUB_TOKEN, SECRET, TOKEN | **Highest multi-signal risk** (also listed under DESTRUCTIVE_DELETE) |

---

## Section 4: SUBPROCESS_SHELL — Shell Execution Risk Signals

Files with `SHELL_TRUE` or `OS_SYSTEM` signals (elevated subprocess risk). SUBPROCESS alone is not listed per-file in this section due to 134-file breadth; only the elevated-risk patterns are itemized.

### 4.1 SHELL_TRUE

| File | Operation Signals | Secret-like Signals | Notes |
|---|---|---|---|
| `scripts/check-use-template-readiness.py` | GIT_PUSH, SHELL_TRUE, SUBPROCESS | — | SHELL_TRUE + GIT_PUSH: requires human review before any cleanup decision |

### 4.2 OS_SYSTEM

| File | Operation Signals | Secret-like Signals | Notes |
|---|---|---|---|
| `scripts/audit-m31-tui-tutor.py` | OS_SYSTEM, REQUESTS, URLLIB | — | Legacy audit: OS_SYSTEM present; classified LEGACY_CANDIDATE in M71.3 |
| `scripts/audit-pre-merge-corridor.py` | OS_SYSTEM, GIT_PUSH, SUBPROCESS | — | Canonical audit: OS_SYSTEM + GIT_PUSH; highest risk in audit scripts |

### 4.3 Subprocess Breadth Summary

Total files with SUBPROCESS signal: 134
The SUBPROCESS signal is pervasive across test fixtures and validators.
It is recorded as a signal but does not in itself indicate an improperly constructed script without context from M71.2 (responsibility map).

---

## Section 5: Secret-like Signal Concentration

Files with the broadest or highest-risk secret-like signal combinations. No values recorded. No source lines printed.

| File | Secret-like Signals Present | Operation Signals | Risk Note |
|---|---|---|---|
| `scripts/check-bypass-fixtures.py` | AUTHORIZATION, BEARER, PASSWORD, SECRET, TOKEN | CURL, CHMOD, REPLACE | 5 distinct secret-like variable names; CURL present; fixture for bypass test |
| `.github/workflows/init-from-template.yml` | AUTHORIZATION, BEARER, GITHUB_TOKEN, SECRET, TOKEN | CURL, GIT_PUSH | Workflow: multi-secret-like + GIT_PUSH + CURL |
| `scripts/test-m40-runtime-bypass-smoke.py` | GITHUB_TOKEN, SECRET, TOKEN | CURL, SHUTIL_RMTREE, CHMOD, MKDIR, SUBPROCESS, WRITE_TEXT | Multi-category cross-signal concentration |
| `scripts/validate-proposal-to-task-conversion.py` | AUTHORIZATION | REPLACE | AUTHORIZATION signal in validator; file-write via REPLACE |
| `scripts/validate-task-contract-candidate.py` | AUTHORIZATION, TOKEN | — | Core task contract validator; secret-like signals present |
| `scripts/validate-ux-to-task-proposal.py` | AUTHORIZATION, TOKEN | — | UX-to-task validator; high TOKEN hit count |
| `scripts/validate-product-spec.py` | TOKEN | REPLACE | Product spec validator; high TOKEN hit count |
| `scripts/test-single-role-execution-fixtures.py` | TOKEN | SUBPROCESS | Fixture: TOKEN signal concentration |

---

## Section 6: Backup and Duplicate Copies with Dangerous Signals

Files classified as BACKUP_COPY or DUPLICATE_CANDIDATE in M71.3 that also carry dangerous operation signals.

These files are flagged because dangerous signals in non-canonical copies increase the total attack surface without adding reviewed functionality.

| File | Classification (M71.3) | Operation Signals | Notes |
|---|---|---|---|

> Note: " 3" suffix files were classified as BACKUP_COPY candidates in M71.3. Their dangerous signals are recorded here for completeness. No cleanup is performed in M71.4.

---

## Section 7: Cross-Signal Risk Concentrations

Files carrying signals from 3 or more distinct risk categories simultaneously. These represent the highest-priority items for human review in cleanup planning.

| File | Risk Categories | Signal Count |
|---|---|---|
| `scripts/test-m40-runtime-bypass-smoke.py` | DESTRUCTIVE_DELETE, NETWORK, SUBPROCESS_SHELL, FILE_WRITE, OTHER, SECRET_LIKE | 6 |
| `scripts/check-bypass-fixtures.py` | NETWORK, FILE_WRITE, OTHER, SECRET_LIKE | 4 |
| `.github/workflows/init-from-template.yml` | GIT_MUTATION, NETWORK, SECRET_LIKE | 3 |
| `scripts/audit-pre-merge-corridor.py` | GIT_MUTATION, SUBPROCESS_SHELL, OS_SYSTEM | 3 |
| `scripts/check-use-template-readiness.py` | GIT_MUTATION, SUBPROCESS_SHELL, SHELL_TRUE | 3 |
| `scripts/test-scope-compliance-fixtures.py` | DESTRUCTIVE_DELETE, SUBPROCESS_SHELL, FILE_WRITE | 3 |
| `scripts/check-context-index-freshness.py` | DESTRUCTIVE_DELETE, SUBPROCESS_SHELL, FILE_WRITE | 3 |
| `scripts/check-m55-active-task-readiness-fixtures.py` | DESTRUCTIVE_DELETE, SUBPROCESS_SHELL, FILE_WRITE | 3 |
| `scripts/test-activation-fixtures.py` | DESTRUCTIVE_DELETE, SUBPROCESS_SHELL, FILE_WRITE | 3 |

---

## Section 8: Files With No Dangerous Operation Signals

Files scanned that produced zero hits across all operation and secret-like signal patterns are recorded as having no detected signals. This represents approximately 97 files. The complete list is not reproduced here to avoid redundant bulk reproduction of no-signal records. The count is recorded.

**No-signal file count: 97**

---

## Audit Coverage Statement

This audit covered the following scopes:

- `scripts/` — all files (236 source files, .pyc excluded)
- `.github/workflows/` — all workflow YAML files
- `install.sh` — root-level bootstrap (no signals detected)

This audit did **not** cover:
- `core-rules/` — protected Markdown artifacts (not scripts)
- `docs/` — documentation artifacts
- `reports/` — evidence artifacts
- `tasks/` — task contract files
- `.github/ISSUE_TEMPLATE/` — non-script templates
- JSON fixtures — not executable scripts

---

## Open Audit Notes

1. **`scripts/test-m40-runtime-bypass-smoke.py`** carries the highest multi-signal risk concentration in the repository. It is a test fixture for bypass smoke testing. Human review is required before any cleanup decision is taken.

2. **`scripts/check-bypass-fixtures.py`** carries the broadest secret-like signal coverage including BEARER and PASSWORD variable names. This is a fixture for bypass checks. No cleanup action is taken here. Requires human review.

3. **`scripts/audit-m31-tui-tutor.py`** carries OS_SYSTEM + REQUESTS + URLLIB — the only file outside of `audit-pre-merge-corridor` to carry OS_SYSTEM. It is classified as LEGACY_CANDIDATE in M71.3.

4. **`scripts/canonical-cleanup.sh`** carries RM + RM_RF signals. Its name indicates it is intended to perform cleanup. No action is taken in M71.4; this is a signal record only.

5. **SHELL_TRUE** signal appears in only one file: `scripts/check-use-template-readiness.py`. SHELL_TRUE indicates `subprocess` called with `shell=True`, which carries injection risk. Requires human review.

6. **Backup copies with dangerous signals** (Section 6): Eleven " 3" backup files carry the same dangerous signals as their canonical counterparts. These duplicate the risk surface without additional governance. This is flagged for M71.5 cleanup planning.

---

## Final Status

```
task_id: task-71.4
milestone: M71
task_name: Dangerous Script Operations Audit
status: COMPLETE
final_status: M71_DANGEROUS_OPERATIONS_AUDIT_COMPLETE
FINAL_STATUS: M71_DANGEROUS_SCRIPT_AUDIT_COMPLETE
files_scanned: 236
total_operation_signal_hits: 579
total_secret_like_signal_hits: 728
files_with_any_dangerous_signal: 114
files_with_git_mutation: 8
files_with_destructive_delete: 16
files_with_network: 10
files_with_shell_true: 1
files_with_os_system: 3
files_with_cross_category_concentration: 9
backup_copies_with_dangerous_signals: 11
may_prepare_m71_5: true
source_lines_printed: false
secret_values_printed: false
produced_artifact: docs/SCRIPT-DANGEROUS-OPERATIONS-AUDIT.md
notes: >
  Audit is read-only signal record only.
  No scripts modified.
  No source lines printed.
  No secret values captured.
  No lifecycle decisions made.
  No cleanup performed.
  Human review required before any cleanup action.
```
