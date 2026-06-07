from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


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

    result = subprocess.run(
        [sys.executable, "-m", "hackathon_war_room", "demo"],
        cwd=ROOT,
        env={"PYTHONPATH": str(ROOT / "src")},
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    assert "WAR_ROOM_DEMO_READY" in result.stdout

    print("WAR_ROOM_SMOKE_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
