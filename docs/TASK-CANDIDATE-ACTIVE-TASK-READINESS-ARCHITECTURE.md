---
type: architecture
milestone: M55
task: 55.1
title: Task Candidate Active-Task Readiness Architecture
status: draft
authority: architecture
created_for: M55
source_intake: reports/m55-m54-readiness-intake.md
active_task_replacement_authorized: false
execution_authorized: false
approval_created: false
m56_authorized: false
m56_started: false
---

# Task Candidate Active-Task Readiness Architecture

## 1. Purpose

This document defines M55 as the Controlled Active-Task Readiness Layer.

M55 determines whether a queue entry may be considered for active-task proposal readiness.

M55 architecture does not authorize active-task replacement, approval, execution, or M56.

## 2. M55 Position in the Pipeline

M54 completion review
-> queue entry
-> active-task readiness input
-> active-task proposal contract
-> readiness policy
-> readiness CLI
-> readiness result
-> integration
-> evidence
-> completion review

M55 sits between controlled queue placement and execution readiness.

M55 does not replace `tasks/active-task.md`.

## 3. Core Boundary

Queue entry is not active task.
Active-task readiness is not active-task replacement.
Active-task readiness is not execution.
Active-task readiness is not approval.
Active-task readiness does not authorize M56.

## 4. Active-Task Proposal Boundary

active_task_proposal is a schema/template/result concept only.
active_task_proposal does not exist as a file in tasks/.
active_task_proposal must not create or modify tasks/active-task.md.
active_task_proposal must not create or modify tasks/queue/*.md.
active_task_proposal must not create approvals.

Active-task proposal describes possible readiness shape; it does not perform lifecycle mutation.

## 5. M55 Pipeline

- 55.2 — Queue Entry Intake Contract
- 55.3 — Active-Task Proposal Contract
- 55.4 — Active-Task Readiness Output Contract
- 55.5 — Active-Task Readiness Policy
- 55.6 — Active-Task Readiness CLI
- 55.7.1 — Active-Task Readiness Positive Fixtures
- 55.7.2 — Active-Task Readiness Negative Fixtures
- 55.8 — Active-Task Readiness Fixture Integration
- 55.9 — Active-Task Readiness Usage Examples
- 55.10 — Active-Task Readiness Controlled Integration
- 55.11 — Active-Task Readiness Evidence Report
- 55.12 — Active-Task Readiness Lesson Entry
- 55.13 — M55 Completion Review

No M55 architecture section authorizes downstream task execution.

## 6. Authority Model

- active_task_replacement_authorized: false
- execution_authorized: false
- approval_created: false
- m56_authorized: false
- m56_started: false

M55 architecture is descriptive authority only.

M55 architecture cannot approve, execute, activate, or start M56.

## 7. Carry-Forward Boundary

M54 limitations must remain visible in M55 readiness contracts and results.

Carry-forward material must not be converted into approval.

Limitations do not authorize active-task replacement.

## 8. Future Contract Stack

- docs/TASK-CANDIDATE-ACTIVE-TASK-READINESS-INPUT-CONTRACT.md
- docs/ACTIVE-TASK-PROPOSAL-CONTRACT.md
- docs/TASK-CANDIDATE-ACTIVE-TASK-READINESS-OUTPUT-CONTRACT.md
- docs/TASK-CANDIDATE-ACTIVE-TASK-READINESS-POLICY.md

Task 55.1 names future contracts but does not create them.

## 9. Future CLI Boundary

The future M55 CLI must be read-only.

The future M55 CLI must not write to tasks/active-task.md, tasks/queue/, approvals/, or M56 artifacts.

The future M55 CLI must not include a fixture mode; fixture integration belongs to 55.8.

## 10. Integration Boundary

M55 controlled integration may create readiness evidence only.

M55 controlled integration must not replace active-task.md.

M55 controlled integration must not create M55 completion review.

## 11. Evidence Boundary

M55 evidence is not approval.

M55 evidence does not authorize execution.

M55 evidence does not authorize active-task replacement.

M55 evidence does not authorize M56.

## 12. M56 Boundary

M56 must independently validate execution readiness.
M55 completion does not authorize M56 execution.
M55 readiness does not start M56.
M55 readiness does not create M56 artifacts.

## 13. Non-Authority Markers

M55 architecture is not approval.
M55 architecture does not authorize execution.
M55 architecture does not authorize active-task replacement.
M55 architecture does not create approval records.
M55 architecture does not authorize M56.
M55 architecture does not start M56.

## 14. Forbidden Mutations

Task 55.1 did not inspect queue entries.
Task 55.1 did not inspect active-task state.
Task 55.1 did not inspect approvals.
Task 55.1 did not inspect generated artifacts.
Task 55.1 did not modify tasks/active-task.md.
Task 55.1 did not create active-task proposal as a real file in tasks/.
Task 55.1 did not create approval records.
Task 55.1 did not authorize execution.
Task 55.1 did not authorize M56.

## 15. Summary

M55 defines active-task readiness only.

It does not replace active-task.md.
It does not approve a task.
It does not execute a task.
It does not create approval records.
It does not authorize M56.
