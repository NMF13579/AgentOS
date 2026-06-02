## Human Summary

- Can next M80 task be prepared: true_with_warnings
- Does this create new baseline: false
- Does this approve cleanup: false
- Does this start M81: false
- Main blockers:
  - "none"
- Main warnings:
  - "M80_0_WARNINGS_CARRIED_FORWARD"
  - "M79_WARNINGS_CARRIED_FORWARD"
  - "M78_WARNINGS_CARRIED_FORWARD"
  - "GIT_STATUS_HAS_UNRELATED_CHANGES"
- Required evidence usable: 9
- Required evidence missing: 0
- Required evidence unreadable: 0
- Supporting evidence missing: 0
- Evidence reliable for M80: true
- M81 artifacts created: false
- M81 task briefs created: false
- Next readiness field: "may_prepare_m80_2: true_with_warnings"
Human Summary must match machine-readable fields.

# Title
M80.1 Consolidation Source Evidence Intake

# Purpose
Classify the source material that M80 may rely on for consolidation. This is intake only. It does not create a baseline, update anything, or start downstream work.

# 80.0 Intake Check
- `reports/m80-m79-completion-intake.md` exists: true
- `reports/m80-m79-completion-intake.md` readable: true
- `m80_0_final_status_detected`: `FINAL_STATUS: M80_M79_COMPLETION_INTAKE_READY_WITH_WARNINGS`
- `m80_0_final_status_acceptable`: true
- `m80_0_readiness_detected`: `may_prepare_m80_1: true_with_warnings`
- `m80_0_readiness_acceptable`: true
- `m80_0` metadata captured from git: true
- `m80_0` last modified: `2026-06-02 07:19:39 +0500`
- `m80_0` last commit: `487e5a32912b97cb33e972d961803d934e18a7d5`

# Evidence Intake Method
Read-only file existence checks, read-only git metadata capture, and direct classification of evidence into required, supporting, usable, missing, unreadable, contradictory, unknown, blocking gap, and non-blocking gap buckets. Missing evidence stays missing. Unknown evidence stays unknown.

