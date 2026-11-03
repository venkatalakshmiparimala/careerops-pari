# Evaluation: CGI — Agentic AI Developer

**Date:** 2026-06-17
**URL:** https://cgi.njoyn.com/corp/xweb/xweb.asp?clid=21001&page=jobdetails&jobid=J0626-1051&BRID=1309191&SBDID=943&lang=1
**Archetype:** Agentic / Automation + AI Platform / LLMOps (hybrid)
**Score:** 4.2/5
**Legitimacy:** High Confidence
**PDF:** output/cv-cgi-agentic-ai-developer-2026-06-17.pdf

---

## A) Role Summary

| Dimension | Detail |
|-----------|--------|
| Archetype | Agentic / Automation + AI Platform / LLMOps |
| Domain | Enterprise GenAI for healthcare financial workflows |
| Function | Build + Deploy |
| Seniority | Mid-Senior (5+ years SE, 2+ years LangChain/LangGraph) |
| Remote | Hybrid — Hartford CT / Bloomfield CT / Raleigh NC / Lafayette LA |
| Team | AI Center of Excellence (CoE) |
| TL;DR | Build and deploy LLM-powered RAG agents and eval pipelines for a healthcare client within CGI's AI CoE |

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| 5+ years Python | 8+ years Python at Entrata (120+ Agile sprints, 20+ modules) | Strong |
| LangChain / LangGraph | AgentProbe: 3-agent LangGraph runtime (Orchestrator, RAG Tracer, Auto Fix) | Strong |
| Multi-agent orchestration | AgentProbe: tool calling, inter-agent state handoffs, multi-provider model routing | Strong |
| RAG / vector search / embeddings | AgentProbe: ChromaDB RAG pipeline with per-run retrieval quality metrics | Strong |
| LLM evaluation loops | AgentProbe: 5-metric LLM-as-judge eval engine (factual accuracy, hallucination, retrieval, completeness, compliance) | Strong |
| Prompt engineering | AgentProbe: multi-provider routing, prompt optimization per model | Strong |
| Production AI deployment | Entrata: 1.6M financial records, PyTorch + OpenAI API, output validation + quality gates | Strong |
| Enterprise API + data integration | Entrata: 15-endpoint FastAPI backend, RabbitMQ, PostgreSQL, AWS S3 | Strong |
| Healthcare domain | AI on FHIR: HIPAA-compliant RBAC, NLP-to-FHIR query translation, structured medical records | Strong |
| Mentor developers | Entrata: 300+ peer code reviews across 120+ Agile sprints | Moderate |
| AI governance / responsible AI | Entrata: 100% PHI compliance, Libsodium-encrypted pipelines, zero security incidents | Strong |
| LangSmith (observability) | Not explicitly in profile — AgentProbe traces agent runs via React dashboard + ChromaDB metrics | Gap (mitigable) |
| Multimodal AI | Not in profile | Gap (minor — not core to role) |

### Gaps

| Gap | Blocker? | Mitigation |
|-----|----------|------------|
| LangSmith | No | Frame AgentProbe's custom trace-level agent monitoring as equivalent (you built what LangSmith does, from scratch). Say: "I built end-to-end observability directly into AgentProbe — per-run metrics, retrieval quality, latency, regression drift — before adopting third-party tooling." |
| Multimodal AI | No | Mentioned once in JD, not in requirements or bonus. Don't address unless asked. |
| Team lead title | No | Cite "led Docker containerization initiative" + "300+ peer code reviews" + "5+ internal platform tools." Senior contributor with cross-team impact = lead-equivalent. |

---

## C) Level and Strategy

**Level detected:** Mid-Senior — 5+ years SE, 2+ years LangChain/LangGraph
**Parimala's natural level:** Senior — 8+ years SE, 2 years hands-on agentic AI

**Sell senior plan:**
- Lead with AgentProbe as a *production system*, not a portfolio project: "15-endpoint FastAPI backend, 100% local, zero cost, CI/CD integration blocking failing agent runs before prod."
- AI on FHIR gives healthcare credibility most AI candidates lack: "HIPAA-compliant RBAC, NLP-to-FHIR in EN/ES, structured clinical records."
- Entrata financial data frames the "financial workflows" angle: "production AI on 1.6M financial records with output validation and quality gates."
- AI CoE context: position yourself as someone who can both build *and* define best practices (300+ code reviews, 20+ modules, 120+ sprints).

**If they down-level:**
- Accept if base >= $110K + clear AI CoE career path
- Negotiate: 6-month performance review with defined promotion criteria to Senior AI Engineer
- Ask: "What does the first 90 days look like? Is there a defined scope on the healthcare client from day one?"

---

## D) Comp and Demand

| Source | Data |
|--------|------|
| Posted range | $80,600 – $194,000 |
| CGI Software Engineer median (Levels.fyi 2026) | $100K total comp |
| CGI Software Engineer top (Levels.fyi 2026) | $146,150 total comp |
| AI/LLM specialist premium | +20-35% over SE median = ~$120K–$145K estimated |
| Parimala's target | $100K–$140K |
| Verdict | Well within range. At her experience level + AI specialization, target $120K–$135K base. |

**H-1B sponsorship:** CGI Technologies and Solutions filed 780 LCAs in FY2025, ranked #72 among all US sponsors. Strong, established H-1B track record.

**Demand trend:** Enterprise agentic AI demand is strong in 2026, especially for healthcare + financial workflows. LangGraph engineers remain scarce relative to demand.

---

## E) Customization Plan

