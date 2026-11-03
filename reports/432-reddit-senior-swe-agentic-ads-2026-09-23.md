# Evaluation: Reddit — Senior Software Engineer, Agentic Ads Experience

**Date:** 2026-09-23
**URL:** (pasted JD — reddit.com/careers)
**Archetype:** Agentic / Automation + AI Platform / LLMOps (hybrid — primary archetypes)
**Score:** 4.7/5
**Legitimacy:** High Confidence
**PDF:** ✅ output/cv-venkata-lakshmi-parimala-pasupuleti-reddit-2026-09-23.pdf

---

## A) Role Summary

| Dimension | Details |
|-----------|---------|
| **Archetype** | Agentic / Automation + AI Platform (both PRIMARY archetypes) |
| **Domain** | Ads — campaign assistants, creative generation, audience discovery, conversational analytics |
| **Function** | Design + ship advertiser-facing AI features end-to-end: framing → prototype → GA |
| **Seniority** | Senior Software Engineer |
| **Work model** | Remote (mentions "remote environment" in collaboration; Reddit is remote-friendly) |
| **Comp** | $190,800–$267,100 USD + equity (RSUs) |
| **Sponsorship** | Reddit is a public company — established H-1B sponsor; verify in screening |
| **TL;DR** | Campaign assistant + agentic AI features for Reddit Ads. Every hard requirement maps directly to AgentProbe or LeaseI. Ads domain is listed as a *bonus*, not required. **Score: 4.7/5 — strong APPLY.** |

---

## B) Match with CV

| JD Requirement | CV Evidence | Match |
|---|---|---|
| 5+ years SWE, shipping production systems | 8+ years at Entrata (100K+ MAU, 99.5% uptime) | ✅ Strong |
| Generative AI applications: structured outputs, function/tool calling, prompt design, RAG, model routing, failure modes | AgentProbe: structured output validation, tool calling, LLM Router (model routing), multi-provider; LeaseI: RAG, structured HITL escalation, hallucination guardrails | ✅ Direct match |
| Agentic systems design: workflows, skills, retrieval, agent loops, HITL | LeaseI: 8-agent LangGraph StateGraph with real conditional edges, confidence-based HITL escalation, tool/action boundaries; AgentProbe: 3 LangGraph agents with orchestration | ✅ Strongest signal |
| Reliability + guardrails: retries, cost controls, tracing, evals, HITL | AgentProbe: CI-integrated regression harness, LLM-as-judge, latency/token-efficiency metrics (cost controls); LeaseI: every compliance call human-reviewed or deterministic | ✅ Direct match |
| Offline + online evals, A/B tests, model + product metrics | AgentProbe: pass@k harness (offline eval), 5-metric engine, regression gate; LeaseI eval'd across 1,240 PDFs | ✅ AgentProbe IS this |
| Safety + trust: data isolation, permissioning, auditability, policy compliance | LeaseI: deterministic audit trail for every decision; eligibility calls never resolved by LLM; PHI compliance at Entrata (100%); HIPAA-compliant RBAC in AI on FHIR | ✅ |
| Systems fundamentals: APIs, distributed systems, queues, idempotency, observability | RabbitMQ async + idempotency at Entrata (production, 7yr owned); FastAPI 15-endpoint; Agent Observability + Tracing in AgentProbe | ✅ |
| Python production | 8+ years Python | ✅ |
| **Bonus: AI where mistakes are expensive** | LeaseI: core design rule "LLM reasons, human decides every regulated call" — compliance/eligibility stakes, enforced in code | ✅ Perfect example |
| **Bonus: Ads / marketing tech** | No ads experience — this is a gap | ⚠️ Gap (bonus only) |
| Go, Rust (mentioned) | Not in her stack | ⚠️ Minor — Python acceptable |

**Gap analysis:**
1. Ads / marketing technology — listed as *bonus*, not required. Zero weight on required qualification gate.
2. Go/Rust — Python explicitly listed as sufficient in required qualifications.

No hard gaps on required qualifications.

---

## C) Level and Strategy

