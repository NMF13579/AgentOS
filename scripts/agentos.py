#!/usr/bin/env python3
import argparse
import subprocess
import sys
from pathlib import Path

ALLOWED = {"dashboard", "status", "why", "next", "log", "help"}
FORBIDDEN_COMMANDS = {"fix", "go", "approve", "ready", "commit", "push", "merge", "promote", "run", "execute"}
FORBIDDEN_FLAGS = {"--approve", "--ready", "--fix", "--go", "--execute", "--commit", "--push", "--merge", "--promote", "--force", "--write-protected"}


def print_help():
    print("AgentOS M31 commands:\n")
    print("agentos            Show dashboard")
    print("agentos dashboard  Show dashboard")
    print("agentos status     Show current status")
    print("agentos why        Explain what happened")
    print("agentos next       Show next safe step")
    print("agentos log        Show read-only event summary")
    print("agentos help       Show help\n")
    print("M31 does not execute actions.")
    print("M31 does not create approval.")
    print("M31 does not mark READY.")


def run_script(script, args):
    p = subprocess.run([sys.executable, script] + args)
    return p.returncode


def command_log(root: Path):
    reports = root / "reports"
    if not reports.exists():
        print("ℹ️ Журнал пока недоступен. Используй agentos status для текущего состояния.")
        return 1
    patterns = ["status-snapshot.md", "m31-dashboard-snapshot.md"]
    files = []
    for pat in patterns:
        f = reports / pat
        if f.exists():
            files.append(str(f.relative_to(root)))
    files += [str(p.relative_to(root)) for p in reports.glob("m31-*.md")]
    files += [str(p.relative_to(root)) for p in reports.glob("*status*.md")]
    files += [str(p.relative_to(root)) for p in reports.glob("*audit*.md")]
    uniq = sorted(set(files))
    if not uniq:
        print("ℹ️ Журнал пока недоступен. Используй agentos status для текущего состояния.")
        return 0
    print("ℹ️ Журнал в M31 ограничен.\n")
    print("Доступные файлы:")
    for x in uniq:
        print(f"- {x}")
    print("\nЭто read-only summary.")
    print("Это не audit proof.")
    return 0


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("command", nargs="?")
    ns, unknown = parser.parse_known_args()

    root = Path(__file__).resolve().parent.parent

    cmd = ns.command or "dashboard"
    rest = list(unknown)
    if cmd and cmd.startswith("--"):
        rest = [cmd] + rest
        cmd = "dashboard"

    if any(f in FORBIDDEN_FLAGS for f in rest):
        print("⛔ Флаг недоступен в M31.")
        print("Используй безопасные команды: agentos why / agentos next")
        return 1

    if cmd in FORBIDDEN_COMMANDS:
        print("⛔ Команда недоступна в M31.\n")
        print("M31 не исправляет и не выполняет действия.")
        print("Используй:")
        print("agentos why")
        print("agentos next")
        return 1

    if cmd not in ALLOWED:
        print("Неизвестная команда. Используй: agentos help")
        return 2

    if cmd == "help":
        print_help()
        return 0

    if cmd == "log":
        return command_log(root)

    mapping = {
        "dashboard": root / "scripts/agentos-tui.py",
        "status": root / "scripts/agentos-status.py",
        "why": root / "scripts/agentos-explain.py",
        "next": root / "scripts/agentos-next-step.py",
    }

    target = mapping[cmd]
    if not target.exists():
        print("❓ Команда недоступна: отсутствует downstream script")
        return 1

    return run_script(str(target), rest)


if __name__ == "__main__":
    sys.exit(main())
