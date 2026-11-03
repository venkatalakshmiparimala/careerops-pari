# Evaluation: Google — Technical Solutions Consultant / FDE, Google Maps Platform

**Date:** 2026-09-29
**URL:** https://careers.google.com/jobs/results/ (FDE Google Maps Platform)
**Archetype:** Agentic / Automation + AI Forward Deployed
**Score:** 4.4/5
**Legitimacy:** High Confidence
**PDF:** output/484-google-maps-fde-2026-09-29.pdf

---

## A) Role Summary

| Attribute | Detail |
|---|---|
| **Archetype** | Agentic AI Engineer + Forward Deployed Engineer (FDE) hybrid |
| **Domain** | Google Maps Platform — enterprise AI deployment on geospatial infrastructure |
| **Function** | Build, deploy, and co-architect production agentic AI applications with customer engineering teams using Google AI products (Gemini models, Vertex AI, Maps APIs) |
| **Seniority** | Mid-Senior — 5yr minimum; production AI systems required, not research or prototyping |
| **Location** | Mountain View CA / NYC / Seattle / SF — candidate's choice (hybrid) |
| **Team Size** | Google Maps Platform Solutions team; cross-functional with customer and product engineering |
| **Visa** | Google is a top H-1B sponsor — confirmed strong sponsorship record |
| **Comp** | $152K–$221K base + 15% bonus + equity |
| **TL;DR** | Google is hiring an FDE who can build complex production agentic AI systems using LangGraph, MCP servers, and Google AI products — and deploy them alongside customer engineering teams. This role is a builder FDE: rapid prototypes → production agentic workflows, evaluation pipelines, observability frameworks, reusable field patterns. Strong match on every technical qualifier via LeaseI (8-agent LangGraph) and AgentProbe (evaluation pipelines + observability). |

---

## B) Match with CV

### Strengths — Direct Hits

| JD Requirement | CV / Profile Match | Strength |
|---|---|---|
| 5yr Python | 8 years Python — primary language across all roles and projects | Exceeds |
| Production-grade AI solutions from conception to launch | LeaseI (FastAPI + LangGraph, 8-agent, production RAG pipeline, CI-gated evals); AgentProbe (open-source, CI/CD integrated, multi-provider) | Exact |
| Multi-agent systems using LangGraph / ReAct / hierarchical delegation | LeaseI: 8-agent LangGraph StateGraph (Triage → Retrieval → Configuration → Historical Incident → Structured Data → Reasoning → Validation → Human Escalation) — hierarchical delegation with conditional routing | Exact — Preferred Qual Met |
| Vector databases + RAG pipelines for enterprise AI | LeaseI: ChromaDB, hybrid search (TF-IDF + semantic reranking), citation grounding, 93.6% precision on 1,240 lease PDFs | Exact — Preferred Qual Met |
| Build evaluation pipelines and observability frameworks for agentic systems | AgentProbe IS this: 5-metric eval engine (correctness, groundedness, latency, token efficiency, hallucination rate), CI/CD regression harness, golden datasets, React observability dashboard with per-run drift and latency tracking, LangSmith tracing | Exact — Responsibility Match |
| LLM-native metrics (tokens/sec, cost-per-request, latency) | AgentProbe: token efficiency and latency are explicit first-class metrics in the eval engine, not afterthoughts | Exact — Preferred Qual Met |
| Develop rapid prototypes → production agentic workflows (MCP servers, multi-agent) | Magizhs: agentic LangGraph mission-planning system (parse → plan → retrieve → validate → conditional routing) shipped from prototype to operational use; LeaseI: same builder pattern at larger scale | Strong |
| Convert repeatable field patterns into reusable modules | AgentProbe: built because LeaseI needed repeatable eval infra — extracted into reusable open-source toolkit; same "field pattern → reusable module" behavior | Strong |
| M.S. or PhD in AI/CS (preferred) | M.S. Data Analytics Engineering, George Mason University, GPA 3.87, May 2026 | Preferred Qual Met |
| Architect connective tissue between Google AI products and customer infrastructure | Entrata: 7 years integrating enterprise systems (AWS S3 migration, RabbitMQ async, multi-tenant architecture, PHI-compliant pipelines) — demonstrates integration engineering muscle | Strong Adjacent |
| Co-build with customer engineering teams | Research Associate (faculty collaboration on multi-source pipelines); TA (600+ students); Magizhs intern (stakeholder-driven agentic system) | Adjacent |

### Gaps

