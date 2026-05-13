import os
import sys

def validate():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    
    checks = [
        (os.path.exists(os.path.join(base_dir, "README.md")), "README.md exists"),
        (os.path.exists(os.path.join(base_dir, ".agentos", "config.yml")), ".agentos/config.yml exists"),
        (os.path.exists(os.path.join(base_dir, "tasks")), "tasks/ exists"),
        (os.path.exists(os.path.join(base_dir, "reports")), "reports/ exists"),
        (os.path.exists(os.path.join(base_dir, "agentos", "docs", "user-modes.md")), "agentos/docs/user-modes.md exists"),
        (os.path.exists(os.path.join(base_dir, ".github", "ISSUE_TEMPLATE", "agentos_task.yml")), ".github/ISSUE_TEMPLATE/agentos_task.yml exists"),
    ]
    
    config_path = os.path.join(base_dir, ".agentos", "config.yml")
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            content = f.read()
            checks.append(("mode: simple" in content, ".agentos/config.yml contains mode: simple"))
    
    # Check for forbidden artifacts (milestone reports)
    forbidden_found = False
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if any(m in file for m in ["m37", "m38", "m39", "m40"]):
                checks.append((False, f"Forbidden milestone report found: {os.path.join(root, file)}"))
                forbidden_found = True
    
    if not forbidden_found:
        checks.append((True, "No forbidden milestone reports found"))

    all_pass = True
    for passed, msg in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {msg}")
        if not passed:
            all_pass = False
            
    if all_pass:
        print("OVERALL: PASS")
        sys.exit(0)
    else:
        print("OVERALL: FAIL")
        sys.exit(1)

if __name__ == "__main__":
    # Support 'all' subcommand as an alias for full validation
    if len(sys.argv) > 1 and sys.argv[1] == "all":
        validate()
    else:
        validate()