# Required Evidence Sources
```yaml
evidence_sources:
  - path: "reports/m76-pre-cleanup-baseline.md"
    evidence_group: "m76_baseline"
    required_for_m80_v1: true
    exists: true
    readable: true
    evidence_status: "usable"
    last_modified: "2026-06-01 09:39:21 +0500"
    last_commit: "6e3489237f09ce125422008a12c4771006b37519"
    metadata_available: true
    blocking_if_missing: true
    blocking_if_unreadable: true
    supports_m80_tasks: ["80.2", "80.3", "80.4", "80.5", "80.6", "80.7", "80.8"]
    notes: "Baseline source for M76 reference only; usable as context for M80 consolidation preparation."
  - path: "reports/m77-cleanup-plan.md"
    evidence_group: "m77_cleanup_plan"
    required_for_m80_v1: true
    exists: true
    readable: true
    evidence_status: "usable"
    last_modified: "2026-06-01 11:06:48 +0500"
    last_commit: "62fcc557f2e53b20098ad4b1ee6e12babdcbd3c4"
    metadata_available: true
    blocking_if_missing: true
    blocking_if_unreadable: true
    supports_m80_tasks: ["80.2", "80.3", "80.4", "80.5", "80.6", "80.7", "80.8"]
    notes: "Cleanup plan source remains readable and usable as historical context."
  - path: "reports/m78-completion-review.md"
    evidence_group: "m78_completion"
    required_for_m80_v1: true
    exists: true
    readable: true
    evidence_status: "usable"
    last_modified: "2026-06-02 06:19:11 +0500"
    last_commit: "00ff52c82da21fce355b31a04bceacc1bdbe73c0"
    metadata_available: true
    blocking_if_missing: true
    blocking_if_unreadable: true
    supports_m80_tasks: ["80.2", "80.3", "80.4", "80.5", "80.6", "80.7", "80.8"]
    notes: "M78 completion evidence is present and usable."
  - path: "reports/m78-physical-cleanup-diff-summary.md"
    evidence_group: "m78_diff"
    required_for_m80_v1: true
    exists: true
    readable: true
    evidence_status: "usable"
    last_modified: "2026-06-01 20:48:13 +0500"
    last_commit: "7a94683157c3e9890ad967fc941b2c5d871000e8"
    metadata_available: true
    blocking_if_missing: true
    blocking_if_unreadable: true
    supports_m80_tasks: ["80.2", "80.3", "80.4", "80.5", "80.6", "80.7", "80.8"]
    notes: "Diff summary is present and usable."
  - path: "reports/m78-validation-summary.md"
    evidence_group: "m78_validation"
    required_for_m80_v1: true
    exists: true
    readable: true
    evidence_status: "usable"
    last_modified: "2026-06-01 22:14:41 +0500"
    last_commit: "60c9855c2b80f8b3c989508df781f596025b11de"
    metadata_available: true
    blocking_if_missing: true
    blocking_if_unreadable: true
    supports_m80_tasks: ["80.2", "80.3", "80.4", "80.5", "80.6", "80.7", "80.8"]
    notes: "Validation summary is present and usable."
  - path: "reports/m79-completion-review.md"
    evidence_group: "m79_completion"
    required_for_m80_v1: true
    exists: true
    readable: true
    evidence_status: "usable"
    last_modified: "2026-06-02 07:14:39 +0500"
    last_commit: "28ca380417e90d5a508f834e479915ff4affa698"
    metadata_available: true
    blocking_if_missing: true
    blocking_if_unreadable: true
    supports_m80_tasks: ["80.2", "80.3", "80.4", "80.5", "80.6", "80.7", "80.8"]
    notes: "Primary M79 completion proof; carries the no-approval, no-lifecycle, no-repair, no-new-baseline boundary facts."
  - path: "reports/m79-post-cleanup-drift-report.md"
    evidence_group: "m79_drift"
    required_for_m80_v1: true
    exists: true
    readable: true
    evidence_status: "usable"
    last_modified: "2026-06-02 07:19:39 +0500"
    last_commit: "487e5a32912b97cb33e972d961803d934e18a7d5"
    metadata_available: true
    blocking_if_missing: true
    blocking_if_unreadable: true
    supports_m80_tasks: ["80.2", "80.3", "80.4", "80.5", "80.6", "80.7", "80.8"]
    notes: "Drift measurement is present and usable."
  - path: "reports/m79-baseline-comparison-report.md"
    evidence_group: "m79_baseline_comparison"
    required_for_m80_v1: true
    exists: true
    readable: true
    evidence_status: "usable"
    last_modified: "2026-06-02 07:19:39 +0500"
    last_commit: "487e5a32912b97cb33e972d961803d934e18a7d5"
    metadata_available: true
    blocking_if_missing: true
    blocking_if_unreadable: true
    supports_m80_tasks: ["80.2", "80.3", "80.4", "80.5", "80.6", "80.7", "80.8"]
    notes: "Baseline comparison is present and usable; unknowns and not-claimed metrics remain explicit."
  - path: "reports/m79-boundary-review.md"
    evidence_group: "m79_boundary"
    required_for_m80_v1: true
    exists: true
    readable: true
    evidence_status: "usable"
    last_modified: "2026-06-02 07:19:39 +0500"
    last_commit: "487e5a32912b97cb33e972d961803d934e18a7d5"
    metadata_available: true
    blocking_if_missing: true
    blocking_if_unreadable: true
    supports_m80_tasks: ["80.2", "80.3", "80.4", "80.5", "80.6", "80.7", "80.8"]
    notes: "Boundary review is present and usable; confirms no M80/M81 start and no approval/lifecycle/repair violations."
```

