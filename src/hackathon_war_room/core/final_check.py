from __future__ import annotations

from pathlib import Path
from typing import Any

REQUIRED_FILES = [
    "README.md",
    "docs/architecture.md",
    "docs/copilot_build_log.md",
    "docs/demo_video_script.md",
    "docs/final_submission_checklist.md",
    "docs/submission_notes.md",
    "docs/submission_safety.md",
    ".github/workflows/smoke.yml",
]

REQUIRED_OUTPUTS = [
    "demo/output/judge_packet.md",
    "demo/output/project_readiness_dashboard.html",
    "demo/output/launch_packet.md",
    "demo/output/submission_checklist.md",
    "demo/output/copilot_battle_log_summary.md",
    "demo/output/release_manifest.json",
]

def _check_path(root: Path, rel_path: str) -> dict[str, Any]:
    path = root / rel_path
    return {"name": rel_path, "passed": path.exists(), "detail": str(path)}


def run_final_check(root: Path, profile: dict[str, Any], report: dict[str, Any]) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []

    for rel_path in REQUIRED_FILES:
        check = _check_path(root, rel_path)
        check["group"] = "required_file"
        checks.append(check)

    for rel_path in REQUIRED_OUTPUTS:
        check = _check_path(root, rel_path)
        check["group"] = "generated_output"
        checks.append(check)

    checks.append({"group": "runtime_truth", "name": "uses_synthetic_data", "passed": profile.get("uses_synthetic_data") is True, "detail": "demo profile must use synthetic data only"})
    checks.append({"group": "runtime_truth", "name": "launch_gate_ready", "passed": report.get("verdict") == "READY TO SUBMIT", "detail": str(report.get("verdict", "UNKNOWN"))})
    checks.append({"group": "runtime_truth", "name": "readiness_score_at_least_90", "passed": int(report.get("readiness_score", 0)) >= 90, "detail": str(report.get("readiness_score", 0))})
    checks.append({"group": "runtime_truth", "name": "ci_configured", "passed": profile.get("ci_status") == "configured", "detail": str(profile.get("ci_status", "unknown"))})

    passed = sum(1 for check in checks if check["passed"])
    failed = [check for check in checks if not check["passed"]]
    return {"project_name": report.get("project_name", "Hackathon War Room"), "readiness_score": report.get("readiness_score", 0), "verdict": report.get("verdict", "UNKNOWN"), "passed": passed, "total": len(checks), "failed": failed, "checks": checks, "final_check_passed": len(failed) == 0}

def format_final_check(result: dict[str, Any]) -> str:
    lines = [
        "Final Check: {}".format(result["project_name"]),
        "Launch Gate: {}".format(result["verdict"]),
        "Readiness score: {}/100".format(result["readiness_score"]),
        "Checks passed: {}/{}".format(result["passed"], result["total"]),
    ]
    if result["failed"]:
        lines.append("Failed checks:")
        for check in result["failed"]:
            lines.append("- {}: {}".format(check["name"], check["detail"]))
    else:
        lines.append("All final checks passed.")
    return chr(10).join(lines)
