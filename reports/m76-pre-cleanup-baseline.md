# M76.3 — Pre-Cleanup Baseline

## 1. Purpose
This report establishes the measurable pre-cleanup baseline for the repository, recording initial metrics before any physical cleanup or optimization occurs. These metrics will serve as the baseline comparison for M79/M80.

## 2. 76.2 Candidate Inventory Check
The candidate inventory report was verified.
- `reports/m76-cleanup-candidate-inventory.md` exists and is readable.
- `m76_2_final_status_detected: "M76_CLEANUP_CANDIDATE_INVENTORY_COMPLETE_WITH_WARNINGS"` (Acceptable)
- `m76_2_readiness_detected: "true_with_warnings"` (Acceptable)
- Preconditions passed successfully.

## 3. Baseline Measurement Sources
The baseline measurements are sourced from:
- `reports/m76-cleanup-candidate-inventory.md`
- Git tracked-files list via command line checks (`git ls-files`)

## 4. Baseline Measurement Method
Measurements were performed by querying categories inside the verified candidate inventory (76.2) and performing deterministic command-line regex checks on tracked repository files (e.g., git ls-files tracking of bytecode compiled assets).

## 5. Required Baseline Fields
The 10 required baseline metrics are recorded below.

### 5.1. pre_cleanup_unknown_file_count
- **value**: 0
- **measurement_method**: "counts of category: unknown_file in reports/m76-cleanup-candidate-inventory.md"
- **measurement_source**: "reports/m76-cleanup-candidate-inventory.md"
- **measurement_confidence**: "high"
- **later_improvement_claim_allowed**: true
- **unknown_reason**: "none"

### 5.2. pre_cleanup_duplicate_script_count
- **value**: 23
- **measurement_method**: "counts of category: duplicate_script in reports/m76-cleanup-candidate-inventory.md"
- **measurement_source**: "reports/m76-cleanup-candidate-inventory.md"
- **measurement_confidence**: "high"
- **later_improvement_claim_allowed**: true
- **unknown_reason**: "none"

### 5.3. pre_cleanup_legacy_entrypoint_count
- **value**: 5
- **measurement_method**: "counts of category: legacy_entrypoint in reports/m76-cleanup-candidate-inventory.md"
- **measurement_source**: "reports/m76-cleanup-candidate-inventory.md"
- **measurement_confidence**: "high"
- **later_improvement_claim_allowed**: true
- **unknown_reason**: "none"

### 5.4. pre_cleanup_copy_file_count
- **value**: 1
- **measurement_method**: "counts of category: copy_file in reports/m76-cleanup-candidate-inventory.md"
- **measurement_source**: "reports/m76-cleanup-candidate-inventory.md"
- **measurement_confidence**: "medium"
- **later_improvement_claim_allowed**: true
- **unknown_reason**: "none"

### 5.5. pre_cleanup_tracked_pycache_count
- **value**: 6
- **measurement_method**: "git ls-files | grep -E '(^|/)__pycache__/|\\.pyc$' | wc -l"
- **measurement_source**: "git ls-files"
- **measurement_confidence**: "high"
- **later_improvement_claim_allowed**: true
- **unknown_reason**: "none"

### 5.6. pre_cleanup_stale_report_count
- **value**: 0
- **measurement_method**: "counts of category: stale_report in reports/m76-cleanup-candidate-inventory.md"
- **measurement_source**: "reports/m76-cleanup-candidate-inventory.md"
- **measurement_confidence**: "high"
- **later_improvement_claim_allowed**: true
- **unknown_reason**: "none"

### 5.7. pre_cleanup_bootstrap_doc_count
- **value**: 5
- **measurement_method**: "counts of category: bootstrap_doc in reports/m76-cleanup-candidate-inventory.md"
- **measurement_source**: "reports/m76-cleanup-candidate-inventory.md"
- **measurement_confidence**: "high"
- **later_improvement_claim_allowed**: true
- **unknown_reason**: "none"

### 5.8. pre_cleanup_prompt_surface_estimate
- **value**: unknown
- **measurement_method**: "unknown"
- **measurement_source**: "unknown"
- **measurement_confidence**: "unknown"
- **later_improvement_claim_allowed**: false
- **unknown_reason**: "No deterministic method exists to measure actual agent prompt token surface area in the repository."

### 5.9. pre_cleanup_validation_entrypoint_count
- **value**: 10
- **measurement_method**: "counts of category: validation_wrapper in reports/m76-cleanup-candidate-inventory.md"
- **measurement_source**: "reports/m76-cleanup-candidate-inventory.md"
- **measurement_confidence**: "high"
- **later_improvement_claim_allowed**: true
- **unknown_reason**: "none"

### 5.10. pre_cleanup_adapter_duplication_signal_count
- **value**: unknown
- **measurement_method**: "unknown"
- **measurement_source**: "unknown"
- **measurement_confidence**: "unknown"
- **later_improvement_claim_allowed**: false
- **unknown_reason**: "Semantic duplication signals among adapter files cannot be counted deterministically without subjective analysis."