# Supporting Evidence Sources
```yaml
evidence_sources:
  - path: "reports/m80-m79-completion-intake.md"
    evidence_group: "m80_intake"
    required_for_m80_v1: false
    exists: true
    readable: true
    evidence_status: "usable"
    last_modified: "2026-06-02 07:19:39 +0500"
    last_commit: "487e5a32912b97cb33e972d961803d934e18a7d5"
    metadata_available: true
    blocking_if_missing: true
    blocking_if_unreadable: true
    supports_m80_tasks: ["80.2", "80.3", "80.4", "80.5", "80.6", "80.7", "80.8"]
    notes: "Required intake gate for M80.1; usable as the M80 readiness handoff."
  - path: "reports/m76-cleanup-candidate-inventory.md"
    evidence_group: "supporting"
    required_for_m80_v1: false
    exists: true
    readable: true
    evidence_status: "usable"
    last_modified: "2026-06-01 09:35:00 +0500"
    last_commit: "52e19bd0108521e87e86f23ec52a49772f7ebf7e"
    metadata_available: true
    blocking_if_missing: false
    blocking_if_unreadable: false
    supports_m80_tasks: ["80.2", "80.3", "80.4", "80.5", "80.6", "80.7", "80.8"]
    notes: "Supporting historical inventory."
  - path: "reports/m76-optimization-risk-map.md"
    evidence_group: "supporting"
    required_for_m80_v1: false
    exists: true
    readable: true
    evidence_status: "usable"
    last_modified: "2026-06-01 09:48:07 +0500"
    last_commit: "0f127c9724e9ff83a4dea98058e62a422b8948b7"
    metadata_available: true
    blocking_if_missing: false
    blocking_if_unreadable: false
    supports_m80_tasks: ["80.2", "80.3", "80.4", "80.5", "80.6", "80.7", "80.8"]
    notes: "Supporting risk context."
  - path: "reports/m76-optimization-scope-lock.md"
    evidence_group: "supporting"
    required_for_m80_v1: false
    exists: true
    readable: true
    evidence_status: "usable"
    last_modified: "2026-06-01 10:12:45 +0500"
    last_commit: "e126f29409384676bb951dfba867d319e6b3f82e"
    metadata_available: true
    blocking_if_missing: false
    blocking_if_unreadable: false
    supports_m80_tasks: ["80.2", "80.3", "80.4", "80.5", "80.6", "80.7", "80.8"]
    notes: "Supporting scope context."
  - path: "reports/m77-completion-review.md"
    evidence_group: "supporting"
    required_for_m80_v1: false
    exists: true
    readable: true
    evidence_status: "usable"
    last_modified: "2026-06-01 13:02:23 +0500"
    last_commit: "d4a936c449591ef0519151c9ea755558a4c746e1"
    metadata_available: true
    blocking_if_missing: false
    blocking_if_unreadable: false
    supports_m80_tasks: ["80.2", "80.3", "80.4", "80.5", "80.6", "80.7", "80.8"]
    notes: "Supporting completion review context."
  - path: "reports/m77-prewrite-check.md"
    evidence_group: "supporting"
    required_for_m80_v1: false
    exists: true
    readable: true
    evidence_status: "usable"
    last_modified: "2026-06-01 11:22:49 +0500"
    last_commit: "b19bf3ddb6abef0ff8ad5762d949196c6a48b4f8"
    metadata_available: true
    blocking_if_missing: false
    blocking_if_unreadable: false
    supports_m80_tasks: ["80.2", "80.3", "80.4", "80.5", "80.6", "80.7", "80.8"]
    notes: "Supporting prewrite evidence."
  - path: "reports/m77-rollback-plan.md"
    evidence_group: "supporting"
    required_for_m80_v1: false
    exists: true
    readable: true
    evidence_status: "usable"
    last_modified: "2026-06-01 11:32:37 +0500"
    last_commit: "ee2bcbc7431bf0af5e92d2d6ba58b300256ea381"
    metadata_available: true
    blocking_if_missing: false
    blocking_if_unreadable: false
    supports_m80_tasks: ["80.2", "80.3", "80.4", "80.5", "80.6", "80.7", "80.8"]
    notes: "Supporting rollback-plan context only; no rollback execution."
  - path: "reports/m77-protected-artifact-review.md"
    evidence_group: "supporting"
    required_for_m80_v1: false
    exists: true
    readable: true
    evidence_status: "usable"
    last_modified: "2026-06-01 10:52:13 +0500"
    last_commit: "d6e993e0bbd33c371b64a484ce3534f373a06215"
    metadata_available: true
    blocking_if_missing: false
    blocking_if_unreadable: false
    supports_m80_tasks: ["80.2", "80.3", "80.4", "80.5", "80.6", "80.7", "80.8"]
    notes: "Supporting protected-artifact context."
  - path: "reports/m77-human-checkpoint-requirements.md"
    evidence_group: "supporting"
    required_for_m80_v1: false
    exists: true
    readable: true
    evidence_status: "usable"
    last_modified: "2026-06-01 13:02:23 +0500"
    last_commit: "d4a936c449591ef0519151c9ea755558a4c746e1"
    metadata_available: true
    blocking_if_missing: false
    blocking_if_unreadable: false
    supports_m80_tasks: ["80.2", "80.3", "80.4", "80.5", "80.6", "80.7", "80.8"]
    notes: "Supporting human-checkpoint requirements."
  - path: "reports/m78-execution-scope-lock.md"
    evidence_group: "supporting"
    required_for_m80_v1: false
    exists: true
    readable: true
    evidence_status: "usable"
    last_modified: "2026-06-01 18:13:01 +0500"
    last_commit: "e6009aadf9279943d92e400cf6275862ad77e590"
    metadata_available: true
    blocking_if_missing: false
    blocking_if_unreadable: false
    supports_m80_tasks: ["80.2", "80.3", "80.4", "80.5", "80.6", "80.7", "80.8"]
    notes: "Supporting execution scope context."
  - path: "reports/m78-human-checkpoint-intake.md"
    evidence_group: "supporting"
    required_for_m80_v1: false
    exists: true
    readable: true
    evidence_status: "usable"
    last_modified: "2026-06-01 19:29:49 +0500"
    last_commit: "83630518af26548e67e5130e5c6ff906697150ab"
    metadata_available: true
    blocking_if_missing: false
    blocking_if_unreadable: false
    supports_m80_tasks: ["80.2", "80.3", "80.4", "80.5", "80.6", "80.7", "80.8"]
    notes: "Supporting human-checkpoint intake context."
  - path: "reports/m78-wave-1-cleanup-report.md"
    evidence_group: "supporting"
    required_for_m80_v1: false
    exists: true
    readable: true
    evidence_status: "usable"
    last_modified: "2026-06-01 19:38:20 +0500"
    last_commit: "8fe888265a5f9f682e1bf07f130e65b915a88e67"
    metadata_available: true
    blocking_if_missing: false
    blocking_if_unreadable: false
    supports_m80_tasks: ["80.2", "80.3", "80.4", "80.5", "80.6", "80.7", "80.8"]
    notes: "Supporting cleanup-wave evidence."
  - path: "reports/m78-wave-2-cleanup-report.md"
    evidence_group: "supporting"
    required_for_m80_v1: false
    exists: true
    readable: true
    evidence_status: "usable"
    last_modified: "2026-06-01 19:50:15 +0500"
    last_commit: "dd62ce8da8643d1a21152d9633f21d60bfc35f10"
    metadata_available: true
    blocking_if_missing: false
    blocking_if_unreadable: false
    supports_m80_tasks: ["80.2", "80.3", "80.4", "80.5", "80.6", "80.7", "80.8"]
    notes: "Supporting cleanup-wave evidence."
  - path: "reports/m78-wave-3-cleanup-report.md"
    evidence_group: "supporting"
    required_for_m80_v1: false
    exists: true
    readable: true
    evidence_status: "usable"
    last_modified: "2026-06-01 20:06:56 +0500"
    last_commit: "849bcbb9df70463c1e613cd22e76f54787f6df95"
    metadata_available: true
    blocking_if_missing: false
    blocking_if_unreadable: false
    supports_m80_tasks: ["80.2", "80.3", "80.4", "80.5", "80.6", "80.7", "80.8"]
    notes: "Supporting cleanup-wave evidence."
  - path: "reports/m78-wave-4-cleanup-report.md"
    evidence_group: "supporting"
    required_for_m80_v1: false
    exists: true
    readable: true
    evidence_status: "usable"
    last_modified: "2026-06-01 20:14:24 +0500"
    last_commit: "3cdccbb32c994d23300b52cf3aafd3bf5a1e00c6"
    metadata_available: true
    blocking_if_missing: false
    blocking_if_unreadable: false
    supports_m80_tasks: ["80.2", "80.3", "80.4", "80.5", "80.6", "80.7", "80.8"]
    notes: "Supporting cleanup-wave evidence."
  - path: "reports/m79-m78-completion-intake.md"
    evidence_group: "supporting"
    required_for_m80_v1: false
    exists: true
    readable: true
    evidence_status: "usable"
    last_modified: "2026-06-02 07:19:39 +0500"
    last_commit: "487e5a32912b97cb33e972d961803d934e18a7d5"
    metadata_available: true
    blocking_if_missing: false
    blocking_if_unreadable: false
    supports_m80_tasks: ["80.2", "80.3", "80.4", "80.5", "80.6", "80.7", "80.8"]
    notes: "Supporting M79 intake evidence."
  - path: "reports/m79-post-cleanup-evidence-intake.md"
    evidence_group: "supporting"
    required_for_m80_v1: false
    exists: true
    readable: true
    evidence_status: "usable"
    last_modified: "2026-06-02 07:19:39 +0500"
    last_commit: "487e5a32912b97cb33e972d961803d934e18a7d5"
    metadata_available: true
    blocking_if_missing: false
    blocking_if_unreadable: false
    supports_m80_tasks: ["80.2", "80.3", "80.4", "80.5", "80.6", "80.7", "80.8"]
    notes: "Supporting M79 evidence intake."
  - path: "reports/m79-regression-scope.md"
    evidence_group: "supporting"
    required_for_m80_v1: false
    exists: true
    readable: true
    evidence_status: "usable"
    last_modified: "2026-06-02 07:19:39 +0500"
    last_commit: "487e5a32912b97cb33e972d961803d934e18a7d5"
    metadata_available: true
    blocking_if_missing: false
    blocking_if_unreadable: false
    supports_m80_tasks: ["80.2", "80.3", "80.4", "80.5", "80.6", "80.7", "80.8"]
    notes: "Supporting M79 regression scope."
  - path: "reports/m79-governance-validation-proof.md"
    evidence_group: "supporting"
    required_for_m80_v1: false
    exists: true
    readable: true
    evidence_status: "usable"
    last_modified: "2026-06-02 07:19:39 +0500"
    last_commit: "487e5a32912b97cb33e972d961803d934e18a7d5"
    metadata_available: true
    blocking_if_missing: false
    blocking_if_unreadable: false
    supports_m80_tasks: ["80.2", "80.3", "80.4", "80.5", "80.6", "80.7", "80.8"]
    notes: "Supporting M79 governance proof."
  - path: "reports/m79-false-pass-regression-proof.md"
    evidence_group: "supporting"
    required_for_m80_v1: false
    exists: true
    readable: true
    evidence_status: "usable"
    last_modified: "2026-06-02 07:19:39 +0500"
    last_commit: "487e5a32912b97cb33e972d961803d934e18a7d5"
    metadata_available: true
    blocking_if_missing: false
    blocking_if_unreadable: false
    supports_m80_tasks: ["80.2", "80.3", "80.4", "80.5", "80.6", "80.7", "80.8"]
    notes: "Supporting M79 false PASS proof."
```

