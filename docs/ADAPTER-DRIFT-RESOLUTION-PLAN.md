# Adapter Drift Resolution Plan

## Task Boundary

This adapter drift resolution plan is a planning artifact only.
This adapter drift resolution plan does not modify bootstrap files.
This adapter drift resolution plan does not modify adapter files.
This adapter drift resolution plan does not modify scripts.
This adapter drift resolution plan does not decide final validation authority.
This adapter drift resolution plan does not create machine-readable registry authority.
This adapter drift resolution plan does not approve cleanup, deletion, compression, consolidation, registry creation, validator creation, fixture creation, or lifecycle mutation.
Human review remains required.

## Active Task Record

- id: task-70.4
- milestone: M70
- name: "Adapter Drift Resolution Plan"
- status: active
- mode: "EXECUTION / PLANNING / ADAPTER DRIFT RESOLUTION"
- branch: dev
- started_at: "2026-05-28"

## Inputs Reviewed

- `reports/m70-m69-completion-intake.md`
- `docs/DOCUMENTATION-COMPRESSION-PLAN.md`
- `docs/CANONICAL-DOCS-REGISTRY.md`
- `docs/DEPRECATED-DOCS-REGISTRY.md`
- `docs/SOURCE-OF-TRUTH-RULES.md`
- `reports/m69-validation-authority-drift-review.md`
- `reports/m69-script-audit-report.md`
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
- `.github/instructions/` (read-only if present)

## M70.3 Source-of-Truth Rules Status

The M70.3 rules document `docs/SOURCE-OF-TRUTH-RULES.md` is complete with warnings (`FINAL_STATUS: M70_SOURCE_OF_TRUTH_RULES_COMPLETE_WITH_WARNINGS`). The constraints on document relationships and validation entrypoints are carried forward.

## Adapter / Bootstrap Surface Model

Canonical governance belongs in source-of-truth documents.
Bootstrap files route to source-of-truth documents.
Adapter files contain only adapter-specific delta.
No adapter file may create governance authority above canonical docs.

Additional constraints:
- Adapter files may contain adapter-specific delta only.
- Adapter files must not override canonical governance rules.
- Adapter files must not expand permissions.
- Adapter files must not create approval, completion, or lifecycle semantics.
- Final validation dispatcher cleanup belongs to M73.

## Files Reviewed

We have reviewed the following bootstrap and adapter files (read-only):
- `llms.txt` (present)
- `START.md` (present)
- `SYSTEM_PROMPT.md` (present)
- `ROUTES-REGISTRY.md` (present)
- `AGENTS.md` (present)
- `CLAUDE.md` (present)
- `GEMINI.md` (present)
- `.github/copilot-instructions.md` (present)
- `.github/instructions/` (none observed in this repository, recorded as missing/empty folder)

## Common Canonical Instruction Candidates

We identify the following repeated instructions that should later move to or reference canonical source-of-truth docs:
- PASS/evidence/approval separation rules (e.g. repeated in `AGENTS.md` and `GEMINI.md`).
- Human review requirements for execution and completion reviews.
- Fail-closed semantics for validator execution.
- Scope boundaries restricting file modifications.
- Protected artifact boundaries preventing modifications to M61-M67 assets.
- Source-of-truth rules that declare markdown/yaml authority.
- Validation authority cautions highlighting the legacy status of `run-all.sh`.

## Adapter-Specific Delta Candidates

We identify the following adapter-specific deltas (cautious candidates):
- `AGENTS.md`: Adapter-specific roles such as entry point boot sequences and canonical role execution declarations (adapter-specific delta candidate, requires human review, not yet implemented).
- `GEMINI.md`: Gemini-specific parameters, such as Gemini 3.5 Flash modeling instructions, Single-Role execution flags, and YAML frontmatter empty brackets limitations (adapter-specific delta candidate, requires human review, not yet implemented).
- `CLAUDE.md`: Claude-specific system prompts and instructions (adapter-specific delta candidate, requires human review, not yet implemented).
- `.github/copilot-instructions.md`: GitHub Copilot specific developer prompts (adapter-specific delta candidate, requires human review, not yet implemented).

## Repeated Instruction Blocks

The following repeated instruction blocks exist across multiple files:
- Russian-first issue reporting guidelines (repeated in `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`).
- Bootstrap routing sequence steps (repeated in `llms.txt`, `AGENTS.md`, `CLAUDE.md`).
- Validation rules and audit command syntax references.

These blocks must not be deleted or replaced in M70.4.

## Hidden Governance Mandate Risks

