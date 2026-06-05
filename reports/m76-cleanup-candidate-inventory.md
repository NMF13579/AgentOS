# M76.2 — Cleanup Candidate Inventory

## 1. Purpose
This report inventories the repository's potential cleanup and optimization candidates, capturing the factual evidence for each file/group without performing or authorizing any physical cleanup actions.

## 2. 76.1 Intake Check
The precondition optimization facts report was checked.
- `reports/m76-optimization-intake.md` exists and is readable.
- `m76_1_final_status_detected: "M76_OPTIMIZATION_INTAKE_COMPLETE_WITH_WARNINGS"` (Acceptable)
- `m76_1_readiness_detected: "true_with_warnings"` (Acceptable)
- `source_facts_reliable_detected: true` (Acceptable)
- Preconditions passed successfully.

## 3. Source Evidence Used
The inventory was compiled using read-only checks on:
- `reports/m76-optimization-intake.md`
- `reports/m75-drift-repo-hygiene-facts-review.md`
- Git tracked-file listings (`git ls-files`)

## 4. Candidate Discovery Method
Discovery was conducted using read-only Git commands and directory layout searches to detect copy scripts, compiled bytecode files, outdated wrappers, and other legacy files.

## 5. Candidate Category Summary
A total of 58 cleanup and optimization candidates were discovered:
- `obsolete_file_candidate_count: 0`
- `unknown_file_candidate_count: 0`
- `copy_file_candidate_count: 1`
- `tracked_pycache_candidate_count: 6`
- `duplicate_script_candidate_count: 23`
- `legacy_entrypoint_candidate_count: 5`
- `stale_report_candidate_count: 0`
- `bootstrap_doc_candidate_count: 5`
- `adapter_file_candidate_count: 0`
- `validation_wrapper_candidate_count: 10`
- `generated_cache_artifact_candidate_count: 0`
- `protected_canonical_artifact_candidate_count: 6`
- `derived_navigation_index_artifact_candidate_count: 2`
- `other_candidate_count: 0`
- `candidate_count_total: 58`

Confidence ratings:
- `candidate_confidence_high_count: 57`
- `candidate_confidence_medium_count: 1`
- `candidate_confidence_low_count: 0`
- `candidate_confidence_unknown_count: 0`

## 6. Cleanup Candidate Inventory
The discovered candidates are listed in detail in the machine-readable section. No candidate is approved for deletion, move, or rename during M76.

## 7. Unknown Candidate Summary
No unknown files were registered in this inventory.

## 8. Protected/Canonical Candidate Summary
A total of 6 protected canonical documents were mapped to keep them active and strictly prevent any modification during future cleanup passes (DO_NOT_TOUCH).

## 9. Duplicate/Copy Candidate Summary
- 23 duplicate script files ending in ` 3.py` are mapped as duplicate candidates.
- `HANDOFF 2.md` is mapped as copy_file candidate.

## 10. Tracked Cache Artifact Summary
6 tracked `.pyc` files exist under `scripts/__pycache__/` and are registered as bytecode cache candidates.

## 11. Legacy Entrypoint Candidate Summary
5 legacy scripts (e.g., `scripts/agentos.py`, `scripts/agent-next.py`) are registered for future review and legacy marking.

## 12. Bootstrap/Adapter Candidate Summary
5 bootstrap documents (including `llms.txt`, `README.md`) are mapped to preserve context boundaries.

## 13. Validation Wrapper Candidate Summary
10 validation wrappers (such as `scripts/agentos-validate.py`) are mapped as active validation authority files.

## 14. Generated/Derived Artifact Candidate Summary
2 derived index files are mapped.

## 15. Boundary Check
No files were physically deleted, moved, renamed, archived, compressed, or consolidated.
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
- `pre_cleanup_baseline_created: false`
- `risk_map_created: false`
- `human_checkpoint_plan_created: false`
- `scope_lock_created: false`
- `m77_started: false`
- `m81_started: false`

## 16. Blockers
- `blocker_codes:`
  - "none"

## 17. Warnings
- `warning_codes:`
  - "PROTECTED_CANONICAL_CANDIDATES_PRESENT"
  - "BOOTSTRAP_CANDIDATES_PRESENT"
  - "VALIDATION_WRAPPER_CANDIDATES_PRESENT"
  - "M76_1_WARNINGS_CARRIED_FORWARD"

## 18. Local Final Status
- `FINAL_STATUS: "M76_CLEANUP_CANDIDATE_INVENTORY_COMPLETE_WITH_WARNINGS"`

## 19. Readiness for 76.3
- `may_prepare_m76_3: "true_with_warnings"`

