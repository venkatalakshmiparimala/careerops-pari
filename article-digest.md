# Article Digest — Proof Points

Detailed proof point expansions for use in CVs, cover letters, and evaluations.
Read this file alongside cv.md. Metrics here take precedence over cv.md when they conflict.

---

## LeaseI — Full Proof Point

**What it is:** AI-powered platform for affordable housing / LIHTC compliance operations. Three user-facing surfaces sharing one SQLite knowledge repository.

**Positioning statement:** An AI-powered document intelligence and support investigation platform that helps enterprise teams understand complex product knowledge, diagnose customer issues, and discover hidden dependencies across documents, settings, releases, and historical incidents — without allowing AI to make final regulated business decisions.

**Core design rule (enforced in code everywhere):** The LLM extracts and reasons; a human or deterministic logic makes every final eligibility, compliance, and financial call. Every answer is either cited or explicitly flagged as unsupported.

### Three surfaces

| Surface | What it does |
|---------|-------------|
| **Document Intelligence & Review** | Ingest leases, certification forms, policy docs; extract fields, answer questions with citations, diff document versions, flag missing/conflicting clauses |
| **Support Ticket & Root-Cause Investigation** | Classify a ticket, pull relevant business rules/settings/historical tickets, produce ranked evidence-backed root-cause hypotheses, escalate to human engineers when confidence is too low |
| **Tenant Self-Service** | Tenants get direct answers to document/policy questions; anything eligibility- or configuration-related always routes to staff — never resolved or explained by AI directly to a tenant |

### Architecture

```
Documents, manuals, tickets, release notes, HUD/LIHTC regs
                     │
             Ingestion + OCR fallback
          (pdfplumber, pytesseract, pdf2image)
                     │
            Chunking (section/clause-aware)
                     │
    TF-IDF retrieval (hand-rolled, hybrid+reranking as next target)
                     │
             SQLite knowledge repository
  (documents, chunks, settings, tickets, release notes, audit log)
                     │
  ┌──────────────────┼──────────────────────┐
  │                  │                       │
Phase 1:          Phase 3:              Tenant Agent:
Document Q&A   LangGraph 8-agent graph  wraps Phase 1+3,
(linear pipe)  + income limit API node  hard eligibility/
               + Config/History/         config boundary —
                 StructuredData agents   never auto-resolves
                                          for tenants
                     │
            Engineer Console (Streamlit)
    Ticket Investigation · Document Q&A · HUD Lookup · Settings
```

### Tech stack

| Layer | Tool |
|-------|------|
| Agent orchestration | LangGraph (StateGraph, real conditional edges) |
| RAG | Hand-rolled: regex-based chunking + scikit-learn TF-IDF + cosine similarity — no LangChain, no vector DB |
| API | FastAPI + Uvicorn |
| UI | Streamlit (Engineer Console) |
| Validation | Pydantic |
| Database | Python stdlib sqlite3, no ORM |
| PDF/OCR | pdfplumber, pytesseract, pdf2image |
| Live regulatory data | requests against the real HUD User API |
| Synthetic data | Faker, reportlab |

**Deliberately excluded:** LangChain, ORM, task queue, vector store, second LLM provider — each is a real requirement at a scale this project isn't at yet. Every architectural choice is intentional.

### Measured results

| Component | Result |
|-----------|--------|
| Phase 1 — Document Q&A | 100% citation correctness, 100% grounding, 0% unsupported-claim rate on eval set |
| Phase 3 — 8-agent investigation graph | Reproduces the exact spec worked example: correctly traces a false-ineligibility ticket to a misconfigured setting, tagged to the release that introduced it |
| Tenant Self-Service Agent | Safety boundary tested explicitly — never auto-resolves eligibility/config/calculation for a tenant, even at high confidence |
| HUD income-limit API client | Built against the real documented API; parsing verified against realistic canned response |
| Engineer Console (Streamlit) | 4 tabs, smoke-tested |
| API layer | 4 FastAPI endpoints, tested end-to-end |

### How to use this in applications

**For document intelligence / RAG roles:** Lead with Phase 1 results (100% citation correctness, 0% unsupported-claim rate) and the hand-rolled TF-IDF approach — signals understanding of retrieval fundamentals, not just "I called LangChain."

**For agentic / LangGraph roles:** Lead with Phase 3 — 8-agent StateGraph with real conditional edges, HITL escalation when confidence is too low, root-cause tracing across settings + release history.

**For compliance / regulated AI roles:** Lead with the core design rule: LLM reasons, human or deterministic logic decides every final regulated call. Tenant self-service safety boundary is a concrete example of this enforced in code.