# Evidence Group Classification
- M76 baseline evidence: usable
- M77 cleanup plan evidence: usable
- M78 cleanup completion evidence: usable
- M78 diff evidence: usable
- M78 validation evidence: usable
- M79 post-cleanup proof evidence: usable
- M79 drift measurement evidence: usable
- M79 baseline comparison evidence: usable
- M79 boundary review evidence: usable
- M80 intake evidence: usable
- no-M81 boundary evidence: usable
- no-approval/no-lifecycle/no-repair evidence: usable
- no-new-baseline-before-M80 evidence: usable

# Required Evidence Availability
- required evidence count: 9
- required evidence exists count: 9
- required evidence usable count: 9
- required evidence missing count: 0
- required evidence unreadable count: 0
- required evidence contradictory count: 0
- required evidence unknown count: 0

# Supporting Evidence Availability
- supporting evidence count: 20
- supporting evidence exists count: 20
- supporting evidence usable count: 20
- supporting evidence missing count: 0
- supporting evidence unreadable count: 0
- supporting evidence contradictory count: 0
- supporting evidence unknown count: 0

# Missing Evidence Review
No required source is missing. No supporting source is missing in a blocking way.

# Unreadable Evidence Review
No required source is unreadable. No supporting source is unreadable.

# Contradictory Evidence Review
No required source is contradictory. No supporting source is contradictory.

