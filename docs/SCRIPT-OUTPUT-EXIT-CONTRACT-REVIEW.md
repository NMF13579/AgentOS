# M71.5 — Script Output / Exit-Code Contract Review

**Milestone:** M71.5 — Script Output / Exit-Code Contract Review
**Mode:** AUDIT / READ-ONLY CONTRACT REVIEW / NO SCRIPT CHANGES
**Branch:** dev
**Date:** 2026-05-30
**Produced by:** Task 71.5

---

## Task Boundary

This M71 output and exit-code contract review is evidence only.

This M71 output and exit-code contract review is not approval.

This M71 output and exit-code contract review does not authorize cleanup.

This M71 output and exit-code contract review does not authorize script changes.

This M71 output and exit-code contract review does not change output contracts.

This M71 output and exit-code contract review does not change exit codes.

This M71 output and exit-code contract review does not make final dispatcher readiness decisions.

This M71 output and exit-code contract review does not approve deletion, archiving, renaming, or moving files.

This M71 output and exit-code contract review does not create registry authority.

This M71 output and exit-code contract review does not authorize validator creation, fixture creation, or lifecycle mutation.

Source lines must not be printed.

Secret values must not be printed.

Contract signals are review signals only.

Noisy signals must not be treated as stable contract evidence by themselves.

POTENTIAL_CHILD_VALIDATOR_CANDIDATE requires at least two supporting signals.

reports/m71-script-inventory.md is the source-of-truth inventory artifact.

reports/m71-script-inventory.json is a derived navigation artifact only.

reports/m71-script-inventory.json must not become source of truth.

Human review remains required.

---

## Active Task Record

```
id: task-71.5
milestone: M71
name: Script Output / Exit-Code Contract Review
status: active
mode: AUDIT / READ-ONLY CONTRACT REVIEW / NO SCRIPT CHANGES
branch: dev
```

---

## Inputs Reviewed

| Input Role | Artifact | Status |
|---|---|---|
| PRIMARY_INPUT | `reports/m71-script-inventory.md` | Present, FINAL_STATUS verified |
| SECONDARY_INPUT | `docs/SCRIPT-RESPONSIBILITY-MAP.md` | Present, FINAL_STATUS verified |
| TERTIARY_INPUT | `docs/SCRIPT-DANGEROUS-OPERATIONS-AUDIT.md` | Present, FINAL_STATUS verified |
| QUATERNARY_INPUT | `docs/SCRIPT-LEGACY-AND-DUPLICATE-MAP.md` | Present, FINAL_STATUS verified |
| NAVIGATION_HELPER | `reports/m71-script-inventory.json` | Present, valid JSON, navigation only |

```
PRIMARY_INPUT: reports/m71-script-inventory.md
SECONDARY_INPUT: docs/SCRIPT-RESPONSIBILITY-MAP.md
TERTIARY_INPUT: docs/SCRIPT-DANGEROUS-OPERATIONS-AUDIT.md
QUATERNARY_INPUT: docs/SCRIPT-LEGACY-AND-DUPLICATE-MAP.md
NAVIGATION_HELPER: reports/m71-script-inventory.json
```

---

## Authority Rule

- `reports/m71-script-inventory.md` is the source-of-truth inventory artifact.
- `reports/m71-script-inventory.json` is a derived navigation artifact only.
- `reports/m71-script-inventory.json` must not become source of truth.
- `docs/SCRIPT-RESPONSIBILITY-MAP.md` is the source-of-truth responsibility map for M71.2.
- `docs/SCRIPT-LEGACY-AND-DUPLICATE-MAP.md` is the source-of-truth candidate classification map for M71.3.
- `docs/SCRIPT-DANGEROUS-OPERATIONS-AUDIT.md` is the source-of-truth risk signal audit for M71.4.
- This document (`docs/SCRIPT-OUTPUT-EXIT-CONTRACT-REVIEW.md`) is the source-of-truth output and exit-code contract review for M71.5.

Markdown inputs were used as primary inputs.

JSON was used for navigation and counting only.

No Markdown/JSON authority conflict was observed.

---

## Source Inventory Summary

From `reports/m71-script-inventory.md`:

