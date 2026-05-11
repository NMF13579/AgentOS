import os
import sys
import argparse
import yaml
import glob

def main():
    parser = argparse.ArgumentParser(description="Check AgentOS clean template cleanliness")
    parser.add_argument("--template", default="templates/agentos-clean", help="Template directory")
    parser.add_argument("--json", action="store_true", help="Output in JSON (not implemented)")
    args = parser.parse_args()

    template_dir = args.template
    manifest_path = os.path.join(template_dir, "template-manifest.yml")

    if not os.path.exists(manifest_path):
        print("TEMPLATE_CHECK_BLOCKED: Manifest missing")
        sys.exit(1)

    with open(manifest_path, 'r') as f:
        manifest = yaml.safe_load(f)

    errors = []
    warnings = []

    # Verify must_include
    for path in manifest.get('must_include', []):
        if not os.path.exists(os.path.join(template_dir, path)):
            errors.append(f"Missing must_include: {path}")

    # Verify must_not_include
    for pattern in manifest.get('must_not_include', []):
        matches = glob.glob(os.path.join(template_dir, pattern), recursive=True)
        if matches:
            errors.append(f"Found forbidden artifact: {matches}")

    # Verify empty_dirs_except_gitkeep
    for d in manifest.get('empty_dirs_except_gitkeep', []):
        full_path = os.path.join(template_dir, d)
        if os.path.exists(full_path):
            files = os.listdir(full_path)
            if any(f != ".gitkeep" for f in files):
                errors.append(f"Directory not empty (except .gitkeep): {d}")

    # Verify .agentos/config.yml mode: simple
    config_path = os.path.join(template_dir, ".agentos", "config.yml")
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
            if config.get('agentos', {}).get('mode') != 'simple':
                errors.append("Default mode is not simple")
            if config.get('agentos', {}).get('mode_policy', {}).get('full_mode_grants_extra_permissions'):
                errors.append("Full mode grants extra permissions")

    # Verify .gitignore
    gitignore_path = os.path.join(template_dir, ".gitignore")
    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r') as f:
            content = f.read()
            for entry in manifest.get('runtime_gitignored', []):
                if entry not in content:
                    errors.append(f"Missing gitignore entry: {entry}")

    if errors:
        print("TEMPLATE_NOT_CLEAN")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    elif warnings:
        print("TEMPLATE_CLEAN_WITH_WARNINGS")
        for w in warnings:
            print(f"  - {w}")
        sys.exit(0)
    else:
        print("TEMPLATE_CLEAN")
        sys.exit(0)

if __name__ == "__main__":
    main()
