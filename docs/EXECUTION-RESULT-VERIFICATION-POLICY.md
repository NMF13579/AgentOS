# Execution Result Verification Policy

## Purpose

This document defines the Execution Result Verification Policy for milestone M59. It defines the source-of-truth policy rules that map preconditions, diff/scope verification, validation evidence, and result/output signals into an execution result verification decision.

## Preconditions

Before evaluating this policy, the following preconditions must be verified:
1. `reports/m59-m58-completion-intake.md` exists and contains:
   - `MAY_PROCEED_TO_M59_VERIFICATION_PLANNING: true`
2. `docs/EXECUTION-RESULT-VERIFICATION-ARCHITECTURE.md` exists and contains:
   - `FINAL_STATUS: M59_ARCHITECTURE_DEFINED`
   - `M59 architecture preserves the approved downstream task map through 59.14.`
3. `docs/EXECUTION-RESULT-VERIFICATION-INPUT-CONTRACT.md` exists and contains:
   - `FINAL_STATUS: M59_EXECUTION_RESULT_VERIFICATION_INPUT_CONTRACT_DEFINED`
4. `schemas/execution-result-verification-input.schema.json` exists and is valid JSON
5. `templates/execution-result-verification-input.md` exists
6. `docs/EXECUTION-RESULT-VERIFICATION-PRECONDITIONS-CONTRACT.md` exists and contains:
   - `FINAL_STATUS: M59_EXECUTION_RESULT_VERIFICATION_PRECONDITIONS_CONTRACT_DEFINED`
7. `schemas/execution-result-verification-preconditions.schema.json` exists and is valid JSON
8. `templates/execution-result-verification-preconditions.md` exists
9. `docs/GIT-DIFF-SCOPE-VERIFICATION-CONTRACT.md` exists and contains:
   - `FINAL_STATUS: M59_GIT_DIFF_SCOPE_VERIFICATION_CONTRACT_DEFINED`
10. `schemas/git-diff-scope-verification.schema.json` exists and is valid JSON
11. `templates/git-diff-scope-verification.md` exists
12. `docs/VALIDATION-EVIDENCE-CONTRACT.md` exists and contains:
    - `FINAL_STATUS: M59_VALIDATION_EVIDENCE_CONTRACT_DEFINED`
13. `schemas/validation-evidence.schema.json` exists and is valid JSON
14. `templates/validation-evidence.md` exists
15. `docs/EXECUTION-RESULT-VERIFICATION-RESULT-OUTPUT-CONTRACT.md` exists and contains:
    - `FINAL_STATUS: M59_EXECUTION_RESULT_VERIFICATION_RESULT_OUTPUT_CONTRACT_DEFINED`
16. `schemas/execution-result-verification-result-output.schema.json` exists and is valid JSON
17. `templates/execution-result-verification-result-output.md` exists
18. `reports/m58-completion-review.md` exists
19. No M59 downstream artifact already exists except the list of allowed artifacts.
20. No M60 cleanup or consolidation artifact already exists.
21. No unapproved downstream task IDs (such as tasks beyond 59.14) were introduced.

If preconditions fail, do not create the policy document and report:
`PRECONDITION_FAILED_M59_RESULT_OUTPUT_CONTRACT_NOT_READY`

## Position in M59

This policy represents task 59.7 of the M59 milestone. It consumes preconditions (59.3), git diff / scope verification (59.4), validation evidence (59.5), and verification result/output (59.6) to establish a structured verification decision. It is followed by the CLI implementation (59.8), positive fixtures (59.9.1), negative fixtures (59.9.2), fixture runner (59.10), integration summary (59.11), action review (59.12), evidence report (59.13), and completion review (59.14).

## Policy Role

The policy defines decision rules for execution result verification.
- It does not verify execution result.
- It does not approve task completion.
- It does not create approval.
- It does not authorize merge, push, or release.
- It does not mutate lifecycle state.
- It does not replace human review.
- It only defines decision rules for future execution result verification classification.

## Policy Decision Values

The policy defines exactly these decision values:
```text
M59_VERIFICATION_POLICY_VERIFIED
M59_VERIFICATION_POLICY_VERIFIED_WITH_WARNINGS
M59_VERIFICATION_POLICY_NOT_VERIFIED
M59_VERIFICATION_POLICY_BLOCKED
```

## Result Values

