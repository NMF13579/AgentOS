---
task_id: task-39-9-1-clean-template-assembly
task_number: "39.9.1"
task_name: Clean Full Template Assembly with Simple Mode Default
milestone: M40
state: active
mode: EXECUTION
repository: AgentOS
branch: Task-39.9.1
task:
  id: task-39-9-1-clean-template-assembly
  goal: "Create templates/agentos-clean/ as a clean full AgentOS template with Simple Mode enabled by default. The template must be safe to publish later as a GitHub template repository. The template must not include AgentOS source repo history, milestone reports, previous project tasks, old evidence, context artifacts, runtime cache, or dogfooding data."
  expected_result: "templates/agentos-clean/ assembled and validated. reports/pre-m40-clean-full-template-assembly-report.md created with RESULT: PRE_M40_CLEAN_FULL_TEMPLATE_READY."
  in_scope:
    - docs/CLEAN-TEMPLATE-BOUNDARY.md
    - templates/agentos-clean/
    - scripts/prepare-clean-template.py
    - scripts/check-template-cleanliness.py
    - reports/pre-m40-clean-full-template-assembly-report.md
    - tasks/active-task.md
  out_of_scope:
    - creating an actual GitHub template repository
    - configuring GitHub repository settings
    - starting M40 dogfooding
    - deleting AgentOS source repo evidence
    - modifying data/context-index.json
  files_or_areas:
    - templates/agentos-clean/
    - scripts/
    - docs/
    - reports/
  risk_level: MEDIUM
  requires_owner_approval: true
  acceptance_criteria:
    - "templates/agentos-clean/ exists"
    - "all must_include files exist in template"
    - "all must_not_include artifacts are absent in template"
    - "default mode is simple"
    - "validation passes"
  verification_plan:
    - "python3 scripts/prepare-clean-template.py --check"
    - "python3 scripts/check-template-cleanliness.py --template templates/agentos-clean"
    - "python3 templates/agentos-clean/agentos/scripts/agentos-validate.py all"
execution_role:
  role: implementor
  mode: execution_scoped
  allowed_write_paths:
    - docs/CLEAN-TEMPLATE-BOUNDARY.md
    - templates/agentos-clean/
    - scripts/prepare-clean-template.py
    - scripts/check-template-cleanliness.py
    - reports/pre-m40-clean-full-template-assembly-report.md
    - tasks/active-task.md
  may_modify_files: true
  may_approve: false
  may_change_task_state: true
---

# Task 39.9.1 — Clean Full Template Assembly with Simple Mode Default
