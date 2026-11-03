# Evaluation: Ramp — Applied AI Engineer

**Date:** 2026-06-05
**URL:** https://jobs.ashbyhq.com/ramp/d204e136-2749-42de-82b4-88a0dd352090
**Archetype:** Agentic / Automation + Software Engineer (AI-focused)
**Score:** 4.0/5
**Legitimacy:** High Confidence
**PDF:** pending

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | Agentic / Automation + Software Engineer (AI-focused) |
| Domain | Full-stack AI, LLM agents, RAG, structured extraction, LLM inference infrastructure |
| Function | Build |
| Seniority | All levels — flexible (posted as "Applied AI Engineer | All Levels") |
| Remote | Hybrid — New York, NY or San Francisco, CA (WFH stipend + relocation support listed) |
| Comp | Not disclosed in JD; Levels.fyi median SWE total comp $335K–$340K (NYC/US) |
| TL;DR | Ship full-stack AI projects end to end at Ramp — agents, RAG pipelines, structured extraction, fine-tuning, and LLM inference infrastructure for a fintech platform serving 25K+ businesses. |

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| Full-stack proficiency (web + backend + cloud) | Python, TypeScript, JavaScript, FastAPI, PostgreSQL, AWS, Docker — 8+ years | ✅ Strong |
| Track record on production LLM projects | AgentProbe: 15-endpoint FastAPI + LangGraph + LLM Router, deployed on Azure | ✅ Direct proof |
| AI agents | AgentProbe: 3 LangGraph agents (Orchestrator, RAG Tracer, Auto Fix) | ✅ Direct proof |
| RAG pipelines | AgentProbe: ChromaDB RAG pipeline with retrieval quality scoring | ✅ Direct proof |
| Ship end-to-end AI projects | AgentProbe built solo end-to-end: data → agents → eval → API → dashboard | ✅ Direct proof |
| Backend systems supporting AI-driven products | FastAPI async backend, 1M+ records at Entrata, 99.5% uptime | ✅ Strong |
| Structured extraction | AI on FHIR: NLP → structured FHIR API calls (intent → schema) | ✅ Adjacent |
| LLM inference infrastructure | AgentProbe LLM Router (dynamic routing: Ollama/OpenAI/Anthropic/Groq) | ✅ Adjacent |
| Fine-tuning models | Not in CV | ⚠️ Gap |
| Fintech domain knowledge | Entrata is proptech — no fintech/accounting/expense management experience | ⚠️ Domain gap |

**Gaps and mitigations:**
- **Fine-tuning** — Soft: not in CV. Hugging Face + PyTorch + scikit-learn are listed — signals ML fundamentals. Mitigate by noting familiarity with model fine-tuning concepts via MS coursework.
- **Fintech domain** — Soft: Ramp cares far more about LLM/AI engineering skills than fintech background for this role. The JD focuses on AI infrastructure, not domain expertise. Entrata's accounting automation modules (billing, payment workflows) are a reasonable bridge.

---

## C) Level and Strategy

**Level detected:** All levels — Ramp explicitly posted this role as "All Levels." Parimala at 8+ years is a strong mid-senior candidate.

**Sell plan:**
- Lead with AgentProbe as proof of end-to-end AI shipping ability — exactly what the JD asks for: *"ship full-stack AI projects end to end"*
- Frame the LLM Router as inference infrastructure experience (dynamic routing across Ollama/OpenAI/Anthropic/Groq)
- Frame AI on FHIR's NLP-to-structured-API pipeline as structured extraction experience
- Entrata's accounting automation modules (billing, payment pipelines, automated decision support) bridge the fintech gap
- Quote: *"AgentProbe is my proof that I can go from zero to a production-grade AI system — agents, RAG, eval, API, dashboard — without a team. That's the end-to-end ownership Ramp is describing."*

---

## D) Comp and Demand

| Source | Range | Notes |
|--------|-------|-------|
| JD | Not disclosed | WFH stipend + relocation support listed |
| Levels.fyi (June 2026) | $218K–$858K total comp | Median $335K–$340K NYC/US for SWE |
| Market (mid-senior AI SWE) | $240K–$397K total comp | Per Levels.fyi SWE level at Ramp |

**Assessment:** Ramp does not list salary in the JD but Levels.fyi data shows median total comp around $335K+ at mid-senior level — well above target. Backed by General Catalyst, Founders Fund, Stripe, Goldman Sachs. Strong equity upside.

**H-1B:** Strong sponsor — 30 LCAs FY2025, 22/23 approved (96% approval rate). 3-4 LCAs FY2026. Confirmed sponsor with a clean record.

---

## E) Customization Plan

| # | Section | Current | Proposed change | Why |
|---|---------|---------|-----------------|-----|
| 1 | Summary | Generic AI builder | Lead with: *"Full-stack AI engineer — built AgentProbe end to end: LLM agents, RAG pipeline, structured extraction, LLM Router for multi-provider inference. 8+ years backend at scale."* | Mirrors JD language exactly |
| 2 | AgentProbe | General description | Emphasize: end-to-end ownership, LLM Router as inference infra, structured RAG retrieval | JD: agents + RAG + LLM inference |
| 3 | AI on FHIR | NLP pipeline | Reframe: *"structured extraction pipeline — NL intent → structured schema → API call"* | JD: structured extraction |
| 4 | Entrata | Scale metrics | Add one bullet referencing accounting/billing automation modules | Bridge fintech domain gap |
| 5 | Competencies | AI focus | Add: Structured Extraction, LLM Inference, End-to-End AI Delivery | JD keyword alignment |

