# M71.6 — Active-Tree Cleanup Plan

## Task Boundary

This M71 active-tree cleanup plan is evidence only.
This M71 active-tree cleanup plan is not approval.
This M71 active-tree cleanup plan does not authorize cleanup.
This M71 active-tree cleanup plan does not execute cleanup.
This M71 active-tree cleanup plan does not authorize script changes.
This M71 active-tree cleanup plan does not approve deletion, archiving, renaming, or moving files.
This M71 active-tree cleanup plan does not create registry authority.
This M71 active-tree cleanup plan does not authorize validator creation, fixture creation, or lifecycle mutation.
Cleanup candidates require human checkpoint before any later execution task.
Proposed action classes are planning labels only.
No executable cleanup commands may be included.
reports/m71-script-inventory.md is the source-of-truth inventory artifact.
reports/m71-script-inventory.json is a derived navigation artifact only.
reports/m71-script-inventory.json must not become source of truth.
Human review remains required.

## Active Task Record

id: task-71.6
milestone: M71
name: "Active-Tree Cleanup Plan"
status: active
mode: "PLANNING / READ-ONLY CLEANUP CANDIDATES / NO CLEANUP EXECUTION"
branch: dev
started_at: "2026-05-29"

## Inputs Reviewed

PRIMARY_INPUT: reports/m71-script-inventory.md
SECONDARY_INPUT: docs/SCRIPT-RESPONSIBILITY-MAP.md
TERTIARY_INPUT: docs/SCRIPT-LEGACY-AND-DUPLICATE-MAP.md
QUATERNARY_INPUT: docs/SCRIPT-DANGEROUS-OPERATIONS-AUDIT.md
QUINARY_INPUT: docs/SCRIPT-OUTPUT-EXIT-CONTRACT-REVIEW.md
NAVIGATION_HELPER: reports/m71-script-inventory.json

## Authority Rule

markdown_inputs_used_as_primary: true
json_used_as_navigation_only: true
json_overrode_markdown: false

The Markdown inventory is the source of truth for this pass.
The JSON inventory is a navigation helper only.
The M71.1 through M71.5 Markdown artifacts stay authoritative over JSON if there is any mismatch.
No cleanup action is approved by this plan.

## Source Inventory Summary

The inventory artifact is present and treated as the primary source.
The navigation JSON is present and treated as derived only.
The repository file list shows one obvious generated-cache cluster under scripts/__pycache__.
The repository file list also shows one obvious legacy-looking root file name: HANDOFF 2.md.

## Responsibility Map Summary

M71.2 exists and remains the responsibility source for script ownership.
The responsibility map keeps ownership in Markdown, not JSON.
Governance-critical files stay active or blocked, not cleaned up by this plan.

## Legacy / Duplicate Map Summary

M71.3 exists and remains the duplicate and legacy signal source.
The only obvious duplicate-looking root name from the file list is HANDOFF 2.md.
That file needs owner review because the intent is not clear from the name alone.

## Dangerous Operations Summary

M71.4 exists and remains the risk-signal source for dangerous operations.
Files whose names point at dangerous commands, execution authorization, lifecycle mutation, or approval boundaries are blocked from cleanup planning approval.

## Output / Exit-Code Contract Summary

M71.5 exists and remains the output and exit-code contract source.
The review says the contract was not changed and the final dispatcher decision was not made.
Files with unclear runner or validation contracts stay under owner review or blocked protection.

## Current Git Status Snapshot

clean

## Proposed Action Classes

keep_active_count: 15
archive_candidate_count: 0
remove_candidate_count: 6
rename_candidate_count: 0
needs_owner_review_count: 2
blocked_protected_count: 10
generated_cache_candidate_count: 6
duplicate_backup_legacy_candidate_count: 1
risk_sensitive_candidate_count: 12
contract_risk_candidate_count: 1
human_checkpoint_required_count: 18
later_governed_execution_required_count: 18

