# Interview Answer Record Contract

## 1. Purpose
Interview Answer Record stores structured interview evidence from M45.

Interview answer record stores interview evidence, not industrial specification.

## 2. Authority and Relationship to Previous M45 Artifacts
- `docs/PROBLEM-INTERVIEW-ARCHITECTURE.md` defines the conceptual boundary.
- `templates/problem-interview.md` defines the basic interview capture template from 45.2.
- `templates/interview-answer-record.md` defines the fillable answer record format for finalized structured interview evidence.
- `docs/INTERVIEW-QUESTION-BANK.md` defines safe question patterns.
- `schemas/interview-answer-record.schema.json` defines the machine-checkable record structure.

templates/problem-interview.md is the basic interview capture template.
templates/interview-answer-record.md is the structured answer record template governed by the schema.

## 3. Field Definitions
- `interview_id`: unique interview record identifier.
- `created_at`: timestamp text for record creation.
- `interview_status`: current status of the interview record.
- `source_user_input`: raw user-provided input.
- `idea_summary`: neutral short summary of source input.
- `problem_summary`: core problem statement or `MISSING_FROM_INTERVIEW`.
- `target_users`: affected/target users or `MISSING_FROM_INTERVIEW`.
- `current_workaround`: current coping process or `MISSING_FROM_INTERVIEW`.
- `desired_outcome`: expected user-level outcome or `MISSING_FROM_INTERVIEW`.
- `success_criteria`: user-level success signal or `MISSING_FROM_INTERVIEW`.
- `constraints`: explicit constraints, `NONE`, or `MISSING_FROM_INTERVIEW`.
- `risks`: explicit risks, `NONE`, or `MISSING_FROM_INTERVIEW`.
- `non_goals`: explicit out-of-scope intentions, `NONE`, or `MISSING_FROM_INTERVIEW`.
- `unknowns`: unresolved unknown items.
- `assumptions`: explicit assumptions.
- `answered_questions`: captured Q/A entries with answers.
- `unanswered_questions`: captured questions without answer yet.
- `follow_up_questions`: targeted clarification questions.
- `non_approval_warning`: mandatory constant warning text.

## 4. Status Model
Allowed statuses only:
- `INTERVIEW_DRAFT`
- `INTERVIEW_NEEDS_CLARIFICATION`
- `INTERVIEW_READY_FOR_SPEC`
- `INTERVIEW_BLOCKED`

INTERVIEW_READY_FOR_SPEC does not mean approved for implementation.

## 5. Missing Information Contract
Missing information must be recorded as MISSING_FROM_INTERVIEW, not inferred.
Missing information must become follow-up questions, not hallucinated requirements.

Missing required information must never be replaced with guesses.

## 6. NONE Contract
Use NONE only when the user explicitly says there are no constraints.
Use NONE only when the user explicitly says there are no risks.
Use NONE only when the user explicitly says there are no non-goals.

`NONE` и `MISSING_FROM_INTERVIEW` не взаимозаменяемы.

## 7. idea_summary Contract
idea_summary must not add information not present in source_user_input.

- `idea_summary` is a neutral short summary.
- It must not improve, complete, or reinterpret the user idea.
- It must not add features, constraints, risks, users, integrations, acceptance criteria, or implementation details.
- If source input is unclear, summary must preserve that uncertainty.

## 8. Success Criteria Boundary
M45 records user-level success_criteria.
M45 does not create formal industrial acceptance criteria.
Formal acceptance criteria belong to M46.

## 9. Non-Approval Boundary
Interview evidence is not industrial spec.
Interview completeness is not execution readiness.
INTERVIEW_READY_FOR_SPEC does not mean approved for implementation.

This record does not authorize:
- implementation
- task creation
- queue entry creation
- autopilot
- commit
- push
- merge
- release
- deployment

## 10. Forbidden Fields
The answer record must not contain M46 or execution fields.

Forbidden fields:
- `functional_requirements`
- `non_functional_requirements`
- `acceptance_criteria`
- `validation_strategy`
- `implementation_plan`
- `task_contract`
- `queue_entry`
- `approval`
- `execution_ready`
- `approved_for_implementation`

These names may be documented here for explanation, but JSON Schema properties must not define them.

## 11. Schema Validation Meaning
- JSON Schema validation confirms record shape only.
- Schema validation does not prove interview completeness.
- Schema validation does not approve implementation.
- Schema validation does not authorize M46 by itself.
- Completeness checking belongs to 45.5.

Schema validity is not interview completeness.

## 12. M45 to M46 Boundary
No interview evidence → no industrial spec.
No interview evidence -> no industrial spec.
M45 = ask correctly, record answers, detect gaps.
M46 = transform interview evidence into industrial specification.

M46 may consume the interview answer record, but M45 must not create M46 artifacts.

## 13. Final Boundary
Interview evidence is not industrial spec.
Interview completeness is not execution readiness.
Schema validity is not interview completeness.
No interview evidence → no industrial spec.
No interview evidence -> no industrial spec.
Missing information must be recorded as MISSING_FROM_INTERVIEW, not inferred.
Missing information must become follow-up questions, not hallucinated requirements.
INTERVIEW_READY_FOR_SPEC does not mean approved for implementation.
M45 = ask correctly, record answers, detect gaps.
M46 = transform interview evidence into industrial specification.
