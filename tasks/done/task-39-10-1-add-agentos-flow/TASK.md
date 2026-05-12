---
task_id: task-39-10-1-add-agentos-flow
task_number: "39.10.1"
task_name: Add AgentOS to Existing Project Flow
milestone: M40
state: active
mode: EXECUTION
repository: AgentOS
branch: Task-39.10.1
task:
  id: task-39-10-1-add-agentos-flow
  goal: "Implement scripts/install-agentos.py and docs/ADD-AGENTOS.md to allow adding AgentOS to existing projects safely."
  expected_result: "Installer implemented, documentation created, README updated, and installer validated (dry-run/apply)."
  in_scope:
    - docs/ADD-AGENTOS.md
    - scripts/install-agentos.py
    - README.md
    - tasks/active-task.md
  out_of_scope:
    - modifying target project source code
    - automatic commits or pushes
  risk_level: MEDIUM
  requires_owner_approval: true
---
# Task 39.10.1 — Add AgentOS to Existing Project Flow