| Dimension | Finding |
|-----------|---------|
| Title | Senior Software Engineer — no penalty |
| Reddit leveling | Senior at Reddit is a strong IC role; less formal leveling than FAANG |
| Her fit | 8yr SWE depth + 2yr hands-on agentic AI. AgentProbe + LeaseI are production-grade systems with evals, not toy demos. |
| Strategy | Lead with eval infrastructure as the differentiator: "I didn't just use LLMs — I built the harness that tells you when they're working and when they're not." |

---

## D) Comp and Demand

| Metric | Data |
|--------|------|
| JD range | $190,800–$267,100 + RSUs |
| Score | **5.0/5** — top of market, well above her $120K ceiling |
| Equity | RSUs — meaningful at Reddit's scale |
| Total comp at midpoint | ~$229K base + RSUs = strong offer |

---

## E) Customization Plan

| # | Section | Proposed change |
|---|---------|-----------------|
| 1 | Summary | Lead: "Agentic AI systems engineer who builds evals alongside agents — AgentProbe (eval infrastructure) + LeaseI (8-agent LangGraph system for regulated decisions) — with 8yr production SWE depth in distributed systems, idempotency, and observability." |
| 2 | AgentProbe | Lead bullet — front-load: eval infrastructure, offline + online eval loops, cost controls, model routing. This IS their measurement requirement. |
| 3 | LeaseI | Frame as "AI system where mistakes are expensive" — deterministic audit, HITL, policy compliance enforced in code. Maps directly to their Bonus requirement AND their Safety/Trust section. |
| 4 | Entrata | Lead with: RabbitMQ idempotency (systems fundamentals), 8yr production ownership, FastAPI APIs |
| 5 | Summary tagline | "AgentProbe: github.com/venkatalakshmiparimala/AgentProbe" — case study URL in summary, visible to recruiter in 6-second scan |

---

## F) Interview Plan

| # | JD Requirement | Story |
|---|----------------|-------|
| 1 | Agentic systems design — when to use agent vs. workflow vs. single LLM call | LeaseI design decision: 8 agents vs. single chain. The Triage agent routes to Config vs. Historical vs. StructuredData based on ticket type — not every ticket needs all agents. Conditional routing = cost control. |
| 2 | Reliability + guardrails for LLMs | LeaseI safety boundary: tenant eligibility questions NEVER resolved by AI. Enforced in code via routing condition, not just a prompt. "I don't trust prompts for safety boundaries — I trust code." |
| 3 | Evals: defining quality bar for agentic system | AgentProbe pass@k harness — 5-metric engine, golden datasets, regression gate that blocks CI if quality drops. Evaluated LeaseI across 1,240 lease PDFs: 93.6% precision, 87.9% F1. |
| 4 | Cost controls + model routing | AgentProbe LLM Router — route OpenAI/Anthropic/Groq/Ollama dynamically. Latency + token efficiency are first-class eval metrics, not afterthoughts. Local Ollama for dev = zero cost. |
| 5 | AI where mistakes are expensive | LeaseI: a wrong eligibility decision affects a real person's housing. Core design rule enforced in code: LLM extracts + reasons; human or deterministic logic makes every final regulated call. Pass@3 88.3% — even at high accuracy, HITL escalation gates the cases below threshold. |
| 6 | Systems fundamentals: idempotency + queues | Entrata RabbitMQ system — designed retry logic and idempotency guarantees that eliminated double-processing failures for annual gross-rent updates. Owned through production incidents. |
| 7 | Cross-functional collaboration + design docs | 120+ Agile sprints across product, engineering, compliance teams at Entrata; wrote technical design docs for HUD pipeline migrations reviewed by cross-team stakeholders. |

**Recommended case study to lead with:** AgentProbe + LeaseI together — "I built the agent and the eval harness for it simultaneously. That feedback loop is what let me catch precision drops before they reached users."

