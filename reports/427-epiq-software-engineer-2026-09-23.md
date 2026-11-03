# Evaluation: Epiq AI Labs — Software Engineer

**Date:** 2026-09-23
**URL:** (pasted JD — no public URL provided)
**Archetype:** AI Platform / LLMOps + Agentic / Automation (hybrid)
**Score:** 4.4/5 *(updated: VA office confirmed, +0.3 location boost applied)*
**Legitimacy:** High Confidence
**PDF:** ✅ output/cv-venkata-lakshmi-parimala-pasupuleti-epiq-2026-09-23.pdf

---

## A) Role Summary

| Dimension | Details |
|-----------|---------|
| **Archetype** | AI Platform / LLMOps + Agentic/Automation hybrid |
| **Domain** | Legal AI platform — enterprise legal departments + global law firms |
| **Function** | Build + own orchestration runtime, RAG layer, and eval infrastructure |
| **Seniority** | Mid-level (5+ yr SWE + 1yr LLM in production — no "Senior" in title) |
| **Work model** | Hybrid, **3–4 days/week in office** (location not stated — likely NYC or Chicago; verify in screening) |
| **Comp** | $195K–$255K + bonus eligible |
| **Sponsorship** | Unconfirmed — Epiq is a large global company (established H-1B filer probable; verify in screening) |
| **TL;DR** | Exceptional comp ($195K–$255K) + exact stack match (Python/LangGraph/RAG/RabbitMQ/evals). Core concern: 3–4 days in office at unknown location (likely not VA/DC). Score boosted by LangGraph/evals alignment. Apply if office is DC-metro or within reasonable distance. |

---

## B) Match with CV

| JD Requirement | CV Evidence | Match |
|---|---|---|
| 5+ years SWE backend/distributed/AI | 8+ years at Entrata (backend, distributed, data pipelines) | ✅ Strong |
| 1+ year LLM systems in production | Magizhs (LangGraph mission-planning system, May–Aug 2025) + AgentProbe + LeaseI | ⚠️ Borderline (Magizhs was unpaid intern; projects are production-grade but self-built) |
| Agentic architectures + orchestration frameworks | LeaseI: 8-agent LangGraph StateGraph with real conditional edges + HITL; AgentProbe: 3 LangGraph agents | ✅ Direct match |
| RAG systems at scale | AgentProbe: ChromaDB + embeddings; LeaseI: hand-rolled TF-IDF over 1,240 lease PDFs (5 US states) | ✅ Strong |
| Python production proficiency | 8+ years Python at Entrata + all AI projects in Python | ✅ |
| Evaluating agentic system accuracy/performance | AgentProbe: 5-metric eval engine (correctness, groundedness, latency, token efficiency, hallucination); pass@k harness; LLM-as-judge | ✅ Strongest differentiator |
| Design services + APIs consumed by other teams | FastAPI 15-endpoint backend in AgentProbe; 20+ production modules at Entrata consumed by other product areas | ✅ |
| Observability: Prometheus, Grafana, OpenTelemetry | "Observability", "Agent Tracing" in skills; Docker/K8s — but no Prometheus/Grafana/OTel specifically | ⚠️ Gap — transferable concepts, not named tools |
| Containerized cloud (Docker, K8s, Azure) | Docker + K8s + Azure in cv.md Technical Skills | ✅ |
| System design + TDD documentation | 20+ full-stack modules at Entrata; cross-team schema ownership; HUD pipeline owned end-to-end | ✅ |
| RabbitMQ (tech stack) | **Production ownership**: designed retry logic + idempotency guarantees for gross-rent async processing at Entrata | ✅ Rare differentiator — most AI candidates have zero RabbitMQ |
| Qdrant (tech stack) | Uses ChromaDB — same vector DB concept, different library | ⚠️ Minor gap |
| Solr (tech stack) | Not in her stack | ⚠️ Gap — has PostgreSQL full-text, Redis, TF-IDF retrieval |
| PostgreSQL | 200+ SQL queries optimized, complex schemas at Entrata | ✅ |
| Fine-tuning / model adaptation (preferred) | GMU coursework: HuggingFace Transformers + PyTorch custom classification model, deployed on Quart, presented to faculty | ✅ (academic; real implementation) |
| Large-scale data pipelines (preferred) | HUD income-limit pipeline: few thousand federal rows → 180K domain records; AWS Glue, S3 | ✅ |
| Multi-tenant SaaS + data isolation (preferred) | Entrata: multi-tenant production environment for 100K+ MAU; PHI encryption with Libsodium | ✅ |
| Startup / scale-up env (preferred) | No startup experience; Entrata is mid-size PropTech | ⚠️ Minor |
| Legal tech / enterprise workflow (preferred) | Compliance/regulated domain (HUD, LIHTC, PHI, HIPAA-adjacent); LeaseI = legal compliance AI | ✅ Adjacent — stronger than generic |
| Technical consulting / solutions eng background (preferred) | Not in CV | ⚠️ |

