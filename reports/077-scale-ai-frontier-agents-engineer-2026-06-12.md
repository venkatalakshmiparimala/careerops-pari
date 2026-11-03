# Evaluation: Scale AI — Frontier Agents Engineer

**Date:** 2026-06-12
**URL:** https://job-boards.greenhouse.io/scaleai/jobs/4694861005
**Archetype:** AI Forward Deployed Engineer / Agentic AI
**Score:** 4.2/5
**Legitimacy:** High Confidence
**PDF:** output/cv-scale-ai-frontier-agents-engineer-2026-06-12.pdf

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | AI FDE — build production AI agents for enterprise clients, serve as primary technical contact |
| Domain | Frontier AI agents: multi-agent systems, eval frameworks, RAG, prompt engineering, customer integration |
| Function | Build + deploy AI agents tailored to enterprise customers; guide fine-tuning + eval; influence product roadmap |
| Seniority | Mid-to-Senior (4+ years required) |
| Location | San Francisco, CA or New York, NY (in-person/hybrid — relocation required from VA) |
| Comp | $180K–$225K base + equity + benefits — far above target |
| TL;DR | AgentProbe is the exact proof point for this role: multi-agent LangGraph system, 5-metric eval engine, RAG pipelines, prompt engineering. Python 8+ years exceeds bar. $180-225K above target. Strong apply. |

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| 4+ years SWE, Python production | 8+ years Python production at Entrata (100K+ MAU, 1.6M records) | ✅ Far exceeds |
| Build production AI agents + multi-agent systems | AgentProbe: 3-agent LangGraph system (Orchestrator, RAG Tracer, Auto Fix), tool calls, inter-agent state handoffs | ✅ Direct proof |
| Implement evaluation frameworks | AgentProbe: 5-metric LLM-as-judge engine (factual accuracy, hallucination, retrieval, completeness, compliance) with CI/CD gates | ✅ Direct proof |
| RAG systems | AgentProbe: ChromaDB vector store + embeddings + retrieval quality scoring | ✅ Direct proof |
| Prompt engineering | AgentProbe: multi-provider LLM routing (Anthropic, OpenAI, Groq, Ollama), dynamic prompt strategies | ✅ Direct proof |
| Customer integration / enterprise scale | Entrata: 100K+ MAU, 1.6M records, cross-functional delivery across 120+ Agile sprints | ✅ Strong |
| Cloud: AWS/GCP/Azure | AWS S3 migration (100% PHI compliance), Azure-compatible AgentProbe endpoints, Docker | ✅ Present |
| LLM knowledge + agent development | AgentProbe: LangChain, LangGraph, multi-provider routing, tool calls, agent reasoning | ✅ Direct proof |
| Vector database familiarity | AgentProbe: ChromaDB | ✅ Direct proof |
| Enterprise security/compliance (HIPAA, GDPR) | Entrata: 100% PHI compliance, zero security incidents, Libsodium encryption; AI on FHIR: HIPAA-compliant RBAC | ✅ Strong |
| H-1B sponsorship | Scale AI: 83 LCAs FY2025, 97% approval rate | ✅ Confirmed |

**Gaps:**
- Docker/Kubernetes/Terraform (Docker ✅, Kubernetes absent) — minor; FastAPI microservices covers the intent
- Technical consulting/solutions engineering experience — adjacent via Entrata cross-functional delivery + GMU TA, not explicit enterprise consulting
- Scale AI's Frontier product is GenAI-first — Parimala's work is open-source, not Scale's proprietary stack (learnable)

---

## C) Level and Strategy

**Level:** Mid-to-Senior (4+ years). Parimala has 8+ years — exceeds bar. Positioning as "senior new grad": MS May 2026 + 8 years of production experience at Entrata + AgentProbe as live open-source proof. The combination is genuinely unusual.

**Sell senior without lying:**
- Lead with AgentProbe as a live system, not a class project: "I didn't build a demo — I built a production-grade agentic platform that runs 100% locally at zero cost with 3 LangGraph agents and a 5-metric eval engine."
- Frame Entrata tenure as evidence of reliability at scale: 99.5% uptime, 100K+ MAU, zero security incidents.
- The eval engine directly maps to Scale's core business: AI quality assurance. "I built the same system Scale sells."

**If they downlevel:** Accept if $150K+ base; negotiate 6-month review with clear criteria.

---

## D) Comp and Demand

- **Role range:** $180K–$225K base (confirmed from posting)
- **Total comp estimate:** $180-225K base + equity (Scale AI private, $13B+ val) + benefits → TC likely $220-300K+
- **vs. target:** Far above ($100-140K target) — this is a top-tier comp offer
- **Scale AI H-1B:** 83 LCAs FY2025, 97% approval; active sponsor
- **Market context:** FDE/Applied AI Engineer at this level typical range $160-280K TC; Scale AI is top of range

---

## E) Customization Plan

