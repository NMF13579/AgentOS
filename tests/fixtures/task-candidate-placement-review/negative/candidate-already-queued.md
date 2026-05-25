```json
{
  "negative_fixture": {
    "fixture_id": "candidate-already-queued",
    "fixture_type": "AUTHORITY_ESCALATION_BLOCKER",
    "expected_result": "PLACEMENT_REVIEW_BLOCKED",
    "expected_exit_code": 2,
    "expected_blocker": "candidate already queued",
    "payload_kind": "placement_review_input",
    "payload": {
      "candidate_already_queued": true
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