| Gap | Severity | Mitigation |
|---|---|---|
| Google Maps Platform / geospatial domain | Low-Moderate — role is AI deployment on GMP, not GIS expertise | Role explicitly requires AI engineering skills; GMP is the deployment surface, not the domain expertise required; Mapbox listed in skills as adjacent geospatial context |
| Customer-facing technical discovery sessions | Moderate — not primary background | TA role (600+ students, debugging support, cross-section coordination) and stakeholder-driven project work at Magizhs provide adjacent evidence; frame as "technical co-build partner" |
| Google interview bar (multi-round in-person loop) | Process risk, not fit risk | Prepare for coding + system design + behavioral; interview prep report recommended |

---

## C) Level and Strategy

### Level Analysis

Google TSC/FDE at this scope maps to approximately L4–L5 depending on team. The JD requires 5yr Python and production AI — at 8 years total with two production AI systems (LeaseI, AgentProbe) plus enterprise-scale backend experience (Entrata 7yr), the experience bar is solidly met.

**Memory context:** Strategy shift to mid-level + FDE roles at 4.0+ threshold; this is exactly that. Apply at 4.4. Avoid overclaiming scope — present as production builder who ships, not as Staff-level architect.

### Sell Senior FDE Plan

- Lead with **AgentProbe as the evaluation pipeline**: this is the exact responsibility listed in the JD. The hiring manager will recognize immediately that building eval infra is the hardest part of FDE work.
- Frame **LeaseI as the multi-agent proof**: 8-agent LangGraph with hierarchical delegation and HITL is the exact preferred qual — name the pattern (ReAct-adjacent, hierarchical delegation, conditional routing).
- Anchor on **builder identity**: "I don't just advise customers on AI architecture — I build the working system alongside them." Magizhs intern role demonstrates this FDE pattern: stakeholder request → prototype → agentic system → production delivery.
- **Geospatial gap is not a blocker**: explicitly acknowledge it as a new domain and frame the strength: "I learn deployment surfaces fast; the AI engineering patterns are the same regardless of whether the API surface is a property management system or a Maps endpoint."

### If Google Loop Is Multi-Round Formal

Per memory, consistent rejection pattern at formal-leveling companies when technical crispness wasn't fast enough. Google loop is rigorous. Prioritize:
1. Coding: Python + LangGraph agent graph construction (StateGraph, tool calling, conditional routing)
2. System design: RAG pipeline architecture + eval/observability layer
3. Behavioral: FDE-specific (customer co-build, translating field patterns to product feedback)

---

## D) Comp and Demand

| Signal | Data |
|---|---|
| **Base range** | $152K–$221K (listed in JD) |
| **Bonus** | 15% target (listed in JD) |
| **Equity** | RSUs — Google standard; expect $50K–$150K/year depending on level |
| **Total comp estimate** | $190K–$290K total at midpoint-to-top of range |
| **Demand signal** | Google Maps Platform is actively growing its AI deployment practice — GMP + Gemini integration is a core 2026 product initiative |
| **Location** | SF / NYC / Seattle / Mountain View — all tier-1 markets; base reflects market rate |
| **Visa** | Google is the #1 or #2 H-1B sponsor in the US by volume — confirmed strong; H-1B process well-established |

---

## E) Customization Plan

| # | Section | Current | Proposed Change | Why |
|---|---|---|---|---|
| 1 | Headline | Generic AI Engineer | `Forward Deployed AI Engineer · LangGraph Multi-Agent · MCP Servers · RAG Pipelines · LLM Evaluation · Agentic Workflows · Production AI · Python · AWS` | Hits FDE identity + all JD keywords in one line |
| 2 | Summary | Compliance/regulated framing | Lead with builder FDE identity: (1) LeaseI 8-agent LangGraph multi-agent system, (2) AgentProbe evaluation pipelines + observability, (3) Entrata enterprise production scale. Note M.S. pref qual. | Google JD's core ask is "builder FDE who ships production agentic AI" |
| 3 | Projects order | AgentProbe first (AmEx format) | LeaseI FIRST (8-agent, multi-agent, HITL, RAG — hits every preferred qual), then AgentProbe (evaluation pipelines + observability = exact JD responsibility), then Magizhs (FDE builder pattern) | Google JD preferred quals are multi-agent systems first; evaluation second |
| 4 | Skills | Compliance/financial framing | Lead: Python (expert), LangGraph, LangChain, Multi-Agent Systems, MCP, RAG Pipelines, Vector Databases (ChromaDB, Qdrant), LLM Evaluation, Observability, LLM-native metrics (token efficiency, latency, cost-per-request), FastAPI, TypeScript, AWS, Docker, Kubernetes, Kafka | ATS coverage for all JD keywords |
| 5 | Magizhs bullet | Generic agentic | Reframe as FDE builder pattern: stakeholder request → rapid prototype → production agentic workflow → operational deployment | Matches "rapid prototypes to production agentic workflows" responsibility |
| 6 | Skills — Google stack | Missing | Add: Vertex AI, GCP, Google Maps APIs (familiar), Gemini models | Signal awareness of Google's stack; list as "familiar/target" |

