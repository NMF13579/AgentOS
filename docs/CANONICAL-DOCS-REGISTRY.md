# Canonical Docs Registry

## Task Boundary

This registry is a Markdown planning artifact only.
This registry does not create machine-readable registry authority.
This registry does not override source-of-truth documents.
This registry does not approve cleanup, deletion, compression, consolidation, registry creation, validator creation, fixture creation, or lifecycle mutation.
This registry does not modify bootstrap files.
This registry does not modify adapter files.
This registry does not modify scripts.
Human review remains required.

## Active Task Record

- id: task-70.2
- milestone: M70
- name: "Canonical Docs and Deprecated Docs Registry"
- status: active
- mode: "EXECUTION / DOCUMENTATION REGISTRY / MARKDOWN ONLY"
- branch: dev
- started_at: "2026-05-28"

## Inputs Reviewed

- `reports/m70-m69-completion-intake.md`
- `docs/DOCUMENTATION-COMPRESSION-PLAN.md`
- `reports/m69-completion-review.md`
- `reports/m69-script-audit-report.md`
- `reports/m69-validation-authority-drift-review.md`
- `docs/SOURCE-OF-TRUTH-MAP.md`
- `docs/DUPLICATION-MAP.md`
- `docs/REPO-ANOMALY-MAP.md`
- `llms.txt` (bootstrap, read-only)
- `START.md` (bootstrap, read-only)
- `SYSTEM_PROMPT.md` (bootstrap, read-only)
- `ROUTES-REGISTRY.md` (bootstrap, read-only)
- `AGENTS.md` (adapter, read-only)
- `CLAUDE.md` (adapter, read-only)
- `GEMINI.md` (adapter, read-only)
- `.github/copilot-instructions.md` (adapter, read-only)

## Registry Model

This registry is Markdown-only.
This registry is a planning and documentation organization artifact.
This registry is not a machine-readable authority layer.
Machine-readable registries belong to M72.

## Classification Labels

- `CANONICAL_CANDIDATE`: Candidate for primary source-of-truth or governance rules
- `SUPPORTING_DOC`: Document that guides implementation but remains subservient to canonical docs
- `DERIVED_DOC`: Document containing generated summaries or maps
- `REPORT_ARTIFACT`: Execution milestone summaries and historical review reports
- `TEMPLATE_ARTIFACT`: Structural blueprints or layout formats
- `SCHEMA_ARTIFACT`: Data validation shapes
- `CHECKER_DOC`: Manual execution checklists and scripts descriptions
- `HISTORICAL_ARTIFACT`: Legacy context logs
- `PROTECTED_REFERENCE`: Mandatory files that must not be changed casually
- `OUT_OF_SCOPE_FOR_M70`: Files outside M70 boundary
- `NEEDS_REVIEW`: High ambiguity files requiring direct human attention

## Canonical Candidates

The following files are classified as canonical candidates:
- `llms.txt` — `CANONICAL_CANDIDATE` (startup nav route)
- `core-rules/MAIN.md` — `CANONICAL_CANDIDATE` (governance authority)
- `state/MAIN.md` — `CANONICAL_CANDIDATE` (state machine authority)
- `workflow/MAIN.md` — `CANONICAL_CANDIDATE` (execution backbone)
- `quality/MAIN.md` — `CANONICAL_CANDIDATE` (verification and smoke test authority)
- `security/MAIN.md` — `CANONICAL_CANDIDATE` (data security boundaries)
- `tasks/active-task.md` — `CANONICAL_CANDIDATE` (current task binding record)

## Supporting Documents

The following files are classified as supporting documents:
- `docs/GETTING-STARTED.md` — `SUPPORTING_DOC`
- `docs/VALIDATION.md` — `SUPPORTING_DOC`
- `docs/SAFETY-BOUNDARIES.md` — `SUPPORTING_DOC`
- `FAQ.md` — `SUPPORTING_DOC`
- `README.md` — `SUPPORTING_DOC`

## Derived Documents

The following files are classified as derived documents:
- `docs/SOURCE-OF-TRUTH-MAP.md` — `DERIVED_DOC`
- `docs/DUPLICATION-MAP.md` — `DERIVED_DOC`
- `docs/REPO-ANOMALY-MAP.md` — `DERIVED_DOC`

## Report Artifacts

The following reports are classified as report artifacts:
- `reports/m70-m69-completion-intake.md` — `REPORT_ARTIFACT`
- `docs/DOCUMENTATION-COMPRESSION-PLAN.md` — `REPORT_ARTIFACT` (records planning design)
- Reports are evidence artifacts, not approval and not source-of-truth authority.

## Template Artifacts

The following files are classified as template artifacts:
- `templates/` — `TEMPLATE_ARTIFACT` (format structures)
- `handoff/templates/` — `TEMPLATE_ARTIFACT`

## Schema Artifacts

The following files are classified as schema artifacts:
- `schemas/handoff.schema.json` — `SCHEMA_ARTIFACT`

## Checker Documentation

The following files are classified as checker documentation:
- `scripts/VALIDATORS.md` — `CHECKER_DOC`
- `docs/SCRIPT-OUTPUT-CONTRACT.md` — `CHECKER_DOC`
- `docs/SCRIPT-EXIT-CODE-STANDARD.md` — `CHECKER_DOC`

## Historical Artifacts

The following files are classified as historical artifacts:
- `reports/m67-completion-review.md` — `HISTORICAL_ARTIFACT`
- `reports/m68-inventory-review.md` — `HISTORICAL_ARTIFACT`
- `reports/m69-script-audit-report.md` — `HISTORICAL_ARTIFACT`

## Protected References

The following files are classified as protected references:
- `docs/COMPLETION-GATE-HARDENING-CONTRACT.md` — `PROTECTED_REFERENCE`
- `reports/m63-completion-review.md` — `PROTECTED_REFERENCE`
- `reports/m64-completion-review.md` — `PROTECTED_REFERENCE`
- `reports/m65-completion-review.md` — `PROTECTED_REFERENCE`
- `reports/m66-completion-review.md` — `PROTECTED_REFERENCE`
- `reports/m67-completion-review.md` — `PROTECTED_REFERENCE`

## Out Of Scope For M70

The following items are out of scope for M70:
- `scripts/` (except read-only) — `OUT_OF_SCOPE_FOR_M70`
- `tests/` — `OUT_OF_SCOPE_FOR_M70`
- `.github/workflows/` — `OUT_OF_SCOPE_FOR_M70`
- `data/` — `OUT_OF_SCOPE_FOR_M70`

## Validation Authority Caution

Documents that mention validation entrypoints must preserve M69 validation authority drift caution.
M70.2 does not decide final validation authority.
Do not mark validator docs or script docs as final authority if M69 left authority drift unresolved.

## Human Review Requirements

- Changing status of any canonical candidate requires human review.
- Adding new classification labels requires human review.

## Explicit Non-Authority Boundary

This registry is a Markdown planning artifact only.
This registry does not create machine-readable registry authority.
This registry does not override source-of-truth documents.
This registry does not approve cleanup, deletion, compression, consolidation, registry creation, validator creation, fixture creation, or lifecycle mutation.
This registry does not modify bootstrap files.
This registry does not modify adapter files.
This registry does not modify scripts.
Human review remains required.

## Final Status

FINAL_STATUS: M70_CANONICAL_DOCS_REGISTRY_COMPLETE_WITH_WARNINGS
