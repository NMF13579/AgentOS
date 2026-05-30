# Script Output Contract
## Task Boundary
This script output contract documents observed and proposed output behavior only.
This script output contract does not modify scripts.
This script output contract does not create validators.
This script output contract does not decide final validation authority.
This script output contract does not approve M69.
Human review remains required.

## Active Task Record
- active_task_id: task-69.4
- milestone: M69
- mode: EXECUTION / READ-ONLY SCRIPT CONTRACT AUDIT

## Inputs Reviewed
- reports/m69-m68-completion-intake.md
- reports/m69-script-inventory-intake.md
- docs/SCRIPT-RESPONSIBILITY-MAP.md
- docs/SCRIPT-LIFECYCLE-POLICY.md
- reports/m68-docs-to-code-drift.json
- reports/m68-anomaly-grep.txt
- scripts/
- scripts/VALIDATORS.md
- .github/workflows/

## M69.3 Lifecycle Classification Status
- M69.3 status: `FINAL_STATUS: M69_SCRIPT_LIFECYCLE_CLASSIFICATION_COMPLETE_WITH_WARNINGS`
- M69.3 preparation value: `may_prepare_m69_4: true_with_warnings`

## Observed Output Patterns
- Many scripts print human-readable text to stdout.
- Some scripts print JSON in `--json` mode or as a machine-readable variant.
- Some scripts print both a human summary and structured lines such as `RESULT:`, `PASS`, `FAIL`, or `warnings:` labels.
- Some workflow steps capture script output into artifacts like `reports/ci/agentos-validate.json`.

## JSON Output Signals
- observed JSON-emitting scripts include `scripts/agentos-enforce.py`, `scripts/agentos-retry-enforce.py`, `scripts/agentos-explain.py`, `scripts/check-context-pipeline.py`, `scripts/check-required-context-compliance.py`, `scripts/check-scope-compliance.py`, `scripts/check-private-evaluator-consistency.py`, `scripts/check-process-trace.py`, `scripts/check-evidence-immutability.py`, `scripts/validate-ux-to-task-proposal.py`, `scripts/check-execution-result-verification.py`, `scripts/check-task-acceptance-mvp.py`
- `scripts/agentos-validate.py` is referenced by CI for both human-readable and JSON reporting
- `scripts/validate-ux-to-task-proposal.py` explicitly guards that `--json` writes valid JSON to stdout

## Text Output Signals
- observed text-only or primarily text-emitting scripts include `scripts/VALIDATORS.md`, `scripts/validate-gate-contract.py`, `scripts/health-check.sh`, `scripts/check-llms-graph-files.sh`, `scripts/validate-architecture.sh`, `scripts/agentos.py`, `scripts/audit-execution-control.py`, `scripts/audit-mvp-readiness.py`, `scripts/check-template-cleanliness.py`, `scripts/check-template-integrity.py`
- many scripts mix text summaries with optional JSON output, so text-only vs JSON-only should be treated carefully

## Stdout / Stderr Signals
- several scripts route diagnostics to stderr and structured payloads to stdout
- `scripts/validate-ux-to-task-proposal.py` explicitly says JSON mode must keep non-JSON diagnostics off stdout
- `scripts/check-context-pipeline.py` and `scripts/check-required-context-compliance.py` parse subprocess stdout and can treat stderr as failure evidence
- mixed stdout/stderr handling is part of the observed contract surface and needs later review

## Machine-Readable Output Requirements
- future preferred shape should include a stable machine-readable object with fields like:
  - `tool`
  - `version`
  - `result`
  - `status`
  - `warnings`
  - `errors`
  - `inputs`
  - `outputs`
  - `evidence`
  - `manual_review_required`
  - `non_approval_boundary`
- machine-readable output should be explicit about evidence and must not imply approval

## Human-Readable Output Requirements
- human-readable output should keep a clear result line and a short explanation
- human-readable output should separate warnings from errors
- human-readable output should not hide whether manual review is still required

## Proposed Future Output Contract
- preferred future contract:
  - one consistent structured result object for JSON mode
  - one consistent human summary format for text mode
  - explicit `manual_review_required` marker when the result is not an approval
  - explicit `non_approval_boundary` text in both human and JSON forms
- recommended future JSON fields:
  - `tool`
  - `version`
  - `result`
  - `status`
  - `warnings`
  - `errors`
  - `inputs`
  - `outputs`
  - `evidence`
  - `manual_review_required`
  - `non_approval_boundary`
- Script output may provide evidence.
- Script output must not create approval.
- Script output must not create lifecycle mutation.

## Non-Approval Output Boundary
- PASS is not approval.
- Evidence is not approval.
- JSON output is not approval by itself.
- CI output is not approval unless a human separately says so.

## Scripts Requiring Later Output Contract Review
- `scripts/agentos-enforce.py`
- `scripts/agentos-retry-enforce.py`
- `scripts/agentos-explain.py`
- `scripts/check-context-pipeline.py`
- `scripts/check-required-context-compliance.py`
- `scripts/check-scope-compliance.py`
- `scripts/validate-ux-to-task-proposal.py`
- `scripts/check-execution-result-verification.py`
- `scripts/check-task-acceptance-mvp.py`
- `scripts/agentos.py`
- `scripts/audit-execution-control.py`
- `scripts/audit-mvp-readiness.py`
- scripts that mix human summary and machine-readable output need later review

## Explicit Non-Implementation Boundary
- This script output contract does not modify scripts.
- This script output contract does not create validators.
- This script output contract does not decide final validation authority.
- This script output contract does not approve M69.
- Human review remains required.

## Final Status
FINAL_STATUS: M69_SCRIPT_OUTPUT_CONTRACT_COMPLETE_WITH_WARNINGS