---

## F) Interview Plan

| # | JD Requirement | Story | S | T | A | R | Reflection |
|---|----------------|-------|---|---|---|---|------------|
| 1 | Ship full-stack AI end to end | AgentProbe solo build | No existing tool ran LLM eval locally at zero cost | Build production-grade eval system from scratch | Designed architecture, built 3 LangGraph agents, FastAPI backend, React dashboard, LLM Router, ChromaDB RAG — solo | 15-endpoint API, 5-metric eval, full trace visibility, zero cloud dependency | Define the API contract first — everything else flows from it |
| 2 | AI agents | AgentProbe 3-agent system | Multi-agent coordination had no good open-source solution for eval | Build agents that coordinate across eval, tracing, and prompt fixing | Orchestrator routes, RAG Tracer enriches, Auto Fix iterates — async LangGraph | Closed improvement loop without human intervention | Async coordination matters more than agent count |
| 3 | RAG pipelines | AgentProbe ChromaDB RAG | Retrieval quality was invisible — couldn't tell if bad answers were retrieval or generation failures | Build retrieval evaluation layer | ChromaDB + embeddings + RAG Tracer scores chunk relevance per query | Full trace: retrieval quality separated from generation quality | Score retrieval and generation independently — combined scores hide the root cause |
| 4 | Structured extraction | AI on FHIR | Clinicians typed questions; FHIR APIs needed structured parameters | Build NL → structured schema extraction pipeline | spaCy + BERT + LLMs extract intent → map to FHIR schema → structured API call | ~60% retrieval time reduction; EN/ES multilingual | Schema-first design makes NL extraction far more reliable |
| 5 | Backend systems at scale | Entrata production | 100K+ MAU, 1M+ records, multi-tenant — needed reliable data infrastructure | Own data pipelines and backend modules end-to-end | AWS S3 migration, PostgreSQL tuning, Docker containerization, TDD/BDD | 99.5% uptime, 40% faster deployments, zero security incidents | Observability from day one — you can't debug what you can't measure |

**Case study to present:** AgentProbe end-to-end — show the full stack: LLM Router (inference infra) → Orchestrator (agent) → ChromaDB RAG (retrieval) → LLM judges (eval) → Auto Fix (iteration). Frame it as: *"This is the kind of end-to-end AI system I'd build at Ramp."*

**Red flag questions:**
- *"You don't have fintech experience"* → *"True for consumer fintech. At Entrata I built billing automation, payment pipelines, and accounting decision support for property management — process automation at scale is the same discipline. I'd ramp into Ramp's domain in the first sprint."*
- *"Have you fine-tuned models?"* → *"Not in production yet — my LLM work has been prompt engineering, RAG, and evaluation. I have the PyTorch and Hugging Face foundations to ramp into fine-tuning. Happy to dig into a specific fine-tuning challenge as a practical exercise."*

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Posting freshness | Active on Ashby + General Catalyst + Lux Capital + LinkedIn | Positive |
| Apply button | Active | Positive |
| JD specificity | Named projects (jsonformer open-source), specific domains (RAG, structured extraction, fine-tuning, inference) | Positive |
| Company health | 25K+ businesses, tens of billions in purchases, backed by GC + Founders Fund + Stripe + Goldman | Positive |
| H-1B | 30 LCAs FY2025, 96% approval — strong sponsor | Positive |
| Salary | Not disclosed but Levels.fyi data is strong ($335K+ median) | Neutral |
| Reposting | "All Levels" variant also posted — suggests active, ongoing hiring | Positive |

---

## Keywords Extracted

applied ai, ai engineer, full-stack, llm, rag, structured extraction, ai agents, fine-tuning, llm inference, langchain, langgraph, python, typescript, backend, cloud infrastructure, fastapi, chromadb, production ai, fintech, ramp, end-to-end, jsonformer

---

## Machine Summary

```yaml
report_num: 036
company: Ramp
role: Applied AI Engineer
date: 2026-06-05
score: 4.0
archetype: Agentic / Automation + Software Engineer (AI-focused)
legitimacy: High Confidence
location: New York, NY or San Francisco, CA — hybrid (WFH stipend)
comp_range: "$335K+ median total comp (Levels.fyi); base not disclosed"
visa_risk: low (30 LCAs FY2025, 96% approval; 3-4 LCAs FY2026)
key_gaps:
  - Fine-tuning (not in CV — soft gap)
  - Fintech domain (proptech background — soft gap)
key_strengths:
  - AgentProbe = direct proof of end-to-end AI shipping (agents + RAG + inference + eval)
  - Full-stack Python/TS/FastAPI/AWS = exact stack match
  - "All levels" role — no seniority mismatch
  - Strong H-1B sponsor
  - WFH stipend + relocation support = flexible location
location_risk: medium — hybrid NYC or SF; relocation from Virginia possible with support
recommend: strong apply — end-to-end AI match, flexible seniority, strong H-1B record, exceptional comp
```
