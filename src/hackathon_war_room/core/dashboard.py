from __future__ import annotations

from html import escape
from pathlib import Path
from typing import Any

from hackathon_war_room.core.launch_bundle import artifact_status

LT = chr(60)
GT = chr(62)

CATEGORY_LABELS = {
    "rules_compliance": "Rules Compliance",
    "demo_clarity": "Demo Clarity",
    "technical_completeness": "Technical Completeness",
    "judge_appeal": "Judge Appeal",
    "safety_readiness": "Safety Readiness",
    "asset_polish": "Asset Polish",
}


def _tag(name: str, body: str = "", attrs: str = "") -> str:
    attr = " " + attrs if attrs else ""
    return f"{LT}{name}{attr}{GT}{body}{LT}/{name}{GT}"


def _void(name: str, attrs: str = "") -> str:
    attr = " " + attrs if attrs else ""
    return f"{LT}{name}{attr}{GT}"


def _li(items: list[Any]) -> str:
    values = items or ["None listed"]
    return "".join(_tag("li", escape(str(item))) for item in values)


def _score_rows(scores: dict[str, Any]) -> str:
    rows = []
    for key, value in scores.items():
        label = CATEGORY_LABELS.get(key, key.replace("_", " ").title())
        row_body = _tag("span", escape(label)) + _tag("strong", escape(str(value)))
        rows.append(_tag("div", row_body, "class=\"score-row\""))
    return "".join(rows)


def _artifact_cards(profile: dict[str, Any]) -> str:
    cards = []
    for item in artifact_status(profile):
        state = "ready" if item["ready"] else "missing"
        body = (
            _tag("strong", escape(item["name"]))
            + _tag("span", escape(state.upper()))
            + _tag("small", escape(item["path"]))
        )
        cards.append(_tag("div", body, "class=\"artifact {}\"".format(state)))
    return "".join(cards)


def _intel_panel(title: str, body: str, proof: str) -> str:
    content = (
        _tag("div", title, "class=\"label\"")
        + _tag("h2", escape(body))
        + _tag("p", escape(proof), "class=\"tagline\"")
    )
    return _tag("div", content, "class=\"card ok\"")


