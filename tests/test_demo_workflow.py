from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def run_cli(command: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "hackathon_war_room", command],
        cwd=ROOT,
        env={"PYTHONPATH": str(ROOT / "src")},
        text=True,
        capture_output=True,
        check=False,
    )


def main() -> int:
    profile_path = ROOT / "demo" / "sample_project_profile.json"
    rules_path = ROOT / "demo" / "sample_rules_summary.json"
    profile = load_json(profile_path)
    rules = load_json(rules_path)

    assert profile["project_name"] == "Hackathon War Room"
    assert profile["track"] == "Creative Apps"
    assert profile["uses_synthetic_data"] is True
    assert rules["track"] == "Creative Apps"
    assert "Demonstrate meaningful GitHub Copilot usage during development" in rules["core_requirements"]

    demo_result = run_cli("demo")
    assert demo_result.returncode == 0, demo_result.stderr
    assert "Readiness score: 94/100" in demo_result.stdout
    assert "Launch Gate: READY TO SUBMIT" in demo_result.stdout
    assert "WAR_ROOM_DEMO_READY" in demo_result.stdout

    evaluate_result = run_cli("evaluate")
    assert evaluate_result.returncode == 0, evaluate_result.stderr
    assert "Readiness score: 94/100" in evaluate_result.stdout
    assert "Launch Gate: READY TO SUBMIT" in evaluate_result.stdout
    assert "WAR_ROOM_EVALUATE_OK" in evaluate_result.stdout

    export_result = run_cli("export")
    assert export_result.returncode == 0, export_result.stderr
    assert "Judge packet:" in export_result.stdout
    assert "Dashboard:" in export_result.stdout
    assert "Generated artifacts: 6" in export_result.stdout
    assert "WAR_ROOM_EXPORT_OK" in export_result.stdout
    judge_packet = ROOT / "demo" / "output" / "judge_packet.md"
    assert judge_packet.exists()
    packet_text = judge_packet.read_text(encoding="utf-8")
    assert "Hackathon War Room - Judge Packet" in packet_text
    assert "Launch Gate" in packet_text

    dashboard = ROOT / "demo" / "output" / "project_readiness_dashboard.html"
    assert dashboard.exists()
    dashboard_text = dashboard.read_text(encoding="utf-8")
    assert "Hackathon War Room Dashboard" in dashboard_text
    assert "Mission Board" in dashboard_text
    assert "Risk Console" in dashboard_text
    assert "Asset Bay" in dashboard_text
    assert "README" in dashboard_text
    assert "Architecture doc" in dashboard_text
    assert "Copilot build log" in dashboard_text
    assert "READY TO SUBMIT" in dashboard_text

    launch_packet = ROOT / "demo" / "output" / "launch_packet.md"
    release_manifest = ROOT / "demo" / "output" / "release_manifest.json"
    submission_checklist = ROOT / "demo" / "output" / "submission_checklist.md"
    copilot_summary = ROOT / "demo" / "output" / "copilot_battle_log_summary.md"

    for artifact in [launch_packet, release_manifest, submission_checklist, copilot_summary]:
        assert artifact.exists(), artifact

    assert "Hackathon War Room - Launch Packet" in launch_packet.read_text(encoding="utf-8")
    assert "READY TO SUBMIT" in release_manifest.read_text(encoding="utf-8")
    assert "Generated Submission Checklist" in submission_checklist.read_text(encoding="utf-8")
    assert "Copilot Battle Log Summary" in copilot_summary.read_text(encoding="utf-8")

    print("WAR_ROOM_SMOKE_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
