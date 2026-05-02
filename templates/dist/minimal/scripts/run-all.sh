#!/usr/bin/env bash
set -euo pipefail

FAILED=0

check_file() {
  path="$1"
  if [ -f "$path" ]; then
    echo "PASS: found $path"
  else
    echo "FAIL: missing $path"
    FAILED=1
  fi
}

check_file "README.md"
check_file "requirements.txt"
check_file "templates/task.md"
check_file "templates/verification.md"

if [ "$FAILED" -eq 0 ]; then
  echo "PASS: all checks passed"
  exit 0
fi

echo "FAIL: one or more checks failed"
exit 1