| path | source_signal | responsibility_category | risk_signal | contract_signal | proposed_action_class | reason | human_checkpoint_required | later_execution_allowed_without_human | rollback_or_recovery_note | cleanup_authorized | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| llms.txt | canonical startup entry | canonical guardrail | low | startup authority only | KEEP_ACTIVE | Required bootstrap file for every agent run | false | true | Keep as-is; this is the bootstrap entry | false | source-of-truth entry point |
| ROUTES-REGISTRY.md | canonical route registry | canonical routing | low | route ownership only | KEEP_ACTIVE | Confirms which modules own runtime routing | false | true | Keep as-is; route registry remains canonical | false | route authority reference |
| core-rules/MAIN.md | canonical governance module | governance | low | authority boundary | KEEP_ACTIVE | Owns priority, authority, and agent boundaries | false | true | Keep as-is; governance stays central | false | canonical governance file |
| state/MAIN.md | canonical state module | lifecycle and recovery | low | state contract | KEEP_ACTIVE | Owns state lifecycle and recovery rules | false | true | Keep as-is; state remains canonical | false | canonical state file |
| workflow/MAIN.md | canonical workflow module | execution boundary | low | plan-gate contract | KEEP_ACTIVE | Owns execution sequence and scope control | false | true | Keep as-is; workflow remains canonical | false | canonical workflow file |
| quality/MAIN.md | canonical quality module | verification | low | readiness proof contract | KEEP_ACTIVE | Owns verification and smoke-check rules | false | true | Keep as-is; quality remains canonical | false | canonical quality file |
| security/MAIN.md | canonical security module | security | medium | access and compliance boundary | KEEP_ACTIVE | Owns sensitive-data and access rules | false | true | Keep as-is; security remains canonical | false | canonical security file |
| tasks/active-task.md | active task record | active-task governance | medium | lifecycle/task contract | KEEP_ACTIVE | Current active task record must stay in place | false | true | Keep as-is; task record is required for this milestone | false | active task boundary |
| reports/m71-script-inventory.md | source-of-truth inventory artifact | M71 source-of-truth | low | inventory authority | KEEP_ACTIVE | Primary inventory artifact for M71 | false | true | Keep as-is; later steps must continue to read Markdown first | false | authoritative inventory |
| reports/m71-script-inventory.json | derived navigation artifact only | derived navigation | low | derived only | KEEP_ACTIVE | Navigation helper only; not authoritative | false | true | Keep as-is; if regenerated later it still must not override Markdown | false | navigation helper only |
| docs/SCRIPT-RESPONSIBILITY-MAP.md | source-of-truth responsibility map | M71 source-of-truth | medium | responsibility map contract | KEEP_ACTIVE | Required M71.2 map stays active as evidence | false | true | Keep as-is; map remains canonical for ownership | false | source-of-truth map |
| docs/SCRIPT-LEGACY-AND-DUPLICATE-MAP.md | source-of-truth legacy map | M71 source-of-truth | medium | legacy classification contract | KEEP_ACTIVE | Required M71.3 map stays active as evidence | false | true | Keep as-is; map remains canonical for legacy signals | false | source-of-truth map |
| docs/SCRIPT-DANGEROUS-OPERATIONS-AUDIT.md | source-of-truth risk audit | M71 source-of-truth | medium | dangerous-operations contract | KEEP_ACTIVE | Required M71.4 audit stays active as evidence | false | true | Keep as-is; audit remains canonical for risk signals | false | source-of-truth audit |
| docs/SCRIPT-OUTPUT-EXIT-CONTRACT-REVIEW.md | source-of-truth contract review | M71 source-of-truth | medium | output and exit-code contract | KEEP_ACTIVE | Required M71.5 review stays active as evidence | false | true | Keep as-is; review remains canonical for contract signals | false | source-of-truth review |
| docs/ACTIVE-TREE-CLEANUP-PLAN.md | this plan artifact | active planning artifact | low | planning-only | KEEP_ACTIVE | This file is the required M71.6 output | false | true | Keep as-is; later cleanup tasks must not rewrite history here | false | current planning artifact |
| scripts/__pycache__/agent-complete.cpython-314.pyc | tracked compiled bytecode cache | generated/cache | low | none | REMOVE_CANDIDATE | Bytecode cache looks generated and removable in a later governed task | true | false | Recreate from source if a later task needs it | false | generated cache-looking artifact |
| scripts/__pycache__/agent-fail.cpython-314.pyc | tracked compiled bytecode cache | generated/cache | low | none | REMOVE_CANDIDATE | Bytecode cache looks generated and removable in a later governed task | true | false | Recreate from source if a later task needs it | false | generated cache-looking artifact |
| scripts/__pycache__/agent-next.cpython-314.pyc | tracked compiled bytecode cache | generated/cache | low | none | REMOVE_CANDIDATE | Bytecode cache looks generated and removable in a later governed task | true | false | Recreate from source if a later task needs it | false | generated cache-looking artifact |
| scripts/__pycache__/generate-task-contract.cpython-314.pyc | tracked compiled bytecode cache | generated/cache | low | none | REMOVE_CANDIDATE | Bytecode cache looks generated and removable in a later governed task | true | false | Recreate from source if a later task needs it | false | generated cache-looking artifact |
| scripts/__pycache__/validate-task.cpython-314.pyc | tracked compiled bytecode cache | generated/cache | low | none | REMOVE_CANDIDATE | Bytecode cache looks generated and removable in a later governed task | true | false | Recreate from source if a later task needs it | false | generated cache-looking artifact |
| scripts/__pycache__/validate-verification.cpython-314.pyc | tracked compiled bytecode cache | generated/cache | low | none | REMOVE_CANDIDATE | Bytecode cache looks generated and removable in a later governed task | true | false | Recreate from source if a later task needs it | false | generated cache-looking artifact |
| HANDOFF 2.md | duplicate-looking root name | legacy/duplicate-looking | medium | unclear intent | NEEDS_OWNER_REVIEW | The name suggests a secondary handoff file, but content intent is not confirmed | true | false | Keep until owner says whether it belongs in active tree, archive, or rename review | false | duplicate/legacy-looking candidate |
| scripts/validate-runner-protocol.py | validator-like runner protocol file | contract-sensitive validation | medium | output and exit-code contract unclear | NEEDS_OWNER_REVIEW | The name suggests a protocol contract, but the cleanup direction is not clear enough | true | false | Keep until owner confirms whether this belongs in active tree or in a later governed task | false | contract-risk candidate |
| scripts/agentos-validate.py | validation entrypoint | governance-critical validator | high | validator authority boundary | BLOCKED_PROTECTED | Validator-like and governance-critical; not a cleanup candidate without separate human checkpoint | true | false | No change; preserve as protected validation authority | false | protected artifact candidate |
| scripts/check-dangerous-commands.py | dangerous-commands audit | dangerous-operation audit | high | dangerous-operation boundary | BLOCKED_PROTECTED | Name points directly at dangerous command checks | true | false | No change; preserve as protected risk check | false | risk-sensitive protected file |
| scripts/check-execution-authorization.py | execution authorization check | approval boundary | high | approval contract | BLOCKED_PROTECTED | Name points at approval gating and execution authorization | true | false | No change; preserve as protected approval boundary | false | protected approval boundary file |
| scripts/check-execution-readiness.py | execution readiness check | readiness gate | medium | readiness contract | BLOCKED_PROTECTED | Readiness checks are governance-sensitive and should not be cleaned up here | true | false | No change; preserve as protected readiness gate | false | protected readiness file |
| scripts/check-human-approval.py | human approval check | approval boundary | high | human approval contract | BLOCKED_PROTECTED | Human approval boundaries are not cleanup targets | true | false | No change; preserve as protected approval boundary | false | protected approval boundary file |
| scripts/check-lifecycle-mutation.py | lifecycle mutation check | lifecycle boundary | high | lifecycle mutation contract | BLOCKED_PROTECTED | Lifecycle mutation signals are governance-critical | true | false | No change; preserve as protected lifecycle guard | false | protected lifecycle file |
| scripts/check-readiness-assertions.py | readiness assertion checker | readiness gate | medium | readiness assertion contract | BLOCKED_PROTECTED | Readiness assertions are boundary checks, not cleanup targets | true | false | No change; preserve as protected readiness guard | false | protected readiness file |
| scripts/check-validator-authority-boundary.py | validator authority check | authority boundary | high | validator authority contract | BLOCKED_PROTECTED | Authority-boundary logic must stay protected | true | false | No change; preserve as protected governance guard | false | protected governance file |
| scripts/validate-lifecycle-apply.py | lifecycle apply validator | lifecycle mutation boundary | high | lifecycle apply contract | BLOCKED_PROTECTED | Validator for lifecycle changes is governance-critical | true | false | No change; preserve as protected lifecycle validator | false | protected lifecycle validator |
| scripts/validate-task.py | task validator | task lifecycle governance | medium | validation contract | BLOCKED_PROTECTED | Task validation is governance-sensitive and should stay protected | true | false | No change; preserve as protected task validator | false | protected validation file |

