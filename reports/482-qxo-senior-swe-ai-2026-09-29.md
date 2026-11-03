# Evaluation: QXO — Senior Software Engineer, AI

**Date:** 2026-09-29
**URL:** careers@QXO.com (no public URL in JD)
**Archetype:** Agentic / Automation + AI Platform / LLMOps
**Score:** 4.4/5
**Legitimacy:** High Confidence
**PDF:** output/482-qxo-senior-swe-ai-2026-09-29.pdf

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| **Archetype** | Agentic / Automation (primary) + AI Platform / LLMOps (secondary) |
| **Domain** | Applied AI / Enterprise automation — building products distribution |
| **Function** | Build (production AI agents, eval frameworks, CI/CD for LLM systems) |
| **Seniority** | Senior (3–7+ years required, flexible) |
| **Remote** | Not specified — pay transparency wording suggests specific state; likely remote or hybrid |
| **Comp** | $150K–$220K + variable compensation |
| **Team** | Acquisition Engineering (Sales, Marketing, Onboarding) — QXO Marketplace |
| **TL;DR** | Build and deploy production AI agents for Sales/Marketing automation at N. America's largest building products distributor, using the exact stack — LangChain, MCP, LangGraph, eval harnesses — that Parimala already runs in production. |

QXO (founded by Brad Jacobs, former XPO/GXO chairman) is targeting $50B revenue through aggressive tech-led differentiation in an industry it describes as ripe for modernization. This role is the AI engineering layer powering that transformation. The JD is technically specific, realistic, and the use cases (BOM generation, CRM automation, quoting agents) are real operational problems.

---

## B) Match with CV

### Required Qualifications

| JD Requirement | Match | CV Evidence |
|----------------|-------|-------------|
| 3–7+ years SWE/MLE/AI Engineer | ✅ Strong | 8+ years: Entrata (2017–2024), Blue Horse (2026–), Magizhs (2025), GMU RA (2024–2025) |
| Production AI agents / LLM applications | ✅ Strong | LeaseI: 8-agent LangGraph pipeline in production; Magizhs: agentic drone mission planner with LangGraph |
| LangChain / OpenAI/MCP / LlamaIndex | ✅ Strong | LangChain, LangGraph, MCP — all listed in Skills (cv.md:16) |
| Python or TypeScript/Node | ✅ Strong | Python (primary), TypeScript, Node.js — all in Skills (cv.md:16) |
| LLMs + external tools + vector DBs + retrieval | ✅ Strong | AgentProbe: multi-provider routing (OpenAI/Anthropic/Groq/Ollama); ChromaDB, Qdrant, Pinecone; TF-IDF hybrid search in LeaseI |
| CI/CD + Docker + cloud (AWS/GCP/Azure) | ✅ Strong | GitHub Actions CI/CD, Docker, AWS S3/EC2/Lambda, Azure (ADF/ADLS), GCP — all in Skills |
| Automated testing / eval harnesses for LLM apps | ✅ Exact | AgentProbe IS an eval harness: 5-metric engine, golden datasets, regression gates, CI-integrated LLM-as-judge scoring |

### Preferred Qualifications

| JD Preference | Match | CV Evidence |
|---------------|-------|-------------|
| MCP servers / custom toolchains | ✅ | MCP listed explicitly in Skills (cv.md:16) |
| Building industry background | ✅ Partial | Entrata: PropTech / affordable housing / real estate SaaS (8 years) — construction-adjacent |
| Sales/Marketing RevOps (Salesforce, HubSpot, Outreach) | ❌ Gap | No direct experience — see mitigation below |
| Workflow engines (Airflow, Prefect) | ✅ | Apache Airflow listed in Skills (cv.md:22) |
| Vector / search / retrieval systems | ✅ Strong | ChromaDB, Qdrant, Pinecone, hybrid search, semantic search, reranking, contextual retrieval (cv.md:18) |
| Prompt engineering / RLHF / eval frameworks | ✅ Strong | Prompt Engineering, RLHF, LLM-as-judge scoring, AgentProbe 5-metric eval engine |
| LlamaIndex | ❌ Gap | Not in CV — minor; LangChain/LangGraph are direct alternatives |

### Gap Analysis

