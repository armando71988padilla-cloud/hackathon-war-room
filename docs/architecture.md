# Hackathon War Room Architecture

## Purpose

Hackathon War Room is a deterministic local command center for hackathon builders. It converts synthetic project profile data and challenge rule summaries into readiness scoring, judge-facing artifacts, a dark dashboard, full launch bundle, and final submission guidance.

## Runtime Flow

1. Load synthetic project profile from `demo/sample_project_profile.json`.
2. Load challenge rules from `demo/sample_rules_summary.json`.
3. Evaluate readiness with `hackathon_war_room.core.evaluate`.
4. Export `demo/output/judge_packet.md` with `hackathon_war_room.core.export_packet`.
5. Export `demo/output/project_readiness_dashboard.html` with `hackathon_war_room.core.dashboard`.
6. Export launch bundle artifacts with `hackathon_war_room.core.launch_bundle`.
7. Verify the full demo path with `tests/test_demo_workflow.py`.

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
- `core/launch_bundle.py`: full launch bundle exporter for launch packet, checklist, Copilot summary, and release manifest.
- `tests/test_demo_workflow.py`: deterministic smoke test covering CLI, score, verdict, dashboard panels, and artifact generation.

## Microsoft IQ Alignment

Hackathon War Room aligns with Foundry IQ through a grounded reasoning pattern: project context and rule summaries are treated as the trusted knowledge base, then transformed into cited, inspectable project guidance and artifacts.

The current build does not claim a live Microsoft Foundry deployment. Instead, it provides a deterministic local fallback that demonstrates the same core product behavior: grounding outputs in known context, reducing hallucination risk, and making every recommendation inspectable through generated artifacts.

### Grounding Sources

- synthetic project profile
- synthetic challenge rules summary
- judging criteria and track requirements
- artifact readiness state
- known risks
- safety and secret hygiene posture

### Foundry-Ready Extension Path

A future Foundry or Agent Framework integration could replace local JSON inputs with managed knowledge sources, connected project repositories, event rules, team documents, or challenge briefs. The current design keeps those boundaries explicit so the project remains safe and reliable for public hackathon judging.

## Creative Apps Fit

Hackathon War Room is a creative productivity application. It helps builders transform raw project work into a polished story, dashboard, launch packet, and submission plan.

## Safety Posture

The demo uses synthetic data only. No customer data, private repository contents, credentials, tokens, production logs, or confidential company data are required.

## Freeze Discipline

Video and portal submission happen last. After the final feature pass, remaining work should focus on screenshot capture, demo video recording, portal copy, safety review, and final release tagging.
