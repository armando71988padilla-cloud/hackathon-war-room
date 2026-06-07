# Submission Notes

## Tagline

Turn hackathon chaos into a judge ready launch packet.

## Portal Description Under 1000 Characters

Hackathon War Room is an AI assisted creative command center for hackathon builders. It helps teams turn scattered project state, challenge rules, judging criteria, risks, and missing assets into a clean launch plan. The tool scores submission readiness, shows a Launch Gate verdict, highlights what judges should notice through Judge Lens, and exports a judge packet plus a dark readiness dashboard. It aligns with Foundry IQ by grounding guidance in project context, rules summaries, artifact status, and safety signals. The demo uses synthetic data only, includes a deterministic local CLI, GitHub Actions smoke test, Copilot build log, architecture notes, demo script, and final checklist so builders can stop guessing, stop overbuilding, and ship stronger submissions.

## Short Pitch

Hackathon War Room helps builders stop overbuilding and ship stronger hackathon submissions with a readiness score, Judge Lens, risk console, dashboard, and judge packet.

## Demo Closing Line

The funny part is that this tool could help teams submit to the same hackathon it was built for.

## Final Proof Commands

```bash
PYTHONPATH="$PWD/src" python3 -m hackathon_war_room export
PYTHONPATH="$PWD/src" python3 tests/test_demo_workflow.py
```
