import os
import sys

def check():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    
    checks = [
        (os.path.exists(os.path.join(base_dir, "README.md")), "README.md exists"),
        (os.path.exists(os.path.join(base_dir, ".agentos", "config.yml")), ".agentos/config.yml exists"),
        (os.path.exists(os.path.join(base_dir, ".github", "ISSUE_TEMPLATE", "agentos_task.yml")), "Issue template exists"),
        (os.path.exists(os.path.join(base_dir, ".github", "workflows", "agentos-bootstrap.yml")), "Bootstrap workflow exists"),
        (os.path.exists(os.path.join(base_dir, "tasks")), "tasks/ exists"),
        (os.path.exists(os.path.join(base_dir, "reports")), "reports/ exists"),
    ]
    
    config_path = os.path.join(base_dir, ".agentos", "config.yml")
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            content = f.read()
            checks.append(("mode: simple" in content, "Mode is simple"))
            checks.append(("full_mode_grants_extra_permissions: false" in content, "Full mode boundary enforced"))

    workflow_path = os.path.join(base_dir, ".github", "workflows", "agentos-bootstrap.yml")
    if os.path.exists(workflow_path):
        with open(workflow_path, 'r') as f:
            content = f.read()
            checks.append(("contents: read" in content, "Workflow has read-only permission"))
            checks.append(("contents: write" not in content, "Workflow does not have write permission"))
            checks.append(("git commit" not in content, "Workflow does not commit"))
            checks.append(("git push" not in content, "Workflow does not push"))

    # Empty dirs check
    for d in ["reports", "tasks/done", "tasks/failed"]:
        full_path = os.path.join(base_dir, d)
        if os.path.exists(full_path):
            files = os.listdir(full_path)
            checks.append((all(f == ".gitkeep" for f in files), f"Dir {d} is empty except .gitkeep"))

    all_pass = True
    for passed, msg in checks:
        if not passed:
            print(f"[FAIL] {msg}")
            all_pass = False
        else:
            print(f"[PASS] {msg}")
            
    if all_pass:
        print("BOOTSTRAP_READY")
        sys.exit(0)
    else:
        print("BOOTSTRAP_NOT_READY")
        sys.exit(1)

if __name__ == "__main__":
    check()