**1. Sales/Marketing CRM domain (Salesforce, HubSpot, Outreach)**
- Hard blocker? No. The JD weights agentic architecture skills over domain expertise.
- Mitigation: Frame LeaseI's 8-agent investigation pipeline as architecturally equivalent — it routes real-world support tickets through the same pattern: triage → retrieve → reason → escalate. Replacing "lease documents" with "CRM records" and "compliance rules" with "sales playbooks" is a configuration change, not an architectural one.
- Cover letter phrase: "My agentic work in compliance has the same core pattern as your sales agent use cases: ingest domain data, reason over it, take a next-best action, escalate when confidence is low. The domain changes; the architecture doesn't."

**2. LlamaIndex**
- Hard blocker? No. LlamaIndex and LangChain/LangGraph are equivalent in the market.
- Mitigation: One line in cover letter: "I primarily use LangChain/LangGraph, which covers the same orchestration patterns as LlamaIndex — I can get up to speed on LlamaIndex specifics quickly."

**3. Building products domain (roofing, insulation, BOM generation, pricing)**
- Hard blocker? No. Entrata is PropTech (property management, affordable housing) — same industry adjacency (real estate, construction, building).
- Mitigation: "8 years shipping production software in a specialized regulated domain — affordable housing compliance — is the closest any candidate has to your domain. The patterns of domain-specific agent tooling are the same."

---

## C) Level and Strategy

**Level detected:** Senior SWE, AI. 3–7+ years required (flexible for seniority). Parimala has 8+ years. Senior title penalty removed 2026-09-23. No conflict.

**Natural level for this archetype:** Strong Senior. The agentic AI work (LeaseI, AgentProbe) is genuinely senior — production deployment, eval harnesses, HITL design — not junior tutorial work.

**"Sell senior without lying" plan:**

Lead with the meta-engineering signal: AgentProbe. She didn't just *use* LangChain — she *built an evaluation toolkit for agentic systems*. That's the level above "I shipped an agent." At the interview:
1. Open with: "The thing I'd bring here that's different is I've built both the agent and the harness that validates it. Most candidates have built agents. Fewer have built the CI/CD infrastructure that gates them."
2. For the "agentic workflows for sales automation" requirement → present LeaseI Phase 3 as the architectural template: 8-agent LangGraph graph with conditional routing, HITL escalation, and confidence-gated output. Replacing the domain is trivial.
3. For "develop internal libraries and standardized patterns" → AgentProbe IS that library. It already standardizes eval, routing, and observability patterns for agentic systems.

**"If they downlevel":**
If QXO pushes for a lower title due to non-traditional background (no FAANG or prior SWE/AI title explicitly on LinkedIn):
- Accept if base is ≥ $150K
- Negotiate 6-month review with promotion criteria tied to shipped agents (measurable output, not subjective performance)
- Request clear criteria: "If I ship 3 production agents in the first 6 months, what does promotion to Senior look like?"

---

## D) Comp and Demand

| Source | Data |
|--------|------|
| QXO offering | $150K–$220K base + variable compensation |
| Senior AI Engineer market (2026, US) | $180K–$280K base; $220K–$350K+ TC (Levels.fyi, kore1.com) |
| LangGraph specialist median | $209.5K US median (agentic-engineering-jobs.com, 2026) |
| Agentic AI premium | $200K–$320K TC, growing 136% YoY (presenc.ai, 2026) |

**Assessment:** QXO's range ($150K–$220K) is on the lower end of the 2026 market for senior agentic AI engineers. At a traditional industry company (not FAANG, not a pure-tech AI startup), this is expected — they offset with stability, equity, and operational scale exposure. The top of the range ($220K) is competitive. Parimala's target ($100K–$140K) is below even the floor of this posting — this is above-target compensation. Score: 4.5/5.

**Variable compensation:** Not specified. Could be a bonus multiplier (5–20% of base) — ask at offer stage.

---

## E) Customization Plan

### CV Changes (Top 5)

