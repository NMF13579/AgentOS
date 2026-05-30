# M73.5 — Existing Entrypoint Alignment Plan

## Purpose
This alignment plan analyzes and maps the existing validation entrypoints in the AgentOS repository to the M73 validation authority model, thin dispatcher contract, and dispatcher IO contract. It establishes recommended pathways, checkpoints, and sequences for future tasks without authorizing changes or finalizing decisions.

## Input Preconditions
m73_4_dispatcher_io_contract_exists: true
m73_4_creation_report_exists: true
m73_4_final_status: M73_DISPATCHER_IO_CONTRACT_COMPLETE_WITH_WARNINGS
may_prepare_m73_5: true_with_warnings
m73_5_allowed_to_run: true_with_warnings

## Source Artifacts Reviewed
m73_1_inventory_reviewed: true
m73_2_authority_model_reviewed: true
m73_3_thin_dispatcher_contract_reviewed: true
m73_4_dispatcher_io_contract_reviewed: true
protected_registry_reviewed: true
canonical_registry_reviewed: true
protected_change_policy_reviewed: true

Limitation Record:
- The root level `VALIDATORS.md` is not present in the workspace root. We reviewed `scripts/VALIDATORS.md` as its local equivalent and documented references accordingly.

## Current Entrypoint Summary
entrypoint_count: 7
canonical_dispatcher_candidates_count: 1
compatibility_wrapper_candidates_count: 1
legacy_entrypoint_candidates_count: 5
unknown_entrypoint_classification_count: 0
authority_claim_count: 5
ci_authority_claim_count: 1
ci_approval_claim_count: 0
protected_or_canonical_entrypoint_count: 2
unknown_review_required_count: 5

## Candidate Dispatcher Analysis
The following candidate coordinates validation run flows:

- path: `scripts/agentos-validate.py`
  candidate_reason: It is the only Python coordinator validator running child checks and outputting validation results.
  evidence_from_inventory: Currently aggregates results and writes machine JSON output.
  matches_authority_model: true
  matches_thin_dispatcher_contract: true
  matches_io_contract: true
  protected_status: NOT_PROTECTED
  canonical_status: NOT_CANONICAL
  pre_write_checkpoint_required: true
  future_task: 73.6
  recommendation: candidate_for_73_6

Wording Reference:
- `scripts/agentos-validate.py` may be a canonical thin dispatcher candidate pending M73.6 pre-write check.

## Compatibility Wrapper Analysis
The wrappers below provide convenience but must delegate exit codes to the dispatcher:

- path: `scripts/run-all.sh`
  candidate_reason: Existing shell validation runner scripts.
  delegation_target_candidate: `scripts/agentos-validate.py`
  preserve_exit_code_required: true
  help_side_effect_risk: low
  protected_status: NOT_PROTECTED
  canonical_status: NOT_CANONICAL
  pre_write_checkpoint_required: true
  future_task: 73.7
  recommendation: candidate_for_73_7

- path: `scripts/health-check.sh`
  candidate_reason: Top-level entrypoint that runs validation checks alongside other repository architecture verification.
  delegation_target_candidate: `scripts/agentos-validate.py`
  preserve_exit_code_required: true
  help_side_effect_risk: low
  protected_status: NOT_PROTECTED
  canonical_status: NOT_CANONICAL
  pre_write_checkpoint_required: true
  future_task: 73.7
  recommendation: candidate_for_73_7

Wording Reference:
- `run-all.sh` may be a compatibility wrapper candidate pending M73.7 pre-write check.

## Legacy Entrypoint Analysis
The legacy targets overlap with the thin dispatcher candidate and should be deprecated:

- path: `scripts/validate-architecture.sh`
  legacy_reason: Custom shell wrapper logic that overlaps with newer python architectural checks.
  overlap_with: `scripts/health-check.sh`
  authority_claim_risk: low
  mutation_risk: low
  protected_status: NOT_PROTECTED
  canonical_status: NOT_CANONICAL
  cleanup_authorized: false
  deprecation_final: false
  future_handling: deprecate and redirect validation flows to dispatcher
  recommendation: document_as_legacy_candidate

- path: `scripts/validate-lifecycle-apply.py`
  legacy_reason: Governs high-risk lifecycle mutations rather than checking code correctness.
  overlap_with: none
  authority_claim_risk: high
  mutation_risk: high
  protected_status: PROTECTED
  canonical_status: NOT_CANONICAL
  cleanup_authorized: false
  deprecation_final: false
  future_handling: keep separate from thin dispatcher execution
  recommendation: do_not_modify_in_m73

- path: `scripts/check-execution-readiness.py`
  legacy_reason: Controls execution checks rather than static model checks.
  overlap_with: `scripts/check-active-task-readiness.py`
  authority_claim_risk: high
  mutation_risk: medium
  protected_status: PROTECTED
  canonical_status: NOT_CANONICAL
  cleanup_authorized: false
  deprecation_final: false
  future_handling: keep separate from thin dispatcher checks
  recommendation: do_not_modify_in_m73

## Documentation Reference Alignment Candidates
The documents below reference validation commands and require alignment:

- path: `README.md`
  reference_issue: Lists unsupported legacy validation subcommands.
  current_reference: References `python3 scripts/agentos-validate.py template`, `negative`, `guard`, etc.
  desired_reference_direction: Align with the consolidated commands defined in the thin dispatcher contract.
  protected_status: NOT_PROTECTED
  canonical_status: NOT_CANONICAL
  pre_write_checkpoint_required: true
  future_task: 73.8
  recommendation: candidate_for_73_8

