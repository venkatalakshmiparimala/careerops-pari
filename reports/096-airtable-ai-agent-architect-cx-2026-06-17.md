# Evaluation: Airtable — AI Agent Architect, Customer Experience

**Date:** 2026-06-17
**URL:** https://job-boards.greenhouse.io/airtable/jobs/8409168002
**Archetype:** AI Platform / Agentic (CX-focused)
**Score:** 4.0/5
**Legitimacy:** High Confidence
**PDF:** output/cv-airtable-ai-agent-architect-cx-2026-06-17.pdf

---

## A) Role Summary

| Dimension | Detail |
|-----------|--------|
| Archetype | AI Platform / Agentic (CX-focused) |
| Domain | Customer Experience AI — building agents that handle support and CX workflows |
| Function | Architect + Build + Cross-functional |
| Seniority | Mid-to-Senior (production AI systems required) |
| Remote | Remote - US |
| Team | Customer Experience / AI |
| TL;DR | Design and build AI agent knowledge systems, safety guardrails, and observability for Airtable's CX function |

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| Deep LLM understanding (failure modes, reasoning) | AgentProbe: 5-metric eval engine explicitly tests hallucination and failure modes | Strong |
| RAG architectures | AgentProbe: ChromaDB RAG pipeline with per-run retrieval quality tracking | Strong |
| Prompt engineering + chain-of-thought | AgentProbe: multi-provider prompt routing, 5-metric scoring per prompt | Strong |
| Production AI systems experience | Entrata: 1.6M financial records AI pipelines + output validation; AgentProbe: CI/CD-gated production system | Strong |
| Observability layer (retrieval accuracy, action metrics) | AgentProbe: React dashboard tracking retrieval quality, latency, regression drift per run | Strong |
| Safety guardrails (prompt injection, failures) | AgentProbe: compliance metric in eval engine; AI on FHIR: HIPAA-compliant RBAC | Moderate |
| API / database scripting | Entrata: 200+ SQL queries tuned, RabbitMQ, PostgreSQL, 15-endpoint FastAPI backend | Strong |
| Solutions architecture / TPM / platform engineering | Entrata: 20+ full-stack modules, 120+ Agile sprints, cross-team delivery | Moderate |
| Cross-functional communication with non-technical stakeholders | GMU: faculty dashboards + research reporting (40% comprehension improvement) | Moderate |

### Gaps

| Gap | Blocker? | Mitigation |
|-----|----------|------------|
| CX / customer-facing AI experience | No | Frame AI on FHIR as "deploying AI that end users interact with" (clinical staff); AgentProbe observability as "building the layer that monitors agent reliability" |
| Solutions architect title | No | Frame as "platform engineer who also architects systems" — Entrata 20+ modules is sufficient evidence |
| Airtable product domain knowledge | No | Not required; learn on ramp |

---

## C) Level and Strategy

**Level detected:** Mid-to-Senior
**Parimala's natural level:** Senior (9 years SWE + AI systems)

**Sell strategy:**
- Safety + guardrails angle: "I built compliance evaluation into my LLM-as-judge engine — failing agents get blocked before reaching users. That's what you need for a CX agent handling real customer interactions."
- Observability angle: "AgentProbe gives me a React dashboard tracking retrieval accuracy, latency, and regression drift per run — exactly the observability layer you're building for CX agents."
- Regulated-domain angle: "HIPAA-compliant RBAC on AI on FHIR + PHI-compliant AWS pipelines at Entrata — I've built safe AI for end users before."

**If down-leveled:** Role might be classified as IC3/IC4. Accept if base ≥ $160K + equity in a company at Airtable's scale.

---

## D) Comp and Demand

| Source | Data |
|--------|------|
| Posted range | $177,000–$278,100 (SF/NYC/SEA/LA); $177,000–$250,300 (all other US including remote) |
| Airtable SWE market (Levels.fyi 2026) | ~$210K–$270K total comp at IC4-IC5 |
| Parimala's target | $150K–$175K base — well within range |
| Verdict | Well above target even at the floor. Fully remote at this comp level is rare. |

**H-1B:** Airtable is an established Series F company (~$11B valuation). Moderate-to-good H-1B sponsorship history. Ask recruiter to confirm.

---

## E) Customization Plan

| # | Section | Change | Why |
|---|---------|--------|-----|
| 1 | Summary | Lead with RAG, safety guardrails, observability, and AI systems | JD core requirements |
| 2 | AgentProbe | Lead bullet: observability layer + safety guardrails (compliance metric) | Direct JD language match |
| 3 | AI on FHIR | Frame as "AI serving end users with HIPAA-compliant guardrails" | CX + safety angle |
| 4 | Entrata | Frame as "cross-functional delivery across enterprise clients" | Solutions architecture signal |
| 5 | Skills | Lead AI row with: LLM Observability, RAG Pipelines, Prompt Engineering, Safety Guardrails, Agent Observability | ATS alignment |

---

## F) Interview Plan

| # | JD Requirement | Story | S | T | A | R | Reflection |
|---|---------------|-------|---|---|---|---|------------|
| 1 | Safety guardrails for AI agents | AgentProbe compliance metric | Needed to prevent non-compliant agent outputs in production | Build compliance evaluation | Added compliance as 5th metric in LLM-as-judge; failing runs blocked before prod via CI/CD | Zero non-compliant runs reach production | Would add per-query audit logging |
| 2 | Observability layer (retrieval, actions) | AgentProbe React dashboard | Needed visibility into RAG performance across concurrent runs | Build trace-level observability | React dashboard tracking per-run retrieval quality, latency, regression drift across agent test suites | Complete observability without cloud costs | Would integrate with Grafana for long-term dashboarding |
| 3 | RAG architecture for knowledge systems | AgentProbe ChromaDB RAG | Needed accurate knowledge retrieval for agent Q&A | Design traceable RAG pipeline | ChromaDB embeddings + per-run quality metrics; regression detection | Full retrieval quality visibility | Would add hybrid BM25 + vector search |
| 4 | Communicating AI behavior to non-technical stakeholders | GMU research dashboards | Faculty needed to understand ML outputs from 3 research pipelines | Translate ML to accessible insights | Tableau, ggplot2, Quarto dashboards — designed for non-technical faculty audiences | 40% comprehension improvement across two cohorts | Would do live demo sessions alongside dashboards |
| 5 | Production AI on real user data | Entrata + AI on FHIR | Clinical staff needed NL access to FHIR records; 1.6M financial records needed automation | Build user-facing AI in regulated environments | NLP-to-FHIR platform with HIPAA RBAC + OpenAI API on financial records with quality gates | ~60% retrieval reduction; 100% PHI compliance, zero incidents | Would add real-time monitoring from day one |

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Greenhouse ATS | Direct Airtable posting | Positive |
| Salary disclosed | $177K–$278K range clearly stated | Positive |
| Remote-US | Legitimate fully-remote role at established company | Positive |
| Role specificity | Prompt injection, chain-of-thought, RAG, action confidence — highly specific | Positive |
| Airtable stability | Series F, well-funded, established product | Positive |

---

## Machine Summary

```yaml
company: Airtable
role: AI Agent Architect, Customer Experience
date: 2026-06-17
score: 4.0
archetype: AI Platform/Agentic
location: Remote - US
comp_range: "$177,000-$278,100"
h1b: likely (established company, ask recruiter)
legitimacy: High Confidence
apply: evaluate-and-hold (4.0-4.4 range)
pdf: output/cv-airtable-ai-agent-architect-cx-2026-06-17.pdf
```
