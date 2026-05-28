# False PASS Resistance Checker

## 1. Purpose
This document describes the M67 false PASS resistance checker.

The checker detects overclaiming of validation PASS.
The checker blocks fake approval claims.
The checker blocks fake completion claims.
The checker blocks fake completion gate claims.
The checker blocks human review waiver claims.
The checker blocks lifecycle mutation claims.
The checker blocks M68 auto-start claims.
The checker is not approval.
The checker does not complete tasks.
Human review remains required.

## 2. CLI
Use:

`python3 scripts/check-false-pass-resistance.py --input <false-pass-check-input-json> --json`

Optional:
- `--strict`

Rules:
- `--input` means the false PASS check input JSON.
- `--input` is not a lifecycle mutation request.
- `--input` is not approval evidence.
- `--input` is not a completion request by itself.

## 3. Input Model
Expected fields:
- `contract_version`
- `package_type`
- `task_id`
- `m66_result`
- `m66_result_source`
- `claims`
- `operative_fields`
- `completion_gate`
- `human_review`
- `warnings`
- `blockers`
- `non_authority_boundary`

Required values:
- `contract_version`: `"1.0.0"`
- `package_type`: `"false_pass_check_input"`

## 4. Result Values
- `M67_FALSE_PASS_CHECK_PASS`
- `M67_FALSE_PASS_CHECK_PASS_WITH_WARNINGS`
- `M67_FALSE_PASS_CHECK_BLOCKED`
- `M67_FALSE_PASS_CHECK_NOT_ENOUGH_EVIDENCE`

## 5. Exit Codes
- `exit 0` — `M67_FALSE_PASS_CHECK_PASS`
- `exit 0` — `M67_FALSE_PASS_CHECK_PASS_WITH_WARNINGS`
- `exit 1` — `M67_FALSE_PASS_CHECK_BLOCKED`
- `exit 1` — `M67_FALSE_PASS_CHECK_NOT_ENOUGH_EVIDENCE`
- `exit 2` — CLI misuse / internal checker error

## 6. Forbidden Claims
The checker blocks these claim categories:
- approval claims
- completion claims
- completion gate claims
- human review waiver claims
- lifecycle mutation claims
- merge/push/release/production claims
- M68 claims

## 7. Forbidden Operative Fields
The checker blocks forbidden operative fields such as:
- `approved`
- `task_approved`
- `task_accepted`
- `task_complete`
- `task_completed`
- `completion_approved`
- `completion_authorized`
- `completion_gate_passed`
- `completion_gate_inferred`
- `human_review_not_required`
- `skip_human_review`
- `merge_authorized`
- `push_authorized`
- `release_authorized`
- `deployment_authorized`
- `production_ready`
- `ready_for_production`
- `m68_started_automatically`
- `m68_auto_started`
- `lifecycle_mutated`
- `completion_state_applied`
- `automatic_completion_allowed`

## 8. Safe Context
Safe context types:
- `safe_boundary`
- `documentation_example`
- `fixture_name`
- `negative_fixture_description`
- `policy_explanation`

Safe context must not be treated as operative approval/completion claim when clearly marked.

## 9. Recursive String Scanning
The checker recursively inspects string values in:
- dictionaries / objects
- arrays / lists
- nested result objects
- nested summaries
- completion request objects
- human review objects
- gate result objects

Rules:
- scan operative string values.
- scan nested string values.
- preserve safe non-authority boundary statements.
- preserve clearly marked forbidden examples.
- do not treat object keys alone as string claims unless the key is a forbidden operative field.
- treat ambiguous approval/completion wording as warning, `NOT_ENOUGH_EVIDENCE`, or `BLOCKED` according to strict mode.

## 10. Strict Mode
If `--strict` is provided:
- ambiguous approval wording → `BLOCKED`
- ambiguous completion wording → `BLOCKED`
- ambiguous gate-pass wording → `BLOCKED`
- unclear safe-context marking → `BLOCKED`
- missing optional but relevant evidence → `NOT_ENOUGH_EVIDENCE` or `BLOCKED` depending on severity

Strict mode must not weaken checks.

## 11. Completion Gate Boundary
Completion gate cannot be inferred from M66 PASS.
Completion gate cannot be inferred from M67 PASS.
Completion gate requires explicit policy.
Completion gate requires explicit human review status.
The checker is not the completion gate.

## 12. Non-Authority Boundary
M67 checker result is not approval.
M67 checker result does not complete tasks.
M67 checker result does not mutate lifecycle state.
M67 checker result does not authorize merge, push, release, or deployment.
M67 checker result does not start M68.
Human review remains required.

## 13. Relationship to Later Tasks
67.6 creates fixtures.
67.7 defines completion gate hardening contract.
67.8 validates integration.
67.9 reviews actions.
67.10 collects evidence.
67.11 closes M67.

## 14. Final Status
FINAL_STATUS: M67_FALSE_PASS_CHECKER_DEFINED_WITH_WARNINGS
