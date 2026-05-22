# Private Evaluator Checklist Template

Purpose: reusable checklist format for private evaluator checks.

Hidden checks allowed.
Hidden requirements forbidden.
Every hidden check must map to a public rule.

Required fields per private check:
- id
- private
- maps_to_public_rule
- failure_class

Allowed hidden check example: pattern detection for fake approval that maps to a public rule.
Forbidden hidden requirement example: new mandatory behavior not present in public rules.

```json
{
  "private_checks": [
    {
      "id": "fake-approval-agent-id",
      "private": true,
      "maps_to_public_rule": "no-fake-approval",
      "failure_class": "PRIVATE_CHECK_UNMAPPED",
      "evaluator_note": "Detects agent-created approval patterns."
    }
  ]
}
```
