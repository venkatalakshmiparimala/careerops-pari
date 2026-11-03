# Evaluation: KPMG — Senior Engineer, Audit Technology Organization

**Date:** 2026-08-27
**URL:** (not provided — pasted as JD text; verify posting is active before submitting)
**Archetype:** AI Platform / LLMOps + Agentic / Automation (hybrid)
**Score:** 4.2/5
**Legitimacy:** Proceed with Caution
**PDF:** output/cv-venkata-lakshmi-parimala-pasupuleti-kpmg-2026-08-27.pdf

---

## A) Role Summary

| Dimension | Detail |
|-----------|--------|
| Archetype | AI Platform / LLMOps + Agentic / Automation (hybrid) |
| Domain | Enterprise audit AI (RAG, agents, eval framework for audit/tax workflows) |
| Function | Build — implement generative AI features, RAG pipelines, AI microservices |
| Seniority | "Senior Engineer" — min 3 years required; effectively mid-level by tech-company standards |
| Remote | Not specified; KPMG ATO roles are typically hybrid at US office locations |
| Team size | Not mentioned; ATO is KPMG's internal technology organization |
| TL;DR | Build and ship RAG pipelines, AI agents, and evaluation tooling inside KPMG's audit technology arm using Azure AI Search, Databricks, LangChain, Python, and Docker — with an explicit evaluation framework component that maps directly to AgentProbe. |

---

## B) Match with CV

| JD Requirement | CV Match | Quality |
|----------------|----------|---------|
| 3+ years SE, AI/data-intensive apps | 8+ years Entrata backend + GMU Research Associate + Magizhs AI internship | **STRONG** |
| Python + LangChain/LlamaIndex/Semantic Kernel | Python: core stack; LangChain + LangGraph: listed in AI & Agents skills; Context Engineering: listed explicitly | **STRONG** |
| RAG pipelines | LeaseI hand-rolled TF-IDF RAG (100% citation correctness); AgentProbe ChromaDB RAG eval | **STRONG** |
| Context engineering modules | "Context Engineering" listed explicitly in AI & Agents technical skills | **STRONG** |
| Enhanced evaluation framework | AgentProbe: 5-metric eval engine (correctness, groundedness, latency, token efficiency, hallucination), CI-integrated regression gate, 1,240+ test cases | **STRONG — direct proof point** |
| Unit tests, code reviews | 300+ peer code reviews at Entrata; CI-integrated regression gate in AgentProbe | **STRONG** |
| Agile, Git, CI/CD pipelines | 120+ Agile sprints at Entrata; GitHub Actions CI/CD in AgentProbe | **STRONG** |
| AI microservices, deploy/maintain | 15-endpoint FastAPI backend (AgentProbe); LeaseI FastAPI + Uvicorn | **STRONG** |
| MS degree preferred | MS Data Analytics Engineering, GPA 3.87, George Mason University (May 2026) | **STRONG** |
| Azure DevOps | GitHub Actions CI/CD only — not Azure DevOps specifically | **PARTIAL** |
| Cloud platforms — Azure | AWS primary (S3, EC2, RDS, Glue). Azure not featured in CV. | **GAP** |
| Azure AI Search | Not listed | **GAP** |
| Databricks | PySpark + Apache Spark listed in Technical Skills; Databricks itself not named | **PARTIAL** |
| Docker | Listed in CV: Cloud & Infrastructure skills | **MATCH** |
| Kubernetes | Not explicitly listed | **GAP** |

### Gaps and mitigations

| Gap | Blocker? | Mitigation |
|-----|----------|-----------|
| Azure vs AWS | No | Cloud concepts transfer. LangChain integrations are provider-agnostic. Frame as "cloud-agnostic RAG experience (AWS); familiar with Azure AI ecosystem." |
| Azure AI Search | No | Functionally equivalent to OpenSearch/pgvector. RAG retrieval expertise (TF-IDF, ChromaDB, cosine similarity) covers the fundamentals; ramp on managed Azure search is fast. |
| Databricks | No | PySpark listed — Databricks is managed Spark. Frame as "Spark/PySpark experience, familiar with Databricks as managed layer." |
| Kubernetes | Minor | Docker containerization is solid. K8s is a common mid-level gap; KPMG likely uses managed AKS — experience shipping containerized microservices covers the baseline. |
| Azure DevOps | No | GitHub Actions covers CI/CD intent. Azure DevOps boards = Jira equivalent. Mention "experienced with agile tooling; have used GitHub Actions for CI/CD." |

