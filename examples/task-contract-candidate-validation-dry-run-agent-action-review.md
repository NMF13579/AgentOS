# Example M52 Candidate Validation Dry-Run — Agent Action Review

Flow:

M51 generated staging artifact
↓
M52 validation input
↓
candidate validator dry-run / validation check
↓
validation result OK or OK_WITH_LIMITATIONS
↓
still no queue placement

The validator command must be written in multi-line shell format using backslash continuation.

```bash
python3 scripts/validate-task-contract-candidate.py \
  --candidate generated/task-contract-candidates/agent-action-review.generated-conversion-package.md \
  --json
```

The future report command shape must also be written in multi-line shell format using backslash continuation.

```bash
python3 scripts/validate-task-contract-candidate.py \
  --candidate generated/task-contract-candidates/agent-action-review.generated-conversion-package.md \
  --json > reports/m52-candidate-validation-result-agent-action-review.json
```

This command shape is for Task 52.8 integration validation.
Task 52.7 must not create reports/m52-candidate-validation-result-agent-action-review.json.
The validator writes JSON to stdout.
The caller shell redirection creates reports JSON.
The validator must not open, create, or modify reports/*.json directly.

Example candidate validation is not approval.
Example candidate validation does not authorize execution.
Example candidate validation does not authorize queue placement.
Example candidate validation does not authorize active-task replacement.
Example candidate validation does not authorize M53 placement.
Example candidate validation does not create lifecycle state.

m53_review_input_candidate: true means only that the artifact may be used as input for M53 review.
m53_review_input_candidate: true is not placement approval.
M53 must independently decide placement eligibility.

Illustrative result fragment:

```yaml
candidate_validation_result:
  result: TASK_CONTRACT_CANDIDATE_VALIDATION_OK
  validated: true
  m53_review_input_candidate: true
  placement_authorized: false
  execution_authorized: false
  queue_write_allowed: false
  active_task_write_allowed: false
  approval_record_creation_allowed: false
```

This illustrative result fragment is not a real validation result.
This illustrative result fragment is not evidence.
This illustrative result fragment must not be copied into reports/.
Task 52.8 creates the real integration validation result by running the validator.
