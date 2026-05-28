# M66 Unified Runner Claim Boundary

## 1. Purpose

This document defines the claim boundary for M66 Unified Runner.

M66 result is a validation signal.
M66 result is not approval.
M66 result does not complete the task.
M66 result does not authorize merge, push, release, or production deployment.
M66 result does not create completion gate.
M66 result does not start M67.
Human review remains required.

## 2. Scope

66.4 defines:
- forbidden claims
- forbidden output fields
- allowed wording
- safe result language
- unsafe result language
- boundaries for runner JSON output
- boundaries for runner documentation
- boundaries for fixtures
- boundaries for integration/action/evidence/completion reports
- relationship to M67

66.4 does not:
- implement runner
- modify schema
- modify aggregation semantics
- create fixtures
- create integration summary
- create action review
- create evidence report
- create completion review
- create M67 artifacts
- integrate completion gate

## 3. Core Non-Authority Principle

M66 is a validation runner, not an approver.
M66 validation result is a signal, not a decision to accept work.
M66 validation result does not complete a task.
M66 validation result does not waive human review.
Human review remains required.

## 4. Forbidden Claims

- task approved
- task accepted by system
- task completed
- completion approved
- human review not required
- human review waived
- merge authorized
- push authorized
- release authorized
- production ready
- ready for production
- completion gate passed
- M67 started automatically
- false PASS resistance activated automatically

Any operative claim equivalent to these must be blocked by future runner validation or downstream review.

## 5. Forbidden Output Fields

- approved
- task_approved
- task_accepted
- task_complete
- task_completed
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
- m67_started_automatically
- false_pass_resistance_activated

If such fields appear as operative fields, future validation must block.

## 6. Allowed Result Language

Unified runner validation passed at M66 level.
Unified runner validation passed with warnings at M66 level.
Unified runner validation was blocked at M66 level.
Unified runner validation did not have enough evidence at M66 level.
This is not approval.
This does not complete the task.
Human review remains required.

## 7. Unsafe Result Language

Task is approved.
Task is accepted.
Task is complete.
Completion is approved.
This can be merged.
This can be pushed.
This can be released.
This is production ready.
Completion gate passed.
M67 can start automatically.
Human review is not needed.

These phrases must not be used as M66 result claims.

## 8. Runner JSON Output Boundary

M66 runner JSON output may include:
- result
- task_id
- execution_mode
- effective_execution_mode
- human_review_required
- checker_results
- aggregation
- findings
- warnings
- blockers
- not_enough_evidence
- non_authority_boundary
- exit_code

M66 runner JSON output must include or preserve:
human_review_required: true
non_authority_boundary

The non_authority_boundary should include:
Unified runner result is not approval.
Unified runner result does not complete the task.
Human review remains required.

M66 runner JSON output must not include forbidden operative fields from Section 5.

## 9. Checker Result Boundary

M66 may report child checker results.
M66 must not convert child checker PASS into approval.

Child checker PASS is a validation signal.
Child checker PASS_WITH_WARNINGS is a validation signal with warnings.
Child checker BLOCKED is a validation blocker.
Child checker NOT_ENOUGH_EVIDENCE is an inconclusive validation signal.
None of these are approval.

## 10. PASS Boundary

M66_UNIFIED_RUN_PASS means all required checker validations passed at M66 runner level.
M66_UNIFIED_RUN_PASS does not mean task approved.
M66_UNIFIED_RUN_PASS does not mean task completed.
M66_UNIFIED_RUN_PASS does not authorize merge, push, release, or deployment.
M66_UNIFIED_RUN_PASS does not waive human review.

## 11. PASS_WITH_WARNINGS Boundary

M66_UNIFIED_RUN_PASS_WITH_WARNINGS means required validation did not block but warnings exist.
Warnings must remain visible.
Warnings must not be silently converted into clean PASS.
PASS_WITH_WARNINGS is not approval.
Human review remains required.

## 12. BLOCKED Boundary

M66_UNIFIED_RUN_BLOCKED means the unified validation runner blocked or could not validate safely.
BLOCKED is not proof of task failure.
BLOCKED means the validation pipeline cannot honestly continue as passed.
Human review remains required.

## 13. NOT_ENOUGH_EVIDENCE Boundary

M66_UNIFIED_RUN_NOT_ENOUGH_EVIDENCE means automated validation did not have enough executable or structured evidence.
NOT_ENOUGH_EVIDENCE is not PASS.
NOT_ENOUGH_EVIDENCE is not approval.
NOT_ENOUGH_EVIDENCE must not allow pipeline continuation as if validation passed.
Human review remains required.

## 14. no_execute Boundary

No execution means no validation proof.
No validation proof means no PASS.

no_execute cannot produce M66_UNIFIED_RUN_PASS.
no_execute cannot produce M66_UNIFIED_RUN_PASS_WITH_WARNINGS.
no_execute can produce only M66_UNIFIED_RUN_NOT_ENOUGH_EVIDENCE or M66_UNIFIED_RUN_BLOCKED.

## 15. Mock-Execution Boundary

mock-execution fixtures validate runner mechanics only.
mock-execution fixtures do not validate the full M63/M64/M65 pipeline.
mock-execution fixtures do not replace real execution fixtures.
mock-only validation cannot support M66 completion.
production runner inputs must not execute mock checkers.

## 16. Runtime Unavailable Boundary

If Python subprocess execution environment is unavailable, results must not be inferred.
If fixture execution cannot run, results must not be inferred.
If actual exit codes are unavailable, exit codes must not be guessed.
Unavailable executable evidence must block integration/evidence/completion stages where execution is required.

## 17. Runner Documentation Boundary

Future runner documentation must preserve:
M66 runner is not approval.
M66 runner does not complete tasks.
M66 runner does not create completion gate.
M66 runner does not start M67.
Human review remains required.

## 18. Fixture Boundary

M66 fixtures may test:
- structure validation
- mock-execution mechanics
- real execution pipeline

M66 fixtures must not claim:
- approval
- task completion
- production readiness
- completion gate pass
- automatic M67 start

## 19. Integration / Action / Evidence / Completion Report Boundary

Later M66 reports may state:
M66 integration passed
M66 action review passed
M66 evidence report complete
M66 completion review complete

But must not state:
task approved
task completed
completion approved
completion gate passed
M67 started automatically

## 20. Relationship to M67

M67 will handle false PASS resistance and completion gate hardening.
M66 must not create false PASS resistance suite.
M66 must not create completion gate.
M66 must not start M67 automatically.
ready_for_m67 later means roadmap readiness only.

## 21. Claim Detection Guidance

Future runner/checks should recursively inspect operative string values for forbidden claims.

Guidance:
- safe non-authority boundary statements must not trigger forbidden claim failure
- forbidden examples inside documentation sections are safe context
- operative result fields are not safe context
- ambiguous approval-like claims should block or require review
- object keys listed as forbidden operative fields must block when present in runner output/input where prohibited

## 22. Allowed Boundary Statements

This is not approval.
This does not complete the task.
Human review remains required.
Unified runner result is not approval.
Unified runner result does not complete the task.
Unified runner result does not authorize merge, push, release, or production deployment.
Unified runner result does not start M67.

## 23. Final Status

FINAL_STATUS: M66_UNIFIED_RUNNER_CLAIM_BOUNDARY_DEFINED_WITH_WARNINGS
