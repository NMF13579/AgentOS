#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

READY='M30_CONTEXT_PIPELINE_AUDIT_READY'
READY_WARN='M30_CONTEXT_PIPELINE_AUDIT_READY_WITH_WARNINGS'
NOT_READY='M30_CONTEXT_PIPELINE_AUDIT_NOT_READY'
INCOMPLETE='M30_CONTEXT_PIPELINE_AUDIT_INCOMPLETE'
NEEDS_REVIEW='M30_CONTEXT_PIPELINE_AUDIT_NEEDS_REVIEW'
BLOCKED='M30_CONTEXT_PIPELINE_AUDIT_BLOCKED'

ORDER={BLOCKED:0,NOT_READY:1,INCOMPLETE:2,NEEDS_REVIEW:3,READY_WARN:4,READY:5}

REQ_DOCS=[
'docs/M30-ENFORCED-RAG-LIGHT-PIPELINE.md',
'docs/M30-CONTEXT-INDEX-FRESHNESS-GATE.md',
'docs/M30-REQUIRED-CONTEXT-PACK-GATE.md',
'docs/M30-CONTEXT-COMPLIANCE-REQUIRED-GATE.md',
'docs/M30-UNIFIED-CONTEXT-PIPELINE-CHECK.md',
'docs/M30-CONTEXT-PIPELINE-CI.md',
'docs/M30-REQUIRED-CHECK-POLICY.md',
'docs/M30-BRANCH-PROTECTION-SETUP-GUIDE.md',
]
REQ_SCRIPTS=[
'scripts/check-context-index-freshness.py',
'scripts/check-required-context-pack.py',
'scripts/check-required-context-compliance.py',
'scripts/check-context-pipeline.py',
]
REQ_WORK=['.github/workflows/context-pipeline.yml']
REQ_FIX=[
'tests/fixtures/context-index-freshness',
'tests/fixtures/required-context-pack-gate',
'tests/fixtures/context-compliance-required-gate',
'tests/fixtures/context-pipeline-check',
'tests/fixtures/context-pipeline-ci',
'tests/fixtures/context-pipeline-required-check-policy',
]


def pick(a,b):
    return b if ORDER[b] < ORDER[a] else a


def add(findings,sev,cat,artifact,msg):
    findings.append({'severity':sev,'category':cat,'artifact':artifact,'message':msg})


