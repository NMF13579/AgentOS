#!/usr/bin/env python3
import argparse
import json
from pathlib import Path
import sys

OK="ROLE_SEPARATION_OK"
VIOL="ROLE_SEPARATION_VIOLATION"
REVIEW="ROLE_SEPARATION_NEEDS_REVIEW"
ALLOWED_ACTOR_TYPES={"agent","human","runner","ci","maintainer"}


def emit(result,failure_class,message,path,details,as_json):
    payload={"result":result,"failure_class":failure_class,"message":message,"checked_path":str(path),"details":details}
    if as_json: print(json.dumps(payload))
    else: print(f"{result}: {message}")
    return 0 if result==OK else 1


def load(path):
    if path.is_dir(): path=path/"role-separation.json"
    return path, json.loads(path.read_text(encoding="utf-8"))


def main():
    ap=argparse.ArgumentParser(description="Check role separation policy.")
    ap.add_argument("path", nargs="?")
    ap.add_argument("--json", action="store_true", dest="as_json")
    args=ap.parse_args()
    if not args.path:
        ap.print_help(); return 0
    p=Path(args.path)
    try:
        _,d=load(p)
    except Exception as e:
        return emit(REVIEW,"VERIFICATION_AUTHORITY_AMBIGUOUS",f"Invalid input: {e}",p,[],args.as_json)
    risk=d.get("risk_level")
    if risk not in {"LOW","MEDIUM","HIGH","CRITICAL"}:
        return emit(REVIEW,"ROLE_SEPARATION_MISSING","Missing/unknown risk level.",p,[],args.as_json)
    prod=d.get("produced_by") or {}
    impl=d.get("implemented_by") or {}
    ver=d.get("verified_by") or {}
    appr=d.get("approved_by")
    final=d.get("final_verifier")
    for actor in [prod,impl,ver]+([appr] if appr else []):
        if actor.get("actor_type") and actor.get("actor_type") not in ALLOWED_ACTOR_TYPES:
            return emit(REVIEW,"VERIFICATION_AUTHORITY_AMBIGUOUS","Unknown actor type.",p,[],args.as_json)
    if not ver or not final:
        return emit(REVIEW,"ROLE_SEPARATION_MISSING","Verifier/final verifier missing.",p,[],args.as_json)
    if appr is None and d.get("approval_claimed") is True:
        return emit(REVIEW,"VERIFICATION_AUTHORITY_AMBIGUOUS","Approval claimed but approver missing.",p,[],args.as_json)

    if risk in {"HIGH","CRITICAL"}:
        if final==prod.get("actor_id"):
            return emit(VIOL,"PRODUCER_FINAL_VERIFIER","Producer is final verifier.",p,[],args.as_json)
        if final==impl.get("actor_id"):
            return emit(VIOL,"IMPLEMENTOR_FINAL_VERIFIER","Implementor is final verifier.",p,[],args.as_json)
        if ver.get("actor_id")==prod.get("actor_id") or ver.get("actor_id")==impl.get("actor_id"):
            return emit(VIOL,"SAME_ACTOR_CREATED_AND_VERIFIED","Same actor produced/implemented and verified.",p,[],args.as_json)
        for a in d.get("verified_artifacts",[]):
            if a.get("patched_by_verifier") is True:
                return emit(VIOL,"VERIFIER_PATCHED_VERIFIED_ARTIFACT","Verifier patched verified artifact.",p,[],args.as_json)
        if appr and appr.get("actor_type")=="agent":
            return emit(VIOL,"AGENT_APPROVER_CONFLICT","Agent approver conflict.",p,[],args.as_json)
    else:
        if ver.get("actor_id") in {prod.get("actor_id"),impl.get("actor_id")} and not d.get("same_actor_validation_allowed_by_policy"):
            return emit(REVIEW,"ROLE_SEPARATION_MISSING","Low/medium same-actor validation not explicitly allowed.",p,[],args.as_json)

    return emit(OK,None,"Role separation rules satisfied.",p,[],args.as_json)

if __name__=="__main__":
    sys.exit(main())
