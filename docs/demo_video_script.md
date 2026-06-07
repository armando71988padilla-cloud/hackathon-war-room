# Hackathon War Room Demo Video Script

Target length: 90 to 120 seconds

## Opening Hook

Hackathons are not just about building. They are about shipping clearly.

Most teams do not lose because they built nothing. They lose because the final project story is scattered: the README is unfinished, the demo is unclear, judging criteria are easy to miss, risks are invisible, and nobody knows when to stop adding features.

Hackathon War Room turns that chaos into a judge ready launch packet.

## Scene 1 - Cinematic Mission Board

Show the final dashboard:
`demo/output/project_readiness_dashboard.html`

Narration: Hackathon War Room is an AI assisted creative command center for hackathon builders. It turns project state, challenge rules, judging criteria, risks, and asset readiness into a clean launch plan.

Point out the Citadel-AI styled dashboard, sidebar tabs, Launch Gate, scorecard, Asset Bay, and command drawer.

## Scene 2 - Launch Gate

Show the top dashboard cards.

Narration: The Launch Gate gives the project a clear verdict. This demo shows `READY TO SUBMIT` with a readiness score of `94/100`. The point is not to overbuild forever. The point is to know when the project is strong enough to freeze, record, and submit.

## Scene 3 - Judge Lens And Risk Console

Click or point to the Scorecard and Risk Console areas.

Narration: Judge Lens reframes the project through what judges need to see: rules compliance, demo clarity, technical completeness, judge appeal, safety readiness, and asset polish. Risks stay visible instead of getting buried at the end.

## Scene 4 - Asset Bay

Show the Asset Bay links.

Narration: Asset Bay turns submission assets into clickable proof points: README, judge packet, dashboard, demo script, architecture notes, final checklist, and Copilot build log. Builders can jump straight from the dashboard into the materials judges care about.

## Scene 5 - Settings Command Drawer

Click the Settings tab.

Narration: The Settings command drawer gives quick access to proof artifacts and submission docs without leaving the War Room. It is a lightweight command center for final review.

## Scene 6 - Export The Launch Bundle

Run:

```bash
PYTHONPATH="$PWD/src" python3 -m hackathon_war_room export
```

Narration: One deterministic local command exports the judge packet, dashboard, launch packet, checklist, Copilot summary, and release manifest.

## Scene 7 - Release Manifest And Proof

Open or mention:
`demo/output/release_manifest.json`

Narration: The release manifest records the project identity, track, Foundry IQ alignment, launch gate, quality signals, safety posture, artifacts, proof commands, and freeze guidance. It does not claim a live Foundry deployment. It shows a Foundry IQ aligned workflow with deterministic local fallback.

## Scene 8 - Final Check And Smoke Test

Run:

```bash
PYTHONPATH="$PWD/src" python3 -m hackathon_war_room final-check
PYTHONPATH="$PWD/src" python3 tests/test_demo_workflow.py
```

Expected proof:

```text
WAR_ROOM_FINAL_CHECK_OK
WAR_ROOM_SMOKE_OK
```

Narration: The workflow is locally testable, CI backed, synthetic-data-only, and safe for public judging.

## Scene 9 - GitHub Actions Proof

Show the latest GitHub Actions Smoke Test success if time allows.

Narration: The same smoke workflow runs in GitHub Actions on push, which gives judges a public reliability signal.

## Closing Line

The funny part is that this tool could help teams submit to the same hackathon it was built for.

## Recording Notes

- Keep the dashboard visible as the visual hero.
- Do not mention unfinished features.
- Do not claim live Microsoft Foundry deployment.
- Say Foundry IQ aligned, not Foundry deployed.
- Keep the final proof commands on screen long enough to read.
- Record the video only after the final repo proof sweep is green.

