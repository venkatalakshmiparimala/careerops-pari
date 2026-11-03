# Evaluation: Boom — AI Engineer

**Date:** 2026-08-04
**URL:** via recruiter (boom.com)
**Archetype:** Applied AI Engineer / Forward Deployed Engineer
**Score:** 4.0/5
**Legitimacy:** High Confidence
**PDF:** ✅

---

## A) Role Summary

| Dimension | Detail |
|-----------|--------|
| **Archetype** | Applied AI Engineer — customer-facing agents + internal AI productivity, full agent stack ownership |
| **Domain** | Residential real estate — leasing, application, underwriting agents for low-to-moderate income renters |
| **Function** | Build — ship production AI agents and internal productivity tooling, own evals + observability |
| **Seniority** | Mid-to-senior (5+ years web dev, 1-2 years production LLM) |
| **Location** | Austin, TX — in-person (relocation required from Virginia) |
| **H-1B** | Not stated — seed-stage startup, needs verification at screen |
| **Comp** | Not disclosed ("directional and adjustable +/- based on competency") |
| **Stage** | Seed → Series A — small team, close collaboration with co-founders |
| **Interview** | Likely 2–3 rounds (early-stage, direct team access) |
| **TL;DR** | Near-perfect domain match — Boom is building leasing + underwriting agents for affordable housing renters. Parimala has 8 years of exactly that domain (LIHTC, HUD, HAP, AMI at Entrata) + LeaseI as a direct proof point. Ruby gap is real; AI/agent depth and domain advantage are decisive. |

---

## B) Match with CV

**Domain: Exceptional — Rarest Possible Match**

Boom's mission is "agentic operational layer for residential real estate: leasing, application, underwriting agents" for "low-to-moderate-income renters." Parimala has 8 years at Entrata specifically building affordable housing compliance systems (LIHTC, Section 8/HCV, HUD, HAP, AMI) for this exact population. LeaseI is a leasing compliance AI platform. This combination — domain depth + agentic AI execution — is extremely rare.

| JD Requirement | CV Evidence | Strength |
|----------------|-------------|----------|
| Residential real estate domain | 8 years Entrata (leasing, affordable housing, LIHTC, HUD, HAP, AMI) | **Exceptional** |
| Leasing / application / underwriting agents | LeaseI: 8-agent LangGraph platform for lease compliance + HITL | **Direct proof point** |
| Low-to-moderate income renters empathy | 8 years building LIHTC/HUD/Section 8 compliance for this exact population | **Exceptional** |
| Anthropic/OpenAI APIs + agent patterns | AgentProbe multi-provider routing (Anthropic/OpenAI/Groq/Ollama); LeaseI + Magizhs | Strong |
| Eval suite ownership | AgentProbe: CI-integrated 5-metric LLM-as-judge eval — every commit scored, regressions blocked | **Direct proof point** |
| Guardrails / when to fall back to deterministic logic | LeaseI core rule enforced in code: LLM reasons, deterministic logic or human makes every regulated call | **Direct proof point** |
| HITL / human review queues | LeaseI confidence-gated HITL escalation; AgentProbe eval flags for human review | Strong |
| RAG, multi-step planning, tool use | LeaseI TF-IDF RAG + 8-agent StateGraph; AgentProbe ChromaDB RAG + tool calling | Strong |
| **"Daily Claude Code use is table stakes"** | Currently using Claude Code for all development — literal current tool | **Direct differentiator** |
| Python | Primary language across all roles | Strong |
| React / TypeScript | AgentProbe React dashboard; TypeScript in skills | Medium |
| AWS | Entrata S3/EC2/RDS/Glue (production) | Strong |
| CI/CD + observability | AgentProbe GitHub Actions + per-run metrics dashboard | Strong |
| **Ruby / Grape / Sequel** | Not in stack — PHP is closest analog | **Real gap** |
| Voice AI (LiveKit, Deepgram, ElevenLabs) | Not in stack (listed as "Plus") | Gap |
| Terraform | Not in stack (listed as "Plus") | Gap |

