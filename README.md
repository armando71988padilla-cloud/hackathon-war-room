# Hackathon War Room

Hackathon War Room is an AI assisted creative command center for hackathon builders.

It turns raw project state, challenge rules, judging criteria, risk signals, and asset status into a judge ready launch packet.

## Track

Creative Apps - Battle 1 with GitHub Copilot

## Tagline

Turn hackathon chaos into a judge ready launch packet.

## Why It Exists

Most hackathon teams do not lose because they cannot build anything. They lose because the final project is scattered: the README is unfinished, the demo is unclear, judging criteria are easy to miss, risks are unknown, and nobody knows when to stop adding features.

Hackathon War Room gives builders a Launch Gate, Judge Lens, Risk Console, scorecard, judge packet, and dashboard so they can stop guessing and ship cleanly.

## Microsoft IQ Alignment

Hackathon War Room aligns with Foundry IQ by grounding its guidance in project profiles, challenge rules, judging criteria, risks, and artifact status to generate structured, explainable build guidance and submission outputs.

This repository does not claim a live Foundry deployment. It uses deterministic local sample data for reliable judging and includes a clear path for future Foundry or agent framework integration.

## GitHub Copilot Story

The project includes a Copilot Build Log in `docs/copilot_build_log.md` documenting how AI assisted development shaped the implementation, CLI flow, tests, scoring, and dashboard polish.

## Current Demo

The demo uses synthetic project data only. It does not require private repositories, customer data, credentials, production logs, or confidential documents.

## Quick Start

```bash
PYTHONPATH="$PWD/src" python3 -m hackathon_war_room demo
```

## Export Judge Assets

```bash
PYTHONPATH="$PWD/src" python3 -m hackathon_war_room export
```

This creates:

- `demo/output/judge_packet.md`
- `demo/output/project_readiness_dashboard.html`

## Smoke Test

```bash
PYTHONPATH="$PWD/src" python3 tests/test_demo_workflow.py
```

Expected output:

```text
WAR_ROOM_SMOKE_OK
```

## Architecture

See `docs/architecture.md`.

## Submission Safety

See `docs/submission_safety.md`. The project uses synthetic demo data only and should not include secrets, credentials, private customer data, or confidential materials.

