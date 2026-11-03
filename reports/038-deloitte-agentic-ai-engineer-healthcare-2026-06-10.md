# Evaluation: Deloitte — Agentic AI Engineer, Healthcare AI

**Date:** 2026-06-10
**URL:** https://apply.deloitte.com/en_US/careers/InviteToApply?jobId=355577&source=LinkedIn
**Archetype:** AI Platform / LLMOps
**Score:** 4.0/5
**Legitimacy:** High Confidence
**PDF:** output/cv-deloitte-agentic-ai-engineer-2026-06-10.pdf

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | AI Platform / LLMOps |
| Domain | Agentic AI systems, RAG pipelines, observability, LLM evaluation, healthcare AI |
| Function | Build |
| Seniority | Senior IC ("production agentic systems is your primary craft") |
| Remote | 40 US locations — Arlington/Rosslyn VA listed (no relocation needed) |
| Comp | $134,500–$265,100 base ("benchmarked to leading tech companies") |
| TL;DR | Build production agentic systems for healthcare — LangGraph/LangChain orchestration, end-to-end RAG, observability/tracing, LLM evaluation, human-in-the-loop checkpoints — inside Deloitte's $1B healthcare AI investment. |

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| Production agentic systems (LangGraph/LangChain) | AgentProbe: 3 LangGraph agents (Orchestrator, RAG Tracer, Auto Fix) | ✅ Direct proof |
| End-to-end RAG: ingestion, chunking, embeddings, retrieval | AgentProbe RAG pipeline + ChromaDB vector store | ✅ Direct proof |
| Observability & tracing (prompt, tool calls, retrieval, agent traces) | AgentProbe RAG Tracer agent + React observability dashboard | ✅ Direct proof |
| LLM evaluation — task/trajectory level, not just output quality | AgentProbe 5-metric LLM-as-judge engine + Auto Fix feedback loop | ✅ Direct proof |
| Human-in-the-loop checkpoints + human oversight models | AgentProbe: eval gates designed to keep humans informed before deployment | ✅ Direct proof |
| Guardrails, safety controls, failure-handling | AgentProbe: anomaly flags, threshold-based Auto Fix triggers | ✅ Strong |
| Strong Python + testing/CI/CD/API integration | 8+ years Python at Entrata; TDD/BDD; 15-endpoint FastAPI; GitHub Actions | ✅ Strong |
| Frontier model platform experience (Anthropic, OpenAI) | AgentProbe: multi-provider (Ollama, Anthropic, OpenAI, Groq) | ✅ Direct proof |
| Memory and context management | AgentProbe context assembly + ChromaDB persistent memory | ✅ Strong |
| Multi-agent systems + collaboration patterns | AgentProbe 3-agent LangGraph pipeline: Orchestrator → RAG Tracer → Auto Fix | ✅ Strong |
| FHIR / healthcare exposure | AI on FHIR project: NLP-to-FHIR query system, BERT, RBAC, HIPAA-compliant | ✅ Rare differentiator |
| Vector databases (Pinecone, Weaviate, Milvus) | ChromaDB only — not the preferred list | ⚠️ Soft gap |
| Model adaptation (LoRA, QLoRA) | No fine-tuning experience listed | ⚠️ Soft gap |
| 0–50% travel | Not previously flagged; manageable | ⚠️ Note |

**Gaps and mitigations:**
- **Vector DB preference** — JD lists Pinecone/Weaviate/Milvus; Parimala has ChromaDB. All are semantically identical in purpose; ChromaDB is architecturally equivalent. Mitigate by naming ChromaDB's vector store design explicitly.
- **Fine-tuning** — LoRA/QLoRA is preferred, not required. Zero mentions in required qualifications. Skip.
- **"Primary craft, not a recent exploration"** — AgentProbe is a full production system with 15-endpoint API, CI, multi-provider support, open-source. That's not exploration. Frame explicitly: "AgentProbe is my primary project, not a class project."
- **H-1B language** — "Limited immigration sponsorship may be available" is cautious but Deloitte Consulting filed 1,793 LCAs in FY2026. Treat as medium risk; confirm in first recruiter call.

---

## C) Level and Strategy

**Level detected:** Senior IC. "Your primary craft" + production systems framing = mid-to-senior.

