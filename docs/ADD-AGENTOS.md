# Add AgentOS to an Existing Project

> Status: Draft.
>
> This flow requires `scripts/install-agentos.py`.
> Do not publish this guide as a stable user path until the installer exists and passes validation.

AgentOS can be added to an existing Git repository safely.

The default path is:

```text
dry-run → install plan → review → apply
```

Dry-run does not modify your project.

AgentOS installs into its own namespace:
agentos/
.agentos/

agentos/ contains AgentOS docs, templates, scripts, tasks, and reports.
.agentos/ contains local AgentOS config and runtime state. Runtime/cache files inside .agentos/ should not become source of truth.

AgentOS must not overwrite existing project files, modify source code, commit, push, or approve actions automatically.

---

Step 0 — Get AgentOS Installer

Choose one option.

Option A — Clone AgentOS next to your project

From the parent folder that contains your project:
```bash
git clone https://github.com/NMF13579/AgentOS.git
cd your-project
```
Then run the dry-run command from your project root:
```bash
python3 ../AgentOS/scripts/install-agentos.py --target . --dry-run
```
Expected folder layout:
```text
parent-folder/
  your-project/
  AgentOS/
```

Option B — Clone AgentOS into a temporary installer folder

From your project root:
```bash
git clone https://github.com/NMF13579/AgentOS.git .agentos-installer
python3 .agentos-installer/scripts/install-agentos.py --target . --dry-run
```
After installation, you may delete .agentos-installer/ manually after review.
Do not delete .agentos/. That is the local AgentOS config/runtime folder.

---

Step 1 — Create an Install Plan

Run dry-run first.

If you used Option A:
```bash
python3 ../AgentOS/scripts/install-agentos.py --target . --dry-run
```
If you used Option B:
```bash
python3 .agentos-installer/scripts/install-agentos.py --target . --dry-run
```
This checks:
* whether the target is a Git repository;
* whether AgentOS is already installed;
* whether agentos/ or .agentos/ already exist;
* whether AgentOS can be added without overwriting files;
* whether Simple Mode will remain the default;
* whether Full Mode grants no extra permissions.

Dry-run creates an install plan.
Dry-run must not modify your project.

---

Step 2 — Review the Install Plan

Continue only if the install plan is safe.

Blocking conflicts:
* agentos/ exists
* .agentos/ exists

Warnings, not blockers:
* README.md exists
* .github/ exists
* docs/ exists
* scripts/ exists
* tasks/ exists
* reports/ exists

These are warnings because AgentOS does not install into those project folders during existing-project integration.
AgentOS does not merge into an existing agentos/ or .agentos/ folder in this version.
If a blocking conflict exists, stop and review manually.

---

Step 3 — Apply Only If Safe

If the dry-run plan is safe, run apply explicitly.

If you used Option A:
```bash
python3 ../AgentOS/scripts/install-agentos.py --target . --apply
```
If you used Option B:
```bash
python3 .agentos-installer/scripts/install-agentos.py --target . --apply
```
Apply may copy new AgentOS files only to paths that do not already exist.

Apply must not:
* overwrite existing files;
* delete files;
* modify source code;
* modify existing CI;
* modify deployment files;
* modify package files;
* commit;
* push;
* approve actions;
* enable Full Mode by default;
* grant the agent extra permissions.

---

After Install

Review the added files:
```bash
git status
```
Expected new folders:
```text
agentos/
.agentos/
```
If everything is correct, commit manually:
```bash
git add agentos .agentos
git commit -m "chore: add AgentOS"
```
Push only after review:
```bash
git push
```
If you used Option B, you may delete .agentos-installer/ manually after review.

---

Modes

AgentOS starts in Simple Mode.

| Mode | What you see | Extra agent permissions |
|---|---|---|
| Simple | Current task, risk, next safe action, validation result | No |
| Advanced | More validation details, report links, troubleshooting details | No |
| Full | Policies, advanced templates, audit/context internals | No |

Advanced and Full modes can be enabled later by explicit user choice.
Full Mode does not grant the agent extra permissions.

---

What AgentOS Does Not Claim

AgentOS does not claim:
* production readiness;
* production-grade sandboxing;
* guaranteed safe AI output;
* bug-free AI output;
* automatic approval safety;
* destructive workflow support;
* SaaS readiness.

AgentOS is a repo-based guardrail framework for AI coding workflows.
