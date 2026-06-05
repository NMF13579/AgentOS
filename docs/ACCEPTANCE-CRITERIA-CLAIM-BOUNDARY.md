# Acceptance Criteria Claim Boundary

## 1. Purpose
This document defines the M65 claim boundary.

M65 acceptance criteria results are validation signals.
M65 acceptance criteria results are not approval.
M65 acceptance criteria results are not task completion.
M65 acceptance criteria results are not production readiness.
Human review remains required.

## 2. Scope
65.4 defines:
1. forbidden claims
2. allowed claims
3. safe boundary language
4. non-authority statements
5. claim scanning expectations for the future checker
6. decision mapping for forbidden claims
7. safe contexts where forbidden phrases may appear as examples

65.4 does not:
1. implement checker logic
2. create checker script
3. create fixtures
4. create unified runner
5. create false PASS suite
6. integrate completion gate
7. start M66
8. start M67

## 3. Core Boundary
Acceptance criteria appear satisfied at M65 level.
This is not approval.
This does not complete the task.
Human review remains required.

M65 checker must not infer full task meaning from free-form Markdown.
M65 checker must operate on structured acceptance criteria package.

## 4. Non-Authority Principle
1. M65 checker output is a validation signal.
2. M65 checker output is not authority to approve.
3. M65 checker output is not authority to merge.
4. M65 checker output is not authority to push.
5. M65 checker output is not authority to release.
6. M65 checker output is not authority to mark production ready.
7. M65 checker output is not authority to skip human review.
8. Human review remains above M65 results.

PASS means structured required criteria appear satisfied at M65 level.
PASS does not mean the task is approved.
PASS does not mean the task is complete.
PASS does not mean the system may proceed without human review.

## 5. Forbidden Claims
Exact forbidden claims:
- task approved
- task accepted by system
- completion approved
- human review not required
- merge authorized
- push authorized
- release authorized
- production ready
- ready for production
- completion gate passed
- M66 started automatically
- M67 started automatically

Equivalent forbidden claim categories:
1. approval claims
2. acceptance-as-approval claims
3. completion claims
4. human-review-bypass claims
5. merge authorization claims
6. push authorization claims
7. release authorization claims
8. production readiness claims
9. completion gate claims
10. automatic next-milestone start claims

## 6. Forbidden Field Names
Forbidden or suspicious package/output field names:
- approved
- task_approved
- task_complete
- task_completed
- accepted_by_system
- completion_approved
- completion_authorized
- completion_gate_passed
- human_review_not_required
- skip_human_review
- merge_authorized
- push_authorized
- release_authorized
- production_ready
- ready_for_production
- m66_started_automatically
- m67_started_automatically

These field names must not be accepted as authority.
If they appear as operative package fields, future checker behavior should block.
If they appear only inside this claim-boundary document as examples, they are safe context.

## 7. Allowed Claims
Allowed M65-level statements:
1. Acceptance criteria appear satisfied at M65 level.
2. Required criteria appear satisfied based on structured package data.
3. Optional criteria produced warnings.
4. Structured package lacks enough evidence for optional or ambiguous criteria.
5. Required criterion failed.
6. Required artifact is missing.
7. Required validation failed.
8. Human review remains required.
9. M65 result is a validation signal.
10. M65 does not approve or complete the task.

The phrase “appear satisfied” is preferred over “are satisfied” when describing automated M65 outcomes.

## 8. Disallowed Wording Patterns
1. “Task is approved”
2. “Task is accepted”
3. “Task is complete”
4. “Completion is approved”
5. “Ready to merge”
6. “Ready to push”
7. “Ready to release”
8. “Production ready”
9. “Human review is no longer required”
10. “Completion gate passed”
11. “M66 started”
12. “M67 started”
13. “No human review needed”
14. “Automatically approved”
15. “System accepted the task”

