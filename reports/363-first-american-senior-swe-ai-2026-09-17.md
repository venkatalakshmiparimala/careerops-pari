# Evaluation: First American -- Senior Software Engineer (AI Systems)

**Date:** 2026-09-17
**URL:** (pasted directly, no URL provided)
**Archetype:** Agentic / Automation + Applied AI Engineer (Real Estate Title & Settlement)
**Score:** 4.0/5
**Legitimacy:** High Confidence
**PDF:** output/cv-venkata-lakshmi-parimala-pasupuleti-first-american-2026-09-17.pdf (2 pages, est.)
**Location:** Remote (explicitly stated: "Remote Work Welcome")
**Comp:** $129,300 -- $172,300 base

---

## A) Role Summary

| Dimension | Detail |
|-----------|--------|
| Archetype | Agentic / Automation + Applied AI Engineer |
| Domain | Real estate title & settlement -- modernizing First American's core Title & Settlement Platform with production AI systems |
| Function | Build and own production LLM features (0→1 lifecycle), design agentic architectures, implement evaluation frameworks, establish AI-assisted dev practices (Claude Code/Cursor/Copilot), collaborate with product + ML on AI system design |
| Seniority | Senior Software Engineer -- 5+ years required. Large public company (NYSE: FAF, Fortune 500) = formal leveling. Soft concern per interview rejection pattern; NOT a hard block. |
| Location | Remote (explicitly stated) |
| Company | First American Financial Corporation (NYSE: FAF) -- title insurance and real estate settlement, founded 1889, Fortune 500, Forbes Best Companies, 11 consecutive years Fortune 100 Best Companies to Work For |
| TL;DR | Remote Senior SWE role at a Fortune 500 real estate company building production AI / agentic systems. Exceptional technical match (LeaseI = direct 0→1 proof point, AgentProbe = eval framework, Claude Code named in JD). Real estate domain depth from 8yr Entrata. Comp $129K-$172K. H-1B: best situation in today's pipeline (large established public company). Soft concern: Senior at formal-leveling company (documented interview rejection pattern). |

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| 5+ years building production-grade systems | 9yr production (Entrata 7yr + Magizhs + solo projects) | ✅ Exceeds |
| LLM features 0→1: prototype → production → monitoring → iteration | LeaseI: built from scratch, 93.6% precision on 1,240 test cases, CI regression gate, iterated through prompt engineering and eval | ✅ Direct, exactly this lifecycle |
| Agentic systems -- planning/reasoning loops, tool use, memory/context, orchestration | LeaseI: 8-agent LangGraph StateGraph (Triage → Retrieval → Config → Historical → Reasoning → Validation → HITL Escalation) -- planning, tool calls, multi-step execution, conditional routing | ✅ Direct, architecturally complete |
| Evaluation frameworks + quality metrics (accuracy, hallucination rates, task completion, regression) | AgentProbe: 5-metric eval engine (correctness, groundedness, latency, token efficiency, hallucination rate), CI regression gate blocking deploys, LLM-as-judge, multi-trial sampling | ✅ Direct, purpose-built for exactly this |
| AI-assisted dev tools (Cursor, Claude Code, GitHub Copilot) as daily workflow | Claude Code is primary daily development tool -- used throughout LeaseI and AgentProbe builds | ✅ Named directly in JD |
| Help establish team-wide AI dev practices (prompt patterns, context management, quality gates) | AgentProbe: CI quality gates + eval discipline; LeaseI: prompt engineering + context management across 8-agent pipeline | ✅ Built these practices, didn't just use them |
| Backend services and APIs, secure agent ↔ system interaction | FastAPI 15-endpoint backend (AgentProbe); REST APIs; PostgreSQL multi-tenant; RabbitMQ async | ✅ Strong |
| LLM operational concerns: token economics, latency, model routing, caching, cost at scale | AgentProbe: multi-provider routing (Anthropic, OpenAI, Groq), latency metric, token efficiency metric; LeaseI: TF-IDF RAG (deliberate cost choice over vector DB) | ✅ Present |
| Observability strategies supporting continuous delivery | AgentProbe: structured agent tracing, confidence scoring, result tracking; CI integration | ✅ Direct |
| Real estate domain knowledge | 8yr Entrata -- HUD/LIHTC/HCV compliance, leasing, onboarding, eligibility, document management for 100K+ housing units | ✅ Exceptional (8yr, same industry) |
| Mentor and influence engineers | 5+ junior engineers mentored; 300+ peer code reviews; Entrata 7yr technical leadership | ✅ Strong |
| Cloud-native infrastructure, distributed system design | AWS (S3, EC2, RDS, Glue), Docker, Kubernetes, RabbitMQ, microservices redesign (50% scalability improvement) | ✅ Present |

