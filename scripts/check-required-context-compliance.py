#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

PASS = "CONTEXT_COMPLIANCE_PASS"
PASS_WARN = "CONTEXT_COMPLIANCE_PASS_WITH_WARNINGS"
MISSING = "CONTEXT_COMPLIANCE_MISSING"
INVALID = "CONTEXT_COMPLIANCE_INVALID"
VIOLATION = "CONTEXT_COMPLIANCE_VIOLATION"
INCOMPLETE = "CONTEXT_COMPLIANCE_INCOMPLETE"
NEEDS_REVIEW = "CONTEXT_COMPLIANCE_NEEDS_REVIEW"
BLOCKED = "CONTEXT_COMPLIANCE_BLOCKED"

ORDER = {BLOCKED:0, VIOLATION:1, INVALID:2, INCOMPLETE:3, MISSING:4, NEEDS_REVIEW:5, PASS_WARN:6, PASS:7}


def pick(a:str,b:str)->str:
    return b if ORDER[b] < ORDER[a] else a


def add(fs:list[dict[str,Any]], sev:str, cat:str, msg:str, path:str|None=None):
    f={"severity":sev,"category":cat,"message":msg}
    if path: f["path"]=path
    fs.append(f)


def read(p:Path)->str|None:
    try: return p.read_text(encoding='utf-8')
    except Exception: return None


def section(text:str, name:str)->str|None:
    m=re.search(rf"^##\s+{re.escape(name)}\s*$", text, re.M)
    if not m: return None
    s=m.end()
    n=re.search(r"^##\s+", text[s:], re.M)
    e=s+n.start() if n else len(text)
    return text[s:e]


def extract_required_items(ctx:str)->list[str]:
    sec=section(ctx,"Required Context")
    if sec is None: return []
    out=[]
    for ln in sec.splitlines():
        ln=ln.strip()
        if ln.startswith('- '):
            v=ln[2:].strip()
            if v and v.lower() not in {'none','-'}:
                out.append(v)
    return out


def check_artifact_coverage(text:str, required:list[str], findings:list[dict[str,Any]], label:str)->str:
    res=PASS
    low=text.lower()
    if "context reviewed" in low or "context pack applied" in low:
        add(findings,"needs_review","generic_context_claim","Generic claim patterns are insufficient",label)
        res=pick(res,NEEDS_REVIEW)
    if "command success" in low and "override" in low:
        add(findings,"blocking","command_success_as_compliance","Command success does not override context violation",label)
        res=pick(res,BLOCKED)
    if "tests passed" in low and "compliance" in low:
        add(findings,"blocking","source_of_truth_violation","Tests passing is not context compliance",label)
        res=pick(res,BLOCKED)
    for item in required:
        if item not in text:
            add(findings,"error","required_context_unacknowledged",f"required context not acknowledged: {item}",label)
            res=pick(res,VIOLATION)
    return res


def call_context_pack_checker(root:Path, task:Path, context:Path, index:Path)->tuple[str|None,str|None]:
    checker=root/"scripts/check-required-context-pack.py"
    if not checker.exists(): return None,"missing"
    proc=subprocess.run([sys.executable,str(checker),"--json","--root",str(root),"--task",str(task),"--context",str(context),"--index",str(index)],capture_output=True,text=True,shell=False)
    if proc.returncode not in (0,1): return None,"exec_failed"
    try:data=json.loads(proc.stdout or '{}')
    except Exception:return None,'malformed_json'
    return data.get('result'),None


def map_pack_result(r:str)->str:
    return {
        "CONTEXT_PACK_VALID":PASS,
        "CONTEXT_PACK_VALID_WITH_WARNINGS":NEEDS_REVIEW,
        "CONTEXT_PACK_MISSING":MISSING,
        "CONTEXT_PACK_INVALID":INCOMPLETE,
        "CONTEXT_PACK_STALE":INCOMPLETE,
        "CONTEXT_PACK_INCOMPLETE":INCOMPLETE,
        "CONTEXT_PACK_NEEDS_REVIEW":NEEDS_REVIEW,
        "CONTEXT_PACK_BLOCKED":BLOCKED,
    }.get(r,INCOMPLETE)