- path: `scripts/VALIDATORS.md`
  reference_issue: Mentions outdated legacy validation checks.
  current_reference: Lists legacy architecture check wrappers.
  desired_reference_direction: Align lists with the thin dispatcher candidate checks.
  protected_status: NOT_PROTECTED
  canonical_status: NOT_CANONICAL
  pre_write_checkpoint_required: true
  future_task: 73.8
  recommendation: candidate_for_73_8

## CI / Workflow Alignment Candidates
The workflows below invoke validation commands and require alignment:

- path: `.github/workflows/agentos-validate.yml`
  validation_command: `python scripts/agentos-validate.py all`
  authority_claim_risk: medium
  claims_approval: false
  claims_platform_enforcement: false
  exit_2_interpretation_present: false
  pass_with_warnings_visibility_present: false
  protected_status: NOT_PROTECTED
  canonical_status: NOT_CANONICAL
  pre_write_checkpoint_required: true
  future_task: 73.8
  recommendation: candidate_for_73_8

## Protected / Canonical Pre-Write Requirements
protected_registry_read: true
canonical_registry_read: true
protected_change_policy_read: true
protected_targets_count: 8
canonical_targets_count: 10
unknown_target_status_count: 0
human_checkpoint_required_count: 14

Any future write to a protected or canonical target requires explicit human checkpoint evidence before the write when M72 policy requires it.
UNKNOWN protected/canonical status blocks writes.
Agent-written claims do not satisfy human checkpoint evidence.
Readiness is not write authorization.
Evidence is not write authorization.
PASS is not write authorization.

## Proposed Alignment Sequence
We recommend the following sequence of validation tasks:

1. Task: 73.6 — Thin Dispatcher Implementation with Protected/Canonical Pre-Write Check
   candidate_targets: `scripts/agentos-validate.py`
   required_pre_write_inputs: `docs/THIN-DISPATCHER-CONTRACT.md`, `docs/DISPATCHER-IO-CONTRACT.md`
   expected_action: Implement dispatcher exit codes and error mapping in Python.
   blocked_if: M73.6 pre-write checklist is incomplete or unverified.
   must_not_do: change validation semantics or bypass failures.

2. Task: 73.7 — Compatibility Wrapper / Legacy Entrypoint Alignment with Structured Pre-Write Check
   candidate_targets: `scripts/run-all.sh`, `scripts/health-check.sh`, `scripts/validate-architecture.sh`
   required_pre_write_inputs: `docs/THIN-DISPATCHER-CONTRACT.md`, `docs/DISPATCHER-IO-CONTRACT.md`
   expected_action: Realign wrappers to delegate to the thin dispatcher.
   blocked_if: wrapper exits do not match dispatcher exits.
   must_not_do: delete files or finalize deprecation.

3. Task: 73.8 — Documentation / Workflow Reference Alignment with BLOCKED-by-default Protected File Rule
   candidate_targets: `README.md`, `.github/workflows/agentos-validate.yml`
   required_pre_write_inputs: `docs/CANONICAL-ARTIFACTS-REGISTRY.md`, `docs/PROTECTED-ARTIFACTS-REGISTRY.md`
   expected_action: Update documentation markdown references and CI workflow step commands.
   blocked_if: branch protection is claimed without verification.
   must_not_do: bypass human checkpoints on protected registry targets.

The sequence preserves this rule:
Implementation or alignment may occur only in the later scoped task with its own pre-write check.

## Forbidden Alignment Actions
This planning document does not authorize:
- script modification
- wrapper modification
- docs modification
- workflow modification
- cleanup
- deletion
- final deprecation
- dispatcher implementation
- dispatcher selection as completed decision
- protected/canonical writes
- approval
- lifecycle mutation
- M74 start
- M74 regression fixtures

## Risk and Warning Carry-Forward
m73_4_warnings_carried_forward: true
m73_4_unknowns_carried_forward: true
warnings_carried_forward: true
exit_2_semantics_requires_m74_regression_fixture: true
pass_with_warnings_exit_0_requires_visible_warning_evidence: true

Warnings carried forward from M73.4/M73.3/M73.2/M73.1:
- Overlapping validation entrypoints.
- Shell execution risks in scripts and workflows.
- Documentation references drift in README.md.
- Embed of raw Python checks logic in CI workflow.

This planning document does not create M74 regression fixtures.

## Scope Verification
scripts_modified: false
workflows_modified: false
wrappers_modified: false
readme_modified: false
validators_md_modified: false
authority_model_modified: false
authority_model_report_modified: false
thin_dispatcher_contract_modified: false
thin_dispatcher_contract_report_modified: false
dispatcher_io_contract_modified: false
dispatcher_io_contract_report_modified: false
protected_canonical_registries_modified: false
lifecycle_mutation_occurred: false
approval_claim_created: false

## Premature Artifact Check
m73_6_plus_artifacts_created: false
m74_artifacts_created: false

## Validation Results
validation_commands_run: true
validation_passed: true

## Intake Decision for 73.6
may_prepare_m73_6: true_with_warnings

## Boundary Statement
M73.5 created the existing entrypoint alignment plan only.
M73.5 did not approve M72 or M73.
M73.5 did not select final dispatcher.
M73.5 did not implement dispatcher behavior.
M73.5 did not align scripts, wrappers, docs, or workflows.
M73.5 did not modify protected artifacts or canonical artifacts.
M73.5 did not authorize cleanup.
M73.5 did not declare deprecation final.
M73.5 did not start M73.6.
M73.5 did not start M74.
may_prepare_m73_6 is roadmap preparation readiness only and is not approval.

## Final Status
FINAL_STATUS: M73_ENTRYPOINT_ALIGNMENT_PLAN_COMPLETE_WITH_WARNINGS
