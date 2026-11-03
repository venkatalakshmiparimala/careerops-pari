# Evaluation: LangChain — Fullstack Software Engineer, Applied AI

**Date:** 2026-06-11
**URL:** https://jobs.ashbyhq.com/langchain/c75915ba-a32b-4e17-873d-19b47564170d
**Archetype:** AI Platform / LLMOps — Applied AI Engineering
**Score:** 4.1/5
**Legitimacy:** High Confidence
**PDF:** output/cv-langchain-fullstack-swe-applied-ai-2026-06-11.pdf

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | AI Platform — Applied AI Engineering (agent development, open-source, full-stack) |
| Domain | Build production AI agents for LangChain's internal GTM/engineering workflows + ship open-source reference agents |
| Function | Build (end-to-end agent development, full-stack deployment) |
| Seniority | Mid-Senior IC (no explicit level — responsibilities suggest 5+ years) |
| Remote | SF or NYC office preferred (5 days/week within commuting distance); hybrid possible for candidates outside commuting distance — Virginia qualifies |
| Comp | $165,000–$190,000 base + equity + benefits |
| TL;DR | Build and deploy production LangChain/LangGraph agents for internal automation and open-source reference implementations. Own agent problem spaces end-to-end: design → deploy → iterate. Full-stack: Python + JavaScript/React + FastAPI. |

---

## ⚠️ LOCATION FLAG

Role is listed as **San Francisco or New York** — 5 days/week onsite for candidates within commuting distance. Virginia is outside commuting distance — job description explicitly notes hybrid arrangements are possible for such candidates. Confirm exact hybrid policy (frequency of onsite visits) in recruiter screen before applying.

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| LangChain / LangGraph expertise | AgentProbe: 3-agent LangGraph system (Orchestrator, RAG Tracer, Auto Fix) | ✅ Direct proof |
| Build and deploy production AI agents | AgentProbe: production FastAPI backend + LangGraph agent orchestration | ✅ Direct proof |
| Open-source experience | AgentProbe is fully open-source, public GitHub | ✅ Direct proof |
| Python production | 8+ years Python at Entrata + AgentProbe | ✅ Exceeds |
| JavaScript / React (full-stack) | AgentProbe: React dashboard; Entrata: 20+ full-stack modules (JS + Python) | ✅ Strong |
| Agent architecture: plan-execute-react loop | AgentProbe: LangGraph plan-execute-react with custom tool calls | ✅ Direct proof |
| RAG + vector search | AgentProbe: ChromaDB, embedding pipeline, retrieval quality scoring | ✅ Direct proof |
| Multi-provider LLM routing | AgentProbe: Anthropic, OpenAI, Groq, Ollama dynamic routing | ✅ Direct proof |
| Production deployment + CI/CD | AgentProbe: GitHub Actions CI/CD + Docker | ✅ Strong |
| "Ship agents for internal GTM / engineering workflows" | Applied AI automation use case — LangGraph patterns transfer directly | ✅ Adjacent |
| H-1B | LangChain is well-funded AI startup — likely sponsors; verify in screen | ⚠️ Confirm |
| Location | SF/NYC office — hybrid possible for Virginia-based candidates | ⚠️ Confirm hybrid terms |

**Gaps and mitigations:**
- **Location** — Not a hard block. Virginia is outside commuting distance, so hybrid arrangement is explicitly noted as eligible. Must clarify frequency of required onsite visits in first call.
- **H-1B** — LangChain is a venture-backed AI company (Series B stage). Likely sponsors but not confirmed public company. Verify in recruiter screen.
- **Node.js / JavaScript depth** — CV is Python-heavy. React frontend exists (AgentProbe) and Entrata full-stack (JS + Python), but not JS/Node-first. Mitigate: the role's core is agent development in Python/LangGraph; React is secondary.

---

## C) Level and Strategy

**Level detected:** Mid-Senior IC. The JD doesn't specify "Senior" — responsibilities suggest 3–6 year range but AgentProbe ownership and 8+ years place Parimala above the bar.

**Sell plan:**
- Lead with AgentProbe as the literal product demo: *"I built production LangGraph agents — Orchestrator, RAG Tracer, Auto Fix — with plan-execute-react loops, tool calls, and multi-provider routing. That's exactly what this team builds. I did it as an open-source project that other engineers use."*
- Open-source = cultural fit: *"AgentProbe is open-source. I understand what it takes to ship tooling that others adopt — documentation, clean APIs, reproducible local setup."*
- Applied AI automation: *"LangChain's Applied AI team builds internal agents for GTM and engineering. I've done exactly this — automated decision support workflows at Entrata and built the full eval + orchestration stack from scratch."*
- Comp target: Push toward $180K+ — LangChain/LangGraph depth + open-source ownership exceeds the bar clearly.

**H-1B:** LangChain is a well-funded startup. They hire globally and sponsor H-1Bs — but as a smaller company vs. a public company like Upstart, the certainty is lower. Verify in first call.

