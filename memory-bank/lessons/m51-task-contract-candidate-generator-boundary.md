# M51 Lesson — Task Contract Candidate Generator Boundary

## Lesson Metadata
```yaml
lesson_metadata:
  lesson_id: m51-task-contract-candidate-generator-boundary
  source_milestone: M51
  source_evidence: reports/m51-task-contract-candidate-generator-evidence-report.md
  source_integration_report: reports/m51-generator-integration-validation.md
  lesson_status: DRAFT
  lesson_confirmed_by: null
  confirmation_expected_from: reports/m51-completion-review.md
  downstream_reuse:
    - M52
    - M53
```

## Purpose
Зафиксировать короткие практические выводы по границам M51: что генератор доказал, чего не доказал, и что обязательно сохранить в M52/M53.

## Source Evidence
- reports/m51-task-contract-candidate-generator-evidence-report.md
- reports/m51-generator-integration-validation.md
- generated/task-contract-candidates/agent-action-review.generated-conversion-package.md

## Core Lesson
A generated task contract candidate is still not lifecycle state.

M51 generator output is a controlled staging artifact only.

Dry-run success is not approval.

Write success is not approval.

Fixture PASS is not approval.

M50 validator PASS is not approval.

M51 evidence complete is not queue placement.

M51 evidence complete is not active-task replacement.

## What M51 Proved
M51 proved that a validated M50 conversion package can be used as generator input.

M51 proved that generator dry-run can predict would_write_to without writing files.

M51 proved that controlled write can create one staging artifact under generated/task-contract-candidates/.

M51 proved that the generated staging artifact can remain M50-validator compatible.

M51 proved that generated_candidate_path can remain null while output_path points to the generated conversion package.

M51 proved that fixtures can detect unsafe generator inputs.

M51 proved that examples can remain documentation-only.

M51 proved that integration validation can produce evidence without queue placement.

## What M51 Did Not Prove
M51 did not prove that a generated candidate is ready for execution.

M51 did not perform M52 candidate validation.

M51 did not perform M53 placement review.

M51 did not create a queue entry.

M51 did not modify active task state.

M51 did not create an approval record.

M51 did not authorize implementation.

M51 did not authorize lifecycle movement.

M51 did not validate arbitrary generator inputs beyond the canonical example and fixture set.

## Boundary Lessons
Staging is not lifecycle state.

Generated is not queued.

Generated is not active.

Generated is not approved.

Evidence is not approval.

A validator can check shape without granting authority.

A generator can produce a file without granting execution permission.

A report can summarize evidence without changing lifecycle state.

## Generator Lessons
The generator must remain dry-run by default.

The generator must require explicit --write for writes.

The generator must require explicit --out for writes.

The generator must restrict writes to generated/task-contract-candidates/.

The generator must not write to tasks/active-task.md.

The generator must not write to tasks/queue/.

The generator must not create approval records.

The generator output filename must derive from generator_input.input_id.

The generator must create a generated conversion package with embedded task_contract_candidate, not a standalone candidate artifact.

## Fixture Lessons
Positive fixtures must exercise real dry-run validation logic.

Positive fixtures must not pass merely because metadata exists.

Negative fixtures must contain unsafe values intentionally.

Negative fixtures must verify blocking behavior.

Fixture PASS is not approval.

Fixture PASS is not execution permission.

Fixture PASS is not queue placement.

Fixture PASS is not active-task replacement.

## Integration Lessons
Integration validation must run dry-run before write.

Integration validation must check naming convention before write.

Integration validation must validate generated staging artifact with M50 validator.

Integration validation must confirm generated_candidate_path remains null.

Integration validation must confirm no standalone candidate-only artifact was created.

Integration validation must confirm no queue entry was created.

Integration validation must confirm active task was not modified.

Integration validation must confirm no approval record was created.

## Failure Patterns to Prevent
- Treating dry-run success as approval.
- Treating write success as approval.
- Treating fixture PASS as approval.
- Treating M50 validator PASS as execution permission.
- Treating generated staging artifact as queue placement.
- Treating generated staging artifact as active task state.
- Creating standalone candidate-only artifact in M51.
- Setting generated_candidate_path to non-null in M51.
- Deriving output filename from input file path instead of generator_input.input_id.
- Writing outside generated/task-contract-candidates/.
- Creating reports/m51-completion-review.md before completion review task.
- Creating tasks/queue/ entry during generator or evidence tasks.
- Modifying tasks/active-task.md during generator or evidence tasks.

## Required Reuse in M52
M52 must validate the generated task contract candidate shape independently.

M52 must not rely on M51 evidence as approval.

M52 must verify carry-forward fields.

M52 must verify forbidden changes are preserved.

M52 must verify downstream limits are preserved.

M52 must verify non-authority boundary is preserved.

M52 must reject candidate artifacts that imply execution permission.

M52 must treat generated staging artifacts as input only, not lifecycle state.

## Required Reuse in M53
M53 is the first layer allowed to evaluate controlled placement.

M53 must not treat M51 generated artifact as already queued.

M53 must not treat M51 evidence as placement authorization.

M53 must require explicit placement gate decision.

M53 must verify no active-task replacement occurs without controlled placement authorization.

M53 must preserve the distinction between staging artifact, queue entry, and active task.

## Non-Authority Boundary
M51 lessons entry is not approval.

M51 lessons entry does not authorize execution.

M51 lessons entry does not authorize queue placement.

M51 lessons entry does not authorize active-task replacement.

M51 lessons entry does not authorize implementation.

M51 lessons entry does not create lifecycle state.

M51 lessons entry does not confirm M51 completion.

M51 lessons entry requires M51 completion review for confirmation.

## Lesson Status
Lesson Status: DRAFT

Confirmation expected from: reports/m51-completion-review.md

This lesson is captured before M51 completion review.

This lesson must be treated as draft until M51 completion review confirms or revises it.
