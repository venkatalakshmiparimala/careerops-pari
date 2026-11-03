# Evaluation: Unisys (via staffing) — Sr. AI Data Engineer

**Date:** 2026-09-23
**URL:** (recruiter email — Vinay Kumar, Unisys Talent Solutions)
**Archetype:** AI Platform / LLMOps + Data Engineering (both PRIMARY archetypes)
**Score:** 4.5/5
**Legitimacy:** Medium-High Confidence (staffing firm placement, client not named)
**PDF:** ✅ output/cv-venkata-lakshmi-parimala-pasupuleti-unisys-2026-09-23.pdf

---

## A) Role Summary

| Dimension | Details |
|-----------|---------|
| **Archetype** | AI Platform / LLMOps + Data Engineering (both primary) |
| **Domain** | Generative AI platform — RAG pipelines, ETL ingestion, retrieval quality, knowledge stores |
| **Function** | Design + build ETL pipelines + RAG retrieval infrastructure for a GenAI platform |
| **Seniority** | Sr. AI Data Engineer |
| **Work model** | On-site / Hybrid — Rockville, MD or McLean, VA (McLean is in Fairfax County, VA — commutable from Virginia) |
| **Comp** | Contract (long-term) — recruiter asking for expected pay rate |
| **Sponsorship** | ⚠️ Staffing contract — W2 through Unisys is OPT-compatible; verify H-1B sponsorship status for long-term. OPT W2 is fine for now. |
| **TL;DR** | RAG pipeline + retrieval eval + ETL = AgentProbe + LeaseI IS this role. McLean, VA is commutable. Contract W2 compatible with OPT. Suggest $80–$90/hr W2. **Score: 4.5/5 — APPLY.** |

---

## B) Match with CV

| JD Requirement | CV Evidence | Match |
|---|---|---|
| ETL pipelines, document ingestion at scale | Entrata 7yr: HUD pipeline (180K records), RabbitMQ async processing, AWS S3 migration, AWS Glue | ✅ Strong |
| RAG pipeline development — chunking, embedding, retrieval | LeaseI: section-aware chunking, TF-IDF + semantic hybrid search, ChromaDB vector retrieval, citation grounding | ✅ Direct |
| Vector databases + hybrid search | LeaseI: ChromaDB + TF-IDF reranking; AgentProbe: multi-provider vector routing | ✅ |
| Evaluation frameworks — retrieval precision, recall, relevance | AgentProbe IS this: 5-metric eval engine, golden datasets, regression harness, CI gate, pass@k | ✅ Direct — AgentProbe is their eval requirement |
| AWS: S3, Lambda, Step Functions, OpenSearch, Bedrock | S3 (7yr) ✅; Lambda/Step Functions (learnable, serverless adjacent to CI/CD) ⚠️; Bedrock (AWS LLM API, learnable from OpenAI/Anthropic API experience) ⚠️; OpenSearch (adjacent to Solr/ChromaDB/Qdrant) ⚠️ | ✅/⚠️ S3 strong; others learnable |
| Data quality checks, validation, completeness | Entrata: baseline validation + reconciliation on every HUD release; AgentProbe: data completeness checks in eval pipeline | ✅ |
| PII/sensitive regulatory data handling | Entrata: 100% PHI compliance, Libsodium encryption, zero security incidents; HIPAA RBAC in AI on FHIR | ✅ Strong |
| Regulated financial/compliance environments | Entrata 8yr: HUD compliance, income eligibility, rent calculations — regulated housing sector | ✅ Adjacent |
| TDD for pipeline code | AgentProbe: CI-integrated regression gate, automated tests block deploys on quality drop | ✅ |
| Reranking, contextual retrieval, hybrid search strategies | LeaseI: TF-IDF + semantic reranking, hybrid search; continual improvement via AgentProbe eval | ✅ |
| Collaborate with agent developers | Exact workflow: I AM the agent developer AND the data engineer — built both LeaseI (agent) and AgentProbe (eval/retrieval) | ✅ |

**Gap analysis:**
1. AWS Lambda / Step Functions — not in stack; serverless orchestration is learnable from CI/CD + RabbitMQ background
2. AWS Bedrock — AWS's LLM API service; directly learnable from existing OpenAI/Anthropic API experience
3. Amazon OpenSearch — learnable from Solr/ChromaDB/Qdrant search experience

---

## C) Level and Strategy

| Dimension | Finding |
|-----------|---------|
| Title | Sr. AI Data Engineer — no penalty |
| What they need | Someone who can own RAG pipeline quality end-to-end: ingest → chunk → embed → retrieve → evaluate → improve |
| Her fit | AgentProbe is the eval framework. LeaseI is the RAG pipeline. Together they ARE this job description. |
| Strategy | Lead with: "I built the RAG pipeline AND the evaluation harness that measures its quality — that's the exact loop this role requires." |

---

## D) Comp and Demand

| Metric | Data |
|--------|------|
| Contract type | Long-term W2 contract through Unisys |
| **Suggested pay rate** | **$80–$90/hr W2** (Sr. AI Data Engineer, DC metro, GenAI/RAG specialization) |
| Notes | C2C rate would be $95–$110/hr if she has her own LLC. W2 is simpler on OPT. Recruiter asked — respond promptly with a specific number. |

---

## E) Customization Plan

