#!/usr/bin/env python3
import argparse, json
from pathlib import Path
import sys

OK='EVIDENCE_IMMUTABILITY_OK'
VIOL='EVIDENCE_IMMUTABILITY_VIOLATION'
REVIEW='EVIDENCE_IMMUTABILITY_NEEDS_REVIEW'


def emit(r,f,m,p,d,j):
    out={"result":r,"failure_class":f,"message":m,"checked_path":str(p),"details":d}
    print(json.dumps(out) if j else f"{r}: {m}")
    return 0 if r==OK else 1

def load(p):
    if p.is_dir(): p=p/'evidence-immutability.json'
    return p, json.loads(p.read_text(encoding='utf-8'))

def main():
    ap=argparse.ArgumentParser(description='Check evidence immutability.')
    ap.add_argument('path', nargs='?')
    ap.add_argument('--json', action='store_true', dest='as_json')
    a=ap.parse_args()
    if not a.path: ap.print_help(); return 0
    p=Path(a.path)
    try: f,d=load(p)
    except Exception as e: return emit(REVIEW,'IMMUTABILITY_STATE_AMBIGUOUS',f'Invalid input: {e}',p,[],a.as_json)
    if d.get('status')=='LEGACY': return emit(REVIEW,'LEGACY_IMMUTABILITY_METADATA_MISSING','Legacy status needs review.',p,[],a.as_json)
    arts=d.get('artifacts')
    if not isinstance(arts,list): return emit(REVIEW,'IMMUTABILITY_STATE_AMBIGUOUS','Artifacts missing.',p,[],a.as_json)
    rerun=d.get('rerun',{})
    if rerun.get('rerun_performed') and not rerun.get('rerun_cause_recorded'):
        return emit(VIOL,'RERUN_CAUSE_MISSING','Rerun performed without cause record.',p,[],a.as_json)
    for art in arts:
        t=art.get('artifact_type')
        if not art.get('sha256_before') or not art.get('sha256_after'):
            return emit(REVIEW,'IMMUTABILITY_STATE_AMBIGUOUS','Hashes missing.',p,[],a.as_json)
        changed=art.get('changed_after_finalization')
        amend_req=art.get('amendment_required')
        amend=art.get('amendment_record')
        if amend_req and not amend:
            return emit(VIOL,'AMENDMENT_REQUIRED_MISSING','Amendment required but missing.',p,[],a.as_json)
        if amend:
            apath=(f.parent / amend) if isinstance(amend,str) else None
            if isinstance(amend,str) and (not apath.exists() or apath.read_text(encoding='utf-8').strip()==''):
                return emit(REVIEW,'AMENDMENT_REQUIRED_MISSING','Amendment reference exists but not inspectable.',p,[],a.as_json)
        if changed and not amend:
            if t=='process_trace': return emit(VIOL,'TRACE_CHANGED_AFTER_COMPLETION','Trace changed without amendment.',p,[],a.as_json)
            if t=='evidence_binding': return emit(VIOL,'BINDING_CHANGED_AFTER_PASS','Binding changed without amendment.',p,[],a.as_json)
            if t=='completion_review': return emit(VIOL,'COMPLETION_REVIEW_REWRITTEN','Completion review changed without amendment.',p,[],a.as_json)
            if art.get('result_status')=='FAIL': return emit(VIOL,'FAILED_EVIDENCE_OVERWRITTEN','Failed evidence overwritten.',p,[],a.as_json)
            return emit(VIOL,'COMPLETED_EVIDENCE_REWRITTEN','Completed evidence rewritten.',p,[],a.as_json)
    return emit(OK,None,'Immutability rules satisfied.',p,[],a.as_json)

if __name__=='__main__': sys.exit(main())
