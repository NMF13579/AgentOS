# M76.4 — Optimization Risk Map

## 1. Purpose
This report classifies every cleanup and optimization candidate from `reports/m76-cleanup-candidate-inventory.md` into one of the allowed M76 risk classes. Risk classification is not cleanup authorization.

## 2. 76.3 Baseline Check
- `reports/m76-pre-cleanup-baseline.md` exists and is readable.
- `m76_3_final_status_detected: "M76_PRE_CLEANUP_BASELINE_COMPLETE_WITH_WARNINGS"` (Acceptable)
- `m76_3_readiness_detected: "true_with_warnings"` (Acceptable)
- Preconditions passed successfully.

## 3. 76.2 Candidate Inventory Check
- `reports/m76-cleanup-candidate-inventory.md` exists and is readable.
- `candidate_count_total: 58`
- No `candidate_confidence: unknown` detected in 76.2 inventory.
- No `evidence_status: evidence_unknown` or `evidence_contradictory` detected in 76.2 inventory.

## 4. Risk Classification Method
Each candidate was classified based on:
1. The candidate's `category` from the 76.2 inventory.
2. The candidate's `candidate_confidence` (all are high or medium).
3. The candidate's `evidence_status` (all are `evidence_present`).
4. Task-spec default classification rules per category.
5. Hard rules: protected/canonical → PROTECTED_DO_NOT_TOUCH; unknown confidence → UNKNOWN_BLOCKED.
6. Conservative tie-breaking: when uncertain, the stricter class was used.

## 5. Risk Class Summary
| Risk Class | Count |
|---|---|
| SAFE_READONLY | 0 |
| LOW_RISK_CLEANUP | 6 |
| REQUIRES_HUMAN_CHECKPOINT | 43 |
| PROTECTED_DO_NOT_TOUCH | 6 |
| UNKNOWN_BLOCKED | 3 |
| **Total** | **58** |

## 6. Full Risk Map
See machine-readable section below for the complete per-candidate risk map.

## 7. Unknown Blocked Candidates
3 candidates are classified as `UNKNOWN_BLOCKED`:
- `M76-CAND-035` — `HANDOFF 2.md` (copy_file, medium confidence, purpose uncertain)
- `M76-CAND-051` — `reports/m71-script-inventory.json` (derived_navigation_index_artifact, purpose and freshness uncertain)
- `M76-CAND-052` — `repo-map.md` (derived_navigation_index_artifact, regeneration dependency uncertain)

## 8. Protected/Canonical Do-Not-Touch Candidates
6 candidates are classified as `PROTECTED_DO_NOT_TOUCH`:
- `M76-CAND-053` — `ROUTES-REGISTRY.md`
- `M76-CAND-054` — `core-rules/MAIN.md`
- `M76-CAND-055` — `state/MAIN.md`
- `M76-CAND-056` — `workflow/MAIN.md`
- `M76-CAND-057` — `quality/MAIN.md`
- `M76-CAND-058` — `security/MAIN.md`

## 9. Human Checkpoint Required Candidates
43 candidates require a future human checkpoint before any action:
- 23 duplicate scripts (`scripts/*  3.py`) — macOS-created copies of validation/test scripts; potential validation behavior overlap.
- 5 legacy entrypoint scripts — user-facing and potentially CI-facing behavior.
- 5 bootstrap documents — governance-critical startup files.
- 10 validation wrapper scripts — active validation authority files.

## 10. Low-Risk Cleanup Candidates
6 candidates are classified as `LOW_RISK_CLEANUP`:
- All 6 tracked bytecode caches under `scripts/__pycache__/` — deterministic git tracking evidence, no runtime behavior impact.

## 11. Safe Read-Only Candidates
0 candidates qualify as `SAFE_READONLY`.

## 12. Cleanup Authorization Boundary
- 76.4 does not authorize cleanup.
- 76.4 does not approve deletion.
- 76.4 does not approve archiving.
- 76.4 does not approve script consolidation.
- 76.4 does not approve bootstrap compression.
- 76.4 does not start M77.
- Human review remains required.

## 13. Premature Artifact Check
- `downstream_m76_artifacts_exist: false`
- `m77_artifacts_exist: false`
- `m81_artifacts_exist: false`
- `m81_task_briefs_exist: false`

