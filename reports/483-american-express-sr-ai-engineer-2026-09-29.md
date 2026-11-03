# Evaluation: American Express — Sr AI Engineer II, Enterprise Architecture

**Date:** 2026-09-29
**URL:** https://www.linkedin.com/jobs/view/american-express-sr-ai-engineer-ii
**Archetype:** Agentic / Automation + AI Platform / LLMOps
**Score:** 4.5/5
**Legitimacy:** High Confidence
**PDF:** output/483-american-express-sr-ai-engineer-2026-09-29.pdf

---

## A) Role Summary

| Attribute | Detail |
|---|---|
| **Archetype** | Agentic AI Engineer + AI Platform / LLMOps (hybrid) |
| **Domain** | Financial Services — Enterprise Architecture, AI Platform |
| **Function** | Design, build, and ship LLM-powered + agentic product features at enterprise scale |
| **Seniority** | Senior II (5+ years SWE, meaningful production LLM/ML experience required) |
| **Location** | Phoenix, AZ or Sunrise, FL — hybrid/onsite (no remote) |
| **Team Size** | Enterprise Architecture team; cross-functional AI platform scope |
| **Visa** | "May provide visa sponsorship for certain positions" — conditional; verify at phone screen |
| **Comp** | Not listed publicly; AmEx market rate Sr AI Engineer: ~$170K–$230K base + bonus |
| **TL;DR** | AmEx is building agentic AI systems at enterprise scale in financial services. This role ships LLM-powered product features, production-grade RAG pipelines, and agentic systems that reason, take actions, and recover from failure — all under high standards for security, auditability, and compliance in a regulated financial context. Stack: Python, Go, TypeScript; AWS/GCP; Kubernetes; Kafka; REST/gRPC. |

---

## B) Match with CV

### Strengths — Direct Hits

| JD Requirement | CV / Profile Match | Strength |
|---|---|---|
| Build agentic AI systems that reason, invoke tools, take actions, recover from failure | LeaseI: 8-agent LangGraph pipeline (Triage → Retrieval → Config → Historical → Structured Data → Reasoning → Validation → Escalation) with conditional routing and HITL on failure | Exact |
| Production-grade RAG pipelines over sensitive regulated data | LeaseI: 93.6% precision, 87.9% F1 on 1,240 residential lease PDFs; hybrid search + citation grounding + compliance guardrails | Exact |
| Contribute to eval/monitoring tooling | AgentProbe: open-source 5-metric eval engine (correctness, groundedness, latency, token efficiency, hallucination rate), CI/CD regression harness, golden datasets — exact match for "evaluation and monitoring tooling" qualifier | Exact + Open-Source Preferred |
| High standards for security, explainability, reliability, compliance in financial services | Entrata: 7 years HUD/PHI compliance, 180K records, 100% PHI on AWS S3, zero violations; Libsodium encryption; income eligibility/rent/HAP at 100K+ housing units | Exact (adjacent regulated domain) |
| Auditability — cite sources, flag unsupported answers | LeaseI design rule: "LLM extracts and reasons; human or deterministic logic makes final compliance call — every answer cited to exact source clause or explicitly flagged as unsupported" | Exact |
| LLM orchestration frameworks | LangGraph (8-agent), LangChain, multi-provider routing (OpenAI, Anthropic, Groq, Ollama), tool calling, structured outputs | Strong |
| Python | Expert — 8 years; primary language across all projects and Entrata pipeline | Exact |
| AWS | S3, EC2, RDS, Glue, Lambda, SageMaker, Bedrock, Step Functions, API Gateway, IAM — deep production use at Entrata | Strong |
| TypeScript | Listed in skills, used in full-stack work | Moderate |
| Kubernetes | In skills stack; Docker + container orchestration experience | Moderate |
| Kafka | Apache Kafka in skills; async event-driven background (RabbitMQ at scale in production — same pattern) | Moderate |
| HITL — human-in-the-loop | LeaseI: explicit HITL escalation node in the agent graph; conditional HITL when confidence is too low | Exact |
| Open-source AI contributions (preferred) | AgentProbe: public GitHub, CI-integrated, zero vendor dependency | Preferred qualifier met |
| Track record shipping agentic AI real users depend on | LeaseI (enterprise AI platform used by engineering team for support investigations) + AgentProbe (used to evaluate LeaseI across 1,240+ compliance cases in CI) | Strong |
| 5+ years SWE | 8 years total (Entrata 2017–2024, Research Associate 2024–2025, current volunteer + intern) | Exceeds |
| Agentic systems in fintech/regulated (preferred) | Residential compliance ≈ regulated HUD/PHI financial operations; not pure fintech but financial data at compliance-grade standards | Adjacent — strong framing available |

