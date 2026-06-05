# New Artifact Pre-Write Gate

## Purpose

This policy controls creation of future repository artifacts. Its purpose is to prevent uncontrolled growth of reports, docs, scripts, schemas, workflows, templates, indexes, and other artifacts.

## Scope

This policy applies before creating any new artifact in the repository. It does not clean the repository and does not delete, move, archive, compress, rename, rewrite, or consolidate existing files.

## Non-Approval Boundary

The pre-write gate is not approval.
The pre-write gate is not cleanup authorization.
The pre-write gate is not lifecycle mutation.
The pre-write gate is not task completion.

## Artifact Types Covered

The gate covers at least these artifact types:

- `report`
- `docs`
- `canonical`
- `protected`
- `script`
- `schema`
- `workflow`
- `fixture`
- `template`
- `adapter`
- `generated_index`
- `registry`
- `dependency_map`
- `task_lifecycle`
- `unknown`

## Pre-Write Gate Requirement

New artifact creation is blocked unless the pre-write packet is complete.

- Every new artifact must have a clear reason before it is created.
- Reuse of an existing artifact must be checked first.
- If the artifact would create a new source of truth, a human checkpoint is required first.

## Required Pre-Write Packet

```yaml
prewrite_packet:
  proposed_path: "<path>"
  artifact_type: "report | docs | canonical | protected | script | schema | workflow | fixture | template | adapter | generated_index | registry | dependency_map | task_lifecycle | unknown"
  purpose: "<specific purpose>"
  milestone_or_task: "<id>"
  authority_level: "canonical | protected | supporting | generated | evidence | draft | unknown"
  source_of_truth: true | false | unknown
  owner_area: "<area or unknown>"
  existing_artifact_reuse_checked: true | false
  why_existing_artifact_cannot_be_used: "<reason or unknown>"
  dependency_impact_checked: true | false
  expected_references:
    - "<path or none>"
  lifecycle_expectation: "active | temporary | historical | generated | unknown"
  cleanup_authorization: false
  approval_created: false
  lifecycle_mutation_created: false
  human_checkpoint_required: true | false
  human_checkpoint_present: true | false
```

## Source-of-Truth Classification

- `source_of_truth: true` means the artifact becomes a primary reference for future decisions.
- `source_of_truth: false` means the artifact supports another source.
- `source_of_truth: unknown` is blocked.

Unknown source-of-truth status is blocked.
A new source of truth requires an explicit human checkpoint.

## Authority Classification

- `canonical` means primary rule or primary reference.
- `protected` means sensitive artifact that must not be changed casually.
- `supporting` means supporting context.
- `generated` means produced from another source.
- `evidence` means proof or record.
- `draft` means not active authority.
- `unknown` is blocked.

Unknown authority is blocked.
Protected and canonical artifacts require an explicit human checkpoint.

## Duplicate Artifact Check

- A new artifact must not duplicate an existing artifact without a clear reason.
- The creator must check whether an existing artifact can be reused.
- If duplication is not justified, creation must be blocked.

## Dependency Impact Check

- Every new artifact must include a dependency check.
- Dependency means expected references, links, validation use, ownership impact, or confusion risk.
- If dependency impact is not checked, creation must be blocked.

## Lifecycle Expectation

- `active` means intended for current use.
- `temporary` means short-lived supporting use.
- `historical` means retained for traceability.
- `generated` means derived output.
- `unknown` is blocked until clarified.

## Human Checkpoint Rules

Explicit human checkpoint is required for:

- a new canonical artifact
- a new protected artifact
- a new source of truth
- a new workflow
- a new schema that affects validation authority
- a new script that affects validation authority
- a new task lifecycle mutation file
- any artifact that changes approval, evidence, PASS, lifecycle, or cleanup semantics

An agent cannot self-declare human checkpoint.

## Allowed Gate Decisions

- `ALLOW_CREATE`
- `ALLOW_CREATE_WITH_WARNINGS`

## Blocked Gate Decisions

- `BLOCK_DUPLICATE_ARTIFACT`
- `BLOCK_UNKNOWN_ARTIFACT_TYPE`
- `BLOCK_UNKNOWN_AUTHORITY`
- `BLOCK_UNKNOWN_SOURCE_OF_TRUTH`
- `BLOCK_MISSING_PURPOSE`
- `BLOCK_MISSING_REUSE_CHECK`
- `BLOCK_MISSING_DEPENDENCY_CHECK`
- `BLOCK_PROTECTED_WITHOUT_HUMAN_CHECKPOINT`
- `BLOCK_CANONICAL_WITHOUT_HUMAN_CHECKPOINT`
- `BLOCK_NEW_SOURCE_OF_TRUTH_WITHOUT_HUMAN_CHECKPOINT`
- `BLOCK_SCOPE_EXPANSION`
- `BLOCK_CLEANUP_AUTHORIZATION_CLAIM`
- `BLOCK_APPROVAL_CLAIM`
- `BLOCK_LIFECYCLE_MUTATION_CLAIM`

## Forbidden Interpretations

- Do not treat the gate as approval.
- Do not treat the gate as cleanup authorization.
- Do not treat the gate as task completion.
- Do not treat a completed packet as automatic permission.
- Do not treat an unclear artifact as acceptable.

## Validation Checklist

- Artifact type is known.
- Purpose is specific.
- Reuse of existing artifact was checked.
- Dependency impact was checked.
- Authority is known.
- Source-of-truth status is known.
- Human checkpoint is present where required.
- Cleanup authorization remains false.
- Approval remains false.
- Lifecycle mutation remains false.

Unknown artifact type is blocked.
