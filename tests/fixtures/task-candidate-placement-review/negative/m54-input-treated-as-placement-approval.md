```json
{
  "negative_fixture": {
    "fixture_id": "m54-input-treated-as-placement-approval",
    "fixture_type": "M54_BOUNDARY_BLOCKER",
    "expected_result": "PLACEMENT_REVIEW_BLOCKED",
    "expected_exit_code": 2,
    "expected_blocker": "m54 input treated as placement approval",
    "payload_kind": "placement_review_result",
    "payload": {
      "eligible_as_m54_queue_materialization_input": true,
      "placement_approved": true
    }
  }
}
```

m54_queue_materialization_input_candidate is not placement approval.

This negative fixture proves M53 blocks placement authority escalation.

This fixture is not approval.
This fixture does not authorize execution.
This fixture does not authorize queue placement.
This fixture does not authorize active-task replacement.
This fixture does not authorize lifecycle mutation.
This fixture does not authorize M54 materialization.
