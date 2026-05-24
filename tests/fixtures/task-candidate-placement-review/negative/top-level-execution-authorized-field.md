```json
{
  "negative_fixture": {
    "fixture_id": "top-level-execution-authorized-field",
    "fixture_type": "AUTHORITY_ESCALATION_BLOCKER",
    "expected_result": "PLACEMENT_REVIEW_BLOCKED",
    "expected_exit_code": 2,
    "expected_blocker": "execution_authorized field must exist only under boundary_flags",
    "payload_kind": "placement_review_result",
    "payload": {
      "execution_authorized": false,
      "boundary_flags": {
        "execution_authorized": false
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
