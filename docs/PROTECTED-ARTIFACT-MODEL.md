# Protected Artifact Model

## Purpose

This model defines how AgentOS classifies protected, canonical, generated, derived, and unknown artifacts.
It is a source-of-truth model document for M72.1.

## Source-of-Truth Boundary

Markdown/YAML artifacts are source of truth.
JSON, SQLite, indexes, caches, and generated reports are derived or navigation artifacts only.
Generated artifacts must not override Markdown/YAML source-of-truth artifacts.
Evidence is not approval.
PASS is not approval.
CI PASS is not approval.
Human approval cannot be simulated.

## Artifact Categories

- `protected_artifact`
- `canonical_artifact`
- `generated_report`
- `derived_navigation_artifact`
- `cache_artifact`
- `unknown_review_required_artifact`

## Protected Artifact Definition

A protected artifact is a file whose change can affect governance, approval boundaries, lifecycle mutation, validation authority, or protected runtime behavior.
Protected artifacts require explicit human checkpoint before change.

## Canonical Artifact Definition

A canonical artifact is the primary source-of-truth document for a policy, template, schema, validator, or governance rule.
Canonical artifacts define how a rule should be read and applied.

## Generated Report Definition

A generated report is a derived evidence artifact produced from existing inputs.
It can summarize or reflect state, but it does not become the source of truth for upstream policy.

## Derived Navigation Artifact Definition

A derived navigation artifact helps locate or index other content.
It is useful for discovery, but it does not override the underlying Markdown/YAML source.

## Unknown / Review-Required Artifact Definition

An unknown artifact is one whose role, owner, or change impact is not clear enough for safe classification.
Unknown artifacts require review before any protection decision.

## Artifact Classes

- `PROTECTED_GOVERNANCE_CORE`
- `PROTECTED_COMPLETION_GATE`
- `PROTECTED_FALSE_PASS_RESISTANCE`
- `PROTECTED_APPROVAL_BOUNDARY`
- `PROTECTED_LIFECYCLE_MUTATION`
- `PROTECTED_RUNTIME_ENFORCEMENT`
- `PROTECTED_VALIDATION_AUTHORITY`
- `CANONICAL_POLICY_DOC`
- `CANONICAL_TEMPLATE`
- `CANONICAL_SCHEMA`
- `CANONICAL_VALIDATOR`
- `DERIVED_NAVIGATION_ARTIFACT`
- `GENERATED_REPORT`
- `REVIEW_REQUIRED_UNKNOWN`

## Protection Levels

- `HIGH_PROTECTED`
- `MEDIUM_PROTECTED`
- `LOW_PROTECTED`
- `REVIEW_REQUIRED_UNKNOWN`

`HIGH_PROTECTED` means any change requires explicit human checkpoint and review.
`MEDIUM_PROTECTED` means the change is sensitive and must be routed carefully with rationale.
`LOW_PROTECTED` means the artifact is still controlled, but the change risk is lower than core governance files.
`REVIEW_REQUIRED_UNKNOWN` means the artifact cannot be safely changed until its role is understood.

## Human Checkpoint Rules

Protected artifact changes require explicit human checkpoint.
Canonical artifact changes require explicit rationale.
Human checkpoint cannot be replaced by PASS.
Human checkpoint cannot be replaced by evidence.
Human checkpoint cannot be replaced by CI.
Human checkpoint cannot be simulated by an agent.

## Owner Requirement Rules

- `OWNER_DEFINED`
- `OWNER_MISSING`
- `OWNER_PLACEHOLDER`
- `OWNER_AMBIGUOUS`
- `CODEOWNERS_MISSING`
- `CHECKPOINT_MISSING`
- `REVIEW_REQUIRED`

Owner requirement is review routing, not approval.
Owner presence does not authorize changes.
Missing owner must be carried forward, not hidden.
Placeholder owner must be treated as a warning or blocker depending on protection level.

## Change Risk Levels

- `LOW_RISK_CHANGE`
- `MEDIUM_RISK_CHANGE`
- `HIGH_RISK_CHANGE`
- `BLOCKED_PROTECTED_CHANGE`
- `UNKNOWN_REVIEW_REQUIRED`

## Allowed Change Pathways

Allowed change pathways are:
- update a low-risk derived artifact after review;
- revise a canonical artifact with explicit rationale and human checkpoint;
- create a new generated report from reviewed source inputs;
- refine a model document when the change stays within M72.1 scope.

