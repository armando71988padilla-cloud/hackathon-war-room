from __future__ import annotations

from typing import Any


WEIGHTS = {
    "rules_compliance": 25,
    "demo_clarity": 20,
    "technical_completeness": 20,
    "judge_appeal": 15,
    "safety_readiness": 10,
    "asset_polish": 10,
}


def verdict_for_score(score: int) -> str:
    if score >= 90:
        return "READY TO SUBMIT"
    if score >= 75:
        return "NEEDS POLISH"
    if score >= 50:
        return "AT RISK"
    return "BLOCKED"


def _lower_list(values: list[Any]) -> list[str]:
    return [str(value).lower() for value in values]


def _score_rules(profile: dict[str, Any], rules: dict[str, Any]) -> int:
    score = 0
    if profile.get("track") == rules.get("track"):
        score += 7
    if profile.get("primary_iq_fit"):
        score += 7
    if profile.get("uses_synthetic_data") is True:
        score += 6
    planned = " ".join(_lower_list(profile.get("features_planned", [])))
    if "copilot" in planned:
        score += 5
    return min(score, WEIGHTS["rules_compliance"])


def _score_demo_clarity(profile: dict[str, Any]) -> int:
    score = 6
    if profile.get("tagline"):
        score += 4
    if profile.get("demo_video_status") == "recorded":
        score += 6
    planned = " ".join(_lower_list(profile.get("features_planned", [])))
    if "launch gate" in planned or "judge lens" in planned:
        score += 4
    return min(score, WEIGHTS["demo_clarity"])


def _score_technical(profile: dict[str, Any]) -> int:
    score = 4
    if profile.get("repo_status"):
        score += 4
    if profile.get("ci_status") == "configured":
        score += 5
    if profile.get("features_planned"):
        score += 4
    assets = profile.get("assets", {})
    if assets.get("judge_packet") and assets.get("dashboard"):
        score += 3
    return min(score, WEIGHTS["technical_completeness"])


def _score_judge_appeal(profile: dict[str, Any]) -> int:
    planned = " ".join(_lower_list(profile.get("features_planned", [])))
    score = 5
    for phrase in ["judge lens", "launch gate", "copilot battle log", "demo producer", "safety"]:
        if phrase in planned:
            score += 2
    return min(score, WEIGHTS["judge_appeal"])


def _score_safety(profile: dict[str, Any], rules: dict[str, Any]) -> int:
    score = 0
    if profile.get("uses_synthetic_data") is True:
        score += 5
    if rules.get("security_rules"):
        score += 3
    risks = " ".join(_lower_list(profile.get("known_risks", [])))
    if "secret" not in risks and "credential" not in risks:
        score += 2
    return min(score, WEIGHTS["safety_readiness"])


def _score_assets(profile: dict[str, Any]) -> int:
    required = ["readme", "dashboard", "judge_packet", "demo_script", "submission_checklist", "copilot_build_log"]
    assets = profile.get("assets", {})
    complete = sum(1 for item in required if assets.get(item) is True)
    return round((complete / len(required)) * WEIGHTS["asset_polish"])


def evaluate_project(profile: dict[str, Any], rules: dict[str, Any]) -> dict[str, Any]:
    category_scores = {
        "rules_compliance": _score_rules(profile, rules),
        "demo_clarity": _score_demo_clarity(profile),
        "technical_completeness": _score_technical(profile),
        "judge_appeal": _score_judge_appeal(profile),
        "safety_readiness": _score_safety(profile, rules),
        "asset_polish": _score_assets(profile),
    }
    total = int(sum(category_scores.values()))
    risks = list(profile.get("known_risks", []))
    strengths = [
        "Clear Creative Apps fit",
        "Foundry IQ alignment through grounded project context",
        "Synthetic data posture",
        "Strong Copilot assisted development story planned",
    ]
    if total >= 90:
        next_action = "Record the final demo video, capture the dashboard screenshot, run the smoke test, and freeze feature changes."
    elif total >= 75:
        next_action = "Finish the missing submission assets, regenerate exports, and rerun the smoke test."
    else:
        next_action = "Resolve blocking risks before adding polish or recording the final demo."
    return {
        "project_name": profile.get("project_name", "Unknown Project"),
        "track": profile.get("track", "Unknown Track"),
        "readiness_score": total,
        "verdict": verdict_for_score(total),
        "category_scores": category_scores,
        "strengths": strengths,
        "risks": risks,
        "next_safest_action": next_action,
    }