## KEEP_ACTIVE Items

These rows in the table stay active for now.
They are the canonical modules, M71 source-of-truth artifacts, and this planning file.

## ARCHIVE_CANDIDATE Items

No archive candidates were identified in this read-only pass.

## REMOVE_CANDIDATE Items

The six tracked files under scripts/__pycache__ are the cleanup candidates that look generated and cache-like.

## RENAME_CANDIDATE Items

No rename candidates were identified in this read-only pass.

## NEEDS_OWNER_REVIEW Items

HANDOFF 2.md needs owner review because the name looks legacy-like but the intended role is not confirmed.
scripts/validate-runner-protocol.py needs owner review because the contract direction is not clear enough from the name alone.

## BLOCKED_PROTECTED Items

The blocked rows are governance-critical, validation-related, approval-related, lifecycle-related, or dangerous-operations-related.
They should not be proposed for cleanup without a later governed execution task and explicit human checkpoint.

## Generated / Cache Candidate Items

The generated/cache candidate set is scripts/__pycache__/agent-complete.cpython-314.pyc, scripts/__pycache__/agent-fail.cpython-314.pyc, scripts/__pycache__/agent-next.cpython-314.pyc, scripts/__pycache__/generate-task-contract.cpython-314.pyc, scripts/__pycache__/validate-task.cpython-314.pyc, and scripts/__pycache__/validate-verification.cpython-314.pyc.