**Sell plan:**
- Lead with the precise mapping: *"I built AgentProbe — a production LangGraph system with exactly the architecture this role requires: multi-agent orchestration, RAG pipeline end-to-end, observability tracing per run, and an LLM-as-judge eval engine."*
- AI on FHIR is a rare signal: FHIR experience is listed as a preferred qualification and healthcare exposure is explicitly valued. Only a fraction of agentic engineers have built a healthcare data system. Name it.
- Healthcare safety framing maps directly to AgentProbe's design: *"AgentProbe was designed to prevent AI quality regressions before deployment — the same principle as healthcare-grade deployment eval gates."*
- Arlington VA is in the location list — zero relocation friction. Mention proximity.
- The "startup-style upside" language and $1B investment framing signals this is a high-autonomy, high-impact team inside Deloitte — not traditional consulting. Frame as a builder role.

**If they downlevel:** Only acceptable if base ≥ $165K. The $134K floor is well below market for this skillset.

---

## D) Comp and Demand

| Source | Range | Notes |
|--------|-------|-------|
| Job posting | $134,500–$265,100 base | Wide band — senior range is $200-265K |
| Deloitte market | $144K–$219K (AI/ML Engineer median) | Consulting scale; "benchmarked to tech" |
| Performance incentive | Listed — "startup-style upside" | Unclear quantum |

**Assessment:** Comp is lower than pure AI-lab roles (Anthropic $320-405K) but competitive for consulting at senior band. The healthcare AI vertical + 40-location flexibility + Arlington VA proximity make this worth applying. H-1B medium risk.

**H-1B:** Deloitte Consulting filed 1,793 LCAs FY2026 — one of the largest sponsors in the country. The "limited sponsorship may be available" language is standard Deloitte boilerplate for non-core-consulting tracks. Confirm availability in recruiter screen.

---

## E) Customization Plan

| # | Section | Current | Proposed change | Why |
|---|---------|---------|-----------------|-----|
| 1 | Summary | Generic AI builder | Lead: *"Agentic AI engineer — built AgentProbe, a production LangGraph system with multi-agent orchestration, RAG, observability tracing, and LLM-as-judge evaluation."* | Mirrors JD language exactly |
| 2 | AgentProbe | General description | Emphasize: LangGraph orchestration, RAG end-to-end, observability + tracing, human-in-the-loop eval gates | JD: these are the 4 primary requirement pillars |
| 3 | AI on FHIR | Secondary project | Surface prominently: FHIR healthcare data, NLP-to-structured-query, HIPAA-compliant RBAC | Rare differentiator; healthcare exposure is preferred |
| 4 | Competencies | AI Observability focus | Add: Multi-Agent Orchestration, Healthcare Data (FHIR), Context & Memory Management, Frontier Model Integration | Map to JD's 4 pillars |
| 5 | Entrata data pipelines | AWS S3 migration | Reframe: *"production-quality code across 120+ Agile sprints"* + CI/CD + testing discipline | JD: "strong practices in testing, CI/CD, logging, versioning" |

---

## F) Interview Plan

| # | JD Requirement | Story | S | T | A | R | Reflection |
|---|----------------|-------|---|---|---|---|------------|
| 1 | Production LangGraph agentic systems | AgentProbe 3-agent pipeline | No tool to monitor multi-agent RAG runs end-to-end | Build production agentic system: orchestrate RAG Tracer + Auto Fix via LangGraph | Designed stateful LangGraph pipeline with branching, retries (Auto Fix), human-oversight gates (eval thresholds) | Full production system: 15-endpoint API, multi-provider support, open-source — ships to real users | Agent state management is the hard part — LangGraph's state graph makes branching deterministic |
| 2 | End-to-end RAG: indexing → retrieval → evaluation | AgentProbe RAG pipeline | No way to attribute failures to retrieval vs generation vs prompt | Build RAG Tracer that enriches every run with per-stage attribution | Ingestion → chunking → ChromaDB embeddings → retrieval scoring → generation quality → eval score | Full trace visibility per query; retrieval score surfaced per run | Hybrid retrieval (BM25 + vector) beats pure vector for factual healthcare queries |
| 3 | Observability + tracing (prompt, tool calls, agent traces) | AgentProbe React dashboard | Silent failures in multi-step pipelines — no visibility into what failed where | Build trace-level observability for every agent run | RAG Tracer enriches per query: retrieval score, generation score, anomaly flags; React dashboard visualizes per-run | Every run inspectable: prompt → retrieval → generation → eval; failure attribution in <1 trace | Async trace collection > sync: blocking kills throughput in multi-step pipelines |
| 4 | Healthcare-grade deployment eval gates + human oversight | AI on FHIR + AgentProbe eval gates | Healthcare AI systems deployed without validation have patient-safety risk | Build eval-gated system: no output goes live without scoring above threshold | AgentProbe: threshold-based Auto Fix triggers; AI on FHIR: HIPAA RBAC, FHIR-structured grounding reduces hallucination risk | Systems where human oversight is built into the deployment pipeline, not bolted on after | Structured output (FHIR schema) as a grounding constraint is more reliable than free-text in clinical context |
| 5 | Python engineering + testing + CI/CD | Entrata 120+ sprints + AgentProbe | Large-scale production engineering with TDD/BDD quality gates | Maintain 99.5% uptime and sub-10 bug count for 6+ consecutive months | TDD/BDD, Docker, GitHub Actions, PostgreSQL schema design, 20+ production modules | 99.5% uptime; 50% exec time cut via Docker containerization; 80% workload eliminated | Documentation is a first-class feature — undocumented production code has the same adoption problem as undocumented APIs |

