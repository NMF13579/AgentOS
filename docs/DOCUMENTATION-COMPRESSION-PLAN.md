# Documentation Compression Plan

## Task Boundary

This plan is a planning artifact only.
This plan does not compress documentation.
This plan does not modify bootstrap files.
This plan does not modify adapter files.
This plan does not modify scripts.
This plan does not approve cleanup, deletion, compression, consolidation, registry creation, validator creation, fixture creation, or lifecycle mutation.
This plan does not start M70.2.
Human review remains required.

## Active Task Record

- id: task-70.1
- milestone: M70
- name: "Documentation Compression Plan"
- status: active
- mode: "EXECUTION / PLANNING / DOCUMENTATION COMPRESSION DESIGN"
- branch: dev
- started_at: "2026-05-28"

## Inputs Reviewed

- `reports/m70-m69-completion-intake.md`
- `reports/m69-completion-review.md`
- `reports/m69-script-audit-report.md`
- `reports/m69-validation-authority-drift-review.md`
- `docs/SCRIPT-RESPONSIBILITY-MAP.md`
- `docs/SCRIPT-LIFECYCLE-POLICY.md`
- `docs/SCRIPT-OUTPUT-CONTRACT.md`
- `docs/SCRIPT-EXIT-CODE-STANDARD.md`
- `docs/ACTIVE-TREE-CLEANUP-PLAN.md`
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

## M70.0 Intake Status

The M70.0 intake completed with a status of `FINAL_STATUS: M70_INTAKE_READY_WITH_WARNINGS`. The warnings from the M69 script audit are carried forward and serve as constraints for this plan.

## M69 Script Audit Constraints

The plan carries forward M69 script audit constraints:
- M70 documentation must not present unresolved validation authority as resolved.
- M70 documentation must not call a validator canonical unless M69 evidence and later M73 authority model support it.
- M70 must preserve cautious wording around validation entrypoints.
- Final validation dispatcher cleanup belongs to M73.
- All M69 script lifecycle, output contract, and active-tree warnings remain active.

## Compression Principles

- Compress repeated text by replacing it with references to canonical source-of-truth documents where safe.
- Do not remove safety boundaries.
- Do not compress away PASS/evidence/approval separation.
- Do not compress away human review requirements.
- Do not turn reports into approval.
- Do not turn registries into authority above source-of-truth docs.
- Do not present unresolved validation authority as resolved.

## Source-of-Truth Preservation Rules

- Markdown/YAML remain the source of truth.
- Reports remain evidence, not approval.
- JSON/indexes remain derived/navigation artifacts.
- Adapter files cannot create new governance mandates.
- Source-of-truth changes require human review.
- Validation authority claims must remain cautious until M73.

## Bootstrap Surface Candidates

We review the following bootstrap surface files for potential compression candidates:

1. `llms.txt`
   - *Observed issue*: Contains duplicate description of bootstrap order and core principle sections that are also found in `core-rules/MAIN.md` and `state/MAIN.md`.
   - *Possible compression approach*: A bootstrap compression candidate. Condense references by replacing repeated descriptions with links to the canonical `core-rules/MAIN.md` and `state/MAIN.md`.
   - *Safety risk*: Low-medium. Breaking startup links can disrupt LLM parsing and initialization.
   - *Human review requirement*: Modifying this file requires human review before edits.

2. `START.md`
   - *Observed issue*: Repeats general agent instructions and bootstrap guidelines that are already owned by `core-rules/MAIN.md`.
   - *Possible compression approach*: A bootstrap compression candidate. Point directly to canonical core-rules files and replace duplicate passages with references.
   - *Safety risk*: Low-medium.
   - *Human review requirement*: Requires human review before edits.

3. `SYSTEM_PROMPT.md`
   - *Observed issue*: Short bootstrap prompt pointing to other rules, but contains pre-existing references.
   - *Possible compression approach*: A bootstrap compression candidate. Ensure it serves only as a entry-point pointer.
   - *Safety risk*: Low.
   - *Human review requirement*: Requires human review before edits.

4. `ROUTES-REGISTRY.md`
   - *Observed issue*: Repeats canonical path definitions.
   - *Possible compression approach*: Keep as a clean tabular index only. Do not add rules here.
   - *Safety risk*: Low.
   - *Human review requirement*: Requires human review before edits.

