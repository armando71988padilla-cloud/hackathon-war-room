from __future__ import annotations

from pathlib import Path
from typing import Any


CATEGORY_LABELS = {
    "rules_compliance": "Rules compliance",
    "demo_clarity": "Demo clarity",
    "technical_completeness": "Technical completeness",
    "judge_appeal": "Judge appeal",
    "safety_readiness": "Safety readiness",
    "asset_polish": "Asset polish",
}


def _bullets(items: list[Any]) -> list[str]:
    if not items:
        return ["- None listed"]
    return ["- {}".format(item) for item in items]


def render_judge_packet(profile: dict[str, Any], rules: dict[str, Any], report: dict[str, Any]) -> str:
    lines: list[str] = []
    lines.append("# Hackathon War Room - Judge Packet")
    lines.append("")
    lines.append("## Project Summary")
    lines.append("")
    lines.append("**Project:** {}".format(report["project_name"]))
    lines.append("**Track:** {}".format(report["track"]))
    lines.append("**Challenge:** {}".format(rules.get("challenge", "Unknown challenge")))
    lines.append("**Battle:** {}".format(rules.get("battle", "Unknown battle")))
    lines.append("**Tagline:** {}".format(profile.get("tagline", "No tagline provided")))
    lines.append("")
    lines.append("Hackathon War Room is an AI assisted creative command center that helps builders turn scattered project state into a judge ready launch packet.")
    lines.append("")
    lines.append("## Launch Gate")
    lines.append("")
    lines.append("**Readiness score:** {} / 100".format(report["readiness_score"]))
    lines.append("**Verdict:** {}".format(report["verdict"]))
    lines.append("**Next safest action:** {}".format(report["next_safest_action"]))
    lines.append("")
    lines.append("## Scorecard")
    lines.append("")
    for key, value in report["category_scores"].items():
        label = CATEGORY_LABELS.get(key, key.replace("_", " ").title())
        lines.append("- {}: {}".format(label, value))
    lines.append("")
    lines.append("## Judge Lens")
    lines.append("")
    lines.extend(_bullets(report.get("strengths", [])))
    lines.append("")
    lines.append("## Known Risks")
    lines.append("")
    lines.extend(_bullets(report.get("risks", [])))
    lines.append("")
    lines.append("## Microsoft IQ Alignment")
    lines.append("")
    lines.append(profile.get("primary_iq_fit", "Foundry IQ"))
    lines.append("")
    lines.append(rules.get("war_room_alignment", {}).get("foundry_iq", "The workflow grounds recommendations in project context and rules."))
    lines.append("")
    lines.append("## Copilot Assisted Development Story")
    lines.append("")
    lines.append(rules.get("war_room_alignment", {}).get("copilot_usage", "The project documents AI assisted development through a Copilot build log."))
    lines.append("")
    lines.append("## Safety Posture")
    lines.append("")
    lines.append(rules.get("war_room_alignment", {}).get("safety", "The demo uses synthetic data only."))
    lines.append("")
    lines.append("## Required Before Final Submit")
    lines.append("")
    lines.append("- Export dashboard")
    lines.append("- Export demo script")
    lines.append("- Export final submission checklist")
    lines.append("- Record demo video")
    lines.append("- Confirm GitHub repository is public and clean")
    lines.append("- Run smoke test and evaluation proof")
    lines.append("")
    return "\n".join(lines) + "\n"


def write_judge_packet(root: Path, profile: dict[str, Any], rules: dict[str, Any], report: dict[str, Any]) -> Path:
    output_dir = root / "demo" / "output"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "judge_packet.md"
    output_path.write_text(render_judge_packet(profile, rules, report), encoding="utf-8")
    return output_path
