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

check_dir() {
  path="$1"
  if [ -d "$path" ]; then
    echo "PASS: found directory $path"
  else
    echo "FAIL: missing directory $path"
    FAILED=1
  fi
}

check_file "README.md"
check_file "requirements.txt"
check_file "templates/task.md"
check_file "templates/verification.md"
check_file "docs/architecture.md"
check_file "docs/guardrails.md"
check_file "docs/limitations.md"
check_file "docs/troubleshooting.md"
check_file "examples/README.md"
check_dir "docs"
check_dir "examples"

if [ "$FAILED" -eq 0 ]; then
  echo "PASS: all checks passed"
  exit 0
fi

echo "FAIL: one or more checks failed"
exit 1
