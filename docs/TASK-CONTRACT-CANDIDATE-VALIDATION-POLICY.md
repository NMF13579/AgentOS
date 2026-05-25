# Task Contract Candidate Validation Policy (M52)

## Purpose

This policy defines what M52 candidate validation must accept, fail, or block for generated task contract candidates before any M53 placement review.

## Policy Authority

The M52 policy is subordinate to the M52 architecture, input contract, and output contract.
The M52 policy must not override M52 non-authority boundaries.
The M52 policy must not authorize placement, execution, queue write, active-task replacement, approval creation, commit, push, merge, deployment, or release.
If this policy conflicts with a higher AgentOS safety boundary, the higher safety boundary wins.

## Accepted Source Artifacts

Primary accepted source artifact:
- generated/task-contract-candidates/agent-action-review.generated-conversion-package.md

M52 validates a generated conversion package wrapper containing an embedded task_contract_candidate.
M52 must not treat a standalone candidate-only file as the primary valid artifact when expected_candidate_shape is generated_conversion_package_with_embedded_candidate.
Candidate-only artifacts may be used only as secondary extracted views if traceable to the generated conversion package wrapper.
For M52 MVP, the primary source artifact must remain the generated conversion package wrapper.

## Accepted Source Origins

M52 MVP accepted source origin:
- M51_GENERATED_STAGING_ARTIFACT

Future source origins may be added only by future policy updates.
M52 MVP must not silently accept non-M51 origins.
Unknown source_candidate_origin must produce TASK_CONTRACT_CANDIDATE_VALIDATION_BLOCKED.

## M51-Origin Evidence Requirements

Required M51-origin evidence:
- source_generator_evidence
- source_generator_completion_review
- source_generator_integration_report

m51_origin fields are required only when source_candidate_origin is M51_GENERATED_STAGING_ARTIFACT.
For M52 MVP, because source_candidate_origin is M51_GENERATED_STAGING_ARTIFACT, m51_origin evidence is required for every valid MVP input.
Missing M51-origin evidence for an M51-origin candidate must produce TASK_CONTRACT_CANDIDATE_VALIDATION_BLOCKED.
M52 must not silently accept missing M51 evidence for M51-origin candidates.

## Accepted Candidate Shape

Accepted M52 MVP shape:
- generated_conversion_package_with_embedded_candidate

Expected structure (or M51-compatible equivalent in the generated artifact):

```yaml
conversion_package:
  candidate_output:
    task_contract_candidate:
```

If the conversion package wrapper is missing, result must be TASK_CONTRACT_CANDIDATE_VALIDATION_BLOCKED.
If task_contract_candidate is missing, result must be TASK_CONTRACT_CANDIDATE_VALIDATION_FAILED or TASK_CONTRACT_CANDIDATE_VALIDATION_BLOCKED depending on whether the validator can safely parse source provenance.
If a standalone candidate-only artifact is submitted as the primary source while expected_candidate_shape is generated_conversion_package_with_embedded_candidate, result must be TASK_CONTRACT_CANDIDATE_VALIDATION_BLOCKED.

## Required Candidate Sections

Required candidate sections:
- goal
- scope
- allowed_changes
- forbidden_changes
- validation
- expected_final_report

Required carry-forward sections:
- accepted_limitations
- open_questions
- downstream_limits
- non_authority_boundary

Missing goal must produce TASK_CONTRACT_CANDIDATE_VALIDATION_FAILED.
Missing scope must produce TASK_CONTRACT_CANDIDATE_VALIDATION_FAILED.
Missing allowed_changes must produce TASK_CONTRACT_CANDIDATE_VALIDATION_FAILED.
Missing forbidden_changes must produce TASK_CONTRACT_CANDIDATE_VALIDATION_FAILED.
Missing validation must produce TASK_CONTRACT_CANDIDATE_VALIDATION_FAILED.
Missing expected_final_report must produce TASK_CONTRACT_CANDIDATE_VALIDATION_FAILED.

