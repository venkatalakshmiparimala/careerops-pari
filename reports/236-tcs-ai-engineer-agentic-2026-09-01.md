# Evaluation: TCS — AI Engineer (Agentic AI / RAG / Azure OpenAI)

**Date:** 2026-09-01
**URL:** (pasted — verify on tcs.com/careers or LinkedIn)
**Archetype:** Applied AI Engineer / Agentic (RAG + LangChain + Enterprise APIs)
**Score:** 3.8/5
**Legitimacy:** High Confidence
**PDF:** output/cv-venkata-lakshmi-parimala-pasupuleti-tcs-ai-engineer-2026-09-01.pdf

---

## A) Role Summary

| Dimension | Detail |
|-----------|--------|
| Archetype | Applied AI Engineer — agentic workflows, RAG-based document intelligence, enterprise API integration, Python backend; Azure AI Foundry stack |
| Company | Tata Consultancy Services (TCS) — global IT services; likely client placement model |
| Function | Build AI-powered agentic applications, RAG knowledge/search systems, document intelligence, backend APIs, data pipelines; production-ready delivery |
| Seniority | Not stated — $120K–$145K + "7+ years" equivalent scope suggests mid-to-senior IC |
| Location | Not specified — TCS has US offices; remote/hybrid unknown |
| Comp | $120,000–$145,000 |
| H-1B | TCS is one of the highest-volume H-1B filers in the US (thousands of LCA petitions annually) — but see caveat in Section C |
| TL;DR | Strong archetype match on the AI/agentic side: RAG, LangChain, LangGraph, Python, prompt engineering, enterprise APIs — all confirmed in stack. Two gaps: Azure AI Foundry (have AWS + OpenAI API) and Snowflake (listed as must-have). TCS consulting model limits long-term career growth vs. product company. Score 3.8/5 — below 4.5 threshold; user call. |

---

## B) Match with CV

### Must-Have Skills

| Requirement | CV Match | Quality |
|-------------|----------|---------|
| **Azure AI Foundry & Azure OpenAI** | OpenAI API confirmed (AgentProbe multi-provider routing: OpenAI, Anthropic, Groq, Ollama). Azure AI Foundry = Azure-hosted OpenAI — same APIs, different cloud wrapper. **No Azure-specific deployment experience; AWS is the cloud stack.** | MODERATE — API transfer, platform gap |
| **RAG, Vector Databases, Prompt Engineering** | LeaseI: RAG pipeline (TF-IDF + section-aware chunking, 100% citation correctness); AgentProbe: RAG eval framework; ChromaDB vector DB; prompt engineering across all projects (few-shot, chain-of-thought, output validation) | STRONG |
| **Agentic AI Frameworks (LangChain, Semantic Kernel, CrewAI)** | LangChain + LangGraph confirmed (LeaseI 8-agent LangGraph StateGraph; AgentProbe). Semantic Kernel (Microsoft) and CrewAI not in stack — but LangGraph is the closest equivalent to both. | STRONG (LangChain/LangGraph); PARTIAL (Semantic Kernel/CrewAI) |
| **Python** | 8+ years, expert | STRONG |
| **Snowflake, SQL & Data Integration** | SQL: expert (200+ production optimizations, PostgreSQL/MySQL). Snowflake: NOT in stack — cloud data warehouse, no project or employment history uses Snowflake. Data integration: Entrata ETL/HUD pipelines, AWS S3. | STRONG (SQL + integration); GAP (Snowflake) |
| **Enterprise API / Microservices Development** | FastAPI (15-endpoint AgentProbe backend), REST APIs across 20+ Entrata modules, RabbitMQ async, Docker microservices redesign (50% scalability improvement) | STRONG |

### Nice-to-Have Skills

| Skill | CV Match |
|-------|---------|
| Databricks | Not in stack |
| Snowflake Cortex / Cortex Agents | Not in stack |
| Azure ML | Not in stack (AWS is the cloud; PyTorch/scikit-learn for ML) |
| MLOps / Model Monitoring | AgentProbe: CI regression gate, per-run performance tracking, latency monitoring — adjacent to MLOps |
| **React / Angular** | **React confirmed: AgentProbe dashboard, AI on FHIR frontend** |
| Manufacturing / Supply Chain / Life Sciences | No domain experience |

---

## C) Level and Strategy

**No hard blocks fire.** No clearance requirement, no L6/L7 salary band, no ML infrastructure focus, no Senior title at formal-leveling company.

**What makes this role a real option:**

