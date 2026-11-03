# Evaluation: Tennr — Senior Backend Engineer, ML Team

**Date:** 2026-09-29
**URL:** (not provided — paste URL here)
**Archetype:** Agentic/Automation + AI Platform/LLMOps
**Score:** 4.5/5
**Legitimacy:** High Confidence
**PDF:** output/490-tennr-senior-backend-engineer-ml-2026-09-29.pdf

---

## A) Role Summary

| Dimension | Detail |
|-----------|--------|
| Archetype | Agentic/Automation (primary) + AI Platform/LLMOps (secondary) |
| Domain | Healthcare AI — referral workflows, insurance paperwork, patient routing |
| Function | Build — agentic systems, eval harnesses, data pipelines |
| Seniority | Senior Backend Engineer |
| Remote | NYC hybrid (Chelsea office 4 days/week) |
| Team size | Small ML team embedded with ML researchers |
| TL;DR | Build production agentic AI systems that process healthcare paperwork end-to-end — from data pipelines and evaluation harnesses to LLM-powered agent orchestration in real US healthcare environments. |

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| Agentic workflows, LLM orchestration | LeaseI: 8-agent LangGraph StateGraph with durable state, conditional routing, HITL escalation | Exact |
| Evaluation harnesses | AgentProbe: 5-metric eval engine, CI-integrated regression harness, golden datasets, LLM-as-judge scoring | Exact |
| Data pipelines | Entrata: HUD income-limit pipeline (few thousand → 180K domain records); AWS S3 migration; RabbitMQ async workflows | Strong |
| Full lifecycle: build → test → deploy → scale → monitor | LeaseI (prototype → 1,240-case eval in CI); Entrata (7yr production ownership of compliance pipelines) | Strong |
| LLM APIs (OpenAI, Anthropic, etc.) | AgentProbe: multi-provider routing (OpenAI/Anthropic/Groq/Ollama); LeaseI: LLM-as-judge scoring | Strong |
| Healthcare domain | AI on FHIR: FHIR APIs, HIPAA-compliant RBAC, NLP-to-clinical-query translation; LeaseI: compliance + PHI boundary rules | Strong |
| "Full-stack AI systems end-to-end" | FastAPI backend + Streamlit frontend (LeaseI); Flask + React (AI on FHIR); PHP/JS full-stack (Entrata 20+ modules) | Strong |
| Model deployment, observability, monitoring | AgentProbe: online + offline eval loops, latency + token efficiency metrics, hallucination rate tracking | Strong |
| "Ideation to code within hours, iterate quickly" | Magizhs internship: LangGraph mission planner from scratch within internship sprint cadence | Moderate |
| Bridge ML research → production | Research Associate (GMU): fine-tuned classification model → deployed inference API → presented to faculty | Strong |

**Gaps:**

| Gap | Type | Mitigation |
|-----|------|------------|
| Vision models (LLMs + vision mentioned) | Soft gap | JD says "LLMs, and vision models" — LLMs are primary; vision is secondary. She has Computer Vision in skills list; no production CV model ownership |
| NYC hybrid 4 days/week | Location | Open to relocation; never penalize |
| No salary listed | Uncertainty | Tennr is well-funded NYC startup — comp likely competitive; verify at first contact |
| H-1B: small startup | Risk | Tennr Series B (~200 employees); not a top-100 H-1B filer; clarify at first contact |

---

## C) Level and Strategy

**Level:** Senior Backend Engineer on ML team — IC role, collaborating with researchers. No direct reports implied.

**Sell points:**
- "I've built the exact system you're describing — an agentic pipeline for healthcare compliance (LeaseI) and the eval harness to regression-test it (AgentProbe). I can go from research insight to production system without waiting for someone else to productionize it."
- "At Entrata, I owned production systems for 7 years in a regulated domain where a wrong output has real consequences. Healthcare AI requires that same discipline — I've lived it."
- The "Cowboy" value maps directly: at Entrata, I owned the HUD pipeline as the sole engineer — I set the pace, handled incidents, and shipped every annual cycle without escalation.

