```json
{
  "negative_fixture": {
    "fixture_id": "accepted-limitations-dropped",
    "fixture_type": "CARRY_FORWARD_BLOCKER",
    "expected_result": "PLACEMENT_REVIEW_BLOCKED",
    "expected_exit_code": 2,
    "expected_blocker": "accepted limitations dropped",
    "payload_kind": "placement_review_input",
    "m52_source_contains": {
      "accepted_limitations": [
        "M52 limitation carried forward into M53 eligibility review."
      ]
    },
    "payload_drops": {
      "accepted_limitations": true
    },
    "payload": {}
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
