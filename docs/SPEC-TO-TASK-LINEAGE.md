---
type: canonical
module: product-spec
status: draft
authority: supporting
created: 2026-05-21
last_validated: unknown
---

# Spec-to-Task Lineage

## Purpose
Lineage connects Product Spec intent to downstream task artifacts.

Lineage exists so AgentOS can answer:
- which Product Spec produced this task?
- which Product Spec version was used?
- which task graph came from which spec?
- which task contracts are stale after spec changes?
- which downstream artifacts need revalidation?

Lineage is traceability.
Lineage is not approval.
Lineage is not execution authorization.
Lineage does not bypass task state rules.
Lineage does not bypass runtime enforcement.

## Non-Authority Boundary
This document defines lineage policy.
It does not authorize execution, commit, push, merge, deploy, or release.
It does not create approval records.
It does not replace human gate requirements.
It does not override runtime enforcement.
It does not override task transition rules.

## Required Lineage Identifiers
lineage:
  spec_id:
  spec_version:
  source_interview_id:
  product_spec_path:
  lifecycle_status_at_generation:
  generated_at:
  generated_by:
  generator:
  generated_task_graphs:
  generated_task_contracts:

Field meaning:
- spec_id: stable Product Spec identifier.
- spec_version: Product Spec version used for generation.
- source_interview_id: upstream interview artifact ID; nullable if unavailable.
- product_spec_path: repo-relative path to Product Spec.
- lifecycle_status_at_generation: Product Spec lifecycle status at generation time.
- generated_at: date/time when lineage was created.
- generated_by: agent/user/tool identity; use `unknown` when unavailable.
- generator: generator name/version, `manual`, or `unknown`.
- generated_task_graphs: list of repo-relative graph IDs/paths.
- generated_task_contracts: list of repo-relative contract IDs/paths.

Required path boundary:
- Use repo-relative paths only.

Forbidden:
- absolute local filesystem paths
- machine-specific paths
- secret-bearing paths
- URLs as the only source of lineage
- generated artifacts without spec_id
- generated artifacts without spec_version
- empty string as substitute for unknown identity
- empty string as substitute for unknown generator

## Lifecycle Compatibility
No Product Spec in APPROVED state means no downstream task generation.

No Product Spec in EXECUTION_READY state means no execution planning.

Lineage may be recorded for draft analysis, but must not be treated as downstream authorization.

lineage_status:
  - DRAFT_TRACE
  - GENERATED
  - STALE
  - SUSPENDED
  - REVALIDATED
  - ARCHIVED

Status meaning:
- DRAFT_TRACE: lineage record for exploratory/non-executable draft work.
- GENERATED: downstream artifacts generated from current spec version.
- STALE: spec changed after downstream artifacts were generated.
- SUSPENDED: downstream task contracts must not proceed until revalidated.
- REVALIDATED: downstream artifacts reviewed against current spec version.
- ARCHIVED: lineage retained for history, not active downstream work.

A DRAFT_TRACE lineage record must not be treated as authorization for task generation or execution planning.

DRAFT_TRACE is for exploratory traceability only.
It does not permit downstream task contracts.
It does not permit execution planning.
It does not weaken APPROVED or EXECUTION_READY requirements.

A lineage record does not make a Product Spec executable.
A lineage record does not move tasks between lifecycle states.
A lineage record does not authorize task execution.

## Spec Versioning Rules
Product Specs must carry spec_id and spec_version.

Downstream artifacts must record the spec_id and spec_version they were generated from.

If spec_version changes after downstream artifacts are generated, those artifacts must be treated as potentially stale until reviewed.

version_impact:

  material_spec_change:
    requires_new_spec_version: true
    downstream_status: STALE_OR_SUSPENDED
    requires_revalidation: true

  non_material_spec_change:
    requires_new_spec_version: false
    downstream_status: unchanged
    must_be_recorded: true

Material changes include changes to:
- Problem
- Goals
- Non-Goals
- Acceptance Criteria
- Constraints
- Risks
- Dependencies
- Open Questions
- Success Metrics
- lifecycle status

Material Product Spec changes invalidate previous execution readiness and may invalidate downstream task contracts.

## Downstream Invalidation Rules
downstream_invalidation_policy:

  spec_leaves_execution_ready:
    generated_task_contracts:
      status: SUSPENDED
      requires_revalidation: true

    generated_task_graphs:
      status: STALE
      requires_regeneration_or_review: true

  spec_material_change_after_generation:
    generated_task_contracts:
      status: SUSPENDED
      requires_revalidation: true

    generated_task_graphs:
      status: STALE
      requires_regeneration_or_review: true

  spec_archived:
    generated_task_contracts:
      status: SUSPENDED
      requires_human_review: true

    generated_task_graphs:
      status: ARCHIVED
      requires_human_review: true

If a Product Spec leaves EXECUTION_READY due to material changes, downstream generated task contracts must not continue as if the spec were still valid.

Downstream invalidation is a policy requirement only in this task.

This task does not implement task suspension automation.
This task does not modify task state files.
This task does not move task contracts to SUSPENDED.

## Relationship to Task Graphs
A task graph may reference:
- spec_id
- spec_version
- product_spec_path
- generated milestone candidates
- generated task candidates
- dependencies
- blocking relationships

Task graphs are downstream planning artifacts.
Task graphs are not execution authority.
Task graphs must not override Product Spec lifecycle state.
Task graphs must not override task transition rules.

Task graph lineage should be marked STALE if:
- Product Spec leaves EXECUTION_READY
- Product Spec has material changes
- Product Spec version changes
- Product Spec is archived
- human review marks lineage invalid

## Relationship to Task Contracts
Task contracts generated from Product Specs must include:
source_product_spec:
  spec_id:
  spec_version:
  product_spec_path:
  lineage_record:

Task contracts inherit product intent from Product Specs but do not inherit approval automatically.

Task contracts still require existing task validation, task state rules, scope controls, and execution gates.

A valid Product Spec lineage does not mean the task contract is executable.

Task contracts must be treated as SUSPENDED or non-executable if:
- source Product Spec leaves EXECUTION_READY
- source Product Spec has material changes
- recorded spec_version no longer matches current Product Spec version
- lineage record is missing
- lineage record is invalid
- human review blocks downstream continuation

This is policy only.
Do not implement suspension logic.

## Relationship to Existing Task Lifecycle
Product Spec lineage governs traceability between product intent and downstream task artifacts.

Task lifecycle governs executable task state.

Lineage status does not directly mutate task state.

Task state changes require existing task transition rules.

## Audit Expectations
A lineage record should support these audit questions:
- Which spec generated this downstream artifact?
- Which spec version was used?
- What lifecycle state was the spec in at generation time?
- Which generator/tool/person created the downstream artifact?
- Which task graph or task contracts were produced?
- Was the spec later changed materially?
- Should downstream artifacts be revalidated?
- Are generated artifacts stale or suspended?

Lineage supports auditability.
Lineage does not replace evidence reports.
Lineage does not replace human approval records.

## Cross Reference
- Validation policy: 

## Cross Reference
- Validation policy: docs/PRODUCT-SPEC-VALIDATION.md