| # | Section | Change | Why |
|---|---------|--------|-----|
| 1 | Summary | Replace "AgentProbe — open-source agentic AI testing toolkit" framing with "builds production AI agents for enterprise customers — the exact function of Scale's Frontier Agents team" | JD is FDE + enterprise agents, not open-source testing |
| 2 | AgentProbe bullets | Add: "multi-agent system that mirrors Scale's Frontier agent architecture: Orchestrator routes tasks, RAG Tracer validates retrieval, Auto Fix closes the loop" | Maps directly to Scale's customer-facing agent deployments |
| 3 | Eval engine | Emphasize CI/CD gates + compliance scoring → "ensures agents are audit-ready for enterprise production, aligned with Scale's reliability standards" | Scale AI's core value prop is AI quality |
| 4 | Entrata | Add "served as de-facto technical point of contact for cross-functional product delivery across 100K+ MAU" — maps to "primary technical contact for strategic accounts" | FDE archetype requirement |
| 5 | Skills | Add: ChromaDB, vector search, LLM-as-judge evaluation, CI/CD eval gates explicitly | Keywords from JD |

---

## F) Interview Plan

| # | JD Requirement | Story | S | T | A | R | Reflection |
|---|----------------|-------|---|---|---|---|------------|
| 1 | Build production AI agents | AgentProbe: 3-agent LangGraph | Testing LLMs had no pre-deployment infrastructure | Build the system no one had | 3 LangGraph agents with tool calls, state handoffs | 15-endpoint FastAPI, runs 100% locally | Would add human-in-the-loop checkpoints earlier |
| 2 | Implement eval frameworks | AgentProbe 5-metric eval engine | LLM outputs unverifiable before CI/CD | Make agents auditable in prod | 5-metric LLM-as-judge: factual accuracy, hallucination, retrieval, completeness, compliance | CI/CD gates block bad agents automatically | Would expand to adversarial testing |
| 3 | RAG systems | AgentProbe RAG Tracer agent | RAG failures hard to trace | Observable retrieval layer | ChromaDB + embeddings + retrieval quality scoring | RAG quality measurable per-query | Would add latency profiling |
| 4 | Enterprise compliance | Entrata AWS migration | 1M+ client records needed PHI compliance | Zero incidents, 100% compliance | Libsodium encryption, automated pipelines, AWS S3 | 100% PHI compliance, zero security incidents | Would start with threat model earlier |
| 5 | Customer-facing delivery | Entrata 120+ sprint delivery | 20+ modules shipped cross-functionally | Primary technical liaison per module | Python, TypeScript, GraphQL, PostgreSQL full-stack | 100K+ MAU, 40% deploy time reduction | Would invest more in documentation earlier |
| 6 | Multi-provider LLM routing | AgentProbe LLM Router | Different tasks need different models | Dynamic model selection | Provider routing across Anthropic, OpenAI, Groq, Ollama by capability + cost | Zero hardcoded model; adaptive routing | Would add cost telemetry per-call |

**Case study to present:** AgentProbe — "Here's the architecture. Orchestrator receives the test suite, routes sub-tasks to RAG Tracer (retrieval quality) and Auto Fix (hallucination repair). Each agent uses tool calls. The eval engine scores the full run. The CI/CD gate fails the pipeline if any metric drops. This is what Scale's Frontier customers need."

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Freshness | Discovered via ATS API 2026-06-12 (real-time) | Positive |
| Apply button | Active (Greenhouse ATS) | Positive |
| JD specificity | Detailed: compensation range, specific tech (vLLM, TensorRT-LLM mentioned in sibling roles), named responsibilities | Positive |
| H-1B track record | 83 LCAs FY2025, 97% approval — active program | Positive |
| Company hiring signals | Scale AI raised $1B+ in 2024, active GenAI expansion | Positive |
| Reposting pattern | No prior appearances in scan-history.tsv | Positive |

---

## Keywords

production AI agents, multi-agent systems, evaluation frameworks, RAG, LangGraph, LangChain, prompt engineering, ChromaDB, vector database, Python, AWS, enterprise integration, LLM-as-judge, FastAPI, TypeScript, agentic AI, technical account management, forward deployed engineer

---

## Machine Summary

```yaml
report_num: 077
company: Scale AI
role: Frontier Agents Engineer
date: 2026-06-12
score: 4.2
archetype: AI Forward Deployed / Agentic AI
legitimacy: High Confidence
location: San Francisco, CA or New York, NY (relocation required from VA)
comp_range: "$180K–$225K base + equity (TC est. $220K–$300K+)"
visa_risk: low (83 LCAs FY2025, 97% approval)
key_gaps:
  - No Kubernetes (Docker present; minor)
  - No formal enterprise consulting title (Entrata delivery is adjacent)
  - Scale's proprietary Frontier stack is new (learnable)
key_strengths:
  - AgentProbe = direct proof for every core JD requirement
  - 5-metric eval engine = Scale's core value prop (AI quality)
  - Python 8+ years far exceeds 4+ year bar
  - Enterprise scale (100K+ MAU, PHI compliance)
  - $180-225K base far above target
  - H-1B confirmed strong sponsor
recommend: strong apply — AgentProbe is the proof of concept for this exact role
```
