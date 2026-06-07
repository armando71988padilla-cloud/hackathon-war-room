from __future__ import annotations

import base64
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


def _asset_data_uri(filename: str) -> str:
    path = Path(__file__).resolve().parents[1] / "assets" / filename
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return "data:image/png;base64," + encoded

def _hotspot(label: str, href: str, class_name: str) -> str:
    attrs = "href=\"{}\" class=\"action-hotspot {}\" title=\"{}\" target=\"_blank\" rel=\"noopener\"".format(escape(href, quote=True), escape(class_name, quote=True), escape(label, quote=True))
    return _tag("a", label, attrs)


def _dashboard_hotspots() -> str:
    links = [
        ("Track overview", "../../README.md", "hotspot-track"),
        ("Launch packet", "launch_packet.md", "hotspot-launch-gate"),
        ("Release manifest", "release_manifest.json", "hotspot-readiness"),
        ("Microsoft IQ architecture", "../../docs/architecture.md", "hotspot-iq"),
        ("README", "../../README.md", "hotspot-readme"),
        ("Judge packet", "judge_packet.md", "hotspot-judge-packet"),
        ("Dashboard", "project_readiness_dashboard.html", "hotspot-dashboard"),
        ("Demo script", "../../docs/demo_video_script.md", "hotspot-demo-script"),
        ("Architecture doc", "../../docs/architecture.md", "hotspot-architecture"),
        ("Final checklist", "../../docs/final_submission_checklist.md", "hotspot-final-checklist"),
        ("Copilot build log", "../../docs/copilot_build_log.md", "hotspot-copilot-build-log"),
    ]
    items = "".join(_hotspot(label, href, class_name) for label, href, class_name in links)
    return _tag("nav", items, "class=\"action-hotspots\" aria-label=\"dashboard action links\"")

def _command_link(label: str, href: str) -> str:
    attrs = "href=\"{}\" target=\"_blank\" rel=\"noopener\"".format(escape(href, quote=True))
    return _tag("a", label, attrs)


def _command_drawer() -> str:
    links = [
        ("Open judge packet", "judge_packet.md"),
        ("Open dashboard", "project_readiness_dashboard.html"),
        ("Open launch packet", "launch_packet.md"),
        ("Open final checklist", "submission_checklist.md"),
        ("Open release manifest", "release_manifest.json"),
        ("Read README", "../../README.md"),
        ("Read architecture", "../../docs/architecture.md"),
        ("Read Copilot build log", "../../docs/copilot_build_log.md"),
        ("Read submission notes", "../../docs/submission_notes.md"),
    ]
    body = _tag("div", "Command Links", "class=\"drawer-kicker\"")
    body += _tag("h2", "Settings Command Drawer")
    body += _tag("p", "Quick-launch proof artifacts and submission docs without leaving the War Room.")
    body += _tag("div", "".join(_command_link(label, href) for label, href in links), "class=\"drawer-links\"")
    body += _tag("a", "Close", "href=\"#war-room\" class=\"drawer-close\"")
    return _tag("aside", body, "class=\"command-drawer\" aria-label=\"settings command drawer\"")