**Red-flag questions:**
- "You don't have ads experience" → "The hard requirements are all about building reliable agentic systems with evals — that's AgentProbe and LeaseI. Ads is a domain I'll ramp on fast; the AI primitives are the same whether the agent is managing campaign copy or compliance tickets."
- "Your LLM work is project-based, not a company" → "Magizhs was production (real client, deployed system). LeaseI is evaluated on 1,240 real documents with a pass@k harness and CI regression gate. These aren't demos — they're systems with test coverage."

---

## G) Posting Legitimacy

| Signal | Finding | Weight |
|--------|---------|--------|
| Company | Reddit — public company, ~$1B+ revenue run rate, known employer | Positive |
| Salary disclosed | $190,800–$267,100 + equity | Positive |
| Team specificity | "Agentic Ads Experience" — named team with specific roadmap | Positive |
| Tech specificity | LLMs, RAG, evals, HITL, guardrails, A/B tests — real AI team | Positive |
| Remote-friendly | "remote environment" in collaboration req | Positive |
| H-1B sponsorship | Reddit confirmed sponsor (large public tech company); verify in screening | Likely positive |
| Posting end date | Not stated — active listing | Neutral |

**Assessment: High Confidence** — Real opening on a real team building real products.

---

## H) Draft Application Answers (score 4.7 ≥ 4.5)

**"Why Reddit / this team?"**
> "The Agentic Ads Experience team is building exactly what I've been building on my own — agentic systems where reliability and trust matter more than impressive demos. LeaseI taught me that an agent that auto-resolves the wrong decision is worse than no agent at all. Building campaign assistants that advertisers actually trust requires the same discipline: clear action boundaries, HITL where stakes are high, evals that catch quality drops before they reach users. I want to bring that to a product with real revenue impact at Reddit's scale."

**"Describe your experience with agentic systems"**
> "LeaseI is an 8-agent LangGraph system for compliance investigation — Triage routes to specialized sub-agents (Config, Historical Incident, StructuredData), each producing evidence-backed hypotheses. HITL escalates when confidence is below threshold. The core rule enforced in code: LLM reasons, human or deterministic logic decides every regulated call. AgentProbe is the eval infrastructure I built alongside it — 5-metric engine, pass@k harness, CI regression gate. I ran LeaseI through 1,240 lease PDFs: 93.6% precision, 87.9% F1."

---

## Verdict

**4.7/5 — APPLY NOW.**

This is the strongest AI engineering match today. Every hard requirement is covered by AgentProbe or LeaseI:
- Agentic systems ✅ (LeaseI 8-agent LangGraph)
- Evals + measurement ✅ (AgentProbe — literally an eval infrastructure)
- Reliability + guardrails ✅ (HITL, confidence scoring, structured outputs)
- Safety + auditability ✅ (deterministic compliance decisions, PHI compliance)
- Systems fundamentals ✅ (RabbitMQ idempotency, FastAPI, distributed systems)

The only "gap" (ads domain) is explicitly listed as a bonus. Lead with the eval infrastructure angle — it's rare and directly named in the JD.

---

## Keywords extracted

agentic systems, LLM, generative AI, RAG, structured outputs, function calling, tool calling, model routing, guardrails, HITL, human-in-the-loop, offline evaluation, online evaluation, A/B testing, evals, observability, tracing, cost controls, campaign assistant, advertiser, data isolation, auditability, policy compliance, LangChain, LangGraph, agent loop, idempotency, distributed systems, Python, FastAPI, production AI

## Machine Summary
```yaml
company: Reddit
role: Senior Software Engineer, Agentic Ads Experience
score: 4.7
archetype: Agentic/Automation + AI Platform/LLMOps (both primary)
level: Senior
comp_range: "$190,800-$267,100"
location: Remote
sponsorship: Likely confirmed (public tech company — verify in screening)
apply: YES — strong apply
top_proof_points:
  - AgentProbe (eval infrastructure = their measurement requirement)
  - LeaseI 8-agent LangGraph (agentic systems = their core ask)
  - RabbitMQ idempotency + Entrata production depth (systems fundamentals)
  - LeaseI HITL + deterministic compliance (safety/trust + "AI where mistakes expensive" bonus)
key_gap:
  - Ads/marketing domain (bonus only — not required)
```