| # | Section | Current Status | Proposed Change | Why |
|---|---------|---------------|-----------------|-----|
| 1 | Summary | "agentic AI support investigation platform" + "5-metric eval engine" | Add "MCP servers," "CI/CD eval harnesses," and "enterprise workflow automation" as explicit terms | JD's three core requirements: agents + eval + automation |
| 2 | AgentProbe | "CI-integrated 5-metric eval engine" | Lead with "CI/CD pipeline for LLM-powered systems with eval harnesses, scenario simulation, and regression detection" — match JD's exact language | Direct match to "Build CI/CD pipelines for model-related code and agent-specific behavior" |
| 3 | LeaseI | "3-surface enterprise AI knowledge platform" | Add "multi-step autonomous workflows with production observability and HITL escalation" framing | Mirrors JD's "agentic workflows that can operate autonomously, perform multi-step reasoning" |
| 4 | Skills header (AI & Agents) | Long list | Move MCP, LangGraph, Eval Harnesses, Agentic AI, HITL to positions 1–5 in the AI & Agents section | ATS keyword matching for top JD terms |
| 5 | Magizhs | "agentic mission-planning system" | Add "production-ready agent with compliance validation guardrails and RAG layer" — emphasize the build-validate-deploy cycle | Matches "Package and deploy agents into production environments with attention to reliability, observability" |

### LinkedIn Changes (Top 5)

| # | Field | Change |
|---|-------|--------|
| 1 | Headline | Add "AI Agent Systems | LLM Evaluation | MCP" |
| 2 | About | Add sentence: "I build production AI agents and the evaluation harnesses that keep them reliable — specializing in LangChain, LangGraph, MCP, and CI-integrated LLM evals." |
| 3 | Featured | Pin AgentProbe GitHub repo as first Featured item |
| 4 | Skills | Add "Model Context Protocol (MCP)," "AI Agent Development," "LLM Evaluation" as top skills |
| 5 | Magizhs experience | Add "agentic workflow automation" and "production agent deployment" as keywords |

---

## F) Interview Plan

### STAR+R Stories (6 mapped to JD)