| # | Section | Current | Proposed Change | Why |
|---|---------|---------|-----------------|-----|
| 1 | Summary | Generic AI Engineer | Add "enterprise GenAI" and healthcare AI on FHIR signal | JD explicitly says "enterprise-grade GenAI for healthcare client" |
| 2 | AgentProbe | Eval engine + observability | Lead with "multi-agent orchestration" + "evaluation loops" — exact JD language | Block B shows this is the core requirement |
| 3 | AI on FHIR | ~60% retrieval reduction | Lead with "HIPAA-compliant" and "healthcare structured records" | Healthcare domain is a differentiator vs. generic AI candidates |
| 4 | Entrata | Financial records + production AI | Add "financial workflows" framing and "output validation + quality gates" | Exact JD phrase match |
| 5 | Skills | LangChain/LangGraph listed | Move to top of AI & Agents row; add "Agent Observability, LLM Evaluation Frameworks" | ATS keyword alignment with JD |

---

## F) Interview Plan

| # | JD Requirement | Story | S | T | A | R | Reflection |
|---|---------------|-------|---|---|---|---|------------|
| 1 | Build AI agents for multi-step workflows | AgentProbe Orchestrator | Needed to test AI agents end-to-end without cloud costs | Build agentic eval system locally | Designed 3-agent LangGraph runtime: Orchestrator routes tasks, RAG Tracer evaluates retrieval, Auto Fix handles regressions | 15-endpoint FastAPI backend, 100% local, CI/CD blocks failing runs | Would integrate LangSmith earlier for observability dashboards |
| 2 | LLM evaluation frameworks | AgentProbe eval engine | Agent quality was hard to measure consistently | Build reproducible eval pipeline | 5-metric LLM-as-judge engine: factual accuracy, hallucination, retrieval, completeness, compliance | Automated quality gates blocking prod deployments | Would add latency-per-agent-step as a 6th metric |
| 3 | RAG + vector search | AgentProbe ChromaDB RAG | Needed per-run retrieval quality visibility | Build traceable RAG pipeline | ChromaDB + embeddings with per-run metrics, regression drift detection, latency tracking | Full retrieval observability across concurrent test suites | Would add hybrid BM25 + vector search for better recall |
| 4 | Production AI on financial data | Entrata 1.6M records | Manual data transformation across 1.6M regulated financial records | Automate with AI pipeline | Applied PyTorch + OpenAI API with output validation and quality gates | Zero compliance incidents, pipeline now fully automated | Would add anomaly detection as a second validation layer |
| 5 | HIPAA-compliant systems | AI on FHIR | Clinicians needed natural language access to FHIR records across 2 languages | Build NLP-to-FHIR platform | Flask + React NLP platform with HIPAA-compliant RBAC, LLMs + BERT + spaCy | ~60% reduction in manual clinical retrieval time | Would add audit logging for every FHIR query |
| 6 | Enterprise API + data integration | Entrata microservices | 100K+ MAU on aging monolith, 40% deployment delay | Containerize and restructure | 20+ microservices (Python, PostgreSQL, RabbitMQ), Docker containerization | 40% deployment time reduction, 50% microservices execution time cut | Would implement service mesh earlier for observability |

**Recommended case study to present:** AgentProbe — it covers 4 of the 6 JD focus areas simultaneously (agents, RAG, eval, observability). Open GitHub link during interview. Walk through: architecture diagram → LLM-as-judge eval engine → CI/CD integration → React dashboard.

**Red-flag questions:**
- *"You don't have LangSmith experience"* → "I built equivalent functionality inside AgentProbe from scratch — per-run trace logging, retrieval quality metrics, latency tracking, regression drift detection. I understand what LangSmith does because I built it. Adopting it for a team environment is a one-week ramp."
- *"You've been at one company for 7 years"* → "Entrata scaled from a small team to 100K+ MAU during my tenure — I grew with it from a new graduate to leading containerization and production AI pipelines. The scope changed; the company name didn't."

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Posting system | njoyn.com — CGI's own ATS. Direct corporate posting. | Positive |
| Job ID | J0626-1051 — "J0626" = June 2026. Fresh posting. | Positive |
| Salary disclosed | $80,600–$194,000 range clearly stated | Positive |
| Technology specificity | LangChain, LangGraph, LangSmith, RAG, RLHF, multimodal — highly specific | Positive |
| Business context | Healthcare client + AI CoE = real org structure | Positive |
| CGI layoffs (2025) | Reports of Q3/Q4 2025 layoffs in non-AI departments; some bench-clearing in Canada | Neutral |
| H-1B activity | 780 LCAs in FY2025, ranked #72 — actively hiring internationally | Positive |

**Context notes:** CGI had layoffs in offshore-able support roles. The AI CoE role is the opposite profile — specialized, hard to offshore, active LCA filing confirms US hiring intent. Apply with confidence.

---

## Keywords Extracted

LangChain, LangGraph, LangSmith, RAG, multi-agent systems, agentic AI, LLM evaluation, prompt engineering, vector search, embeddings, ChromaDB, Python, PyTorch, Hugging Face, instruction tuning, RLHF, AI governance, healthcare AI, HIPAA, FastAPI, enterprise GenAI, AI Center of Excellence, retrieval-augmented generation, agent orchestration, production AI

---

## Machine Summary

```yaml
company: CGI
role: Agentic AI Developer
date: 2026-06-17
score: 4.2
archetype: Agentic/LLMOps
location: Hybrid (Hartford CT / Raleigh NC / Lafayette LA)
comp_range: "$80,600-$194,000"
h1b: confirmed (780 LCAs FY2025, rank #72)
legitimacy: High Confidence
apply: evaluate-and-hold (4.0-4.4 range)
pdf: output/cv-cgi-agentic-ai-developer-2026-06-17.pdf
```