The policy maps to exactly these result values:
```text
EXECUTION_RESULT_VERIFIED
EXECUTION_RESULT_VERIFIED_WITH_WARNINGS
EXECUTION_RESULT_NOT_VERIFIED
EXECUTION_RESULT_BLOCKED
```

## Policy-to-Result Mapping

The policy defines exactly this mapping:
```text
M59_VERIFICATION_POLICY_VERIFIED -> EXECUTION_RESULT_VERIFIED
M59_VERIFICATION_POLICY_VERIFIED_WITH_WARNINGS -> EXECUTION_RESULT_VERIFIED_WITH_WARNINGS
M59_VERIFICATION_POLICY_NOT_VERIFIED -> EXECUTION_RESULT_NOT_VERIFIED
M59_VERIFICATION_POLICY_BLOCKED -> EXECUTION_RESULT_BLOCKED
```

## Exit Code Mapping

The policy defines exactly these exit codes:
```text
EXECUTION_RESULT_VERIFIED -> exit 0
EXECUTION_RESULT_VERIFIED_WITH_WARNINGS -> exit 0
EXECUTION_RESULT_NOT_VERIFIED -> exit 1
EXECUTION_RESULT_BLOCKED -> exit 2
```

Rules:
- exit 0 is not approval
- exit 0 is not task completion
- exit 0 does not authorize merge, push, or release
- exit 0 does not mutate lifecycle state
- exit 0 does not replace human review

## Priority Order

The policy defines this exact priority order:
```text
BLOCKED > NOT_VERIFIED > VERIFIED_WITH_WARNINGS > VERIFIED
```

Rules:
- Any blocker overrides warnings and verified signals.
- Any not-verified condition overrides verified signals.
- Warnings must be preserved and must downgrade clean verified to verified with warnings.
- Clean verified is allowed only when no blockers, no not-verified conditions, and no warnings exist.

## Upstream Authority Rule

Upstream verification layers are authoritative for safety classification.
59.6 result/output status is a consistency signal, not a self-authorizing signal.
59.6 result/output status must never upgrade blocked or not-verified upstream evidence to verified.
59.6 result/output status may only confirm, downgrade, or block the composite decision.

The upstream layers are:
- 59.3 preconditions
- 59.4 git diff and scope verification
- 59.5 validation evidence

Rules:
- If any upstream layer is BLOCKED, final policy decision must be `M59_VERIFICATION_POLICY_BLOCKED`.
- If any upstream layer is missing, unknown, malformed, contradictory, or unsafe, final policy decision must be `M59_VERIFICATION_POLICY_BLOCKED`.
- If any upstream layer is NOT_READY or NOT_CONFIRMED, final policy decision must not be `M59_VERIFICATION_POLICY_VERIFIED` or `M59_VERIFICATION_POLICY_VERIFIED_WITH_WARNINGS`.
- If 59.6 result/output claims `EXECUTION_RESULT_VERIFIED` while any upstream layer is BLOCKED, final policy decision must be `M59_VERIFICATION_POLICY_BLOCKED`.
- If 59.6 result/output claims `EXECUTION_RESULT_VERIFIED` while any upstream layer is NOT_READY or NOT_CONFIRMED, final policy decision must be `M59_VERIFICATION_POLICY_NOT_VERIFIED` only when:
  - no approval claim exists
  - no task-complete claim exists
  - no merge/push/release claim exists
  - no lifecycle mutation claim exists
  - no human-review-replacement claim exists
  - no missing required source artifact exists
  - no malformed artifact exists
  - no blocker list is non-empty
- If 59.6 result/output claims `EXECUTION_RESULT_VERIFIED` while upstream is NOT_READY or NOT_CONFIRMED and any unsafe, contradictory, authority-expanding, malformed, missing-artifact, or blocker condition exists, final policy decision must be `M59_VERIFICATION_POLICY_BLOCKED`.
- If 59.6 result/output is missing, unknown, malformed, or contradictory, final policy decision must be `M59_VERIFICATION_POLICY_BLOCKED`.
- The result/output consistency table is authoritative for resolving mixed upstream/output states.

## Result / Output Consistency Rule

The result/output artifact cannot self-authorize EXECUTION_RESULT_VERIFIED.
The result/output artifact is accepted only when it is consistent with upstream preconditions, diff/scope verification, and validation evidence.
The result/output consistency table is authoritative for resolving mixed upstream/output states.