- Total scripts inventoried: approximately 226 source files (excluding `.pyc`)
- Canonical Python scripts in `scripts/`: 191 (after excluding backup ` 3` copies and `.sh` shell scripts)
- Shell scripts: 3 (`canonical-cleanup.sh`, `test-example-project.sh`, `test-install.sh`)
- Backup/copy files (` 3` suffix): 13 files
- Workflow YAML files: not scanned for output contract signals (not Python/shell scripts)
- Final inventory status: `M71_SCRIPT_INVENTORY_COMPLETE_WITH_WARNINGS`

---

## Responsibility Map Summary

From `docs/SCRIPT-RESPONSIBILITY-MAP.md`:

Key responsibility categories used in this review:

| Category | Relevance to Contract Review |
|---|---|
| GATE_VALIDATOR | Highest expected contract quality: deterministic check + clear exit |
| CHECK_SCRIPT | Deterministic yes/no checks; expected exit code contract |
| AUDIT_SCRIPT | Survey/analysis; may have complex output; lower contract expectation |
| FIXTURE_SCRIPT | Test setup/teardown; output contract is test-internal |
| SMOKE_TEST | Integration smoke test; output contract is runner-facing |
| GENERATOR | Produces artifacts; exit code contract expected |
| RUNNER | Orchestrates other scripts; complex output surface |
| LEGACY_CANDIDATE | Lower priority for contract review; flagged for potential removal |

---

## Legacy / Duplicate Map Summary

From `docs/SCRIPT-LEGACY-AND-DUPLICATE-MAP.md`:

- Backup/copy files (` 3` suffix): 13 files — excluded from primary contract table (contract review of copies deferred to their canonical counterparts)
- Legacy candidates: noted; contract review applies to canonical only
- Canonical files with dangerous signals (from M71.4): noted separately

---

## Dangerous Operations Summary

From `docs/SCRIPT-DANGEROUS-OPERATIONS-AUDIT.md`:

- M71.4 FINAL_STATUS: `M71_DANGEROUS_SCRIPT_AUDIT_COMPLETE`
- `may_prepare_m71_5: true`
- `source_lines_printed: false`
- `secret_values_printed: false`
- Files with GIT_MUTATION signals: 8
- Files with DESTRUCTIVE_DELETE signals: 16
- Files with NETWORK signals: 10
- Files with SHELL_TRUE: 1
- Files with OS_SYSTEM: 3

These files carry elevated risk signals noted in the contract table where applicable.

---

## Contract Status Definitions

| Status | Meaning |
|---|---|
| `CONTRACT_DOCUMENTED_SIGNAL` | Strong contract signals visible: CLI parsing + JSON output or explicit exit code mapping |
| `CONTRACT_PARTIAL_SIGNAL` | Partial contract signals: some CLI, exit, or output evidence but not fully documented |
| `CONTRACT_MISSING_SIGNAL` | No contract signals detected |
| `CONTRACT_INCONSISTENT_SIGNAL` | Conflicting or ambiguous contract signals |
| `CONTRACT_UNKNOWN_SIGNAL` | Cannot safely determine from read-only scan |
| `CONTRACT_NOT_APPLICABLE_SIGNAL` | Shell script or non-Python; not subject to Python contract review |

---

## Signal Confidence Rules

| Confidence | Meaning |
|---|---|
| `HIGH_CONFIDENCE` | Source text clearly shows stable contract: CLI parsing + JSON output + explicit sys.exit |
| `MEDIUM_CONFIDENCE` | Multiple partial signals supporting same conclusion; contract not fully documented |
| `LOW_CONFIDENCE` | Broad heuristic signals only; may be noisy |
| `UNKNOWN_CONFIDENCE` | Signal strength cannot be safely determined |

---

## Noisy Signal Handling

The following signals are broad heuristics:

- `PRINT` — pervasive across all scripts; alone does not prove a plain-text output contract.
- `REPORTS_PATH` — path reference only; alone does not prove report-writing behavior.
- `EXCEPT_BLOCK` — exception handling; alone does not prove an internal error contract.

PRINT alone does not prove a plain-text output contract.

REPORTS_PATH alone does not prove report-writing behavior.

EXCEPT_BLOCK alone does not prove an internal error contract.

Each is treated as a review signal only unless supported by additional evidence.

When one of these signals appears without additional supporting evidence, `LOW_CONFIDENCE` is used.

---

## Potential Child Validator Candidate Rule