**Overall CV match score: 4.3/5** — strong technical alignment on the AI/ML layer; Azure ecosystem gap is real but not a blocker at this level.

---

## C) Level and Strategy

**Level detected:** "Senior Engineer" at KPMG ATO, minimum 3 years required. At a FAANG-style company this maps to L5/E5. At KPMG — a Big 4 professional services firm — ATO is an internal engineering org, not a product tech company. Interview process is typically competency-based + technical screen, not multi-round algorithmic loops. "3 years minimum" is effectively a mid-level experience bar.

**Profile flag applied:** "Senior at 200+ employee company" → −0.25 (reduced from −0.5). KPMG ATO is materially different from the companies where the rejection pattern was confirmed (AppFolio, Amazon, Juniper Square). Their leveling is experience-based, not title-based.

**"Sell at the right level" plan:**
- Lead with delivery metrics, not leadership framing. "I built and shipped" not "I led the architecture."
- Position the AgentProbe eval framework as direct experience with exactly what they call their "enhanced evaluation framework" — use their phrasing.
- 8 years of production engineering experience answers the seniority question with evidence; don't over-explain it.
- The "collaborate with senior engineers" framing suggests a contributor role — position as an implementer who owns quality end-to-end.

**"If they downlevel me" plan:**
- KPMG's official band in VA/DC: $106,800–$190,100. Even at a lower intra-band position, the floor exceeds your target.
- Accept if compensation is fair + visa sponsorship confirmed. Request 12-month review as a promotion checkpoint.

---

## D) Comp and Demand

| Location | Low | High | Source |
|----------|-----|------|--------|
| Tysons/McLean/Ashburn VA | $106,800 | $190,100 | KPMG pay transparency (job ID 8154_9_26) |
| Washington DC | $106,800 | $190,100 | KPMG pay transparency |
| Virginia Beach VA | $92,200 | $164,200 | KPMG pay transparency |
| Seattle/Bellevue WA | $126,200 | $224,600 | KPMG pay transparency |
| New York City | $111,700 | $198,700 | KPMG pay transparency |
| KPMG Engineering (general) | ~$141K–$194K (25th–75th pct) | — | ZipRecruiter/6figr 2026 |
| KPMG H-1B median salary filed | $99,000 | — | H1BGrader (1,471 LCA filings) |

**Realistic offer for this profile (Virginia/DC area):** $115K–$145K based on 8+ years experience + MS degree + AI specialization, within KPMG's published band.

**Target alignment:** Parimala's target range $80K–$140K; even the floor of $106K in VA/DC is above any floor. Score: **4.0/5**

**H-1B sponsorship:** KPMG LLP — 1,471 certified LCA filings, 97.2% approval rate. Active sponsor. One of the more reliable H-1B sponsors outside FAANG. Standard March lottery submission timeline.

**Demand trend:** Big 4 firms are investing heavily in AI for audit automation and advisory. KPMG ATO is a strategic internal build — this role exists specifically because they're trying to reduce audit headcount costs with AI tooling, which makes ATO hiring more stable, not less.

**Comp score: 4.0/5**

---

## E) Customization Plan

| # | Section | Current Status | Proposed Change | Why |
|---|---------|---------------|-----------------|-----|
| 1 | Professional Summary | PropTech/Entrata-first framing | Lead with AgentProbe eval framework + RAG production work. One sentence on audit/compliance domain (Entrata). Add "Azure AI ecosystem" as growth direction. | KPMG cares about evals + RAG + AI agents, not PropTech specifically. |
| 2 | Skills — AI & Agents | LangChain listed, no Azure mention | Surface as cluster: "LangChain, RAG Pipelines, Context Engineering, LLM Evaluation, LangGraph, Multi-Agent Orchestration." Add "Azure AI ecosystem (learning)." | Matches JD keywords exactly; covers the Azure gap honestly. |
| 3 | Skills — Cloud | AWS-first listing | Add "PySpark / Databricks-compatible" as explicit callout under Cloud & Infrastructure | Bridges the Databricks gap with existing PySpark listing. |
| 4 | Projects order | AgentProbe second | Move AgentProbe to #1 project. Lead bullet: "5-metric eval engine + CI-integrated regression gate across 1,240+ test cases" | Directly mirrors "enhanced evaluation framework" in JD — lead with the strongest match. |
| 5 | LeaseI bullets | 3-surface HITL platform framing | Open with "8-agent LangGraph orchestration pipeline" and "RAG pipeline achieving 93.6% precision on 1,240 compliance documents" | Maps to "AI agents and orchestration patterns" and "RAG pipelines" from JD requirements. |