We identify the following hidden governance risks where adapter/bootstrap instructions appear to introduce behaviors not grounded in canonical docs:
- Gemini YAML bracket rules in `GEMINI.md` (hidden mandate risk, requires source-of-truth review).
- Startup routing overrides in `AGENTS.md` (hidden mandate risk, requires source-of-truth review).

## Permission Expansion Risks

We identify the following instruction risks:
- Instructions in `GEMINI.md` or `AGENTS.md` that might expand file system modification permissions or suggest command execution outside tasks/active-task.md boundaries.
- No instructions should expand write, cleanup, or command permissions.

## Approval / Completion / Lifecycle Semantics Risks

- Adapter files must not create approval semantics.
- Adapter files must not create completion semantics.
- Adapter files must not create lifecycle mutation semantics.
- Adapter files must not simulate human review.
Every transition must remain explicitly governed by canonical Markdown/YAML rules and human checkpoint validations.

## Validation Authority Wording Risks

- Validation authority wording must remain cautious until M73.
- M70.4 does not decide final validation authority.
- M70.4 does not approve any validation entrypoint as canonical.
Any wording that implies `run-all.sh` or `agentos-validate.py` has final authority is a risk and must be phrased cautiously.

## Bootstrap Surface Reduction Candidates

We identify the following bootstrap surface reduction candidates (to be compressed later):
- Duplicated boot lists in `llms.txt` and `START.md` that can be replaced with direct links to `ROUTES-REGISTRY.md`.
- Repeated governance descriptions in `llms.txt` that can refer to `core-rules/MAIN.md`.

## Adapter File Compression Candidates

We identify the following adapter file compression candidates:
- `AGENTS.md` (remove duplicate Russian-first/startup rules, replace with links).
- `GEMINI.md` (condense rule lists, reference core rules).
- `CLAUDE.md` (re-align with a compact delta-only file).

## Files Not Safe To Modify Without Human Review

The following files must not be modified without explicit human review:
- `llms.txt`
- `START.md`
- `SYSTEM_PROMPT.md`
- `ROUTES-REGISTRY.md`
- `AGENTS.md`
- `CLAUDE.md`
- `GEMINI.md`
- `.github/copilot-instructions.md`
- `.github/instructions/*`
- All canonical rules files (`core-rules/MAIN.md`, `state/MAIN.md`, `workflow/MAIN.md`, `quality/MAIN.md`, `security/MAIN.md`).

## Proposed Future Adapter Structure

Target Model:
1. Canonical governance lives in source-of-truth docs (under `core-rules/`, `state/`, `workflow/`, `quality/`, `security/`).
2. Bootstrap files point to canonical docs and minimal route instructions.
3. Adapter files contain only adapter-specific delta.
4. Adapter-specific delta must be traceable to canonical governance.
5. Any new governance rule must first exist in canonical docs, not only in adapter files.

## Proposed M70.5 / M70.6 Execution Order

The proposed sequence for execution:
- 70.5 — Bootstrap Surface Compression
- 70.6 — Adapter Files Compression

This execution order is planning only.
Each task requires a separate task brief.
M70.4 does not start M70.5 or M70.6.

## Human Review Checkpoints

Human review is required before:
- modifying `llms.txt`
- modifying `START.md`
- modifying `SYSTEM_PROMPT.md`
- modifying `ROUTES-REGISTRY.md`
- modifying `AGENTS.md`
- modifying `CLAUDE.md`
- modifying `GEMINI.md`
- modifying `.github/copilot-instructions.md`
- modifying `.github/instructions/*`
- removing repeated boundary statements
- replacing safety text with references
- changing validation authority wording
- changing adapter-specific permissions
- adding or removing governance mandates

## Explicit Non-Implementation Boundary

This adapter drift resolution plan is a planning artifact only.
This adapter drift resolution plan does not modify bootstrap files.
This adapter drift resolution plan does not modify adapter files.
This adapter drift resolution plan does not modify scripts.
This adapter drift resolution plan does not decide final validation authority.
This adapter drift resolution plan does not create machine-readable registry authority.
This adapter drift resolution plan does not approve cleanup, deletion, compression, consolidation, registry creation, validator creation, fixture creation, or lifecycle mutation.
Human review remains required.

## M70.5 Preparation Decision

may_prepare_m70_5: true_with_warnings

may_prepare_m70_5 is roadmap preparation only.
may_prepare_m70_5 does not start M70.5.
may_prepare_m70_5 is not approval.

## Final Status

FINAL_STATUS: M70_ADAPTER_DRIFT_RESOLUTION_PLAN_COMPLETE_WITH_WARNINGS
