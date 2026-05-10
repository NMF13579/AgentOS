# AgentOS Quickstart

Welcome to AgentOS! This guide will help you verify your setup and start your first task.

**Current Stage:** Milestone 39 — Public MVP Release Candidate.

If you have not yet installed AgentOS into your project, please complete the steps in the [Installation Guide](installation.md) first.

## 1. Verify Your Setup (First Validation)

Depending on which template you installed (`--minimal` or `--full`), run the appropriate first validation command to ensure all schemas and templates are correctly in place.

**For Minimal Template:**
```bash
python3 scripts/validate-task.py tasks/active-task.md
bash scripts/run-all.sh
```

**For Full Template:**
```bash
python3 scripts/agentos-validate.py all
python3 scripts/audit-mvp-readiness.py
```

## 2. Understanding the Output

AgentOS validation tools will return one of these standard results:

- **PASS:** The checked area passed completely. You are safe to proceed.
- **PASS_WITH_WARNINGS:** The checked area is usable, but known (non-blocking) gaps remain.
- **WARNING:** Something should be reviewed, but it may not block first use.
- **BLOCKED:** Execution or readiness is stopped. Continuing would be unsafe.
- **NOT_READY:** The system is not at the eligible level for the claimed use yet.
- **INCONCLUSIVE:** The check did not produce trustworthy evidence.

## 3. What to do if validation fails

If you see a `FAIL` or `BLOCKED` result:
- Do **not** treat failure as success.
- Read the terminal output. AgentOS is designed to tell you exactly which file or schema caused the issue.
- Check the generated reports in the `reports/` directory for detailed breakdown.
- Fix **only** the scoped blocker mentioned in the error.
- Rerun the exact same validation command to verify the fix.
- Do **not** proceed to release, publish, merge, or deployment based on failed validation.

## 4. What to do after success

If validation passes:
- Open `tasks/active-task.md`. This is the single source of truth for what your AI assistant is currently allowed to do.
- Proceed to the [First Project Onboarding Guide](first-project-onboarding.md) for a step-by-step tutorial on starting your first actual task.
- Look at the example project (if available) by running `bash scripts/test-example-project.sh` to see how a healthy project looks.
- Remember: Keep human approval for any risky actions (like deployments or large refactors).

## 5. Explicit Non-Goals

While using AgentOS, remember that it does **not** provide:
- A web UI, dashboard, or cloud/server platform.
- A marketplace or hosted service.
- Pip/npm packaging.
- A vector DB or full RAG backend.
- LangGraph, CrewAI, multi-agent orchestration, or a self-heal platform.
- Production deployment approval (AgentOS validates the process, but you must approve the release).

## Safety Boundaries Reminder

- Validation result `PASS` does not automatically mean your application is a candidate for production.
- `NOT_RUN` is not `PASS`. A check that was not run provides no evidence.
- AgentOS is not autonomous. Human review is required for all execution decisions.
