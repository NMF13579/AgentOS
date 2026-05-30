# Canonical Artifacts Registry

## Purpose

This registry lists canonical AgentOS artifacts that define source-of-truth review boundaries and change checkpoints.

## Registry Authority Boundary

Canonical artifact registry is a source-of-truth registry for canonical artifact review requirements.
Canonical artifact registry is not approval.
Canonical artifact registry does not authorize changes.
Canonical artifact registry does not modify canonical artifacts.
Canonical artifact registry does not modify protected artifact registry.
Canonical artifact registry does not create ownership gap map.

## Source-of-Truth Boundary

Markdown/YAML artifacts are source of truth.
JSON, SQLite, indexes, caches, and generated reports are derived or navigation artifacts only.
Generated artifacts must not override Markdown/YAML source-of-truth artifacts.
Evidence is not approval.
PASS is not approval.
CI PASS is not approval.
Human approval cannot be simulated.

## Input Model

This registry is derived from the M72.1 protected artifact model and the M72.2 protected artifact registry.

## Protected Registry Relationship

canonical does not automatically mean protected.
protected does not automatically mean canonical.
A path may appear in both protected and canonical registries only if the roles do not conflict.
Protected/canonical cross-conflict detection is deferred to M72.8.
M72.3 must not modify docs/PROTECTED-ARTIFACTS-REGISTRY.md.

## Registry Scope

The registry covers high-confidence canonical artifacts and review-required canonical artifacts only.
It does not attempt to classify the whole repository.
It does not duplicate M71 script inventory.
It does not create ownership gap maps.

## Inclusion Rules

- Include task lifecycle artifacts.
- Include approval boundary artifacts.
- Include completion review artifacts.
- Include false PASS resistance artifacts.
- Include evidence contract artifacts.
- Include validation contract artifacts.
- Include runtime enforcement artifacts.
- Include repository governance artifacts.
- Include protected artifact governance artifacts.

## Exclusion Rules

- Do not classify all docs.
- Do not classify all scripts.
- Do not classify all reports.
- Do not classify all templates.
- Do not classify all schemas.
- Do not classify all workflows.
- Do not classify all generated files.
- Do not classify all cache files.

## Canonical Domains

- `task_lifecycle`
- `approval_boundary`
- `completion_review`
- `false_pass_resistance`
- `evidence_contract`
- `validation_contract`
- `runtime_enforcement`
- `context_layer`
- `script_audit`
- `repository_governance`
- `protected_artifacts`
- `REVIEW_REQUIRED_UNKNOWN`

## Canonical Roles

- `PRIMARY_SOURCE_OF_TRUTH`
- `SUPPORTING_SOURCE_OF_TRUTH`
- `POLICY_CONTRACT`
- `SCHEMA_CONTRACT`
- `TEMPLATE_CONTRACT`
- `VALIDATOR_CONTRACT`
- `PROCESS_CONTRACT`
- `REVIEW_REQUIRED_UNKNOWN`

## Registry Fields

Each registry row records:
- `path`
- `canonical_domain`
- `canonical_role`
- `replaces_or_supersedes`
- `supporting_artifacts`
- `derived_artifacts`
- `owner_required`
- `change_checkpoint_required`
- `source_of_truth`
- `entry_confidence`
- `notes`

## Canonical Artifacts Table

| path | canonical_domain | canonical_role | replaces_or_supersedes | supporting_artifacts | derived_artifacts | owner_required | change_checkpoint_required | source_of_truth | entry_confidence | notes |
| tasks/active-task.md | task_lifecycle | PRIMARY_SOURCE_OF_TRUTH | none | reports/m71-completion-review.md | unknown | true | true | true | HIGH_CONFIDENCE | active task record and task boundary source |
| reports/m71-completion-review.md | completion_review | PRIMARY_SOURCE_OF_TRUTH | reports/m71-evidence-precheck.md; reports/m71-script-audit-evidence-report.md | reports/m71-m70-completion-intake.md | unknown | true | true | true | HIGH_CONFIDENCE | final M71 completion review |
| docs/FALSE-PASS-RESISTANCE-SEMANTICS.md | false_pass_resistance | POLICY_CONTRACT | none | docs/FALSE-PASS-RESISTANCE-CLAIM-BOUNDARY.md | unknown | true | true | true | HIGH_CONFIDENCE | false PASS semantics contract |
| docs/TASK-EXECUTION-AUTHORIZATION-POLICY.md | approval_boundary | POLICY_CONTRACT | none | docs/TASK-EXECUTION-AUTHORIZATION-INPUT-CONTRACT.md; templates/task-execution-authorization-input.md | unknown | true | true | true | HIGH_CONFIDENCE | approval boundary policy |
| docs/VALIDATION-EVIDENCE-CONTRACT.md | evidence_contract | PRIMARY_SOURCE_OF_TRUTH | none | schemas/validation-evidence.schema.json; templates/validation-evidence.md | unknown | true | true | true | HIGH_CONFIDENCE | evidence contract for validation artifacts |
| docs/TASK-VALIDATION-CONTRACT-VALIDATOR.md | validation_contract | VALIDATOR_CONTRACT | none | schemas/task-validation-result.schema.json; schemas/task-validation-package.schema.json | unknown | true | true | true | HIGH_CONFIDENCE | validator contract boundary |
| docs/TASK-EXECUTION-READINESS-POLICY.md | runtime_enforcement | PROCESS_CONTRACT | none | docs/TASK-EXECUTION-READINESS-INPUT-CONTRACT.md | unknown | true | true | true | HIGH_CONFIDENCE | runtime readiness enforcement policy |
| docs/CANONICAL-DOCS-REGISTRY.md | repository_governance | PRIMARY_SOURCE_OF_TRUTH | none | docs/REQUIRED-CHECK-NAMES.md; docs/COMPLETION-TRANSITION.md | unknown | true | true | true | HIGH_CONFIDENCE | canonical docs governance registry |
| docs/PROTECTED-ARTIFACT-MODEL.md | protected_artifacts | PRIMARY_SOURCE_OF_TRUTH | none | docs/PROTECTED-ARTIFACTS-REGISTRY.md | unknown | true | true | true | HIGH_CONFIDENCE | protected artifact governance model |
| schemas/validator-authority.schema.json | validation_contract | SCHEMA_CONTRACT | none | docs/VALIDATION-EVIDENCE-CONTRACT.md | templates/validator-authority-record.md | true | true | true | HIGH_CONFIDENCE | schema for validator authority records |