**The technical match is exceptional.** First American's JD reads like a description of LeaseI's build journey: 0→1 LLM deployment, evaluation harness, agentic orchestration, production monitoring, and iterating on real user conversations. "You will define agent behaviors, constraints, and failure modes -- ensuring systems degrade gracefully" = LeaseI's HITL design rule. "Evaluation frameworks and quality metrics for AI systems" = AgentProbe. "AI-assisted development tools (Cursor, Claude Code)" = Claude Code is her primary tool.

**One notable signal:** Claude Code is explicitly named in the JD ("AI-assisted development tools (e.g., Cursor, Claude Code, Copilot)") and appears under "What You'll Do" -- this is an operational requirement, not just a preference. She uses it every day.

---

## C) Level and Strategy

**Soft concern (not hard block).** First American is a Fortune 500 public company with formal leveling. The documented pattern is rejection at Senior level at formal-leveling companies (Juniper Square, AppFolio, Amazon). However, this role has meaningful differences from those cases:

1. **This is an AI transformation team, not core engineering.** First American has been building title insurance software for 130 years. Their "Senior Software Engineer" for AI systems is likely evaluated on "can you build production LLM/agentic systems" -- not on FAANG-style algorithm depth. The bar is probably "5+ years of real engineering + demonstrable AI production experience," not "solve LC hard in 45 minutes."

2. **5+ years required (not 7+).** The JD targets a reasonably experienced engineer, not a staff-level architect. Parimala has 9 years, which puts her solidly in the middle of Senior without being overqualified.

3. **"Build 0→1 AI systems" is not a well-saturated role.** Most Senior engineers in 2026 cannot point to a production agentic platform they built from scratch. LeaseI and AgentProbe are genuinely differentiating here.

**Sell plan:**
- Lead with the 0→1 production AI proof: "I built LeaseI -- an 8-agent LangGraph agentic platform from scratch to production. The eval harness (AgentProbe) came second, because I needed to trust it before shipping prompt changes. That lifecycle -- build, instrument, measure, iterate -- is exactly what this JD describes."
- Claude Code: "It's named in your JD and it's my primary daily tool. I've built production systems with it. I know how to review AI-generated code -- for edge cases, security implications, whether the abstraction actually fits the problem."
- Real estate: "I spent 8 years at Entrata owning compliance-critical systems for the real estate industry. I understand the domain, the data patterns, and the cost of getting it wrong."
- Observability: "AgentProbe traces what was retrieved, what confidence was, where the agent branched -- that's how I can tell a CX team why a response went sideways, which is what your 'observability strategies' requirement is asking for."

---

## D) Comp and Demand

| Source | Range | Notes |
|--------|-------|-------|
| Disclosed | $129,300 -- $172,300 base | Transparent comp range; well above Parimala's target |
| Parimala's target | $80K -- $140K | Floor ($129K) is at top of her stated target; ceiling ($172K) is 23% above |
| Equity / benefits | Stock purchase plan, 401k, full benefits | Standard Fortune 500 package |
| H-1B risk | **Lowest in today's pipeline** | Fortune 500 public company with established H-1B program; standard process, no verification call needed |

**Comp note:** $129K floor hits the very top of her target range. The $172K ceiling is above market for what she's been targeting. This is a clean offer if it clears the level bar.

---

## E) Customization Plan

