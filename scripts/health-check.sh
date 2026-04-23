#!/usr/bin/env bash
# AgentOS Canonical Health Check
# STATUS: canonical
# Validates modular architecture — the current primary architecture.
# HEALTH: OK is only possible after checking the modular control plane.

set -euo pipefail
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ERRORS=0

echo "=== AgentOS Health Check (Canonical) ==="
echo ""

check_file() {
  local path="$1"
  local label="$2"
  if [[ -f "$REPO_ROOT/$path" ]]; then
    echo "  OK  $label"
  else
    echo "  FAIL  MISSING: $label ($path)"
    ERRORS=$((ERRORS + 1))
  fi
}

echo "--- Control plane entrypoints ---"
check_file "START.md"            "START.md"
check_file "llms.txt"            "llms.txt"
check_file "ROUTES-REGISTRY.md"  "ROUTES-REGISTRY.md"
check_file "architecture/CANON.md" "architecture/CANON.md"

echo ""
echo "--- Canonical modules (*/MAIN.md) ---"
MAIN_COUNT=0
for f in "$REPO_ROOT"/*/MAIN.md; do
  [[ -f "$f" ]] && MAIN_COUNT=$((MAIN_COUNT + 1))
done
if [[ $MAIN_COUNT -gt 0 ]]; then
  echo "  OK  Found $MAIN_COUNT */MAIN.md modules"
else
  echo "  FAIL  No */MAIN.md modules found"
  ERRORS=$((ERRORS + 1))
fi

echo ""
echo "--- Canonical validators ---"
if bash "$REPO_ROOT/scripts/validate-architecture.sh" > /dev/null 2>&1; then
  echo "  OK  validate-architecture.sh"
else
  echo "  FAIL  validate-architecture.sh"
  ERRORS=$((ERRORS + 1))
fi

if python3 "$REPO_ROOT/scripts/validate-route.py" > /dev/null 2>&1; then
  echo "  OK  validate-route.py"
else
  echo "  FAIL  validate-route.py"
  ERRORS=$((ERRORS + 1))
fi

if python3 "$REPO_ROOT/scripts/validate-docs.py" > /dev/null 2>&1; then
  echo "  OK  validate-docs.py"
else
  echo "  FAIL  validate-docs.py"
  ERRORS=$((ERRORS + 1))
fi

echo ""
if [[ $ERRORS -eq 0 ]]; then
  echo "HEALTH: OK — modular architecture validated"
  exit 0
else
  echo "HEALTH: FAIL — $ERRORS issue(s) found"
  exit 1
fi
