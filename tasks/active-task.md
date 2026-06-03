---
task:
  id: "m86.4"
  goal: "M86.4 M86 Completion Review"
  expected_result: "reports/m86-completion-review.md created"
  in_scope:
    - "Create reports/m86-completion-review.md"
  out_of_scope:
    - "Continue M84"
    - "Reopen M83 recovery"
    - "Authorize physical cleanup"
    - "Start M87"
    - "Start M88"
  files_or_areas:
    - "reports/m86-completion-review.md"
  risk_level: "LOW"
  requires_owner_approval: true
  acceptance_criteria:
    - "All M86.0 through M86.3 artifacts reviewed"
    - "No cleanup, physical action, approval, or lifecycle mutation authorized"
    - "No M87 or M88 start detected"
    - "M87 preparation readiness decided under M86.4 contract"
  verification_plan:
    - "Run validation commands specified in task brief"
---
