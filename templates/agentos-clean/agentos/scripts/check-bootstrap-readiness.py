#!/usr/bin/env python3
import os
import sys
from pathlib import Path

def check():
    print('Checking AgentOS bootstrap readiness...')
    repo_root = Path(__file__).resolve().parent.parent.parent
    
    checks = [
        ('README.md', repo_root / 'README.md'),
        ('.agentos/config.yml', repo_root / '.agentos/config.yml'),
        ('Issue template', repo_root / '.github/ISSUE_TEMPLATE/agentos_task.yml'),
        ('Bootstrap workflow', repo_root / '.github/workflows/agentos-bootstrap.yml'),
        ('tasks/ directory', repo_root / 'tasks'),
        ('reports/ directory', repo_root / 'reports'),
    ]

    passed = True
    for label, path in checks:
        if path.exists():
            print(f'[PASS] {label} exists')
        else:
            print(f'[FAIL] {label} missing at {path}')
            passed = False

    if not passed:
        print('BOOTSTRAP_NOT_READY')
        sys.exit(1)

    config_path = repo_root / '.agentos/config.yml'
    config_text = config_path.read_text()
    if 'mode: simple' in config_text:
        print('[PASS] Mode is simple')
    else:
        print('[FAIL] Mode is not simple')
        passed = False

    if 'full_mode_grants_extra_permissions: false' in config_text:
        print('[PASS] Full mode boundary enforced')
    else:
        print('[FAIL] Full mode boundary not enforced')
        passed = False

    workflow_path = repo_root / '.github/workflows/agentos-bootstrap.yml'
    workflow_text = workflow_path.read_text()
    if 'contents: read' in workflow_text:
        print('[PASS] Workflow has read-only permission')
    else:
        print('[FAIL] Workflow missing read-only permission')
        passed = False

    if 'contents: write' in workflow_text:
        print('[FAIL] Workflow has write permission')
        passed = False
    else:
        print('[PASS] Workflow does not have write permission')

    if 'git commit' in workflow_text or 'git push' in workflow_text:
        print('[FAIL] Workflow contains mutating commands')
        passed = False
    else:
        print('[PASS] Workflow does not commit or push')

    for d in ['reports', 'tasks/done', 'tasks/failed']:
        dir_path = repo_root / d
        if dir_path.exists():
            files = [f for f in os.listdir(dir_path) if f != '.gitkeep']
            if files:
                print(f'[FAIL] Dir {d} is not empty: {files}')
                passed = False
            else:
                print(f'[PASS] Dir {d} is empty except .gitkeep')

    if passed:
        print('BOOTSTRAP_READY')
        sys.exit(0)
    else:
        print('BOOTSTRAP_NOT_READY')
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] in ["--help", "-h"]:
        print("Usage: python3 check-bootstrap-readiness.py")
        print("Checks if the AgentOS workspace is ready for bootstrapping.")
        sys.exit(0)
    check()
