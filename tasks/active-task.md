---
task:
  id: "m83.7"
  goal: "M83.7 M83 Completion Review"
  expected_result: "reports/m83-completion-review.md created with blocked status"
  in_scope:
    - "Create reports/m83-completion-review.md"
  out_of_scope:
    - "Perform physical repo changes"
    - "Create M84 task brief"
    - "Start M84"
  files_or_areas:
    - "reports/m83-completion-review.md"
  risk_level: "LOW"
  requires_owner_approval: false
  acceptance_criteria:
    - "M83.6 Intake verified (blocks M83.7)"
    - "reports/m83-completion-review.md created"
    - "FINAL_STATUS set to BLOCKED"
    - "may_prepare_m84 set to false"
  verification_plan:
    - "Run validation commands specified in task brief"
---
