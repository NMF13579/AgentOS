# Protected Change Policy

## Purpose

This policy defines the minimum review rules for future protected and canonical artifact changes.

## Policy Authority Boundary

Protected Change Policy is a source-of-truth policy for future protected/canonical change review.
Protected Change Policy is not approval.
Protected Change Policy does not authorize any actual change.
Protected Change Policy does not modify protected artifacts.
Protected Change Policy does not modify canonical artifacts.
Protected Change Policy does not modify registries.
Protected Change Policy does not resolve ownership gaps.
Protected Change Policy does not configure platform enforcement.

## Source-of-Truth Boundary

Markdown/YAML artifacts are source of truth.
JSON, SQLite, indexes, caches, and generated reports are derived or navigation artifacts only.
Generated artifacts must not override Markdown/YAML source-of-truth artifacts.
Evidence is not approval.
PASS is not approval.
CI PASS is not approval.
Human approval cannot be simulated.

## Inputs Reviewed

- `docs/PROTECTED-ARTIFACT-MODEL.md`
- `docs/PROTECTED-ARTIFACTS-REGISTRY.md`
- `docs/CANONICAL-ARTIFACTS-REGISTRY.md`
- `docs/OWNERSHIP-GAP-MAP.md`
- `docs/CODEOWNERS-BRANCH-PROTECTION-ALIGNMENT.md`
- `reports/m72-m71-completion-intake.md`

## Protected Artifact Relationship

Protected artifact changes require explicit human checkpoint.
Protected artifact registry signals do not authorize changes.
Owner signals do not authorize changes.
Evidence does not authorize changes.
PASS does not authorize changes.

## Canonical Artifact Relationship

Canonical artifact changes require explicit human checkpoint.
Canonical registry signals do not authorize changes.
Owner signals do not authorize changes.
Evidence does not authorize changes.
PASS does not authorize changes.

## Ownership Gap Relationship

Ownership gaps must be carried forward.
Owner gaps block or warn future changes depending on risk.
Missing ownership must not be treated as OK.
Ownership gap signals do not resolve ownership gaps.

## CODEOWNERS / Platform Alignment Relationship

CODEOWNERS is review routing only.
CODEOWNERS does not equal approval.
Platform enforcement must not be claimed without external platform evidence.
M72.6 does not modify CODEOWNERS.
M72.6 does not configure branch protection.
M72.6 does not create GitHub rulesets.

## Change Classification

- `protected_artifact_change`
- `canonical_artifact_change`
- `protected_and_canonical_artifact_change`
- `generated_report_change`
- `derived_navigation_artifact_change`
- `cleanup_or_deletion`
- `registry_change`
- `unknown_artifact_change`

## Required Change Request Fields

change_request_id:
target_artifact_path:
artifact_status:
change_context:
change_summary:
reason_for_change:
requested_by:
owner_signal:
codeowners_status:
platform_status:
human_checkpoint_required:
approval_artifact_required:
expected_validation:
rollback_or_revert_plan:
risk_level:
scope_boundary:
forbidden_changes:
evidence_required:

## Human Checkpoint Rules

Protected artifact changes require explicit human checkpoint.
Canonical artifact changes require explicit human checkpoint.
Protected and canonical registry changes require explicit human checkpoint.
Human checkpoint cannot be replaced by PASS.
Human checkpoint cannot be replaced by evidence.
Human checkpoint cannot be replaced by CI.
Human checkpoint cannot be replaced by CODEOWNERS.
Human checkpoint cannot be replaced by owner signal.
Human checkpoint cannot be simulated by an agent.

## Owner Signal Rules

OWNER_DEFINED does not authorize changes by itself.
OWNER_MISSING must not be treated as OK.
OWNER_PLACEHOLDER must not be treated as real ownership.
OWNER_AMBIGUOUS requires review.
Ownership gaps must be carried forward.

## CODEOWNERS Rules