## 6. Unknown Baseline Values
The fields `pre_cleanup_prompt_surface_estimate` and `pre_cleanup_adapter_duplication_signal_count` are honestly recorded as `unknown` and will block future improvement claims for these specific metrics during validation stages.

## 7. Prompt Surface Estimate
The prompt surface area has no deterministic scanner tool. It is recorded as `unknown` with `prompt_surface_estimate_unknown_allowed: true`.

## 8. Measurement Confidence Summary
- High confidence metrics: 8 fields
- Medium confidence metrics: 1 field (`pre_cleanup_copy_file_count`)
- Unknown confidence metrics: 2 fields (`pre_cleanup_prompt_surface_estimate`, `pre_cleanup_adapter_duplication_signal_count`)

## 9. Later Improvement Claim Boundaries
Any metric marked as `unknown` cannot be used to claim improvement in downstream verification/completion reports.

## 10. Premature Artifact Check
- `downstream_m76_artifacts_exist: false`
- `m77_artifacts_exist: false`
- `m81_artifacts_exist: false`
- `m81_task_briefs_exist: false`
No premature downstream artifacts were found.

## 11. Boundary Check
No files were deleted, moved, renamed, archived, compressed, or consolidated. No risk map or checkpoint plans were created.
- `approval_claim_created: false`
- `lifecycle_mutation_occurred: false`
- `repair_authorized: false`
- `fix_tasks_created: false`
- `physical_cleanup_occurred: false`
- `files_deleted: false`
- `files_moved: false`
- `files_renamed: false`
- `files_archived: false`
- `files_compressed: false`
- `scripts_consolidated: false`
- `docs_compressed: false`
- `risk_map_created: false`
- `human_checkpoint_plan_created: false`
- `scope_lock_created: false`
- `m77_started: false`
- `m81_started: false`

## 12. Blockers
- `blocker_codes:`
  - "none"

## 13. Warnings
- `warning_codes:`
  - "BASELINE_FIELD_UNKNOWN"
  - "PROMPT_SURFACE_ESTIMATE_UNKNOWN"
  - "M76_2_WARNINGS_CARRIED_FORWARD"

## 14. Local Final Status
- `FINAL_STATUS: "M76_PRE_CLEANUP_BASELINE_COMPLETE_WITH_WARNINGS"`

## 15. Readiness for 76.4
- `may_prepare_m76_4: "true_with_warnings"`

## 16. Final Boundary Statement
Task 76.3 only establishes the pre-cleanup baseline metrics and outputs `reports/m76-pre-cleanup-baseline.md`. It does not execute or authorize cleanup, delete, move, or rename files, archive logs, compress bootstrap docs, start 76.4, or start M77/M81 milestones. Human review remains required.

---

### Machine-Readable Metadata
```yaml
task_id: "76.3"
task_name: "Pre-Cleanup Baseline"
reports_directory_exists: true
input_file: "reports/m76-cleanup-candidate-inventory.md"
m76_2_inventory_exists: true
m76_2_inventory_readable: true
m76_2_final_status_detected: "M76_CLEANUP_CANDIDATE_INVENTORY_COMPLETE_WITH_WARNINGS"
m76_2_final_status_acceptable: true
m76_2_readiness_detected: "true_with_warnings"
m76_2_readiness_acceptable: true
baseline_created: true
baseline_field_count_required: 10
baseline_field_count_present: 10
baseline_unknown_field_count: 2
baseline_integer_field_count: 8
pre_cleanup_unknown_file_count: 0
pre_cleanup_duplicate_script_count: 23
pre_cleanup_legacy_entrypoint_count: 5
pre_cleanup_copy_file_count: 1
pre_cleanup_tracked_pycache_count: 6
pre_cleanup_stale_report_count: 0
pre_cleanup_bootstrap_doc_count: 5
pre_cleanup_prompt_surface_estimate: "unknown"
pre_cleanup_validation_entrypoint_count: 10
pre_cleanup_adapter_duplication_signal_count: "unknown"
prompt_surface_estimate_unknown_allowed: true
prompt_surface_later_improvement_claim_allowed: false
downstream_m76_artifacts_exist: false
m77_artifacts_exist: false
m81_artifacts_exist: false
m81_task_briefs_exist: false
approval_claim_created: false
lifecycle_mutation_occurred: false
repair_authorized: false
fix_tasks_created: false
physical_cleanup_occurred: false
files_deleted: false
files_moved: false
files_renamed: false
files_archived: false
files_compressed: false
scripts_consolidated: false
docs_compressed: false
risk_map_created: false
human_checkpoint_plan_created: false
scope_lock_created: false
m77_started: false
m81_started: false
blocker_codes:
  - "none"
warning_codes:
  - "BASELINE_FIELD_UNKNOWN"
  - "PROMPT_SURFACE_ESTIMATE_UNKNOWN"
  - "M76_2_WARNINGS_CARRIED_FORWARD"
```
