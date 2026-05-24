```json
{
  "negative_fixture": {
    "fixture_id": "allowed-changes-expanded",
    "fixture_type": "AUTHORITY_ESCALATION_BLOCKER",
    "expected_result": "PLACEMENT_REVIEW_BLOCKED",
    "expected_exit_code": 2,
    "expected_blocker": "allowed changes expanded",
    "payload_kind": "placement_review_input",
    "payload": {
      "allowed_changes_expanded": true,
      "boundaries": {},
      "required_traceability": {},
      "required_carry_forward": {}
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