**Ruby gap context:** Ruby is the primary backend language. PHP (Parimala's background) is syntactically similar — both are OOP server-side languages. At a seed-stage company prioritizing AI velocity, Ruby ramp is realistic. The AI agent work will likely be Python/TypeScript-primary. Still a gap to address honestly in the screen.

---

## C) Level and Strategy

**Score: 4.0/5 — Apply** (PropTech threshold is 4.0+)

**"Sell senior without overclaiming" strategy:**

Lead with the domain intersection — this is the single most powerful differentiator:
> "I spent 8 years building affordable housing compliance systems at Entrata — LIHTC, Section 8/HCV, HUD, HAP, AMI — for exactly the low-to-moderate income renter population Boom serves. LeaseI is a leasing compliance AI platform I built from scratch: 8-agent LangGraph with confidence-gated HITL, deterministic compliance gates, and 100% citation correctness. When Boom talks about leasing and underwriting agents for affordable housing tenants, I understand that domain from the inside."

Lead the eval angle second:
> "AgentProbe is my CI-integrated eval platform — 5-metric LLM-as-judge scoring on every commit, regressions blocked before merge. I've owned the eval suite end-to-end. I know the difference between a demo that wows and a system that works at scale."

Address Ruby honestly:
> "My backend primary is Python and PHP — PHP and Ruby are architecturally similar OOP languages and I've ramped on new stacks before. I'd accelerate on Ruby fast, and the AI agent work in Python is where I'd contribute from day one."

**Claude Code differentiator:** The job explicitly says "Daily Claude Code use is table stakes." Parimala uses Claude Code as her active development tool right now — not a talking point, a current fact. Mention it naturally.

**Red-flag Q&A:**
- *"You don't have Ruby experience — how do you handle that?"*
  > "PHP and Ruby are both server-side OOP web frameworks — similar patterns, different syntax. I've shipped production PHP at scale for 8 years; I learn new languages by building in them. I'd pair with your team on Ruby in the first weeks and contribute to the AI stack in Python from day one. The ramp is real but short."

---

## D) Comp and Demand

| Item | Data |
|------|------|
| Disclosed salary | Not disclosed ("directional and adjustable") |
| Stage | Seed → Series A — equity upside meaningful if they execute |
| H-1B | Not stated — must confirm at first screen |
| Location | Austin TX — in-person, relocation required |
| Interview | ~2–3 rounds (early-stage, co-founder involvement) |
| Domain demand | Residential real estate AI is a high-priority vertical; very few engineers have both AI depth and proptech domain |
| Comp score | 3/5 — undisclosed at seed-stage (equity + comp TBD) |

---

## E) Customization Plan

| # | Section | Current | Proposed | Why |
|---|---------|---------|---------|-----|
| 1 | Summary | General AI/agentic framing | Lead with: "8 years in residential real estate compliance (LIHTC, HUD, HAP, AMI) + LeaseI as direct proof of leasing agent architecture with HITL and confidence-gated guardrails" | Domain match is the decisive differentiator |
| 2 | LeaseI bullet | 8-agent HITL | Add: "built for exactly the leasing + compliance workflow Boom is automating — LLM reasons, deterministic logic makes every regulated eligibility call" | Direct product alignment |
| 3 | Entrata | Compliance framing | Add: "8 years serving low-to-moderate income renters across affordable housing programs (LIHTC, Section 8/HCV, HUD, HAP, AMI) — the exact user population Boom cares about" | Empathy + domain depth signal |
| 4 | AgentProbe | Eval engine | Lead with: "owned full eval suite — CI-integrated, every commit scored, regressions blocked before merge" | Direct match to "strong instincts for evals" requirement |
| 5 | Skills | Remove Ruby (not in stack) | Add note on PHP proximity; ensure Python + TypeScript + React prominent | Honest framing of backend profile |

---

## F) Interview Plan

| # | JD Requirement | Story | S | T | A | R | Reflection |
|---|----------------|-------|---|---|---|---|------------|
| 1 | Ship production AI features | LeaseI leasing compliance platform | Affordable housing compliance needed AI for document intelligence + support investigation | Build 8-agent LangGraph with HITL and guardrails | TF-IDF RAG, confidence-gated HITL, deterministic compliance gates | 100% citation correctness, 0 safety violations, end-to-end validation | Compliance gates must be in architecture, not prompts — prompts drift |
| 2 | Own eval suite | AgentProbe eval engine | No CI-integrated eval for LLM agents | Build 5-metric eval that runs on every commit | LLM-as-judge + GitHub Actions | Every commit scored, regressions blocked before merge | LLM-as-judge is slow — cache reference answers early |
| 3 | Guardrails + when to use deterministic logic | LeaseI safety boundary | AI risk of wrong eligibility answer for tenant | Design hard boundary enforced in code | Guardrails at prompt layer AND routing layer | 0 safety boundary violations | Defense in depth: both layers needed |
| 4 | Internal AI productivity | Magizhs + Entrata automation | 80% manual operational workload at Entrata | Build Python/Bash automation pipelines | Replaced Excel workflows across operations | 80% manual workload eliminated | Start with the highest-volume manual task — impact compounds |
| 5 | Partner with product on AI bets | Entrata cross-functional delivery | Compliance, operations, product, finance with conflicting requirements across 120+ sprints | Translate requirements into production architecture | Ran sprint planning across teams, mapped federal housing requirements to modular service design | 120+ sprints, zero compliance violations, 99.5% uptime | Stakeholders remember the reasoning, not the code |

---

## G) Posting Legitimacy

| Signal | Finding | Weight |
|--------|---------|--------|
| Company | Boom — real residential real estate AI startup | Positive |
| Stage | Seed (active hiring for Series A push) | Positive |
| Role coherence | AI Engineer building leasing/underwriting agents = coherent and active market need | Positive |
| Domain | "Low-to-moderate income renters" signals mission-driven company | Positive |
| H-1B | Not stated — to confirm at screen | Neutral |
| Ruby stack | Real production stack for the company's existing product | Positive |
| "Claude Code daily use" | Unusual requirement — signals AI-forward culture | Positive |

**Assessment: High Confidence** — Real company, real mission, coherent engineering requirements.

---

## Machine Summary

```yaml
company: Boom
role: AI Engineer
date: 2026-08-04
score: 4.0
archetype: Applied AI Engineer / PropTech
legitimacy: High Confidence
compensation: not disclosed (seed-stage + equity)
h1b: unconfirmed (must verify at screen)
location: Austin TX (in-person, relocation required)
verdict: apply
key_gap: Ruby/Grape/Sequel not in stack (PHP is closest analog; ramp realistic)
key_strength: 8yr LIHTC/HUD/affordable housing domain + LeaseI leasing compliance platform + AgentProbe eval suite + Claude Code daily use — near-perfect match for exactly what Boom is building
```

---

## Keywords extracted

Residential Real Estate, Leasing Agent, Underwriting, Agentic AI, LLM Orchestration, RAG, HITL, Eval Suite, Confidence Scoring, Guardrails, Deterministic Logic, Python, Ruby, React, TypeScript, AWS, Claude Code, Multi-Agent, Tool Use, Affordable Housing, Low-to-Moderate Income, Seed Stage, Austin TX
