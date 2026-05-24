```json
{
  "negative_fixture": {
    "fixture_id": "m52-completion-blocked",
    "fixture_type": "DEPENDENCY_BLOCKER",
    "expected_result": "PLACEMENT_REVIEW_BLOCKED",
    "expected_exit_code": 2,
    "expected_blocker": "M52 final_status is M52_BLOCKED",
    "payload_kind": "m52_completion_review",
    "payload": {
      "final_status": "M52_BLOCKED",
      "m53_handoff_ready": false
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
