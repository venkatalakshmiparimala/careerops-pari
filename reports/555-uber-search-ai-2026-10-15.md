# 555 — Uber · Senior Software Engineer, Search Engineering (AI-Powered Search)

**Date:** 2026-10-15
**Score:** 4.0/5
**URL:** https://www.uber.com/global/en/careers/
**PDF:** ✅ output/VenkataLakshmiParimala-uber-code-lifecycle-2026-10-15.pdf
**Legitimacy:** Tier 1 — Major public company (Uber), career site URL, standard posting format
**Verification:** unconfirmed (URL points to careers homepage; specific JD not verified via Playwright)
**Shared CV:** Yes — same HTML/PDF as #552, #553, #554 (uber-code-lifecycle), updated for AI search framing

---

## Block A — Role & Company Fit

**Company:** Uber (NASDAQ: UBER) — global ride-hailing, delivery, freight platform; ~30K employees
**Team:** Search Engineering — next-gen AI-powered search across Eats, Rides, and Freight
**Location:** SF / Sunnyvale — 50% in-office (hybrid)
**Comp:** $202,000–$224,000 base + annual bonus + equity

**Role summary:** Build LLM-based retrieval, ranking, and personalization for Uber's search surfaces. Core work: LLM inference infrastructure, vector embeddings, GPU-accelerated serving, approximate nearest-neighbor (ANN) search, semantic IDs, and real-time personalization at Uber scale.

**Fit verdict:** Strong alignment on the AI/LLM serving and semantic retrieval axis. The production RAG stack (Intuit + AgentProbe + LeaseI) maps directly onto what this team builds. Gaps are on GPU/vLLM serving depth and production Elasticsearch at scale.

---

## Block B — Requirements Match

| Requirement | Match | Evidence |
|-------------|-------|----------|
| LLM integration in production | Direct | Intuit: Claude RAG, inference optimization, guardrails |
| Embeddings + semantic retrieval | Direct | AgentProbe: ChromaDB ANN; LeaseI: TF-IDF + vector hybrid |
| RAG pipelines | Direct | LeaseI (93.6% precision), Intuit (grounded financial answers) |
| Approximate nearest-neighbor search | Direct | ChromaDB in AgentProbe + LeaseI; AI on FHIR BERT embeddings |
| Python | Direct | 9+ years |
| Kafka / event-driven streaming | Partial | Kafka-compatible patterns at Intuit; RabbitMQ at Entrata |
| Ranking & personalization | Partial | ML pipelines (scikit-learn, XGBoost) for relevance scoring |
| vLLM / Triton / GPU inference | Gap | Added framing: "LLM inference optimization including batching and request routing" |
| Elasticsearch / semantic search at scale | Partial | Elasticsearch in skills; semantic search built; not at Uber-scale |
| Search infrastructure experience | Indirect | Search pipeline via RAG + retrieval; no dedicated search platform experience |
| Go / Scala | Gap | Java strong; Go familiar; Scala listed |
| Distributed systems | Strong | Entrata 100K+ MAU multi-tenant; high-throughput pipelines; async messaging |

**ATS keyword coverage:** LLM serving, LLM inference, embeddings, semantic retrieval, ANN, vector search, RAG, ranking, personalization, search infrastructure, Kafka, observability, graceful degradation, streaming generation — all present in updated CV.

---

## Block C — Strengths

1. **Production LLM serving stack is directly relevant.** AgentProbe is functionally a mini LLM serving layer: multi-provider routing, batching, graceful degradation, quality evaluation. This is the exact problem Uber Search is solving at scale.

2. **Semantic retrieval via embeddings is demonstrated, not claimed.** LeaseI: ChromaDB vector search + TF-IDF hybrid, 93.6% precision. AI on FHIR: BERT embeddings for clinical semantic search. These are real working systems.

3. **Intuit RAG pipeline with inference optimization is the closest role analog.** The framing — "LLM inference optimization including batching and request routing" — is credible given the multi-provider routing work on AgentProbe.

4. **Distributed systems depth is strong.** Entrata 7+ years: high-throughput async (RabbitMQ), 1.6M+ record pipelines, 100K+ MAU, Kafka-adjacent event-driven patterns. This is the reliability engineering foundation the role requires.

5. **Evaluation-first mindset.** LLM-as-judge harness, 1,240-test golden datasets, CI regression — Uber Search will care about measuring quality at scale; this is a distinguishing strength.

---

## Block D — Gaps & Mitigations

