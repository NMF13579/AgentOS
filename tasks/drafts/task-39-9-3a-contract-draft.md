---
task_id: task-39-9-3a-safe-installer
task_number: "39.9.3a"
task_name: Existing Project Safe Installer Script
milestone: M40
state: active
mode: EXECUTION
repository: AgentOS
branch: Task-39.9.3a
task:
  id: task-39-9-3a-safe-installer
  goal: "Implement a robust and safe scripts/install-agentos.py for existing project integration."
  expected_result: "Installer script implemented with dry-run/apply modes, JSON support, and full safety checks. Report created with PRE_M40_INSTALL_SCRIPT_READY."
  in_scope:
    - scripts/install-agentos.py
    - reports/pre-m40-install-agentos-script-report.md
    - tasks/active-task.md
  out_of_scope:
    - user-facing documentation
    - root README updates
  risk_level: MEDIUM
  requires_owner_approval: true
---
# Task 39.9.3a — Existing Project Safe Installer Script
