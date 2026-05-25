---
type: example
milestone: M53
task: 53.7
title: Example Placement Review Dry Run — Agent Action Review
status: draft
authority: example
created_for: M53
example_kind: placement_review_dry_run
source_example_input: examples/task-candidate-placement-review-input-agent-action-review.md
m54_materialization_authorized: false
---

This example dry-run demonstrates placement eligibility review without queue placement.

This dry-run references example production-style M52 artifacts.
If those artifacts are absent, the dry-run may return PLACEMENT_REVIEW_BLOCKED.
A blocked dry-run caused by missing example source artifacts is an example limitation, not approval, placement, execution, or materialization.

This dry-run example is not approval.
This dry-run example does not authorize execution.
This dry-run example does not authorize queue placement.
This dry-run example does not authorize active-task replacement.
This dry-run example does not authorize lifecycle mutation.
This dry-run example does not authorize M54 materialization.

```bash
python3 scripts/review-task-candidate-placement.py \
  --input examples/task-candidate-placement-review-input-agent-action-review.md \
  --m52-reports-dir reports \
  --json > /tmp/m53-example-placement-review-result-agent-action-review.json
EXAMPLE_PLACEMENT_REVIEW_EXIT_CODE=$?
```

The JSON result is written to /tmp by shell redirection, not by the CLI.

This dry-run does not create reports/m53-placement-review-result-agent-action-review.json.

```yaml
possible_success_results:
  - PLACEMENT_REVIEW_ELIGIBLE
  - PLACEMENT_REVIEW_ELIGIBLE_WITH_LIMITATIONS

possible_non_success_results:
  - PLACEMENT_REVIEW_NOT_ELIGIBLE
  - PLACEMENT_REVIEW_BLOCKED
```

Any exit code 0 from this example dry-run still does not authorize queue placement, active-task replacement, execution, lifecycle mutation, or M54 materialization.

If the optional dry-run exits 0, the /tmp JSON result must still preserve all non-authority boundary flags.

A successful dry-run result is still not approval, not execution permission, not queue placement, and not M54 materialization.

```yaml
m54_independent_validation_required: true
m54_may_not_start_without_own_gate: true
m54_materialization_authorized: false
queue_placement_performed: false
active_task_replacement_performed: false
approval_created: false
```

M53 example dry-run may produce a placement eligibility result.
M53 example dry-run does not authorize M54 to run.
M53 example dry-run does not authorize queue materialization.
M53 example dry-run does not authorize active-task proposal materialization.
M54 must independently validate materialization.

The M53 dry-run example confirms example behavior only.

It does not place a candidate.
It does not approve a candidate.
It does not execute a candidate.
It does not materialize a candidate.