Missing accepted_limitations from the source carry-forward baseline must produce TASK_CONTRACT_CANDIDATE_VALIDATION_FAILED.
Missing open_questions from the source carry-forward baseline must produce TASK_CONTRACT_CANDIDATE_VALIDATION_FAILED.
Missing downstream_limits from the source carry-forward baseline must produce TASK_CONTRACT_CANDIDATE_VALIDATION_FAILED.
Missing non_authority_boundary must produce TASK_CONTRACT_CANDIDATE_VALIDATION_FAILED.

## Required Traceability Policy

Required traceability:
- source_proposal
- source_authorization
- source_conversion_package
- source_generated_artifact
- source_candidate_origin
- m50_traceability
- m51_generator_evidence

Traceability must be explicit and machine-readable enough for the validator to record source_traceability in the output result.
Missing source traceability must produce TASK_CONTRACT_CANDIDATE_VALIDATION_BLOCKED if the validator cannot safely determine source lineage.
Missing source traceability must produce TASK_CONTRACT_CANDIDATE_VALIDATION_FAILED if source lineage is known but required traceability fields are absent from the candidate.

## Source Authorization Boundary

source_authorization means provenance authorization for source conversion or candidate generation only.
source_authorization is not approval.
source_authorization is not execution authorization.
source_authorization is not placement authorization.
source_authorization does not authorize queue placement.
source_authorization does not authorize active-task replacement.
source_authorization does not authorize approval record creation.

## Carry-Forward Preservation Policy

accepted_limitations, open_questions, downstream_limits, and non_authority_boundary must be carried forward from the source conversion package without deletion.
Additional stricter limitations may be added.
Additional open questions may be added.
Additional downstream limits may be added.
Additional non-authority warnings may be added.
Existing carry-forward items must not be removed, softened, renamed into weaker meaning, converted into resolved state, converted into approved state, or hidden from M53 review.

If carry-forward baseline is unavailable, result must be TASK_CONTRACT_CANDIDATE_VALIDATION_BLOCKED.
If carry-forward baseline is available and candidate drops required carry-forward items, result must be TASK_CONTRACT_CANDIDATE_VALIDATION_FAILED.

## Allowed Changes Policy

allowed_changes may be equal to or narrower than the baseline allowed_changes.
allowed_changes must not add new paths, new actions, new write authority, new execution authority, new placement authority, or broader implementation scope.
allowed_changes must not authorize queue write.
allowed_changes must not authorize active-task replacement.
allowed_changes must not authorize approval creation.
allowed_changes must not authorize commit.
allowed_changes must not authorize push.
allowed_changes must not authorize merge.
allowed_changes must not authorize deployment.
allowed_changes must not authorize release.

If no baseline is available for allowed_changes comparison, result must be TASK_CONTRACT_CANDIDATE_VALIDATION_BLOCKED.
If allowed_changes expands beyond the baseline, result must be TASK_CONTRACT_CANDIDATE_VALIDATION_FAILED.

## Forbidden Changes Policy

forbidden_changes may be equal to or stricter than the baseline forbidden_changes.
forbidden_changes must not remove, soften, rename away, make conditional, or weaken any prior forbidden boundary.
forbidden_changes must preserve prohibitions against:
- queue placement
- active-task replacement
- execution permission
- approval creation
- commit
- push
- merge
- deployment
- release
- M53 placement authorization

If no baseline is available for forbidden_changes comparison, result must be TASK_CONTRACT_CANDIDATE_VALIDATION_BLOCKED.
If forbidden_changes weakens prior forbidden boundaries, result must be TASK_CONTRACT_CANDIDATE_VALIDATION_FAILED.

## Validation Section Policy

The validation section must define verifiable checks.
The validation section must not claim that validation success authorizes execution.
The validation section must not claim that validation success authorizes placement.
The validation section must not claim that validation success creates approval.
The validation section must not require or imply commit, push, merge, deployment, or release.

If validation section is missing, result must be TASK_CONTRACT_CANDIDATE_VALIDATION_FAILED.
If validation section implies execution or placement authority, result must be TASK_CONTRACT_CANDIDATE_VALIDATION_FAILED.

## Expected Final Report Policy

expected_final_report may request validation evidence.
expected_final_report may request findings, warnings, blockers, and boundary confirmations.
expected_final_report must not request commit.
expected_final_report must not request push.
expected_final_report must not request queue placement.
expected_final_report must not request active-task replacement.
expected_final_report must not request approval creation.
expected_final_report must not request M53 placement decision.

