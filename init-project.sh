#!/usr/bin/env bash
# init-project.sh — Initialize a new project from AgentOS template
# Usage: bash init-project.sh "My Project Name"
# Run ONCE after cloning. IRREVERSIBLE.
set -euo pipefail

RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'
BLUE='\033[0;34m'; BOLD='\033[1m'; RESET='\033[0m'
ok()   { echo -e "${GREEN}[OK]${RESET}  $*"; }
info() { echo -e "${BLUE}[..]${RESET}  $*"; }
warn() { echo -e "${YELLOW}[!!]${RESET}  $*"; }

PROJECT_NAME="${1:-}"
if [[ -z "$PROJECT_NAME" ]]; then
  echo "Usage: bash init-project.sh \"My Project Name\""; exit 1
fi

echo -e "\n${BOLD}AgentOS — New Project Init${RESET}"
echo -e "Project: ${BLUE}${PROJECT_NAME}${RESET}\n"
warn "This will reset all template data."
read -rp "Continue? (yes/no): " CONFIRM
[[ "$CONFIRM" != "yes" ]] && echo "Aborted." && exit 0

# 1. VERSION
info "[1/8] VERSION → 0.1.0"
echo "0.1.0" > VERSION && ok "done"

# 2. README
info "[2/8] Writing README.md..."
cat > README.md << READMEEOF
# ${PROJECT_NAME}

> Powered by [AgentOS](https://github.com/NMF13579/AgentOS)

## Getting Started
1. Read \`llms.txt\` — agent startup entry point
2. Read \`ARCHITECTURE.md\` — runtime module structure
3. Create your first task in \`tasks/active-task.md\`

## Runtime Spine
\`\`\`
llms.txt → core-rules/ → state/ → workflow/ → quality/ → security/
\`\`\`
READMEEOF
ok "README.md written"

# 3. CHANGELOG
info "[3/8] Resetting CHANGELOG.md..."
cat > CHANGELOG.md << 'CHANGELOGEOF'
# Changelog

## [Unreleased]
- Initial project setup from AgentOS template
CHANGELOGEOF
ok "done"

# 4. active-task.md → idle
info "[4/8] Resetting tasks/active-task.md..."
[[ -f tasks/active-task.md ]] && cat > tasks/active-task.md << 'ACTIVETASKEOF'
---
status: none
---

# Active Task

No active task yet.
ACTIVETASKEOF
ok "tasks/active-task.md → idle"

# 5. Clear task history
info "[5/8] Clearing task history..."
find tasks -maxdepth 1 -type d -name "task-*" -exec rm -rf {} + 2>/dev/null || true
for dir in tasks/done tasks/drafts tasks/dropped tasks/queue; do
  [[ -d "$dir" ]] && find "$dir" -type f ! -name ".gitkeep" -delete && touch "$dir/.gitkeep"
done
ok "done"

# 6. Clear runtime data
info "[6/8] Clearing reports/ handoff/ memory-bank/ incidents/ lessons/..."
for dir in reports handoff memory-bank incidents lessons; do
  [[ -d "$dir" ]] && find "$dir" -type f ! -name ".gitkeep" ! -name "README.md" -delete && touch "$dir/.gitkeep"
done
ok "done"

# 7. Remove LAYER-1
info "[7/8] Removing legacy LAYER-1/..."
[[ -d LAYER-1 ]] && rm -rf LAYER-1 && ok "LAYER-1/ removed" || echo "    not found — skip"

# 8. Remove macOS artifacts
info "[8/8] Removing macOS copy artifacts..."
find . -not -path "./.git/*" -type f \( -name "* 3.md" -o -name "* 2.md" \) -delete 2>/dev/null || true
ok "done"

echo -e "\n${GREEN}${BOLD}✓ Project '${PROJECT_NAME}' is ready!${RESET}"
echo -e "\nNext:\n  git add -A\n  git commit -m 'chore: init project ${PROJECT_NAME}'\n  git push\n"
