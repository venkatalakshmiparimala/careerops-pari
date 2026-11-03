# 114 — Pager Health · Applied AI Engineer

**Date:** 2026-06-23
**Score:** 4.5/5
**URL:** https://boards.greenhouse.io/pagerhealth/jobs/7749574
**PDF:** ❌
**Legitimacy:** Medium-High Confidence — Pager Health, health AI company NY; Greenhouse ATS; active posting confirmed 2026-06-23

---

## Block A — Role Summary

| Field | Detail |
|---|---|
| Archetype | Applied AI Engineer — Agentic Systems + Eval Infrastructure |
| Domain | Health AI — agentic workflows, RAG pipelines, clinical data automation |
| Function | Build agentic applications, RAG pipelines with vector stores, eval infrastructure, tool integrations, API orchestration |
| Seniority | Mid-level (3+ years required) |
| Location | Remote US |
| Comp | $150,000–$160,000 base + equity + benefits |
| H-1B | ⚠️ Low volume but confirmed — 7 LCAs FY2022–2024, 1 petition FY2024 approved |

---

## Block B — Match with CV

| Requirement | Evidence | Strength |
|---|---|---|
| Python (3+ yrs) | 8+ years production Python at Entrata | ✅ Strong |
| LangChain / LangGraph | AgentProbe (3-agent LangGraph runtime, multi-provider routing) | ✅ Direct |
| RAG pipelines + vector stores | AgentProbe (ChromaDB), LeaseI (RAG over 1,240 lease PDFs) | ✅ Direct |
| Eval infrastructure for agents | AgentProbe 5-metric LLM-as-judge engine, CI/CD quality gates | ✅ Strongest proof point |
| Agentic applications end-to-end | AgentProbe (Orchestrator + RAG Tracer + Auto Fix), LeaseI | ✅ Strong |
| AWS (Bedrock / cloud) | AWS S3/EC2/RDS/Glue at Entrata (not Bedrock specifically) | ✅ Good — same cloud, different service |
| Healthcare domain | AI on FHIR (HIPAA-compliant, FHIR APIs, RBAC) | ✅ Direct domain match |
| CrewAI | Not in stack (uses LangGraph — same paradigm) | ⚠️ Minor gap |
| Azure OpenAI / Vertex AI | Not specifically (has OpenAI API + Anthropic API) | ⚠️ Minor gap |
| Pinecone / Weaviate / pgvector | Has ChromaDB / FAISS — same concept, different vendor | ⚠️ Minor gap |
| LangSmith / RAGAS | Not specifically (AgentProbe builds equivalent observability) | ⚠️ Minor gap |

**Gap assessment:** All gaps are tooling variants within concepts she already knows. LangGraph → CrewAI is an afternoon. ChromaDB → Pinecone is a week. AgentProbe already demonstrates LangSmith-equivalent observability. No conceptual gaps.

---

## Block C — Level & Strategy

Mid-level (3+ years required). User has 8+ years — honest fit, not overqualified in a way that triggers rejection at a startup. Healthcare AI + HIPAA compliance overlap with AI on FHIR is a genuine differentiator.

**Positioning:**
1. **Eval infrastructure** — AgentProbe's 5-metric LLM-as-judge engine is exactly what they're building. Most candidates talk about evaluation; you shipped it.
2. **Healthcare compliance** — AI on FHIR (HIPAA-compliant RBAC, FHIR APIs, clinical NLP) maps directly to Pager Health's regulated domain.
3. **Production RAG** — LeaseI (93.6% precision, 1,240 PDFs) + AgentProbe ChromaDB pipeline = end-to-end RAG in production.

**Interview expectation:** Take-home project or system design for healthcare AI agents likely. No LeetCode-heavy rounds at this company type.

---

## Block D — Comp

$150,000–$160,000 base + equity + benefits. Above target range ($100K–$140K). Equity upside depends on stage — Pager Health is likely Series B/C. Strong offer if visa confirms.

---

## Block E — Why 4.5

| Factor | Score |
|---|---|
| CV match | 4.2 — LangGraph/RAG/eval exact; minor tooling variants |
| North Star fit | 4.8 — Agentic AI Engineer in a regulated domain = top target archetype |
| Comp | 5.0 — above target range |
| Location | 5.0 — Remote US |
| Healthcare domain boost | +0.2 — AI on FHIR is direct proof |
| H-1B risk | -0.2 — confirmed sponsor but low volume (small company) |
| **Global** | **4.5/5** |

---

## Block G — Posting Legitimacy

**Medium-High Confidence.**
- Pager Health: health AI company, NY-based, Greenhouse ATS (established companies use Greenhouse)
- Active posting confirmed 2026-06-23 via agentic-engineering-jobs.com and Greenhouse board
- H-1B: 7 LCAs FY2022–2024, 1 petition FY2024 approved — low volume but real track record
- Salary disclosed ($150K–$160K) — legitimate signal

## Machine Summary

```yaml
id: 114
company: Pager Health
role: Applied AI Engineer
date: 2026-06-23
score: 4.5
status: Evaluated
pdf: false
url: https://boards.greenhouse.io/pagerhealth/jobs/7749574
location: Remote US
comp_base: "$150,000–$160,000"
archetype: Applied AI Engineer — Agentic + Eval + Healthcare
verdict: APPLY — LangGraph/RAG/eval exact match; healthcare domain AI on FHIR proof; above-target comp; verify H-1B early in screen
```