Rules:
- Output cannot upgrade upstream severity.
- Output can only preserve or increase severity.
- Output inconsistency must be preserved as warning or blocker.
- Output authority claims must block.
- Output claiming VERIFIED against blocked upstream evidence must block.
- Output claiming VERIFIED against not-verified upstream evidence may result in NOT_VERIFIED only when the mismatch is non-authority-expanding and all required artifacts are present and well-formed.

Consistency Table:
```text
upstream BLOCKED + output VERIFIED -> BLOCKED
upstream BLOCKED + output BLOCKED -> BLOCKED
upstream BLOCKED + output NOT_VERIFIED -> BLOCKED
upstream BLOCKED + output missing/unknown/malformed -> BLOCKED

upstream NOT_VERIFIED + output VERIFIED -> NOT_VERIFIED only if no unsafe, authority-expanding, malformed, missing-artifact, or blocker condition exists
upstream NOT_VERIFIED + output VERIFIED -> BLOCKED if unsafe, authority-expanding, malformed, missing-artifact, contradictory, or blocker condition exists
upstream NOT_VERIFIED + output NOT_VERIFIED -> NOT_VERIFIED
upstream NOT_VERIFIED + output BLOCKED -> BLOCKED
upstream NOT_VERIFIED + output missing/unknown/malformed -> BLOCKED

upstream VERIFIED_WITH_WARNINGS + output VERIFIED -> VERIFIED_WITH_WARNINGS
upstream VERIFIED_WITH_WARNINGS + output VERIFIED_WITH_WARNINGS -> VERIFIED_WITH_WARNINGS
upstream VERIFIED_WITH_WARNINGS + output NOT_VERIFIED -> NOT_VERIFIED
upstream VERIFIED_WITH_WARNINGS + output BLOCKED -> BLOCKED
upstream VERIFIED_WITH_WARNINGS + output missing/unknown/malformed -> BLOCKED

upstream VERIFIED + output VERIFIED -> VERIFIED
upstream VERIFIED + output VERIFIED_WITH_WARNINGS -> VERIFIED_WITH_WARNINGS
upstream VERIFIED + output NOT_VERIFIED -> NOT_VERIFIED
upstream VERIFIED + output BLOCKED -> BLOCKED
upstream VERIFIED + output missing/unknown/malformed -> BLOCKED
```

## Preconditions Status Interpretation

The policy interprets 59.3 preconditions statuses as:
```text
EXECUTION_RESULT_PRECONDITIONS_READY -> may allow VERIFIED if all other layers are clean
EXECUTION_RESULT_PRECONDITIONS_READY_WITH_WARNINGS -> may allow VERIFIED_WITH_WARNINGS if no blockers/not-verified conditions exist
EXECUTION_RESULT_PRECONDITIONS_NOT_READY -> NOT_VERIFIED
EXECUTION_RESULT_PRECONDITIONS_BLOCKED -> BLOCKED
missing / unknown / malformed -> BLOCKED
```

Rules:
- Preconditions ready is not result verification.
- Preconditions ready does not approve task completion.
- Preconditions not ready must not become verified.
- Preconditions blocked must block.

## Git Diff and Scope Status Interpretation

The policy interprets 59.4 diff/scope statuses as:
```text
SCOPE_VERIFICATION_PASS -> may allow VERIFIED if all other layers are clean
SCOPE_VERIFICATION_PASS_WITH_WARNINGS -> may allow VERIFIED_WITH_WARNINGS if no blockers/not-verified conditions exist
SCOPE_VERIFICATION_NOT_READY -> NOT_VERIFIED
SCOPE_VERIFICATION_BLOCKED -> BLOCKED
missing / unknown / malformed -> BLOCKED
```

Rules:
- Scope pass is not task approval.
- Scope pass is not validation evidence confirmation.
- Out-of-scope changes must block or prevent verification according to severity.
- Protected path violation must block.
- Forbidden scope violation must block.

## Validation Evidence Status Interpretation

The policy interprets 59.5 validation evidence statuses as:
```text
VALIDATION_EVIDENCE_CONFIRMED -> may allow VERIFIED if all other layers are clean
VALIDATION_EVIDENCE_CONFIRMED_WITH_WARNINGS -> may allow VERIFIED_WITH_WARNINGS if no blockers/not-verified conditions exist
VALIDATION_EVIDENCE_NOT_CONFIRMED -> NOT_VERIFIED
VALIDATION_EVIDENCE_BLOCKED -> BLOCKED
missing / unknown / malformed -> BLOCKED
```

