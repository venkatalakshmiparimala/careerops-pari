# Evaluation: Juniper Square — Staff Software Engineer (AI)

**Date:** 2026-06-24
**URL:** https://jobs.ashbyhq.com/junipersquare/c0f6d8c5-7dad-4599-be77-b04b8a2b8af0
**Archetype:** Applied AI Engineer / LLMOps (Hybrid)
**Score:** 4.0/5
**Legitimacy:** Proceed with Caution
**PDF:** pending

---

## A) Role Summary

| Dimension | Detail |
|-----------|--------|
| Archetype | Applied AI Engineer + LLMOps (hybrid) |
| Domain | Private markets / financial document processing |
| Function | Build hands-on — RAG systems, document pipelines, LLM eval, agentic workflows |
| Seniority | Staff (7+ YOE required) |
| Remote | Fully remote (US) |
| Stack | Python, FastAPI/Django, RAG, pgvector/Pinecone, LangGraph-style agents, AWS, Docker |
| Comp | $210,000–$260,000 + equity |
| TL;DR | Own the AI layer (document processing, RAG, eval) for JunieAI — Juniper Square's embedded AI platform serving $300B+ in private markets assets |

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| Python backend, FastAPI/Django | AgentProbe (15-endpoint FastAPI), 8yrs Python at Entrata | ✅ Direct |
| RAG pipelines + vector stores | AgentProbe (ChromaDB), LeaseI (RAG over 1,240 lease PDFs) | ✅ Direct |
| LLM evaluation frameworks + HITL | AgentProbe 5-metric LLM-as-judge eval engine, pass@k harness | ✅ Direct |
| Document processing pipelines (PDFs) | LeaseI — chunking, embedding, classification on 1,240 PDFs, 93.6% precision | ✅ Direct |
| Tool-calling agents / multi-step reasoning | AgentProbe 3-agent LangGraph runtime (Orchestrator, RAG Tracer, Auto Fix) | ✅ Direct |
| AWS, Docker | AWS S3/RDS/Glue at Entrata (100% PHI compliance), Docker (50% speedup) | ✅ Strong |
| Production AI at scale | Entrata 1.6M records AI pipeline with quality gates | ✅ Strong |
| PostgreSQL | 200+ SQL queries optimized (30% perf gain) at Entrata | ✅ Strong |
| CI/CD, GitHub Actions | AgentProbe CI/CD via GitHub Actions | ✅ Direct |
| 7+ years Staff-level | 8 years production engineering (Jan 2017 – Aug 2024) | ✅ |
| Financial documents / private markets | Property management / affordable housing — NOT fund administration or LP reporting | ⚠️ Domain gap |
| pgvector, Pinecone, Weaviate | ChromaDB used — same paradigm, different implementation | ⚠️ Minor |
| Staff-level cross-team leadership | Senior Engineer leading 20+ modules + Docker rollout — Staff signals, not Staff title | ⚠️ Level gap |

**Gaps:**
1. **Private markets domain** — LeaseI processes lease PDFs; this role processes fund statements, K-1s, LP reports. Both are complex financial/legal documents. Adjacent, not identical. Mitigation: frame LeaseI as proof of "high-stakes document AI" — auditable output, deterministic rules engine, same stakes.
2. **pgvector/Pinecone vs ChromaDB** — Not a hard blocker. All are vector stores. A 1-line mention of familiarity with pgvector in cover letter closes this.
3. **Staff title gap** — Senior Engineer for 3.5 years at Entrata + 20+ end-to-end modules + GMU research. No Staff title but Staff-level scope. Frame the breadth of ownership, not the title.

---

## C) Level and Strategy

**Level detected:** Staff IC (7+ years, cross-team scope, architecture ownership)
**Parimala's natural level:** Senior → Staff transition (8 years, strong breadth, no Staff title yet)

**Sell Senior as Staff:**
- "I led 20+ production modules end-to-end across 120+ sprints — architecture, design, rollout, adoption tracking. That's Staff scope without the title."
- "AgentProbe is a proof of Staff-level initiative: I identified a gap in agentic AI testing tooling, designed the system from scratch, and shipped it open source."
- "At Entrata I was the technical owner of Docker containerization for the entire microservices layer — that's cross-team platform work, not feature work."

**If they downlevel to Senior:**
- Accept if comp stays above $185K (well above target)
- Negotiate 6-month review with explicit promotion criteria
- Senior at Juniper Square = $185-225K per other open roles

---

## D) Comp and Demand

| Data Point | Detail |
|------------|--------|
| JD stated comp | $210,000–$260,000 USD base + equity |
| Market comp (Staff SWE, AI, remote) | $180–260K (Levels.fyi, remote.io listings for similar roles) |
| Vs Parimala's target ($100–140K) | Exceeds target by ~70–85% — exceptional |
| Equity | Included; amount unstated (Series C private, not public) |
| Juniper Square funding | $350M+ raised, Series C — reasonable exit probability |

**Assessment:** Best comp of any role evaluated so far. Even at the floor ($210K), this is 2x the stated minimum target. The equity upside on a $350M+ funded Series C is real.

---

## E) Customization Plan