# Unknown Evidence Review
No required source is unknown in a blocking way. No supporting source is unknown in a blocking way.

# Blocking Evidence Gaps
None.

# Non-Blocking Evidence Gaps
None.

# Evidence Reliability for M80
The source set is reliable for M80 because all required evidence is present, readable, usable, and non-contradictory. Supporting evidence is also present and usable.

# No-New-Baseline Boundary
- new baseline created by 80.1: false
- baseline updated by 80.1: false
- derived artifacts updated by 80.1: false
- repo-map updated by 80.1: false
- context-index updated by 80.1: false

# No-Repair / No-Cleanup / No-Rollback Boundary
- physical cleanup performed by 80.1: false
- rollback executed by 80.1: false
- repair authorized by 80.1: false
- fix tasks created by 80.1: false
- lifecycle mutation by 80.1: false
- approval claim created by 80.1: false

# M81 Boundary Check
- M81 artifacts created by 80.1: false
- M81 task briefs created by 80.1: false
- M81 started by 80.1: false
- SaaS/UI artifacts created by 80.1: false
- autopilot enabled by 80.1: false

# Blockers
- none

# Warnings
- M80_0_WARNINGS_CARRIED_FORWARD
- M79_WARNINGS_CARRIED_FORWARD
- M78_WARNINGS_CARRIED_FORWARD
- GIT_STATUS_HAS_UNRELATED_CHANGES

