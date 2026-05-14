# Quickstart

## Local Installation

When copying this template into a local project, you must ensure hidden dotfiles (`.agentos/` and `.github/`) are copied.

Use a dotfile-preserving command:

```bash
cp -a templates/agentos-clean/. <target>/
```

Do not use `cp -r * <target>/` as it will skip the required dotfiles.

## Local Usage

If you have a local environment set up:

1. Create a task:
   \`python3 agentos/scripts/new-task.py "Task title"\`

2. Run validation:
   \`python3 agentos/scripts/agentos-validate.py all\`

## GitHub Usage

1. Go to Issues.
2. New issue → AgentOS Task Request.
3. Label as \`agentos-task\`.
