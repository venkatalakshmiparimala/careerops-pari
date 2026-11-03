# Evaluation: AI Agent Engineer — Seed-Stage AI Startup (via Harrison Clarke)

**Date:** 2026-08-14
**URL:** https://www.clay.com/jobs?ashby_jid=232ab8c1-36d7-4114-91c1-0f9c9e4064bc
**Archetype:** Agentic / Applied AI Engineer
**Score:** 4.5/5
**Legitimacy:** Proceed with Caution (anonymous company; recruiter-sourced)
**PDF:** ❌

---

## A) Role Summary

| Dimension | Details |
|-----------|---------|
| **Archetype** | Agentic AI Engineer — production multi-agent systems for enterprise automation |
| **Team** | Small early engineering team; early hire with architectural ownership |
| **Domain** | Enterprise AI agents (SAP, Salesforce, Workday automation) |
| **Function** | Build: design agents, RAG pipelines, guardrails, inference optimization, cloud deployment |
| **Seniority** | Mid-Senior (no explicit years; "strong experience in production" = 3-5yr effective bar) |
| **Work model** | Palo Alto, Bay Area — likely hybrid/onsite |
| **Comp** | Undisclosed — seed-stage; expect equity-heavy package |
| **Sponsorship** | Unconfirmed — candidate on OPT (3yr runway); H-1B at seed stage is unlikely but possible |
| **TL;DR** | Near-perfect technical match — LangGraph, RAG, guardrails, multi-agent, enterprise integrations all direct. Seed-stage risk + anonymous company + undisclosed comp are the concerns. Candidate has OPT runway. Strong apply. |

---

## B) Match with CV

| JD Requirement | CV Evidence | Match |
|----------------|-------------|-------|
| LLM-powered systems in production | LeaseI (93.6% precision, 1,240 lease PDFs); AgentProbe (CI-integrated eval, live GitHub); Magizhs (production deployment) | ✅ Direct |
| RAG, embeddings, vector databases | LeaseI (TF-IDF RAG, 91% Precision@1, 100% citation correctness); AgentProbe (ChromaDB RAG pipeline); Magizhs (RAG over FAA corpus) | ✅ Direct — 3 production RAG systems |
| LangGraph, LangChain, AutoGen or similar | LeaseI 8-agent StateGraph; AgentProbe 3-agent LangGraph; Magizhs LangGraph stateful graph | ✅ Direct |
| Tool-calling, API orchestration, multi-step reasoning | AgentProbe: multi-provider LLM routing with tool calls; LeaseI: 8-agent conditional routing with tool integration; FastAPI 15-endpoint backend | ✅ |
| Guardrails and reliability mechanisms | LeaseI: confidence scoring, HITL escalation, deterministic safety boundaries enforced in code; code-enforced audit trail | ✅ Direct |
| Planning, execution, verification loops | LeaseI: Triage → Retrieval → Reasoning → Validation → HITL pipeline; Magizhs: parse → plan → retrieve → validate → conditional routing | ✅ |
| Python + cloud deployment | Python 8+ years; AWS (S3, EC2, RDS, Glue); Docker; FastAPI backends deployed | ✅ |
| Enterprise platform integrations (SAP, Salesforce, Workday) | Salesforce integrations at Entrata (data sync, reporting automations, Clay/n8n); SAP/Workday: no experience | ✅ Salesforce / ❌ SAP, Workday |
| Understands how agents fail | LeaseI eval harness (regression gating, LLM-as-judge, pass@k); AgentProbe (5-metric CI-integrated eval blocking failing runs) | ✅ Direct — rare proof point |
| Small fast-moving team comfort | Magizhs: sole architect from requirements to production with no spec doc; AgentProbe: self-directed open-source project | ✅ |

### Gaps

| Gap | Severity | Mitigation |
|-----|----------|------------|
| SAP / Workday integrations | Soft — listed as examples, not requirements | Salesforce integration experience shows enterprise systems pattern |
| Anonymous company | Medium — can't verify culture, funding, or H-1B history | Ask recruiter for company name before signing anything |
| Seed-stage risk | Soft — candidate prioritizing employment over stability currently | Eyes open: seed = equity-heavy, may pivot, small team |
| Comp undisclosed | Soft | Ask recruiter for range upfront |

---

## C) Level and Strategy

**Level:** Mid-Senior IC. No explicit year requirement — "strong experience in production" is the bar. LeaseI + AgentProbe + Magizhs = three production agentic systems. That clears the bar.

**Sell yourself:**
- "I've shipped three production agentic systems end-to-end — LeaseI (8-agent LangGraph with eval harness and guardrails), AgentProbe (3-agent LangGraph with multi-provider routing and CI eval), and Magizhs (LangGraph mission planner). I understand how agents fail because I've built the eval harnesses that catch those failures."
- Lead with the eval harness + guardrails angle — the JD explicitly says "engineers who understand how agents fail." This is the differentiator.

---

## D) Comp and Demand

| Metric | Value |
|--------|-------|
| **Base** | Undisclosed — seed stage; likely $130K–$180K + significant equity |
| **Equity** | Meaningful seed-stage equity expected |
| **Parimala target** | No hard floor — open to right role + sponsorship |
| **H-1B risk** | OPT covers 3 years; seed-stage H-1B sponsorship possible but not guaranteed |

---

## E) Customization Plan