**Top 5 LinkedIn changes:**
1. Headline: Add "LLM Evaluation | RAG Pipelines | AI Agents" to headline
2. About section: Mention AgentProbe eval framework with GitHub link as a headline project
3. Featured: Pin AgentProbe GitHub as top featured item (visible to recruiters)
4. Skills: Ensure LangChain, RAG, Context Engineering, LLM Evaluation are listed as top skills
5. Experience at Entrata: Add "CI/CD pipeline ownership" and "production microservices" phrasing to Senior SWE bullets

---

## F) Interview Plan

| # | JD Requirement | STAR+R Story | S | T | A | R | Reflection |
|---|---------------|-------------|---|---|---|---|-----------|
| 1 | Enhanced evaluation framework | AgentProbe 5-metric eval engine | AgentProbe had no systematic way to verify RAG answer correctness | Build a reusable evaluation toolkit any agent can plug into | Implemented 5 metrics (correctness, groundedness, latency, token efficiency, hallucination), CI gate, multi-provider LLM-as-judge scoring | 1,240+ test cases; pass@1 81.7%, pass@3 88.3%; CI regression gate catches regressions before merge | Would add per-agent-type regression baselines earlier; one threshold doesn't fit all task types |
| 2 | RAG pipelines | LeaseI Phase 1 (TF-IDF RAG) | Lease and compliance documents across 5 states — LLM answers were uncited and ungrounded | Build a RAG layer where every answer traces to an exact clause or is flagged as unsupported | Hand-rolled TF-IDF + cosine similarity, section-aware chunking, OCR fallback for scanned PDFs, human-review gate on regulated decisions | 100% citation correctness, 0% unsupported-claim rate, 100% grounding on Phase 1 eval set | Hand-rolling TF-IDF built deep retrieval intuition — next target: hybrid dense retrieval with embeddings reranking |
| 3 | AI agents / orchestration patterns | LeaseI 8-agent LangGraph (Phase 3) | Complex support tickets required cross-referencing business rules, settings, release history, and past tickets | Build an 8-agent investigation pipeline with conditional routing and HITL escalation | LangGraph StateGraph: Triage → Retrieval → Configuration → Historical Incident → Structured Data → Reasoning → Validation → Human Escalation agents | Correctly traces false-ineligibility ticket to misconfigured setting tagged to the exact release that introduced it | HITL confidence threshold is hard to calibrate — next would add human review at multiple decision points, not only final output |
| 4 | Agile sprint delivery | Entrata 120+ Agile sprints | HUD compliance deadlines are inflexible — regulatory release cycles repeat every year | Own the HUD income-limit import pipeline through annual cycles, from planning to post-release monitoring | Led requirement gathering, development, baseline validation, reconciliation, rollback preparation, and post-release debugging each year | Zero compliance violations across 7 years of annual release cycles | "Done" in regulated environments means evidence-backed: baseline before, reconciliation after, documented rollback — not just tests pass |
| 5 | Code quality / reviews | Entrata code review practice + debugging tools | High-volume team; bug count above threshold; debugging time was disproportionate to issue complexity | Implement structured review practices and internal debugging tooling | Built custom debugging tools; enforced review rubric; tracked bug count against sprint benchmarks | 40% reduction in debugging time; below 10 open bugs for 6+ consecutive months; 300+ peer reviews completed | Catching a wrong data mapping at review is 10x cheaper than catching it post-import — code review ROI compounds over time |
| 6 | AI microservices, deploy/maintain | AgentProbe FastAPI + Docker | Eval results scattered across scripts with no queryable API; no repeatable deployment | Build a 15-endpoint FastAPI backend + Docker packaging for evaluation workloads | Designed endpoint contracts, Pydantic validation, multi-provider LLM routing, Docker packaging, CI integration | Fully local, zero-cost, pluggable into any agent via API; CI gate integrated in GitHub Actions | Would add async task queue earlier — synchronous eval calls block on batch eval jobs; async would parallelize multi-agent scoring |

