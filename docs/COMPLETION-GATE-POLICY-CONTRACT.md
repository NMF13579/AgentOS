# Completion Gate Policy Contract

## 1. Purpose
This document defines the M67 completion gate policy contract.

Completion gate is a separate explicit process.
Completion gate cannot be inferred from M66 PASS.
Completion gate cannot be inferred from M67 PASS.
Completion gate policy is not approval by itself.
Completion gate policy does not complete tasks by itself.
Human review remains required.

## 2. Scope
67.2 defines:
- completion gate policy model
- required policy fields
- required human review status
- validation result references
- completion request boundary
- allowed policy decisions
- blocked policy decisions
- non-authority boundary
- relationship to M66/M67/M68

67.2 does not:
- implement a completion gate
- mutate lifecycle state
- approve completion
- create false PASS checker
- create fixtures
- create completion gate hardening contract
- create integration/action/evidence/completion reports
- start M68

## 3. Completion Gate Definition
Completion gate is an explicit policy-controlled lifecycle checkpoint that determines whether a task may be considered eligible for completion review or lifecycle completion processing.

Completion gate is not inferred.
Completion gate is not automatically passed.
Completion gate requires explicit inputs.
Completion gate requires explicit human review status.
Completion gate requires absence of blockers.
Completion gate remains separate from validation PASS.

## 4. Relationship to Validation PASS
M66_UNIFIED_RUN_PASS is a validation signal.
M66_UNIFIED_RUN_PASS_WITH_WARNINGS is a validation signal with warnings.
M66_UNIFIED_RUN_NOT_ENOUGH_EVIDENCE is inconclusive.
M66_UNIFIED_RUN_BLOCKED is blocked.

M66 PASS alone cannot complete a task.
M66 PASS_WITH_WARNINGS alone cannot complete a task.
M66 NOT_ENOUGH_EVIDENCE cannot complete a task.
M66 BLOCKED cannot complete a task.

M67 PASS alone cannot complete a task.
M67 PASS_WITH_WARNINGS alone cannot complete a task.
M67 NOT_ENOUGH_EVIDENCE cannot complete a task.
M67 BLOCKED cannot complete a task.

## 5. Required Policy Fields
Minimum future policy package fields:
- task_id
- task_brief_path
- validation_result_reference
- runner_evidence_reference
- acceptance_check_reference
- false_pass_check_reference
- human_review_required
- human_review_status
- completion_gate_requested
- completion_gate_allowed
- completion_gate_result
- warnings
- blockers
- non_authority_boundary

## 6. Field Semantics
task_id:
Non-empty task identifier.

task_brief_path:
Reference to task brief.

validation_result_reference:
Reference to M66 unified runner result.

runner_evidence_reference:
Reference to M66 evidence report or runner output evidence.

acceptance_check_reference:
Reference to M65 acceptance criteria checker output or acceptance evidence.

false_pass_check_reference:
Reference to future M67 false PASS checker result.

human_review_required:
Must be true.

human_review_status:
Explicit status of human review.

completion_gate_requested:
Whether completion gate evaluation was explicitly requested.

completion_gate_allowed:
Whether policy allows completion gate to proceed.

completion_gate_result:
Final gate policy result.

warnings:
Non-blocking concerns that must remain visible.

blockers:
Blocking concerns that prevent completion gate pass.

non_authority_boundary:
Boundary statements preserving non-approval semantics.

## 7. Human Review Status
Allowed human_review_status values:
- not_requested
- pending
- reviewed
- approved_by_human
- rejected_by_human
- blocked

Rules:
human_review_required must be true.
human_review_status missing → BLOCKED.
human_review_status pending → BLOCKED for completion.
human_review_status not_requested → BLOCKED for completion.
human_review_status blocked → BLOCKED.
human_review_status rejected_by_human → BLOCKED.
human_review_status approved_by_human may allow policy to proceed only if all other required checks pass.

Important:
approved_by_human does not mean the automated policy itself approved.
It means human approval evidence exists and may be considered by the policy.

## 8. Completion Gate Request Boundary
completion_gate_requested must be explicit.

Rules:
completion_gate_requested false → no gate pass.
completion_gate_requested missing → BLOCKED.
completion_gate_requested true without required references → BLOCKED.
completion_gate_requested true without human_review_status → BLOCKED.

Completion gate must not be inferred from:
- M66 PASS
- M67 PASS
- evidence report complete
- completion review complete
- CI pass
- fixture pass
- dashboard green status

## 9. Completion Gate Allowed Boundary
completion_gate_allowed may be true only if:
- completion_gate_requested is true
- human_review_required is true
- human_review_status is approved_by_human
- M66 validation reference is PASS or PASS_WITH_WARNINGS according to policy
- M67 false PASS check reference is PASS or PASS_WITH_WARNINGS according to policy
- no BLOCKED result exists
- no NOT_ENOUGH_EVIDENCE result exists where required evidence is needed
- blockers is empty
- required artifacts exist
- forbidden claims are absent