## Duplicate / Backup / Legacy Candidate Items

HANDOFF 2.md is the only obvious duplicate or legacy-looking candidate from the file list alone.

## Risk-Sensitive Candidate Items

The risk-sensitive candidates are the files whose names point at dangerous commands, approvals, readiness checks, lifecycle mutation, or validator authority.
These remain blocked or owner-review only.

## Contract-Risk Candidate Items

scripts/validate-runner-protocol.py is the only clear contract-risk candidate from the name alone.
The output and exit-code contract is not confirmed by this planning pass.

## Human Checkpoint Requirements

Every non-KEEP row requires human checkpoint before any later execution task.
That applies to archive, remove, rename, owner-review, and blocked-protected candidates.

## Later Governed Execution Requirements

Any later cleanup action needs a separate governed task, explicit human checkpoint, and a recovery plan.
No later execution may be inferred from this plan.

## Rollback / Recovery Considerations

Removal candidates should be recoverable from source or regenerated if a later governed task needs them.
Protected files should be left untouched unless a later governed task explicitly reclassifies them.

## Markdown / JSON Authority Check

markdown_inputs_used_as_primary: true
json_used_as_navigation_only: true
json_overrode_markdown: false

The Markdown artifacts stay authoritative.
The JSON artifact is only a navigation helper.
No conflict was used to override the Markdown sources.

## No Cleanup Execution Check

scripts_modified: false
scripts_executed: false
validators_executed: false
cleanup_performed: false
cleanup_authorized: false
files_deleted: false
files_archived: false
files_renamed: false
files_moved: false
registries_created: false
validators_created: false
json_artifacts_created: false
scope_violations: false

No cleanup was performed.
No cleanup was authorized.
No scripts were modified.
No scripts were executed.
No validators were executed.
No files were deleted, archived, renamed, or moved.
No registries, validators, or JSON artifacts were created.
No scope violation was recorded.

## No Executable Cleanup Commands Check

cleanup_commands_written: false
unsafe_paths_written: false

No executable cleanup commands were written.
No unsafe paths were written.

## Source Line / Secret Leakage Check

source_lines_printed: false
secret_values_printed: false

No source lines were printed into this plan.
No secret values were printed into this plan.

## Scope Compliance

The only allowed file updates for M71.6 are tasks/active-task.md and docs/ACTIVE-TREE-CLEANUP-PLAN.md.
This plan stays within that boundary.

## M71.7 Preparation Decision

may_prepare_m71_7: true_with_warnings
may_prepare_m71_7 is roadmap preparation only.
may_prepare_m71_7 does not start M71.7.
may_prepare_m71_7 is not approval.
Human review remains required.

## Explicit Non-Approval Boundary

This M71 active-tree cleanup plan is evidence only.
This M71 active-tree cleanup plan is not approval.
This M71 active-tree cleanup plan does not authorize cleanup.
This M71 active-tree cleanup plan does not execute cleanup.
This M71 active-tree cleanup plan does not authorize script changes.
This M71 active-tree cleanup plan does not approve deletion, archiving, renaming, or moving files.
This M71 active-tree cleanup plan does not create registry authority.
This M71 active-tree cleanup plan does not authorize validator creation, fixture creation, or lifecycle mutation.
Cleanup candidates require human checkpoint before any later execution task.
Proposed action classes are planning labels only.
No executable cleanup commands may be included.
reports/m71-script-inventory.md is the source-of-truth inventory artifact.
reports/m71-script-inventory.json is a derived navigation artifact only.
reports/m71-script-inventory.json must not become source of truth.
Human review remains required.

## Final Status

FINAL_STATUS: M71_ACTIVE_TREE_CLEANUP_PLAN_COMPLETE_WITH_WARNINGS
