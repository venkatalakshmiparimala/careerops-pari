# Evaluation: Tako — Backend Engineer (Search, AI, Data Infrastructure)

**Date:** 2026-09-23
**URL:** (pasted JD)
**Archetype:** Applied AI Engineer + Agentic / Automation (hybrid)
**Score:** 4.2/5
**Legitimacy:** High Confidence
**PDF:** ✅ output/cv-venkata-lakshmi-parimala-pasupuleti-tako-2026-09-23.pdf

---

## A) Role Summary

| Dimension | Details |
|-----------|---------|
| **Archetype** | Applied AI Engineer + backend data infrastructure |
| **Domain** | Knowledge indexing, search infrastructure, AI-powered knowledge retrieval |
| **Function** | Own backend + data + search + AI infrastructure; ship with high velocity on small team |
| **Seniority** | Mid-career+ (3+ years; "not ready to mentor entry-level") |
| **Work model** | SF Fair Chance Ordinance mentioned — likely SF-based or SF-friendly; remote not explicit |
| **Comp** | Not disclosed — early-stage startup, likely equity-heavy |
| **Sponsorship** | Not stated — small startup, flag early |
| **TL;DR** | Python + Django + modern AI stack = direct match. AgentProbe + LeaseI = their "edge" criterion for side projects demonstrating genuine AI/search interest. Location unclear (SF implied), comp unknown, sponsorship unconfirmed. Score 4.2/5 — below 4.5 threshold. |

---

## B) Match with CV

