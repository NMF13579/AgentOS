---
type: canonical
module: product-spec
status: draft
authority: supporting
created: 2026-05-21
last_validated: unknown
---

# Product Spec Validation

## Purpose
Product Spec validation checks deterministic structure and safety boundaries.

Product Spec validation does not prove product quality.
Product Spec validation does not prove feasibility.
Product Spec validation does not detect every semantic contradiction.
Product Spec validation does not authorize execution.

Validation is not approval.
Validation does not authorize execution.
Validation does not authorize task generation.
Validation does not authorize execution planning.
Validation does not authorize commit, push, merge, deploy, or release.

A structurally valid Product Spec is not automatically EXECUTION_READY.

A validation PASS does not authorize task generation, execution planning, commit, push, merge, deploy, or release.

## Validation Layers
| Layer | Responsibility |
|---|---|
| JSON syntax/schema files | schema files are valid JSON |
| Product Spec structural validation | frontmatter, lifecycle status, required sections |
| Safety boundary validation | no execution/approval/deployment authority claims |
| Future semantic review | contradictions, realism, hidden assumptions |
| Future readiness gate | whether validated spec may proceed downstream |

## Deterministic Validator Scope
The validator checks:
- file existence and readability;
- frontmatter delimiters and required flat fields;
- allowed frontmatter status values;
- body lifecycle_status presence and allowed values;
- required Product Spec headings;
- required Goals / Success Metrics / Non-Goals / Open Questions structure;
- lineage placeholders;
- forbidden authority phrases.

The validator does not implement:
- semantic contradiction detection;
- feasibility estimation;
- UX validation;
- task generation;
- execution planning;
- lifecycle transition automation;
- runtime enforcement.

## Open Questions Markers
For APPROVED Product Specs:
- unresolved Open Questions require `open_questions_acknowledged_by_human: true`.

For EXECUTION_READY Product Specs:
- unresolved Open Questions with `open_questions_block_execution_ready: true` fail validation.

## Lineage Placeholder Rules
Expected placeholders:

lineage:
  source_interview_id:
  generated_task_graphs:
  generated_task_contracts:

Missing placeholders fail structural validation.
Empty lineage arrays are allowed.

## Non-Authority Boundary
This document defines validation policy only.
It does not create approvals.
It does not change Product Spec lifecycle state.
It does not override runtime enforcement.

- Readiness gate policy: docs/PRODUCT-SPEC-READINESS-GATE.md

- Requirement extraction rules: docs/REQUIREMENT-EXTRACTION-RULES.md
- Clarification policy: docs/CLARIFICATION-QUESTION-POLICY.md

- Product summary policy: docs/PRODUCT-SUMMARY-POLICY.md
