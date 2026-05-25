```json
{
  "negative_fixture": {
    "fixture_id": "non-canonical-m52-completion-review-path",
    "fixture_type": "DEPENDENCY_BLOCKER",
    "expected_result": "PLACEMENT_REVIEW_BLOCKED",
    "expected_exit_code": 2,
    "expected_blocker": "source_m52_completion_review must equal reports/m52-completion-review.md",
    "payload_kind": "placement_review_input",
    "payload": {
      "source_m52_completion_review": "reports/52.11-task-close-record.md"
    }
  }
}
```

This negative fixture proves M53 blocks placement authority escalation.

This fixture is not approval.
This fixture does not authorize execution.
This fixture does not authorize queue placement.
This fixture does not authorize active-task replacement.
This fixture does not authorize lifecycle mutation.
This fixture does not authorize M54 materialization.
