# Installing AgentOS

AgentOS is designed to be installed directly into your existing Git repository. It adds a set of Markdown templates, validation scripts, and JSON schemas to act as a programmable guardrail layer for your AI workflows.

## 1. Prerequisites

Before installing AgentOS, ensure your system has:
- A working **Git repository** (you must run the installer from the root of your repo).
- **Bash** shell.
- **Python 3.10+**.
- **pip** (for installing dependencies if needed).

## 2. Choosing a Template

AgentOS offers two templates depending on your needs:

- **Minimal Template (`--minimal`):**
  Use this for your first trial, small projects, or learning AgentOS basics. It includes only the core schemas, basic task/verification templates, and essential validation scripts (`run-all.sh`).

- **Full Template (`--full`):**
  Use this when your project needs the complete guardrail structure. It includes advanced enforcement scripts, execution boundaries, release checklists, and full audit capabilities.

*If unsure: Start with the minimal template, then move to the full template after understanding the workflow.*

## 3. Installation Steps

You do not install AgentOS globally. You copy it into your specific project.

1. **Clone the AgentOS repository** somewhere on your machine:
   ```bash
   git clone https://github.com/NMF13579/AgentOS.git /path/to/AgentOS
   ```

2. **Navigate to your own project's root directory**:
   ```bash
   cd /path/to/your/git-project
   ```
   *(Ensure this directory has a `.git` folder).*

3. **Run the installation script** (Dry run first to see what will be copied):
   ```bash
   bash /path/to/AgentOS/install.sh --minimal --dry-run
   ```

4. **Perform the actual installation**:
   ```bash
   bash /path/to/AgentOS/install.sh --minimal
   ```

## 4. First Validation Command

Once installed, verify that the templates and scripts are correctly placed in your repository.

If you installed the **minimal template**, run:
```bash
bash scripts/run-all.sh
```

If you installed the **full template**, run the official full unified validation:
```bash
python3 scripts/agentos-validate.py all
```

## 5. Understanding the Results

When you run validation, you will see one of these results:

- **PASS:** The checked area passed completely.
- **PASS_WITH_WARNINGS:** The checked area is usable, but known (non-blocking) gaps remain.
- **WARNING:** Something should be reviewed, but it may not block first use.
- **BLOCKED:** Execution or readiness is stopped because continuing would be unsafe or unsupported.
- **NOT_READY:** The system is not ready for the claimed use yet.
- **INCONCLUSIVE:** The check did not produce trustworthy evidence.

## 6. What to do if validation fails

If a command fails:
- Do **not** treat failure as success.
- Read the command output carefully.
- Check the matching report generated under the `reports/` directory.
- Identify whether the result is BLOCKED, NOT_READY, WARNING, or INCONCLUSIVE.
- Fix only the scoped blocker mentioned in the error.
- Rerun the exact same command to verify the fix.
- Do **not** proceed to release, publish, merge, or deployment based on failed validation.

## 7. What to do after success

If your first validation passes:
- Inspect the generated or existing reports in the `reports/` folder.
- If available (full template), run the MVP readiness audit: `python3 scripts/audit-mvp-readiness.py`.
- Continue with a small scoped task using `tasks/active-task.md`.
- Keep human approval for any risky actions.

## 8. What NOT to do during first run

- Do **not** manually edit JSON schemas in `schemas/`.
- Do **not** bypass `scripts/run-all.sh` or `agentos-validate.py`.
- Do **not** assume AgentOS will write code for you autonomously.

## 9. Explicit Non-Goals

Please note that installing AgentOS does **not** give you:
- A web UI, dashboard, or cloud/server platform.
- A marketplace or hosted service.
- Pip/npm packaging (AgentOS is copied directly, not installed via package managers).
- A vector DB or full RAG backend.
- LangGraph, CrewAI, multi-agent orchestration, or a self-heal platform.
- Production deployment approval (AgentOS validates process, humans approve release).

## Next Steps
After a successful installation, proceed to the [Quickstart Guide](quickstart.md) to learn how to structure your first task.