If expected_final_report is missing, result must be TASK_CONTRACT_CANDIDATE_VALIDATION_FAILED.
If expected_final_report implies authority escalation, result must be TASK_CONTRACT_CANDIDATE_VALIDATION_FAILED.

## Accepted Limitations Policy

accepted_limitations must be preserved.
accepted_limitations may produce TASK_CONTRACT_CANDIDATE_VALIDATION_OK_WITH_LIMITATIONS if candidate is otherwise structurally valid and no blockers exist.
accepted_limitations must not be converted into approvals.
accepted_limitations must not be hidden from M53.
accepted_limitations must not be removed to make the candidate appear cleaner.

## Open Questions Policy

open_questions must be preserved.
open_questions may produce TASK_CONTRACT_CANDIDATE_VALIDATION_OK_WITH_LIMITATIONS if candidate is otherwise structurally valid and no blockers exist.
open_questions must not be silently resolved by M52.
open_questions must not be converted into approval.
open_questions must not be hidden from M53.
If open_questions affect M53 review readiness but do not violate authority boundaries, result may be TASK_CONTRACT_CANDIDATE_VALIDATION_OK_WITH_LIMITATIONS.
If open_questions make candidate validity impossible to determine, result must be TASK_CONTRACT_CANDIDATE_VALIDATION_BLOCKED.

## Downstream Limits Policy

downstream_limits must be preserved.
downstream_limits define what later milestones, including M53, may not assume.
downstream_limits must not be weakened, removed, or converted into permission.
downstream_limits must not authorize placement, execution, queue write, active-task replacement, approval creation, commit, push, merge, deployment, or release.
Dropped or weakened downstream_limits must produce TASK_CONTRACT_CANDIDATE_VALIDATION_FAILED.

## Non-Authority Boundary Policy

Candidate validation is not approval.
Candidate validation is not execution permission.
Candidate validation is not queue placement.
Candidate validation is not active-task replacement.
Candidate validation does not create lifecycle state.
Candidate validation does not authorize M53 placement.

TASK_CONTRACT_CANDIDATE_VALIDATION_OK is not approval.
TASK_CONTRACT_CANDIDATE_VALIDATION_OK is not queue placement.
TASK_CONTRACT_CANDIDATE_VALIDATION_OK is not active-task replacement.
TASK_CONTRACT_CANDIDATE_VALIDATION_OK is not execution permission.
TASK_CONTRACT_CANDIDATE_VALIDATION_OK is not M53 placement authorization.

m53_review_input_candidate: true means only that the artifact may be used as input for M53 review.
m53_review_input_candidate: true does not authorize M53 placement.

If non_authority_boundary is missing or weakened, result must be TASK_CONTRACT_CANDIDATE_VALIDATION_FAILED.

## Boundary Flags Policy

Required fixed boundary values:
- validation_only: true
- placement_authorized: false
- execution_authorized: false
- queue_write_allowed: false
- active_task_write_allowed: false
- approval_record_creation_allowed: false

Any candidate or result that sets placement_authorized, execution_authorized, queue_write_allowed, active_task_write_allowed, or approval_record_creation_allowed to true is invalid.
Any candidate that implies placement, execution, queue write, active-task replacement, or approval creation must produce TASK_CONTRACT_CANDIDATE_VALIDATION_FAILED.

## Mode Policy

Generated task contract candidate mode must be EXECUTION_SHAPE, not EXECUTION.
Mode EXECUTION in a generated candidate is authority escalation.
If a generated candidate uses mode EXECUTION, result must be TASK_CONTRACT_CANDIDATE_VALIDATION_FAILED.

Task execution mode and generated candidate mode are different concepts.
Task 52.4 mode = EXECUTION because the implementation agent is executing bounded repository work to create this policy document.
Generated candidate mode = EXECUTION_SHAPE because the candidate is not executable.

## Result Classification Policy

TASK_CONTRACT_CANDIDATE_VALIDATION_OK:
- candidate is structurally valid
- required sections exist
- required traceability exists
- required carry-forward fields are preserved
- no authority boundary is weakened
- no blockers exist
- m53_review_input_candidate may be true
- all authority flags remain false

