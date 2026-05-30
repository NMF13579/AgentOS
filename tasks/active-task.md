---
id: task-72.6
milestone: M72
name: "Protected Change Policy"
status: active
mode: "POLICY CREATION / CHANGE RULES ONLY / NO CHANGE AUTHORIZATION"
branch: dev
started_at: "2026-05-29"
---

# Active Task: 72.6 — Protected Change Policy

## Purpose

Declare the active task identity for M72.6 protected change policy creation.

## Task Boundary

This file records the active task only.

It does not approve M72.

It does not modify protected artifact model.

It does not modify protected artifact registry.

It does not modify canonical artifact registry.

It does not modify ownership gap map.

It does not modify CODEOWNERS alignment review.

It does not modify CODEOWNERS.

It does not configure branch protection.

It does not create GitHub rulesets.

It does not claim platform enforcement.

It does not assign owners.

It does not resolve ownership gaps.

It does not authorize protected artifact changes.

It does not authorize canonical artifact changes.

It does not authorize cleanup.

It does not create protected artifact audit checklist.

It does not create registry evidence report.

It does not create M72 completion review.

It does not modify scripts.

It does not create JSON artifacts.

It does not mutate lifecycle state.

It does not start M72.7.

It authorizes only creation of one Markdown protected change policy.

## Current Task

72.6 — Protected Change Policy
Validate:
test -f tasks/active-task.md
grep -q "^id: task-72.6$" tasks/active-task.md
grep -q "^milestone: M72$" tasks/active-task.md
grep -q '^name: "Protected Change Policy"$' tasks/active-task.md
grep -q "^status: active$" tasks/active-task.md
grep -q '^mode: "POLICY CREATION / CHANGE RULES ONLY / NO CHANGE AUTHORIZATION"$' tasks/active-task.md
grep -q "^branch: dev$" tasks/active-task.md
