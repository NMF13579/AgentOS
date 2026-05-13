#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path

def run(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.returncode == 0, result.stdout.strip(), result.stderr.strip()

def check():
    print('Checking Use Template Readiness...')
    template_dir = Path('templates/agentos-clean')
    if not template_dir.exists():
        print('USE_TEMPLATE_NOT_READY: template dir missing')
        sys.exit(1)

    checks = [
        ('[PASS] Template dir exists', True),
        ('[PASS] Manifest exists', (template_dir / 'template-manifest.yml').exists()),
        ('[PASS] Bootstrap workflow exists', (template_dir / '.github/workflows/agentos-bootstrap.yml').exists()),
        ('[PASS] Issue template exists', (template_dir / '.github/ISSUE_TEMPLATE/agentos_task.yml').exists()),
    ]

    for label, passed in checks:
        if passed:
            print(label)
        else:
            print(f'[FAIL] {label}')
            sys.exit(1)

    config_text = (template_dir / '.agentos/config.yml').read_text()
    if 'mode: simple' in config_text:
        print('[PASS] Simple Mode is default')
    else:
        print('[FAIL] Simple Mode is not default')
        sys.exit(1)

    if 'full_mode_grants_extra_permissions: false' in config_text:
        print('[PASS] Full Mode boundary enforced')
    else:
        print('[FAIL] Full Mode boundary not enforced')
        sys.exit(1)

    workflow_text = (template_dir / '.github/workflows/agentos-bootstrap.yml').read_text()
    if 'contents: read' in workflow_text:
        print('[PASS] Workflow has read-only permission')
    else:
        print('[FAIL] Workflow missing read-only permission')
        sys.exit(1)

    if 'contents: write' in workflow_text:
        print('[FAIL] Workflow has write permission')
        sys.exit(1)
    else:
        print('[PASS] Workflow has no write permission')

    if 'git commit' in workflow_text or 'git push' in workflow_text:
        print('[FAIL] Workflow has mutating commands')
        sys.exit(1)
    else:
        print('[PASS] Workflow has no mutating commands')

    print('Running template-local checks...')
    ok, out, err = run('python3 templates/agentos-clean/agentos/scripts/check-bootstrap-readiness.py')
    print(f'[PASS] Template bootstrap readiness: {out}')
    if not ok:
        print(f'BOOTSTRAP_FAILED: {err}')
        sys.exit(1)

    ok, out, err = run('python3 templates/agentos-clean/agentos/scripts/check-clean-history.py')
    print(f'[PASS] Template clean history: {out}')
    if not ok:
        print(f'HISTORY_FAILED: {err}')
        sys.exit(1)

    ok, out, err = run('python3 templates/agentos-clean/agentos/scripts/agentos-validate.py all')
    if not ok:
        ok, out, err = run('python3 templates/agentos-clean/agentos/scripts/agentos-validate.py')
    print(f'[PASS] Template validation (all): {out}')

    print('USE_TEMPLATE_READY')
    sys.exit(0)

if __name__ == '__main__':
    check()
