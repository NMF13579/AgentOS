#!/usr/bin/env bash
set -euo pipefail

echo "Removing duplicate template files with ' 3.md' suffix..."

rm -f \
  "templates/agent-permission-record 3.md" \
  "templates/agent-token-scope-review 3.md" \
  "templates/agent-violation-record 3.md" \
  "templates/command-approval-record 3.md" \
  "templates/command-guard-decision-record 3.md" \
  "templates/git-guard-decision-record 3.md" \
  "templates/validation-summary 3.md" \
  "templates/write-guard-decision-record 3.md"

echo "Done."
