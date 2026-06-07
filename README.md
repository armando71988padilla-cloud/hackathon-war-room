# Hackathon War Room

Hackathon War Room is an AI assisted creative command center for hackathon builders.

It turns raw project state, challenge rules, judging criteria, risk signals, and asset status into a judge ready launch packet.

## Track

Creative Apps - Battle 1 with GitHub Copilot

## Microsoft IQ Alignment

Hackathon War Room aligns with Foundry IQ by grounding its guidance in project profiles, challenge rules, judging criteria, risks, and artifact status to generate structured, explainable build guidance and submission outputs.

## Current Demo

The demo uses synthetic project data only. It does not require private repositories, customer data, credentials, production logs, or confidential documents.

## Quick Start

```bash
PYTHONPATH="$PWD/src" python3 -m hackathon_war_room demo
```

## Smoke Test

```bash
PYTHONPATH="$PWD/src" python3 tests/test_demo_workflow.py
```

Expected output:

```text
WAR_ROOM_SMOKE_OK
```

## Core Concept

Most hackathon teams do not lose because they cannot build anything. They lose because the final project is scattered: the README is unfinished, the demo is unclear, judging criteria are easy to miss, assets are missing, risks are unknown, and nobody knows when to stop adding features.

Hackathon War Room helps builders move from chaos to launch by generating readiness scores, risk reports, demo scripts, judge packets, and final submission checklists.