**Case study to present:** AgentProbe + AI on FHIR tandem — *"I've built two systems that are directly relevant: one that monitors AI pipelines with observability and eval gates (AgentProbe), and one that grounds LLM queries in structured healthcare data (AI on FHIR). The Deloitte Healthcare AI role is the first role I've seen that makes both projects simultaneously relevant."*

**Red flag questions:**
- *"You don't have healthcare background"* → *"The JD says explicitly: 'You do not need a healthcare background.' I do have it anyway — I built AI on FHIR, an NLP-to-FHIR query system with HIPAA-compliant RBAC. That's healthcare data systems experience most AI engineers don't have."*
- *"Limited sponsorship — will you need visa support?"* → *"Yes, I'm on F-1 OPT STEM extension (valid through 2027). I'd want to confirm H-1B availability early in the process. Given Deloitte's 1,793 LCAs filed in FY2026, I'm confident it's possible — but want to be transparent."*

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Posting freshness | Active on Deloitte careers portal | Positive |
| Apply button | Active (InviteToApply URL provided) | Positive |
| JD specificity | Named tech stack (LangGraph, LangChain, RAG, FHIR), specific healthcare context, explicit comp range | Positive |
| Salary listed | Yes ($134,500–$265,100) — rare transparency for consulting | Positive |
| Company health | Deloitte: $1B committed healthcare AI investment; major firm, no freeze signals | Positive |
| H-1B | 1,793 LCAs FY2026 — large sponsor, cautious boilerplate language | Positive (with caveat) |
| Travel requirement | 0–50% — disclosed and manageable | Neutral |

---

## Keywords Extracted

agentic ai, langchain, langgraph, rag pipeline, multi-agent systems, observability, tracing, llm evaluation, human-in-the-loop, healthcare ai, fhir, context management, vector database, frontier models, python, production agents, deloitte, deployment eval gates, guardrails, safety controls

---

## Machine Summary

```yaml
report_num: 038
company: Deloitte
role: Agentic AI Engineer, Healthcare AI
date: 2026-06-10
score: 4.0
archetype: AI Platform / LLMOps
legitimacy: High Confidence
location: 40 US locations — Arlington/Rosslyn VA available (no relocation)
comp_range: "$134,500–$265,100 base"
visa_risk: medium (Deloitte = large sponsor; "limited sponsorship" language is caution, not denial)
key_gaps:
  - H-1B language cautious (confirm in recruiter call)
  - Vector DB preference (Pinecone/Weaviate/Milvus vs ChromaDB — architecturally equivalent)
  - No fine-tuning experience (LoRA/QLoRA — preferred only, not required)
key_strengths:
  - AgentProbe = direct proof of LangGraph, RAG, observability, LLM evaluation, human-in-the-loop
  - AI on FHIR = rare healthcare differentiator (FHIR listed as preferred)
  - Arlington VA in location list — zero relocation friction
  - $1B healthcare AI investment — real product, not internal skunkworks
  - Frontier model multi-provider (Anthropic + OpenAI + Groq)
location_risk: low — Arlington VA is in the location list
recommend: apply — strongest technical match possible for agentic AI role; healthcare differentiator via AI on FHIR is rare signal; confirm visa early
```
