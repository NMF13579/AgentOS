---
task_id: task-m36-external-mvp-usability-intake
task_number: "36.1.1"
task_name: M36 External MVP Usability Intake and Scope Lock
milestone: M36
state: active
mode: EXECUTION
repository: AgentOS
branch: dev
scope_control:
  allowed_paths:
    - reports/m36-external-mvp-usability-intake.md
  forbidden_paths:
    - tasks/active-task.md
    - scripts/
    - docs/
    - templates/
    - examples/
    - prompts/
    - data/
    - tests/
    - schemas/
    - VERSION
    - CHANGELOG.md
    - README.md
  allowed_actions:
    - read_m35_completion_review
    - read_m35_evidence
    - inspect_existing_usability_surface
    - create_m36_usability_intake_report
  forbidden_actions:
    - execute_m36_implementation
    - modify_active_task
    - modify_docs
    - modify_scripts
    - modify_templates
    - modify_examples
    - modify_prompts
    - run_install_smoke
    - run_example_smoke
    - run_full_validation
    - stage
    - commit
    - push
---

# Task 36.1.1 — M36 External MVP Usability Intake and Scope Lock

M36 starts after M35 completion review concluded:

- M35_MVP_READY or M35_MVP_READY_WITH_GAPS
- M35_COMPLETION_REVIEW_COMPLETE
- READY_FOR_M36 or READY_FOR_M36_WITH_GAPS

M36 purpose:

Make AgentOS understandable, installable, and usable by a first external user without the author nearby.

This task is intake and scope-lock only.

It must create:

- reports/m36-external-mvp-usability-intake.md

It must identify the external MVP usability surface and lock the scope for the next M36 tasks.

M36 must focus on external MVP usability.

Do not add new guardrail layers.

Do not build web UI, cloud/server platform, vector DB, multi-agent orchestration, or M37 features.
