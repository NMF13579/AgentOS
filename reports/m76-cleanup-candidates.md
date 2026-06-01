# M76.1 — Cleanup Candidates and Pre-cleanup Baseline

## 1. Purpose
This report identifies repository cleanup candidates (duplicate scripts, compiled bytecode caches, and legacy entrypoints) and records the baseline status metrics of the repository before any physical cleanup actions are performed.

## 2. Precondition Check
The precondition completion intake report was successfully checked.
- `precondition_artifact_exists: true`
- `precondition_final_status_value: "M76_M75_COMPLETION_INTAKE_READY_WITH_WARNINGS"`
- `precondition_readiness_value: "true_with_warnings"`

## 3. Pre-cleanup Baseline Metrics
The current repository baseline is measured as follows:
- `git_working_tree_clean: true`
- `total_tracked_files: 5245`
- `python_audit_status: "PASS_WITH_WARNINGS"`

## 4. Cleanup Candidates

### 4.1. Duplicate Scripts (23 Files)
A total of 23 scripts ending with ` 3.py` exist in the `scripts/` directory as copy/backup files:
- `scripts/audit-m27 3.py`
- `scripts/audit-m27-level1 3.py`
- `scripts/audit-metadata-consistency 3.py`
- `scripts/audit-pre-merge-corridor 3.py`
- `scripts/audit-validation-integration 3.py`
- `scripts/build-index 3.py`
- `scripts/check-commit-push-preconditions 3.py`
- `scripts/check-github-platform-enforcement 3.py`
- `scripts/check-pre-merge-scope 3.py`
- `scripts/check-scope-compliance 3.py`
- `scripts/test-ci-advisory-config 3.py`
- `scripts/test-commit-push-preconditions-fixtures 3.py`
- `scripts/test-enforcement-fixtures 3.py`
- `scripts/test-m22-guardrails 3.py`
- `scripts/test-m27-level1-fixtures 3.py`
- `scripts/test-pre-merge-corridor-fixtures 3.py`
- `scripts/test-pre-merge-scope-fixtures 3.py`
- `scripts/test-scope-compliance-fixtures 3.py`
- `scripts/validate-boundary-claims 3.py`
- `scripts/validate-frontmatter 3.py`
- `scripts/validate-index 3.py`
- `scripts/validate-required-sections 3.py`
- `scripts/validate-status-semantics 3.py`

### 4.2. Compiled Bytecode Caches (6 Files)
A total of 6 tracked `.pyc` files exist in `scripts/__pycache__/`:
- `scripts/__pycache__/agent-complete.cpython-314.pyc`
- `scripts/__pycache__/agent-fail.cpython-314.pyc`
- `scripts/__pycache__/agent-next.cpython-314.pyc`
- `scripts/__pycache__/generate-task-contract.cpython-314.pyc`
- `scripts/__pycache__/validate-task.cpython-314.pyc`
- `scripts/__pycache__/validate-verification.cpython-314.pyc`

### 4.3. Legacy Entrypoint Scripts (5 Files)
A total of 5 legacy scripts remain in the `scripts/` directory:
- `scripts/agent-complete.py`
- `scripts/agent-fail.py`
- `scripts/agent-next.py`
- `scripts/agentos.py`
- `scripts/run-active-task.py`

## 5. Gaps Carried Forward
The 9 open P0 blocker gaps from M74 regression remain open and are carried forward as visible blockers:
1. `exit_2_semantics`
2. `pass_with_warnings_exit_0`
3. `missing_child_validator`
4. `malformed_child_output`
5. `child_failure_propagation`
6. `unknown_not_pass_requires_m74_regression_fixture`
7. `not_run_not_pass_requires_m74_regression_fixture`
8. `warning_visibility`
9. `wrapper_gaps`

## 6. Boundaries and Non-Execution Statement
This task is planning and baseline documentation only. No physical files have been deleted, moved, renamed, or modified. No codebase logic has been altered. Human review remains required before any physical changes are proposed or authorized.

## 7. Local Final Status
- `FINAL_STATUS: "M76_CLEANUP_CANDIDATES_COMPLETE_WITH_WARNINGS"`

## 8. Output Readiness
- `may_prepare_m76_2: "true_with_warnings"`

---