## 9. Safe Boundary Wording
1. “M65_ACCEPTANCE_CHECK_PASS indicates that structured required criteria appear satisfied at M65 level.”
2. “This result is not approval.”
3. “This result does not complete the task.”
4. “Human review remains required.”
5. “M65 readiness is roadmap readiness only.”
6. “M65 does not authorize merge, push, release, or production deployment.”
7. “M65 does not start M66 or M67 automatically.”

## 10. Claim Detection Expectations for Future Checker
The future checker in 65.5 should:
1. scan relevant package string values for forbidden claims
2. scan checker-produced output strings for forbidden claims
3. treat operative package claims as BLOCKED
4. treat forbidden claims inside safe documentation examples as safe context
5. not treat object keys alone as full natural-language claims unless they are forbidden operative fields
6. not treat non_authority_boundary safe wording as a forbidden claim
7. not treat this document’s forbidden examples as violations
8. recursively inspect nested string values in package content where practical
9. produce M65_ACCEPTANCE_CHECK_BLOCKED when forbidden operative claims are found

Forbidden claim detection should focus on operative package content and checker output, not on safe policy examples.

## 11. Safe Contexts
Safe contexts where forbidden phrases may appear:
1. this claim boundary document
2. forbidden examples in docs
3. fixture descriptions explicitly testing forbidden claims
4. README sections explaining forbidden claims
5. non_authority_boundary statements that negate approval/completion
6. decision semantics examples that map forbidden claims to BLOCKED

The same phrase can be safe in policy context and forbidden in operative result context.

Example:
“production ready” is safe when listed as a forbidden claim.
“production ready” is forbidden when asserted as a result of the task.

## 12. Decision Mapping
Any operative forbidden approval, acceptance-as-approval, completion, human-review-bypass, merge, push, release, production-ready, completion-gate, M66 auto-start, or M67 auto-start claim must map to:

M65_ACCEPTANCE_CHECK_BLOCKED

Forbidden claims must not be downgraded to warnings.
Forbidden claims must not produce PASS_WITH_WARNINGS.
Forbidden claims must never produce clean PASS.

## 13. Human Review Boundary
human_review_required must remain true.
human_review_required false is a blocker.
Human review remains required even after M65_ACCEPTANCE_CHECK_PASS.
Human review remains required even after M65_ACCEPTANCE_CHECK_PASS_WITH_WARNINGS.
Human review remains required after M65_ACCEPTANCE_CHECK_NOT_ENOUGH_EVIDENCE.
Human review remains required after M65_ACCEPTANCE_CHECK_BLOCKED.

## 14. Relationship to M63 and M64
1. M63 formalized task validation contract boundaries.
2. M64 formalized agent output evidence boundaries.
3. M65 extends boundary control to acceptance criteria checking.
4. M65 must preserve M63 and M64 non-approval principles.
5. M65 must not weaken M64 evidence claim boundaries.

## 15. Relationship to M66 and M67
1. M66 will later create a unified runner.
2. M67 will later harden false PASS resistance and completion gate boundaries.
3. M65 must not create M66 unified runner artifacts.
4. M65 must not create M67 false PASS suite artifacts.
5. M65 must not integrate a completion gate.
6. M65 must not auto-start M66 or M67.

## 16. Failure Modes
1. PASS is interpreted as approval
2. PASS_WITH_WARNINGS is interpreted as safe to merge
3. NOT_ENOUGH_EVIDENCE is treated as non-blocking success
4. BLOCKED is softened into warning
5. manual-review-required criteria are treated as automated PASS
6. production-ready wording appears in checker output
7. completion-gate wording appears before M67
8. M65 starts absorbing M66/M67 scope
9. checker trusts agent self-claims
10. non_authority_boundary is omitted or weakened

## 17. Relationship to Later Tasks
65.5 implements the read-only checker using this claim boundary.
65.6 creates fixtures for forbidden and safe claim cases.
65.7 validates integration.
65.8 reviews actions.
65.9 collects evidence.
65.10 closes M65.

## 18. Final Status
FINAL_STATUS: M65_ACCEPTANCE_CLAIM_BOUNDARY_DEFINED_WITH_WARNINGS