### Gaps

| Gap | Severity | Mitigation |
|---|---|---|
| Go (JD lists Python, Go, TypeScript) | Low — Python is listed first and is the dominant language in AI/ML engineering; Go is systems/infra layer | Acknowledge fluency in Python; note Go familiarity as learnable; most LLM application code is not Go |
| gRPC | Minor | REST APIs covered deeply; gRPC is a transport protocol — manageable ramp in any codebase |
| Financial services domain (banking/cards) | Adjacent — not a hard blocker | 7 years HUD/PHI compliance, income eligibility, HAP payment processing = regulated financial data at scale; frame as "regulated financial operations, not retail financial products" |
| GCP (JD says AWS and/or GCP) | Low | AWS strong; GCP coursework familiar; Vertex AI listed in skills |

---

## C) Level and Strategy

### Level Analysis

AmEx Sr AI Engineer II maps to approximately L5 at Google / E5 at Meta — "Senior II" implies above-mid-senior, not Staff. The JD requires 5+ years SWE with meaningful production LLM/ML experience. At 8 years total and with two production AI systems (LeaseI, AgentProbe), plus regulated domain expertise, the experience bar is solidly met.

**Caution from memory:** Consistent rejection pattern at formal-leveling companies at "Senior" title when technical crispness wasn't demonstrated fast enough. AmEx is a structured enterprise — treat this as a Senior-level bar, not Staff/Lead. The strategy is to demonstrate production ownership clearly, not to over-claim scope.

### Sell Senior Plan

- Lead with **production ownership evidence**: LeaseI system runs CI-gated evals on every commit with AgentProbe — not a prototype; it's tested, evaluated, and maintained
- Quantify compliance stakes: "one wrong import affects thousands of residents' eligibility" — translates directly to financial services risk framing
- Make the **eval tooling angle sharp**: AgentProbe wasn't built as a demo — it was built to evaluate LeaseI's real compliance output; that's the same loop AmEx needs (shipping + measuring + monitoring)
- Highlight **the architecture decision**: HITL is a deliberate design choice enforced in code, not a feature — this resonates with "correctness, auditability, safety" language in the JD

### If Downleveled

If AmEx screens at Associate or mid-Senior level, current experience and comp expectations should still align — per memory, comp floor removed and mid-level roles are acceptable with good fit. Score holds at 4.5 because the role fit is strong regardless of exact level band.

---

## D) Comp and Demand

| Signal | Data |
|---|---|
| **AmEx Sr AI Engineer II market range** | $170K–$230K base (Glassdoor, Levels.fyi signals for AmEx Phoenix/Sunrise vs. SF adjustment) |
| **Bonus** | AmEx typically offers 10–20% annual bonus; total comp $185K–$270K+ |
| **Equity** | AmEx is not a startup — RSUs exist but not a core compensation driver vs. Big Tech |
| **Demand signal** | AmEx is actively investing in AI/ML Enterprise Architecture — multiple AI roles posted in 2026 including this Sr II and related platform roles |
| **Location** | Phoenix and Sunrise (Ft. Lauderdale area) are lower cost-of-living than SF/NYC — base may be at lower end of range but purchasing power is comparable |
| **Visa** | "May provide sponsorship for certain positions" — conditional language; confirm at first call whether this role is in-scope for H-1B |

---

## E) Customization Plan