completion_gate_allowed must be false if:
- human review is missing, pending, blocked, or rejected
- M66 result is BLOCKED
- M66 result is NOT_ENOUGH_EVIDENCE
- M67 result is BLOCKED
- M67 result is NOT_ENOUGH_EVIDENCE
- blockers is non-empty
- forbidden approval/completion claims exist
- required references are missing
- completion_gate_requested is false

## 10. Completion Gate Result Values
Future policy result values:
- COMPLETION_GATE_PASS
- COMPLETION_GATE_PASS_WITH_WARNINGS
- COMPLETION_GATE_BLOCKED
- COMPLETION_GATE_NOT_ENOUGH_EVIDENCE
- COMPLETION_GATE_NOT_REQUESTED

Rules:
COMPLETION_GATE_PASS requires explicit human approval evidence and no blockers.
COMPLETION_GATE_PASS_WITH_WARNINGS requires explicit human approval evidence, no blockers, and visible warnings.
COMPLETION_GATE_BLOCKED means gate cannot pass.
COMPLETION_GATE_NOT_ENOUGH_EVIDENCE means required evidence is missing or inconclusive.
COMPLETION_GATE_NOT_REQUESTED means no explicit completion gate request was made.

## 11. Forbidden Gate Inference
No completion from M66 PASS alone.
No completion from M67 PASS alone.
No completion from evidence report alone.
No completion from completion review alone.
No completion from fixture PASS alone.
No completion from CI PASS alone.
No completion from dashboard green status.
No completion from agent final report alone.

## 12. Required Blocking Conditions
Completion gate must block if:
- human_review_required is false
- human_review_status is missing
- human_review_status is pending
- human_review_status is not_requested
- human_review_status is rejected_by_human
- human_review_status is blocked
- completion_gate_requested is false
- completion_gate_requested is missing
- M66 result is BLOCKED
- M66 result is NOT_ENOUGH_EVIDENCE
- M67 result is BLOCKED
- M67 result is NOT_ENOUGH_EVIDENCE
- required reference is missing
- blockers is non-empty
- forbidden approval claim exists
- forbidden completion claim exists
- completion gate pass is claimed without policy result
- M68 auto-start claim exists

## 13. Warnings
Warnings may include:
- M66 PASS_WITH_WARNINGS
- M67 PASS_WITH_WARNINGS
- non-critical documentation warnings
- carried warnings from previous milestones
- optional evidence limitations

Warnings must remain visible.
Warnings must not be silently converted into clean PASS.
Warnings do not override blockers.

## 14. Non-Authority Boundary
Completion gate policy contract is not approval.
Completion gate policy contract does not complete tasks.
Completion gate policy contract does not mutate lifecycle state.
Completion gate policy contract does not authorize merge, push, release, or deployment.
Completion gate policy contract does not start M68.
Human review remains required.

## 15. Relationship to M67 False PASS Checker
67.5 false PASS checker will check whether validation signals are being overclaimed.
67.5 checker is not the completion gate.
67.5 checker does not approve completion.
67.5 checker result may become one input to future completion gate policy.

## 16. Relationship to 67.7 Hardening Contract
67.2 defines the policy contract.
67.7 will harden completion gate behavior.
67.7 must not implement automatic lifecycle completion.
67.7 must preserve explicit gate request, human review, and blocker rules.

## 17. Relationship to M68
M67 does not define M68.
M67 does not start M68.
ready_for_m68 later means roadmap readiness only.
ready_for_m68 must not assume M68 content.
M68 requires a separate explicit milestone plan and task chain.

## 18. Example Safe Policy Interpretation
M66 result: M66_UNIFIED_RUN_PASS
M67 false PASS check: M67_FALSE_PASS_CHECK_PASS
human_review_required: true
human_review_status: pending
completion_gate_requested: true

Result:
COMPLETION_GATE_BLOCKED

Reason:
Human review is pending. Validation PASS does not complete task.

## 19. Example Allowed Policy Interpretation
M66 result: M66_UNIFIED_RUN_PASS
M67 false PASS check: M67_FALSE_PASS_CHECK_PASS
human_review_required: true
human_review_status: approved_by_human
completion_gate_requested: true
blockers: []

Result:
COMPLETION_GATE_PASS

Boundary:
This still does not mean the policy document itself approved the task.
It means a future completion gate policy could allow completion processing if explicitly invoked and all conditions are satisfied.

## 20. Example Forbidden Policy Interpretation
M66 result: M66_UNIFIED_RUN_PASS
human_review_status: pending
completion_gate_requested: false
agent claim: "task completed"

Result:
COMPLETION_GATE_BLOCKED

Reason:
Completion was inferred from validation PASS and human review was not approved.

## 21. Later Task Responsibilities
67.3 defines false PASS decision semantics.
67.4 defines false PASS claim boundary.
67.5 implements false PASS checker.
67.6 creates false PASS fixtures.
67.7 defines completion gate hardening contract.
67.8 validates integration.
67.9 reviews actions.
67.10 collects evidence.
67.11 closes M67.

## 22. Final Status
FINAL_STATUS: M67_COMPLETION_GATE_POLICY_DEFINED_WITH_WARNINGS