| # | JD Requirement | Story | S | T | A | R | Reflection |
|---|----------------|-------|---|---|---|---|------------|
| 1 | Agentic workflows for multi-step reasoning | **LeaseI Phase 3 — 8-agent support investigation** | Support investigations took a full day; root cause (misconfigured setting by another team) was invisible to anyone looking only at the compliance module | Build an agentic system that traces root causes autonomously over enterprise documents, configs, and release history | 8-agent LangGraph StateGraph (Triage → Retrieval → Configuration → Historical Incident → Structured Data → Reasoning → Validation → Human Escalation) with conditional HITL when confidence <80% | Correctly traces false-ineligibility ticket to a misconfigured global setting + release tag; 93.6% precision on 1,240 compliance test cases | The hardest part was defining the escalation threshold — too high and everything routed to humans, too low and the system was overconfident on complex tickets. Confidence scoring is a product decision, not just a technical one. |
| 2 | CI/CD for LLM-powered agent systems + eval harnesses | **AgentProbe — CI-integrated LLM eval engine** | Teams building on LLMs had no reliable way to catch hallucination, groundedness, or latency regressions before production | Build a CI-integrated eval harness that gates production deploys on agent quality | FastAPI backend, 5-metric LLM-as-judge (factual accuracy, hallucination, retrieval, completeness, compliance), golden datasets with regression gates, GitHub Actions integration, Orchestrator + RAG Tracer + Auto Fix agents | Runs 100% locally at zero vendor cost; used to validate LeaseI across 1,240+ test cases; regressions caught and fixed before production 3+ times | The LLM-as-judge prompt engineering was harder than the application prompts. The eval judge needs to be calibrated against known-good and known-bad outputs first — it can't gate production until you've verified it catches the failure modes you actually care about. |
| 3 | Monitor agents in production, iterate on improvements | **Entrata RabbitMQ — async processing with idempotency** | Gross-rent updates across thousands of tenant records were producing double-processing failures under retry conditions | Eliminate double-processing in an async regulated system without disrupting annual rent-schedule cycles | RabbitMQ async processing with idempotency keys and retry logic; owned the system through production incidents and annual changes | Zero double-processing incidents after deployment; system ran reliably across 7+ annual rent-schedule release cycles | Production async systems need both retry logic AND idempotency — retry without idempotency makes the failure mode worse, not better. This is a lesson that can't be taught from first principles; you have to see the failure to believe it. |
| 4 | Integrate agents with enterprise APIs, databases, operational infrastructure | **LeaseI — ingestion pipeline for enterprise documents** | Enterprise compliance documents came in 12+ formats, mixed quality, inconsistent section markers | Build a reliable ingestion pipeline that handled all formats without manual preprocessing per file | pdfplumber + pytesseract OCR fallback, regex-based section-aware chunking, TF-IDF retrieval, confidence scoring on citations; validated against real HUD income-limit API | 100% citation correctness, 0% unsupported-claim rate on eval set | I chose hand-rolled TF-IDF over LangChain's retriever — at 1,240 documents, a vector DB was overkill, and TF-IDF was more debuggable. Scale the tool to the problem, not the other way around. That design decision directly enabled the citation correctness result. |
| 5 | Develop internal libraries and standardized patterns for agentic applications | **AgentProbe — open-source eval toolkit architecture** | Evaluating LLM applications was done ad hoc across projects — no standardized methodology, no reusable tooling | Design a reusable eval library that worked across different agent architectures (RAG, multi-agent, single-model) | 15-endpoint FastAPI backend with provider-agnostic LLM routing (OpenAI, Anthropic, Groq, Ollama), pluggable eval metrics, model routing logic separated from eval logic for reuse; 3 LangGraph agents for orchestration, RAG evaluation, and auto-fixing | Library reused across LeaseI and Magizhs evaluations without modification to core eval logic; zero vendor dependency enables cost control in CI | Making the routing layer provider-agnostic was the highest-leverage architectural decision. Teams that depend on a single LLM provider are one API change away from a broken eval pipeline. |
| 6 | Partner with Sales/Marketing/Ops to translate business processes into agentic flows | **Entrata: 80% manual workload elimination via automation** | Multiple operational teams were manually running regulatory workflows (gross-rent, income limits, document validation) — each cycle took hours and introduced error on regulated data | Automate regulated workflows without introducing compliance risk or requiring ops teams to change their mental model | Python/Bash pipelines for bulk updates; stored-procedure automation for income-limit imports with pre/post reconciliation; RabbitMQ async processing with retry/idempotency; internal debugging tools adopted team-wide | 80% of manual operational workload eliminated; zero compliance violations across all cycles; team debugging time cut by 40% | Automation on regulated data needs a validation gate, not just a scheduler. Silent failures (wrong outputs that don't throw errors) are the hardest problem; the gate that catches them is more valuable than the automation itself. |

### Recommended Case Study to Present

**AgentProbe** — strongest proof of the meta-engineering signal. The key talking point: "I didn't just build an agent — I built the CI/CD infrastructure that validates agents. That's the difference between a demo and a production system." Walk them through: the 5-metric eval engine → CI integration → how it blocked a regression in LeaseI → why the LLM-as-judge prompt calibration was the hardest part.

Present the GitHub repo live: [github.com/venkatalakshmiparimala/AgentProbe](https://github.com/venkatalakshmiparimala/AgentProbe)

### Red-Flag Questions

**"You don't have direct sales/marketing CRM experience."**
> "The agent architecture patterns — multi-step reasoning, tool calling, RAG over domain data, HITL escalation when confidence is low — are domain-agnostic. I've applied them in compliance and property management. CRM integration (Salesforce API, HubSpot webhooks) is a new domain, but the agent engineering methodology I've built translates directly. LeaseI's investigation pipeline and your sales agent use cases have the same shape: ingest domain records, reason over them, produce a next-best action, escalate when uncertain."

**"You've only worked at one company for 8 years."**
> "That's fair. What it also means is that I shipped 20+ production modules at scale, owned systems through 7+ annual release cycles, and understood the full operational lifecycle of software — not just the green-field build. The agents I'm building now have production monitoring, regression gates, and rollback plans because I've seen what happens when systems don't have them."

**"Are you comfortable with the building products industry?"**
> "I spent 8 years shipping software for affordable housing and property management — a highly regulated, operationally complex real estate domain. The building products distribution space is the upstream of what I worked in. I'm not learning a foreign industry; I'm shifting one step earlier in the same supply chain."

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Posting freshness | No date in JD; contact email provided (careers@QXO.com) — direct contact is a positive signal | Positive |
| Apply button | Not assessable (JD pasted; no URL provided) — needs manual verification via careers.qxo.com | Neutral |
| Description quality | Highly specific: names LangChain, LlamaIndex, MCP, Airflow, Prefect, MLflow, Flyte, Salesforce, HubSpot, Outreach, Docker, AWS/GCP/Azure — not boilerplate | Positive |
| Requirements realism | 3–7+ years flexible; specific use cases (BOM generation, quoting, CRM integration) — internally consistent | Positive |
| Salary transparency | Explicitly provided ($150K–$220K) — positive signal | Positive |
| Company hiring signals | No layoffs found; Brad Jacobs stepped down from XPO/GXO boards Dec 2025 to focus full-time on QXO; analyst commentary confirms "high-profile tech hires" | Positive |
| H-1B sponsorship | 0 LCA filings on record — but QXO is a brand-new company (incorporated 2023–2024); XPO/GXO (parent companies) have extensive H-1B history | Neutral (new company artifact) |
| Reposting | No prior QXO entries in scan-history.tsv | Positive |
| Role-company fit | QXO is explicitly targeting AI-led modernization as a core strategic differentiator; this role is the execution layer for that strategy | Positive |

**Context Notes:**
- QXO is a genuinely new company (Brad Jacobs' newest build), acquiring Beacon Roofing Supply and building a technology stack from scratch. The 0 H-1B filings are not a policy signal — they're an artifact of the company's age. Historically, Brad Jacobs' companies (XPO, GXO) are major H-1B sponsors.
- **Action required:** Verify H-1B sponsorship availability at first recruiter contact. Parimala's negotiation script: "I'm on F-1 STEM OPT, which provides 3 years of work authorization. Can you confirm QXO sponsors H-1B petitions?"
- JD contact: careers@QXO.com — reach out directly if no portal link available.

---

## H) Draft Application Answers

*(Score 4.4/5 — drafted for apply stage)*

**"Describe your experience building AI agents in production."**
> I've built two production agentic systems end-to-end. LeaseI is a three-surface compliance AI platform with an 8-agent LangGraph pipeline — it takes a support ticket, runs it through triage, retrieval, configuration, and historical-incident agents, and produces ranked root-cause hypotheses with HITL escalation when confidence falls below threshold. AgentProbe is an open-source LLM eval toolkit with a 5-metric eval engine, golden dataset regression gates, and CI integration — it's the harness I used to validate LeaseI across 1,240+ compliance test cases. Both are live on GitHub.

**"What frameworks and tools do you use for agentic systems?"**
> LangChain and LangGraph for orchestration, FastAPI for APIs, ChromaDB and Qdrant for vector retrieval, and the Anthropic/OpenAI/Groq APIs for model calls. I also implement MCP for tool integration. For evaluation, I built my own harness (AgentProbe) rather than relying on third-party eval platforms — it runs 100% locally with zero vendor dependency.

**"How do you ensure reliability and observability in production AI agents?"**
> Three ways: (1) CI-integrated eval harnesses that run before every deploy — if a metric drops below threshold, the deploy is blocked; (2) LLM-as-judge scoring with calibrated prompts to catch hallucinations and groundedness failures; (3) HITL escalation gates in the agent graph itself — when confidence is below threshold, the agent escalates rather than guessing. I learned from production experience at Entrata that silent failures (wrong outputs that don't throw errors) are the most dangerous failure mode in regulated systems.

---

## Keywords Extracted

LangChain, LlamaIndex, LangGraph, MCP, Model Context Protocol, agentic workflows, multi-step reasoning, LLM orchestration, AI agents, eval harness, CI/CD for LLM, agent evaluation, production AI, observability, HITL, human-in-the-loop, vector database, RAG, retrieval-augmented generation, prompt engineering, Python, TypeScript, FastAPI, Docker, AWS, Kubernetes, CI/CD, GitHub Actions, Airflow, Salesforce, HubSpot, CRM automation, building products, BOM generation, quoting automation, enterprise automation, sales automation, MLflow, LLM evaluation

---

## Machine Summary

```yaml
company: QXO
role: Senior Software Engineer, AI
date: 2026-09-29
score: 4.4
archetype: Agentic/Automation + AI Platform/LLMOps
status: Evaluated
comp_range: "$150K-$220K + variable"
location: Not specified (likely remote)
visa_sponsorship: Unknown (0 LCA filings — new company; must verify at first contact)
apply_threshold: 4.0 (mid-level AI role)
recommendation: Apply — verify H-1B sponsorship at first recruiter contact
key_gap: Sales/Marketing CRM domain (Salesforce, HubSpot)
key_strength: AgentProbe = exact match for their eval harness requirement; LeaseI = exact match for their agentic workflow requirement
```
