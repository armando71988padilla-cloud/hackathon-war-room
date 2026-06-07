# Hackathon War Room Architecture

## Purpose

Hackathon War Room is a deterministic local command center for hackathon builders. It converts synthetic project profile data and challenge rule summaries into readiness scoring, judge-facing artifacts, a dark dashboard, and final submission guidance.

## Runtime Flow

1. Load synthetic project profile from `demo/sample_project_profile.json`.
2. Load challenge rules from `demo/sample_rules_summary.json`.
3. Evaluate readiness with `hackathon_war_room.core.evaluate`.
4. Export `demo/output/judge_packet.md` with `hackathon_war_room.core.export_packet`.
5. Export `demo/output/project_readiness_dashboard.html` with `hackathon_war_room.core.dashboard`.
6. Verify the full demo path with `tests/test_demo_workflow.py`.

## Commands

```bash
PYTHONPATH="$PWD/src" python3 -m hackathon_war_room demo
PYTHONPATH="$PWD/src" python3 -m hackathon_war_room evaluate
PYTHONPATH="$PWD/src" python3 -m hackathon_war_room export
PYTHONPATH="$PWD/src" python3 tests/test_demo_workflow.py
```

## Core Modules

- `__main__.py`: CLI entrypoint for demo, evaluate, and export commands.
- `core/evaluate.py`: readiness scoring and Launch Gate verdict logic.
- `core/export_packet.py`: judge packet markdown exporter.
- `core/dashboard.py`: dark readiness dashboard HTML exporter.
- `tests/test_demo_workflow.py`: deterministic smoke test covering CLI, score, verdict, and artifact generation.

## Microsoft IQ Alignment

The project aligns with Foundry IQ by grounding output in project context, challenge requirements, judging criteria, artifact status, risk signals, and safety posture. It does not claim live Foundry deployment. The current build uses a deterministic local fallback for reliable judging.

## Safety Posture

The demo uses synthetic data only. No customer data, private repository contents, credentials, tokens, production logs, or confidential company data are required.

## Freeze Discipline

After smoke, CI, README, demo script, dashboard, judge packet, and final checklist are ready, feature work should freeze. Remaining work should focus on screenshots, video recording, portal copy, and final safety review.