---

## F) Interview Plan

### STAR+R Stories Mapped to JD Requirements

---

**Story 1: Multi-Agent System Design — LeaseI 8-Agent LangGraph**
*Best for: "Tell me about a multi-agent system you designed and shipped"*

- **S:** Engineering team spent ~1 day reconstructing context before investigating a compliance failure — the root cause (a system setting changed by another team) was invisible from the compliance module alone.
- **T:** Build a multi-agent investigation platform using LangGraph that could reason across product knowledge, regulatory rules, historical incidents, and live system data — with hierarchical delegation and conditional HITL escalation.
- **A:** Designed an 8-agent LangGraph StateGraph with durable state: Triage → Retrieval → Configuration → Historical Incident → Structured Data → Reasoning → Validation → Human Escalation. Each agent had a specific bounded responsibility (hierarchical delegation pattern). Added conditional routing — when the Reasoning agent's confidence fell below threshold, it routed to Human Escalation rather than producing a potentially wrong answer. Enforced design rule in code: LLM extracts and reasons; human or deterministic logic makes the final compliance call.
- **R:** 93.6% precision, 87.9% F1 across 10 compliance rules on 1,240 lease PDFs. pass@1 81.7%, pass@3 88.3% via AgentProbe regression-gated eval harness. Investigation time reduced from ~1 day to minutes for standard cases.
- **Reflection:** Agent boundary design is a failure mode design. Every handoff is where things go wrong — you need to define the contract at each boundary before you write the first agent.

---

**Story 2: Evaluation Pipelines and Observability — AgentProbe**
*Best for: "How do you ensure agentic AI systems work reliably in production?" / "Tell me about evaluation infrastructure you built"*

- **S:** After building LeaseI, I had no vendor-neutral way to continuously evaluate whether agent behavior was degrading as I iterated — existing eval tools were cloud-locked or required manual runs outside the dev loop.
- **T:** Build an evaluation toolkit integrated into CI/CD so every commit to LeaseI triggered a regression check — and make it open-source so field engineers building agentic systems could reuse the infra.
- **A:** Built AgentProbe: 15-endpoint FastAPI backend, 5-metric eval engine (correctness, groundedness, latency, token efficiency, hallucination rate — all LLM-native metrics), golden datasets, CI/CD regression harness via GitHub Actions, multi-provider LLM routing, offline + online eval loops, React observability dashboard tracking per-run drift and latency in real time, LangSmith tracing integration.
- **R:** LeaseI now has automated eval gates on every commit — regressions blocked before reaching production. AgentProbe is public on GitHub with zero vendor dependency.
- **Reflection:** Eval tooling is the connective tissue between prototype and production. Without it, you don't know if your agent got better or worse between commits.

---

**Story 3: FDE Builder Pattern — Magizhs Agentic Mission Planning**
*Best for: "Tell me about a time you built a rapid prototype that became a production system" / "How do you work with non-technical stakeholders?"*

- **S:** Marketing, real estate, and commercial survey stakeholders needed a way to turn natural-language survey requests into compliant drone flight plans — manually planning each mission took significant time and required regulatory expertise.
- **T:** Build an agentic system that could parse stakeholder requests, generate structured flight plans, enforce regulatory compliance, and block non-compliant missions before export.
- **A:** Built a LangGraph stateful graph (parse → plan → retrieve → validate → conditional routing); implemented RAG layer over FAA Part 107 + operational-guidance corpus with cited compliance checks; engineered validation guardrails enforcing altitude limits, battery budgets, and geometric no-fly-zone checks; non-compliant missions blocked with grounded rejection reasons before MAVLink/QGroundControl export.
- **R:** Delivered a fully operational agentic system that converted unstructured stakeholder input into compliant, export-ready flight plans — with every compliance check functioning as a hypothesis test grounded in source regulation.
- **Reflection:** The FDE pattern is: understand the stakeholder's real problem (not the stated request), prototype fast with LLMs handling the ambiguous parts, validate rigorously with deterministic checks on the high-stakes parts.

---

**Story 4: RAG Pipeline Correctness — Citation Grounding in LeaseI**
*Best for: "How do you handle hallucination in production AI?" / "How do you design RAG for enterprise data?"*

- **S:** LeaseI needed to answer compliance questions about residential leases — wrong answers have real regulatory consequences; users needed to know when to trust the system and when NOT to.
- **T:** Design the RAG layer so every answer was either cited to an exact source clause or explicitly flagged as unsupported — enforced in code, not just in the prompt.
- **A:** Section-aware chunking and hybrid search (TF-IDF + semantic reranking) for precision retrieval; citation grounding returning exact clause offsets; missing/conflicting clause detector flagging contradictions in retrieved passages; human-review gate on all regulated compliance decisions.
- **R:** 93.6% precision across 10 compliance rules; every unsupported or conflicting answer surfaced to a human reviewer rather than auto-resolved. No silent hallucinations in production.
- **Reflection:** In enterprise RAG, retrieval quality determines everything. The generation step can't fix bad retrieval — you need to evaluate the retrieval layer independently from the generation layer.

