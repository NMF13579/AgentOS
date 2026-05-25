```json
{
  "negative_fixture": {
    "fixture_id": "lifecycle-mutation-allowed-true",
    "fixture_type": "AUTHORITY_ESCALATION_BLOCKER",
    "expected_result": "PLACEMENT_REVIEW_BLOCKED",
    "expected_exit_code": 2,
    "expected_blocker": "lifecycle mutation authority",
    "payload_kind": "placement_review_input",
    "payload": {
      "boundaries": {
        "lifecycle_mutation_allowed": true
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
