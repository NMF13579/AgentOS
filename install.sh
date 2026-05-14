#!/usr/bin/env bash
# AgentOS Installer
#
# Запуск из внешнего проекта:
#   cd /path/to/your-project
#   bash /path/to/AgentOS/install.sh
#
# Что делает:
# - копирует clean template в текущий git-проект
# - не перезаписывает существующие файлы
# - сохраняет dotfiles (.agentos/, .github/)
# - показывает план перед установкой
# - спрашивает подтверждение
# - создаёт install report без silent overwrite
# - запускает проверку установки, если validator доступен

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_DIR="$(pwd)"
TEMPLATE_DIR="$SCRIPT_DIR/templates/agentos-clean"

GREEN="\033[0;32m"
YELLOW="\033[1;33m"
RED="\033[0;31m"
BOLD="\033[1m"
RESET="\033[0m"

pass() { echo -e "${GREEN}✓${RESET}  $1"; }
warn() { echo -e "${YELLOW}⚠${RESET}  $1"; }
fail() { echo -e "${RED}✗${RESET}  $1"; exit 1; }
info() { echo -e "   $1"; }

echo ""
echo -e "${BOLD}AgentOS — установка в твой проект${RESET}"
echo "──────────────────────────────────────"
echo ""

# Проверка 1: шаблон существует
if [ ! -d "$TEMPLATE_DIR" ]; then
  fail "Не найден шаблон AgentOS: $TEMPLATE_DIR"
fi

# Проверка 2: запуск из git-проекта
if [ ! -d "$TARGET_DIR/.git" ]; then
  fail "Это не git-репозиторий. Перейди в папку своего проекта и повтори."
fi

# Защита: нельзя ставить AgentOS в сам AgentOS
if [ "$TARGET_DIR" = "$SCRIPT_DIR" ]; then
  fail "Нельзя устанавливать AgentOS в сам AgentOS. Перейди в свой внешний проект."
fi

pass "Папка проекта найдена: $(basename "$TARGET_DIR")"
info "Путь проекта: $TARGET_DIR"
echo ""

# Уже установлен?
if [ -d "$TARGET_DIR/agentos" ]; then
  warn "AgentOS уже установлен: папка agentos/ существует."
  info "Существующие файлы будут пропущены, не перезаписаны."
  echo ""
fi

# Сбор плана установки
TOTAL_FILES=0
TO_INSTALL=0
TO_SKIP=0

while IFS= read -r source_file; do
  relative_path="${source_file#$TEMPLATE_DIR/}"
  target_path="$TARGET_DIR/$relative_path"

  TOTAL_FILES=$((TOTAL_FILES + 1))

  if [ -e "$target_path" ]; then
    TO_SKIP=$((TO_SKIP + 1))
  else
    TO_INSTALL=$((TO_INSTALL + 1))
  fi
done < <(find "$TEMPLATE_DIR" -type f | sort)

echo -e "${BOLD}План установки:${RESET}"
info "Источник шаблона: $TEMPLATE_DIR"
info "Проект-получатель: $TARGET_DIR"
info "Файлов в шаблоне: $TOTAL_FILES"
info "Будет добавлено: $TO_INSTALL"
info "Будет пропущено, потому что уже существует: $TO_SKIP"
echo ""

echo -e "${BOLD}Что будет добавлено в проект:${RESET}"
info "• agentos/     — скрипты и документация AgentOS"
info "• .agentos/    — настройки AgentOS"
info "• .github/     — шаблон задач GitHub, если есть в template"
info "• tasks/       — папка для задач"
info "• reports/     — папка для отчётов"
echo ""
info "Твои существующие файлы НЕ будут перезаписаны."
echo ""

# Подтверждение через /dev/tty, чтобы работало стабильнее при pipe/stdin
CONFIRM=""
if [ -r /dev/tty ]; then
  printf "Продолжить установку? [y/N] " > /dev/tty
  read -r CONFIRM < /dev/tty
else
  read -r -p "Продолжить установку? [y/N] " CONFIRM
fi

case "$CONFIRM" in
  y|Y|yes|YES)
    ;;
  *)
    warn "Установка отменена пользователем."
    exit 0
    ;;