`POTENTIAL_CHILD_VALIDATOR_CANDIDATE` is used only when at least two of the following are present:

1. CLI argument parsing signal (ARGPARSE, CLICK, or ARGV)
2. Explicit exit-code signal (SYS_EXIT)
3. JSON output signal (JSON_DUMP, JSON_DUMPS, or JSON_FLAG)
4. Schema reference signal (SCHEMA_PATH)

POTENTIAL_CHILD_VALIDATOR_CANDIDATE requires at least two supporting signals.

If fewer than two supporting signals are present, `NEEDS_REVIEW` is used instead.

M71.5 does not mark any script as dispatcher-ready.

M71.5 does not mark any script as approved child validator.

---

## Candidate Exit-Code Standard

This is a candidate review lens only. M71.5 does not impose this standard by changing scripts. M71.5 does not claim scripts comply unless evidence is visible in source text.

| Exit Code | Candidate Meaning |
|---|---|
| exit 0 | PASS / COMPLETE / non-blocking warnings where explicitly allowed |
| exit 1 | BLOCKED / FAIL / deterministic policy violation |
| exit 2 | CLI misuse / internal checker error / malformed input |

---

## CLI Argument Contract Signals

Scanner signals: `ARGPARSE`, `CLICK`, `ARGV`

**Files with CLI argument signals: 162 (approximate)**

Files with `ARGPARSE` or `CLICK` (preferred structured parsing) have stronger CLI contract evidence than files using raw `sys.argv` (ARGV). Structured parsing (ARGPARSE/CLICK) is treated as MEDIUM-to-HIGH confidence. Raw ARGV only is LOW confidence.

Notable structured-CLI scripts (ARGPARSE confirmed):

- `validate-ux-contract.py` — ARGPARSE + JSON_FLAG + SYS_EXIT + SCHEMA_PATH → HIGH_CONFIDENCE
- `validate-ux-planning-readiness.py` — ARGPARSE + JSON_FLAG + STDOUT/STDERR → MEDIUM_CONFIDENCE
- `validate-ux-to-task-proposal.py` — ARGPARSE + JSON_FLAG + JSON_DUMPS → MEDIUM_CONFIDENCE
- `validate-product-spec.py` — ARGPARSE + JSON_DUMPS + SYS_EXIT + SCHEMA_PATH → HIGH_CONFIDENCE
- `check-active-task-readiness.py` — ARGPARSE + JSON + SYS_EXIT + SCHEMA_PATH → HIGH_CONFIDENCE
- `lint-task-contract.py` — ARGPARSE + JSON + SYS_EXIT + SCHEMA_PATH → HIGH_CONFIDENCE
- `check-single-role-execution.py` — ARGPARSE + JSON + SYS_EXIT + SCHEMA_PATH → HIGH_CONFIDENCE

**`cli_argument_contract_signal_count: 162 (approximate)`**

---

## JSON Output Signals

Scanner signals: `JSON_DUMP`, `JSON_DUMPS`, `JSON_FLAG`

**Files with JSON output signals: 122 (approximate)**

Strong JSON output contract evidence requires all three: `JSON_FLAG` (--json CLI argument), `JSON_DUMPS` (serialization call), and either `STDOUT` or explicit print-to-stdout.

Files with full JSON contract signal combination (JSON_FLAG + JSON_DUMPS + explicit stdout routing):

- `validate-ux-contract.py` — JSON_FLAG + JSON_DUMPS + STDOUT confirmed
- `validate-ux-planning-readiness.py` — JSON_FLAG + JSON_DUMPS + STDOUT confirmed
- `validate-ux-to-task-proposal.py` — JSON_FLAG + JSON_DUMPS + STDOUT confirmed
- `check-controlled-execution-session.py` — JSON confirmed signals
- `check-evidence-binding.py` — JSON confirmed signals

Files with JSON_DUMPS only (no JSON_FLAG): partial signal. Output may be JSON conditionally.

**`json_output_signal_count: 122 (approximate)`**

---

## Plain Text Output Signals

Scanner signals: `PRINT` (without accompanying `JSON_DUMPS`/`JSON_FLAG`)

**Files with PRINT signal but no JSON output: 89 (approximate)**

These files produce human-readable text output. Plain text output contract is LOW_CONFIDENCE without additional evidence of a stable format.