TASK_CONTRACT_CANDIDATE_VALIDATION_OK_WITH_LIMITATIONS:
- candidate is structurally valid
- required traceability exists
- required carry-forward fields are preserved
- accepted_limitations and/or open_questions remain present
- no authority boundary is weakened
- no blockers exist
- m53_review_input_candidate may be true
- all authority flags remain false

TASK_CONTRACT_CANDIDATE_VALIDATION_FAILED:
- candidate artifact exists and can be parsed
- required sections, traceability, carry-forward, policy, or boundary checks fail
- m53_review_input_candidate must be false
- all authority flags remain false

TASK_CONTRACT_CANDIDATE_VALIDATION_BLOCKED:
- validator cannot safely determine candidate validity
- source artifact is missing
- expected wrapper is missing
- source origin is unsupported or unknown
- M51-origin evidence is missing for M51-origin candidate
- baseline comparison source is unavailable
- carry-forward baseline is unavailable
- m53_review_input_candidate must be false
- all authority flags remain false

## Blocking Conditions

Blocking conditions:
- source generated artifact missing
- source generated artifact not M50-validator compatible
- conversion package wrapper missing
- unsupported source_candidate_origin
- unknown source_candidate_origin
- M51-origin evidence missing for M51 candidate
- baseline unavailable for allowed_changes comparison
- baseline unavailable for forbidden_changes comparison
- carry-forward baseline unavailable
- candidate without conversion package wrapper treated as primary artifact
- validator cannot safely determine source lineage
- validator input or downstream interpretation explicitly treats m53_review_input_candidate as placement approval

If any M52 input, output, report, or downstream consumer treats m53_review_input_candidate as placement approval, M52 must treat that as an authority-boundary violation and BLOCKED handoff condition.

## Failure Conditions

Failure conditions:
- task_contract_candidate missing when source provenance is otherwise known
- source traceability fields missing when source lineage is known
- source authorization missing
- goal missing
- scope missing
- allowed_changes missing
- forbidden_changes missing
- validation missing
- expected_final_report missing
- accepted limitations dropped
- open questions dropped
- downstream limits dropped
- non_authority_boundary dropped
- forbidden changes weakened
- allowed changes expanded
- mode EXECUTION used instead of EXECUTION_SHAPE
- execution_authorized true
- active_task_write_allowed true
- queue_write_allowed true
- approval_record_creation_allowed true
- placement_authorized true
- candidate implies queue placement
- candidate implies active-task replacement
- candidate implies execution permission
- candidate implies approval creation
- validation section implies execution or placement authority
- expected_final_report implies authority escalation

## OK_WITH_LIMITATIONS Conditions

OK_WITH_LIMITATIONS is allowed only when:
- candidate is structurally valid
- source traceability exists
- M51-origin evidence exists when required
- required carry-forward fields are preserved
- no authority boundary is weakened
- no blockers exist
- limitations or open questions remain visible for M53 review

OK_WITH_LIMITATIONS must not be used to bypass blockers.
OK_WITH_LIMITATIONS must not be used when candidate validity cannot be safely determined.
OK_WITH_LIMITATIONS must not be used when authority boundary is weakened.

## M53 Handoff Policy

M52 may produce m53_review_input_candidate: true only for OK or OK_WITH_LIMITATIONS results.
m53_review_input_candidate: true means only that the validated candidate may be used as input for M53 review.
M53 must independently decide placement eligibility.
M52 must not decide queue placement.
M52 must not create queue entries.
M52 must not modify tasks/active-task.md.
M52 must not create approval records.
M52 must not authorize execution.

## Non-Goals

M52 policy does not authorize:
- queue placement
- active task replacement
- task execution
- approval record creation
- human approval simulation
- M53 placement decision
- modifying generated staging artifact
- creating tasks/queue entry
- copying anything into tasks/active-task.md
- commit
- push
- merge
- deploy
- release

## Policy Summary

M52 validates generated candidates only for readiness of M53 review input. M52 does not place tasks, does not authorize execution, does not change active task state, and does not create approvals.
