# False PASS Resistance Semantics

## 1. Purpose
This document defines when checker output is considered false PASS.

It explains which patterns must be blocked and how severity mapping works.
It follows the false PASS resistance architecture and preserves the human review boundary.

## 2. Scope
This document defines:
- when checker output counts as false PASS
- which patterns are blocked
- which patterns are warning-level only
- how severity mapping works
- how safe wording is preserved
- how ambiguous wording is handled

This document does not:
- define the checker implementation
- define fixtures
- define the completion gate policy
- define the claim boundary
- create integration, action, evidence, or completion reports
- start M68

## 3. What Counts as False PASS
Checker output counts as false PASS when it gives stronger authority than the validation actually provides.

Examples of false PASS:
- validation PASS treated as approval
- validation PASS treated as task completion
- validation PASS treated as completion gate pass
- validation PASS treated as merge authorization
- validation PASS treated as release authorization
- validation PASS treated as production readiness
- validation PASS used to waive human review
- validation evidence used as lifecycle mutation

False PASS can appear in:
- runner output
- evidence summary
- completion review
- agent final report
- status fields
- dashboard text
- automation output

## 4. Blocked Patterns
The following patterns must be blocked when they appear as operative claims:
- task approved
- task accepted
- approved by system
- validation approved task
- task completed
- task complete
- completion approved
- completion authorized
- completion gate passed
- gate passed
- human review not required
- human review waived
- skip human review
- merge authorized
- push authorized
- release authorized
- production ready
- ready for production
- lifecycle mutated
- completion state applied
- M68 started automatically

Blocked patterns also include:
- any claim that M66 PASS alone completes a task
- any claim that M67 PASS alone completes a task
- any claim that completion is inferred from validation
- any claim that human review is replaced by checker output

## 5. Severity Mapping
Severity mapping works like this:

- `PASS` means no false PASS was found.
- `PASS_WITH_WARNINGS` means no blocked claim was found, but risky or ambiguous wording exists.
- `BLOCKED` means a false PASS claim or unsafe operative claim was found.
- `NOT_ENOUGH_EVIDENCE` means the checker cannot decide safely from the available structured input.

Priority order:
1. `BLOCKED`
2. `NOT_ENOUGH_EVIDENCE`
3. `PASS_WITH_WARNINGS`
4. `PASS`

Higher severity always wins.

## 6. Why Something Is Blocked
Something is blocked when it is a real operative claim, not just an example or description.

Blocked if the text:
- claims approval
- claims completion
- claims completion gate pass
- claims human review is waived
- claims lifecycle mutation
- claims M68 auto-start
- claims merge, push, release, or deployment authorization

Blocked if the structured output contains unsafe operative fields such as:
- `approved`
- `task_approved`
- `task_completed`
- `completion_gate_passed`
- `human_review_not_required`
- `merge_authorized`
- `production_ready`
- `m68_started_automatically`

## 7. When Warnings Are Allowed
Warnings are allowed when wording is not clearly false PASS, but still needs attention.

Examples:
- extra explanatory text around a safe PASS
- documentation examples that are clearly marked as examples
- carried warnings from earlier milestones
- non-critical references that are missing but not required

Warnings must stay visible.
Warnings must not be turned into a clean PASS without review.

## 8. Safe Wording
Safe wording includes:
- This is not approval.
- This does not complete the task.
- Human review remains required.
- Validation PASS is not approval.
- Validation PASS is not completion.
- Completion gate remains separate.
- M67 does not start M68.

Safe wording must not be treated as false PASS.

## 9. Ambiguous Wording
Ambiguous wording is handled conservatively.

If the text could reasonably be read as approval or completion, the checker should return:
- `BLOCKED` when the wording is clearly unsafe or operative
- `NOT_ENOUGH_EVIDENCE` when the checker cannot safely decide

Ambiguous wording includes:
- "approved" without context
- "completed" without clear boundary
- "ready to ship" without policy evidence
- "gate passed" without explicit gate evidence

## 10. Relationship to False PASS Resistance Architecture
The architecture explains why M67 exists.
This semantics document explains how the checker should classify output.

Architecture says what M67 protects.
Semantics says what M67 must block or warn on.

## 11. Relationship to Human Review
Human review remains required.
Human review cannot be replaced by:
- validation PASS
- checker output
- fixture PASS
- evidence report
- dashboard text

## 12. Final Status
FINAL_STATUS: M67_FALSE_PASS_RESISTANCE_SEMANTICS_DEFINED_WITH_WARNINGS
