#!/bin/bash
# Auto-sync context pack before push — prevents stale hash failures
set -e

echo "→ Syncing context index..."
python3 scripts/build-context-index.py 2>/dev/null && echo "  ✓ index OK" || echo "  ⚠ index warnings (non-blocking)"

# Пересобери context pack если есть active task
if [ -f tasks/active-task.md ]; then
  STATE=$(grep "^state:" tasks/active-task.md | head -1 | awk '{print $2}')
  if [ "$STATE" != "completed" ]; then
    python3 scripts/select-context.py tasks/active-task.md 2>/dev/null || true
  fi
fi

# Закоммить изменения data/ если есть
git add data/ reports/context-pack.md reports/context-selection-record.md 2>/dev/null || true
if ! git diff --cached --quiet; then
  git commit -m "chore: auto-sync context pack [skip ci]"
  echo "  ✓ context pack updated"
fi