**For PropTech / housing roles:** The domain — LIHTC, HUD, affordable housing income verification, lease compliance — is the differentiator. No generalist AI candidate has this combination.

---

## AgentProbe — Proof Point Summary

See cv.md for full details. Key signals for applications:
- 15-endpoint FastAPI backend
- 5-metric eval engine: factual accuracy, hallucination, retrieval, completeness, compliance
- LLM Router for dynamic tool routing across providers
- 3 LangGraph agents (Orchestrator, RAG Tracer, Auto Fix)
- Runs 100% locally at zero cost
- Live: github.com/venkatalakshmiparimala/AgentProbe

---

## Entrata — HUD Income Limits Pipeline (Anchor Story)

**What it is:** Annual federal data import system owned for nearly 7 years at Entrata, transforming HUD income-limit source data into domain records used by eligibility, rent, HAP, tax-credit, and document workflows for 100K+ housing units.

**The scale:** A few thousand federal source rows → ~180,000 domain records. Every record has to preserve jurisdiction mappings, household-size variants, effective dates, and historical correctness. One wrong import can trigger incorrect eligibility decisions and require mass document or calculation corrections affecting real residents.

**What ownership meant:**
- Transformation logic, stored procedures, data validation, deployment support, production debugging, and long-term maintenance
- Every release included pre-import baselines, reconciliation counts, effective-date checks, and rollback preparation
- Production debugging across stored procedures and data relationships when downstream modules behaved unexpectedly
- Zero compliance violations across 7 years of annual release cycles

**How to use in applications:**
- **Data engineering roles:** Lead with scale (180K domain records, ETL owned end-to-end) and reliability (7 years, zero compliance violations)
- **Backend/production engineering roles:** Lead with ownership depth — not just "wrote the import" but owned the validation, rollback, and post-release monitoring annually
- **Regulated domain roles:** The stakes (resident eligibility, HUD compliance) show experience with data where correctness isn't optional

---

## Entrata — SQL Performance Engineering

**What it is:** Long-term SQL optimization and database engineering across Entrata's Affordable Housing and property management modules.

**Key numbers:** 200+ SQL queries optimized, 30% average performance gain, multi-tenant production environment with complex schemas for eligibility, financial calculations, and document workflows.

**What the work actually involved:**
- Execution plan analysis — not just "add an index," but reading query plans and diagnosing why a plan was chosen
- Stored procedure engineering for set-based transformations (income limits, eligibility calculations, rent workflows)
- Indexing, partitioning, audit tables, caching strategies
- Production data debugging when calculations produced wrong outputs — finding the data cause, not just the code cause

**Core principle (from the work):** A fast query returning incorrect regulatory or financial data is a production failure, not an optimization. Speed and correctness are both first-class requirements.

**How to use in applications:**
- **Data engineering / analytics engineering roles:** Lead with the production ownership (not just query tuning, but owning the schema and debugging production data)
- **Backend SWE roles:** Lead with execution plan analysis and stored procedure depth — signals database-first engineering thinking

---

## Entrata — AWS S3 Document Migration

**What it is:** Affordable Housing module integration for a company-wide migration from legacy server storage to AWS S3.

**What it involved:** The organization-wide migration framework was owned by another team. Parimala owned the Affordable Housing module side — inventorying all document types, mapping legacy records to the framework's input contracts, handling edge cases the generic framework couldn't infer, validating migrated content and metadata, enabling QA, and confirming customer-facing workflows remained functional after cutover.

**PHI compliance:** Implemented Libsodium-encrypted pipelines encrypting 100% of resident data (phone numbers, SSNs); updated 50%+ of product codebase for encryption compliance; zero security incidents.

**Key lesson (from case study):** "Shared infrastructure creates leverage, but successful adoption depends on strong module ownership." The framework did the heavy lifting; the value was in supplying the correct module-specific mappings, edge cases, and acceptance criteria that defined correctness.

**How to use in applications:**
- **Cloud / AWS roles:** Concrete S3 production migration with validation, not a demo
- **Security / compliance roles:** PHI encryption end-to-end, 100% coverage, zero incidents

---

## Entrata — RabbitMQ Async Processing

**What it is:** Asynchronous processing system for annual gross-rent updates across thousands of tenant records.

**What the work involved:** Designed retry logic and idempotency guarantees that eliminated double-processing failures; owned the system through production incidents and annual rent-schedule changes. RabbitMQ enabled the gross-rent workflow to process tenant records without blocking or overloading the main application.

**How to use in applications:**
- **Backend / distributed systems roles:** Real async processing with retry and idempotency in a production regulated environment — not a tutorial project