## Forbidden Change Pathways

Forbidden change pathways are:
- changing a protected artifact without human checkpoint;
- converting a derived artifact into source of truth;
- using evidence as approval;
- using PASS as approval;
- using CI PASS as approval;
- bypassing owner review;
- mutating lifecycle state without governed task scope.

## CODEOWNERS Relationship

CODEOWNERS is a review routing mechanism.
CODEOWNERS is not approval by itself.
CODEOWNERS is not branch protection by itself.
CODEOWNERS does not prove platform enforcement.
M72.1 does not modify CODEOWNERS.

## Branch Protection Relationship

Branch protection is platform-level enforcement.
Branch protection must not be claimed unless configured and verified.
M72.1 does not configure branch protection.
M72.1 does not claim platform enforcement.

## JSON / Index / Cache Boundary

JSON, SQLite, indexes, and caches are derived navigation or support artifacts unless explicitly promoted by a later governed task.
They must not override Markdown/YAML source-of-truth artifacts.
M72.1 defines the model only.
M72.1 does not create protected artifact registry.
M72.1 does not create canonical artifact registry.
M72.1 does not create ownership gap map.
M72.1 does not classify the full repository.

## Evidence / PASS / Approval Boundary

Evidence is not approval.
PASS is not approval.
CI PASS is not approval.
Human approval cannot be simulated.
Approval claims are not created by observation alone.

## Lifecycle Mutation Boundary

This model does not authorize lifecycle mutation.
Lifecycle mutation requires separate governed task scope and explicit human checkpoint.

## Registry Boundary

M72.1 defines the model only.
M72.1 does not create protected artifact registry.
M72.1 does not create canonical artifact registry.
M72.1 does not create ownership gap map.
M72.1 does not classify the full repository.

## Examples

example_only: `docs/PROTECTED-ARTIFACT-MODEL.md` -> `CANONICAL_POLICY_DOC`
example_only: `reports/m72-m71-completion-intake.md` -> `GENERATED_REPORT`
example_only: `reports/m72-m71-completion-intake.md` -> `DERIVED_NAVIGATION_ARTIFACT` when used as intake evidence

Examples in this model are illustrative only and do not create registry entries.

## Non-Goals

This model does not classify the whole repository.
This model does not create registry entries for specific files.
This model does not authorize cleanup.
This model does not approve protected artifact changes.
This model does not modify CODEOWNERS.
This model does not configure branch protection.
This model does not create JSON authority.

## M72.2 Preparation Decision

warnings_carried_forward: true
pre_existing_changes:
- none
m72_1_changes:
- `tasks/active-task.md`
- `docs/PROTECTED-ARTIFACT-MODEL.md`
model_is_source_of_truth: true
protected_registry_created: false
canonical_registry_created: false
ownership_gap_map_created: false
json_authority_created: false
json_artifacts_created: false
codeowners_modified: false
branch_protection_claimed: false
platform_enforcement_claimed: false
cleanup_authorized: false
cleanup_performed: false
protected_artifact_change_authorized: false
approval_claim_created: false
lifecycle_mutation_occurred: false
m72_2_started: false
scope_violations: false
may_prepare_m72_2: true_with_warnings
may_prepare_m72_2 is roadmap preparation only.
may_prepare_m72_2 does not start M72.2.
may_prepare_m72_2 is not approval.
Human review remains required.

## Explicit Non-Approval Boundary

This protected artifact model is a source-of-truth model document.
This protected artifact model is not approval.
This protected artifact model does not create protected artifact registry.
This protected artifact model does not create canonical artifact registry.
This protected artifact model does not create ownership gap map.
This protected artifact model does not authorize protected artifact changes.
This protected artifact model does not authorize cleanup.
This protected artifact model does not modify CODEOWNERS.
This protected artifact model does not configure branch protection.
This protected artifact model does not claim platform enforcement.
This protected artifact model does not create JSON authority.
Examples in this model are illustrative only and do not create registry entries.
may_prepare_m72_2 is roadmap preparation only.
may_prepare_m72_2 does not start M72.2.
may_prepare_m72_2 is not approval.
Human review remains required.

## Final Status

FINAL_STATUS: M72_PROTECTED_ARTIFACT_MODEL_COMPLETE_WITH_WARNINGS
