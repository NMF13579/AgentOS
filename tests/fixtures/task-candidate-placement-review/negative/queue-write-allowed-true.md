```json
{
  "negative_fixture": {
    "fixture_id": "queue-write-allowed-true",
    "fixture_type": "AUTHORITY_ESCALATION_BLOCKER",
    "expected_result": "PLACEMENT_REVIEW_BLOCKED",
    "expected_exit_code": 2,
    "expected_blocker": "queue write authority escalation",
    "payload_kind": "placement_review_input",
    "payload": {
      "boundaries": {
        "queue_write_allowed": true
      }
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