def main()->int:
    ap=argparse.ArgumentParser(description='M30.8 audit')
    ap.add_argument('--json',action='store_true')
    ap.add_argument('--root',default='.')
    ap.add_argument('--strict',action='store_true',default=True)
    a=ap.parse_args()

    root=Path(a.root).resolve()
    result=READY
    findings=[]

    checked_docs=[]; checked_scripts=[]; checked_workflows=[]; checked_fixture_roots=[]
    missing=0; unread=0; empty=0

    for rel in REQ_DOCS:
        p=root/rel
        st='exists'
        if not p.exists(): st='missing'; missing+=1; result=pick(result,INCOMPLETE); add(findings,'error','artifact_missing',rel,'required doc missing')
        else:
            try:t=p.read_text(encoding='utf-8')
            except Exception: st='exists_not_readable'; unread+=1; result=pick(result,NEEDS_REVIEW); add(findings,'needs_review','artifact_unreadable',rel,'doc unreadable'); t=''
            if st=='exists' and not t.strip(): empty+=1; result=pick(result,NOT_READY); add(findings,'error','artifact_empty',rel,'doc empty')
            if 'is not approval' not in t:
                result=pick(result,NOT_READY); add(findings,'error','non_authorization_missing',rel,'missing non-authorization phrase')
            if 'branch protection is enabled' in t or 'M31 can start' in t:
                result=pick(result,BLOCKED); add(findings,'blocking','forbidden_authorization_claim',rel,'forbidden claim found')
        checked_docs.append({'path':rel,'status':st})

    for rel in REQ_SCRIPTS:
        p=root/rel; st='exists'
        if not p.exists(): st='missing'; missing+=1; result=pick(result,INCOMPLETE); add(findings,'error','artifact_missing',rel,'required script missing')
        checked_scripts.append({'path':rel,'status':st})

    for rel in REQ_WORK:
        p=root/rel; st='exists'
        if not p.exists(): st='missing'; missing+=1; result=pick(result,INCOMPLETE); add(findings,'error','ci_workflow_missing',rel,'workflow missing')
        else:
            t=p.read_text(encoding='utf-8')
            if 'contents: read' not in t:
                result=pick(result,BLOCKED); add(findings,'blocking','ci_permissions_write',rel,'workflow not read-only')
            if 'scripts/check-context-pipeline.py --json --strict' not in t:
                result=pick(result,NOT_READY); add(findings,'error','ci_result_validation_missing',rel,'required checker command missing')
            if 'continue-on-error: true' in t or ('scripts/check-context-pipeline.py' in t and '|| true' in t):
                result=pick(result,BLOCKED); add(findings,'blocking','ci_masks_failure',rel,'failure masking found')
        checked_workflows.append({'path':rel,'status':st})

    for rel in REQ_FIX:
        p=root/rel; st='exists'
        if not p.exists(): st='missing'; missing+=1; result=pick(result,INCOMPLETE); add(findings,'error','fixture_root_missing',rel,'fixture root missing')
        else:
            dirs=[d for d in p.iterdir() if d.is_dir()]
            if not dirs:
                result=pick(result,NOT_READY); add(findings,'error','fixture_root_empty',rel,'fixture root empty')
            for d in dirs:
                er=d/'expected-result.txt'
                fn=d/'fixture-notes.md'
                if not er.exists(): result=pick(result,INCOMPLETE); add(findings,'error','fixture_expected_result_missing',d.as_posix(),'expected-result missing')
                if not fn.exists(): result=pick(result,INCOMPLETE); add(findings,'error','fixture_notes_missing',d.as_posix(),'fixture-notes missing')
                if er.exists():
                    v=er.read_text().strip()
                    allowed=True
                    if 'context-pipeline-ci' in rel:
                        allowed=v in {'CONTEXT_PIPELINE_CI_PASS','CONTEXT_PIPELINE_CI_FAIL','CONTEXT_PIPELINE_CI_INVALID','CONTEXT_PIPELINE_CI_BLOCKED','CONTEXT_PIPELINE_CI_NEEDS_REVIEW'}
                    elif 'required-check-policy' in rel:
                        allowed=v.startswith('M30_REQUIRED_CHECK_')
                    elif 'context-index-freshness' in rel:
                        allowed=v.startswith('CONTEXT_INDEX_')
                    elif 'required-context-pack-gate' in rel:
                        allowed=v.startswith('CONTEXT_PACK_')
                    elif 'context-compliance-required-gate' in rel:
                        allowed=v.startswith('CONTEXT_COMPLIANCE_')
                    elif 'context-pipeline-check' in rel:
                        allowed=v.startswith('CONTEXT_PIPELINE_')
                    if not allowed:
                        result=pick(result,NOT_READY); add(findings,'error','fixture_expected_result_invalid',er.as_posix(),'invalid expected-result namespace')
        checked_fixture_roots.append({'path':rel,'status':st})

    if any(f['severity']=='blocking' for f in findings) and result in (READY,READY_WARN): result=BLOCKED
    if any(f['severity']=='needs_review' for f in findings) and result==READY: result=NEEDS_REVIEW
    if any(f['severity']=='error' for f in findings) and result==READY: result=NOT_READY

    warnings=[f"{f['category']}: {f['message']}" for f in findings if f['severity'] in ('warning','needs_review')]
    errors=[f"{f['category']}: {f['message']}" for f in findings if f['severity'] in ('error','blocking')]

    out={
        'result':result,
        'checked_artifacts':{
            'docs_total':len(REQ_DOCS),'scripts_total':len(REQ_SCRIPTS),'workflows_total':len(REQ_WORK),'fixture_roots_total':len(REQ_FIX),
            'missing_total':missing,'unreadable_total':unread,'empty_total':empty,
        },
        'checked_docs':checked_docs,
        'checked_scripts':checked_scripts,
        'checked_workflows':checked_workflows,
        'checked_fixture_roots':checked_fixture_roots,
        'warnings':warnings,
        'errors':errors,
        'findings':findings,
    }

    if a.json:
        print(json.dumps(out,ensure_ascii=False,indent=2))
    else:
        print(f"RESULT: {result}")
        print(f"checked docs: {len(checked_docs)}")
        print(f"checked scripts: {len(checked_scripts)}")
        print(f"checked workflows: {len(checked_workflows)}")
        print(f"checked fixture roots: {len(checked_fixture_roots)}")
        print(f"warnings: {len(warnings)}")
        print(f"errors: {len(errors)}")
        print(result)

    return 0 if result==READY else 1


if __name__=='__main__':
    raise SystemExit(main())