### Gaps and Mitigation

| Gap | Severity | Mitigation |
|-----|----------|-----------|
| Prometheus/Grafana/OTel not named | Soft | "Observability" + Agent Tracing + DockerK8s signals the concept; state "familiar with observability patterns, expanding into specific tooling" |
| Solr | Soft | Has TF-IDF retrieval in LeaseI + Postgres full-text; Solr learning curve is days |
| Qdrant vs ChromaDB | Trivial | Same paradigm; swap in screen or cover letter |
| LLM in production at company (not self-built) | Medium | Magizhs unpaid intern (real system, deployed); address directly: "I ship systems, not demos — here's the eval harness" |
| Startup experience | Soft | Magizhs internship + solo project ownership closes this gap functionally |

---

## C) Level and Strategy

| Dimension | Finding |
|-----------|---------|
| JD level | Mid-level ("5+ years" — not "Senior") |
| Title check | "Software Engineer" — no formal Senior title → no penalty applied |
| Epiq company size | ~5,000 employees globally — large company, has formal leveling |
| Her natural level | Mid / Senior-adjacent for backend SWE; Mid for AI systems (1 year LLM depth) |
| Risk | Title is not Senior so formal-leveling penalty does NOT apply — cleared |

**Strategy:** Lead with production ownership depth (RabbitMQ, HUD pipeline, multi-tenant schemas) + agentic eval infrastructure (AgentProbe). The combination of RabbitMQ production ops + LangGraph agentic systems + eval tooling is genuinely rare for this role's tech stack.

**If downleveled:** Role is already mid-level — unlikely to downlevel further. If comp comes in at $195K floor, that's still excellent.

---

## D) Comp and Demand

| Metric | Data |
|--------|------|
| JD range | $195K–$255K annually + bonus |
| Her target | $100K–$140K |
| Score | **5.0/5** — more than doubles her target ceiling |
| Comp vs market | AI/LLMOps platform engineer at enterprise: $160K–$230K market (2026). Epiq is above market. |
| Bonus | "May be eligible for annual bonus" — upside beyond base |

---

## E) Customization Plan

| # | Section | Current | Proposed | Why |
|---|---------|---------|----------|-----|
| 1 | Summary | Generic AI/backend framing | Lead with: RabbitMQ production ownership + LangGraph agentic systems + eval infrastructure (AgentProbe) — hits all 3 JD pillars | All 3 are in Epiq's tech stack or JD requirements |
| 2 | Projects order | LeaseI → AgentProbe | Keep order; add explicit "8-agent LangGraph orchestration runtime" phrasing | Maps to "Design the agentic platform" requirement |
| 3 | AgentProbe | Current description | Add: "evaluation infrastructure with golden datasets, regression gate, LLM-as-judge — run as CI harness" | Maps directly to "Build evaluation infrastructure" JD req |
| 4 | Entrata experience | RabbitMQ mentioned briefly | Expand: "Owned RabbitMQ async processing system — designed retry logic and idempotency guarantees for annual gross-rent updates across thousands of tenant records" | RabbitMQ is in Epiq's tech stack; almost no AI candidate has this |
| 5 | Skills | Standard list | Add: Qdrant (adjacent: ChromaDB), highlight Azure, K8s, PostgreSQL, RabbitMQ at top | Matches Epiq's exact tech stack section |

