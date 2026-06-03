---
task:
  id: "m82.9"
  goal: "M82.9 Archive Reduction Debt Closure Decision"
  expected_result: "reports/m82-archive-reduction-debt-closure.md created with final no-action closure decision"
  in_scope:
    - "Create reports/m82-archive-reduction-debt-closure.md"
  out_of_scope:
    - "Claim M82 reduction succeeded"
    - "Start M83 recovery"
    - "Unblock M84"
    - "Archive or move files"
  files_or_areas:
    - "reports/m82-archive-reduction-debt-closure.md"
  risk_level: "LOW"
  requires_owner_approval: true
  acceptance_criteria:
    - "M82.7R no-safe-candidate result verified"
    - "Human closure decision verified from current task prompt"
    - "Archive reduction debt closed as no-action for this line"
    - "Only reports/m82-archive-reduction-debt-closure.md created"
  verification_plan:
    - "Run validation commands specified in task brief"
---
