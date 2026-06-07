from __future__ import annotations

import json
import sys
from pathlib import Path

from hackathon_war_room.core.evaluate import evaluate_project


def project_root() -> Path:
    return Path(__file__).resolve().parents[2]


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def build_report() -> dict:
    root = project_root()
    profile = load_json(root / "demo" / "sample_project_profile.json")
    rules = load_json(root / "demo" / "sample_rules_summary.json")
    return evaluate_project(profile, rules)


def print_report(report: dict) -> None:
    print("Project: {}".format(report["project_name"]))
    print("Track: {}".format(report["track"]))
    print("Readiness score: {}/100".format(report["readiness_score"]))
    print("Launch Gate: {}".format(report["verdict"]))
    print("Next safest action: {}".format(report["next_safest_action"]))


def run_demo() -> int:
    root = project_root()
    output_dir = root / "demo" / "output"
    output_dir.mkdir(parents=True, exist_ok=True)
    print("Hackathon War Room")
    print("Mission status: scoring engine online")
    print_report(build_report())
    print(f"Output bay: {output_dir}")
    print("WAR_ROOM_DEMO_READY")
    return 0


def run_evaluate() -> int:
    print_report(build_report())
    print("WAR_ROOM_EVALUATE_OK")
    return 0


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    command = args[0] if args else "demo"
    if command == "demo":
        return run_demo()
    if command == "evaluate":
        return run_evaluate()
    if command in {"help", "--help", "-h"}:
        print("Usage: PYTHONPATH=\"$PWD/src\" python3 -m hackathon_war_room demo")
        print("Commands: demo, evaluate")
        return 0
    print(f"Unknown command: {command}")
    print("Usage: PYTHONPATH=\"$PWD/src\" python3 -m hackathon_war_room demo")
    print("Commands: demo, evaluate")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
