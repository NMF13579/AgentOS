#!/usr/bin/env python3

try:
    from .plain_status_renderer import (
        render_status_view_model as plain_status,
        render_tutor_explanation as plain_explain,
        render_next_safe_step as plain_next,
    )
except Exception:
    from plain_status_renderer import (  # type: ignore
        render_status_view_model as plain_status,
        render_tutor_explanation as plain_explain,
        render_next_safe_step as plain_next,
    )


def _rich_available():
    try:
        import rich  # noqa: F401
        return True
    except Exception:
        return False


def render_status_view_model(view_model: dict, ascii: bool = False, no_color: bool = False) -> str:
    if ascii or no_color or not _rich_available():
        return plain_status(view_model, ascii=ascii, no_color=no_color)
    try:
        from rich.console import Console
        from rich.panel import Panel
        from rich.text import Text
        from io import StringIO

        buf = StringIO()
        c = Console(file=buf, force_terminal=False, color_system=None if no_color else "auto")
        title = view_model.get("title", "Статус неизвестен")
        summary = view_model.get("summary", "Нет данных")
        body = Text(f"{summary}\n\nStatus: {view_model.get('overall_status')}\nReason: {view_model.get('top_status_code')}")
        c.print(Panel(body, title=title))
        return buf.getvalue().rstrip("\n")
    except Exception:
        return plain_status(view_model, ascii=True, no_color=True)


def render_tutor_explanation(explanation: dict, ascii: bool = False, no_color: bool = False) -> str:
    if ascii or no_color or not _rich_available():
        return plain_explain(explanation, ascii=ascii, no_color=no_color)
    return plain_explain(explanation, ascii=False, no_color=no_color)


def render_next_safe_step(next_step: dict, ascii: bool = False, no_color: bool = False) -> str:
    if ascii or no_color or not _rich_available():
        return plain_next(next_step, ascii=ascii, no_color=no_color)
    return plain_next(next_step, ascii=False, no_color=no_color)


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--demo", action="store_true")
    ap.add_argument("--ascii", action="store_true")
    ap.add_argument("--no-color", action="store_true")
    args = ap.parse_args()
    if args.demo:
        demo = {"title": "Нужно проверить", "summary": "Демо Rich fallback.", "overall_status": "AGENTOS_STATUS_NEEDS_REVIEW", "top_status_code": "CONTEXT_PIPELINE_NEEDS_REVIEW"}
        print(render_status_view_model(demo, ascii=args.ascii, no_color=args.no_color))