Rules:
- Validation evidence confirmed is not task approval.
- Exit code 0 is not approval.
- Claimed validation is not evidence.
- Missing evidence is not PASS.
- Wrong tests are not PASS.
- Stale evidence is not PASS.
- Failed validation/test evidence must block unless explicitly documented as non-blocking and preserved.

## Verification Result / Output Status Interpretation

The policy interprets 59.6 verification result/output statuses as:
```text
EXECUTION_RESULT_VERIFIED -> accepted only if upstream layers allow verified
EXECUTION_RESULT_VERIFIED_WITH_WARNINGS -> accepted only if upstream layers allow verified or verified-with-warnings
EXECUTION_RESULT_NOT_VERIFIED -> M59_VERIFICATION_POLICY_NOT_VERIFIED unless a blocker exists
EXECUTION_RESULT_BLOCKED -> M59_VERIFICATION_POLICY_BLOCKED
missing / unknown / malformed -> M59_VERIFICATION_POLICY_BLOCKED
```

Rules:
- 59.6 output is not authoritative over upstream layers.
- A result/output artifact cannot self-authorize verified status if upstream preconditions, diff/scope, or validation evidence are not clean enough.
- Output claiming verified despite blocked upstream evidence must block.
- Output claiming verified despite missing evidence must not pass.
- Output claiming task approval or task completion must block.
- Output claiming merge, push, release, or lifecycle mutation permission must block.

## Composite Decision Rules

### Verified
Use:
```text
M59_VERIFICATION_POLICY_VERIFIED
```
only when all conditions are true:
- preconditions status is `EXECUTION_RESULT_PRECONDITIONS_READY`
- diff/scope status is `SCOPE_VERIFICATION_PASS`
- validation evidence status is `VALIDATION_EVIDENCE_CONFIRMED`
- result/output status is `EXECUTION_RESULT_VERIFIED`
- no blockers exist across all layers
- no not-verified conditions exist across all layers
- no warnings exist across all layers
- no authority claims exist
- human review handoff remains required
- no premature M60 cleanup artifacts exist

### Verified with warnings
Use:
```text
M59_VERIFICATION_POLICY_VERIFIED_WITH_WARNINGS
```
only when all conditions are true:
- no blockers exist across all layers
- no not-verified conditions exist across all layers
- at least one warning exists
- all upstream layers are at ready/pass/confirmed level or ready/pass/confirmed-with-warnings level
- result/output status is `EXECUTION_RESULT_VERIFIED` or `EXECUTION_RESULT_VERIFIED_WITH_WARNINGS`
- result/output status is consistent with upstream layers
- human review handoff remains required
- no authority claims exist
- warnings are preserved for human review

Explicit prohibition:
```text
M59_VERIFICATION_POLICY_VERIFIED_WITH_WARNINGS is forbidden if any layer is BLOCKED.
M59_VERIFICATION_POLICY_VERIFIED_WITH_WARNINGS is forbidden if any layer is NOT_READY, NOT_CONFIRMED, NOT_VERIFIED, missing, unknown, malformed, contradictory, or unsafe.
```

### Not verified
Use:
```text
M59_VERIFICATION_POLICY_NOT_VERIFIED
```
when any non-blocking but verification-preventing condition exists, including:
- preconditions are not ready
- diff/scope is not ready
- validation evidence is not confirmed
- result/output says not verified
- declared changes do not match actual changes but no unsafe blocker is detected
- validation evidence is missing with explicit reason
- test evidence is missing with explicit reason
- evidence relevance is not confirmed
- evidence freshness is not confirmed
- human review handoff is not ready but not unsafe
- result/output claims verified while upstream is NOT_READY or NOT_CONFIRMED, but all required artifacts are present and well-formed, no blocker list is non-empty, and no approval, task-complete, merge, push, release, lifecycle mutation, or human-review-replacement claim exists

