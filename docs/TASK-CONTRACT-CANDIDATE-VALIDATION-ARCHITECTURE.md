# Task Contract Candidate Validation Architecture (M52)

## Purpose

M52 validates whether a generated staging artifact from M51 can be treated as a valid task contract candidate for controlled placement review in M53.

Task contract candidate validation defines candidate readiness for placement review only.
Task contract candidate validation does not authorize placement or execution.

## What M52 Validation Is

Task contract candidate validation checks structural and semantic readiness of a generated task contract candidate for M53 review.

M52 validates candidate readiness for M53 review.
M52 does not perform M53 review.

## What M52 Validation Is Not

Candidate validation is not approval.
Candidate validation is not execution permission.
Candidate validation is not queue placement.
Candidate validation is not active-task replacement.
Candidate validation does not create lifecycle state.
Candidate validation does not authorize M53 placement.

M52 does not create queue entries.
M52 does not modify active task state.

## Canonical M52 Chain

M50: proposal converted to candidate shape
↓
M51: generator created staging artifact
↓
M52: candidate independently validated
↓
M53: controlled placement gate decides queue / active eligibility

## Primary Source Artifact

Primary M52 source artifact:

`generated/task-contract-candidates/agent-action-review.generated-conversion-package.md`

M52 validates the embedded candidate inside the generated conversion package wrapper, using the M51-compatible structure from the actual artifact, for example:

```yaml
conversion_package:
  candidate_output:
    task_contract_candidate:
```

For M52 MVP, `--candidate` in the future validator must mean a generated conversion package artifact containing an embedded `task_contract_candidate`.
For M52 MVP, candidate validation must not treat a standalone candidate-only artifact as the primary valid artifact when the expected shape is `generated_conversion_package_with_embedded_candidate`.

## Staging Artifact vs Validated Candidate

Generated staging artifact is M51 output that still requires independent validation.
Validated candidate is a validation result state proving candidate readiness for M53 review only.

Validated candidate is not active task state.
Validated candidate must not be copied into tasks/active-task.md.
Validated candidate must not be placed into tasks/queue/ by M52.

## Input, Read Path, and Traceability

M52 input lives in generated task contract candidate artifacts produced by M51.
M52 reads M51 generated staging artifacts from the generated conversion package and validates embedded candidate content plus package boundaries.
M52 must preserve M50/M51 traceability by preserving source references and boundary context carried forward from conversion package fields.

If referenced, `source_authorization` means provenance authorization for source conversion / candidate generation only.
source_authorization is not approval.
source_authorization is not execution authorization.
source_authorization is not placement authorization.

## Output and Handoff

M52 may produce validation results and validation records.
M52 output is candidate validation result for controlled M53 placement review input.
M52 handoff to M53 is review input only and never placement execution.

## Task Execution Context Boundary

Task 52.1 execution mode is bounded to creating the M52 architecture document only.
Generated task contract candidates validated by M52 must remain EXECUTION_SHAPE, not EXECUTION.
Task execution context does not authorize commit, push, merge, queue placement, active-task replacement, approval creation, candidate execution, or M53 placement review.

## Architecture Rules

- M52 validates generated task contract candidates only as review input for M53.
- M52 may produce validation results and validation records.
- M52 must preserve M50/M51 traceability.
- M52 must preserve accepted_limitations.
- M52 must preserve open_questions.
- M52 must preserve downstream_limits.
- M52 must preserve non_authority_boundary.
- M52 must reject boundary weakening.
- M52 must reject authority escalation.
- M52 must reject candidates that imply execution permission.
- M52 must reject candidates that imply queue placement.
- M52 must reject candidates that imply active-task replacement.
- M52 must reject standalone candidate-only files as primary artifacts when a generated conversion package wrapper is expected.

## Write Boundaries

Why validation is not placement:
M52 only determines readiness for M53 review and never performs queue or active-task placement decisions.

Why validation is not approval:
M52 validation result is technical readiness evidence and does not create or grant human approval.

Why validation is not execution permission:
M52 keeps candidate mode at EXECUTION_SHAPE and does not grant EXECUTION authority.

Why M52 cannot write into `tasks/queue/`:
Queue placement belongs to controlled M53 placement decisions, not M52 candidate validation.

Why M52 cannot write into `tasks/active-task.md`:
Active task state changes require explicit human checkpoint and are outside M52 validation scope.
