# Source-of-Truth Rules

## Task Boundary

This source-of-truth rules document is a documentation governance artifact only.
This source-of-truth rules document does not modify source-of-truth documents.
This source-of-truth rules document does not modify bootstrap files.
This source-of-truth rules document does not modify adapter files.
This source-of-truth rules document does not modify scripts.
This source-of-truth rules document does not create machine-readable registry authority.
This source-of-truth rules document does not approve cleanup, deletion, compression, consolidation, registry creation, validator creation, fixture creation, or lifecycle mutation.
Human review remains required.

## Active Task Record

- id: task-70.3
- milestone: M70
- name: "Source-of-Truth Rules"
- status: active
- mode: "EXECUTION / DOCUMENTATION GOVERNANCE / SOURCE-OF-TRUTH RULES"
- branch: dev
- started_at: "2026-05-28"

## Inputs Reviewed

- `reports/m70-m69-completion-intake.md`
- `docs/DOCUMENTATION-COMPRESSION-PLAN.md`
- `docs/CANONICAL-DOCS-REGISTRY.md`
- `docs/DEPRECATED-DOCS-REGISTRY.md`
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

## M70.2 Registry Status

The Markdown registries are complete with warnings:
- `docs/CANONICAL-DOCS-REGISTRY.md` -> `FINAL_STATUS: M70_CANONICAL_DOCS_REGISTRY_COMPLETE_WITH_WARNINGS`
- `docs/DEPRECATED-DOCS-REGISTRY.md` -> `FINAL_STATUS: M70_DEPRECATED_DOCS_REGISTRY_COMPLETE_WITH_WARNINGS`
The warnings from unresolved validation authority drift and possible deprecated candidates carry forward.

## Source-of-Truth Authority Model

Markdown/YAML are the source of truth for meaning, policy, architecture, and human-readable governance.
Reports are evidence, not approval.
JSON, SQLite, indexes, manifests, and caches are derived or navigation artifacts unless a later milestone explicitly defines otherwise.
Scripts check stable deterministic rules only.
Human approval remains above PASS, evidence, and CI.

## Markdown / YAML Authority Rules

Canonical Markdown/YAML documents may define governance meaning.
Supporting documents may explain canonical rules but must not override them.
Deprecated candidates remain visible until a separate human-reviewed deprecation path exists.
No source-of-truth document may be replaced or modified without explicit human approval.

## Report Evidence Rules

Evidence reports do not approve work.
Completion reviews do not create human approval.
A report may record readiness, but readiness is not authorization.
Reports are evidence artifacts, not approval and not source-of-truth authority.

## JSON / Index / Cache Artifact Rules

JSON artifacts may support validation, navigation, indexing, or consistency checks.
JSON artifacts must not become a second source of truth without explicit milestone approval.
SQLite/cache artifacts are rebuildable and must not be source of truth.
They must remain secondary, derived outputs only.

## Script Authority Rules

Scripts may check deterministic and stable invariants.
Scripts must not simulate human approval.
Scripts must not convert UNKNOWN to PASS.
Scripts must not convert NOT_RUN to PASS.
Scripts must not mutate lifecycle state unless explicitly tasked and governed.
Scripts provide check evidence only.

## Adapter Authority Rules

Adapter files may contain adapter-specific delta only.
Adapter files must not override canonical governance rules.
Adapter files must not create new approval semantics.
Adapter files must not create new lifecycle semantics.
Adapter files must not expand command or write permissions.
Adapter instructions are always subject to canonical guidelines.

## Bootstrap Authority Rules

Bootstrap files should route users and agents to source-of-truth documents.
Bootstrap files should not become hidden governance authority.
Bootstrap files should remain compact and reference canonical sources where safe.
They must serve only as directional entry points.

## Registry Authority Rules

M70 Markdown registries are planning artifacts.
M70 Markdown registries do not create machine-readable registry authority.
Machine-readable registry layer belongs to M72.
Registries do not override source-of-truth documents.

## Reference Replacement Rules

Repeated text can be replaced by references under these conditions:

Allowed only if:
- referenced source exists
- referenced source is stable enough
- meaning is preserved
- safety boundary remains visible where operationally required
- human review is not hidden
- no approval/lifecycle claim is introduced

Forbidden if:
- replacement hides PASS/evidence/approval separation
- replacement hides protected artifact boundary
- replacement hides fail-closed semantics
- replacement changes meaning
- replacement makes adapter file more authoritative than canonical docs

## Boundary Statement Compression Rules

We must preserve the exact meanings of key boundary statements:
- `PASS is not approval.`
- `Evidence is not approval.`
- `CI PASS is not approval.`
- `UNKNOWN is not OK.`
- `NOT_RUN is not PASS.`
- `Human approval cannot be simulated.`
- `Human review remains required.`
- `No lifecycle mutation without explicit governed task.`
- `Final validation dispatcher cleanup belongs to M73.`

During compression, these statements may be referenced or consolidated, but their exact meaning must be kept visible where operationally required.

## PASS / Evidence / Approval Preservation Rules

Automated test outputs (PASS), milestone/session evidence (Evidence), and human verification checkpoints (Approval) must be kept strictly separate. Documentation compression must not blend these terms or imply automated validation can replace human review.

## Lifecycle Mutation Preservation Rules

State transition and milestone completion records must not be mutated or automated by documents. Every state change requires an explicit task and human verification.

## Validation Authority Caution Until M73

Until M73 resolves unified validation dispatcher cleanup, M70 documents must use cautious wording around validation entrypoints.
M70 must not state that a validation entrypoint is final canonical authority unless already proven by existing evidence and not contradicted by M69.
Final validation dispatcher cleanup belongs to M73.

## Deprecated Candidate Handling Rules

Possible deprecated documents are not deleted in M70.3.
Possible deprecated documents require human review before final deprecation.
Possible deprecated documents require a deprecation path before removal.
They remain visible until their deprecation path is approved.

## Protected Artifact Reference Rules

Any reference to M61-M67 protected artifacts must respect their read-only and no-modify status. Compression must not affect or reference them in a way that implies authority changes.

## Human Review Requirements

Human review is required before:
- changing source-of-truth relationships
- marking documents finally deprecated
- deleting documents
- replacing repeated safety boundaries with references
- changing validation authority wording
- modifying bootstrap files
- modifying adapter files
- changing references to protected artifacts

## Explicit Non-Approval Boundary

This source-of-truth rules document is a documentation governance artifact only.
This source-of-truth rules document does not modify source-of-truth documents.
This source-of-truth rules document does not modify bootstrap files.
This source-of-truth rules document does not modify adapter files.
This source-of-truth rules document does not modify scripts.
This source-of-truth rules document does not create machine-readable registry authority.
This source-of-truth rules document does not approve cleanup, deletion, compression, consolidation, registry creation, validator creation, fixture creation, or lifecycle mutation.
Human review remains required.

## M70.4 Preparation Decision

may_prepare_m70_4: true_with_warnings

may_prepare_m70_4 is roadmap preparation only.
may_prepare_m70_4 does not start M70.4.
may_prepare_m70_4 is not approval.

## Final Status

FINAL_STATUS: M70_SOURCE_OF_TRUTH_RULES_COMPLETE_WITH_WARNINGS
