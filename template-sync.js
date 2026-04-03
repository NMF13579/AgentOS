#!/usr/bin/env node

/**
 * template-sync.js — синхронизация файлов из шаблона Vibe-coding-docs
 *
 * Использование:
 *   node template-sync.js <source> <target> [--dry-run]
 *
 * Опции:
 *   --dry-run   Показать что будет скопировано, ничего не менять
 *
 * Примеры:
 *   node template-sync.js ../vibe-coding-docs . --dry-run
 *   node template-sync.js ../vibe-coding-docs .
 */

const fs = require('fs');
const path = require('path');

// ─── Конфигурация ───────────────────────────────────────────────────────────

const IGNORE_PATTERNS = [
  '.git',
  'node_modules',
  '.env',
  '.env.local',
  '.env.*',
  '.DS_Store',
  'template-sync.js',
  'template-sync-report.md',
  'TEMPLATE-SYNC-GUIDE.md',
  'TEMPLATE-SYNC-INTEGRATION.md',
  'package-lock.json',
  'yarn.lock',
];

// Файлы которые НИКОГДА не копируются (специфичны для шаблона, не для проекта)
const NEVER_COPY = [
  'README.md',
  'CHANGELOG.md',
  'llms.txt',
];

// ─── Утилиты ────────────────────────────────────────────────────────────────

function shouldIgnore(name) {
  return IGNORE_PATTERNS.some(pattern => {
    if (pattern.includes('*')) {
      const regex = new RegExp('^' + pattern.replace('.', '\\.').replace('*', '.*') + '$');
      return regex.test(name);
    }
    return name === pattern;
  });
}

function shouldNeverCopy(relPath) {
  const basename = path.basename(relPath);
  return NEVER_COPY.includes(basename);
}

function walkDir(dir, base = dir, results = []) {
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const entry of entries) {
    if (shouldIgnore(entry.name)) continue;
    const fullPath = path.join(dir, entry.name);
    const relPath = path.relative(base, fullPath);
    if (entry.isDirectory()) {
      walkDir(fullPath, base, results);
    } else {
      results.push(relPath);
    }
  }
  return results;
}

function ensureDir(filePath) {
  const dir = path.dirname(filePath);
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
}

function formatSize(bytes) {
  if (bytes < 1024) return `${bytes}B`;
  return `${(bytes / 1024).toFixed(1)}KB`;
}

// ─── Основная логика ────────────────────────────────────────────────────────

function sync(sourceDir, targetDir, dryRun) {
  if (!fs.existsSync(sourceDir)) {
    console.error(`❌ Источник не найден: ${sourceDir}`);
    process.exit(1);
  }
  if (!fs.existsSync(targetDir)) {
    console.error(`❌ Целевая директория не найдена: ${targetDir}`);
    process.exit(1);
  }

  const sourceFiles = walkDir(sourceDir);

  const results = {
    copied: [],
    skipped_exists: [],
    skipped_never: [],
    errors: [],
  };

  for (const relPath of sourceFiles) {
    if (shouldNeverCopy(relPath)) {
      results.skipped_never.push(relPath);
      continue;
    }

    const targetPath = path.join(targetDir, relPath);

    if (fs.existsSync(targetPath)) {
      results.skipped_exists.push(relPath);
      continue;
    }

    if (!dryRun) {
      try {
        ensureDir(targetPath);
        fs.copyFileSync(path.join(sourceDir, relPath), targetPath);
        results.copied.push(relPath);
      } catch (err) {
        results.errors.push({ file: relPath, error: err.message });
      }
    } else {
      results.copied.push(relPath);
    }
  }

  return results;
}