esac

echo ""

# Установка
INSTALLED=0
SKIPPED=0

while IFS= read -r source_file; do
  relative_path="${source_file#$TEMPLATE_DIR/}"
  target_path="$TARGET_DIR/$relative_path"
  target_dir="$(dirname "$target_path")"

  if [ -e "$target_path" ]; then
    SKIPPED=$((SKIPPED + 1))
    continue
  fi

  mkdir -p "$target_dir"
  cp "$source_file" "$target_path"
  INSTALLED=$((INSTALLED + 1))
done < <(find "$TEMPLATE_DIR" -type f | sort)

# Гарантируем базовые директории, даже если они были пустыми в template
mkdir -p \
  "$TARGET_DIR/tasks/queue" \
  "$TARGET_DIR/tasks/done" \
  "$TARGET_DIR/tasks/failed" \
  "$TARGET_DIR/reports" \
  "$TARGET_DIR/.agentos/runtime"

echo -e "${BOLD}Результат установки:${RESET}"
pass "Установлено файлов: $INSTALLED"

if [ "$SKIPPED" -gt 0 ]; then
  warn "Пропущено, потому что уже существует: $SKIPPED файлов"
fi

echo ""

# Авто-валидация
VALIDATION_RESULT="NOT_RUN"
VALIDATOR="$TARGET_DIR/agentos/scripts/agentos-validate.py"

if [ -f "$VALIDATOR" ]; then
  echo -e "${BOLD}Проверка установки...${RESET}"

  if python3 "$VALIDATOR" all; then
    echo ""
    pass "AgentOS успешно установлен и прошёл проверку."
    VALIDATION_RESULT="PASS"
  else
    echo ""
    warn "Установка завершена, но проверка вернула предупреждение или ошибку."
    info "Можно повторить вручную:"
    info "python3 agentos/scripts/agentos-validate.py all"
    VALIDATION_RESULT="FAILED_OR_WARNING"
  fi
else
  warn "Validator не найден: agentos/scripts/agentos-validate.py"
  VALIDATION_RESULT="VALIDATOR_NOT_FOUND"
fi

echo ""

# Install report без silent overwrite
mkdir -p "$TARGET_DIR/reports"

INSTALL_REPORT="$TARGET_DIR/reports/agentos-install-report.md"

if [ -e "$INSTALL_REPORT" ]; then
  REPORT_TIMESTAMP="$(date +%Y%m%d-%H%M%S)"
  INSTALL_REPORT="$TARGET_DIR/reports/agentos-install-report-$REPORT_TIMESTAMP.md"
  warn "Базовый install report уже существует."
  info "Новый отчёт будет создан как: reports/agentos-install-report-$REPORT_TIMESTAMP.md"
fi

cat > "$INSTALL_REPORT" <<EOF
# AgentOS Install Report

## Install Summary

- installer: install.sh
- template source: $TEMPLATE_DIR
- target project: $TARGET_DIR
- files in template: $TOTAL_FILES
- files installed: $INSTALLED
- files skipped_existing: $SKIPPED
- validation_result: $VALIDATION_RESULT

## Safety

- existing files overwritten: no
- dependency install performed: no
- deploy performed: no
- push performed: no
- commit performed: no

## Expected Folders

- agentos/
- .agentos/
- .github/
- tasks/
- reports/

## Next Step

Read:

\`\`\`text
agentos/docs/quickstart.md
\`\`\`

Then create a first task:

\`\`\`bash
python3 agentos/scripts/new-task.py "Название задачи"
\`\`\`

## Notes

This report is evidence of installation only.

It is not approval.
It is not validation authority.
It does not authorize commit, push, merge, deploy, or release.
EOF

RELATIVE_REPORT="${INSTALL_REPORT#$TARGET_DIR/}"
pass "Отчёт установки создан: $RELATIVE_REPORT"

echo ""
echo -e "${BOLD}Что делать дальше:${RESET}"
info "1. Прочитай: agentos/docs/quickstart.md"
info "2. Создай первую задачу:"
info "   python3 agentos/scripts/new-task.py \"Название задачи\""
echo ""

pass "Готово."