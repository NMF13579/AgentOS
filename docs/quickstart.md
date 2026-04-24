# AgentOS Quickstart

## Requirements

- Git repository
- Bash
- Python 3
- pip

## Install minimal template

```bash
cd /path/to/your/git-project
bash /path/to/AgentOS/install.sh --minimal --dry-run
bash /path/to/AgentOS/install.sh --minimal
```

## Install full template

```bash
cd /path/to/your/git-project
bash /path/to/AgentOS/install.sh --full --dry-run
bash /path/to/AgentOS/install.sh --full
```

## Validate installation

```bash
pip install -r requirements.txt
bash scripts/run-all.sh
```

## Verify installer

Run the install smoke test:

```bash
bash scripts/test-install.sh
```

## Validate example project

Run the example project validation:

```bash
bash scripts/test-example-project.sh
```

## What gets installed

- `--minimal`: базовые схемы, task/report шаблоны и две проверки
- `--full`: весь текущий набор guardrails и вспомогательных файлов

## What is not included

- backend, RAG, vector DB, agent orchestration
- Docker image, pip package, npm package
