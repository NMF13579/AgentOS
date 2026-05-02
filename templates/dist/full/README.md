# [your project name] Full Template

## What this template is
This is a full Markdown-first template for teams that want task execution, verification, supporting docs, and example guidance.

## How this differs from minimal
The full template includes `docs/` and `examples/` in addition to task and verification templates.

## How to use it
1. Copy this template into your project.
2. Use `templates/task.md` to define work.
3. Use `templates/verification.md` to record evidence.
4. Use docs and examples for onboarding.
5. Run local checks:

```bash
bash scripts/run-all.sh
```

## How docs and examples are used
- `docs/` explains architecture, guardrails, limitations, and troubleshooting.
- `examples/` shows a simple safe workflow.

## Rule priority
Source-of-truth rules and task contracts override prompt packs and helper guidance.

## Safety boundaries
- Validation PASS does not mean production-ready.
- NOT_RUN is not PASS.
- This template is not a backend, not autonomous, not bug-free.
- Human review required for all execution decisions.