## Registry Entry Counts

registry_is_source_of_truth: true
registry_entries_are_review_requirements_not_approval: true
canonical_registry_created: true
canonical_registry_has_entries: true
canonical_registry_entry_count: 10
high_or_medium_confidence_entry_count: 10
review_required_unknown_entry_count: 0
source_of_truth_true_entry_count: 10
empty_path_entries_found: false
duplicate_path_entries_found: false
relation_fields_parseable: true
invalid_relation_field_entries: 0

## Relation Field Format

Relation fields use only `none`, `unknown`, or repo-relative paths separated by `;`.
Free prose is not allowed in relation fields.

## Review-Required Unknowns

No review-required unknown canonical entries were needed for this registry pass.

## Supporting Artifact Boundary

Supporting artifacts may inform review routing, but they do not authorize changes.

## Derived Artifact Boundary

Derived artifacts are navigation or output artifacts only and do not become authority.

## Owner Requirement Boundary

Owner requirement is review routing, not approval.
Owner presence does not authorize changes.
Missing owner must be carried forward, not hidden.
Placeholder owner must be treated as a warning or blocker depending on protection level.

## Change Checkpoint Boundary

Canonical artifact changes require explicit change checkpoint.
Human checkpoint cannot be replaced by PASS.
Human checkpoint cannot be replaced by evidence.
Human checkpoint cannot be replaced by CI.
Human checkpoint cannot be simulated by an agent.

## CODEOWNERS Boundary

CODEOWNERS is a review routing mechanism.
CODEOWNERS is not approval by itself.
CODEOWNERS is not branch protection by itself.
CODEOWNERS does not prove platform enforcement.
This canonical artifact registry does not modify CODEOWNERS.

## Branch Protection Boundary

Branch protection is platform-level enforcement.
Branch protection must not be claimed unless configured and verified.
This canonical artifact registry does not configure branch protection.
This canonical artifact registry does not claim platform enforcement.

## JSON / Derived Artifact Boundary

JSON, SQLite, indexes, caches, and generated reports are derived or navigation artifacts only.
Generated artifacts must not override Markdown/YAML source-of-truth artifacts.
This canonical artifact registry does not create JSON authority.
This canonical artifact registry does not create JSON artifacts.

## Change Authorization Boundary

This canonical artifact registry does not authorize canonical artifact changes.
This canonical artifact registry does not authorize protected artifact changes.
This canonical artifact registry does not authorize cleanup.
This canonical artifact registry does not modify protected artifact registry.
This canonical artifact registry does not create ownership gap map.

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

## M72.4 Preparation Decision

warnings_carried_forward: true
pre_existing_changes:
- none
m72_3_changes:
- `tasks/active-task.md`
- `docs/CANONICAL-ARTIFACTS-REGISTRY.md`
protected_registry_modified: false
ownership_gap_map_created: false
json_authority_created: false
json_artifacts_created: false
codeowners_modified: false
branch_protection_claimed: false
platform_enforcement_claimed: false
cleanup_authorized: false
cleanup_performed: false
protected_artifact_change_authorized: false
canonical_artifact_change_authorized: false
approval_claim_created: false
lifecycle_mutation_occurred: false
m72_4_started: false
scope_violations: false
may_prepare_m72_4: true_with_warnings
may_prepare_m72_4 is roadmap preparation only.
may_prepare_m72_4 does not start M72.4.
may_prepare_m72_4 is not approval.
Human review remains required.

## Explicit Non-Approval Boundary

This canonical artifact registry is a source-of-truth registry for canonical artifact review requirements.
This canonical artifact registry is not approval.
This canonical artifact registry does not authorize canonical artifact changes.
This canonical artifact registry does not authorize protected artifact changes.
This canonical artifact registry does not authorize cleanup.
This canonical artifact registry does not modify protected artifact registry.
This canonical artifact registry does not create ownership gap map.
This canonical artifact registry does not modify CODEOWNERS.
This canonical artifact registry does not configure branch protection.
This canonical artifact registry does not claim platform enforcement.
This canonical artifact registry does not create JSON authority.
This canonical artifact registry does not create JSON artifacts.
This canonical artifact registry does not start M72.4.
may_prepare_m72_4 is roadmap preparation only.
may_prepare_m72_4 does not start M72.4.
may_prepare_m72_4 is not approval.
Human review remains required.

## Final Status

FINAL_STATUS: M72_CANONICAL_ARTIFACT_REGISTRY_COMPLETE_WITH_WARNINGS