def render_dashboard(profile: dict[str, Any], rules: dict[str, Any], report: dict[str, Any]) -> str:
    verdict = escape(str(report.get("verdict", "UNKNOWN")))
    score = escape(str(report.get("readiness_score", 0)))
    project = escape(str(report.get("project_name", "Hackathon War Room")))
    tagline = escape(str(profile.get("tagline", "Turn hackathon chaos into a judge ready launch packet.")))
    next_action = escape(str(report.get("next_safest_action", "Unknown")))
    iq = escape(str(profile.get("primary_iq_fit", "Foundry IQ")))
    battle = escape(str(rules.get("battle", "Creative Apps with GitHub Copilot")))
    bg_uri = _asset_data_uri("perfect_mockup_image.png")
    css = Path(__file__).with_name("dashboard_theme.css").read_text(encoding="utf-8").replace("__MOCKUP_IMAGE__", bg_uri)
    head = _void("meta", "charset=\"utf-8\"") + _void("meta", "name=\"viewport\" content=\"width=device-width, initial-scale=1\"") + _tag("title", "Hackathon War Room Dashboard") + _tag("style", css)
    topline = _tag("div", _tag("span", "Command Deck // Hackathon War Room") + _tag("strong", "Submission Candidate"), "class=\"topline\"")
    status_strip = _tag(
        "div",
        _tag("div", _tag("span", "Track") + _tag("strong", "Creative Apps"), "class=\"status-chip\"")
        + _tag("div", _tag("span", "Launch Gate") + _tag("strong", verdict), "class=\"status-chip\"")
        + _tag("div", _tag("span", "Readiness") + _tag("strong", score + "/100"), "class=\"status-chip\"")
        + _tag("div", _tag("span", "IQ Layer") + _tag("strong", iq), "class=\"status-chip\""),
        "class=\"status-strip\"",
    )
    hero = _tag("section", topline + _tag("div", "Mission Board // Creative Apps", "class=\"kicker\"") + _tag("h1", project, "class=\"title\"") + _tag("p", tagline, "class=\"tagline\"") + _tag("span", battle, "class=\"pill\"") + status_strip, "id=\"war-room\" class=\"hero\"")
    cards = _tag("section", _tag("div", _tag("div", "Launch Gate", "class=\"label\"") + _tag("div", verdict, "class=\"big verdict\""), "class=\"card launch\"") + _tag("div", _tag("div", "Readiness", "class=\"label\"") + _tag("div", score + "/100", "class=\"big\""), "class=\"card\"") + _tag("div", _tag("div", "Microsoft IQ", "class=\"label\"") + _tag("div", iq, "class=\"big\""), "class=\"card ok\""), "id=\"launch\" class=\"cards\"")
    scorecard = _tag("section", _tag("div", _tag("h2", "Scorecard") + _score_rows(report.get("category_scores", {})), "class=\"card\"") + _tag("div", _tag("h2", "Readiness Gauge") + _tag("div", _tag("strong", score), "class=\"score-ring\""), "class=\"card\""), "id=\"scorecard\" class=\"grid\"")
    lens = _tag("section", _tag("div", _tag("h2", "Judge Lens") + _tag("ul", _li(report.get("strengths", [])), "class=\"list\""), "class=\"card\"") + _tag("div", _tag("h2", "Risk Console") + _tag("ul", _li(report.get("risks", [])), "class=\"list\""), "class=\"card risk\""), "id=\"risk-console\" class=\"grid\"")
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
        "id=\"copilot-log\" class=\"grid\"",
    )
    asset_bay = _tag("section", _tag("h2", "Asset Bay") + _tag("div", _artifact_cards(profile), "class=\"artifact-grid\""), "id=\"assets\" class=\"card\"")
    action = _tag("section", _tag("h2", "Next Safest Action") + _tag("p", next_action, "class=\"tagline\""), "id=\"settings\" class=\"card\"")
    footer = _tag("div", "Powered by Citadel AI // synthetic demo data only // generated locally", "class=\"footer\"")
    hotspots = _dashboard_hotspots()
    drawer = _command_drawer()
    nav = _tag("aside", _tag("div", "CITADEL-AI", "class=\"brand-mark\"") + _tag("a", "War Room", "href=\"#war-room\" class=\"nav-item active\"") + _tag("a", "Scorecard", "href=\"#scorecard\" class=\"nav-item\"") + _tag("a", "Assets", "href=\"#assets\" class=\"nav-item\"") + _tag("a", "Risk Console", "href=\"#risk-console\" class=\"nav-item\"") + _tag("a", "Copilot Log", "href=\"#copilot-log\" class=\"nav-item\"") + _tag("a", "Settings", "href=\"#settings\" class=\"nav-item\""), "class=\"side-nav\"")
    content = _tag("main", hero + cards + scorecard + lens + intelligence + asset_bay + action + footer, "class=\"wrap\"")
    main = _tag("div", nav + hotspots + drawer + content, "class=\"shell\"")
    return "<!doctype html>\n" + _tag("html", _tag("head", head) + _tag("body", main), "lang=\"en\"") + "\n"


def write_dashboard(root: Path, profile: dict[str, Any], rules: dict[str, Any], report: dict[str, Any]) -> Path:
    output_dir = root / "demo" / "output"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "project_readiness_dashboard.html"
    output_path.write_text(render_dashboard(profile, rules, report), encoding="utf-8")
    return output_path
