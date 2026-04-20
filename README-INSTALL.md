# Adapter System — Install Guide

## Куда класть файлы

| Файл | Путь в репозитории |
|---|---|
| `governed-repo.mdc` | `.cursor/rules/governed-repo.mdc` |
| `copilot-instructions.md` | `.github/copilot-instructions.md` |
| `AGENTS.md` | `AGENTS.md` |
| `CLAUDE.md` | `CLAUDE.md` |
| `GEMINI.md` | `GEMINI.md` |
| `dot-rules` | `.rules` (переименовать) |
| `validate-adapters.sh` | `scripts/validate-adapters.sh` |
| `fix-adapters.sh` | `scripts/fix-adapters.sh` |
| `run-all.sh` | `scripts/run-all.sh` |

## Быстрый старт

chmod +x scripts/*.sh

# Полный пайплайн одной командой:
scripts/run-all.sh .

# Или по шагам:
scripts/validate-adapters.sh .                       # читаемый вывод
scripts/validate-adapters.sh . --json > report.json  # JSON для CI
scripts/fix-adapters.sh report.json .                # авто-исправление
scripts/fix-adapters.sh report.json . --dry-run      # проверить без изменений