Top 3 LinkedIn changes:
1. Headline: Add "LangGraph • RabbitMQ • AI Eval Infrastructure" 
2. Featured: Pin AgentProbe repo (shows eval tooling = core JD req)
3. About: Mention production async systems (RabbitMQ) + AI eval harness (AgentProbe)

---

## F) Interview Plan

| # | JD Requirement | Story | S | T | A | R | Reflection |
|---|----------------|-------|---|---|---|---|------------|
| 1 | Design agentic platform with orchestration + durable state | LeaseI 8-agent LangGraph — Triage → Retrieval → Config → Historical → StructuredData → Reasoning → Validation → HITL | Customer appeared ineligible; cause invisible | Trace root cause across code + settings + tickets + release history | Built 8-agent LangGraph StateGraph with real conditional edges and confidence-based HITL escalation | Phase 3: correctly traces false-ineligibility to misconfigured setting + release tag | Design upfront: LLM reasons, deterministic logic decides regulated calls |
| 2 | Build evaluation infrastructure + regression harnesses | AgentProbe: 5-metric eval engine, pass@k harness, CI gate, LLM-as-judge | No standard eval framework for multi-LLM agents at zero cost | Build CI-integrated eval that runs locally | 5-metric engine + regression gate + multi-provider routing | LeaseI evaluated across 1,240 lease PDFs; 93.6% precision, 87.9% F1 | Golden datasets should reflect real failure modes, not synthetic happy paths |
| 3 | Build scalable backend + RabbitMQ async | Entrata gross-rent update async processing | Annual rent changes trigger thousands of tenant record updates; blocking was not an option | Design RabbitMQ-based system with retry logic + idempotency | Eliminated double-processing failures; owned through production incidents annually | System survived 7 years of annual rent cycles without redesign | Idempotency is the most important property — retry without it is worse than no retry |
| 4 | Multi-step reasoning + recovery from partial failure | LeaseI HITL escalation | Low-confidence retrieval results on complex tickets | Define confidence threshold triggering human escalation vs autonomous resolution | Conditional routing in LangGraph: if confidence < threshold → escalate, else proceed | Zero false-positive escalations on eval set; tenant safety boundary never broken | Partial failure during long-running execution needs explicit state checkpointing, not just error handling |
| 5 | RAG with hybrid search + citation grounding | LeaseI Phase 1 document Q&A | Legal compliance requires every answer traceable to exact source | Build TF-IDF retrieval with citation pinning (not just chunk return) | Hand-rolled TF-IDF + cosine similarity, section-aware chunking, citation map | 100% citation correctness, 0% unsupported-claim rate on eval set | Hand-rolling retrieval teaches you what LangChain abstracts away — important for debugging production failures |
| 6 | Model-operations: routing, latency, cost budgets | AgentProbe LLM Router | Testing across OpenAI/Anthropic/Groq/Ollama required consistent routing logic | Route dynamically based on task type + cost constraint | LLM Router with multi-provider routing; latency + token efficiency as eval metrics | Zero-cost local operation at full quality (Ollama) | Cost and latency are first-class eval dimensions, not afterthoughts |

**Recommended case study to present:** AgentProbe + LeaseI together — "I built the eval infrastructure (AgentProbe) and the AI system being evaluated (LeaseI) simultaneously, which gave me a deep feedback loop between what the system does and how well it's actually working."

