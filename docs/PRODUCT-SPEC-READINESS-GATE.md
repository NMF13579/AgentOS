---
type: canonical
module: product-spec
status: draft
authority: supporting
created: 2026-05-21
last_validated: unknown
---

# Product Spec Readiness Gate

## Purpose
The Product Spec Readiness Gate decides whether a structurally valid Product Spec may proceed to a downstream stage.

Readiness is stage-specific.

Readiness is not approval.
Readiness is not execution authorization.
Readiness does not bypass task validation.
Readiness does not bypass task transition rules.
Readiness does not bypass runtime enforcement.

Readiness PASS does not authorize execution, commit, push, merge, deploy, or release.

## Downstream Targets
| Target | Requirement |
|---|---|
| task-generation | Product Spec must be structurally valid and lifecycle_status must be APPROVED or EXECUTION_READY |
| execution-planning | Product Spec must be structurally valid and lifecycle_status must be EXECUTION_READY |

APPROVED is sufficient only for downstream task generation readiness.

APPROVED is not sufficient for execution planning readiness.

EXECUTION_READY is required for execution planning readiness.

## Target Rules
### task-generation
Ready only if:
- validation passed;
- lifecycle_status is APPROVED or EXECUTION_READY.

Task-generation readiness does not create task contracts.
Task-generation readiness does not authorize execution planning.
Task-generation readiness does not authorize task execution.

### execution-planning
Ready only if:
- validation passed;
- lifecycle_status is EXECUTION_READY.

Execution-planning readiness does not execute tasks.
Execution-planning readiness does not authorize commits.
Execution-planning readiness does not authorize push, merge, deploy, or release.

## Validator Dependency
The readiness gate relies on `scripts/validate-product-spec.py`.

Open Questions structural marker checks are performed by validate-product-spec.py.
The readiness gate must not downgrade Open Questions failures.

Lineage placeholder checks are performed by validate-product-spec.py.
The readiness gate must not require generated task graphs or generated task contracts to exist before task generation.
Empty generated_task_graphs and generated_task_contracts are allowed before downstream artifacts are created.

## Deterministic Mapping
VALIDATION_FAILED -> PRODUCT_SPEC_READINESS_NOT_READY

VALIDATION_BLOCKED -> PRODUCT_SPEC_READINESS_BLOCKED

VALIDATION_OK + missing/invalid body lifecycle_status -> PRODUCT_SPEC_READINESS_BLOCKED

VALIDATION_OK + valid lifecycle_status but target mismatch -> PRODUCT_SPEC_READINESS_NOT_READY

No fixture may have multiple acceptable expected results.
Every fixture/target combination must have exactly one expected result.

## Non-Authority Boundary
Readiness is not approval.
Readiness does not authorize execution.
Readiness does not authorize commit, push, merge, deploy, or release.
Readiness does not create task contracts.
Readiness does not create task graphs.
Readiness does not mutate task state.

- Requirement extraction rules: docs/REQUIREMENT-EXTRACTION-RULES.md
- Clarification policy: docs/CLARIFICATION-QUESTION-POLICY.md

- Product summary policy: docs/PRODUCT-SUMMARY-POLICY.md