**Recommended case study:** **LeaseI** — covers RAG (Phase 1), multi-agent orchestration (Phase 3), evaluation via AgentProbe, and HITL design. Directly maps to every dimension KPMG ATO cares about. Lead with the three-surface architecture and the core design rule: "LLM reasons; human or deterministic logic makes every final regulated call" — this resonates strongly in an audit context.

**Red-flag questions and how to answer:**
- *"Do you have Azure experience?"* → "My production cloud is AWS, but my AI layer — LangChain, RAG retrieval, agent orchestration — is provider-agnostic by design. I've integrated LangChain's Azure OpenAI client and have been exploring Azure AI Search as a retrieval backend. The retrieval and orchestration fundamentals are solid; the managed services are a fast ramp."
- *"You've been at one company for 8 years. Can you adapt?"* → "Entrata was enterprise scale — 100K+ MAU, 120+ Agile sprints, multi-team microservices. I also built AgentProbe and LeaseI independently, from architecture through tested production-grade implementation. The adaptability is demonstrated in the projects, not just claimed."
- *"Your AI projects aren't company-deployed."* → "AgentProbe has a CI-integrated regression gate I use in production testing — 1,240+ test cases, multi-provider LLM-as-judge scoring. LeaseI has a FastAPI backend, Docker deployment, and end-to-end eval harness. These are engineered systems, not demos. The deployment context is self-hosted; the engineering rigor is the same."

---

## G) Posting Legitimacy

**Assessment: Proceed with Caution**

| Signal | Finding | Weight |
|--------|---------|--------|
| Posting age / date | No URL or date provided — JD was pasted as text. Cannot determine freshness. | Neutral |
| Apply button state | Not verifiable without URL | Neutral |
| JD tech specificity | High: LangChain, LlamaIndex, Semantic Kernel, Azure AI Search, Databricks, Docker, Kubernetes, Azure DevOps — specific and internally coherent stack | **Positive** |
| Requirements realism | "3 years minimum, MS preferred, BS required" — realistic bar. No contradictions (no "3 years of Kubernetes" type issues). | **Positive** |
| Salary transparency | Full pay transparency table published — 27 US cities with specific bands | **Positive** |
| KPMG layoffs 2026 | ~100 US audit partners cut (10% of audit division); 590 UK roles | Neutral — audit practitioners (licensed CPAs), not ATO tech engineers |
| H-1B LCA filings | 1,471 certified LCA filings, 97.2% approval — active tech hiring pipeline | **Positive** |
| "Rolling basis" hiring language | Standard KPMG boilerplate — could indicate evergreen posting or standard rolling intake | Neutral |
| Reposting pattern | No prior KPMG entries in scan-history.tsv | Neutral (no history) |

**Context notes:** The 2026 KPMG layoffs are concentrated in audit partners (licensed CPAs performing client audits) and UK advisory — a different labor category from ATO software engineers. KPMG is investing in audit AI specifically to offset audit headcount costs, which makes ATO hiring more stable. The specific and coherent tech stack (Azure AI Search, Databricks, LangChain, K8s) is inconsistent with a ghost posting. Primary uncertainty is the missing URL — confirm the posting is active before investing application effort.

---

## Keywords extracted

LangChain, LlamaIndex, Semantic Kernel, RAG pipelines, context engineering, Azure AI Search, Databricks, AI agents, orchestration, evaluation framework, Python, Docker, Kubernetes, Azure DevOps, CI/CD, generative AI, microservices, agile, unit tests, code reviews, scalable features, LLMOps, multi-agent, SDLC, Azure cloud, Big 4, audit technology

---

## Machine Summary

```yaml
company: KPMG
role: Senior Engineer, Audit Technology Organization
date: 2026-08-27
score: 4.2
archetype: AI Platform / LLMOps + Agentic / Automation
legitimacy: Proceed with Caution
recommend: apply
comp_low: 106800
comp_high: 190100
location: US (VA/DC area preferred; multiple cities)
h1b_sponsor: confirmed
key_gap: Azure ecosystem (Azure AI Search, Databricks, K8s)
key_strength: AgentProbe eval framework + LeaseI RAG + 8 years production engineering
```
