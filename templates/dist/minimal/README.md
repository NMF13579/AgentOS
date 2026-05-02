# [your project name] Minimal Template

## What this template is
This is a small, Markdown-first template for teams that want a simple, controlled workflow for task execution and verification.

## What it includes
- `templates/task.md` for task contracts
- `templates/verification.md` for verification reports
- `scripts/run-all.sh` for local checks
- `requirements.txt` for optional local dependencies

## How to use it
1. Copy this template into your project.
2. Fill `templates/task.md` for your task.
3. Fill `templates/verification.md` after checks.
4. Run local validation:

```bash
bash scripts/run-all.sh
```

## What it does not include
This template is intentionally minimal and does not include extended docs or examples.

## Safety boundaries
- Validation PASS does not mean production-ready.
- NOT_RUN is not PASS.
- This template is not a backend, not autonomous, not bug-free.
- Human review required for all execution decisions.
