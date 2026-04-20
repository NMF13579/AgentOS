#!/usr/bin/env bash
# fix-adapters.sh — Adapter Auto-Fixer v1.2.1
# Usage: ./fix-adapters.sh [report.json] [repo_root] [--dry-run]

set -euo pipefail

REPORT="${1:-report.json}"
REPO="${2:-.}"
DRY_RUN=false
[[ "${3:-}" == "--dry-run" ]] && DRY_RUN=true

MINIMAL_REDIRECT='Read `llms.txt` and follow it. For behavior after load, use `LAYER-1/agent-rules.md`.'

FIXED=0
SKIPPED=0
MANUAL=0

log() { echo "$1"; }
log_dry() { $DRY_RUN && echo "  [DRY-RUN] $1" || true; }

fix_file() {
  local file="$1" code="$2"
  local abs="$REPO/$file"

  if [[ ! -f "$abs" ]]; then
    log "  ⚠️  File not found: $file — skipping"
    SKIPPED=$((SKIPPED+1))
    return
  fi

  case "$code" in

    MISSING_LLMS_REDIRECT)
      grep -q "llms\.txt" "$abs" && { log "  ✓ Already present"; SKIPPED=$((SKIPPED+1)); return; }
      log_dry "Would append redirect to $file"
      if ! $DRY_RUN; then
        echo "" >> "$abs"
        echo "$MINIMAL_REDIRECT" >> "$abs"
        log "  ✅ Added llms.txt redirect"
        FIXED=$((FIXED+1))
      fi
      ;;

    MISSING_AGENT_RULES_REDIRECT)
      grep -q "LAYER-1/agent-rules\.md" "$abs" && { log "  ✓ Already present"; SKIPPED=$((SKIPPED+1)); return; }
      log_dry "Would append agent-rules reference to $file"
      if ! $DRY_RUN; then
        if grep -q "llms\.txt" "$abs"; then
          sed -i.bak "/llms\.txt/a\\
For behavior after load, use \`LAYER-1/agent-rules.md\`." "$abs"
          rm -f "$abs.bak"
        else
          echo "" >> "$abs"
          echo "For behavior after load, use \`LAYER-1/agent-rules.md\`." >> "$abs"
        fi
        log "  ✅ Added agent-rules reference"
        FIXED=$((FIXED+1))
      fi
      ;;

    MISSING_META_ROLE)
      head -5 "$abs" | grep -q "ROLE: ADAPTER ENTRYPOINT" && { log "  ✓ Already present"; SKIPPED=$((SKIPPED+1)); return; }
      log_dry "Would prepend ROLE tag to $file"
      if ! $DRY_RUN; then
        tmp=$(mktemp)
        echo "<!-- ROLE: ADAPTER ENTRYPOINT -->" > "$tmp"
        cat "$abs" >> "$tmp"
        mv "$tmp" "$abs"
        log "  ✅ Added ROLE meta tag"
        FIXED=$((FIXED+1))
      fi
      ;;

    MISSING_META_AUTHORITY)
      head -5 "$abs" | grep -q "AUTHORITY: NON-AUTHORITY" && { log "  ✓ Already present"; SKIPPED=$((SKIPPED+1)); return; }
      log_dry "Would insert AUTHORITY tag to $file"
      if ! $DRY_RUN; then
        tmp=$(mktemp)
        if head -3 "$abs" | grep -q "ROLE: ADAPTER ENTRYPOINT"; then
          awk '/ROLE: ADAPTER ENTRYPOINT/{print; print "<!-- AUTHORITY: NON-AUTHORITY -->"; next}1' "$abs" > "$tmp"
        else
          echo "<!-- AUTHORITY: NON-AUTHORITY -->" > "$tmp"
          cat "$abs" >> "$tmp"
        fi
        mv "$tmp" "$abs"
        log "  ✅ Added AUTHORITY meta tag"
        FIXED=$((FIXED+1))
      fi
      ;;

    MISSING_META_SOT)
      head -5 "$abs" | grep -q "SOURCE_OF_TRUTH: no" && { log "  ✓ Already present"; SKIPPED=$((SKIPPED+1)); return; }
      log_dry "Would insert SOURCE_OF_TRUTH tag to $file"
      if ! $DRY_RUN; then
        tmp=$(mktemp)
        if head -4 "$abs" | grep -q "AUTHORITY: NON-AUTHORITY"; then
          awk '/AUTHORITY: NON-AUTHORITY/{print; print "<!-- SOURCE_OF_TRUTH: no -->"; next}1' "$abs" > "$tmp"
        elif head -3 "$abs" | grep -q "ROLE: ADAPTER ENTRYPOINT"; then
          awk '/ROLE: ADAPTER ENTRYPOINT/{print; print "<!-- SOURCE_OF_TRUTH: no -->"; next}1' "$abs" > "$tmp"
        else
          echo "<!-- SOURCE_OF_TRUTH: no -->" > "$tmp"
          cat "$abs" >> "$tmp"
        fi
        mv "$tmp" "$abs"
        log "  ✅ Added SOURCE_OF_TRUTH meta tag"
        FIXED=$((FIXED+1))
      fi
      ;;

    *)
      log "  🔧 Manual fix required for $code"
      MANUAL=$((MANUAL+1))
      ;;
  esac
}

# ─── Main ──────────────────────────────────────────────────────────────────

[[ ! -f "$REPORT" ]] && { echo "❌ Report not found: $REPORT"; exit 1; }

echo "═══════════════════════════════════════"
echo "  Adapter Auto-Fixer v1.2.1"
$DRY_RUN && echo "  Mode: DRY-RUN"
echo "  Report: $REPORT | Repo: $REPO"
echo "═══════════════════════════════════════"
echo ""

issues_count=$(jq '.issues | length' "$REPORT")
[[ "$issues_count" -eq 0 ]] && { echo "✅ No issues. Nothing to fix."; exit 0; }

for i in $(seq 0 $((issues_count-1))); do
  issue=$(jq -c ".issues[$i]" "$REPORT")
  code=$(echo "$issue" | jq -r '.code')
  auto_fixable=$(echo "$issue" | jq -r '.auto_fixable')
  locations_count=$(echo "$issue" | jq '.locations | length')

  for j in $(seq 0 $((locations_count-1))); do
    file=$(echo "$issue" | jq -r ".locations[$j].file")
    log "[$code] → $file"
    if [[ "$auto_fixable" == "true" ]]; then
      fix_file "$file" "$code"
    else
      log "  🔧 Manual fix required (not auto-fixable)"
      MANUAL=$((MANUAL+1))
    fi
  done
done

echo ""
echo "═══════════════════════════════════════"
echo "  Fixed: $FIXED | Skipped: $SKIPPED | Manual: $MANUAL"
echo "═══════════════════════════════════════"
[[ $MANUAL -gt 0 ]] && echo "⚠️  Re-run validator to see remaining issues."
exit 0