## 20. Final Boundary Statement
Task 76.2 only compiles the cleanup candidate inventory report. It does not perform cleanup, approve cleanup, create baselines, risk maps, or scope locks. It does not start 76.3, M77, or M81. Human review remains required.

---

### Machine-Readable Metadata
```yaml
FINAL_STATUS: "M76_CLEANUP_CANDIDATE_INVENTORY_COMPLETE_WITH_WARNINGS"
may_prepare_m76_3: "true_with_warnings"
task_id: "76.2"
task_name: "Cleanup Candidate Inventory"
reports_directory_exists: true
input_file: "reports/m76-optimization-intake.md"
m76_1_intake_exists: true
m76_1_intake_readable: true
m76_1_final_status_detected: "M76_OPTIMIZATION_INTAKE_COMPLETE_WITH_WARNINGS"
m76_1_final_status_acceptable: true
m76_1_readiness_detected: "true_with_warnings"
m76_1_readiness_acceptable: true
source_facts_reliable_detected: true
candidate_inventory_created: true
candidate_count_total: 58
obsolete_file_candidate_count: 0
unknown_file_candidate_count: 0
copy_file_candidate_count: 1
tracked_pycache_candidate_count: 6
duplicate_script_candidate_count: 23
legacy_point_candidate_count: 5
stale_report_candidate_count: 0
bootstrap_doc_candidate_count: 5
adapter_file_candidate_count: 0
validation_wrapper_candidate_count: 10
generated_cache_artifact_candidate_count: 0
protected_canonical_artifact_candidate_count: 6
derived_navigation_index_artifact_candidate_count: 2
other_candidate_count: 0
candidate_confidence_high_count: 57
candidate_confidence_medium_count: 1
candidate_confidence_low_count: 0
candidate_confidence_unknown_count: 0
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
pre_cleanup_baseline_created: false
risk_map_created: false
human_checkpoint_plan_created: false
scope_lock_created: false
m77_started: false
m81_started: false
blocker_codes:
  - "none"
warning_codes:
  - "PROTECTED_CANONICAL_CANDIDATES_PRESENT"
  - "BOOTSTRAP_CANDIDATES_PRESENT"
  - "VALIDATION_WRAPPER_CANDIDATES_PRESENT"
  - "M76_1_WARNINGS_CARRIED_FORWARD"

cleanup_candidates:
  - candidate_id: "M76-CAND-001"
    path: "scripts/__pycache__/agent-complete.cpython-314.pyc"
    category: "tracked_pycache"
    source_evidence: "reports/m75-drift-repo-hygiene-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "delete_candidate"
    notes: "Tracked bytecode cache file under scripts/__pycache__."
  - candidate_id: "M76-CAND-002"
    path: "scripts/__pycache__/agent-fail.cpython-314.pyc"
    category: "tracked_pycache"
    source_evidence: "reports/m75-drift-repo-hygiene-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "delete_candidate"
    notes: "Tracked bytecode cache file under scripts/__pycache__."
  - candidate_id: "M76-CAND-003"
    path: "scripts/__pycache__/agent-next.cpython-314.pyc"
    category: "tracked_pycache"
    source_evidence: "reports/m75-drift-repo-hygiene-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "delete_candidate"
    notes: "Tracked bytecode cache file under scripts/__pycache__."
  - candidate_id: "M76-CAND-004"
    path: "scripts/__pycache__/generate-task-contract.cpython-314.pyc"
    category: "tracked_pycache"
    source_evidence: "reports/m75-drift-repo-hygiene-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "delete_candidate"
    notes: "Tracked bytecode cache file under scripts/__pycache__."
  - candidate_id: "M76-CAND-005"
    path: "scripts/__pycache__/validate-task.cpython-314.pyc"
    category: "tracked_pycache"
    source_evidence: "reports/m75-drift-repo-hygiene-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "delete_candidate"
    notes: "Tracked bytecode cache file under scripts/__pycache__."
  - candidate_id: "M76-CAND-006"
    path: "scripts/__pycache__/validate-verification.cpython-314.pyc"
    category: "tracked_pycache"
    source_evidence: "reports/m75-drift-repo-hygiene-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "delete_candidate"
    notes: "Tracked bytecode cache file under scripts/__pycache__."
  - candidate_id: "M76-CAND-007"
    path: "scripts/audit-m27 3.py"
    category: "duplicate_script"
    source_evidence: "reports/m75-drift-repo-hygiene-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "delete_candidate"
    notes: "Duplicate script ending with 3.py"
  - candidate_id: "M76-CAND-008"
    path: "scripts/audit-m27-level1 3.py"
    category: "duplicate_script"
    source_evidence: "reports/m75-drift-repo-hygiene-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "delete_candidate"
    notes: "Duplicate script ending with 3.py"
  - candidate_id: "M76-CAND-009"
    path: "scripts/audit-metadata-consistency 3.py"
    category: "duplicate_script"
    source_evidence: "reports/m75-drift-repo-hygiene-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "delete_candidate"
    notes: "Duplicate script ending with 3.py"
  - candidate_id: "M76-CAND-010"
    path: "scripts/audit-pre-merge-corridor 3.py"
    category: "duplicate_script"
    source_evidence: "reports/m75-drift-repo-hygiene-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "delete_candidate"
    notes: "Duplicate script ending with 3.py"
  - candidate_id: "M76-CAND-011"
    path: "scripts/audit-validation-integration 3.py"
    category: "duplicate_script"
    source_evidence: "reports/m75-drift-repo-hygiene-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "delete_candidate"
    notes: "Duplicate script ending with 3.py"
  - candidate_id: "M76-CAND-012"
    path: "scripts/build-index 3.py"
    category: "duplicate_script"
    source_evidence: "reports/m75-drift-repo-hygiene-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "delete_candidate"
    notes: "Duplicate script ending with 3.py"
  - candidate_id: "M76-CAND-013"
    path: "scripts/check-commit-push-preconditions 3.py"
    category: "duplicate_script"
    source_evidence: "reports/m75-drift-repo-hygiene-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "delete_candidate"
    notes: "Duplicate script ending with 3.py"
  - candidate_id: "M76-CAND-014"
    path: "scripts/check-github-platform-enforcement 3.py"
    category: "duplicate_script"
    source_evidence: "reports/m75-drift-repo-hygiene-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "delete_candidate"
    notes: "Duplicate script ending with 3.py"
  - candidate_id: "M76-CAND-015"
    path: "scripts/check-pre-merge-scope 3.py"
    category: "duplicate_script"
    source_evidence: "reports/m75-drift-repo-hygiene-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "delete_candidate"
    notes: "Duplicate script ending with 3.py"
  - candidate_id: "M76-CAND-016"
    path: "scripts/check-scope-compliance 3.py"
    category: "duplicate_script"
    source_evidence: "reports/m75-drift-repo-hygiene-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "delete_candidate"
    notes: "Duplicate script ending with 3.py"
  - candidate_id: "M76-CAND-017"
    path: "scripts/test-ci-advisory-config 3.py"
    category: "duplicate_script"
    source_evidence: "reports/m75-drift-repo-hygiene-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "delete_candidate"
    notes: "Duplicate script ending with 3.py"
  - candidate_id: "M76-CAND-018"
    path: "scripts/test-commit-push-preconditions-fixtures 3.py"
    category: "duplicate_script"
    source_evidence: "reports/m75-drift-repo-hygiene-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "delete_candidate"
    notes: "Duplicate script ending with 3.py"
  - candidate_id: "M76-CAND-019"
    path: "scripts/test-enforcement-fixtures 3.py"
    category: "duplicate_script"
    source_evidence: "reports/m75-drift-repo-hygiene-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "delete_candidate"
    notes: "Duplicate script ending with 3.py"
  - candidate_id: "M76-CAND-020"
    path: "scripts/test-m22-guardrails 3.py"
    category: "duplicate_script"
    source_evidence: "reports/m75-drift-repo-hygiene-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "delete_candidate"
    notes: "Duplicate script ending with 3.py"
  - candidate_id: "M76-CAND-021"
    path: "scripts/test-m27-level1-fixtures 3.py"
    category: "duplicate_script"
    source_evidence: "reports/m75-drift-repo-hygiene-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "delete_candidate"
    notes: "Duplicate script ending with 3.py"
  - candidate_id: "M76-CAND-022"
    path: "scripts/test-pre-merge-corridor-fixtures 3.py"
    category: "duplicate_script"
    source_evidence: "reports/m75-drift-repo-hygiene-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "delete_candidate"
    notes: "Duplicate script ending with 3.py"
  - candidate_id: "M76-CAND-023"
    path: "scripts/test-pre-merge-scope-fixtures 3.py"
    category: "duplicate_script"
    source_evidence: "reports/m75-drift-repo-hygiene-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "delete_candidate"
    notes: "Duplicate script ending with 3.py"
  - candidate_id: "M76-CAND-024"
    path: "scripts/test-scope-compliance-fixtures 3.py"
    category: "duplicate_script"
    source_evidence: "reports/m75-drift-repo-hygiene-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "delete_candidate"
    notes: "Duplicate script ending with 3.py"
  - candidate_id: "M76-CAND-025"
    path: "scripts/validate-boundary-claims 3.py"
    category: "duplicate_script"
    source_evidence: "reports/m75-drift-repo-hygiene-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "delete_candidate"
    notes: "Duplicate script ending with 3.py"
  - candidate_id: "M76-CAND-026"
    path: "scripts/validate-frontmatter 3.py"
    category: "duplicate_script"
    source_evidence: "reports/m75-drift-repo-hygiene-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "delete_candidate"
    notes: "Duplicate script ending with 3.py"
  - candidate_id: "M76-CAND-027"
    path: "scripts/validate-index 3.py"
    category: "duplicate_script"
    source_evidence: "reports/m75-drift-repo-hygiene-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "delete_candidate"
    notes: "Duplicate script ending with 3.py"
  - candidate_id: "M76-CAND-028"
    path: "scripts/validate-required-sections 3.py"
    category: "duplicate_script"
    source_evidence: "reports/m75-drift-repo-hygiene-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "delete_candidate"
    notes: "Duplicate script ending with 3.py"
  - candidate_id: "M76-CAND-029"
    path: "scripts/validate-status-semantics 3.py"
    category: "duplicate_script"
    source_evidence: "reports/m75-drift-repo-hygiene-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "delete_candidate"
    notes: "Duplicate script ending with 3.py"
  - candidate_id: "M76-CAND-030"
    path: "scripts/agent-complete.py"
    category: "legacy_entrypoint"
    source_evidence: "reports/m75-drift-repo-hygiene-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "mark_legacy_candidate"
    notes: "Legacy entrypoint script"
  - candidate_id: "M76-CAND-031"
    path: "scripts/agent-fail.py"
    category: "legacy_entrypoint"
    source_evidence: "reports/m75-drift-repo-hygiene-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "mark_legacy_candidate"
    notes: "Legacy entrypoint script"
  - candidate_id: "M76-CAND-032"
    path: "scripts/agent-next.py"
    category: "legacy_entrypoint"
    source_evidence: "reports/m75-drift-repo-hygiene-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "mark_legacy_candidate"
    notes: "Legacy entrypoint script"
  - candidate_id: "M76-CAND-033"
    path: "scripts/agentos.py"
    category: "legacy_entrypoint"
    source_evidence: "reports/m75-drift-repo-hygiene-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "mark_legacy_candidate"
    notes: "Legacy entrypoint script"
  - candidate_id: "M76-CAND-034"
    path: "scripts/run-active-task.py"
    category: "legacy_entrypoint"
    source_evidence: "reports/m75-drift-repo-hygiene-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "mark_legacy_candidate"
    notes: "Legacy entrypoint script"
  - candidate_id: "M76-CAND-035"
    path: "HANDOFF 2.md"
    category: "copy_file"
    source_evidence: "read-only workspace tree analysis"
    evidence_status: "evidence_present"
    candidate_confidence: "medium"
    proposed_later_action: "inspect"
    notes: "Duplicate or legacy handoff file"
  - candidate_id: "M76-CAND-036"
    path: "llms.txt"
    category: "bootstrap_doc"
    source_evidence: "reports/m75-governance-validation-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "do_not_touch"
    notes: "Bootstrap source-of-truth roadmap gateway document"
  - candidate_id: "M76-CAND-037"
    path: "AGENTS.md"
    category: "bootstrap_doc"
    source_evidence: "reports/m75-governance-validation-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "do_not_touch"
    notes: "Agent adapter settings doc"
  - candidate_id: "M76-CAND-038"
    path: "CLAUDE.md"
    category: "bootstrap_doc"
    source_evidence: "reports/m75-governance-validation-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "do_not_touch"
    notes: "Claude specific instructions doc"
  - candidate_id: "M76-CAND-039"
    path: "GEMINI.md"
    category: "bootstrap_doc"
    source_evidence: "reports/m75-governance-validation-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "do_not_touch"
    notes: "Gemini specific instructions doc"
  - candidate_id: "M76-CAND-040"
    path: "README.md"
    category: "bootstrap_doc"
    source_evidence: "reports/m75-governance-validation-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "do_not_touch"
    notes: "General project readme"
  - candidate_id: "M76-CAND-041"
    path: "scripts/agentos-validate.py"
    category: "validation_wrapper"
    source_evidence: "reports/m75-governance-validation-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "do_not_touch"
    notes: "Validation runner orchestration entrypoint"
  - candidate_id: "M76-CAND-042"
    path: "scripts/check-dangerous-commands.py"
    category: "validation_wrapper"
    source_evidence: "reports/m75-governance-validation-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "do_not_touch"
    notes: "Dangerous command execution validator"
  - candidate_id: "M76-CAND-043"
    path: "scripts/check-execution-authorization.py"
    category: "validation_wrapper"
    source_evidence: "reports/m75-governance-validation-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "do_not_touch"
    notes: "Execution authorization checking script"
  - candidate_id: "M76-CAND-044"
    path: "scripts/check-execution-readiness.py"
    category: "validation_wrapper"
    source_evidence: "reports/m75-governance-validation-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "do_not_touch"
    notes: "Execution readiness checker"
  - candidate_id: "M76-CAND-045"
    path: "scripts/check-human-approval.py"
    category: "validation_wrapper"
    source_evidence: "reports/m75-governance-validation-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "do_not_touch"
    notes: "Human approval validator"
  - candidate_id: "M76-CAND-046"
    path: "scripts/check-lifecycle-mutation.py"
    category: "validation_wrapper"
    source_evidence: "reports/m75-governance-validation-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "do_not_touch"
    notes: "Lifecycle mutation validator"
  - candidate_id: "M76-CAND-047"
    path: "scripts/check-readiness-assertions.py"
    category: "validation_wrapper"
    source_evidence: "reports/m75-governance-validation-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "do_not_touch"
    notes: "Readiness assertions validator"
  - candidate_id: "M76-CAND-048"
    path: "scripts/check-validator-authority-boundary.py"
    category: "validation_wrapper"
    source_evidence: "reports/m75-governance-validation-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "do_not_touch"
    notes: "Validator authority boundary checking script"
  - candidate_id: "M76-CAND-049"
    path: "scripts/validate-lifecycle-apply.py"
    category: "validation_wrapper"
    source_evidence: "reports/m75-governance-validation-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "do_not_touch"
    notes: "Lifecycle apply checking script"
  - candidate_id: "M76-CAND-050"
    path: "scripts/validate-task.py"
    category: "validation_wrapper"
    source_evidence: "reports/m75-governance-validation-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "do_not_touch"
    notes: "Task contract YAML schema validator"
  - candidate_id: "M76-CAND-051"
    path: "reports/m71-script-inventory.json"
    category: "derived_navigation_index_artifact"
    source_evidence: "reports/m75-drift-repo-hygiene-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "inspect"
    notes: "Derived navigation helper index file"
  - candidate_id: "M76-CAND-052"
    path: "repo-map.md"
    category: "derived_navigation_index_artifact"
    source_evidence: "reports/m75-drift-repo-hygiene-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "inspect"
    notes: "Derived repository layout map"
  - candidate_id: "M76-CAND-053"
    path: "ROUTES-REGISTRY.md"
    category: "DO_NOT_TOUCH"
    source_evidence: "reports/m75-governance-validation-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "do_not_touch"
    physical_change_authorized: false
    human_review_required: true
    notes: "Protected/canonical — cannot be modified without human checkpoint"
  - candidate_id: "M76-CAND-054"
    path: "core-rules/MAIN.md"
    category: "DO_NOT_TOUCH"
    source_evidence: "reports/m75-governance-validation-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "do_not_touch"
    physical_change_authorized: false
    human_review_required: true
    notes: "Protected/canonical — cannot be modified without human checkpoint"
  - candidate_id: "M76-CAND-055"
    path: "state/MAIN.md"
    category: "DO_NOT_TOUCH"
    source_evidence: "reports/m75-governance-validation-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "do_not_touch"
    physical_change_authorized: false
    human_review_required: true
    notes: "Protected/canonical — cannot be modified without human checkpoint"
  - candidate_id: "M76-CAND-056"
    path: "workflow/MAIN.md"
    category: "DO_NOT_TOUCH"
    source_evidence: "reports/m75-governance-validation-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "do_not_touch"
    physical_change_authorized: false
    human_review_required: true
    notes: "Protected/canonical — cannot be modified without human checkpoint"
  - candidate_id: "M76-CAND-057"
    path: "quality/MAIN.md"
    category: "DO_NOT_TOUCH"
    source_evidence: "reports/m75-governance-validation-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "do_not_touch"
    physical_change_authorized: false
    human_review_required: true
    notes: "Protected/canonical — cannot be modified without human checkpoint"
  - candidate_id: "M76-CAND-058"
    path: "security/MAIN.md"
    category: "DO_NOT_TOUCH"
    source_evidence: "reports/m75-governance-validation-facts-review.md"
    evidence_status: "evidence_present"
    candidate_confidence: "high"
    proposed_later_action: "do_not_touch"
    physical_change_authorized: false
    human_review_required: true
    notes: "Protected/canonical — cannot be modified without human checkpoint"