CODEOWNERS_COVERED does not equal approval.
CODEOWNERS_MISSING creates a warning or blocker depending on artifact risk.
CODEOWNERS_PLACEHOLDER_OWNER creates warning or blocker depending on artifact risk.
CODEOWNERS_UNKNOWN must not be treated as OK.
M72.6 does not modify CODEOWNERS.

## Branch Protection Rules

Branch protection requires platform-level evidence.
M72.6 does not configure branch protection.
M72.6 does not create GitHub rulesets.
M72.6 does not claim platform enforcement.

## Platform Enforcement Rules

Platform enforcement must not be claimed without external platform evidence.
PLATFORM_ENFORCEMENT_NOT_CLAIMED is a platform gap.
PLATFORM_ENFORCEMENT_UNKNOWN is a platform gap.
MANUAL_ADMIN_CHECK_REQUIRED must be carried forward.

## PASS / Evidence / Approval Separation

PASS is validation result only.
Evidence is supporting proof only.
CI PASS is platform validation only.
CODEOWNERS is review routing only.
Owner signal is review routing only.
None of these are approval.
Approval requires explicit human approval artifact or human checkpoint according to active AgentOS lifecycle rules.

## Allowed Change Pathways

- Human checkpoint plus valid change request fields plus no blocker conditions may allow a future governed change.
- Human checkpoint plus explicit owner routing plus explicit validation may allow a future governed change.

## Forbidden Change Pathways

- Registry entry alone is not enough.
- Owner signal alone is not enough.
- CODEOWNERS alone is not enough.
- CI PASS alone is not enough.
- Evidence alone is not enough.
- PASS alone is not enough.
- Approval is not simulated.
- Cleanup is not authorized here.

## Policy Decision Table

| change_context | artifact_status | owner_status | codeowners_status | platform_status | human_checkpoint_required | allowed_without_checkpoint | policy_decision | required_follow_up | carry_forward_required | notes |
| protected_artifact_change | PROTECTED | OWNER_MISSING | CODEOWNERS_MISSING | PLATFORM_ENFORCEMENT_NOT_CLAIMED | true | false | BLOCKED_PENDING_OWNER | human review and owner mapping later | true | protected change blocked until owner and routing are resolved |
| canonical_artifact_change | CANONICAL | OWNER_AMBIGUOUS | CODEOWNERS_MISSING | PLATFORM_ENFORCEMENT_NOT_CLAIMED | true | false | BLOCKED_PENDING_CODEOWNERS | human review and routing later | true | canonical change blocked until routing and ownership are clarified |
| protected_and_canonical_artifact_change | PROTECTED_AND_CANONICAL | OWNER_PLACEHOLDER | CODEOWNERS_PLACEHOLDER_OWNER | PLATFORM_ENFORCEMENT_UNKNOWN | true | false | ALLOW_WITH_WARNINGS_AND_HUMAN_CHECKPOINT | human checkpoint and external platform evidence later | true | placeholder and unknown platform state require warning carry-forward |
| cleanup_or_deletion | GENERATED_OR_DERIVED | NOT_APPLICABLE | CODEOWNERS_NOT_APPLICABLE | PLATFORM_ENFORCEMENT_NOT_CLAIMED | true | false | BLOCKED_PENDING_PLATFORM_REVIEW | manual admin review and explicit cleanup task later | true | cleanup stays blocked until platform posture is known |
| registry_change | UNKNOWN_REVIEW_REQUIRED | UNKNOWN | CODEOWNERS_UNKNOWN | MANUAL_ADMIN_CHECK_REQUIRED | true | false | BLOCKED_UNKNOWN_REVIEW_REQUIRED | human review, routing review, and platform evidence later | true | unknown review path must not be treated as safe |
| unknown_artifact_change | UNKNOWN_REVIEW_REQUIRED | UNKNOWN | CODEOWNERS_UNKNOWN | PLATFORM_ENFORCEMENT_UNKNOWN | true | false | BLOCKED_UNKNOWN_REVIEW_REQUIRED | classify artifact before any change request | true | unknown artifact requires classification first |

## Blocker Conditions