| # | Section | Proposed change |
|---|---------|-----------------|
| 1 | Summary | Lead with RAG + ETL + eval angle: "AI Data Engineer who builds RAG pipelines and the evaluation infrastructure to measure their quality — AgentProbe (eval framework), LeaseI (hybrid search + chunking + retrieval), 8yr ETL at scale (AWS, RabbitMQ, 180K records)" |
| 2 | AgentProbe | Lead with: eval framework, retrieval precision/recall/relevance metrics, regression harness, golden datasets — satisfies their "evaluation benchmarks" requirement exactly |
| 3 | LeaseI | Frame as RAG pipeline: document chunking, hybrid search (TF-IDF + semantic reranking), vector retrieval, citation grounding — satisfies "RAG pipeline development" requirement |
| 4 | Entrata | Lead with: ETL pipeline design, data quality validation, AWS S3/Glue, RabbitMQ ingestion at scale, PHI compliance |
| 5 | Skills | Lead with AWS (S3, Lambda, Step Functions, Bedrock, OpenSearch), RAG, vector databases, hybrid search, TDD |

---

## F) Interview Plan

| # | JD Requirement | Story |
|---|----------------|-------|
| 1 | RAG pipeline — chunking, embedding, retrieval | LeaseI: section-aware chunking by document type, TF-IDF + semantic embedding reranking, ChromaDB vector retrieval with citation grounding to exact source clause. Iterated chunk size and overlap to improve F1 from ~80% to 87.9%. |
| 2 | Evaluation framework — precision, recall, relevance | AgentProbe: 5-metric engine with pass@k harness, golden datasets, regression gate. Evaluated LeaseI across 1,240 PDFs: 93.6% precision, 87.9% F1. CI blocks deploy if quality drops. |
| 3 | ETL pipelines at scale + data quality | Entrata: HUD income limit pipeline — federal rows → 180K domain records, baseline validation, reconciliation, rollback preparation every release. Wrong data = wrong eligibility decisions for thousands of residents. Data quality is non-negotiable. |
| 4 | AWS infrastructure | S3 (7yr production), Glue (ETL), RabbitMQ async (idempotency); Lambda/Step Functions and Bedrock learnable — same patterns as serverless orchestration I've designed. |
| 5 | PII / regulated data | 100% PHI compliance at Entrata (Libsodium encryption); HIPAA RBAC in AI on FHIR — I've owned regulated data pipelines where a breach has real consequences. |
| 6 | Improve retrieval quality continuously | AgentProbe + LeaseI feedback loop: I eval, find the drop, trace to the chunk/embed/retrieve stage, fix, re-eval. That loop is the job. |

---

## G) Posting Legitimacy

| Signal | Finding | Weight |
|--------|---------|--------|
| Company | Unisys — established IT services firm, not a sketchy shop | Positive |
| Recruiter | Named recruiter (Vinay Kumar) with title and company | Positive |
| Client unnamed | Actual client company not disclosed — standard for staffing firms | Neutral |
| Location | Specific DC metro locations (Rockville MD, McLean VA) — real offices | Positive |
| Duration | "Long-term contract" — no defined end date, implies ongoing engagement | Positive |
| No salary range | Contract — pay rate negotiated; recruiter asked for expected rate | Neutral |
| Word format request | Standard staffing firm practice (they reformat before sending to client) | Neutral |

**Assessment: Medium-High Confidence** — Real firm, real recruiter, real location. Client and comp not disclosed (standard for staffing). Verify client name in screening.

---

## H) Draft Reply to Recruiter

> Hi Vinay,
>
> Thank you for reaching out. I'm very interested in this Sr. AI Data Engineer role — it maps directly to work I've been doing: RAG pipeline development with hybrid search (TF-IDF + semantic reranking), document chunking and vector retrieval, and AI evaluation infrastructure (I built AgentProbe, an open-source eval toolkit that measures retrieval precision, recall, and quality across LLM pipelines).
>
> My expected rate is **$85/hr W2**.
>
> I'm authorized to work in the US on F-1 STEM OPT (valid through May 2029) and am available immediately.
>
> Please find my resume attached. Happy to connect at your earliest convenience.
>
> Best,
> Venkata Lakshmi Parimala Pasupuleti
> venkatalakshmiparimala@gmail.com | +1-703-261-5410

---

## Verdict

**4.5/5 — APPLY.**

This role IS AgentProbe + LeaseI in a production enterprise context. RAG pipeline + retrieval eval + ETL at scale = her three strongest proof points in one role. McLean, VA is commutable. Contract W2 is OPT-compatible. Reply to recruiter with resume + $85/hr W2 rate today.

---

## Keywords extracted

RAG pipeline, retrieval-augmented generation, document chunking, vector embeddings, hybrid search, reranking, contextual retrieval, OpenSearch, AWS Bedrock, AWS Lambda, AWS Step Functions, S3, ETL pipeline, data ingestion, knowledge stores, retrieval quality, evaluation framework, regression tests, golden datasets, precision, recall, relevance, TDD, test-driven development, PII, data quality, validation, Python, LLM, generative AI, agentic AI, ingestion workflows, unstructured data

## Machine Summary
```yaml
company: Unisys (staffing — client undisclosed)
role: Sr. AI Data Engineer
score: 4.5
archetype: AI Platform/LLMOps + Data Engineering (both primary)
level: Senior
comp_range: "Contract — suggested $85/hr W2"
location: Rockville MD / McLean VA (commutable from Virginia)
sponsorship: W2 contract OPT-compatible; H-1B sponsorship TBD — verify in screening
apply: YES — reply to recruiter today
top_proof_points:
  - AgentProbe (eval framework = their exact eval requirement)
  - LeaseI (RAG pipeline: chunking, hybrid search, vector retrieval, citation grounding)
  - Entrata 7yr ETL (180K records, AWS S3/Glue, data quality, PHI compliance)
key_gap:
  - AWS Lambda / Step Functions (learnable)
  - AWS Bedrock (learnable from existing LLM API experience)
  - Amazon OpenSearch (adjacent to Solr/ChromaDB)
```