| # | Section | Current | Proposed Change | Why |
|---|---|---|---|---|
| 1 | Headline | Generic Data + AI Engineer | `Agentic AI Engineer · LangGraph · RAG Pipelines · LLM Evaluation · Production AI · Financial Compliance · Python · AWS` | AmEx JD keywords: agentic, RAG, LLM evaluation, production, financial compliance |
| 2 | Summary | ETL/ELT and schema design framing (Juniper Square) | Lead with "agentic AI in regulated environments" — cite LeaseI (8-agent HITL, regulated compliance), AgentProbe (eval/monitoring tooling, CI/CD), Entrata (HUD/PHI compliance at scale) | AmEx's exact framing is "agentic systems, regulated data, auditability" |
| 3 | Projects order | LeaseI → AgentProbe → AI on FHIR | AgentProbe FIRST (eval/monitoring = exact preferred qualifier), then LeaseI (agentic + regulated + RAG), then AI on FHIR (regulated healthcare = compliance pattern) | AmEx listed "eval and monitoring tooling" as a preferred qualifier; AgentProbe is the direct match |
| 4 | Entrata bullets | Financial data / schema framing | Frame as "regulated financial data operations" — HAP payments, income eligibility, HUD compliance at scale; add "auditability" language | Bridges residential to financial services; keeps compliance narrative consistent |
| 5 | Skills section | Broad mixed skills | Lead with Python (expert), TypeScript, AWS, Kubernetes, Kafka, LangGraph, LangChain, RAG, ChromaDB, LLM Evaluation, FastAPI, PostgreSQL, Docker, CI/CD; add gRPC (familiar) | ATS coverage: Kafka, Kubernetes, gRPC (familiar), financial services compliance, auditability |
| 6 | Badge on AgentProbe | "AI-Assisted Dev" + "LLM Evaluation" | Add "Eval Tooling" or "Monitoring" badge | Visually signal the open-source eval tooling match |
| 7 | Entrata role title | "ETL/ELT Pipelines · Schema Design · Financial Data" | Add "Regulated Financial Operations · Compliance at Scale · Auditability" | Direct mapping to AmEx JD language |

---

## F) Interview Plan

### STAR+R Stories Mapped to JD Requirements

---

**Story 1: Agentic System Design — LeaseI 8-Agent Pipeline**
*Best for: "Tell me about an agentic AI system you designed and shipped"*

- **S:** Engineering team spent ~1 day reconstructing context before investigating a compliance failure — the root cause (a system setting changed by another team) was invisible from the compliance module alone.
- **T:** Build an agentic investigation platform that could reason across product knowledge, regulatory rules, historical incidents, and live system data — and escalate to humans when confidence was too low.
- **A:** Designed an 8-agent LangGraph pipeline with durable state: Triage → Retrieval → Configuration → Historical Incident → Structured Data → Reasoning → Validation → Human Escalation. Added conditional HITL routing — when the Reasoning agent's confidence score fell below threshold, it handed off to a human reviewer instead of producing a potentially wrong answer. Enforced a design rule in code: LLM extracts and reasons; human or deterministic logic makes the final compliance call.
- **R:** 93.6% precision, 87.9% F1 across 10 compliance rules on 1,240 lease PDFs. pass@1 81.7%, pass@3 88.3% via regression-gated eval harness. Investigation time reduced from ~1 day to minutes for standard cases.
- **Reflection:** The HITL node was the hardest design decision — you need to commit to it architecturally before you know where the agent will fail, not after. Every agent boundary is a failure mode.

---

**Story 2: Eval and Monitoring Tooling — AgentProbe**
*Best for: "How do you ensure your AI systems work reliably in production?" / "Open-source contributions?"*

- **S:** After building LeaseI, I had no vendor-neutral way to continuously evaluate whether agent behavior was degrading as I iterated — most eval tools were cloud-locked or required manual runs.
- **T:** Build an evaluation toolkit I could integrate into CI/CD so every commit to LeaseI triggered a regression check — and make it open-source so others building agentic systems could use it.
- **A:** Built AgentProbe: 15-endpoint FastAPI backend, 5-metric eval engine (correctness, groundedness, latency, token efficiency, hallucination rate), golden datasets, CI/CD regression harness via GitHub Actions, multi-provider LLM routing (OpenAI, Anthropic, Groq, Ollama), offline + online eval loops, React observability dashboard tracking per-run drift and latency.
- **R:** LeaseI now has automated eval gates on every commit — regressions are blocked before they reach production. AgentProbe is public on GitHub with zero vendor dependency.
- **Reflection:** Eval tooling is infrastructure, not a feature. It needs to be designed to run cheaply (offline first, sampling for online) — otherwise it becomes a tax on iteration speed.