| # | Section | Current | Proposed Change | Why |
|---|---------|---------|-----------------|-----|
| 1 | Summary | "housing AI" framing | Reframe as "production document AI" — lease PDFs → financial document PDFs, same underlying challenge | Domain bridge |
| 2 | LeaseI bullet | "housing compliance pipeline" | Add: "document extraction, chunking, embedding — deterministic audit trail on high-stakes documents" | Speaks to financial doc context |
| 3 | AgentProbe bullet | "multi-agent eval framework" | Explicitly call out "LLM evaluation frameworks, HITL feedback loops, pass@k regression gates" | Matches JD terminology exactly |
| 4 | Skills | ChromaDB listed | Add: "pgvector, vector stores (ChromaDB, pgvector)" | Closes minor tool gap |
| 5 | Entrata Senior bullet | "production AI pipeline" | Add: "model output validation, quality gates, human-in-the-loop review" | Matches "trustworthy AI outputs" in JD |

---

## F) Interview Plan

| # | JD Requirement | STAR+R Story | Reflection |
|---|----------------|-------------|------------|
| 1 | RAG system production ownership | LeaseI: built RAG over 1,240 lease PDFs, 93.6% precision, 10 compliance rules — chunking, embedding, retrieval, deterministic rules on top | Learned that RAG alone isn't enough for high-stakes decisions — deterministic rules engine on top of LLM output is what makes it auditable |
| 2 | LLM eval frameworks | AgentProbe: 5-metric LLM-as-judge (factual accuracy, hallucination, retrieval, completeness, compliance), pass@k harness, CI/CD gate blocking production | Eval is the hardest part to get right — you need diverse test cases, not just golden answers |
| 3 | Document processing pipeline | LeaseI: PDF ingestion → chunking → embedding → retrieval → compliance classification on residential leases | Chunking strategy matters more than model choice — wrong chunk size destroyed retrieval quality |
| 4 | Production AI at scale | Entrata: first production AI pipeline on 1.6M real financial records, quality gates, output validation before customer exposure | You need quality gates before AI output reaches production — not just accuracy metrics |
| 5 | Tool-calling multi-step agents | AgentProbe: Orchestrator → RAG Tracer → Auto Fix chain with inter-agent state handoffs, tool calling | State management across agents is the failure mode most people don't test for |
| 6 | Cross-team technical leadership | Docker microservices rollout at Entrata: 50% execution speedup, coordinated across 3 engineering teams | Technical leadership is mostly about making the migration path so clear that other engineers adopt it without being told |
| 7 | Staff-level initiative | AgentProbe: identified tooling gap, designed full system, shipped open source — zero direction, zero budget | The hardest Staff skills aren't technical — it's deciding what to build without being asked |
| 8 | AWS data infrastructure | Entrata AWS S3/RDS/Glue migration: 100% PHI compliance, zero security incidents | Cloud migration is as much a compliance project as an engineering project |

**Case study to present:** LeaseI — document processing (PDFs), RAG, deterministic rules engine, eval harness. Maps directly to "trustworthy AI output on high-stakes documents."

**Red-flag questions:**
- *"You've spent 8 years at one company — can you adapt to a faster-moving environment?"* → "At Entrata I shipped 20+ modules across 120 Agile sprints and led 3 major platform migrations. The breadth is the point — I've worked on everything from data pipelines to AI to compliance to infra. That's startup range inside a scaled company."
- *"Your domain is housing, not private markets"* → "The underlying problem is the same: extract structured signals from complex legal/financial PDFs and make AI output auditable in a high-stakes context. LeaseI does this for leases; JunieAI does it for fund documents. The engineering is identical."

---

## G) Posting Legitimacy

**Assessment: Proceed with Caution**

| Signal | Finding | Weight |
|--------|---------|--------|
| Apply button active | URL resolves (Ashby) — user confirmed accessible | Positive |
| JD tech specificity | Highly specific — FastAPI/Django, pgvector, Cursor/Augment, pass@k eval, HITL | Positive |
| Company funding | $350M+ Series C, 1,000+ employees, 2,300+ clients | Positive |
| H-1B history | 14 LCAs filed 2022–2024, all certified — Software Engineer is listed role type | Positive |
| Layoff history | Late 2022 layoff (5–10%), small subsequent rounds per Blind/Glassdoor | Concerning |
| Sales staff layoff | "Majority of sales staff" laid off recently per Blind | Concerning |
| Hiring freeze reports | Multiple Blind posts mentioning freeze on "almost all US positions" | Concerning |
| Reposting | Staff SWE AI (3ddce7e6) shows "closed" on aggregators; c0f6d8c5 is a new URL — possible re-post | Neutral |

**Context:** The hiring freeze reports appear on anonymous boards (Blind/Glassdoor) and may reflect sales-side freeze, not engineering. The company is actively building JunieAI and the JD is freshly posted with a new Ashby ID. Verify directly: apply and ask the recruiter about engineering headcount status in the first conversation.

---

## Keywords Extracted

RAG pipeline, vector store, pgvector, ChromaDB, Pinecone, document processing, PDF extraction, chunking, embedding, LLM evaluation, HITL, human-in-the-loop, LLM-as-judge, FastAPI, Django, Python, AWS, Docker, Kubernetes, CI/CD, agentic workflows, tool-calling, multi-step reasoning, production AI, evaluation framework, Staff Software Engineer, private markets, fintech, JunieAI, AI-native

---

## Machine Summary

```yaml
company: Juniper Square
role: Staff Software Engineer (AI)
score: 4.0
status: Evaluated
date: 2026-06-24
location: Remote US
salary_range: "$210K–$260K"
visa_sponsorship: confirmed (low volume, all certified)
h1b_risk: medium (low historical volume)
archetype: Applied AI Engineer / LLMOps
pdf: pending
url: https://jobs.ashbyhq.com/junipersquare/c0f6d8c5-7dad-4599-be77-b04b8a2b8af0
```