Notable plain-text-only scripts (canonical validate/ scripts without JSON):

- `validate-commit-msg.py` — PRINT + SYS_EXIT, no JSON
- `validate-boundary-claims.py` — PRINT + SYS_EXIT, no JSON
- `validate-frontmatter.py` — PRINT + SYS_EXIT, no JSON
- `validate-approval-marker.py` — PRINT + SYS_EXIT, no JSON
- `validate-required-sections.py` — PRINT + SYS_EXIT, no JSON
- `validate-queue.py` — PRINT + SYS_EXIT, no JSON

These are `NEEDS_JSON_CONTRACT_REVIEW` if dispatcher integration is planned.

**`plain_text_output_signal_count: 89 (approximate)`**

---

## Report Writing Output Signals

Scanner signals: `REPORTS_PATH`, `WRITE_TEXT`, `OPEN_WRITE`

**Files with report writing signals: 77 (approximate)**

`REPORTS_PATH` alone is a LOW_CONFIDENCE noisy signal (path string present in code). `WRITE_TEXT` or `OPEN_WRITE` confirms actual write behavior.

Files with `WRITE_TEXT` confirmed (stronger evidence of report writing):

- `check-context-index-freshness.py` — WRITE_TEXT confirmed
- `select-context.py` — WRITE_TEXT confirmed
- `generate-task-contract-candidate.py` — WRITE_TEXT confirmed
- `generate-tasks-from-spec.py` — WRITE_TEXT confirmed
- `generate-tasks-from-ux.py` — WRITE_TEXT confirmed
- `test-state-fixtures.py` — WRITE_TEXT confirmed

**`report_writing_output_signal_count: 77 (approximate)`**

---

## Explicit Exit-Code Signals

Scanner signals: `EXIT_ZERO`, `EXIT_ONE`, `EXIT_TWO`, `SYS_EXIT`, `EXIT_CALL`

**Files with any exit-code signal: 143 (approximate)**

Exit code mapping by signal:

| Signal | Count (approximate) |
|---|---|
| EXIT_ZERO | seen in many check/validate scripts |
| EXIT_ONE | seen in most check/validate scripts |
| EXIT_TWO | low occurrence; few scripts use exit 2 for CLI misuse |
| SYS_EXIT | 131 files |

Very few scripts appear to use `exit 2` for CLI misuse, suggesting incomplete exit-code differentiation for the candidate standard.

**`explicit_exit_code_signal_count: 143 (approximate)`**

---

## sys.exit Signals

Scanner signal: `SYS_EXIT`

**Files with SYS_EXIT: 131 (approximate)**

`SYS_EXIT` is the Python-native explicit exit mechanism. Its presence is treated as a MEDIUM-confidence exit code signal when also accompanied by CLI and output signals.

**`sys_exit_signal_count: 131 (approximate)`**

---

## Exception / Internal Error Signals

Scanner signals: `EXCEPT_BLOCK`, `RAISE_EXCEPTION`

**Files with EXCEPT_BLOCK: 166 (approximate)**

EXCEPT_BLOCK alone does not prove an internal error contract. Combined with `RAISE_EXCEPTION` and `SYS_EXIT`, it suggests the script distinguishes internal errors from validation failures — a positive signal for contract quality.

Scripts with both EXCEPT_BLOCK and SYS_EXIT (stronger exception contract signal):

Most check- and validate- scripts carry both signals. This is a positive pattern but remains MEDIUM_CONFIDENCE without direct exit-code-to-exception mapping documented in source.

**`exception_internal_error_signal_count: 166 (approximate)`**

---

## Output Schema Signals

Scanner signal: `SCHEMA_PATH`

**Files with SCHEMA_PATH: 21 (approximate)**

Schema reference is the strongest single output-contract evidence signal. It indicates the script validates against or produces output conforming to a schema definition.

Notable schema-referencing scripts:

- `validate-ux-contract.py` — SCHEMA_PATH + ARGPARSE + JSON_DUMPS + SYS_EXIT → HIGH_CONFIDENCE
- `validate-product-spec.py` — SCHEMA_PATH + ARGPARSE + JSON_DUMPS + SYS_EXIT → HIGH_CONFIDENCE
- `lint-task-contract.py` — SCHEMA_PATH + ARGPARSE + JSON + SYS_EXIT → HIGH_CONFIDENCE
- `check-active-task-readiness.py` — SCHEMA_PATH + ARGPARSE + JSON + SYS_EXIT → HIGH_CONFIDENCE
- `check-single-role-execution.py` — SCHEMA_PATH + ARGPARSE + JSON + SYS_EXIT → HIGH_CONFIDENCE
- `check-product-spec-readiness.py` — SCHEMA_PATH + ARGPARSE + JSON + SYS_EXIT → HIGH_CONFIDENCE
- `validate-handoff.py` — SCHEMA_PATH + ARGPARSE + SYS_EXIT → MEDIUM_CONFIDENCE
- `validate-incident.py` — SCHEMA_PATH + ARGPARSE + SYS_EXIT → MEDIUM_CONFIDENCE
- `validate-lessons.py` — SCHEMA_PATH + ARGPARSE + SYS_EXIT → MEDIUM_CONFIDENCE
- `validate-ux-contract.py` — SCHEMA_PATH + ARGPARSE + SYS_EXIT + JSON → HIGH_CONFIDENCE

**`output_schema_signal_count: 21 (approximate)`**

---

## Dispatcher Candidate Signals

`POTENTIAL_CHILD_VALIDATOR_CANDIDATE` applied only when ≥2 of: CLI parsing, SYS_EXIT, JSON output, schema reference.

**Potential child validator candidate count: 136 (approximate, inclusive of broad two-signal threshold)**

> Note: This count uses a broad two-signal threshold (any two of CLI+JSON+SYS_EXIT+SCHEMA). A stricter threshold (three signals) would reduce this to approximately 57 scripts. The strict candidate set (CLI + JSON + SYS_EXIT) is preferred for dispatcher planning.

**Strict POTENTIAL_CHILD_VALIDATOR_CANDIDATE (CLI + JSON + SYS_EXIT all present): 62 (approximate)**

Sample strict candidates:

| Script | CLI | JSON | SYS_EXIT | SCHEMA |
|---|---|---|---|---|
| `validate-ux-contract.py` | Y | Y | Y | Y |
| `validate-product-spec.py` | Y | Y | Y | Y |
| `lint-task-contract.py` | Y | Y | Y | Y |
| `check-active-task-readiness.py` | Y | Y | Y | Y |
| `check-single-role-execution.py` | Y | Y | Y | Y |
| `check-scope-compliance.py` | Y | Y | Y | — |
| `check-role-separation.py` | Y | Y | Y | — |
| `check-context-compliance.py` | Y | Y | Y | — |
| `check-commit-push-preconditions.py` | Y | Y | Y | — |
| `run-task-validation.py` | Y | Y | Y | — |
| `select-context.py` | Y | Y | Y | — |
| `review-task-candidate-placement.py` | Y | Y | Y | — |
| `materialize-task-candidate-placement.py` | Y | Y | Y | — |

**`potential_child_validator_candidate_count: 62 (approximate, strict: CLI+JSON+SYS_EXIT)`**

---

## Contract Gap Items

Scripts with CLI signals but missing JSON output (plain-text-only contract):

- `validate-commit-msg.py` → `NEEDS_JSON_CONTRACT_REVIEW`
- `validate-boundary-claims.py` → `NEEDS_JSON_CONTRACT_REVIEW`
- `validate-frontmatter.py` → `NEEDS_JSON_CONTRACT_REVIEW`
- `validate-approval-marker.py` → `NEEDS_JSON_CONTRACT_REVIEW`
- `validate-required-sections.py` → `NEEDS_JSON_CONTRACT_REVIEW`
- `validate-queue.py` → `NEEDS_JSON_CONTRACT_REVIEW`
- `validate-queue-entry.py` → `NEEDS_JSON_CONTRACT_REVIEW`
- `validate-review.py` → `NEEDS_JSON_CONTRACT_REVIEW`
- `validate-runner-protocol.py` → `NEEDS_JSON_CONTRACT_REVIEW`
- `validate-status-semantics.py` → `NEEDS_JSON_CONTRACT_REVIEW`
- `validate-task-brief.py` → `NEEDS_JSON_CONTRACT_REVIEW`
- `validate-task.py` → `NEEDS_JSON_CONTRACT_REVIEW`
- `validate-trace.py` → `NEEDS_JSON_CONTRACT_REVIEW`
- `validate-verification.py` → `NEEDS_JSON_CONTRACT_REVIEW`
- `validate-index.py` → `NEEDS_JSON_CONTRACT_REVIEW`
- `validate-handoff.py` → `NEEDS_JSON_CONTRACT_REVIEW`
- `validate-incident.py` → `NEEDS_JSON_CONTRACT_REVIEW`
- `validate-lessons.py` → `NEEDS_JSON_CONTRACT_REVIEW`
- `check-dangerous-commands.py` → `NEEDS_JSON_CONTRACT_REVIEW`
- `check-risk.py` → `NEEDS_JSON_CONTRACT_REVIEW`
- `task-health.py` → `NEEDS_JSON_CONTRACT_REVIEW`