| # | Section | Current | Change | Why |
|---|---------|---------|--------|-----|
| 1 | Summary | Generic SWE | Open with: "AI systems engineer who builds production LLM and agentic platforms -- I built LeaseI (8-agent LangGraph pipeline, 93.6% precision, CI eval gates) and AgentProbe (evaluation framework with regression gate and LLM-as-judge). Claude Code is my primary daily development tool. 8 years in the real estate industry (Entrata: HUD/LIHTC compliance, leasing, onboarding, scheduling for 100K+ housing units)." | Direct 0→1 proof + domain bridge + Claude Code signal |
| 2 | Skills | Mixed | Lead with: LangGraph, Agentic AI, Multi-Agent Systems, RAG, LLM Evaluation, Observability, Production AI, Claude Code; add Token Economics, Latency Optimization, Model Routing | JD emphasis (operational AI concerns) |
| 3 | LeaseI | AI platform framing | "0→1 production LLM/agentic platform -- 8-agent LangGraph pipeline for real estate compliance: routing, retrieval, tool orchestration, reasoning, HITL escalation. Built the eval harness (AgentProbe) to trust it in production." | Mirrors JD's exact lifecycle language |
| 4 | AgentProbe | Open-source toolkit | "CI-integrated evaluation framework for production AI systems -- 5-metric engine, regression gate blocking quality degradation, LLM-as-judge, multi-trial sampling, multi-provider routing. The quality gates First American's AI systems need." | "Evaluation frameworks and quality metrics" = JD requirement |
| 5 | Entrata | SaaS framing | "8-year ownership of compliance-critical workflows in the real estate industry -- the same domain First American's Title & Settlement Platform serves." | Direct domain bridge |

---

## F) Interview Plan

| # | JD Problem | Story + Answer | Key Insight |
|---|------------|----------------|-------------|
| 1 | Take an LLM feature 0→1 from prototype to production | LeaseI: built from prompt design → 8-agent architecture → eval harness → CI gate → production validation across 1,240 test cases | 0→1 only counts if you define what "production" means before you build it -- I built AgentProbe first to define "good enough" |
| 2 | Design an agentic system -- planning, tool use, failure modes | LeaseI pipeline design: Triage (intent classification) → Retrieval (RAG) → tool calls → Reasoning → Validation → HITL (failure mode: confidence drop = route to human) | Design failure modes first; "graceful degradation" requires knowing what graceful looks like |
| 3 | Build evaluation framework + quality metrics | AgentProbe: 5 metrics, why each metric, CI regression gate, why LLM-as-judge vs. rule-based | A hallucination rate without a threshold is decoration; the threshold is what makes it a gate |
| 4 | AI-assisted development + team practices | Claude Code workflow: describe problem + constraints → generate + tests together → review as colleague PR (edge cases, security, abstraction fit) | AI-generated code has the same failure modes as hand-written code, just produced faster |
| 5 | LLM operational concerns (tokens, latency, cost, routing) | LeaseI TF-IDF choice over vector DB: cheaper, more reliable for compliance retrieval; AgentProbe: latency and token efficiency as tracked metrics; multi-provider routing for cost control | "Pragmatic about models" = know when the right answer is TF-IDF, not a 200ms embedding call |
| 6 | Real estate domain knowledge | Entrata 8yr: I built the systems that handle eligibility, leasing, and compliance for 100K+ housing units -- the same domain First American's Title & Settlement Platform touches from the transaction side | I'm not learning real estate; I'm extending 8 years of production experience into the settlement workflow |

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Company identity | First American Financial Corporation -- NYSE: FAF, Fortune 500, founded 1889, 22K+ employees | Positive |
| Role realism | AI transformation team building 0→1 LLM systems at a legacy real estate company -- genuine need, well-described | Positive |
| Description quality | Specific, architecturally precise, describes real engineering work (0→1 lifecycle, agentic systems, eval harnesses, token economics) -- not boilerplate | Positive |
| Comp transparency | $129,300--$172,300 explicitly disclosed | Positive |
| H-1B / OPT | **Fortune 500 company with 22K+ employees and established HR infrastructure.** Files H-1B petitions annually. Standard sponsorship process, no verification call needed before applying. Lowest H-1B risk in today's pipeline. | ✅ Positive |
| Remote | Explicitly stated: "Remote Work Welcome" | Positive |