def main()->int:
    ap=argparse.ArgumentParser(description='M30.4 Context Compliance Required Gate')
    ap.add_argument('--json',action='store_true')
    ap.add_argument('--root',default='.')
    ap.add_argument('--task',default='tasks/active-task.md')
    ap.add_argument('--context',default='reports/context-pack.md')
    ap.add_argument('--plan',default='reports/plan.md')
    ap.add_argument('--verification',default='reports/context-verification.md')
    ap.add_argument('--changed-files',default='reports/changed-files.txt')
    ap.add_argument('--require-valid-context-pack',action='store_true')
    ap.add_argument('--mode',choices=['plan','verification','both'],default='both')
    a=ap.parse_args()

    root=Path(a.root).resolve()
    task=(root/a.task).resolve(); context=(root/a.context).resolve(); plan=(root/a.plan).resolve(); ver=(root/a.verification).resolve(); ch=(root/a.changed_files).resolve()
    res=PASS
    findings=[]
    checked=0
    changed_src='not_provided'
    pack_result=None

    ctext=read(context)
    if ctext is None:
        add(findings,'error','context_pack_missing','Context Pack missing',a.context)
        res=pick(res,MISSING)
        required=[]
    else:
        required=extract_required_items(ctext)
        if not required:
            add(findings,'error','required_context_missing','required context missing/unextractable',a.context)
            res=pick(res,INVALID)
        if 'Context Pack is not approval' not in ctext:
            add(findings,'blocking','approval_claim','Context Pack is treated as approval',a.context)
            res=pick(res,BLOCKED)

    if a.require_valid_context_pack:
        pack_result, perr = call_context_pack_checker(root,task,context,root/"data/context-index.json")
        if perr=='missing':
            add(findings,'error','context_pack_invalid','Context Pack checker missing')
            res=pick(res,INCOMPLETE)
        elif perr:
            add(findings,'needs_review','context_pack_invalid','Context Pack checker execution failure')
            res=pick(res,NEEDS_REVIEW)
        else:
            res=pick(res,map_pack_result(pack_result or ''))

    def run_plan()->str:
        if not plan.exists():
            add(findings,'error','plan_missing','plan missing',a.plan); return MISSING
        t=read(plan)
        if not t or not t.strip():
            add(findings,'error','plan_invalid','plan invalid/empty',a.plan); return INVALID
        return check_artifact_coverage(t,required,findings,a.plan)

    def run_ver()->str:
        if not ver.exists():
            add(findings,'error','verification_missing','verification missing',a.verification); return MISSING
        t=read(ver)
        if not t or not t.strip():
            add(findings,'error','verification_invalid','verification invalid/empty',a.verification); return INVALID
        if 'evidence' not in t.lower():
            add(findings,'error','verification_evidence_missing','Verification evidence is required for context compliance.',a.verification)
            r=VIOLATION
        else:
            r=PASS
        r=pick(r,check_artifact_coverage(t,required,findings,a.verification))
        return r

    if a.mode in ('plan','both'):
        checked += 1
        res = pick(res, run_plan())
    if a.mode in ('verification','both'):
        checked += 1
        res = pick(res, run_ver())

    # changed files
    if ch.exists():
        changed_src=a.changed_files
        t=read(ch) or ''
        for ln in [x.strip() for x in t.splitlines() if x.strip()]:
            if ln.startswith('/') or '..' in Path(ln).parts:
                add(findings,'error','changed_files_out_of_scope','unsafe changed file path',ln)
                res=pick(res,INVALID)
            elif required and ln not in required and ln not in (read(task) or '') and ln not in (read(context) or '') and ln not in (read(plan) or '') and ln not in (read(ver) or ''):
                add(findings,'error','changed_files_unjustified','Undeclared changed files must be treated as scope/context violation, not as neutral.',ln)
                res=pick(res,VIOLATION)
    else:
        changed_src='not_provided'
        add(findings,'needs_review','changed_files_missing','changed files evidence missing')
        res=pick(res,NEEDS_REVIEW)

    if any(f['severity']=='blocking' for f in findings) and res in (PASS,PASS_WARN): res=BLOCKED
    if any(f['severity']=='needs_review' for f in findings) and res==PASS: res=NEEDS_REVIEW
    if any(f['severity']=='error' for f in findings) and res==PASS: res=INVALID

    warns=[]; errs=[]
    for f in findings:
        line=f"{f['category']}: {f['message']}"
        if f.get('path'): line=f"{f['path']}: {line}"
        if f['severity'] in ('warning','needs_review'): warns.append(line)
        if f['severity'] in ('error','blocking'): errs.append(line)

    out={
        'result':res,
        'mode':a.mode,
        'task_path':a.task,
        'context_path':a.context,
        'plan_path':a.plan,
        'verification_path':a.verification,
        'checked_required_items':len(required),
        'changed_files_source':changed_src,
        'warnings':warns,
        'errors':errs,
        'findings':findings,
    }
    if a.require_valid_context_pack:
        out['context_pack_result']=pack_result

    if a.json:
        print(json.dumps(out,ensure_ascii=False,indent=2))
    else:
        print(f"RESULT: {res}")
        print(f"mode: {a.mode}")
        print(f"task_path: {a.task}")
        print(f"context_path: {a.context}")
        print(f"plan_path: {a.plan}")
        print(f"verification_path: {a.verification}")
        print(f"checked_required_items: {len(required)}")
        print(f"warnings: {len(warns)}")
        print(f"errors: {len(errs)}")
        for f in findings:
            p=f" path={f['path']}" if 'path' in f else ''
            print(f"- [{f['severity']}] {f['category']}{p}: {f['message']}")
        print(res)
    return 0 if res==PASS else 1


if __name__=='__main__':
    raise SystemExit(main())
