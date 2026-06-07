from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def _yes(value: bool) -> str:
    return "ready" if value else "missing"


def _bullets(items: list[Any]) -> list[str]:
    if not items:
        return ["- None listed"]
    return ["- {}".format(item) for item in items]


def artifact_status(profile: dict[str, Any]) -> list[dict[str, Any]]:
    assets = profile.get("assets", {})
    return [
        {"name": "README", "path": "README.md", "ready": bool(assets.get("readme"))},
        {"name": "Judge packet", "path": "demo/output/judge_packet.md", "ready": bool(assets.get("judge_packet"))},
        {"name": "Dashboard", "path": "demo/output/project_readiness_dashboard.html", "ready": bool(assets.get("dashboard"))},
        {"name": "Demo script", "path": "docs/demo_video_script.md", "ready": bool(assets.get("demo_script"))},
        {"name": "Architecture doc", "path": "docs/architecture.md", "ready": bool(assets.get("architecture_doc"))},
        {"name": "Final checklist", "path": "docs/final_submission_checklist.md", "ready": bool(assets.get("submission_checklist"))},
        {"name": "Copilot build log", "path": "docs/copilot_build_log.md", "ready": bool(assets.get("copilot_build_log"))},
    ]


def render_launch_packet(profile: dict[str, Any], rules: dict[str, Any], report: dict[str, Any]) -> str:
    status = artifact_status(profile)
    lines: list[str] = []
    lines.append("# Hackathon War Room - Launch Packet")
    lines.append("")
    lines.append("## Mission")
    lines.append("")
    lines.append(profile.get("tagline", "Turn hackathon chaos into a judge ready launch packet."))
    lines.append("")
    lines.append("## Launch Gate")
    lines.append("")
    lines.append("- Project: {}".format(report.get("project_name", "Hackathon War Room")))
    lines.append("- Track: {}".format(report.get("track", "Creative Apps")))
    lines.append("- Readiness score: {}/100".format(report.get("readiness_score", 0)))
    lines.append("- Verdict: {}".format(report.get("verdict", "UNKNOWN")))
    lines.append("- Next action: {}".format(report.get("next_safest_action", "Review final assets.")))
    lines.append("")
    lines.append("## Challenge Fit")
    lines.append("")
    lines.append("- Challenge: {}".format(rules.get("challenge", "Agents League Hackathon")))
    lines.append("- Battle: {}".format(rules.get("battle", "Creative Apps with GitHub Copilot")))
    lines.append("- Microsoft IQ layer: {}".format(profile.get("primary_iq_fit", "Foundry IQ")))
    lines.append("- Data posture: synthetic demo data only")
    lines.append("")
    lines.append("## Artifact Readiness")
    lines.append("")
    for item in status:
        lines.append("- {}: {} ({})".format(item["name"], _yes(item["ready"]), item["path"]))
    lines.append("")
    lines.append("## Judge Lens")
    lines.append("")
    lines.extend(_bullets(report.get("strengths", [])))
    lines.append("")
    lines.append("## Risk Console")
    lines.append("")
    lines.extend(_bullets(report.get("risks", [])))
    lines.append("")
    lines.append("## Final Demo Path")
    lines.append("")
    lines.append("1. Open the dark dashboard.")
    lines.append("2. Show the Launch Gate and readiness score.")
    lines.append("3. Show Judge Lens, Risk Console, and Microsoft IQ alignment.")
    lines.append("4. Run the export command.")
    lines.append("5. Run the smoke test.")
    lines.append("6. Close with the hackathon meta-angle: this tool can help teams submit to the same competition it was built for.")
    lines.append("")
    lines.append("## Final Proof Commands")
    lines.append("")
    lines.append("```bash")
    lines.append('PYTHONPATH="$PWD/src" python3 -m hackathon_war_room export')
    lines.append('PYTHONPATH="$PWD/src" python3 tests/test_demo_workflow.py')
    lines.append("```")
    lines.append("")
    return "\n".join(lines)


def render_submission_checklist(profile: dict[str, Any], report: dict[str, Any]) -> str:
    status = artifact_status(profile)
    lines: list[str] = []
    lines.append("# Generated Submission Checklist")
    lines.append("")
    lines.append("## Launch Gate")
    lines.append("")
    lines.append("- Score: {}/100".format(report.get("readiness_score", 0)))
    lines.append("- Verdict: {}".format(report.get("verdict", "UNKNOWN")))
    lines.append("")
    lines.append("## Required Assets")
    lines.append("")
    for item in status:
        mark = "[x]" if item["ready"] else "[ ]"
        lines.append("- {} {} - `{}`".format(mark, item["name"], item["path"]))
    lines.append("")
    lines.append("## Final Manual Steps")
    lines.append("")
    lines.append("- [ ] Capture dashboard screenshot")
    lines.append("- [ ] Record final demo video after feature freeze")
    lines.append("- [ ] Paste final portal description")
    lines.append("- [ ] Attach public GitHub repository")
    lines.append("- [ ] Run final smoke test after any wording changes")
    lines.append("- [ ] Confirm no secrets or private data are included")
    lines.append("")
    return "\n".join(lines)