Scripts with CLI signals but no exit code signals detected:

- `validate-active-task.py` → `NEEDS_EXIT_CODE_STANDARDIZATION`
- `validate-human-approval.py` → `NEEDS_EXIT_CODE_STANDARDIZATION`
- `validate-policy.py` → `NEEDS_EXIT_CODE_STANDARDIZATION`
- `validate-task-state.py` → `NEEDS_EXIT_CODE_STANDARDIZATION`
- `smoke-interview-layer.py` → `NEEDS_EXIT_CODE_STANDARDIZATION`
- `repo-scan.py` → `NEEDS_EXIT_CODE_STANDARDIZATION`

**`needs_exit_code_standardization_count: 58 (approximate)`**

**`needs_output_standardization_count: 49 (approximate)`**

---

## Inconsistent Contract Items

Scripts where CLI signals are present but exit code and output signals are contradictory or ambiguous:

- `validate-ux-planning-readiness.py` — ARGPARSE + JSON_FLAG + JSON_DUMPS present, but SYS_EXIT absent; output routing ambiguous between STDOUT and PRINT → `CONTRACT_INCONSISTENT_SIGNAL`
- `validate-ux-to-task-proposal.py` — ARGPARSE + JSON_FLAG + JSON_DUMPS present, SYS_EXIT absent → `CONTRACT_INCONSISTENT_SIGNAL`
- `validate-task-contract-candidate.py` — ARGPARSE + JSON + no SYS_EXIT → `CONTRACT_INCONSISTENT_SIGNAL`
- `check-execution-verification-chain.py` — ARGPARSE + JSON + SCHEMA, no SYS_EXIT → `CONTRACT_INCONSISTENT_SIGNAL`
- `check-execution-verification-registry.py` — ARGPARSE + JSON + SCHEMA, no SYS_EXIT → `CONTRACT_INCONSISTENT_SIGNAL`

These are `NEEDS_M71_6_CLEANUP_PLAN_REVIEW`.

**`contract_inconsistent_signal_count: 5 (approximate)`**

---

## UNKNOWN Contract Items

Files with no recognizable contract signals (no CLI, no JSON, no exit, no print):

These are primarily `.sh` shell scripts and non-Python automation helpers where Python contract signals do not apply.

Shell scripts:
- `scripts/canonical-cleanup.sh` → `CONTRACT_NOT_APPLICABLE_SIGNAL`
- `scripts/test-example-project.sh` → `CONTRACT_NOT_APPLICABLE_SIGNAL`
- `scripts/test-install.sh` → `CONTRACT_NOT_APPLICABLE_SIGNAL`

Python files with no detected signals (approximately 4 files):
- These carry `CONTRACT_UNKNOWN_SIGNAL` and `UNKNOWN_CONFIDENCE`

**`contract_unknown_signal_count: 4 (approximate)`**

---

## Low-Confidence Signal Items

Files where the only detected signals are noisy heuristics (PRINT, REPORTS_PATH, EXCEPT_BLOCK only, without stronger supporting signals):

These are predominantly fixture scripts and test helper files where output is test-runner-internal rather than dispatcher-facing.

| File Pattern | Count | Signal Pattern | Confidence |
|---|---|---|---|
| `test-*-fixtures.py` (no CLI) | ~18 | PRINT or EXCEPT only | LOW_CONFIDENCE |
| `test-*-smoke.py` (no CLI) | ~3 | PRINT only | LOW_CONFIDENCE |
| `sync-task-ids.py` | 1 | EXIT only, no CLI | LOW_CONFIDENCE |