Any change touching protected or canonical artifacts is blocked when ownership is missing, ambiguous, or placeholder-based without a human checkpoint.
Any change is blocked when CODEOWNERS is missing or unknown for a high-risk artifact.
Any change is blocked when platform enforcement is not claimed and external evidence is absent.

## Warning Conditions

Warnings apply when ownership gaps are unresolved but a later human checkpoint is still possible.
Warnings apply when CODEOWNERS is missing or placeholder-based and later routing can be added.
Warnings apply when platform enforcement is not claimed and later external evidence may appear.

## Carry-Forward Rules

Unresolved ownership gaps must be carried forward.
Platform gaps must be carried forward.
Warning states must not be collapsed into clean approval.

## Cleanup Boundary

cleanup_authorized: false
cleanup_performed: false

This policy does not authorize cleanup.

## JSON / Derived Artifact Boundary

JSON, SQLite, indexes, caches, and generated reports are derived or navigation artifacts only.
Generated artifacts must not override Markdown/YAML source-of-truth artifacts.
This policy does not create JSON authority.
This policy does not create JSON artifacts.

## Non-Goals

This policy does not authorize actual changes.
This policy does not resolve ownership gaps.
This policy does not configure platform enforcement.
This policy does not modify registries.
This policy does not modify CODEOWNERS.

## M72.7 Preparation Decision

warnings_carried_forward: true
unresolved_ownership_gaps_exist: true
platform_gaps_exist: true
gaps_carried_forward: true
policy_is_source_of_truth: true
protected_change_policy_created: true
protected_registry_read: true
canonical_registry_read: true
ownership_gap_map_read: true
codeowners_alignment_review_read: true
protected_registry_modified: false
canonical_registry_modified: false
ownership_gap_map_modified: false
codeowners_alignment_review_modified: false
policy_authorizes_actual_change: false
policy_creates_approval: false
policy_creates_lifecycle_mutation: false
policy_creates_cleanup_authorization: false
policy_table_has_entries: true
policy_decision_entry_count: 6
blocked_decision_count: 4
warning_decision_count: 1
allowed_review_path_count: 0
invalid_policy_entries: 0
codeowners_modified: false
branch_protection_claimed: false
platform_enforcement_claimed: false
platform_enforcement_verified: false
owners_assigned: false
ownership_gaps_resolved: false
json_authority_created: false
json_artifacts_created: false
cleanup_authorized: false
cleanup_performed: false
protected_artifact_change_authorized: false
canonical_artifact_change_authorized: false
approval_claim_created: false
lifecycle_mutation_occurred: false
m72_7_started: false
scope_violations: false
may_prepare_m72_7: true_with_warnings
may_prepare_m72_7 is roadmap preparation only.
may_prepare_m72_7 does not start M72.7.
may_prepare_m72_7 is not approval.
Human review remains required.

## Explicit Non-Approval Boundary

This Protected Change Policy is a source-of-truth policy for future protected/canonical change review.
This Protected Change Policy is not approval.
This Protected Change Policy does not authorize any actual protected artifact change.
This Protected Change Policy does not authorize any actual canonical artifact change.
This Protected Change Policy does not authorize cleanup.
This Protected Change Policy does not modify protected artifacts.
This Protected Change Policy does not modify canonical artifacts.
This Protected Change Policy does not modify protected artifact registry.
This Protected Change Policy does not modify canonical artifact registry.
This Protected Change Policy does not modify ownership gap map.
This Protected Change Policy does not modify CODEOWNERS alignment review.
This Protected Change Policy does not modify CODEOWNERS.
This Protected Change Policy does not configure branch protection.
This Protected Change Policy does not claim platform enforcement.
This Protected Change Policy does not create JSON authority.
This Protected Change Policy does not create JSON artifacts.
This Protected Change Policy does not start M72.7.
may_prepare_m72_7 is roadmap preparation only.
may_prepare_m72_7 does not start M72.7.
may_prepare_m72_7 is not approval.
Human review remains required.

## Final Status

FINAL_STATUS: M72_PROTECTED_CHANGE_POLICY_COMPLETE_WITH_WARNINGS