def render_copilot_summary(profile: dict[str, Any], rules: dict[str, Any], report: dict[str, Any]) -> str:
    lines: list[str] = []
    lines.append("# Copilot Battle Log Summary")
    lines.append("")
    lines.append("## Track Requirement")
    lines.append("")
    lines.append("The Creative Apps track requires meaningful GitHub Copilot or AI assisted development usage.")
    lines.append("")
    lines.append("## How War Room Shows That")
    lines.append("")
    lines.append("- The project includes a documented Copilot Build Log.")
    lines.append("- The CLI, scoring, smoke tests, dashboard, README, and export flow were developed through an AI assisted build process.")
    lines.append("- Human oversight kept the workflow deterministic, local-first, synthetic-data-only, and safe for public judging.")
    lines.append("")
    lines.append("## Creative Apps Fit")
    lines.append("")
    lines.append("Hackathon War Room is a creative productivity app for builders. It helps teams shape raw work into a polished project story, not just manage tasks.")
    lines.append("")
    lines.append("## Microsoft IQ Fit")
    lines.append("")
    lines.append(profile.get("primary_iq_fit", "Foundry IQ"))
    lines.append("")
    lines.append(rules.get("war_room_alignment", {}).get("foundry_iq", "The workflow grounds recommendations in project context, rules, risks, and artifact status."))
    lines.append("")
    lines.append("## Current Launch Gate")
    lines.append("")
    lines.append("- Score: {}/100".format(report.get("readiness_score", 0)))
    lines.append("- Verdict: {}".format(report.get("verdict", "UNKNOWN")))
    lines.append("")
    return "\n".join(lines)


def build_release_manifest(profile: dict[str, Any], rules: dict[str, Any], report: dict[str, Any]) -> dict[str, Any]:
    artifacts = artifact_status(profile)
    proof_commands = [
        "PYTHONPATH=\"$PWD/src\" python3 -m hackathon_war_room export",
        "PYTHONPATH=\"$PWD/src\" python3 -m hackathon_war_room final-check",
        "PYTHONPATH=\"$PWD/src\" python3 tests/test_demo_workflow.py",
    ]
    return {
        "schema_version": "1.0",
        "project_name": report.get("project_name", "Hackathon War Room"),
        "tagline": profile.get("tagline", "Turn hackathon chaos into a judge ready launch packet."),
        "track": report.get("track", "Creative Apps"),
        "challenge": rules.get("challenge", "Agents League Hackathon"),
        "battle": rules.get("battle", "Battle 1 - Creative Apps with GitHub Copilot"),
        "project_type": profile.get("project_type", "AI assisted creative build command center"),
        "target_user": profile.get("target_user", "hackathon builders"),
        "microsoft_iq": {
            "primary_layer": profile.get("primary_iq_fit", "Foundry IQ"),
            "alignment_summary": rules.get("war_room_alignment", {}).get("foundry_iq", "Grounds recommendations in project context, rules, risks, and artifact status."),
            "live_foundry_deployment_claimed": False,
        },
        "launch_gate": {
            "readiness_score": report.get("readiness_score", 0),
            "verdict": report.get("verdict", "UNKNOWN"),
            "next_safest_action": report.get("next_safest_action", ""),
        },
        "quality_signals": {
            "ci_status": profile.get("ci_status", "unknown"),
            "smoke_test_expected_output": "WAR_ROOM_SMOKE_OK",
            "final_check_expected_output": "WAR_ROOM_FINAL_CHECK_OK",
            "generated_artifact_count": 6,
        },
        "safety_posture": {
            "uses_synthetic_data": profile.get("uses_synthetic_data") is True,
            "secret_hygiene_required": True,
            "private_data_required": False,
            "confidential_material_required": False,
        },
        "artifacts": artifacts,
        "proof_commands": proof_commands,
        "risks": report.get("risks", []),
        "freeze_guidance": "After export, smoke test, final check, screenshot, and demo assets are ready, stop feature churn and submit.",
    }

def write_launch_bundle(root: Path, profile: dict[str, Any], rules: dict[str, Any], report: dict[str, Any]) -> dict[str, Path]:
    output_dir = root / "demo" / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    launch_packet = output_dir / "launch_packet.md"
    submission_checklist = output_dir / "submission_checklist.md"
    copilot_summary = output_dir / "copilot_battle_log_summary.md"
    release_manifest = output_dir / "release_manifest.json"

    launch_packet.write_text(render_launch_packet(profile, rules, report) + "\n", encoding="utf-8")
    submission_checklist.write_text(render_submission_checklist(profile, report) + "\n", encoding="utf-8")
    copilot_summary.write_text(render_copilot_summary(profile, rules, report) + "\n", encoding="utf-8")
    release_manifest.write_text(json.dumps(build_release_manifest(profile, rules, report), indent=2) + "\n", encoding="utf-8")

    return {
        "launch_packet": launch_packet,
        "submission_checklist": submission_checklist,
        "copilot_battle_log_summary": copilot_summary,
        "release_manifest": release_manifest,
    }