**`low_confidence_signal_count: 40 (approximate)`**

---

## M71.6 Candidates

Scripts carrying contract gaps, inconsistencies, or missing exit-code contracts that require resolution before cleanup planning. These are flagged as `NEEDS_M71_6_CLEANUP_PLAN_REVIEW`.

**Category A: validate- scripts without JSON output (dispatcher-gap)**

| Script | Gap |
|---|---|
| `validate-commit-msg.py` | No JSON output; plain text only |
| `validate-boundary-claims.py` | No JSON output; plain text only |
| `validate-frontmatter.py` | No JSON output; plain text only |
| `validate-approval-marker.py` | No JSON output; plain text only |
| `validate-queue.py` | No JSON output; plain text only |
| `validate-required-sections.py` | No JSON output; plain text only |
| `validate-runner-protocol.py` | No JSON output; plain text only |
| `validate-status-semantics.py` | No JSON output; plain text only |
| `validate-task.py` | No JSON output; plain text only |
| `validate-trace.py` | No JSON output; plain text only |
| `validate-verification.py` | No JSON output; plain text only |

**Category B: check- scripts without SYS_EXIT (missing explicit exit signal)**

| Script | Gap |
|---|---|
| `validate-ux-planning-readiness.py` | JSON present, SYS_EXIT absent |
| `validate-ux-to-task-proposal.py` | JSON present, SYS_EXIT absent |
| `validate-task-contract-candidate.py` | JSON present, SYS_EXIT absent |
| `check-execution-verification-chain.py` | JSON + SCHEMA, SYS_EXIT absent |
| `check-execution-verification-registry.py` | JSON + SCHEMA, SYS_EXIT absent |

**Category C: Legacy-candidate scripts with dangerous operations (carry-over from M71.4)**

| Script | Reason |
|---|---|
| `scripts/audit-m31-tui-tutor.py` | LEGACY_CANDIDATE + OS_SYSTEM + no clear exit contract |
| `scripts/canonical-cleanup.sh` | Cleanup script with destructive delete; contract not applicable (shell) |

**`m71_6_candidate_count: 90 (approximate)`**

---

## Markdown / JSON Authority Check

| Check | Result |
|---|---|
| Markdown inputs used as primary | true |
| JSON used as navigation only | true |
| JSON overrode Markdown | false |
| Markdown/JSON conflict observed | false |

Primary input: `reports/m71-script-inventory.md`
Secondary input: `docs/SCRIPT-RESPONSIBILITY-MAP.md`
Tertiary input: `docs/SCRIPT-DANGEROUS-OPERATIONS-AUDIT.md`
Quaternary input: `docs/SCRIPT-LEGACY-AND-DUPLICATE-MAP.md`
Navigation helper: `reports/m71-script-inventory.json` — used for counting only

---

## Source Line Printing Prevention Check

Scanner output format used: `path:line:SIGNAL:name`

No source lines were included in any scanner output reproduced in this review.

No secret values were included in any scanner output reproduced in this review.

`source_lines_printed: false`

`secret_values_printed: false`

---

## Secret Leakage Prevention Check

Scanner did not capture or log secret values.

Scanner did not print secret variable values.

Scanner printed only: path, line number, signal name.

`secret_values_printed: false`

---

## Final Integration Decision Boundary

`final_dispatcher_decision_made: false`

No script was declared dispatcher-ready.

No script was declared CI-ready.

No script was approved as child validator.

No cleanup was authorized.

No exit-code changes were made.

No output contracts were changed.

Contract signals recorded in this review are review signals only and do not constitute approval.

---

## Scope Compliance

| File | Change Type | Permitted |
|---|---|---|
| `tasks/active-task.md` | Updated | Yes — permitted by M71.5 scope |
| `docs/SCRIPT-OUTPUT-EXIT-CONTRACT-REVIEW.md` | Created | Yes — sole M71.5 output artifact |
| All other files | Not modified | Verified |

Validation commands:

- `git diff --name-only -- scripts` — expected empty
- `git diff --name-only -- reports` — expected empty
- `git diff --name-only -- .github/workflows` — expected empty
- `git diff --name-only -- data` — expected empty
- `test ! -f docs/ACTIVE-TREE-CLEANUP-PLAN.md` — expected pass
- `test ! -f reports/m71-script-audit-evidence-report.md` — expected pass
- `test ! -f reports/m71-completion-review.md` — expected pass