# Local Final Status
FINAL_STATUS: M80_CONSOLIDATION_EVIDENCE_INTAKE_COMPLETE_WITH_WARNINGS

# Readiness for 80.2
may_prepare_m80_2: true_with_warnings

# Final Boundary Statement
80.1 collected and classified the evidence only. It did not create a baseline, did not update any derived artifact, did not repair, did not clean, did not roll back, did not start M81, and did not create M81 artifacts or task briefs.

task_id: "80.1"
task_name: "Consolidation Source Evidence Intake"
reports_directory_exists: true
input_file: "reports/m80-m79-completion-intake.md"

m80_0_intake_exists: true
m80_0_intake_readable: true
m80_0_final_status_detected: "FINAL_STATUS: M80_M79_COMPLETION_INTAKE_READY_WITH_WARNINGS"
m80_0_final_status_acceptable: true
m80_0_readiness_detected: "may_prepare_m80_1: true_with_warnings"
m80_0_readiness_acceptable: true

consolidation_evidence_intake_created: true

required_evidence_count: 9
required_evidence_exists_count: 9
required_evidence_missing_count: 0
required_evidence_unreadable_count: 0
required_evidence_usable_count: 9
required_evidence_contradictory_count: 0
required_evidence_unknown_count: 0

supporting_evidence_count: 20
supporting_evidence_exists_count: 20
supporting_evidence_missing_count: 0
supporting_evidence_unreadable_count: 0
supporting_evidence_usable_count: 20
supporting_evidence_contradictory_count: 0
supporting_evidence_unknown_count: 0

usable_evidence_count: 29
missing_evidence_count: 0
unreadable_evidence_count: 0
contradictory_evidence_count: 0
unknown_evidence_count: 0

blocking_evidence_gap_count: 0
non_blocking_evidence_gap_count: 0

m76_baseline_evidence_available: true
m77_cleanup_plan_evidence_available: true
m78_completion_evidence_available: true
m78_diff_evidence_available: true
m78_validation_evidence_available: true
m79_completion_evidence_available: true
m79_drift_evidence_available: true
m79_baseline_comparison_evidence_available: true
m79_boundary_evidence_available: true
m80_intake_evidence_available: true
no_m81_boundary_evidence_available: true
no_approval_lifecycle_repair_evidence_available: true
no_new_baseline_before_m80_evidence_available: true

evidence_reliable_for_m80: true

missing_evidence_treated_as_ok: false
contradictory_evidence_treated_as_ok: false
unknown_evidence_treated_as_ok: false
agent_claim_used_without_source_artifact: false

new_baseline_created_by_80_1: false
baseline_updated_by_80_1: false
derived_artifacts_updated_by_80_1: false
repo_map_updated_by_80_1: false
context_index_updated_by_80_1: false
physical_cleanup_performed_by_80_1: false
rollback_executed_by_80_1: false
repair_authorized_by_80_1: false
fix_tasks_created_by_80_1: false
lifecycle_mutation_by_80_1: false
approval_claim_created_by_80_1: false

m80_artifacts_created_by_80_1_beyond_evidence_intake: false
m80_consolidation_started_by_80_1_beyond_evidence_intake: false
m81_artifacts_created_by_80_1: false
m81_task_briefs_created_by_80_1: false
m81_started_by_80_1: false
saas_or_ui_artifacts_created_by_80_1: false
autopilot_enabled_by_80_1: false

human_summary_consistent_with_machine_fields: true

blocker_codes:
  - "none"
warning_codes:
  - "M80_0_WARNINGS_CARRIED_FORWARD"
  - "M79_WARNINGS_CARRIED_FORWARD"
  - "M78_WARNINGS_CARRIED_FORWARD"
  - "GIT_STATUS_HAS_UNRELATED_CHANGES"
