# Evaluation: Cohere — Applied AI Engineer, Agentic Workflows

**Date:** 2026-06-10
**URL:** https://jobs.ashbyhq.com/cohere/1fa01a03-9253-4f62-8f10-0fe368b38cb9
**Archetype:** AI Platform / LLMOps
**Score:** 3.7/5
**Legitimacy:** High Confidence
**PDF:** output/cv-cohere-agentic-workflows-2026-06-10.pdf

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | AI Platform / LLMOps |
| Domain | Agentic workflows, LLM-powered agents, RAG, eval frameworks, enterprise customer delivery |
| Function | Build + Customer-Facing |
| Seniority | Senior IC ("3+ years production software, 2+ years LLMs") |
| Remote | Remote-friendly — SF, NYC, Toronto, Montreal offices |
| Comp | Not disclosed ($75/week lunch stipend + benefits listed) |
| TL;DR | Design, build, and deploy production agentic workflows for enterprise customers — own the full lifecycle from prototype to production, define eval standards, debug agent behavior, and mentor engineers. Significant customer-facing and delivery component. |

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| Production Python/TypeScript engineering (3+ yrs) | 8+ years Python at Entrata + AgentProbe FastAPI | ✅ Exceeds |
| LLMs/AI APIs (2+ yrs hands-on) | AgentProbe: Anthropic, OpenAI, Groq, Ollama multi-provider | ✅ Direct proof |
| LangChain/LangGraph/orchestration frameworks | AgentProbe: 3 LangGraph agents, LangChain integration | ✅ Direct proof |
| RAG pipelines + vector databases | AgentProbe: end-to-end RAG + ChromaDB | ✅ Direct proof |
| Evaluation frameworks (beyond trial-and-error) | AgentProbe 5-metric LLM-as-judge engine | ✅ Direct proof |
| ReAct / Plan-and-Execute agent architectures | AgentProbe: Orchestrator (plan) + RAG Tracer + Auto Fix (execute + react) | ✅ Direct proof |
| Frontier model experience (GPT, Claude, Gemini) | AgentProbe: Anthropic + OpenAI multi-provider; Gemini not tested | ✅ Strong |
| Production-grade reliability (observable, auditable) | AgentProbe: trace enrichment, per-run eval scores, anomaly flags | ✅ Strong |
| Customer-facing: translate enterprise needs to specs | No enterprise customer-facing experience | ⚠️ Real gap |
| Mentoring distributed teams | TA at GMU (30+ students); no distributed engineering team experience | ⚠️ Soft gap |
| Travel up to 25% | Manageable | ✅ Fine |
| Shared frameworks for consistent delivery | AgentProbe is an open-source reusable framework | ✅ Strong signal |

**Gaps and mitigations:**
- **Customer-facing** — First responsibility block is enterprise customer engagement: "convert business challenges into well-defined agentic problems." Parimala has no enterprise consulting or solutions engineering background. Mitigate by framing AgentProbe as a tool others use + TA communication experience.
- **H-1B risk** — Cohere US filed 10 LCAs in FY2025, 0 in FY2026 to date. Sharp drop — could reflect hiring freeze, headcount shift to Canada, or just lag. Treat as **high visa risk**. Verify before investing significant application time.
- **Salary undisclosed** — No comp listed. Cohere raised a $500M Series C at $5.5B valuation (2024) but is not yet public. Expect $180-250K for US senior IC.

---

## C) Level and Strategy

**Level detected:** Senior IC. "3+ years production software, 2+ years LLMs" is a lower bar — Parimala exceeds it significantly.

**Sell plan:**
- Technical match is near-perfect — lead with AgentProbe: *"I've built exactly this stack: LangGraph orchestration, RAG end-to-end, 5-metric eval engine, production FastAPI backend. The agentic workflow architecture this role requires is what I've been building."*
- Reframe customer-facing gap: *"I built AgentProbe as an open-source tool for other engineers to use. Thinking about developer UX, documentation, and reliability for external users is the same discipline as customer delivery."*
- **Flag visa risk early** — in recruiter screen, ask directly: "Can you confirm H-1B sponsorship availability? I see Cohere filed 0 LCAs in FY2026 and want to understand the current policy before we invest time on both sides."

**If they downlevel:** Only acceptable if base ≥ $160K. At undisclosed comp, negotiate hard.

---

## D) Comp and Demand

| Source | Range | Notes |
|--------|-------|-------|
| Job posting | Not disclosed | $75/wk lunch + benefits listed |
| Market estimate | $180K–$250K base | Senior AI Engineer at $5.5B-valuation company |
| Cohere funding | $500M Series C (2024) | Strong runway; not yet public |

**Assessment:** Comp unknown — significant uncertainty. Cohere is a well-funded AI lab with strong runway but private. H-1B situation is the bigger concern.

**H-1B:** Cohere US filed 10 LCAs FY2025, 0 FY2026. High risk — verify first.

---

## E) Customization Plan

