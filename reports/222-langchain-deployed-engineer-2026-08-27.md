# Evaluation: LangChain — Deployed Engineer

**Date:** 2026-08-27
**URL:** (not provided — pasted as JD text; verify via Ashby jobs portal)
**Archetype:** Forward Deployed Engineer + Agentic / Automation
**Score:** 4.7/5
**Legitimacy:** High Confidence
**PDF:** output/cv-venkata-lakshmi-parimala-pasupuleti-langchain-2026-08-28.pdf

---

## A) Role Summary

| Dimension | Detail |
|-----------|--------|
| Archetype | Forward Deployed Engineer + Agentic / Automation |
| Domain | AI agent platform — LangSmith + LangGraph customer deployment |
| Function | Co-build + advise — production agents with customer engineering teams, pre-sales POCs, post-sale architecture |
| Seniority | Mid-Senior (5+ years); no formal leveling — startup, Series B |
| Company stage | Series B, $125M raised, $1.25B valuation, 280-369 employees, no layoffs, 107 open roles |
| Comp | $165K-$380K base (confirmed LCA filings) + equity |
| TL;DR | Embed with enterprise customers building production AI agents on LangChain/LangGraph/LangSmith -- the exact stack Parimala builds with. |

---

## B) Match with CV

| JD Requirement | CV Match | Quality |
|----------------|----------|---------|
| 5+ years technical (SWE / solutions / founding) | 8+ years Entrata SWE + AI projects | **STRONG** |
| Python | Core stack, 8+ years | **STRONG** |
| JavaScript | Listed in CV; secondary to Python | **MATCH** |
| Agent-based apps -- multi-step, orchestration, failure handling | LeaseI: 8-agent LangGraph StateGraph with conditional routing + HITL + fallback | **STRONG** |
| LangChain / LangGraph specifically | Her actual build stack -- AgentProbe (LangGraph agents) + LeaseI (LangGraph StateGraph) | **EXCEPTIONAL** |
| LLM evaluation + observability | AgentProbe: 5-metric eval engine, LLM-as-judge, CI regression gate -- functionally equivalent to LangSmith's eval layer | **EXCEPTIONAL** |
| Customer-facing: POCs, architecture reviews | No direct solutions/pre-sales experience | **GAP** |
| Run demos + workshops for developer audiences | GMU: delivered technical workshops to 600+ students | **PARTIAL -- usable framing** |
| Cloud (AWS/GCP/Azure) | AWS primary (S3, EC2, RDS, Glue) | **MATCH** |
| Containers + Kubernetes | Docker yes; Kubernetes not listed | **PARTIAL** |
| Shipped + operated production software | Entrata 8yr: 100K+ MAU, zero compliance violations | **STRONG** |

### Key gaps and mitigations

| Gap | Blocker? | Mitigation |
|-----|----------|-----------|
| Customer-facing / pre-sales | No -- FDE roles hire SWEs who can talk to customers, not salespeople who code | Frame GMU technical workshops (600+ students) + Entrata cross-team delivery as evidence of technical communication |
| No enterprise AI deployment (projects self-built) | No -- JD values "beyond simple API calls, orchestration, failure handling" -- LeaseI + AgentProbe demonstrate this | Lead with architecture decisions, not deployment context |
| Kubernetes | Minor ("basic concepts" nice-to-have) | "Docker containerization; familiar with K8s concepts" |

---

## C) Level and Strategy

No hard block. LangChain is a startup -- no formal leveling. "5+ years" minimum. Parimala has 8+.

**Why this role is exceptional for this profile:**

AgentProbe is a LangSmith-equivalent evaluation framework -- she built what LangSmith does. For a Deployed Engineer helping customers get value from LangSmith, having built an alternative from first principles signals depth that no certification can match.

LeaseI runs on LangGraph -- LangChain's own framework. The 8-agent StateGraph with conditional routing, HITL escalation, and failure handling IS the "beyond simple API calls" the JD describes. The interview answer to "show me a production agent architecture" is already built.

**"Sell the FDE angle" plan:**
- Frame Entrata as "8 years shipping systems real teams depended on -- I know what happens when a pipeline fails at 2am for 100K users."
- Frame GMU teaching as "I explain complex AI systems to non-expert audiences -- 600 students across multiple sections."
- Frame AgentProbe as: "I built what your product does. I know exactly where customers hit walls, because I hit them building it."
- "Customer Zero" mentality is natural: she already uses LangGraph and LangChain -- she's a power user of the ecosystem.

---

## D) Comp and Demand

| Data point | Value | Source |
|------------|-------|--------|
| Deployed Engineer base (NYC/Seattle/Boston) | $165K-$380K | LCA filings / RFS data |
| Deployed Engineer base (Denver/Phoenix) | $155K-$360K | LCA filings |
| LangChain median comp (all roles) | ~$208K | Recruiting From Scratch 2026 |
| H-1B LCA filings (2025) | 6 filed, 6 approved (100%) | H1BGrader |
| Company stage | Series B, $125M raised, $1.25B valuation | Crunchbase / Tracxn |
| Headcount growth | 50 -> 280-369 employees in 18 months | Crustdata |
| Layoffs | None reported | Multiple sources |