---

## D) Comp and Demand

| Source | Range | Notes |
|--------|-------|-------|
| Job posting | $165K–$190K base | Disclosed |
| Equity | Meaningful equity (startup) | Series B — significant potential upside |
| Market | $160K–$220K for Sr SWE at AI platform companies | Competitive |

**Assessment:** $165–190K is strong for a full-stack SWE at an AI startup. Equity at LangChain (the framework that powers the majority of production LLM apps) has real upside. Bottom of range ($165K) still beats most roles in the pipeline; top ($190K) is excellent.

---

## E) Customization Plan

| # | Section | Current | Proposed change | Why |
|---|---------|---------|-----------------|-----|
| 1 | Summary | Varies | Lead: *"Fullstack AI engineer who built AgentProbe — open-source LangGraph agent platform with plan-execute-react orchestration, RAG pipeline, multi-provider routing, and production React/FastAPI stack. Built agents. Shipped open-source tooling other engineers adopt."* | JD: LangChain/LangGraph + open-source + agent dev |
| 2 | AgentProbe | Varies | Lead with: LangGraph architecture (3-agent system), open-source, plan-execute-react loop, tool calls, multi-provider routing, React dashboard, FastAPI | JD vocabulary: agents, tool calls, open-source, full-stack |
| 3 | Competencies | Varies | LangChain / LangGraph, Agent Development & Orchestration, Open-Source Engineering, Full-Stack (React + FastAPI), RAG + Vector Search, Multi-Provider LLM Routing, Production AI Systems | Direct JD vocabulary |
| 4 | Entrata | General | Elevate: 20+ full-stack modules (JS/Python/PostgreSQL), Docker containerization, 120+ Agile sprints — full-stack delivery at scale | JD: full-stack + production delivery |

---

## F) Interview Plan

| # | JD Requirement | Story | Key Points |
|---|----------------|-------|------------|
| 1 | Build production LangGraph agents | AgentProbe: Orchestrator + RAG Tracer + Auto Fix | Why LangGraph over plain LangChain; plan-execute-react loop design; how to handle agent failures gracefully |
| 2 | Open-source tooling adopted by others | AgentProbe: public GitHub, local-first setup, clean API design | What makes tooling adoptable: reproducibility, docs, zero-dependency local mode |
| 3 | Full-stack: Python + React | AgentProbe: 15-endpoint FastAPI + React dashboard; Entrata: 20+ JS/Python modules | Frontend/backend integration patterns; observability dashboard design |
| 4 | Applied AI automation for internal workflows | LangGraph agent patterns (plan-execute-react) applied to GTM/engineering automation | "The pattern is the same whether the domain is LLM testing or GTM automation — state machine, tool selection, retry logic" |
| 5 | RAG + retrieval | AgentProbe: ChromaDB, embedding pipeline, retrieval scoring | Chunking strategy, embedding model selection, retrieval quality evaluation |

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Salary disclosed | $165K–$190K | Positive |
| Company health | LangChain: Series B+, the dominant LLM orchestration framework, active hiring | Positive |
| JD specificity | Named frameworks, specific workflow (internal agents + open-source); real team mission | Positive |
| Ashby platform | More stable than Greenhouse — lower rate of ghost postings | Positive |
| H-1B | Venture-backed startup — likely sponsors; verify | ⚠️ Confirm |
| Location | SF/NYC office — hybrid possible for remote candidates | ⚠️ Confirm hybrid terms |

---

## Keywords Extracted

fullstack software engineer, applied ai, langchain, langgraph, agent development, open source, python, javascript, react, fastapi, rag, vector search, ai agents, production deployment, llm orchestration, langchain jobs

---

## Machine Summary

```yaml
report_num: 048
company: LangChain
role: Fullstack Software Engineer, Applied AI
date: 2026-06-11
score: 4.1
archetype: AI Platform / LLMOps
legitimacy: High Confidence
location: SF or NYC office (hybrid possible for Virginia-based candidates — confirm terms)
comp_range: "$165K–$190K base + startup equity"
visa_risk: medium (venture-backed startup — likely H-1B sponsor, verify)
key_gaps:
  - Location: SF/NYC office preferred (hybrid eligible for Virginia — must confirm onsite frequency)
  - H-1B: verify in recruiter screen
  - JavaScript depth: Python-primary CV; React exists but not JS-first
key_strengths:
  - AgentProbe = direct proof of LangChain, LangGraph, open-source agent development
  - Plan-execute-react loop + tool calls = exact JD requirement
  - Open-source = LangChain's DNA; cultural fit is real
  - Python 8+ years + React dashboard + Entrata full-stack
  - Comp $165-190K + startup equity upside
location_risk: medium — hybrid possible from Virginia, but onsite frequency unclear
recommend: strong apply if hybrid confirmed — best SWE-role tech match in pipeline; LangChain literally runs on what AgentProbe was built with
```
