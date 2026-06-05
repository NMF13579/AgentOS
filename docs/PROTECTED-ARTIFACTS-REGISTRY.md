# Protected Artifacts Registry

## Purpose

This registry lists protected AgentOS artifacts that require human review routing and careful change boundaries.

## Registry Authority Boundary

Protected artifact registry is a source-of-truth registry for protected artifact review requirements.
Protected artifact registry is not approval.
Protected artifact registry does not authorize changes.
Protected artifact registry does not modify protected artifacts.
Protected artifact registry does not create canonical artifact registry.
Protected artifact registry does not create ownership gap map.

## Source-of-Truth Boundary

Markdown/YAML artifacts are source of truth.
JSON, SQLite, indexes, caches, and generated reports are derived or navigation artifacts only.
Generated artifacts must not override Markdown/YAML source-of-truth artifacts.
Evidence is not approval.
PASS is not approval.
CI PASS is not approval.
Human approval cannot be simulated.

## Input Model

This registry is derived from the M72.1 protected artifact model and the existing AgentOS governance documents.

## Registry Scope

The registry covers high-confidence protected artifacts and review-required protected artifacts only.
It does not attempt to classify the whole repository.
It does not duplicate M71 script inventory.
It does not create canonical registry entries.

## Inclusion Rules

- Include protected governance core artifacts.
- Include completion gate artifacts.
- Include false PASS resistance artifacts.
- Include approval boundary artifacts.
- Include lifecycle mutation artifacts.
- Include runtime enforcement artifacts.
- Include validation authority artifacts.
- Include protected templates and protected schemas when they are clear protected boundary artifacts.

## Exclusion Rules

- Do not classify all docs.
- Do not classify all scripts.
- Do not classify all reports.
- Do not classify all templates.
- Do not classify all schemas.
- Do not classify all workflows.
- Do not classify all generated files.
- Do not classify all cache files.

## Protected Artifact Classes

- `PROTECTED_GOVERNANCE_CORE`
- `PROTECTED_COMPLETION_GATE`
- `PROTECTED_FALSE_PASS_RESISTANCE`
- `PROTECTED_APPROVAL_BOUNDARY`
- `PROTECTED_LIFECYCLE_MUTATION`
- `PROTECTED_RUNTIME_ENFORCEMENT`
- `PROTECTED_VALIDATION_AUTHORITY`
- `REVIEW_REQUIRED_UNKNOWN`

## Protection Levels

- `HIGH_PROTECTED`
- `MEDIUM_PROTECTED`
- `LOW_PROTECTED`
- `REVIEW_REQUIRED_UNKNOWN`

## Registry Fields

Each registry row records:
- `path`
- `artifact_class`
- `protection_level`
- `owner_required`
- `human_checkpoint_required`
- `allowed_change_path`
- `forbidden_change_path`
- `source_of_truth`
- `generated_or_derived`
- `entry_confidence`
- `notes`

## Protected Artifacts Table

| path | artifact_class | protection_level | owner_required | human_checkpoint_required | allowed_change_path | forbidden_change_path | source_of_truth | generated_or_derived | entry_confidence | notes |
| docs/PROTECTED-ARTIFACT-MODEL.md | PROTECTED_GOVERNANCE_CORE | HIGH_PROTECTED | true | true | governed model update with explicit rationale | silent overwrite or boundary weakening | true | false | HIGH_CONFIDENCE | source-of-truth model document |
| reports/m71-completion-review.md | PROTECTED_COMPLETION_GATE | MEDIUM_PROTECTED | true | true | governed completion-review update with human review | overwrite without review or approval claim | true | true | MEDIUM_CONFIDENCE | completion gate evidence artifact |
| docs/FALSE-PASS-RESISTANCE-SEMANTICS.md | PROTECTED_FALSE_PASS_RESISTANCE | MEDIUM_PROTECTED | true | true | governed semantics update with explicit rationale | weakening PASS/approval boundaries | true | false | MEDIUM_CONFIDENCE | false-pass boundary document |
| docs/AGENTOS-EXECUTION-VERIFICATION-REGISTRY-CONTRACT.md | PROTECTED_APPROVAL_BOUNDARY | HIGH_PROTECTED | true | true | governed boundary update with explicit rationale | turning verification registry into approval | true | false | HIGH_CONFIDENCE | registry cannot authorize execution or approval |
| scripts/validate-lifecycle-apply.py | PROTECTED_LIFECYCLE_MUTATION | HIGH_PROTECTED | true | true | governed validator update with explicit review | mutating lifecycle behavior without governed task scope | false | false | HIGH_CONFIDENCE | lifecycle mutation boundary validator |
| scripts/check-execution-readiness.py | PROTECTED_RUNTIME_ENFORCEMENT | MEDIUM_PROTECTED | true | true | governed readiness update with rationale | weakening readiness enforcement | false | false | MEDIUM_CONFIDENCE | runtime enforcement for readiness checks |
| schemas/validator-authority.schema.json | PROTECTED_VALIDATION_AUTHORITY | HIGH_PROTECTED | true | true | governed schema update with explicit rationale | weakening validator authority checks | true | false | HIGH_CONFIDENCE | protected schema for validator authority |
| templates/task-execution-authorization-input.md | PROTECTED_APPROVAL_BOUNDARY | MEDIUM_PROTECTED | true | true | governed template update with explicit rationale | expanding approval surface or bypassing human gate | true | false | MEDIUM_CONFIDENCE | protected template for execution authorization input |