**Red-flag questions:**
- "Why does your LLM experience come from projects, not a company?" → "Magizhs was production deployment (LangGraph system, real client context). LeaseI is eval'd on 1,240 real lease documents across 5 states — these aren't demos, they're systems with test harnesses and regression gates."
- "You don't have Prometheus/Grafana on your CV" → "I've implemented observability at the agent level (AgentProbe traces latency, hallucination rate, token efficiency per-run). Prometheus/Grafana are the deployment layer I'm adding — the instrumentation mindset is already there."

---

## G) Posting Legitimacy

| Signal | Finding | Weight |
|--------|---------|--------|
| Salary range disclosed | $195K–$255K explicitly stated | Positive |
| Tech specificity | High — names Qdrant, Solr, RabbitMQ, PostgreSQL, OTel | Positive |
| Team context | "Epiq AI Labs" named as innovation hub; role clearly scoped | Positive |
| Company legitimacy | Epiq: large legal services company (~$600M revenue, ~5,000 employees, global operations) | Positive |
| Requirements realism | 5+ years SWE + 1yr LLM — realistic for the scope | Positive |
| Recent layoffs | Not known — large enterprise; legal services sector is stable | Neutral |
| Reposting | Not in scan-history — first appearance | Neutral |
| H-1B sponsorship | **Unconfirmed** — large multinational, likely established H-1B sponsor; verify in screening | Neutral |
| No URL provided | JD pasted directly — cannot verify apply button state | Neutral |

**Assessment: High Confidence** — Real opening at an established company with specific tech requirements. Verify H-1B sponsorship and office location before investing time.

---

## H) Verdict + Recommended Action

**Score: 4.4/5** *(VA office confirmed — +0.3 location boost applied)*
**Threshold check:** 4.5+ required for non-PropTech/FDE roles → **below threshold by 0.1**

**Office location confirmed: Virginia** — zero relocation, immediate start, score boosted from 4.1 → 4.4.

**Borderline apply — strong case for override:**
- $195K–$255K is the highest-comp role evaluated to date
- RabbitMQ production ownership — exact tech stack match, most AI candidates have zero RabbitMQ
- AgentProbe = their eval infrastructure requirement (golden datasets, regression harnesses, offline/online eval loops)
- LeaseI 8-agent LangGraph = their orchestration runtime requirement
- VA office = no relocation cost

**Recommendation:** Run a 5-minute check to find the specific office location (check Epiq careers page or LinkedIn company page). If DC/VA/MD area → apply immediately. If NYC or Chicago → user decides whether relocation is acceptable given the exceptional comp.

---

## Keywords extracted

LangGraph, agentic orchestration, RAG, hybrid search, LLM evaluation, evaluation infrastructure, golden datasets, regression harness, LLM-as-judge, Python, FastAPI, RabbitMQ, Qdrant, PostgreSQL, Docker, Kubernetes, Azure, OpenTelemetry, Prometheus, Grafana, multi-tenant, legal AI, legal technology, HITL, human-in-the-loop, agent observability, production LLM, durable state, orchestration framework, retrieval-augmented generation, citation grounding, model routing, prompt versioning, context versioning

## Machine Summary
```yaml
company: Epiq AI Labs
role: Software Engineer
score: 4.1
archetype: AI Platform / LLMOps + Agentic/Automation
level: Mid
comp_range: "$195K-$255K"
location: Hybrid 3-4 days office (location unconfirmed)
sponsorship: Unconfirmed (likely — large global company)
apply: Conditional — verify office location first
top_proof_points:
  - AgentProbe eval infrastructure (5-metric engine, regression gate)
  - LeaseI 8-agent LangGraph orchestration runtime
  - RabbitMQ production ownership at Entrata (rare differentiator)
key_gaps:
  - Prometheus/Grafana/OTel not named (concepts present)
  - Solr (minor — has TF-IDF + Postgres FTS)
  - LLM in production at company (Magizhs intern + self-built projects)
```
