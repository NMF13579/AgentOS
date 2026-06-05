---
task_id: M90.0
task_name: Markdown Optimization Scope Lock
milestone: M90
milestone_name: Controlled Markdown Documentation Optimization
mode: read_only_scope_lock

scope_type: markdown_docs_only

allowed_surface:
  markdown_docs: true
  reports_for_m90_only: true

forbidden_surface:
  scripts: true
  schemas: true
  workflows: true
  task_lifecycle_files: true
  protected_artifacts_without_human_checkpoint: true
  canonical_artifacts_without_human_checkpoint: true
  templates: true
  adapters: true
  source_code: true

markdown_changes_allowed_in_m90_0: false
markdown_changes_possible_in_later_m90_tasks: true
physical_markdown_changes_allowed_only_in: M90.4
physical_markdown_changes_allowed_only_after_human_selected_subset: true

human_selected_subset_required_for_physical_changes: true
max_first_batch_markdown_candidates: small_human_selected_subset
exact_paths_required: true
broad_globs_allowed: false

canonical_meaning_must_be_preserved: true
approval_boundary_must_be_preserved: true
evidence_chain_must_be_preserved: true
task_lifecycle_meaning_must_be_preserved: true
validation_authority_references_must_be_preserved: true
script_spec_consistency_references_must_be_preserved: true

shorter_is_good_only_if_equally_safe_or_safer: true
ambiguous_compression_forbidden: true
meaning_loss_allowed: false
approval_semantics_change_allowed: false
evidence_semantics_change_allowed: false
pass_semantics_change_allowed: false
unknown_semantics_weakening_allowed: false
not_run_to_pass_conversion_allowed: false

script_changes_allowed_in_m90: false
schema_changes_allowed_in_m90: false
workflow_changes_allowed_in_m90: false
lifecycle_mutation_allowed: false

m91_preparation_allowed_by_this_task: false
m91_execution_authorized: false
m91_started: false

may_prepare_m90_1_markdown_inventory: true_with_warnings

FINAL_STATUS: M90_0_SCOPE_LOCK_READY_WITH_WARNINGS
---

# M90.0 Markdown Optimization Scope Lock

meaning_boundary:
  canonical_meaning_preserved: safe
  canonical_meaning_changed: block_or_human_checkpoint_required
  duplicate_or_stale_text_removed_without_meaning_loss: possible_later_M90_action
  evidence_chain_removed_or_blurred: blocked
  approval_boundary_blurred: blocked
  validation_authority_reference_removed: blocked
  script_spec_consistency_reference_removed: blocked

M90.0 does not approve M89.
M90.0 does not approve M90.
M90.0 does not authorize Markdown optimization.
M90.0 does not authorize M91 execution.
M90.0 is a read-only intake and scope-lock task.
Any physical Markdown optimization requires later M90 tasks and a human-selected subset.
Shorter documentation is acceptable only if it is equally safe or safer.
Canonical meaning must not be weakened.
PASS remains separate from approval.
Evidence remains separate from approval.
Human approval remains required where applicable.
