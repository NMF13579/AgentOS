# False PASS Resistance Claim Boundary

## 1. Purpose
This document defines the forbidden claim boundary for both M67 mechanisms:
- false PASS resistance
- completion gate policy

It explains which claims must block, which wording is safe, and how the boundary protects human review.

## 2. Scope
This document defines:
- forbidden approval claims
- forbidden completion claims
- forbidden completion gate claims
- forbidden human review waiver claims
- forbidden lifecycle mutation claims
- forbidden merge/push/release/deployment claims
- forbidden M68 auto-start claims
- forbidden operative fields
- safe wording
- safe context vs operative context
- recursive string scanning guidance
- boundary rules for checker output and policy output

This document does not:
- implement a checker
- define checker CLI behavior
- define fixtures
- implement completion gate policy
- implement lifecycle mutation
- create integration, action, evidence, or completion reports
- start M68

## 3. Core Boundary
Validation PASS is not approval.
Validation PASS is not completion.
Validation PASS is not completion gate pass.
Validation PASS is not lifecycle mutation.
Runner proof is evidence, not authorization.
Completion requires explicit completion gate process.
Human review remains required.

## 4. Shared Forbidden Claims
The following claims must block in any operative output for either mechanism:
- task approved
- task accepted
- approved by system
- validation approved task
- task completed
- task complete
- completion approved
- completion authorized
- completion accepted
- completion gate passed
- gate passed
- gate approved
- gate authorized
- human review not required
- human review waived
- skip human review
- checker replaces human review
- runner replaces human review
- evidence report replaces human review
- merge authorized
- push authorized
- release authorized
- deployment authorized
- production ready
- ready for production
- lifecycle mutated
- completion state applied
- M68 started automatically

## 5. False PASS Resistance Claim Boundary
For false PASS resistance output, the following are forbidden operative claims:
- validation PASS treated as approval
- validation PASS treated as task completion
- validation PASS treated as completion gate pass
- validation PASS treated as merge authorization
- validation PASS treated as release authorization
- validation PASS treated as production readiness
- validation PASS used to waive human review
- validation evidence used as lifecycle mutation
- M66 PASS alone completes a task
- M67 PASS alone completes a task

The false PASS resistance result must not say:
- task approved
- task completed
- completion gate passed
- human review waived
- production ready
- M68 started automatically

## 6. Completion Gate Policy Claim Boundary
For completion gate policy output, the following are forbidden operative claims unless explicit policy evidence exists and the policy result allows them:
- completion gate passed
- completion gate approved
- completion gate allowed
- completion gate authorized
- gate result pass
- ready to complete automatically
- completion gate satisfied by M66 PASS
- completion gate satisfied by M67 PASS
- completion gate inferred from validation

The completion gate policy result must not say:
- task approved
- task completed
- lifecycle mutated
- merge authorized
- push authorized
- release authorized
- production ready
- M68 started automatically

## 7. Hidden False PASS in Operative Fields
Forbidden operative fields must block when they appear in machine-readable output:
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

## 8. Safe Wording
The following wording is safe and must not be treated as forbidden claim:
- This is not approval.
- This does not complete the task.
- Human review remains required.
- Validation PASS is not approval.
- Validation PASS is not completion.
- Completion gate remains separate.
- Completion gate was not executed.
- M67 does not start M68.
- ready_for_m68 is roadmap readiness only.

## 9. Safe Context vs Operative Context
Safe context includes:
- documentation examples clearly marked as examples
- negative fixture descriptions
- policy explanations
- non-authority boundary statements

Operative context includes:
- final result fields
- summary fields
- decision fields
- status fields
- policy result fields
- machine-readable JSON output

Forbidden claims in operative context must block.
Forbidden wording inside clearly marked examples should be treated according to the semantics document, but must not be mistaken for a real result.

## 10. Recursive String Scanning Guidance
Future checker and policy evaluation should scan string values recursively in:
- objects
- lists
- nested summaries
- nested evidence references
- result payloads
- policy payloads

Guidance:
- scan operative string values
- scan nested string values
- preserve safe non-authority boundary statements
- preserve clearly marked examples
- treat ambiguous approval/completion wording as BLOCKED or NOT_ENOUGH_EVIDENCE according to semantics
- do not rely on object keys alone unless the key itself is a forbidden operative field

## 11. Claim Boundary by Mechanism
False PASS resistance must block claims about:
- approval
- completion
- completion gate pass
- human review waiver
- lifecycle mutation
- merge/push/release/deployment authorization
- M68 auto-start

Completion gate policy must block claims about:
- explicit gate pass without policy evidence
- gate approval without human review evidence
- completion inferred from validation
- lifecycle completion inferred from PASS
- M68 auto-start by gate output

## 12. Documentation Example Boundary
Forbidden examples inside documentation are safe only when clearly marked.

Safe markers include:
- example
- unsafe example
- forbidden example
- negative fixture
- expected blocked case
- must block
- should block

If forbidden wording appears without a safe marker, the output should be treated conservatively.

## 13. Non-Authority Boundary
Neither mechanism may claim:
- approval
- task completion
- lifecycle mutation
- merge authorization
- push authorization
- release authorization
- deployment authorization
- production readiness
- M68 start

Human review remains required.

## 14. Relation to Future Checker and Policy Output
Future false PASS checker output should preserve:
- safe boundary statements
- blocked claims
- warning-only ambiguity when appropriate

Future completion gate policy output should preserve:
- explicit request status
- explicit human review status
- explicit blocker state
- explicit result state

## 15. Final Status
FINAL_STATUS: M67_FALSE_PASS_RESISTANCE_CLAIM_BOUNDARY_DEFINED_WITH_WARNINGS