## Registry Entry Counts

registry_is_source_of_truth: true
registry_entries_are_review_requirements_not_approval: true
protected_registry_created: true
protected_registry_has_entries: true
protected_registry_entry_count: 8
high_or_medium_confidence_entry_count: 8
review_required_unknown_entry_count: 0
empty_path_entries_found: false

## Review-Required Unknowns

No review-required unknown entries were needed for this registry pass.

## Owner Requirement Boundary

Owner requirement is review routing, not approval.
Owner presence does not authorize changes.
Missing owner must be carried forward, not hidden.
Placeholder owner must be treated as a warning or blocker depending on protection level.

## Human Checkpoint Boundary

Protected artifact changes require explicit human checkpoint.
Canonical artifact changes require explicit rationale.
Human checkpoint cannot be replaced by PASS.
Human checkpoint cannot be replaced by evidence.
Human checkpoint cannot be replaced by CI.
Human checkpoint cannot be simulated by an agent.

## CODEOWNERS Boundary

CODEOWNERS is a review routing mechanism.
CODEOWNERS is not approval by itself.
CODEOWNERS is not branch protection by itself.
CODEOWNERS does not prove platform enforcement.
This protected artifact registry does not modify CODEOWNERS.

## Branch Protection Boundary

Branch protection is platform-level enforcement.
Branch protection must not be claimed unless configured and verified.
This protected artifact registry does not configure branch protection.
This protected artifact registry does not claim platform enforcement.

## JSON / Derived Artifact Boundary

JSON, SQLite, indexes, caches, and generated reports are derived or navigation artifacts only.
Generated artifacts must not override Markdown/YAML source-of-truth artifacts.
This protected artifact registry does not create JSON authority.
This protected artifact registry does not create JSON artifacts.

## Change Authorization Boundary

This protected artifact registry does not authorize protected artifact changes.
This protected artifact registry does not authorize cleanup.
This protected artifact registry does not create canonical artifact registry.
This protected artifact registry does not create ownership gap map.

## Cleanup Boundary

cleanup_authorized: false
cleanup_performed: false

No cleanup is authorized or performed by this registry.

## Examples Boundary

Examples in this registry are illustrative only and do not create registry entries.

## Non-Goals

This registry does not become a full repository inventory.
This registry does not duplicate M71 script inventory.
This registry does not approve anything.
This registry does not classify all files in the repository.

## M72.3 Preparation Decision

warnings_carried_forward: true
pre_existing_changes:
- none
m72_2_changes:
- `tasks/active-task.md`
- `docs/PROTECTED-ARTIFACTS-REGISTRY.md`
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
m72_3_started: false
scope_violations: false
may_prepare_m72_3: true_with_warnings
may_prepare_m72_3 is roadmap preparation only.
may_prepare_m72_3 does not start M72.3.
may_prepare_m72_3 is not approval.
Human review remains required.

## Explicit Non-Approval Boundary

This protected artifact registry is a source-of-truth registry for protected artifact review requirements.
This protected artifact registry is not approval.
This protected artifact registry does not authorize protected artifact changes.
This protected artifact registry does not authorize cleanup.
This protected artifact registry does not create canonical artifact registry.
This protected artifact registry does not create ownership gap map.
This protected artifact registry does not modify CODEOWNERS.
This protected artifact registry does not configure branch protection.
This protected artifact registry does not claim platform enforcement.
This protected artifact registry does not create JSON authority.
This protected artifact registry does not create JSON artifacts.
This protected artifact registry does not start M72.3.
may_prepare_m72_3 is roadmap preparation only.
may_prepare_m72_3 does not start M72.3.
may_prepare_m72_3 is not approval.
Human review remains required.

## Final Status

FINAL_STATUS: M72_PROTECTED_ARTIFACT_REGISTRY_COMPLETE_WITH_WARNINGS