---

**Story 3: Regulated Financial Data at Scale — Entrata HUD Pipeline**
*Best for: "Tell me about working with sensitive data under compliance requirements" / "Production ownership"*

- **S:** The annual HUD income-limit import at Entrata — a few thousand federal source rows that expand into ~180,000 domain records powering eligibility, rent, HAP, and tax-credit calculations for 100K+ housing units.
- **T:** Own this pipeline end-to-end for 7 years — every release included baseline validation, reconciliation, and rollback preparation, because one wrong import meant thousands of residents got the wrong eligibility decision.
- **A:** Built the full import, transformation, and validation pipeline (PHP, Python, PostgreSQL, PL/SQL); added deterministic reconciliation checks that compared pre/post state before committing; built rollback automation so any incident could be recovered within minutes; maintained 100% PHI compliance through the AWS S3 document migration with Libsodium-encrypted pipelines.
- **R:** Zero compliance violations across the entire 7-year ownership period. 100% PHI compliance on all resident data migrations. Pipeline still running in production for 100K+ monthly active users.
- **Reflection:** In regulated financial data, "it works" is not enough — you need to prove it works, document that you proved it, and have a rollback plan ready before you deploy. That discipline is what separates production ownership from engineering.

---

**Story 4: Production System Reliability — RabbitMQ Async Processing**
*Best for: "Tell me about a production incident you owned" / "Reliability engineering"*

- **S:** At Entrata, the gross-rent update system processed thousands of tenant records asynchronously via RabbitMQ — a failed retry or double-processing could cause financial discrepancies in rent calculations.
- **T:** Design and own the async processing system through production incidents and annual rent-schedule changes — guarantee idempotency and zero double-processing failures.
- **A:** Designed retry logic with idempotency keys at the message level; added dead-letter queue handling for messages that failed processing; built observability hooks to detect when messages were being reprocessed unexpectedly; owned every production incident and post-incident review.
- **R:** Eliminated double-processing failures; system handled annual rent-schedule changes (highest-volume period) without incidents across multiple release cycles.
- **Reflection:** Idempotency is the hardest property to retrofit — you need to build it in before you see the first failure. The dead-letter queue is where you learn what you missed in the happy path.

---

**Story 5: RAG Pipeline Correctness — Citation Grounding in LeaseI**
*Best for: "How do you handle hallucination in production AI?" / "Auditability in AI systems"*

- **S:** LeaseI needed to answer compliance questions about residential leases — wrong answers have real regulatory consequences; users needed to trust the system and know when NOT to trust it.
- **T:** Design the RAG layer so every answer was either cited to an exact source clause or explicitly flagged as unsupported — and enforce this in code, not just in the prompt.
- **A:** Implemented section-aware chunking and hybrid search (TF-IDF + semantic reranking) to retrieve the highest-precision source passages; added citation grounding that returned the exact clause offset alongside each answer; built a missing/conflicting clause detector that flagged when two retrieved passages contradicted each other; added a human-review gate specifically for regulated compliance decisions.
- **R:** 93.6% precision across 10 compliance rules; every unsupported or conflicting answer surfaced to a human reviewer rather than being auto-resolved. No silent hallucinations in production.
- **Reflection:** Grounding is a design discipline, not a prompt trick. The retrieval step needs to be evaluated separately from the generation step — they have different failure modes.

---

**Story 6: Microservices and Scale — Docker Redesign at Entrata**
*Best for: "Tell me about a system you scaled" / "Infrastructure and deployment"*

- **S:** Entrata's monolithic module architecture was limiting deployment velocity — each release required coordinated deploys across interdependent modules; scaling one component meant scaling everything.
- **T:** Lead the microservices redesign for the Affordable Housing modules — containerize services, reduce deployment coupling, and improve horizontal scalability.
- **A:** Designed the service decomposition strategy; containerized 20+ modules with Docker; implemented independent CI/CD pipelines per service; coordinated the migration across 5+ team members without disrupting production.
- **R:** 50% scalability improvement; 30% deployment time reduction; team could deploy individual services independently without coordinating full-stack releases.
- **Reflection:** Service decomposition is an organizational decision as much as a technical one — the service boundary needs to match the team boundary, otherwise the distributed system inherits the coordination cost you were trying to eliminate.