def render_dashboard(profile: dict[str, Any], rules: dict[str, Any], report: dict[str, Any]) -> str:
    verdict = escape(str(report.get("verdict", "UNKNOWN")))
    score = escape(str(report.get("readiness_score", 0)))
    project = escape(str(report.get("project_name", "Hackathon War Room")))
    tagline = escape(str(profile.get("tagline", "Turn hackathon chaos into a judge ready launch packet.")))
    next_action = escape(str(report.get("next_safest_action", "Unknown")))
    iq = escape(str(profile.get("primary_iq_fit", "Foundry IQ")))
    battle = escape(str(rules.get("battle", "Creative Apps with GitHub Copilot")))
    css = ":root{--bg:#07070c;--panel:#10111c;--panel2:#161827;--text:#f4f7fb;--muted:#9aa4bf;--violet:#8b5cf6;--cyan:#38bdf8;--red:#f43f5e;--gold:#f8c14a;--green:#22c55e}*{box-sizing:border-box}body{margin:0;font-family:Inter,Segoe UI,Arial,sans-serif;background:radial-gradient(circle at top left,#1d1536 0,#07070c 34%,#030306 100%);color:var(--text)}.wrap{max-width:1180px;margin:0 auto;padding:36px 22px 54px}.hero{border:1px solid rgba(139,92,246,.35);background:linear-gradient(135deg,rgba(139,92,246,.18),rgba(56,189,248,.08));box-shadow:0 0 60px rgba(139,92,246,.18);border-radius:28px;padding:30px}.kicker{color:var(--cyan);letter-spacing:.22em;text-transform:uppercase;font-size:12px;font-weight:800}.title{font-size:48px;line-height:1;margin:12px 0}.tagline{color:var(--muted);font-size:18px;max-width:820px}.grid{display:grid;grid-template-columns:1.2fr .8fr;gap:18px;margin-top:18px}.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:18px}.card{background:linear-gradient(180deg,var(--panel),var(--panel2));border:1px solid rgba(255,255,255,.09);border-radius:22px;padding:20px;box-shadow:0 18px 40px rgba(0,0,0,.28)}.label{color:var(--muted);font-size:12px;text-transform:uppercase;letter-spacing:.16em}.big{font-size:42px;font-weight:900;margin-top:8px}.verdict{color:var(--gold)}.score-ring{height:190px;border-radius:22px;display:grid;place-items:center;background:radial-gradient(circle,rgba(56,189,248,.18),rgba(139,92,246,.08) 50%,rgba(255,255,255,.03));border:1px solid rgba(56,189,248,.25)}.score-ring strong{font-size:58px}.score-row{display:flex;justify-content:space-between;border-bottom:1px solid rgba(255,255,255,.08);padding:12px 0;color:var(--muted)}.score-row strong{color:var(--text)}h2{margin:0 0 14px;font-size:20px}.list{margin:0;padding-left:20px;color:var(--muted);line-height:1.7}.launch{border-color:rgba(248,193,74,.35);box-shadow:0 0 44px rgba(248,193,74,.08)}.risk{border-color:rgba(244,63,94,.28)}.ok{border-color:rgba(34,197,94,.25)}.footer{margin-top:18px;color:var(--muted);font-size:13px;text-align:center}.pill{display:inline-block;padding:8px 12px;border-radius:999px;background:rgba(139,92,246,.16);border:1px solid rgba(139,92,246,.32);color:#ddd6fe;margin-top:12px}.artifact-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}.artifact{border:1px solid rgba(255,255,255,.1);border-radius:16px;padding:14px;background:rgba(255,255,255,.035)}.artifact strong{display:block;color:var(--text);font-size:14px}.artifact span{display:inline-block;margin-top:8px;font-size:11px;letter-spacing:.14em}.artifact small{display:block;margin-top:8px;color:var(--muted);font-size:11px}.artifact.ready{border-color:rgba(34,197,94,.28)}.artifact.ready span{color:var(--green)}.artifact.missing{border-color:rgba(244,63,94,.38)}.artifact.missing span{color:var(--red)}@media(max-width:840px){.grid,.cards,.artifact-grid{grid-template-columns:1fr}.title{font-size:36px}}"
    head = _void("meta", "charset=\"utf-8\"") + _void("meta", "name=\"viewport\" content=\"width=device-width, initial-scale=1\"") + _tag("title", "Hackathon War Room Dashboard") + _tag("style", css)
    hero = _tag("section", _tag("div", "Mission Board // Creative Apps", "class=\"kicker\"") + _tag("h1", project, "class=\"title\"") + _tag("p", tagline, "class=\"tagline\"") + _tag("span", battle, "class=\"pill\""), "class=\"hero\"")
    cards = _tag("section", _tag("div", _tag("div", "Launch Gate", "class=\"label\"") + _tag("div", verdict, "class=\"big verdict\""), "class=\"card launch\"") + _tag("div", _tag("div", "Readiness", "class=\"label\"") + _tag("div", score + "/100", "class=\"big\""), "class=\"card\"") + _tag("div", _tag("div", "Microsoft IQ", "class=\"label\"") + _tag("div", iq, "class=\"big\""), "class=\"card ok\""), "class=\"cards\"")
    scorecard = _tag("section", _tag("div", _tag("h2", "Scorecard") + _score_rows(report.get("category_scores", {})), "class=\"card\"") + _tag("div", _tag("h2", "Readiness Gauge") + _tag("div", _tag("strong", score), "class=\"score-ring\""), "class=\"card\""), "class=\"grid\"")
    lens = _tag("section", _tag("div", _tag("h2", "Judge Lens") + _tag("ul", _li(report.get("strengths", [])), "class=\"list\""), "class=\"card\"") + _tag("div", _tag("h2", "Risk Console") + _tag("ul", _li(report.get("risks", [])), "class=\"list\""), "class=\"card risk\""), "class=\"grid\"")
    intelligence = _tag(
        "section",
        _intel_panel(
            "Microsoft IQ",
            "Foundry IQ Alignment",
            "Grounds recommendations in project profile, rules, judging criteria, artifact status, and safety signals without claiming live Foundry deployment.",
        )
        + _intel_panel(
            "AI Assisted Development",
            "Copilot Battle Log",
            "Documents the AI assisted build process behind the CLI, scoring engine, smoke tests, dashboard, README, and launch bundle.",
        ),
        "class=\"grid\"",
    )
    asset_bay = _tag("section", _tag("h2", "Asset Bay") + _tag("div", _artifact_cards(profile), "class=\"artifact-grid\""), "class=\"card\"")
    action = _tag("section", _tag("h2", "Next Safest Action") + _tag("p", next_action, "class=\"tagline\""), "class=\"card\"")
    footer = _tag("div", "Hackathon War Room // synthetic demo data only // generated locally", "class=\"footer\"")
    main = _tag("main", hero + cards + scorecard + lens + intelligence + asset_bay + action + footer, "class=\"wrap\"")
    return "<!doctype html>\n" + _tag("html", _tag("head", head) + _tag("body", main), "lang=\"en\"") + "\n"


def write_dashboard(root: Path, profile: dict[str, Any], rules: dict[str, Any], report: dict[str, Any]) -> Path:
    output_dir = root / "demo" / "output"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "project_readiness_dashboard.html"
    output_path.write_text(render_dashboard(profile, rules, report), encoding="utf-8")
    return output_path
