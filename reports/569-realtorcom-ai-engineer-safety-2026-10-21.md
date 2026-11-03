# Evaluation: Realtor.com — AI Engineer, AI Safety & Guardrails

**Date:** 2026-10-21
**URL:** (pasted JD — same role as #460, 2026-09-24)
**Archetype:** AI Platform / LLMOps + PropTech AI Engineer
**Score:** 4.8/5
**Legitimacy:** High Confidence
**PDF:** output/VenkataLakshmiParimala-realtorcom-ai-safety-engineer.pdf

---

Note: Same role previously evaluated as #460 (4.8/5, 2026-09-24). CV regenerated with updated ATS optimization.

## Key Match Signals

- LLM-as-judge + evaluation harness: AgentProbe (15-endpoint FastAPI, 5-metric eval, 1,240 test cases, CI golden datasets)
- LeaseI: 93.6% precision, 87.9% F1 — exactly the metrics this JD asks for; safety boundary that never lets LLM resolve Fair Housing decisions
- **Fair Housing Act domain**: 8 years at Entrata (LIHTC, HUD, HAP, HCV, affordable housing compliance) — the exact domain RealAssist operates in; no generalist AI candidate has this
- Intuit: LLM guardrails (prompt injection filtering, sensitive-data handling, hallucination regression tests) in production financial app
- Python, FastAPI, Terraform, Docker, AWS, GitHub Actions CI/CD — all confirmed in cv.md
- PropTech +0.3 boost applied

## Gap

- Google Cloud Model Armor / Vertex AI: GCP knowledge is basic (coursework, not production); note adjacent experience with AWS Bedrock-equivalent patterns and Azure AI Content Safety patterns

## Keywords extracted

AI safety, guardrails, LLM-as-judge, classifier, Fair Housing Act, content moderation, precision/recall/F1, confusion matrix, labeled eval dataset, train/test/validate, eval framework, homegrown harness, prompt injection, jailbreak defense, OWASP LLM Top 10, adversarial testing, red-teaming, CI regression, overblocking, Google Cloud Model Armor, Terraform, Python, real estate, compliance, RealAssist
