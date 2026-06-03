---
task:
  id: "m84.0"
  goal: "M84.0 M83 Completion Intake"
  expected_result: "reports/m84-m83-completion-intake.md created with blocked status"
  in_scope:
    - "Create reports/m84-m83-completion-intake.md"
  out_of_scope:
    - "Perform physical repo changes"
    - "Create M84 task briefs"
    - "Implement automation"
  files_or_areas:
    - "reports/m84-m83-completion-intake.md"
  risk_level: "LOW"
  requires_owner_approval: false
  acceptance_criteria:
    - "M83 Completion Review Intake verified (blocks M84.0)"
    - "reports/m84-m83-completion-intake.md created"
    - "M84_0_STATUS set to BLOCKED"
    - "may_prepare_84_1_source_inventory set to false"
  verification_plan:
    - "Run validation commands specified in task brief"
---
