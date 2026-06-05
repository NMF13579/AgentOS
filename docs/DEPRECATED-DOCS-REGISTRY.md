# Deprecated Docs Registry

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

This registry records possible deprecated candidates only.
This registry does not delete documents.
This registry does not finally deprecate documents.
This registry does not authorize cleanup.

## Deprecation Candidate Labels

Allowed labels for deprecation mapping:
- `POSSIBLE_DEPRECATED`: Candidates flagged for potential removal or archiving
- `POSSIBLE_DUPLICATE`: Repeated files with overlapping purpose
- `HISTORICAL_ARTIFACT`: Prior milestone reports or context captures
- `STALE_ADVISORY`: Documentation containing superseded guidance
- `SUPERSEDED_LOOKING`: Files whose responsibilities have been absorbed by canonical files
- `NEEDS_REVIEW`: High risk cases requiring manual validation
- `NOT_SAFE_TO_DEPRECATE`: Critical files required for active system operation and safety

## Possible Deprecated Candidates

We identify the following possible deprecated candidates:

1. Candidate 1
   - path: `HANDOFF 2.md`
   - reason signal: Pre-existing backup copy of `HANDOFF.md` with identical content and duplicate task states.
   - source evidence: `reports/m68-duplicates.json` same-stem signal.
   - risk if changed: Low.
   - required human review: Yes, requires manual confirmation that no unique context is lost.
   - deprecation path needed: Mark as `POSSIBLE_DEPRECATED` and proposal for safe removal in a separate task.

2. Candidate 2
   - path: `docs/task-20260426-brief-readiness-check/`
   - reason signal: Milestone-specific guide folder that is no longer active or referenced.
   - source evidence: `docs/SOURCE-OF-TRUTH-MAP.md` historical list.
   - risk if changed: Low.
   - required human review: Yes, review to ensure no historical context remains unarchived.
   - deprecation path needed: Archive folder path.

3. Candidate 3
   - path: `docs/task-20260426-brief-to-contract-manual-guide/`
   - reason signal: Manual guideline folder superseded by unified runner and current placement workflow.
   - source evidence: `docs/SOURCE-OF-TRUTH-MAP.md` historical list.
   - risk if changed: Low.
   - required human review: Yes.
   - deprecation path needed: Archive folder path.

## Possible Duplicate Candidates

- `HANDOFF 2.md` (duplication candidate of `HANDOFF.md`) — `POSSIBLE_DUPLICATE`
- Duplicate bootstrap descriptions across `.github/instructions/*` — `POSSIBLE_DUPLICATE`

## Historical Artifact Candidates

- Prior milestone evidence reports under `reports/` (e.g. `reports/milestone-22-*`, `reports/m33-*`) — `HISTORICAL_ARTIFACT`
- Legacy context logs — `HISTORICAL_ARTIFACT`

## Superseded-Looking Candidates

- Old task instruction drafts or guides that have been consolidated under canonical `workflow/MAIN.md` — `SUPERSEDED_LOOKING`

## Stale / Advisory Document Candidates

- Non-authoritative guides under `docs/` that contain references to legacy shell script execution paths — `STALE_ADVISORY`

## Documents Not Safe To Deprecate

The following files are strictly NOT safe to deprecate:
- `core-rules/MAIN.md` (contains core safety rules, defines source-of-truth semantics)
- `state/MAIN.md` (defines state machine and state lifecycle/transitions)
- `workflow/MAIN.md` (defines execution and approval boundaries)
- `quality/MAIN.md` (defines validation/smoke check and completion gate readiness rules)
- `security/MAIN.md` (defines sensitive data handling, access policy, and compliance)
- `llms.txt` (primary startup nav route referenced by bootstrap rules)
- `ROUTES-REGISTRY.md` (referenced by bootstrap workflows)
- `docs/COMPLETION-GATE-HARDENING-CONTRACT.md` (connected to protected artifacts)
- `scripts/VALIDATORS.md` (unresolved validation authority role; must remain cautious until M73)

## Human Review Requirements

- Moving any document to archived status requires human review.
- De-registering any canonical candidate requires human review.

## Deprecation Path Requirements

- No document may be deleted in M70.2.
- No document may be removed without deprecation path.
- No document may be deprecated finally without human review.
- No source-of-truth document may be replaced without explicit approval.

## Explicit Non-Deletion Boundary

This registry is a Markdown planning artifact only.
This registry does not create machine-readable registry authority.
This registry does not override source-of-truth documents.
This registry does not approve cleanup, deletion, compression, consolidation, registry creation, validator creation, fixture creation, or lifecycle mutation.
This registry does not modify bootstrap files.
This registry does not modify adapter files.
This registry does not modify scripts.
Human review remains required.

## M70.3 Preparation Decision

may_prepare_m70_3: true_with_warnings

may_prepare_m70_3 is roadmap preparation only.
may_prepare_m70_3 does not start M70.3.
may_prepare_m70_3 is not approval.

## Final Status

FINAL_STATUS: M70_DEPRECATED_DOCS_REGISTRY_COMPLETE_WITH_WARNINGS