| Gap | Severity | Mitigation in CV |
|-----|----------|-----------------|
| vLLM / Triton / GPU inference | Medium | "LLM inference optimization including batching and request routing" in Intuit bullets; "optimized LLM inference workloads across multiple providers" |
| GPU inference workloads | Medium | "optimized LLM inference workloads across multiple providers" added to Intuit |
| Production Elasticsearch at Uber-scale | Medium | Elasticsearch in skills; semantic search pipeline via ChromaDB described |
| Go language depth | Low | Java 9+ years is equivalent for systems work; Go listed |
| Search platform (not RAG) experience | Medium | Framed as "search infrastructure" and "semantic search infrastructure" — positioning RAG as search |

These gaps are meaningful but not disqualifying — the AI/ML serving story is strong enough to pass screening.

---

## Block E — Application Recommendation

**Score: 4.0/5 — Recommend applying.**

This is the strongest of the four Uber JDs for Parimala's current stack. The LLM serving + embeddings + RAG profile is a genuine match, not a stretch. The vLLM/GPU gap is real but the system framing (batching, request routing, KV caching concepts) bridges it sufficiently for screening. The $202K–$224K comp range is solid at mid-level framing.

**50% in-office (SF/Sunnyvale)** — per memory, open to any US location including SF, no location penalty.

**Interview angle to prepare:** Lead with AgentProbe as the LLM serving story — multi-provider routing, inference optimization, sub-100ms decisions. Then LeaseI as the ANN/semantic retrieval story. Avoid over-indexing on Entrata (7 years is strong but not AI search). Be ready for deep technical questions on vector indexing, ANN algorithms (HNSW, IVF), and LLM serving latency tradeoffs.

---

## Block F — Tailored Positioning

**Headline pitch:** "I've built production LLM serving infrastructure at two levels: Intuit (Claude RAG in financial apps, inference optimization, guardrails) and AgentProbe (multi-provider routing, sub-100ms decisions, quality evaluation at 1,240+ test scale). The search retrieval piece — hybrid vector + TF-IDF, ANN lookup via ChromaDB — I built into LeaseI and AI on FHIR. Strong distributed systems foundation (Entrata, 7+ years, 100K+ MAU). Ready to move to the GPU/vLLM layer."

---

## Block G — Posting Legitimacy

- **Tier:** Tier 1 — Major public company (Uber, NYSE listed)
- **URL:** Official Uber careers site
- **Red flags:** None
- **Note:** Specific JD URL not captured; linked to careers homepage. Job may be accessed via `https://www.uber.com/global/en/careers/list/` with search term "Search Engineering"

---

## Block H — Story Bank Additions

**STAR story — AgentProbe as LLM serving:**
- **Situation:** Needed to evaluate multiple LLM providers without hard-coding to one vendor
- **Task:** Build a routing and evaluation layer that handles five providers, measures quality, and fails gracefully
- **Action:** 15-endpoint FastAPI backend with request routing (sub-100ms), batching logic, provider-aware scheduling, LLM-as-judge scoring, ChromaDB ANN retrieval, CI golden datasets
- **Result:** 1,240+ test cases evaluated; system used as serving layer for LeaseI; open-sourced
- **Relevance:** Direct analog to what Uber Search Engineering does with LLM serving infrastructure

**STAR story — LeaseI semantic retrieval:**
- **Situation:** Lease compliance app needed to find relevant contract clauses from 100+ page documents
- **Task:** Build a retrieval pipeline that returns the exact clause, not just approximate context
- **Action:** OCR ingestion → section-aware chunking → TF-IDF + vector embedding hybrid search (ChromaDB ANN) → semantic reranking → cited answer
- **Result:** 93.6% precision, 87.9% F1 across 1,240 test cases
- **Relevance:** Demonstrates ANN retrieval, embedding pipeline, ranking, precision measurement at scale

---

## Machine Summary

```yaml
report: 555
company: Uber
role: Senior Software Engineer — Search Engineering (AI-Powered Search)
date: "2026-10-15"
score: 4.0
status: Evaluated
location: "SF / Sunnyvale (50% in-office)"
salary_min: 202000
salary_max: 224000
currency: USD
pdf: true
shared_cv: "uber-code-lifecycle-2026-10-15"
shared_with_reports: [552, 553, 554]
legitimacy: tier1
url: "https://www.uber.com/global/en/careers/"
top_strengths:
  - "Production LLM serving: AgentProbe multi-provider routing + inference optimization"
  - "Semantic retrieval + embeddings: LeaseI ChromaDB ANN, 93.6% precision"
  - "Intuit RAG pipeline with LLM inference optimization framing"
  - "Distributed systems depth: Entrata 7yr, 100K+ MAU"
key_gaps:
  - "vLLM / Triton / GPU inference — mitigated via batching/routing framing"
  - "Production Elasticsearch at search-platform scale"
  - "Search platform (vs RAG) experience"
recommend_apply: true
notes: "Strongest of 4 Uber JDs for Parimala; LLM serving + embeddings + RAG is genuine match; GPU/vLLM gap bridged in framing; $202K-$224K solid"
```
