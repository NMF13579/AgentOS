# AgentOS Execution Verification Registry Contract

## Purpose

Define the contract for a future machine-readable execution verification registry for M56–M60 artifacts.

## Scope

This task defines the registry contract and schema only.

## Preconditions

M60 intake, architecture, inventory, source-of-truth classification, and duplication/drift audit are present and not blocked.

## Registry Role

Registry is a navigation and validation aid.
Registry does not override canonical Markdown contracts, policy documents, schemas, CLI contracts, fixture oracles, or completion reviews.
If registry conflicts with canonical source-of-truth artifacts, the registry is considered stale or invalid.
Registry must not introduce new authority.
Registry must not create approval.
Registry must not change execution verification semantics.

The registry may help tools find artifacts.
The registry may help validators detect missing paths.
The registry may help humans navigate the execution verification subsystem.
The registry may not redefine policy.
The registry may not redefine status meanings.
The registry may not redefine exit code mappings.
The registry may not authorize execution, approval, merge, push, release, lifecycle mutation, M61, or M62.

## Non-Authority Boundary

M60 registry contract is not approval.
M60 registry contract does not start cleanup execution.
M60 registry contract does not mutate lifecycle state.
M60 registry contract does not authorize merge, push, or release.
M60 registry contract does not change M56–M59 safety semantics.
M60 registry contract does not create registry data.
M60 registry contract does not create registry builder or validator scripts.
M60 registry contract does not delete, rename, move, archive, deprecate, or consolidate artifacts.
M60 registry contract does not authorize starting 60.6 automatically.

## Source-of-Truth Relationship

This contract follows `docs/EXECUTION-VERIFICATION-SOURCE-OF-TRUTH.md` and `reports/m60-artifact-inventory.md` and `reports/m60-duplication-drift-audit.md`.
If registry conflicts with source-of-truth classification, the registry is invalid.
If registry conflicts with canonical contracts, policies, schemas, CLI behavior, fixture oracles, or completion reviews, the registry is invalid.
If registry marks an artifact canonical but source-of-truth classification does not support it, the registry is invalid.
If registry omits a do-not-delete artifact known from source-of-truth classification, the registry is incomplete or invalid.

## Registry Object Structure

Top-level required fields:
- registry_version
- generated_by
- generated_at
- source_contract
- source_classification
- source_inventory
- source_duplication_drift_audit
- non_authority
- artifacts

## Artifact Entry Fields

Required per entry:
- artifact_id
- path
- milestone
- task_id
- artifact_type
- semantics_role
- source_of_truth_role
- authority_level
- status
- depends_on
- validated_by
- owned_by_layer
- deprecated
- replacement_path
- do_not_delete
- notes

## Enum Values

artifact_type:
- doc
- schema
- template
- script
- fixture
- fixture_oracle
- runner
- report
- intake_report
- architecture_doc
- contract_doc
- policy_doc
- cli_doc
- integration_summary
- action_review
- evidence_report
- completion_review
- registry_contract
- registry_schema
- registry_data
- generated_index
- unknown

semantics_role:
- policy
- contract
- implementation
- schema
- template
- fixture
- fixture_oracle
- runner
- report
- completion_review
- action_review
- evidence_report
- integration_summary
- intake_report
- architecture
- supporting_doc
- generated_index
- registry_contract
- registry_schema
- deprecated_candidate
- unknown

source_of_truth_role:
- canonical
- supporting
- generated
- test-only
- deprecated-candidate
- do-not-delete
- unknown

authority_level:
- canonical
- supporting
- non-authoritative
- generated
- test-only
- deprecated-candidate
- unknown

status:
- present
- missing
- planned
- blocked
- stale
- invalid
- deprecated-candidate
- manual-review-required

owned_by_layer:
- M56_EXECUTION_READINESS
- M57_EXECUTION_AUTHORIZATION
- M58_CONTROLLED_EXECUTION_SESSION
- M59_EXECUTION_RESULT_VERIFICATION
- M60_CLEANUP_CONSOLIDATION
- UNKNOWN

## Preservation Rules

do_not_delete: true is a preservation signal.
do_not_delete: true does not necessarily mean canonical.
canonical and do_not_delete are not the same.
A supporting artifact may be do_not_delete if required for audit, traceability, evidence, fixtures, or historical milestone closure.

## Deprecation Rules

deprecated: true in registry data is not an in-place file deprecation.
Registry deprecation is a recorded classification only.
No artifact may be deleted, archived, renamed, moved, or consolidated based only on registry data.
Any future deprecation requires explicit documentation pruning / consolidation task approval.
replacement_path must be nullable string.
notes must be a string.

## Dependency Rules

depends_on must not create authority override.
depends_on is navigation and validation metadata.
Missing dependency should make registry validation fail or warn according to 60.6 validator rules.
Circular dependencies should be reported by future validator when safely detectable.

## Conflict Rules

If registry conflicts with source-of-truth classification, the registry is invalid.
If registry conflicts with canonical contracts, policies, schemas, CLI behavior, fixture oracles, or completion reviews, the registry is invalid.
If registry marks an artifact canonical but source-of-truth classification does not support it, the registry is invalid.
If registry omits a do-not-delete artifact known from source-of-truth classification, the registry is incomplete or invalid.

## Validation Expectations for 60.6

60.6 should validate schema conformance, dependency references, enum integrity, missing required fields, stale conflict checks, and do_not_delete preservation coverage.

## Relationship to 60.2 Artifact Inventory

Registry entries are sourced from inventory coverage but inventory itself is not authoritative.

## Relationship to 60.3 Source-of-Truth Classification

source_of_truth_role and authority_level must align with the 60.3 classification output.

## Relationship to 60.4 Duplication and Drift Audit

Registry metadata should include links/notes for drift-sensitive or manual-review-required entries.

## Relationship to Future Validators

Future validators may check structure and consistency but must not redefine policy, status meanings, or authority.

## Forbidden Uses

- Using registry to override canonical docs/policies/contracts/schemas/scripts/oracles/reviews
- Using registry as approval mechanism
- Using registry as merge/push/release/lifecycle authorization source

## Risks

- Stale registry entries if not synchronized with canonical sources
- False authority assumptions by tools if non-authority boundaries are ignored

## Final Contract Status

FINAL_STATUS: M60_REGISTRY_CONTRACT_DEFINED

This means only that the registry contract and schema are defined.
It does not mean registry data exists.
It does not mean registry builder exists.
It does not mean registry validator exists.
It does not mean artifacts were consolidated.
It does not mean M60 cleanup is complete.
