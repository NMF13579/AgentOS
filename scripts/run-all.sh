#!/usr/bin/env bash
# run-all.sh — Full pipeline: validate → fix → re-validate
# Usage: ./run-all.sh [repo_root]

set -euo pipefail

REPO="${1:-.}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FINAL_EXIT=0

echo "╔═══════════════════════════════════════╗"
echo "║   Adapter Pipeline v1.2.1             ║"
echo "╚═══════════════════════════════════════╝"
echo ""

echo "── Step 1: Validate ─────────────────────"
"$SCRIPT_DIR/validate-adapters.sh" "$REPO" --json > "$REPO/report.json" || true
"$SCRIPT_DIR/validate-adapters.sh" "$REPO" || true
echo ""

echo "── Step 2: Auto-fix ─────────────────────"
"$SCRIPT_DIR/fix-adapters.sh" "$REPO/report.json" "$REPO"
echo ""

echo "── Step 3: Re-validate ──────────────────"
"$SCRIPT_DIR/validate-adapters.sh" "$REPO" --json > "$REPO/report-final.json" || true
"$SCRIPT_DIR/validate-adapters.sh" "$REPO" || FINAL_EXIT=$?

echo ""
if [[ "$FINAL_EXIT" -eq 0 ]]; then
  echo "✅ Pipeline complete. All hard errors resolved."
else
  echo "❌ Hard errors remain — manual fix required."
  echo "   See: report-final.json"
  exit 1
fi