## Adapter Compression Candidates

We review the following adapter files for potential compression:

1. `AGENTS.md`
   - *Observed drift*: Repeats startup sequence rules and Russian-first explanations from `core-rules/MAIN.md`.
   - *Repeated instruction blocks*: Core principles of startup authority are duplicated.
   - *Adapter-specific delta candidate*: Retain only the instruction to read `llms.txt` and specific agent role declarations.
   - *Canonical reference candidate*: Replace core governance rules with references to `core-rules/MAIN.md`.
   - *Safety risk*: Medium. Adapter instructions must stay strictly limited to adapter scope and not introduce new rules.

2. `GEMINI.md`
   - *Observed drift*: Repeats Single-Role Execution, Readiness Assertions, and Russian-first instructions.
   - *Repeated instruction blocks*: Mandates on single-role execution and YAML safety.
   - *Adapter-specific delta candidate*: Retain only Gemini-specific runtime configurations.
   - *Canonical reference candidate*: Refer directly to `core-rules/MAIN.md` and `quality/MAIN.md`.
   - *Safety risk*: Medium.

3. `CLAUDE.md`
   - *Observed drift*: Identical structure to AGENTS.md.
   - *Repeated instruction blocks*: Duplicate copy of instructions for Claude agent bootstrapping.
   - *Adapter-specific delta candidate*: Retain only Claude-specific instructions.
   - *Canonical reference candidate*: Refer directly to `core-rules/MAIN.md`.
   - *Safety risk*: Medium.

4. `.github/copilot-instructions.md`
   - *Observed drift*: Duplicated rule structures.
   - *Repeated instruction blocks*: Standard instruction headers.
   - *Adapter-specific delta candidate*: Retain only Copilot specific behaviors.
   - *Canonical reference candidate*: Refer to `core-rules/MAIN.md`.
   - *Safety risk*: Low.

## Documentation Duplication Candidates

Using `docs/DUPLICATION-MAP.md` and `docs/SOURCE-OF-TRUTH-MAP.md`, we identify the following repeated documentation zones:
- Duplicated checklist definitions between `docs/SAFETY-BOUNDARIES.md` and `docs/GETTING-STARTED.md`.
- Overlapping description of verification gates between `docs/VALIDATION.md` and `quality/MAIN.md`.
- Repeat references to exit codes between `docs/SCRIPT-EXIT-CODE-STANDARD.md` and `docs/SCRIPT-OUTPUT-CONTRACT.md`.

These duplication zones are marked as compression candidates. We do not claim final duplication unless directly proven during execution.

## Boundary Statement Consolidation Candidates

Identify repeated boundary statements across files that may later be replaced by canonical references. We must preserve the exact meaning of:
- `PASS is not approval`
- `Evidence is not approval`
- `CI PASS is not approval`
- `UNKNOWN is not OK`
- `NOT_RUN is not PASS`
- `Human approval remains required`
- `No lifecycle mutation without explicit task`
- `Completion review is not approval`

During compression, these statements must not be weakened or removed. They are compression candidates for consolidation into `core-rules/MAIN.md` or a dedicated rules file, while keeping explicit references in reports.

## PASS / Evidence / Approval Boundary Preservation

The separation between PASS (automated tools validation), Evidence (reports/checklists tracking execution checks), and Approval (explicit human decision) must be preserved in all documentation.
- Automated validation results cannot be documented as overriding human approval.
- Artifacts generated by scripts are evidence only.
- The plan enforces that no documentation changes will imply automatic completion or automatic release gates.

## Canonical Candidate Areas

We identify the following canonical candidate areas:
- Core governance rules (`core-rules/MAIN.md`)
- State transition validation rules (`state/MAIN.md`)
- Execution sequence rules (`workflow/MAIN.md`)
- Evidence verification requirements (`quality/MAIN.md`)
- Data safety boundaries (`security/MAIN.md`)
- Active task binding records (`tasks/active-task.md`)

## Supporting Documentation Candidate Areas