| # | Section | Change | Why |
|---|---------|--------|-----|
| 1 | **Summary** | Lead with: "Agentic AI engineer with three production multi-agent systems — 8-agent LangGraph (LeaseI), 3-agent LangGraph (AgentProbe), LangGraph mission planner (Magizhs). Understands how agents fail: built eval harnesses and guardrails to catch failures before production." | Maps directly to "engineers who understand how agents fail" |
| 2 | **LeaseI** | Surface planning/execution/verification loops: "Triage → Retrieval → Reasoning → Validation → HITL — each stage a verification gate before the next executes." | Maps to "planning, execution, verification loops" requirement |
| 3 | **AgentProbe** | Emphasize inference optimization: "Multi-provider LLM routing (Anthropic, OpenAI, Groq, Ollama) — dynamic selection for cost/latency/quality tradeoffs across inference providers." | Maps to "optimize inference performance and latency" |
| 4 | **Entrata** | Surface Salesforce/enterprise integrations: "Salesforce integrations, reporting automations, and CRM data sync — connecting product data to commercial systems via Clay and n8n." | Maps to enterprise platform integration requirement |
| 5 | **Skills** | Add: "Tool Calling", "API Orchestration", "Memory Systems", "Planning Loops", "Inference Optimization", "Enterprise AI Agents" | ATS coverage for JD terms |

---

## F) Interview Plan

| # | JD Requirement | Story | S | T | A | R | Reflection |
|---|---------------|-------|---|---|---|---|------------|
| 1 | How agents fail + design around failures | **LeaseI eval harness** | Compliance AI silently returning wrong answers is worse than returning no answer — needed to know before production, not after | Build eval harness that validates agents in simulation before every release | 225-query benchmark, pass@k sampling, LLM-as-judge, regression gate blocking deploys | Regressions caught 3+ times before reaching production | Agents fail non-deterministically — you need statistical sampling, not single-run tests |
| 2 | RAG pipelines + grounding | **LeaseI RAG design** | Compliance answers that can't be traced to a source clause are useless in a regulated context | Design RAG that guarantees every answer is cited or explicitly flagged unsupported | Hand-rolled TF-IDF RAG with section-aware chunking, citation enforcement in code, 100% citation correctness on eval set | 91% Precision@1; 0% unsupported-claim rate | The retrieval step is where most RAG systems fail — chunk size and section boundaries matter more than the embedding model |
| 3 | Multi-agent orchestration + conditional routing | **LeaseI 8-agent StateGraph** | Three distinct use cases (document review, staff investigation, tenant self-service) needed different agent logic — one monolithic agent couldn't handle all three correctly | Design a stateful multi-agent system with real conditional routing, not just linear chains | 8-agent LangGraph StateGraph with conditional edges; Triage classifies and routes; specialist agents handle domain-specific reasoning; HITL escalation when confidence too low | 93.6% precision across three enterprise surfaces | State schema design is the foundation — define what the system needs to know at each node, and the routing logic follows |
| 4 | Guardrails for enterprise environments | **LeaseI code-enforced guardrails** | LLM reasoning on regulated compliance decisions creates liability if not bounded correctly | Enforce safety boundaries in code, not prompts — prompts are suggestions; code is guarantees | Core rule in code: LLM extracts and reasons; deterministic logic makes every compliance/financial call; confidence scoring triggers HITL below threshold | 100% compliance on regulated decisions; system auditable end-to-end | Enterprise guardrails need to be deterministic. If your safety boundary relies on the LLM deciding not to cross it, you don't have a safety boundary. |

---

## G) Posting Legitimacy

**Assessment: Proceed with Caution**

| Signal | Finding | Weight |
|--------|---------|--------|
| Recruiter | Harrison Clarke — legitimate tech recruiting firm specializing in AI/ML | Positive |
| Company | Anonymous — "well-funded seed-stage startup" not named | Concerning |
| Funding | "Institutionally backed, top-tier investors" — not verifiable without company name | Neutral |
| JD specificity | Highly specific (SAP, Salesforce, Workday named; LangGraph explicitly listed; failure modes discussed) | Positive |
| Comp | Undisclosed | Neutral |
| Role makes sense | Seed-stage AI startup building enterprise agents = active hiring category in 2026 | Positive |

**Context:** Recruiter-sourced postings for stealth/pre-announcement companies are common at seed stage. Not suspicious — but get the company name before any interview.

---

## Keywords Extracted

AI agent, multi-agent, LangGraph, LangChain, RAG, embeddings, vector database, tool calling, API orchestration, planning loops, guardrails, inference optimization, Python, cloud deployment, enterprise automation, SAP, Salesforce, Workday, production AI, memory systems, agentic systems

---

## Machine Summary

```yaml
report: 211
company: Unnamed seed-stage AI startup (via Harrison Clarke)
role: AI Agent Engineer
score: 4.5
archetype: Agentic / Applied AI Engineer
location: Palo Alto, Bay Area (hybrid/onsite likely; user open to SF relocation)
comp_base: undisclosed (seed-stage; equity-heavy)
sponsorship: unconfirmed; candidate on OPT (3yr runway)
legitimacy: Proceed with Caution (anonymous company; recruiter-sourced)
recommend: strong apply — 4.5; near-perfect technical match; OPT covers immediate need
threshold_used: "4.0+ (Agentic/Applied AI archetype); 4.5 = APPLY"
key_gap: anonymous company (get name before signing); SAP/Workday no experience; comp undisclosed
key_strength: 3 production LangGraph systems; eval harnesses (rare); guardrails; enterprise integrations; Salesforce
action_before_apply: ask recruiter for company name + comp range; confirm OPT acceptable
```