### Blocked
Use:
```text
M59_VERIFICATION_POLICY_BLOCKED
```
when any blocking condition exists, including:
- malformed input
- missing required source artifact
- unknown status
- contradictory upstream statuses
- blocker list is non-empty
- preconditions blocked
- diff/scope blocked
- validation evidence blocked
- result/output blocked
- output claims verified while upstream is blocked
- output claims verified while upstream is not ready or not confirmed and unsafe, contradictory, authority-expanding, malformed, missing-artifact, or blocker condition exists
- out-of-scope change detected as blocker
- forbidden file or directory touched
- protected path modified without checkpoint
- approval artifact detected
- lifecycle mutation detected
- merge, push, or release detected
- M60 cleanup artifact created prematurely
- result claimed verified despite missing evidence
- validation claimed passed but not run
- tests claimed passed but not run
- wrong tests treated as PASS
- stale evidence treated as PASS
- human review replacement claim exists
- task approval claim exists
- task completion claim exists

## False PASS Prevention Rules

The policy includes these exact rules:
```text
Claimed completion is not verification.
Claimed validation is not evidence.
Claimed tests are not evidence.
Missing evidence is not PASS.
Wrong tests are not PASS.
Stale evidence is not PASS.
Out-of-scope changes are not PASS.
Protected path changes are not PASS without explicit human checkpoint.
A clean exit code is not approval.
EXECUTION_RESULT_VERIFIED is not approval.
PASS is not lifecycle mutation.
Human review cannot be replaced by M59.
```

## Authority Claim Blocking Rules

The policy must block if any artifact claims:
```text
task is complete
task is approved
human review is replaced
merge is allowed
push is allowed
release is allowed
lifecycle state may be mutated
M60 cleanup has started
approval has been created by M59
```

Allowed bounded wording:
`EXECUTION_RESULT_VERIFIED` may appear only as M59 verification result status and must always be separated from approval, completion, merge, push, release, and lifecycle mutation.

## Warning Semantics

Warnings capture minor compliance anomalies or metadata issues that do not threaten safety or violate integrity boundaries.
- Warnings do not block verification.
- Warnings downgrade a clean verified status to verified-with-warnings.
- Warnings are preserved in a warnings list within the verification result.
- Warnings must be presented to the human reviewer for evaluation.

## Blocker Semantics

Blockers capture critical security, safety, or functional failures.
- Any non-empty blocker list forces `M59_VERIFICATION_POLICY_BLOCKED`.
- Blockers override all warning or verified states.
- Blockers prevent exit 0, forcing exit 2.

## Human Review Handoff Rules

The policy defines:
- human review is required even when result is verified
- verified result may be handed off to human review
- verified with warnings may be handed off to human review with warnings preserved
- not verified must not be treated as human approval ready
- blocked must not be handed off as successful result
- human review handoff is not approval itself

## M60 Cleanup Planning Boundary

The policy defines:
```text
M59 completion may allow M60 cleanup planning only.
M59 completion does not start M60.
M59 completion does not change safety semantics.
M59 completion does not approve task completion.
M59 completion does not authorize merge, push, or release.
M59 completion does not mutate lifecycle state.
```

## Non-Authority Rules

The policy includes these exact statements:
```text
M59 policy does not verify execution result.
M59 policy does not approve task completion.
M59 policy does not create approval.
M59 policy does not authorize merge, push, or release.
M59 policy does not mutate lifecycle state.
M59 policy does not replace human review.
M59 policy only defines decision rules for future execution result verification classification.
```

## Relationship to 59.8 CLI

The verification CLI (59.8) acts as the operational executor of this policy. It implements the rules defined here to dynamically evaluate preconditions, diff compliance, and validation logs, exporting them to the result schema.

## Relationship to 59.9 Fixtures

Positive and negative fixtures (59.9.1 and 59.9.2) serve as concrete test scenarios representing different combinations of upstream states and authority claims to validate policy enforcement.

## Relationship to 59.10 Fixture Runner

The fixture runner (59.10) automates the execution of 59.8 CLI against 59.9 fixtures to assert that the implementation complies with all rules established in this policy.

## Forbidden Claims

The policy must not claim:
- execution result has been verified by this task
- task is complete
- task is approved
- human review is replaced
- M60 cleanup has started
- commit is allowed
- push is allowed
- merge is allowed
- release is allowed
- lifecycle state may be mutated

## Final Policy Status

```text
FINAL_STATUS: M59_EXECUTION_RESULT_VERIFICATION_POLICY_DEFINED
```

This status means only that the execution result verification policy exists.

It does not mean execution result was verified.

It does not mean task completion was approved.

It does not mean human review was completed.