function buildReport(results, sourceDir, targetDir, dryRun, startTime) {
  const elapsed = ((Date.now() - startTime) / 1000).toFixed(2);
  const date = new Date().toISOString().slice(0, 19).replace('T', ' ');
  const mode = dryRun ? 'DRY RUN (без изменений)' : 'ПРИМЕНЕНО';

  const lines = [
    `# Отчёт синхронизации шаблона`,
    ``,
    `**Дата:** ${date}`,
    `**Режим:** ${mode}`,
    `**Источник:** ${path.resolve(sourceDir)}`,
    `**Цель:** ${path.resolve(targetDir)}`,
    `**Время:** ${elapsed}s`,
    ``,
    `---`,
    ``,
    `## Итог`,
    ``,
    `| Статус | Кол-во |`,
    `|--------|--------|`,
    `| ✅ Скопировано (новые файлы) | ${results.copied.length} |`,
    `| ⏭️ Пропущено (файл уже есть) | ${results.skipped_exists.length} |`,
    `| 🚫 Исключено (системные) | ${results.skipped_never.length} |`,
    `| ❌ Ошибок | ${results.errors.length} |`,
    ``,
  ];

  if (results.copied.length > 0) {
    lines.push(`## ✅ ${dryRun ? 'Будет скопировано' : 'Скопировано'}`);
    lines.push(``);
    for (const f of results.copied) lines.push(`- \`${f}\``);
    lines.push(``);
  }

  if (results.skipped_exists.length > 0) {
    lines.push(`## ⏭️ Пропущено (уже существует)`);
    lines.push(``);
    for (const f of results.skipped_exists) lines.push(`- \`${f}\``);
    lines.push(``);
  }

  if (results.errors.length > 0) {
    lines.push(`## ❌ Ошибки`);
    lines.push(``);
    for (const e of results.errors) lines.push(`- \`${e.file}\`: ${e.error}`);
    lines.push(``);
  }

  return lines.join('\n');
}

// ─── CLI ────────────────────────────────────────────────────────────────────

function main() {
  const args = process.argv.slice(2);

  if (args.length < 2 || args.includes('--help') || args.includes('-h')) {
    console.log([
      'Использование: node template-sync.js <source> <target> [--dry-run]',
      '',
      'Аргументы:',
      '  source    Путь к репозиторию Vibe-coding-docs (шаблон)',
      '  target    Путь к целевому проекту',
      '',
      'Опции:',
      '  --dry-run   Показать что будет скопировано, ничего не менять',
      '  --help      Показать эту справку',
      '',
      'Примеры:',
      '  node template-sync.js ../vibe-coding-docs . --dry-run',
      '  node template-sync.js ../vibe-coding-docs /path/to/project',
    ].join('\n'));
    process.exit(0);
  }

  const sourceDir = path.resolve(args[0]);
  const targetDir = path.resolve(args[1]);
  const dryRun = args.includes('--dry-run');
  const startTime = Date.now();

  console.log(`\n🔄 Синхронизация шаблона${dryRun ? ' (DRY RUN)' : ''}`);
  console.log(`   Источник: ${sourceDir}`);
  console.log(`   Цель:     ${targetDir}\n`);

  const results = sync(sourceDir, targetDir, dryRun);

  // Вывод в консоль
  if (results.copied.length > 0) {
    console.log(`${dryRun ? '📋 Будет скопировано' : '✅ Скопировано'} (${results.copied.length}):`);
    results.copied.forEach(f => console.log(`   + ${f}`));
    console.log('');
  }

  if (results.errors.length > 0) {
    console.log(`❌ Ошибки (${results.errors.length}):`);
    results.errors.forEach(e => console.log(`   ! ${e.file}: ${e.error}`));
    console.log('');
  }

  const elapsed = ((Date.now() - startTime) / 1000).toFixed(2);
  console.log(`📊 Итог: +${results.copied.length} новых, =${results.skipped_exists.length} пропущено, ${results.errors.length} ошибок (${elapsed}s)`);

  // Сохранение отчёта
  const reportPath = path.join(targetDir, 'template-sync-report.md');
  const report = buildReport(results, sourceDir, targetDir, dryRun, startTime);

  if (!dryRun || results.copied.length > 0) {
    if (!dryRun) {
      fs.writeFileSync(reportPath, report, 'utf8');
      console.log(`\n📄 Отчёт сохранён: template-sync-report.md`);
    } else {
      console.log('\n💡 Сухой запуск завершён. Для применения уберите --dry-run');
    }
  }

  if (results.errors.length > 0) process.exit(1);
}

main();