**On vision models gap:** "My focus has been LLM-driven agentic systems, not vision pipelines — but the orchestration and eval infrastructure are the same. I can ramp on vision-specific components while contributing immediately on the agentic and eval layers."

---

## D) Comp and Demand

| Item | Detail |
|------|--------|
| Stated range | Not disclosed |
| Market estimate | NYC Senior Backend Engineer (AI/ML): $160K–$220K base (Levels.fyi, Glassdoor 2026) |
| Tennr funding | Series B (~$101M raised, Andreessen Horowitz); well-funded healthcare AI startup |
| Comp score | 4/5 — no disclosure, but Series B NYC startup range likely competitive |
| Benefits | 100% employee health covered, 401k match, unlimited PTO, parental leave |

---

## E) Customization Plan

| # | Section | Current | Proposed Change | Why |
|---|---------|---------|-----------------|-----|
| 1 | Summary headline | Generic AI engineer | "Healthcare AI Engineer · Agentic Workflows · LLM Eval Harnesses · Python · FastAPI · Production AI" | Matches "ML team bridging research → production" exactly |
| 2 | Summary body | Broad framing | Lead with: LeaseI = "production agentic system for healthcare compliance domain"; AgentProbe = "eval harness I built to regression-test non-deterministic AI in CI" | Two sentences that answer the JD's core ask |
| 3 | LeaseI bullets | Support investigation framing | Add explicit healthcare compliance framing: "compliance eligibility rules = insurance authorization logic analog" | Tennr is insurance paperwork — direct domain analogy |
| 4 | AI on FHIR | Listed as project | Move to top of projects, add: "FHIR APIs + HIPAA RBAC + NLP query translation — real healthcare data infrastructure, not a mock" | Healthcare domain credential |
| 5 | AgentProbe | Eval toolkit | Add: "online + offline eval loops; latency + hallucination monitoring in CI — the observability infrastructure for non-deterministic production systems" | Matches "monitoring that stays reliable as traffic grows" |

---

## F) Interview Plan

| # | JD Requirement | Story | S | T | A | R | Reflection |
|---|----------------|-------|---|---|---|---|------------|
| 1 | "Build agentic systems for complex healthcare processes" | LeaseI end-to-end | Support investigation taking a full day; root cause buried across settings, regulations, incidents | Build a production agentic platform for compliance investigation | 8-agent LangGraph StateGraph, HITL gate, citation-grounded RAG, deterministic compliance boundary | 93.6% precision, 87.9% F1 on 1,240 test cases; CI regression harness running | Should have started with the eval harness before building agents — non-deterministic systems need measurement first |
| 2 | "Evaluation harnesses" | AgentProbe build | Every LLM project had no reusable eval methodology; no way to regression-test outputs in CI | Build a toolkit any team can use to ship LLM systems safely | 5-metric engine, golden datasets, CI regression gate, multi-provider routing, LLM-as-judge | Teams evaluate LLMs locally at zero cost; regression failures surface before merge | The discipline of "define metrics before writing code" is the hardest part — most engineers skip it |
| 3 | "Data pipelines, full lifecycle" | Entrata HUD pipeline | Federal HUD releases income limits annually; pipeline expanding few thousand rows to ~180K domain records powering eligibility calculations | Own the pipeline end-to-end: ingestion, validation, reconciliation, rollback readiness | Built baseline validation, reconciliation tooling, and rollback procedures for 7 consecutive annual cycles | Zero compliance violations; zero rollback incidents; system runs reliably today | The compliance domain (regulated healthcare) and the compliance domain (regulated housing) have the same failure mode: wrong output = real-world harm |
| 4 | "Model deployment, observability, monitoring" | AgentProbe eval loops | After LeaseI shipped, needed ongoing production monitoring — offline eval wasn't enough | Add online evaluation loops tracking live model drift | Instrumented latency, token efficiency, hallucination rate in real-time alongside offline golden-dataset regression | Caught a prompt regression before it reached users | Online eval is more expensive but catches distribution shift that golden datasets miss |
| 5 | "Go from ideation to code within hours" | Magizhs MCP server | Operator needed a way for downstream tools to query the planning system dynamically | Ship MCP server integration in a single sprint | Designed and deployed MCP server enabling Model Context Protocol queries; integrated with LangGraph planning graph | Operators could connect any MCP-compatible tool without additional backend work | MCP as an integration layer is worth defaulting to for any tool that needs to be queried by external systems |
| 6 | "Collaborate with ML researchers → production" | GMU fine-tuning | Faculty had a classification research need with no deployment path | Bridge research → production inference | Fine-tuned HuggingFace/PyTorch model; deployed inference API on Quart; presented results to faculty | Researchers could iterate on model versions and immediately test via API | Research → production requires explicit contracts: input format, output schema, latency budget, failure mode |