| JD Requirement | CV Evidence | Match |
|---|---|---|
| 3+ years relevant engineering | 8+ years Python production SWE at Entrata | ✅ Exceeds |
| Python mastery | 8+ years Python across Entrata + GMU + projects | ✅ Direct match |
| Django familiarity | Django in cv.md Languages & Frameworks | ✅ |
| Modern AI development stack | LangGraph, LangChain, RAG, embeddings, vector DBs, LLMs, FastAPI, ChromaDB | ✅ Direct match |
| Search infrastructure | LeaseI: hybrid TF-IDF + semantic search, reranking, section-aware chunking, retrieval over 1,240 PDFs; AgentProbe: ChromaDB RAG eval | ✅ |
| AI systems in production | LeaseI (93.6% precision, eval'd across 1,240 PDFs); AgentProbe (CI-integrated eval harness) | ✅ |
| Data infrastructure for indexing + serving knowledge | Entrata: HUD income-limit pipeline (few thousand rows → 180K records), 200+ SQL optimizations, multi-tenant schemas; GMU pipelines across 190+ countries | ✅ |
| Build across multiple domains (core product, search, data infra) | Full-stack at Entrata (20+ modules); AI + search (LeaseI); eval infra (AgentProbe) | ✅ |
| **Edge: side projects showing genuine AI + search interest** | **AgentProbe (open-source, CI-integrated eval toolkit) + LeaseI (8-agent RAG system) — both live on GitHub** | ✅ **Exact edge match** |
| **Edge: early-stage startup experience** | Magizhs (small team, shipped to real client); Blue Horse Digital (early-stage volunteer) | ⚠️ Adjacent — not founding/seed experience |
| Production search serving millions of users | Entrata: 100K+ MAU — not millions | ⚠️ Scale gap |
| Sponsorship | Not stated | ⚠️ Risk at small startup |

---

## C) Level and Strategy

| Dimension | Finding |
|-----------|---------|
| Their bar | "Mid-career and more senior" — explicitly not entry-level mentorship mode |
| Her fit | 8yr SWE + hands-on AI projects = strong mid-senior match; owns systems, doesn't need hand-holding |
| Strategy | Lead with AgentProbe + LeaseI as the "side projects demonstrating genuine AI + search interest" they explicitly ask for. These aren't demos — they're CI-integrated systems with eval harnesses. |

---

## D) Comp and Demand

| Metric | Data |
|--------|------|
| JD range | Not disclosed |
| Estimated range | $120K–$160K + significant equity (early-stage startup) |
| Score | **2.5/5** — unknown; early startup = high equity risk, potentially lower base |
| Risk | Early-stage = could fold; equity may be worthless; comp ceiling lower than Series B+ |

---

## E) Customization Plan

| # | Section | Proposed change |
|---|---------|-----------------|
| 1 | Summary | Lead with search + AI infrastructure: "Python backend engineer with 8yr production depth and hands-on AI/search systems — LeaseI (hybrid TF-IDF + semantic search, 8-agent RAG pipeline) and AgentProbe (open-source AI eval infrastructure, CI-integrated). Django in stack." |
| 2 | AgentProbe | Lead with: open-source, CI-integrated, live on GitHub — maps to their "side projects demonstrating genuine AI/search interest" edge criterion |
| 3 | LeaseI | Lead with: search infrastructure (hybrid retrieval, reranking, indexing over document corpus), then agent pipeline |
| 4 | Entrata | Lead with: data infrastructure scale (1.6M+ records, 200+ SQL optimizations), Python ownership, multi-tenant backend |

---

## F) Interview Plan

| # | JD Requirement | Story |
|---|----------------|-------|
| 1 | Search infrastructure | LeaseI: hybrid TF-IDF + semantic search, section-aware chunking, reranking — built and tuned a retrieval stack from scratch with no LangChain dependency, by design. Measured retrieval quality via AgentProbe groundedness metric. |
| 2 | AI systems with high accuracy + low latency | AgentProbe: latency is a first-class eval metric alongside correctness. Model routing selects cheapest provider meeting latency + quality thresholds. LeaseI: pass@3 88.3% — designed for recall via multi-trial sampling. |
| 3 | Data infrastructure for indexing knowledge | Entrata 7yr: annual pipeline expanding few thousand federal rows → 180K domain records; owned schema, indexing, validation, rollback. Designed for correctness, not just throughput. |
| 4 | Side projects showing genuine AI/search interest | AgentProbe is open-source on GitHub with CI-integrated regression harness — not a demo, a system. LeaseI is evaluated on 1,240 real documents with quantified precision + F1. |
| 5 | Owning end-to-end across backend + search + data | At Entrata: owned the HUD pipeline solo for 7 years across schema design, ingestion, validation, rollback, and incident response. Same pattern for RabbitMQ async system. Full ownership = her default mode. |

---

## G) Posting Legitimacy

| Signal | Finding | Weight |
|--------|---------|--------|
| Company | Tako — early-stage, "making world's knowledge available to AI" — small team | Positive |
| Salary | Not disclosed | Neutral |
| Tech specificity | Python, Django, search, AI stack — real engineering context | Positive |
| Remote policy | SF Fair Chance Ordinance only mention — location unclear | Cautious |
| JD quality | Personality-forward JD ("sense of humor", "obsessive craft") — real small team | Positive |
| Sponsorship | Not stated — small startup risk | Unknown |

**Assessment: High Confidence** — Real company, real role.

---

## Verdict

**4.2/5 — Below 4.5 threshold.**

Strong tech match (Python + Django + AI/search stack + open-source side projects = their exact edge criteria). Main drags: location unclear (SF likely), comp unknown (early startup), sponsorship unconfirmed, scale gap (100K MAU vs. "millions").

If remote is confirmed and sponsorship is available → strong apply. Otherwise, proceed with caution.

---

## Keywords extracted

Python, Django, backend, search infrastructure, AI stack, RAG, indexing, data infrastructure, knowledge retrieval, semantic search, LangGraph, embeddings, vector database, ChromaDB, FastAPI, production AI, open-source, early-stage, high velocity

## Machine Summary
```yaml
company: Tako
role: Backend Engineer (Search, AI, Data Infrastructure)
score: 4.2
archetype: Applied AI Engineer + Backend Infrastructure
level: Mid-Senior
comp_range: "Not disclosed (~$120K-$160K + equity estimated)"
location: SF likely — remote not confirmed
sponsorship: Not stated — verify early
apply: Below threshold (4.2 < 4.5) — confirm remote + sponsorship first
top_proof_points:
  - AgentProbe + LeaseI (open-source side projects = their explicit edge criterion)
  - Python 8yr + Django in stack
  - Hybrid TF-IDF + semantic search in LeaseI
  - Entrata data infrastructure depth
key_gap:
  - Location unclear (SF likely)
  - Early-stage comp/equity risk
  - Sponsorship unconfirmed
  - Scale gap (100K MAU vs millions)
```
