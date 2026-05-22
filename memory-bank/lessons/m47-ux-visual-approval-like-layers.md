---
type: agentos-lesson
source_milestone: M47
status: active
severity: medium
applies_to:
  - UX
  - preview
  - approval-like artifacts
  - readiness
  - task generation boundary
created: 2026-05-21
owner: human
---

# New UX / Visual / Approval-like Layers Require Semantic Model First

## Lesson
New UX / Visual / Approval-like Layers Require Semantic Model First.

## Problem
M47 became heavy because it introduced multiple artifacts that were close to implementation surfaces but were not allowed to become implementation authority.

Artifacts involved:
- UX Contract
- Static HTML Preview
- UX Visual Approval Snapshot
- UX Contract Validator
- M47 Evidence Report
- M47 Completion Review

## Root Cause
Ambiguity arose around:
- source of truth
- supporting evidence
- approval
- implementation permission
- task generation permission
- execution authorization

## Rule
For future milestones that introduce a new semantic layer, AgentOS must define the semantic model before creating policy, template, example, or validator tasks.

## Applies To
- UX
- preview
- approval-like artifacts
- readiness
- task generation boundary

## Required Future Behavior
Required order:
1. Authority model
2. Data model
3. Boundary model
4. Required statuses / decisions
5. Optional vs required artifacts
6. Validation strategy
7. Template / example
8. Evidence / completion review

Extra caution is required when artifacts include these terms:
- approval
- snapshot
- preview
- ready
- planning
- generation
- implementation
- execution

## Validation Implication
- Ready is not authorized.
- Validator PASS is not approval.
- Visual approval is supporting evidence only.
- Template uses placeholders.
- Example uses concrete values.
- Optional artifacts require explicit required flag and NOT_APPLICABLE sentinel.
- Stable simple validator is better than fragile smart validator.

## M47 Specific Findings
- UX Contract is source of truth for UX structure only.
- Static HTML Preview is optional visual explanation only.
- UX Visual Approval Snapshot is supporting evidence only.
- Visual direction approval does not authorize implementation.
- Readiness or validation must not be interpreted as task generation permission.

## Process Changes for M48+
Process questions for M48+:
- Does this task introduce a new artifact type?
- Can this artifact be mistaken for approval?
- Can this artifact be mistaken for implementation permission?
- Can this artifact trigger task generation?
- Does it need a data model before policy/template/example?
- Does it need optional/required semantics?
- Does it need a validator or only documentation?

## Non-Authority Boundary
Lesson is reusable process memory.
Lesson is not approval.
Lesson does not authorize task generation.
Lesson does not authorize execution planning.
Lesson does not authorize implementation.
Lesson does not authorize commit, push, merge, deploy, or release.
Lesson does not modify milestone completion status by itself.
To become enforceable, lesson must be translated into policy, template, validator, checklist, or completion criteria.

## Related Milestones
- M47
- M48
- M49
- M50+

This lesson should be applied before M48, M49, and any future milestone that introduces readiness, preview, snapshot, approval-like, or generation-adjacent artifacts.

## Summary
M47 showed that when a milestone introduces UX, preview, snapshot, readiness, or approval-like artifacts, semantic meaning must be defined first. This keeps source-of-truth boundaries clear and prevents supporting artifacts from being mistaken as implementation or execution authority.