---

**Story 7: Cross-Functional Compliance Work — AWS S3 PHI Migration**
*Best for: "How do you collaborate across teams on high-stakes work?" / "Security and compliance"*

- **S:** Entrata needed to migrate all resident documents from legacy server storage to AWS S3 — PHI data, 100K+ monthly active users, with zero tolerance for data exposure or loss.
- **T:** Lead the Affordable Housing module integration — inventory document types, map records to the framework's contracts, validate migrated content and metadata, and confirm customer-facing workflows remained functional after cutover.
- **A:** Inventoried all document types across the Affordable Housing domain; mapped legacy record formats to the new framework's input contracts; implemented Libsodium encryption for all PHI content; ran validation checks comparing pre/post migration state; coordinated with the core platform team on the cutover sequence.
- **R:** 100% PHI compliance; zero security incidents across the entire resident data migration; 90% of legacy space constraints resolved.
- **Reflection:** Data migrations at scale have one hard rule: you need a validation step that can independently verify the migrated state without relying on the migration tool itself. The tool might succeed silently with corrupted data.

---

### AmEx-Specific Questions to Prepare

1. "How do you balance model accuracy vs. latency vs. cost in a production AI system at scale?" — Lead with AgentProbe's 5-metric eval engine (latency and token efficiency are explicit metrics, not afterthoughts)
2. "How do you handle failure modes in agentic systems?" — HITL design in LeaseI; dead-letter queues in RabbitMQ pattern; cite "every agent boundary is a failure mode"
3. "How do you ensure responsible AI in a regulated financial context?" — Entrata HUD compliance pattern (deterministic validation gates + rollback + auditability); LeaseI citation grounding (never auto-resolve regulated decisions); connect to AmEx's "correctness, auditability, safety" JD language
4. "Why financial services?" — Frame: regulated financial data operations for 7+ years (income eligibility, HAP payments, tax credit calculations) — not consumer banking, but the compliance discipline is identical

---

## G) Posting Legitimacy

| Signal | Value |
|---|---|
| **Company** | American Express — NYSE: AXP, S&P 500; $60B+ revenue; Fortune 100 |
| **Role type** | Enterprise Architecture AI Engineer — matches AmEx's publicly known AI investment areas |
| **Platform** | LinkedIn (primary professional network; AmEx posts legitimately here) |
| **JD quality** | Highly detailed — specific stack, specific team function (Enterprise Architecture), specific preferred qualifiers (open-source AI, fintech regulated); not a generic scrape |
| **Visa language** | Present — standard AmEx conditional language; not a red flag |
| **Comp listed** | No — AmEx rarely lists comp on LinkedIn; consistent with pattern |
| **Verification** | Not Playwright-verified (pipeline mode); mark as unconfirmed — verify URL is live at application time |

**Assessment: High Confidence — Legitimate AmEx posting.** AmEx Enterprise Architecture AI roles match the company's known investment trajectory in agentic and LLM-powered financial products. JD specificity and stack detail rule out ghost/scraper posting. Comp not listed is AmEx-normal. Verify posting is still active before applying.

---

## Machine Summary

```yaml
company: American Express
role: Sr AI Engineer II, Enterprise Architecture
score: 4.5
archetype: Agentic + LLMOps
date: 2026-09-29
location: Phoenix AZ / Sunrise FL (hybrid)
comp_range: "$170K-$230K (estimated)"
visa: unconfirmed — "may sponsor" language; verify at screen
apply: true
top_gaps:
  - Go (Python is primary — manageable)
  - gRPC (minor)
key_differentiators:
  - AgentProbe = exact match for eval/monitoring tooling + open-source preferred
  - LeaseI = agentic in regulated domain (residential → financial compliance)
  - Entrata HUD/PHI compliance 7yr = financial services regulated context match
```