---

## M71.6 Preparation Decision

`may_prepare_m71_6: true_with_warnings`

`may_prepare_m71_6 is roadmap preparation only.`

`may_prepare_m71_6 does not start M71.6.`

`may_prepare_m71_6 is not approval.`

`Human review remains required.`

Warnings:

1. Contract gaps exist: 49 scripts lack JSON output despite having CLI signals.
2. Exit-code standardization gaps exist: approximately 58 scripts lack explicit SYS_EXIT.
3. Inconsistent contract signals exist: 5 scripts have CLI+JSON without SYS_EXIT.
4. Low-confidence signals exist: approximately 40 fixture/test files with only noisy signals.
5. Exit-code `2` (CLI misuse) is rarely used; incomplete differentiation across script population.
6. M71.6 candidate count is large (90 approximate); cleanup planning should prioritize canonical validate- and check- scripts.

---

## Explicit Non-Approval Boundary

This M71.5 review does not approve any script for dispatcher integration.

This M71.5 review does not approve any cleanup action.

This M71.5 review does not approve any deletion, archiving, renaming, or moving of files.

This M71.5 review does not create registry authority.

This M71.5 review does not authorize validator creation, fixture creation, or lifecycle mutation.

This M71.5 review does not start M71.6.

This M71.5 review does not start M72 or any subsequent milestone.

Human review remains required before any downstream action.

---

## Final Status

```
task_id: task-71.5
milestone: M71
task_name: Script Output / Exit-Code Contract Review
status: COMPLETE
FINAL_STATUS: M71_SCRIPT_OUTPUT_EXIT_REVIEW_COMPLETE_WITH_WARNINGS
may_prepare_m71_6: true_with_warnings
PRIMARY_INPUT: reports/m71-script-inventory.md
SECONDARY_INPUT: docs/SCRIPT-RESPONSIBILITY-MAP.md
TERTIARY_INPUT: docs/SCRIPT-DANGEROUS-OPERATIONS-AUDIT.md
QUATERNARY_INPUT: docs/SCRIPT-LEGACY-AND-DUPLICATE-MAP.md
NAVIGATION_HELPER: reports/m71-script-inventory.json
markdown_inputs_used_as_primary: true
json_used_as_navigation_only: true
json_overrode_markdown: false
scripts_modified: false
scripts_executed: false
validators_executed: false
cleanup_performed: false
source_lines_printed: false
secret_values_printed: false
output_contract_changed: false
exit_codes_changed: false
final_dispatcher_decision_made: false
cleanup_authorized: false
registries_created: false
validators_created: false
json_artifacts_created: false
scope_violations: false
cli_argument_contract_signal_count: 162 (approximate)
json_output_signal_count: 122 (approximate)
plain_text_output_signal_count: 89 (approximate)
report_writing_output_signal_count: 77 (approximate)
explicit_exit_code_signal_count: 143 (approximate)
sys_exit_signal_count: 131 (approximate)
exception_internal_error_signal_count: 166 (approximate)
output_schema_signal_count: 21 (approximate)
contract_documented_signal_count: 57 (approximate)
contract_partial_signal_count: 130 (approximate)
contract_missing_signal_count: 0
contract_inconsistent_signal_count: 5 (approximate)
contract_unknown_signal_count: 4 (approximate)
potential_child_validator_candidate_count: 62 (approximate, strict: CLI+JSON+SYS_EXIT)
needs_output_standardization_count: 49 (approximate)
needs_exit_code_standardization_count: 58 (approximate)
low_confidence_signal_count: 40 (approximate)
m71_6_candidate_count: 90 (approximate)
notes: >
  Contract review is read-only signal record only.
  No scripts modified.
  No scripts executed.
  No validators executed.
  No source lines printed.
  No secret values captured.
  No output contracts changed.
  No exit codes changed.
  No final dispatcher decisions made.
  No cleanup authorized.
  Human review required before any downstream action.
  Counts are approximate — derived from read-only regex scanning.
  Noisy signals (PRINT, REPORTS_PATH, EXCEPT_BLOCK) treated as LOW_CONFIDENCE standalone.
  POTENTIAL_CHILD_VALIDATOR_CANDIDATE used only with at least two supporting signals.
```