Comp score: 5.0/5 -- $165K-$380K base at Series B with equity. Floor alone exceeds every other role evaluated today.

H-1B: Confirmed sponsor, 100% approval on 6 filings. Small number reflects startup stage -- CONFIRM with recruiter on first contact. Growing headcount suggests more filings ahead.

---

## E) Customization Plan

| # | Section | Change | Why |
|---|---------|--------|-----|
| 1 | Summary | Lead with LangGraph + LangSmith angle: "I build production agents on LangGraph and built an evaluation framework equivalent to LangSmith" | Matches the FDE job description in sentence 1 |
| 2 | AgentProbe | Reframe as "LangSmith-equivalent: observability, correctness, grounding, latency, hallucination detection -- CI-integrated, 1,240+ test cases" | Mirrors LangChain's own product language |
| 3 | LeaseI | Lead with "8-agent LangGraph production system" and "failure handling: HITL escalation when confidence too low" | Directly answers "beyond simple API calls, including failure handling" |
| 4 | GMU TA | "Delivered technical demos and workshops to 600+ developers" framing | Mirrors "run technical demos, trainings, and workshops for developer audiences" |
| 5 | Skills | Surface "LangChain, LangGraph, LLM Evaluation, Agent Observability" as headline cluster | Keyword match to LangChain's own products |

---

## F) Interview Plan

| # | JD Requirement | STAR+R Story | Key punch line |
|---|---------------|-------------|----------------|
| 1 | Multi-step orchestration + failure handling | LeaseI 8-agent LangGraph | HITL escalation when confidence too low; traces false-ineligibility to misconfigured setting |
| 2 | LLM evaluation / observability | AgentProbe | "I built what LangSmith does -- 5-metric eval, CI gate, LLM-as-judge scoring, 1,240+ test cases" |
| 3 | Explain tradeoffs to developer audiences | GMU 600+ workshops | Adapted explanations to skill level in real time across multiple sections |
| 4 | Take responsibility for outcomes | Entrata HUD pipeline | Zero compliance violations across 7 years -- owned validation, rollback, and post-release debugging |
| 5 | Bias toward action | Magizhs AI internship | Parsed FAA Part 107 into RAG corpus and built flight-plan validation from scratch -- no existing playbook |
| 6 | Operate production software | Entrata RabbitMQ async | Retry logic + idempotency guarantees eliminating double-processing failures; owned through production incidents |

**Recommended POC to demo:** AgentProbe -- walk through how a customer plugs their agent into the eval framework, runs the CI regression gate, and uses LLM-as-judge scoring to catch grounding failures. This is literally the LangSmith pitch, delivered from first-principles knowledge.

**Red-flag questions:**
- "No solutions engineering experience?" -> "Technical communication is the skill -- 600 students at GMU, cross-functional delivery at Entrata across product, compliance, and operations. The customer context is the application."
- "Projects aren't enterprise-deployed?" -> "LeaseI and AgentProbe have production engineering contracts: Pydantic validation, HITL escalation, CI regression gate, Docker packaging, FastAPI endpoints. Production discipline is there. The difference is access to enterprise infrastructure, not engineering rigor."

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Company legitimacy | LangChain -- $125M Series B, $1.25B valuation, confirmed entity | Positive |
| JD specificity | Named products (LangSmith, LangGraph), named customers (Klarna, Coinbase, Lyft, Nvidia), specific responsibilities | Positive |
| Growth | 50 -> 280-369 employees in 18 months, 107 open roles, no layoffs | Positive |
| H-1B | 6 filed, 6 approved (100%) in 2025 | Positive |
| Salary | $165K-$380K confirmed via LCA filings | Positive |
| Scan history | Prior LangChain roles in history (2026-06); Deployed Engineer appears fresh | Positive |
| Revenue | $16M ARR -- real business | Positive |

---

## Keywords extracted

LangChain, LangGraph, LangSmith, deployed engineer, production AI agents, agentic workflows, LLM evaluation, observability, multi-step orchestration, failure handling, HITL, Python, JavaScript, AWS, Docker, Kubernetes, pre-sales, POC, architecture review, Series B, customer engineering

---

## Machine Summary

```yaml
company: LangChain
role: Deployed Engineer
date: 2026-08-27
score: 4.7
archetype: Forward Deployed Engineer + Agentic / Automation
legitimacy: High Confidence
recommend: apply_immediately
comp_low: 165000
comp_high: 380000
location: US (multiple cities + likely remote-eligible)
h1b_sponsor: confirmed (verify with recruiter -- 6 filings in 2025)
hard_block: NO
key_gap: customer-facing / pre-sales experience
key_strength: LangGraph + LangChain build stack + AgentProbe = LangSmith-equivalent = exceptional match
priority: highest_in_session
```