We identify the following supporting doc candidates:
- Operational instructions in `docs/GETTING-STARTED.md`
- Verification guides in `docs/VALIDATION.md`
- Core safety limits in `docs/SAFETY-BOUNDARIES.md`
- Non-authoritative summaries in `FAQ.md`

## Possible Deprecated Candidate Areas

We identify the following possible deprecated candidates:
- Older transition and placement guide artifacts (`docs/task-20260426-*`)
- Redundant legacy files such as duplicate handoff text copies (`HANDOFF 2.md`)
- Numbered prompt/instruction backups under `docs/` that repeat active rules

## Reference Cleanup Candidates

We identify the following reference cleanup candidates:
- Stale links to legacy validation scripts (e.g. references to `run-all.sh` inside validator documentation).
- Broken or duplicate module links within `docs/`.
- Stale state-machine maps referencing deprecated lifecycle stages.

## Files Explicitly Out of Scope For M70

The following files and folders are explicitly out of scope for M70 work:
- `scripts/`
- `schemas/`
- `tests/` and `tests/fixtures/`
- `.github/workflows/`
- `data/`
- M61–M67 protected artifacts (listed in the next section)
- M71+ artifacts
- M76+ artifacts

## Protected Artifacts Boundary

The following M61–M67 protected validation files are strictly read-only and must not be modified:
- `schemas/task-validation-package.schema.json`
- `schemas/task-validation-result.schema.json`
- `scripts/check-task-validation-contract.py`
- `schemas/agent-task-output-evidence.schema.json`
- `scripts/check-agent-task-evidence.py`
- `schemas/acceptance-criteria-check-package.schema.json`
- `scripts/check-acceptance-criteria.py`
- `schemas/unified-runner-input.schema.json`
- `scripts/run-task-validation.py`
- `scripts/check-false-pass-resistance.py`
- `tests/fixtures/m67-false-pass-resistance/`
- `docs/COMPLETION-GATE-HARDENING-CONTRACT.md`
- `reports/m63-completion-review.md`
- `reports/m64-completion-review.md`
- `reports/m65-completion-review.md`
- `reports/m66-completion-review.md`
- `reports/m67-completion-review.md`

## Proposed M70 Execution Order

The proposed sequence for milestone execution:
- 70.2 — Canonical Docs and Deprecated Docs Registry
- 70.3 — Source-of-Truth Rules
- 70.4 — Adapter Drift Resolution Plan
- 70.5 — Bootstrap Surface Compression
- 70.6 — Adapter Files Compression
- 70.7 — Documentation Reference Cleanup
- 70.8 — M70 Documentation Compression Evidence Report
- 70.9 — M70 Completion Review

This execution order is planning only.
Each M70 task requires a separate task brief.

## Risk Register

- *Risk*: Broken boot links due to `llms.txt` compression. *Mitigation*: Run check-links.py and validation scripts.
- *Risk*: Loss of boundary definitions. *Mitigation*: Retain exact copies of all mandatory boundary statements in canonical rules.
- *Risk*: Adapter files drift. *Mitigation*: Use strict linting to prevent adapter files from introducing new rules.

## Human Review Checkpoints

We enforce a human checkpoint before:
- modifying bootstrap files
- modifying adapter files
- marking documents as deprecated
- replacing repeated boundary statements with references
- changing any source-of-truth relationship
- changing any validation authority wording
- changing any script reference wording that may imply authority

## Non-Goals

- Execution of documentation cleanup or deletion during the planning task.
- Modification of any scripts or validators.
- Consolidation of active code structures.
- Bypassing human reviews for verification.

## M70.2 Preparation Decision

may_prepare_m70_2: true_with_warnings

may_prepare_m70_2 is roadmap preparation only.
may_prepare_m70_2 does not start M70.2.
may_prepare_m70_2 is not approval.

## Explicit Non-Approval Boundary

This plan is a planning artifact only.
This plan does not compress documentation.
This plan does not modify bootstrap files.
This plan does not modify adapter files.
This plan does not modify scripts.
This plan does not approve cleanup, deletion, compression, consolidation, registry creation, validator creation, fixture creation, or lifecycle mutation.
This plan does not start M70.2.
Human review remains required.

## Final Status

FINAL_STATUS: M70_DOCUMENTATION_COMPRESSION_PLAN_COMPLETE_WITH_WARNINGS
