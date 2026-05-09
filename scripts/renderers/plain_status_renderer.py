#!/usr/bin/env python3

def _lead(data, ascii=False):
    if ascii:
        return data.get("ascii_label", "[UNKNOWN]")
    return data.get("icon", "❓")


def render_status_view_model(view_model: dict, ascii: bool = False, no_color: bool = False) -> str:
    if not isinstance(view_model, dict):
        return "[UNKNOWN] Статус неизвестен\nПродолжать нельзя без проверки."
    lead = _lead(view_model, ascii)
    title = view_model.get("title", "Статус неизвестен")
    summary = view_model.get("summary", "Нет данных")
    lines = [f"{lead} {title}", summary, "", f"Status: {view_model.get('overall_status','AGENTOS_STATUS_UNKNOWN')}", f"Reason: {view_model.get('top_status_code','STATUS_SOURCE_DAMAGED')}"]
    src = (view_model.get("source") or {}).get("report")
    if src:
        lines.append(f"Source: {src}")
    return "\n".join(lines)


def render_tutor_explanation(explanation: dict, ascii: bool = False, no_color: bool = False) -> str:
    if not isinstance(explanation, dict):
        return "[UNKNOWN] Объяснение недоступно."
    lead = (explanation.get("display") or {}).get("ascii_label", "[UNKNOWN]") if ascii else (explanation.get("display") or {}).get("icon", "❓")
    lines = [f"{lead} {explanation.get('title','Статус неизвестен')}", "", "Что случилось:", explanation.get("what_happened", ""), "", "Почему это важно:", explanation.get("why_it_matters", "")]
    return "\n".join(lines)


def render_next_safe_step(next_step: dict, ascii: bool = False, no_color: bool = False) -> str:
    if not isinstance(next_step, dict):
        return "[UNKNOWN] Шаг недоступен."
    lead = (next_step.get("display") or {}).get("ascii_label", "[NEXT]") if ascii else (next_step.get("display") or {}).get("icon", "▶️")
    sel = next_step.get("selected_step") or {}
    cmd = sel.get("command", "Следующий безопасный шаг не найден.")
    lines = [f"{lead} Следующий безопасный шаг", "", cmd, "", "Это подсказка, не выполнение."]
    return "\n".join(lines)


if __name__ == "__main__":
    demo = {"ascii_label": "[REVIEW]", "icon": "🔎", "title": "Нужно проверить", "summary": "Короткое демо.", "overall_status": "AGENTOS_STATUS_NEEDS_REVIEW", "top_status_code": "CONTEXT_PIPELINE_NEEDS_REVIEW"}
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--demo", action="store_true")
    ap.add_argument("--ascii", action="store_true")
    ap.add_argument("--no-color", action="store_true")
    args = ap.parse_args()
    if args.demo:
        print(render_status_view_model(demo, ascii=args.ascii, no_color=args.no_color))