| # | Section | Current | Proposed change | Why |
|---|---------|---------|-----------------|-----|
| 1 | Summary | AI observability | Lead: *"Applied AI engineer — built production LangGraph agents, RAG pipelines, and eval frameworks; designed AgentProbe as a reusable toolkit for teams building agentic systems"* | Mirrors JD: build agents + shared frameworks |
| 2 | AgentProbe | General | Emphasize: ReAct/Plan-Execute architecture, eval framework, multi-provider, open-source reusable tool | JD pillars: agent design + eval standards + shared frameworks |
| 3 | Competencies | Observability-heavy | Add: Enterprise Agent Delivery, Eval Framework Design, ReAct/Plan-Execute, Multi-Provider LLM | JD's technical vocabulary |
| 4 | Entrata | Production scale | Reframe: *"production-grade software across 120+ sprints; reliability, documentation, and UX for 100K+ users"* | JD: "enterprise-high" bar for production quality |

---

## F) Interview Plan

| # | JD Requirement | Story | S | T | A | R | Reflection |
|---|----------------|-------|---|---|---|---|------------|
| 1 | Build LLM-powered agents (ReAct/Plan-Execute) | AgentProbe Orchestrator + Auto Fix | No systematic way to handle multi-step RAG failures | Build agents that plan, execute, and react to failures | Orchestrator plans run; RAG Tracer executes + observes; Auto Fix reacts to eval failures — ReAct loop in production | Full agentic loop: plan → execute → observe → react, no human intervention per cycle | Plan-and-Execute beats pure ReAct for predictable multi-step tasks; reserve ReAct for recovery paths |
| 2 | Evaluation standards (beyond trial-and-error) | AgentProbe 5-metric eval engine | Ad hoc prompt testing — no systematic regression detection | Design eval framework that catches regressions reliably | 5 metrics with LLM-as-judge; dashboard tracks across runs; Auto Fix triggered at threshold | Systematic: regressions detected, attributed, fixed — not just "it feels better" | Calibration between metrics matters — hallucination score and completeness score can trade off against each other |
| 3 | Build shared frameworks for consistent delivery | AgentProbe open source | Needed eval + observability infrastructure that others could reuse | Ship a framework, not just personal tooling | Public GitHub, documented 15-endpoint API, multi-provider support, README, React dashboard — usable by any team | Open-source tool that works beyond my own projects | Documentation is a product decision, not an afterthought — undocumented frameworks get forked once and abandoned |
| 4 | Debug agent behavior + improve prompts/workflows | AgentProbe Auto Fix | Eval failures with no attribution — manual diagnosis slow | Build diagnostic system with root-cause attribution + automated fix | RAG Tracer attributes failure to retrieval vs generation vs prompt; Auto Fix selects strategy, rewrites, re-evals | Closed loop: failure diagnosed + fixed + re-evaluated without manual intervention | Separating retrieval quality from generation quality is the key diagnostic split |
| 5 | Production-grade reliability: observable, auditable | Entrata + AgentProbe | Production bugs at scale are silent until they compound | Build observable, auditable pipelines from day one | TDD/BDD at Entrata; trace enrichment + eval scoring per run in AgentProbe; zero security incidents at Entrata | 99.5% uptime; every AgentProbe run has a full trace + eval score — auditable by design | Observability is cheaper to build in than to retrofit — production debugging without traces is archaeology |

---

## G) Posting Legitimacy

**Assessment: High Confidence (with H-1B caveat)**

| Signal | Finding | Weight |
|--------|---------|--------|
| Posting freshness | Active on Ashby (posted Jan 2026) | Positive |
| JD specificity | Named architectures (ReAct, Plan-Execute), specific responsibilities | Positive |
| Salary listed | No — comp not disclosed | Neutral |
| Company health | $500M Series C (2024), $5.5B valuation, active product | Positive |
| H-1B | 0 LCAs FY2026 (10 in FY2025) — sharp drop, verify | ⚠️ Caution |
| Remote-friendly | Yes — multiple US office options | Positive |

---

## Keywords Extracted

applied ai engineer, agentic workflows, langchain, langgraph, rag, evaluation frameworks, react architecture, plan-and-execute, production agents, vector databases, frontier models, enterprise delivery, python, cohere, llm evaluation, multi-agent systems

---

## Machine Summary

```yaml
report_num: 040
company: Cohere
role: Applied AI Engineer, Agentic Workflows
date: 2026-06-10
score: 3.7
archetype: AI Platform / LLMOps
legitimacy: High Confidence
location: Remote-friendly — SF, NYC, Toronto, Montreal
comp_range: "undisclosed (est. $180-250K)"
visa_risk: high (0 LCAs filed FY2026 vs 10 in FY2025 — verify before investing time)
key_gaps:
  - H-1B: 0 LCAs FY2026 — high risk, confirm in first recruiter call
  - Customer-facing / enterprise consulting gap (real but not disqualifying)
  - Salary undisclosed
key_strengths:
  - AgentProbe = direct proof of LangGraph, RAG, eval, ReAct/Plan-Execute
  - Open-source framework = "shared frameworks for consistent delivery"
  - 8+ years production Python = exceeds 3yr requirement
  - Multi-provider frontier model experience (Anthropic + OpenAI + Groq)
location_risk: low — remote-friendly, multiple US offices
recommend: apply with caution — technical match is strong; verify H-1B in first call; don't invest heavy prep time until visa confirmed
```
