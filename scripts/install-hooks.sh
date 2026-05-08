#!/bin/bash
HOOK=.git/hooks/pre-commit
cat > "$HOOK" << 'EOF2'
#!/bin/bash
active=$(grep "task_id:" tasks/active-task.md 2>/dev/null | awk '{print $2}')
verif=$(grep "task_id:" reports/verification.md 2>/dev/null | awk '{print $2}')

if [ -z "$active" ] || [ -z "$verif" ]; then
  echo "WARN: task_id not found in one of the files, skipping check"
  exit 0
fi

if [ "$active" != "$verif" ]; then
  echo "ERROR: task_id mismatch"
  echo "  active-task:      $active"
  echo "  verification.md:  $verif"
  echo ""
  echo "Fix: update task_id in reports/verification.md"
  exit 1
fi
EOF2
chmod +x "$HOOK"
echo "Hook installed: $HOOK"