### Machine-Readable Metadata
```yaml
FINAL_STATUS: "M76_CLEANUP_CANDIDATES_COMPLETE_WITH_WARNINGS"
may_prepare_m76_2: "true_with_warnings"
physical_change_authorized: false
p0_gaps_carried_forward: 9
warnings_carried_forward: true
git_working_tree_clean: true
total_tracked_files: 5245
python_audit_status: "PASS_WITH_WARNINGS"

cleanup_candidates:
  duplicates:
    - path: "scripts/audit-m27 3.py"
      candidate_class: "REMOVE_CANDIDATE"
      physical_change_authorized: false
      human_review_required: true
    - path: "scripts/audit-m27-level1 3.py"
      candidate_class: "REMOVE_CANDIDATE"
      physical_change_authorized: false
      human_review_required: true
    - path: "scripts/audit-metadata-consistency 3.py"
      candidate_class: "REMOVE_CANDIDATE"
      physical_change_authorized: false
      human_review_required: true
    - path: "scripts/audit-pre-merge-corridor 3.py"
      candidate_class: "REMOVE_CANDIDATE"
      physical_change_authorized: false
      human_review_required: true
    - path: "scripts/audit-validation-integration 3.py"
      candidate_class: "REMOVE_CANDIDATE"
      physical_change_authorized: false
      human_review_required: true
    - path: "scripts/build-index 3.py"
      candidate_class: "REMOVE_CANDIDATE"
      physical_change_authorized: false
      human_review_required: true
    - path: "scripts/check-commit-push-preconditions 3.py"
      candidate_class: "REMOVE_CANDIDATE"
      physical_change_authorized: false
      human_review_required: true
    - path: "scripts/check-github-platform-enforcement 3.py"
      candidate_class: "REMOVE_CANDIDATE"
      physical_change_authorized: false
      human_review_required: true
    - path: "scripts/check-pre-merge-scope 3.py"
      candidate_class: "REMOVE_CANDIDATE"
      physical_change_authorized: false
      human_review_required: true
    - path: "scripts/check-scope-compliance 3.py"
      candidate_class: "REMOVE_CANDIDATE"
      physical_change_authorized: false
      human_review_required: true
    - path: "scripts/test-ci-advisory-config 3.py"
      candidate_class: "REMOVE_CANDIDATE"
      physical_change_authorized: false
      human_review_required: true
    - path: "scripts/test-commit-push-preconditions-fixtures 3.py"
      candidate_class: "REMOVE_CANDIDATE"
      physical_change_authorized: false
      human_review_required: true
    - path: "scripts/test-enforcement-fixtures 3.py"
      candidate_class: "REMOVE_CANDIDATE"
      physical_change_authorized: false
      human_review_required: true
    - path: "scripts/test-m22-guardrails 3.py"
      candidate_class: "REMOVE_CANDIDATE"
      physical_change_authorized: false
      human_review_required: true
    - path: "scripts/test-m27-level1-fixtures 3.py"
      candidate_class: "REMOVE_CANDIDATE"
      physical_change_authorized: false
      human_review_required: true
    - path: "scripts/test-pre-merge-corridor-fixtures 3.py"
      candidate_class: "REMOVE_CANDIDATE"
      physical_change_authorized: false
      human_review_required: true
    - path: "scripts/test-pre-merge-scope-fixtures 3.py"
      candidate_class: "REMOVE_CANDIDATE"
      physical_change_authorized: false
      human_review_required: true
    - path: "scripts/test-scope-compliance-fixtures 3.py"
      candidate_class: "REMOVE_CANDIDATE"
      physical_change_authorized: false
      human_review_required: true
    - path: "scripts/validate-boundary-claims 3.py"
      candidate_class: "REMOVE_CANDIDATE"
      physical_change_authorized: false
      human_review_required: true
    - path: "scripts/validate-frontmatter 3.py"
      candidate_class: "REMOVE_CANDIDATE"
      physical_change_authorized: false
      human_review_required: true
    - path: "scripts/validate-index 3.py"
      candidate_class: "REMOVE_CANDIDATE"
      physical_change_authorized: false
      human_review_required: true
    - path: "scripts/validate-required-sections 3.py"
      candidate_class: "REMOVE_CANDIDATE"
      physical_change_authorized: false
      human_review_required: true
    - path: "scripts/validate-status-semantics 3.py"
      candidate_class: "REMOVE_CANDIDATE"
      physical_change_authorized: false
      human_review_required: true
  pycache_files:
    - path: "scripts/__pycache__/agent-complete.cpython-314.pyc"
      candidate_class: "REMOVE_CANDIDATE"
      physical_change_authorized: false
      human_review_required: true
    - path: "scripts/__pycache__/agent-fail.cpython-314.pyc"
      candidate_class: "REMOVE_CANDIDATE"
      physical_change_authorized: false
      human_review_required: true
    - path: "scripts/__pycache__/agent-next.cpython-314.pyc"
      candidate_class: "REMOVE_CANDIDATE"
      physical_change_authorized: false
      human_review_required: true
    - path: "scripts/__pycache__/generate-task-contract.cpython-314.pyc"
      candidate_class: "REMOVE_CANDIDATE"
      physical_change_authorized: false
      human_review_required: true
    - path: "scripts/__pycache__/validate-task.cpython-314.pyc"
      candidate_class: "REMOVE_CANDIDATE"
      physical_change_authorized: false
      human_review_required: true
    - path: "scripts/__pycache__/validate-verification.cpython-314.pyc"
      candidate_class: "REMOVE_CANDIDATE"
      physical_change_authorized: false
      human_review_required: true
  legacy_entrypoints:
    - path: "scripts/agent-complete.py"
      candidate_class: "ARCHIVE_CANDIDATE"
      physical_change_authorized: false
      human_review_required: true
    - path: "scripts/agent-fail.py"
      candidate_class: "ARCHIVE_CANDIDATE"
      physical_change_authorized: false
      human_review_required: true
    - path: "scripts/agent-next.py"
      candidate_class: "ARCHIVE_CANDIDATE"
      physical_change_authorized: false
      human_review_required: true
    - path: "scripts/agentos.py"
      candidate_class: "REVIEW_REQUIRED"
      physical_change_authorized: false
      human_review_required: true
    - path: "scripts/run-active-task.py"
      candidate_class: "REVIEW_REQUIRED"
      physical_change_authorized: false
      human_review_required: true
```