The core of the JD — RAG-based document intelligence, agentic workflows, LangChain, prompt engineering, Python enterprise APIs — is exactly what LeaseI and AgentProbe demonstrate. LeaseI is specifically a "RAG-based knowledge, search, and document intelligence solution" (the JD's exact words applied to lease compliance). AgentProbe is the evaluation layer. The fit on the AI/agentic side is genuine.

**Snowflake is the real gap.**

Listed as a must-have ("Snowflake, SQL & Data Integration"), but the role is primarily about building AI applications — not running the data warehouse. In practice, TCS/consulting "must-have" lists include the client's full tech stack, and Snowflake is likely there because the target client uses it. SQL expertise is confirmed and deep (200+ production query optimizations). Snowflake SQL is standard SQL with proprietary extensions — the gap is operational (provisioning, warehousing configuration, Snowpark), not fundamental. Frame it as: "Deep SQL expertise on PostgreSQL/MySQL; actively building familiarity with Snowflake's SQL dialect and Snowpark."

**Azure vs. AWS:**

Azure AI Foundry wraps Azure OpenAI, which wraps the same GPT-4o/GPT-4 models Parimala uses via the OpenAI API directly. The programming model is identical — the difference is Azure-specific authentication, resource provisioning, and security controls. This is a 1-2 week learning curve, not a skills gap. Frame it honestly: "Production experience with OpenAI API and AWS cloud; learning Azure AI Foundry for this engagement."

**TCS employer context — important:**

TCS operates on a consulting/services model. In practice:
- You are likely to be placed at a client site (financial services, pharma, manufacturing) under TCS's delivery contract
- Day-to-day direction comes from the client, not TCS management
- Career growth is slower than at a product company — promotions happen on TCS's consulting ladder
- H-1B: TCS IS a top filer (thousands of LCA petitions annually), but their H-1B model has historically faced criticism for concentrating visas on high-billing placements. As an AI engineer on a $120K–$145K role, sponsorship is likely but the quality of the sponsorship relationship matters (attorney, process, proactive filing). Ask directly during screening: "Does TCS sponsor H-1B for this role/client engagement?"

**Score rationale — 3.8/5:**
- AI/agentic archetype match: strong (RAG, LangChain, prompt engineering, enterprise APIs, Python) +0.5 above baseline
- Snowflake must-have gap: −0.3
- Azure vs. AWS platform: −0.2 (addressable gap but present)
- TCS consulting culture vs. product company: −0.2 (career growth, autonomy)
- Comp $120K–$145K: within target, decent for services firm
- H-1B: high volume but consulting-model caveats

Below 4.5 general apply threshold. Apply if you want to expand the funnel or move quickly on a near-certain interview.

---

## D) Comp

| Metric | Value |
|--------|-------|
| Base | $120,000–$145,000 |
| Bonus | Discretionary annual incentive |
| Benefits | Comprehensive (medical, dental, vision, 401K, commuter, etc.) |
| TC estimate | $125K–$155K (base + bonus) |
| vs. target ($80K–$140K) | At top of target, slightly above |
| Comp score | 3.5/5 (within range but IT services ceiling — product companies offer $150K+ for same archetype) |

---

## E) If You Apply — Positioning

| JD Requirement | Proof Point |
|----------------|-------------|
| RAG-based document intelligence | LeaseI: TF-IDF RAG, 100% citation correctness, 0% unsupported-claim rate on 1,240 compliance documents |
| Agentic workflows (LangChain) | LeaseI: 8-agent LangGraph StateGraph (Triage → Retrieval → Configuration → Historical → Reasoning → Validation → Escalation → HITL) |
| Prompt engineering | LeaseI: LLM reasons, deterministic logic decides regulated calls — explicit prompt architecture |
| Enterprise API / microservices | FastAPI (AgentProbe 15-endpoint); Entrata 20+ REST modules; RabbitMQ async |
| SQL & data integration | 200+ production SQL optimizations; Entrata 1.6M HUD records ETL pipeline |
| Python | 8+ years, expert |
| Azure OpenAI (bridge) | OpenAI API production use → "Azure OpenAI uses the same API surface; learning Azure-specific resource configuration" |
| Snowflake (bridge) | SQL expert → "Deep PostgreSQL/MySQL production experience; applying same SQL expertise to Snowflake's dialect" |

---

## G) Posting Legitimacy

**High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Company | TCS — publicly traded (NSE/BSE), $25B+ revenue, well-known employer | Positive |
| JD specificity | Specific stack, specific must-haves vs. nice-to-haves, salary range posted | Positive |
| Salary posted | $120K–$145K — transparent range | Positive |
| Benefits listed | TCS Employee Benefits Summary with detail | Positive |
| Visa welcome | "OPT welcome" explicitly | Positive |

---

## Machine Summary

```yaml
company: TCS (Tata Consultancy Services)
role: AI Engineer (Agentic AI / RAG / Azure OpenAI)
date: 2026-09-01
score: 3.8
archetype: Applied AI Engineer / Agentic (RAG + LangChain + Enterprise APIs)
legitimacy: High Confidence
recommend: BELOW THRESHOLD (4.5) — strong AI archetype match but Snowflake must-have gap + Azure vs. AWS platform gap + TCS consulting model. Apply if expanding funnel. Ask about H-1B sponsorship quality during screening.
comp_low: 120000
comp_high: 145000
comp_bonus: discretionary
h1b_sponsor: high volume (TCS = top H-1B filer) but consulting model — ask explicitly if they sponsor for this specific role/client
hard_block: NO
key_gap: Snowflake (must-have, not in stack); Azure AI Foundry (have AWS + OpenAI API — same API, different platform); Semantic Kernel/CrewAI (have LangChain/LangGraph equivalent)
key_strength: RAG (LeaseI = exact document intelligence use case); LangChain/LangGraph 8-agent system; prompt engineering; Python 8+ years; enterprise APIs; SQL expert
priority: optional — 3.8/5, below 4.5 threshold; user call
```
