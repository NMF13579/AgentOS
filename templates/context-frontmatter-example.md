---
type: policy
module: runtime-boundary
status: canonical
authority: canonical
created: 2026-05-07
last_validated: 2026-05-07
tags: [m27, runtime, guard, no-direct-execution]
context_role: required_when_relevant
summary: "Defines no-direct-execution runtime boundary."
applies_to:
  - "scripts/runtime/**"
  - "docs/M27-*"
excludes:
  - ".github/workflows/**"
---

# Title

This file is eligible for M28 context selection when task tags, module, risk, or affected paths match this context.

---
type: lesson
module: scope-control
status: active
authority: supporting
created: 2026-05-07
last_validated: 2026-05-07
tags: [scope, drift, verification]
context_role: required_when_relevant
summary: "Lesson about preventing scope drift during implementation."
related_tasks:
  - task-example
related_lessons: []
---

# Lesson Title

This lesson is eligible for M28 context selection when task scope, verification, or drift-related tags match.