## 14. Boundary Check
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
- `human_checkpoint_plan_created: false`
- `scope_lock_created: false`
- `m77_started: false`
- `m81_started: false`

## 15. Blockers
- `blocker_codes:`
  - "none"

## 16. Warnings
- `warning_codes:`
  - "UNKNOWN_BLOCKED_CANDIDATES_PRESENT"
  - "REQUIRES_HUMAN_CHECKPOINT_CANDIDATES_PRESENT"
  - "PROTECTED_DO_NOT_TOUCH_CANDIDATES_PRESENT"
  - "MISSING_EVIDENCE_CANDIDATES_PRESENT"
  - "M76_3_WARNINGS_CARRIED_FORWARD"

## 17. Local Final Status
- `FINAL_STATUS: "M76_OPTIMIZATION_RISK_MAP_COMPLETE_WITH_WARNINGS"`

## 18. Readiness for 76.5
- `may_prepare_m76_5: "true_with_warnings"`

## 19. Final Boundary Statement
Task 76.4 only classifies candidate risk and outputs `reports/m76-optimization-risk-map.md`. It does not execute or authorize cleanup, create cleanup plan, create human checkpoint plan, create scope lock, start 76.5, or start M77/M81 milestones. Human review remains required.

---

### Machine-Readable Metadata
```yaml
task_id: "76.4"
task_name: "Optimization Risk Map"
reports_directory_exists: true
input_file_candidate_inventory: "reports/m76-cleanup-candidate-inventory.md"
input_file_baseline: "reports/m76-pre-cleanup-baseline.md"
m76_2_inventory_exists: true
m76_2_inventory_readable: true
m76_3_baseline_exists: true
m76_3_baseline_readable: true
m76_3_final_status_detected: "M76_PRE_CLEANUP_BASELINE_COMPLETE_WITH_WARNINGS"
m76_3_final_status_acceptable: true
m76_3_readiness_detected: "true_with_warnings"
m76_3_readiness_acceptable: true
risk_map_created: true
candidate_count_total: 58
risk_map_item_count: 58
safe_readonly_count: 0
low_risk_cleanup_count: 6
requires_human_checkpoint_count: 43
protected_do_not_touch_count: 6
unknown_blocked_count: 3
candidate_confidence_unknown_count: 0
evidence_unknown_count: 0
evidence_contradictory_count: 0
cleanup_allowed_without_checkpoint_count: 0
protected_or_canonical_count: 6
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
human_checkpoint_plan_created: false
scope_lock_created: false
m77_started: false
m81_started: false
blocker_codes:
  - "none"
warning_codes:
  - "UNKNOWN_BLOCKED_CANDIDATES_PRESENT"
  - "REQUIRES_HUMAN_CHECKPOINT_CANDIDATES_PRESENT"
  - "PROTECTED_DO_NOT_TOUCH_CANDIDATES_PRESENT"
  - "MISSING_EVIDENCE_CANDIDATES_PRESENT"
  - "M76_3_WARNINGS_CARRIED_FORWARD"

FINAL_STATUS: "M76_OPTIMIZATION_RISK_MAP_COMPLETE_WITH_WARNINGS"
may_prepare_m76_5: "true_with_warnings"

risk_map:
  - candidate_id: "M76-CAND-001"
    path: "scripts/__pycache__/agent-complete.cpython-314.pyc"
    category: "tracked_pycache"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "LOW_RISK_CLEANUP"
    risk_reason: "Tracked bytecode cache with deterministic git-ls-files evidence. No runtime behavior impact."
    human_checkpoint_required: false
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: true
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "pycache file tracked in git; safe to plan for untrack+gitignore in future cleanup."

  - candidate_id: "M76-CAND-002"
    path: "scripts/__pycache__/agent-fail.cpython-314.pyc"
    category: "tracked_pycache"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "LOW_RISK_CLEANUP"
    risk_reason: "Tracked bytecode cache with deterministic git-ls-files evidence. No runtime behavior impact."
    human_checkpoint_required: false
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: true
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "pycache file tracked in git; safe to plan for untrack+gitignore in future cleanup."

  - candidate_id: "M76-CAND-003"
    path: "scripts/__pycache__/agent-next.cpython-314.pyc"
    category: "tracked_pycache"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "LOW_RISK_CLEANUP"
    risk_reason: "Tracked bytecode cache with deterministic git-ls-files evidence. No runtime behavior impact."
    human_checkpoint_required: false
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: true
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "pycache file tracked in git; safe to plan for untrack+gitignore in future cleanup."

  - candidate_id: "M76-CAND-004"
    path: "scripts/__pycache__/generate-task-contract.cpython-314.pyc"
    category: "tracked_pycache"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "LOW_RISK_CLEANUP"
    risk_reason: "Tracked bytecode cache with deterministic git-ls-files evidence. No runtime behavior impact."
    human_checkpoint_required: false
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: true
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "pycache file tracked in git; safe to plan for untrack+gitignore in future cleanup."

  - candidate_id: "M76-CAND-005"
    path: "scripts/__pycache__/validate-task.cpython-314.pyc"
    category: "tracked_pycache"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "LOW_RISK_CLEANUP"
    risk_reason: "Tracked bytecode cache with deterministic git-ls-files evidence. No runtime behavior impact."
    human_checkpoint_required: false
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: true
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "pycache file tracked in git; safe to plan for untrack+gitignore in future cleanup."

  - candidate_id: "M76-CAND-006"
    path: "scripts/__pycache__/validate-verification.cpython-314.pyc"
    category: "tracked_pycache"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "LOW_RISK_CLEANUP"
    risk_reason: "Tracked bytecode cache with deterministic git-ls-files evidence. No runtime behavior impact."
    human_checkpoint_required: false
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: true
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "pycache file tracked in git; safe to plan for untrack+gitignore in future cleanup."

  - candidate_id: "M76-CAND-007"
    path: "scripts/audit-m27 3.py"
    category: "duplicate_script"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "macOS Finder copy of a validation/audit script; deletion could affect any workflow referencing this path by name."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Duplicate of scripts/audit-m27.py. Requires confirmation that no workflow or CI references this path."

  - candidate_id: "M76-CAND-008"
    path: "scripts/audit-m27-level1 3.py"
    category: "duplicate_script"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "macOS Finder copy of a validation/audit script; deletion could affect any workflow referencing this path by name."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Duplicate of scripts/audit-m27-level1.py. Requires confirmation that no workflow references this path."

  - candidate_id: "M76-CAND-009"
    path: "scripts/audit-metadata-consistency 3.py"
    category: "duplicate_script"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "macOS Finder copy of a validation/audit script; deletion could affect any workflow referencing this path by name."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Duplicate of scripts/audit-metadata-consistency.py."

  - candidate_id: "M76-CAND-010"
    path: "scripts/audit-pre-merge-corridor 3.py"
    category: "duplicate_script"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "macOS Finder copy of a validation/audit script; deletion could affect any workflow referencing this path by name."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Duplicate of scripts/audit-pre-merge-corridor.py."

  - candidate_id: "M76-CAND-011"
    path: "scripts/audit-validation-integration 3.py"
    category: "duplicate_script"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "macOS Finder copy of a validation/audit script; deletion could affect any workflow referencing this path by name."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Duplicate of scripts/audit-validation-integration.py."

  - candidate_id: "M76-CAND-012"
    path: "scripts/build-index 3.py"
    category: "duplicate_script"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "macOS Finder copy of an index-building script; deletion could affect any workflow referencing this path by name."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Duplicate of scripts/build-index.py."

  - candidate_id: "M76-CAND-013"
    path: "scripts/check-commit-push-preconditions 3.py"
    category: "duplicate_script"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "macOS Finder copy of a validation script with CI-facing behavior; deletion may affect commit validation chains."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Duplicate of scripts/check-commit-push-preconditions.py."

  - candidate_id: "M76-CAND-014"
    path: "scripts/check-github-platform-enforcement 3.py"
    category: "duplicate_script"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "macOS Finder copy of a GitHub platform enforcement script; CI-facing behavior overlap."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Duplicate of scripts/check-github-platform-enforcement.py."

  - candidate_id: "M76-CAND-015"
    path: "scripts/check-pre-merge-scope 3.py"
    category: "duplicate_script"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "macOS Finder copy of a pre-merge scope checker; CI/pre-merge validation overlap."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Duplicate of scripts/check-pre-merge-scope.py."

  - candidate_id: "M76-CAND-016"
    path: "scripts/check-scope-compliance 3.py"
    category: "duplicate_script"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "macOS Finder copy of the scope compliance checker; overlap with agentos-validate dispatcher."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Duplicate of scripts/check-scope-compliance.py."

  - candidate_id: "M76-CAND-017"
    path: "scripts/test-ci-advisory-config 3.py"
    category: "duplicate_script"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "macOS Finder copy of a CI advisory test script; CI-facing behavior overlap."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Duplicate of scripts/test-ci-advisory-config.py."

  - candidate_id: "M76-CAND-018"
    path: "scripts/test-commit-push-preconditions-fixtures 3.py"
    category: "duplicate_script"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "macOS Finder copy of a commit/push fixture test; may be referenced in validation chains."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Duplicate of scripts/test-commit-push-preconditions-fixtures.py."

  - candidate_id: "M76-CAND-019"
    path: "scripts/test-enforcement-fixtures 3.py"
    category: "duplicate_script"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "macOS Finder copy of an enforcement fixture test; may be referenced in validation chains."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Duplicate of scripts/test-enforcement-fixtures.py."

  - candidate_id: "M76-CAND-020"
    path: "scripts/test-m22-guardrails 3.py"
    category: "duplicate_script"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "macOS Finder copy of a guardrail test script; may be referenced in validation chains."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Duplicate of scripts/test-m22-guardrails.py."

  - candidate_id: "M76-CAND-021"
    path: "scripts/test-m27-level1-fixtures 3.py"
    category: "duplicate_script"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "macOS Finder copy of a level-1 fixture test; may be referenced in validation chains."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Duplicate of scripts/test-m27-level1-fixtures.py."

  - candidate_id: "M76-CAND-022"
    path: "scripts/test-pre-merge-corridor-fixtures 3.py"
    category: "duplicate_script"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "macOS Finder copy of a pre-merge corridor fixture test; CI overlap potential."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Duplicate of scripts/test-pre-merge-corridor-fixtures.py."

  - candidate_id: "M76-CAND-023"
    path: "scripts/test-pre-merge-scope-fixtures 3.py"
    category: "duplicate_script"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "macOS Finder copy of a pre-merge scope fixture test; CI overlap potential."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Duplicate of scripts/test-pre-merge-scope-fixtures.py."

  - candidate_id: "M76-CAND-024"
    path: "scripts/test-scope-compliance-fixtures 3.py"
    category: "duplicate_script"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "macOS Finder copy of a scope compliance fixture test; dispatcher overlap."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Duplicate of scripts/test-scope-compliance-fixtures.py."

  - candidate_id: "M76-CAND-025"
    path: "scripts/validate-boundary-claims 3.py"
    category: "duplicate_script"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "macOS Finder copy of a boundary claim validator; validation authority overlap."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Duplicate of scripts/validate-boundary-claims.py."

  - candidate_id: "M76-CAND-026"
    path: "scripts/validate-frontmatter 3.py"
    category: "duplicate_script"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "macOS Finder copy of a frontmatter validator; validation authority overlap."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Duplicate of scripts/validate-frontmatter.py."

  - candidate_id: "M76-CAND-027"
    path: "scripts/validate-index 3.py"
    category: "duplicate_script"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "macOS Finder copy of an index validator; validation authority overlap."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Duplicate of scripts/validate-index.py."

  - candidate_id: "M76-CAND-028"
    path: "scripts/validate-required-sections 3.py"
    category: "duplicate_script"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "macOS Finder copy of a required sections validator; validation authority overlap."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Duplicate of scripts/validate-required-sections.py."

  - candidate_id: "M76-CAND-029"
    path: "scripts/validate-status-semantics 3.py"
    category: "duplicate_script"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "macOS Finder copy of a status semantics validator; validation authority overlap."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Duplicate of scripts/validate-status-semantics.py."

  - candidate_id: "M76-CAND-030"
    path: "scripts/agent-complete.py"
    category: "legacy_entrypoint"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "Legacy entrypoint script potentially used in CI or human-facing workflows; removal requires confirmation."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Listed as legacy entrypoint in 76.2 inventory."

  - candidate_id: "M76-CAND-031"
    path: "scripts/agent-fail.py"
    category: "legacy_entrypoint"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "Legacy entrypoint script potentially used in CI or human-facing workflows; removal requires confirmation."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Listed as legacy entrypoint in 76.2 inventory."

  - candidate_id: "M76-CAND-032"
    path: "scripts/agent-next.py"
    category: "legacy_entrypoint"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "Legacy entrypoint script potentially used in CI or human-facing workflows; removal requires confirmation."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Listed as legacy entrypoint in 76.2 inventory."

  - candidate_id: "M76-CAND-033"
    path: "scripts/agentos.py"
    category: "legacy_entrypoint"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "Legacy entrypoint script potentially user-facing or CI-facing; removal requires confirmation."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Listed as legacy entrypoint in 76.2 inventory."

  - candidate_id: "M76-CAND-034"
    path: "scripts/run-active-task.py"
    category: "legacy_entrypoint"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "Legacy entrypoint script potentially user-facing or CI-facing; removal requires confirmation."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Listed as legacy entrypoint in 76.2 inventory."

  - candidate_id: "M76-CAND-035"
    path: "HANDOFF 2.md"
    category: "copy_file"
    candidate_confidence: "medium"
    evidence_status: "evidence_present"
    risk_class: "UNKNOWN_BLOCKED"
    risk_reason: "Medium confidence copy file with uncertain purpose; no deterministic evidence of safe removal."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Duplicate or legacy handoff file. Purpose and content relationship to HANDOFF.md unknown without inspection."

  - candidate_id: "M76-CAND-036"
    path: "llms.txt"
    category: "bootstrap_doc"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "Bootstrap source-of-truth gateway document; any compression or modification requires explicit human checkpoint."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Primary agent bootstrap entrypoint. Cannot be modified or compressed without human checkpoint."

  - candidate_id: "M76-CAND-037"
    path: "AGENTS.md"
    category: "bootstrap_doc"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "Agent adapter document; any compression or modification requires explicit human checkpoint."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Agent-specific bootstrap adapter. Cannot be modified or compressed without human checkpoint."

  - candidate_id: "M76-CAND-038"
    path: "CLAUDE.md"
    category: "bootstrap_doc"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "Claude-specific bootstrap adapter; any modification requires explicit human checkpoint."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Agent-specific bootstrap adapter. Cannot be modified or compressed without human checkpoint."

  - candidate_id: "M76-CAND-039"
    path: "GEMINI.md"
    category: "bootstrap_doc"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "Gemini-specific bootstrap adapter; any modification requires explicit human checkpoint."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Agent-specific bootstrap adapter. Cannot be modified or compressed without human checkpoint."

  - candidate_id: "M76-CAND-040"
    path: "README.md"
    category: "bootstrap_doc"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "General project readme; any modification requires explicit human checkpoint."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Project readme. Cannot be modified or compressed without human checkpoint."

  - candidate_id: "M76-CAND-041"
    path: "scripts/agentos-validate.py"
    category: "validation_wrapper"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "Active validation authority entrypoint; removal or modification requires human checkpoint."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Canonical validation dispatcher. Cannot be touched without human checkpoint."

  - candidate_id: "M76-CAND-042"
    path: "scripts/check-dangerous-commands.py"
    category: "validation_wrapper"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "Dangerous command validator; removal requires human checkpoint."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Active safety validator. Cannot be touched without human checkpoint."

  - candidate_id: "M76-CAND-043"
    path: "scripts/check-execution-authorization.py"
    category: "validation_wrapper"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "Execution authorization validator; removal requires human checkpoint."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Active safety validator. Cannot be touched without human checkpoint."

  - candidate_id: "M76-CAND-044"
    path: "scripts/check-execution-readiness.py"
    category: "validation_wrapper"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "Execution readiness validator; removal requires human checkpoint."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Active safety validator. Cannot be touched without human checkpoint."

  - candidate_id: "M76-CAND-045"
    path: "scripts/check-human-approval.py"
    category: "validation_wrapper"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "Human approval validator; removal requires human checkpoint."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Active safety validator. Cannot be touched without human checkpoint."

  - candidate_id: "M76-CAND-046"
    path: "scripts/check-lifecycle-mutation.py"
    category: "validation_wrapper"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "Lifecycle mutation validator; removal requires human checkpoint."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Active safety validator. Cannot be touched without human checkpoint."

  - candidate_id: "M76-CAND-047"
    path: "scripts/check-readiness-assertions.py"
    category: "validation_wrapper"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "Readiness assertions validator; removal requires human checkpoint."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Active safety validator. Cannot be touched without human checkpoint."

  - candidate_id: "M76-CAND-048"
    path: "scripts/check-validator-authority-boundary.py"
    category: "validation_wrapper"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "Validator authority boundary checker; removal requires human checkpoint."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Active safety validator. Cannot be touched without human checkpoint."

  - candidate_id: "M76-CAND-049"
    path: "scripts/validate-lifecycle-apply.py"
    category: "validation_wrapper"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "Lifecycle apply validator; removal requires human checkpoint."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Active safety validator. Cannot be touched without human checkpoint."

  - candidate_id: "M76-CAND-050"
    path: "scripts/validate-task.py"
    category: "validation_wrapper"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "REQUIRES_HUMAN_CHECKPOINT"
    risk_reason: "Task contract YAML schema validator; removal requires human checkpoint."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Active safety validator. Cannot be touched without human checkpoint."

  - candidate_id: "M76-CAND-051"
    path: "reports/m71-script-inventory.json"
    category: "derived_navigation_index_artifact"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "UNKNOWN_BLOCKED"
    risk_reason: "Derived index artifact; regeneration dependency and downstream consumers unknown without deeper inspection."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Script inventory JSON from M71. Whether it is actively consumed by other scripts or tools is unknown."

  - candidate_id: "M76-CAND-052"
    path: "repo-map.md"
    category: "derived_navigation_index_artifact"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "UNKNOWN_BLOCKED"
    risk_reason: "Derived repository layout map; consumer scripts and regeneration dependency unknown without deeper inspection."
    human_checkpoint_required: true
    protected_or_canonical: false
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Repo map markdown. Whether actively consumed by other tools or just informational is unknown."

  - candidate_id: "M76-CAND-053"
    path: "ROUTES-REGISTRY.md"
    category: "DO_NOT_TOUCH"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "PROTECTED_DO_NOT_TOUCH"
    risk_reason: "Protected canonical document — source of module ownership and routing authority."
    human_checkpoint_required: true
    protected_or_canonical: true
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Protected/canonical — cannot be modified without human checkpoint."

  - candidate_id: "M76-CAND-054"
    path: "core-rules/MAIN.md"
    category: "DO_NOT_TOUCH"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "PROTECTED_DO_NOT_TOUCH"
    risk_reason: "Protected canonical document — governance priority and authority model source of truth."
    human_checkpoint_required: true
    protected_or_canonical: true
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Protected/canonical — cannot be modified without human checkpoint."

  - candidate_id: "M76-CAND-055"
    path: "state/MAIN.md"
    category: "DO_NOT_TOUCH"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "PROTECTED_DO_NOT_TOUCH"
    risk_reason: "Protected canonical document — current state and recovery source of truth."
    human_checkpoint_required: true
    protected_or_canonical: true
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Protected/canonical — cannot be modified without human checkpoint."

  - candidate_id: "M76-CAND-056"
    path: "workflow/MAIN.md"
    category: "DO_NOT_TOUCH"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "PROTECTED_DO_NOT_TOUCH"
    risk_reason: "Protected canonical document — execution boundaries and approval gate source of truth."
    human_checkpoint_required: true
    protected_or_canonical: true
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Protected/canonical — cannot be modified without human checkpoint."

  - candidate_id: "M76-CAND-057"
    path: "quality/MAIN.md"
    category: "DO_NOT_TOUCH"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "PROTECTED_DO_NOT_TOUCH"
    risk_reason: "Protected canonical document — validation and verification strategy source of truth."
    human_checkpoint_required: true
    protected_or_canonical: true
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Protected/canonical — cannot be modified without human checkpoint."

  - candidate_id: "M76-CAND-058"
    path: "security/MAIN.md"
    category: "DO_NOT_TOUCH"
    candidate_confidence: "high"
    evidence_status: "evidence_present"
    risk_class: "PROTECTED_DO_NOT_TOUCH"
    risk_reason: "Protected canonical document — security boundaries and compliance source of truth."
    human_checkpoint_required: true
    protected_or_canonical: true
    cleanup_allowed_in_m78_without_checkpoint: false
    planned_checkpoint_lowers_risk: false
    cleanup_authorized_by_76_4: false
    notes: "Protected/canonical — cannot be modified without human checkpoint."
```