---

**Story 5: Production Scale and Enterprise Reliability — Entrata HUD Pipeline**
*Best for: "Tell me about production ownership at enterprise scale" / "How do you ship reliable systems?"*

- **S:** The annual HUD income-limit import at Entrata — federal source rows expanding into ~180,000 domain records powering eligibility, rent, HAP, and tax-credit calculations for 100K+ housing units.
- **T:** Own this pipeline end-to-end for 7 years with zero compliance violations.
- **A:** Built import, transformation, and validation pipeline (PHP, Python, PostgreSQL, PL/SQL); deterministic reconciliation checks comparing pre/post state before committing; rollback automation for any incident; 100% PHI compliance on AWS S3 document migration with Libsodium-encrypted pipelines.
- **R:** Zero compliance violations across 7-year ownership. 100% PHI compliance on all migrations. 99.5% uptime. Pipeline running in production for 100K+ MAU.
- **Reflection:** Enterprise reliability means having a rollback plan ready before you deploy — and a validation step that can independently verify state without relying on the migration tool itself.

---

### Google-Specific Questions to Prepare

1. "Why Google Maps Platform specifically?" — Frame: GMP + Gemini is a concrete AI deployment surface; the FDE role is about building AI that runs on top of geospatial APIs, not GIS expertise; my background is in AI system construction and evaluation, which translates directly to any API surface.
2. "How do you design observability for a multi-agent system?" — Lead with AgentProbe: per-run metrics, retrieval drift detection, latency tracking, LangSmith tracing integration — not just logging but structured metrics that tell you which agent is the bottleneck.
3. "Walk me through a reusable pattern you extracted from field work" — AgentProbe story: built to solve a one-off problem (LeaseI eval), extracted into a reusable open-source toolkit — same "convert field pattern into reusable module" behavior the JD explicitly asks for.
4. "How do you handle state management in a long-running agentic workflow?" — LeaseI durable state: LangGraph StateGraph persists intermediate results across agent hops; conditional routing based on confidence state; HITL escalation preserves full context for the human reviewer.
5. "Google interview prep" — If this progresses, run `/career-ops interview-prep` with Google Maps Platform FDE context.

---

## G) Posting Legitimacy

| Signal | Value |
|---|---|
| **Company** | Google (Alphabet Inc.) — NASDAQ: GOOGL; $300B+ revenue; #1 H-1B sponsor |
| **Role type** | Technical Solutions Consultant / FDE, Google Maps Platform — matches Google's known AI-in-maps initiative |
| **Platform** | careers.google.com — official Google careers portal |
| **JD quality** | Highly detailed — specific stack (LangGraph, MCP servers, ADK, ReAct, CrewAI), specific responsibilities (evaluation pipelines, observability frameworks, agentic workflows), specific preferred quals (multi-agent systems, LLM-native metrics, M.S./PhD); not a generic scrape |
| **Comp listed** | Yes — $152K–$221K base + 15% bonus; atypical transparency for Google; increases legitimacy signal |
| **Visa** | Google is the #1 or #2 H-1B sponsor in the US by annual filings — confirmed strong |
| **Verification** | Not Playwright-verified (pipeline mode); mark as unconfirmed — verify URL is live at application time |

**Assessment: High Confidence — Legitimate Google posting.** comp range transparency, stack specificity, and Google careers platform origin rule out ghost/scraper posting. H-1B sponsorship is Google's documented practice at scale. Verify posting is still active before applying.

---

## Machine Summary

```yaml
company: Google Maps Platform
role: Technical Solutions Consultant / FDE
score: 4.4
archetype: Agentic + FDE
date: 2026-09-29
location: Mountain View / NYC / Seattle / SF (hybrid)
comp_range: "$152K-$221K + 15% bonus + equity"
visa: confirmed — Google top H-1B sponsor
apply: true
top_gaps:
  - Google Maps Platform / geospatial domain (new — role is AI deployment, not GIS)
  - Customer-facing discovery sessions (adjacent experience)
key_differentiators:
  - AgentProbe = evaluation pipelines + observability (exact responsibility match)
  - LeaseI = 8-agent LangGraph multi-agent (exact preferred qual match)
  - LLM-native metrics in AgentProbe (token efficiency, latency, cost-per-request)
  - MS Data Analytics Engineering meets preferred Master's qual
```
