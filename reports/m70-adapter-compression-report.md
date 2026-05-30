# M70.6 — Adapter Files Compression Report

<h2>Task Boundary</h2>

This adapter compression report is evidence only.
This adapter compression report is not approval.
This adapter compression report does not authorize documentation reference cleanup.
This adapter compression report does not authorize bootstrap changes.
This adapter compression report does not authorize script changes.
This adapter compression report does not create machine-readable registry authority.
This adapter compression report does not authorize validator creation, fixture creation, or lifecycle mutation.
Human review remains required.

## Active Task Record

- id: task-70.6
- milestone: M70
- name: "Adapter Files Compression"
- status: active
- mode: "EXECUTION / DOCUMENTATION EDIT / ADAPTER COMPRESSION"
- branch: dev
- started_at: "2026-05-28"

## Inputs Reviewed

- `reports/m70-bootstrap-compression-report.md`
- `docs/ADAPTER-DRIFT-RESOLUTION-PLAN.md`
- `docs/SOURCE-OF-TRUTH-RULES.md`
- `docs/CANONICAL-DOCS-REGISTRY.md`
- `docs/DEPRECATED-DOCS-REGISTRY.md`
- `docs/DOCUMENTATION-COMPRESSION-PLAN.md`
- `reports/m69-validation-authority-drift-review.md`

## M70.5 Bootstrap Compression Status

M70.5 is completed with status `FINAL_STATUS: M70_BOOTSTRAP_COMPRESSION_COMPLETE_WITH_WARNINGS` and `may_prepare_m70_6: true_with_warnings`. The bootstrap surface is compressed and rules are preserved.

## Adapter Files Present

- `AGENTS.md` (present)
- `CLAUDE.md` (present)
- `GEMINI.md` (present)
- `.github/copilot-instructions.md` (present)
- `.github/instructions/backend.instructions.md` (present)
- `.github/instructions/frontend.instructions.md` (present)

## Adapter Files Missing

No adapter files are missing.

## .github/instructions Pre-Audit

Direct child regular files reviewed under `.github/instructions/`:
- `.github/instructions/backend.instructions.md` (file type: markdown instructions, not modified, reason: it is already targeted developer guide with no duplicate rules, human review required: yes)
- `.github/instructions/frontend.instructions.md` (file type: markdown instructions, not modified, reason: it is already targeted developer guide with no duplicate rules, human review required: yes)

## Adapter Files Modified

- `AGENTS.md`
- `CLAUDE.md`
- `GEMINI.md`
- `.github/copilot-instructions.md`

## Adapter Files Unchanged With Justification

- `.github/instructions/backend.instructions.md`: Unchanged because it is a highly targeted, 11-line developer guide for backend coding tasks that does not duplicate generic governance rules.
- `.github/instructions/frontend.instructions.md`: Unchanged because it is a highly targeted, 11-line developer guide for frontend coding tasks that does not duplicate generic governance rules.

## Before / After Line Counts

- `AGENTS.md`: Before: 13 | After: 24 (increased due to adding safety semantics block)
- `CLAUDE.md`: Before: 13 | After: 24 (increased due to adding safety semantics block)
- `GEMINI.md`: Before: 22 | After: 31 (increased due to adding safety semantics block)
- `.github/copilot-instructions.md`: Before: 13 | After: 24 (increased due to adding safety semantics block)
- `.github/instructions/backend.instructions.md`: Before: 11 | After: 11 (unchanged)
- `.github/instructions/frontend.instructions.md`: Before: 11 | After: 11 (unchanged)

## Before / After Byte Counts

- `AGENTS.md`: Before: 624 | After: 1080
- `CLAUDE.md`: Before: 624 | After: 1080
- `GEMINI.md`: Before: 1668 | After: 1638 (decreased due to rule referencing)
- `.github/copilot-instructions.md`: Before: 603 | After: 1080
- `.github/instructions/backend.instructions.md`: Before: 484 | After: 484 (unchanged)
- `.github/instructions/frontend.instructions.md`: Before: 429 | After: 429 (unchanged)

## Boilerplate Reduced

- Replaced duplicated descriptions of priority, authority, and agent boundaries across `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, and `.github/copilot-instructions.md` with direct references to `core-rules/MAIN.md` and `quality/MAIN.md`.

## Canonical References Added Or Preserved

- Added links to `core-rules/MAIN.md`, `quality/MAIN.md`, and `ROUTES-REGISTRY.md` inside modified adapter files.

## Adapter-Specific Delta Preservation

- The Gemini-specific mandates (Single-Role execution, readiness asserts, YAML safety, idle bypass) in `GEMINI.md` were preserved untouched.
- General agent constraints for Copilot, Claude, and general agents were preserved.

## AGENTS.md Shared-Adapter Caution

- `AGENTS.md` was compressed in a way that preserves cross-agent readability.
- No agent-specific or parser-specific optimizations were added to ensure multiple agents can parse the file correctly.

## Safety Semantics Preservation

All safety semantics were fully preserved inside all modified adapter files. We confirm that these meanings were preserved:
- **PASS is not approval** (preserved)
- **Evidence is not approval** (preserved)
- **CI PASS is not approval** (preserved)
- **UNKNOWN is not OK** (preserved)
- **NOT_RUN is not PASS** (preserved)
- **Human approval cannot be simulated** (preserved)
- **Human review remains required** (preserved)
- **No lifecycle mutation without explicit governed task** (preserved)

## Validation Authority Caution Preservation

- Wording in all adapter files preserves the warning that validation authority dispatcher cleanup belongs to M73.
- Validator or script authority was not claimed as final.
- Final validation dispatcher cleanup belongs to M73.

## Source-of-Truth Routing Preservation

- All adapter instructions successfully route the user and agent to `llms.txt` and canonical modules (`core-rules/MAIN.md`, etc.).

## Bootstrap Files Boundary Check

- Bootstrap files (`llms.txt`, `START.md`, `SYSTEM_PROMPT.md`, `ROUTES-REGISTRY.md`) were not modified in this task.

## Scripts Boundary Check

- No scripts under `scripts/` or elsewhere were modified.

## Machine-Readable Registry Boundary Check

- No JSON registries under `data/` were created.

## M71+ Artifact Boundary Check

- No M71+ artifacts were created.

## Scope Compliance

- Changes were strictly limited to `tasks/active-task.md`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`, and `reports/m70-adapter-compression-report.md`. No other files were touched.

## M70.7 Preparation Decision

may_prepare_m70_7: true_with_warnings

may_prepare_m70_7 is roadmap preparation only.
may_prepare_m70_7 does not start M70.7.
may_prepare_m70_7 is not approval.

## Explicit Non-Approval Boundary

This adapter compression report is evidence only.
This adapter compression report is not approval.
This adapter compression report does not authorize documentation reference cleanup.
This adapter compression report does not authorize bootstrap changes.
This adapter compression report does not authorize script changes.
This adapter compression report does not create machine-readable registry authority.
This adapter compression report does not authorize validator creation, fixture creation, or lifecycle mutation.
Human review remains required.

## Final Status

FINAL_STATUS: M70_ADAPTER_COMPRESSION_COMPLETE_WITH_WARNINGS