---

## Recommendation: Apply

**Score 4.0/5 = at the PropTech/real estate threshold.** The technical match is exceptional (LeaseI, AgentProbe, Claude Code) and the real estate domain depth (8yr Entrata) is directly applicable to First American's title & settlement context.

**Why this is worth applying to despite the Senior formal-leveling concern:**
- This is an AI transformation team at a legacy company, not a Senior SWE role at a tech-native company. The prior rejections (Juniper Square, AppFolio, Amazon) were at companies where "Senior" is deeply benchmarked against software engineering craft. First American's AI engineering bar is about production LLM/agentic experience -- which Parimala has directly and demonstrably.
- "5+ years" (not 7+ or "substantial experience") signals they're building a new capability with experienced engineers, not recruiting from an existing AI engineering pipeline.
- H-1B is not a gate -- this is the cleanest sponsorship situation in the pipeline. Apply without a pre-verification call.
- Comp floor ($129K) hits top of her stated target; ceiling ($172K) exceeds it.
- Remote -- no location logistics.

**Soft risk to communicate proactively:** She has 9 years but the JD targets 5+. Frame this as "9 years of real estate production engineering, with a deliberate shift to production AI systems over the last 18 months." The narrative should be "deep domain expertise + emerging AI capability" not "senior engineer adding AI on the side."

**Action sequence:**
1. Apply directly via First American careers portal (no pre-verification needed)
2. CV framing: LeaseI = 0→1 proof, AgentProbe = eval discipline, Entrata = domain, Claude Code = operational daily tool
3. Lead the founders call (or initial screening) with: "I built LeaseI from scratch -- that's the 0→1 production AI lifecycle your JD describes. I built AgentProbe because I needed an eval harness before I could trust it in production. And I've spent 8 years building systems for the real estate industry."

---

## Keywords Extracted

`LangGraph`, `agentic AI`, `agentic systems`, `production AI`, `LLM evaluation`, `evaluation framework`, `hallucination detection`, `observability`, `agent tracing`, `RAG`, `tool orchestration`, `function calling`, `HITL`, `multi-agent`, `response pipeline`, `Claude Code`, `prompt engineering`, `token economics`, `latency optimization`, `model routing`, `CI/CD`, `regression testing`, `FastAPI`, `Python`, `TypeScript`, `React`, `PostgreSQL`, `AWS`, `Docker`, `Kubernetes`, `real estate`, `title`, `full stack`, `backend services`, `REST APIs`, `cloud-native`

---

## Machine Summary

```yaml
report: 363
company: First American Financial Corporation
role: Senior Software Engineer (AI Systems)
date: 2026-09-17
score: 4.0
archetype: Agentic / Automation + Applied AI Engineer (Real Estate Title & Settlement)
legitimacy: High Confidence
url: null
status: Evaluated
apply_threshold: 4.0 (real estate domain + PropTech boost) -- exactly at threshold
recommendation: apply
condition: null
notes: >
  No pre-verification gate. Fortune 500 = established H-1B infrastructure.
  Soft concern: Senior at formal-leveling company (documented rejection pattern)
  but AI transformation team = different evaluation bar than core engineering.
boosts_applied:
  - +0.2 real estate industry domain (8yr Entrata, same industry as First American)
  - +0.1 H-1B clean (Fortune 500, no verification needed)
gaps:
  - Senior at Fortune 500 formal-leveling company (soft concern, not hard block)
  - Legacy company culture (traditional industry transforming)
strengths:
  - LeaseI = direct 0→1 production AI proof point (JD's exact lifecycle)
  - AgentProbe = evaluation framework JD explicitly requires
  - Claude Code = named in JD, daily tool
  - 8yr Entrata real estate domain
  - H-1B: lowest risk in today's pipeline (Fortune 500)
  - Remote work explicitly stated
  - Comp $129K-$172K: well above target
company_size: 22K+ employees (NYSE: FAF, Fortune 500)
funding: Public company (NYSE: FAF, 130+ years)
comp_base: $129,300-$172,300
pdf: output/cv-venkata-lakshmi-parimala-pasupuleti-first-american-2026-09-17.pdf
```
