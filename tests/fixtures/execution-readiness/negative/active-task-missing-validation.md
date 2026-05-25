---
task_id: M56_NEGATIVE_ACTIVE_TASK
title: Negative Active Task Fixture
mode: EXECUTION
repository: NMF13579/AgentOS
branch: dev
execution_authorized: false
execution_started: false
approval_created: false
lifecycle_mutation_authorized: false
m57_authorized: false
m57_started: false
---

## Goal

This negative active-task fixture is test data only and does not authorize execution.

## Scope

Allowed to create:

```text
/tmp/m56-negative-output
```

Forbidden actions:

```text
Do not authorize M57.
Do not start M57.
```

## Expected Final Report

Return negative readiness report.

## Final Rule

Stop after negative fixture check.
