# Hackathon War Room

**Turn hackathon chaos into a judge ready launch packet.**

Hackathon War Room is an AI assisted creative command center for hackathon builders. It helps solo builders and teams turn scattered project state, challenge rules, judging criteria, missing assets, and risk signals into a polished submission package.

Built for the **Agents League Hackathon - Creative Apps track**.

---

## What It Does

Hackathon War Room gives a project team a local mission-control workflow:

| Capability | Purpose |
|---|---|
| **Launch Gate** | Scores readiness and gives a clear verdict: `READY TO SUBMIT`, `NEEDS POLISH`, `AT RISK`, or `BLOCKED`. |
| **Judge Lens** | Highlights what judges should notice first. |
| **Risk Console** | Keeps unresolved risks visible before final submission. |
| **Asset Bay** | Shows readiness for README, dashboard, judge packet, architecture doc, demo script, checklist, and Copilot log. |
| **Dark Dashboard** | Generates a cinematic HTML dashboard for review, screenshots, and demo video. |
| **Judge Packet** | Exports a concise judge-facing project summary. |
| **Launch Bundle** | Produces a full output bundle including launch packet, checklist, Copilot summary, and release manifest. |
| **Smoke Test + CI** | Verifies the core workflow locally and in GitHub Actions. |

---

## Why It Exists

Hackathon teams rarely lose only because they cannot build. They lose because the final project story is scattered.

The README is unfinished. The demo is unclear. Judging criteria are easy to miss. Safety notes are missing. Risk is invisible. Nobody knows when to stop adding features.

Hackathon War Room turns that chaos into a structured final launch path.

---

## Microsoft IQ Alignment

Hackathon War Room aligns with **Foundry IQ** by grounding guidance in:

- project profile context
- challenge rules
- judging criteria
- artifact readiness
- risk signals
- safety posture

This repository does **not** claim a live Foundry deployment. The current build uses deterministic local sample data for reliable judging and includes a clear path for future Foundry or agent framework integration.

---

## GitHub Copilot / AI Assisted Development Story

The Creative Apps track requires meaningful GitHub Copilot or AI assisted development usage.

This project documents that story in:

```text
docs/copilot_build_log.md
demo/output/copilot_battle_log_summary.md
```

The build process used AI assisted development to shape:

- project concept and Creative Apps fit
- CLI workflow
- scoring logic
- smoke tests
- dashboard polish
- README and docs
- launch bundle outputs

Human oversight kept the workflow deterministic, local-first, synthetic-data-only, and safe for public judging.

---

## Current Launch Gate

Current demo profile output:

```text
Readiness score: 94/100
Launch Gate: READY TO SUBMIT
```

Run it locally:

```bash
PYTHONPATH="$PWD/src" python3 -m hackathon_war_room evaluate
```

---

## Quick Start

```bash
PYTHONPATH="$PWD/src" python3 -m hackathon_war_room demo
```

## Export Full Launch Bundle

```bash
PYTHONPATH="$PWD/src" python3 -m hackathon_war_room export
```

Generated outputs:

```text
demo/output/judge_packet.md
demo/output/project_readiness_dashboard.html
demo/output/launch_packet.md
demo/output/submission_checklist.md
demo/output/copilot_battle_log_summary.md
demo/output/release_manifest.json
```

## Smoke Test

```bash
PYTHONPATH="$PWD/src" python3 tests/test_demo_workflow.py
```

Expected output:

```text
WAR_ROOM_SMOKE_OK
```

---

## Project Structure

```text
src/hackathon_war_room/__main__.py            CLI entrypoint
src/hackathon_war_room/core/evaluate.py       readiness scoring and Launch Gate logic
src/hackathon_war_room/core/dashboard.py      dark dashboard exporter
src/hackathon_war_room/core/export_packet.py  judge packet exporter
src/hackathon_war_room/core/launch_bundle.py  full launch bundle exporter
tests/test_demo_workflow.py                   deterministic smoke test
demo/sample_project_profile.json              synthetic project profile
demo/sample_rules_summary.json                synthetic challenge/rules summary
docs/architecture.md                          architecture notes
docs/copilot_build_log.md                     Copilot / AI assisted build log
docs/demo_video_script.md                     demo video script
docs/final_submission_checklist.md            final checklist
docs/submission_safety.md                     safety posture
docs/submission_notes.md                      portal-ready notes
```

---

## Safety Posture

The demo uses **synthetic data only**.

Do not include:

- API keys
- passwords
- tokens
- credentials
- customer data
- personally identifiable information
- confidential company data
- private repository contents
- production logs
- NDA or pre-release product information

Sensitive configuration should stay in environment variables and out of Git.

---

## Design Philosophy

Hackathon War Room is intentionally deterministic and local-first.

That makes it reliable for judging:

- no required cloud credentials
- no private data
- no hidden dependencies
- repeatable CLI commands
- smoke test coverage
- GitHub Actions workflow

---

## Final Submission Flow

1. Run export.
2. Run smoke test.
3. Confirm GitHub Actions is green.
4. Review generated dashboard and launch packet.
5. Capture dashboard screenshot.
6. Record final demo video.
7. Paste final portal description.
8. Submit.

Video and portal submission should happen only after final feature freeze.