**Recommended case study:** LeaseI — specifically frame as "healthcare compliance paperwork automation analog" — Tennr does insurance authorization, LeaseI does housing eligibility; same problem structure: structured paperwork → extract key fields → check against regulatory rules → route to human or auto-decide.

**Red-flag questions:**
- *"Do you have production healthcare AI experience?"*
  → "LeaseI processes compliance documents for housing eligibility — a regulated domain with the same failure modes as insurance authorization: wrong extraction, wrong rule application, wrong patient routing. I built HIPAA-compliant FHIR query infrastructure in AI on FHIR. The regulatory rigor is identical even if the domain is different."
- *"NYC hybrid 4 days/week — are you able to commit?"*
  → "Yes — I'm open to relocating to NYC for the right role. Healthcare AI at this scale is the right role."

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Posting freshness | Active posting (provided directly, no stale signals) | Positive |
| Description specificity | Names specific tech (LLMs, vision models, agentic systems), clear responsibilities, healthcare domain stated | Positive |
| Company funding | Series B, $101M raised, a16z-backed — active hiring is expected | Positive |
| Role-company fit | ML team building healthcare AI workflows = exact match for "Senior Backend Engineer on ML team" | Positive |
| Requirements realism | No contradictions; experience ask matches role scope | Positive |
| Salary missing | NYC startup norms — many don't disclose until screen | Neutral |

---

## Keywords Extracted (ATS)

Agentic workflows, LLM APIs, evaluation harnesses, data pipelines, healthcare AI, production AI systems, full-stack AI, model deployment, observability, monitoring, agent orchestration, vision models, FHIR, HIPAA, backend engineering, system design, scalable production systems, LangGraph, FastAPI, Python, CI/CD, iterative development, ML research to production

---

## Machine Summary

```yaml
role: Senior Backend Engineer, ML Team
company: Tennr
score: 4.5
archetype: Agentic/Automation + AI Platform/LLMOps
location: NYC hybrid (Chelsea, 4 days/week)
salary_range: not disclosed (Series B, a16z, ~$160K-$220K estimated)
sponsorship: unconfirmed (verify at first contact — smaller startup)
top_proof_points:
  - LeaseI 8-agent LangGraph (healthcare compliance = insurance authorization analog)
  - AgentProbe eval harness (5-metric CI regression for non-deterministic AI)
  - AI on FHIR (FHIR APIs, HIPAA RBAC, clinical NLP)
  - Entrata data pipelines (7yr regulated production ownership)
key_gaps:
  - vision models (secondary in JD; soft gap)
  - NYC hybrid 4 days (open to relocate)
  - H-1B: Series B startup, confirm at first contact
recommendation: apply — agentic + eval + healthcare = exact triple match; comp and H-1B to verify
```
