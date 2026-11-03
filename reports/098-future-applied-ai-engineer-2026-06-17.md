# Evaluation: Future — Applied AI Engineer

**Date:** 2026-06-17
**URL:** https://job-boards.greenhouse.io/future/jobs/4683133005
**Archetype:** Agentic / Automation (primary) + AI Platform / LLMOps (secondary)
**Score:** 4.5/5
**Legitimacy:** High Confidence
**PDF:** output/cv-future-applied-ai-engineer-2026-06-17.pdf

---

## A) Role Summary

| Dimension | Detail |
|-----------|--------|
| **Archetype** | Agentic / Automation + AI Platform / LLMOps |
| **Domain** | Digital fitness / personal coaching AI |
| **Function** | Build and ship AI agents serving real users — tool-calling LLMs, eval harnesses, production monitoring |
| **Seniority** | Mid–Senior IC (no explicit YOE, emphasis on production track record) |
| **Remote** | Remote (continental US) |
| **Comp** | $215,000–$250,000 + equity + health + 401k + wellness stipend |
| **Team** | Applied AI / engineering |
| **TL;DR** | Build production AI agents (tool calling, structured output, eval harnesses) at a well-funded wellness startup — $215-250K Remote with exact AgentProbe stack match. |

---

## B) Match with CV

### Requirements Map

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| Production Python + service deployment | Entrata 7+ years, FastAPI microservices | ✅ Strong |
| LangChain / LangGraph or similar agent frameworks | AgentProbe 3-agent LangGraph runtime | ✅ Direct |
| LLM production (prompt engineering, function/tool calling, structured output) | AgentProbe tool calls + Orchestrator agent | ✅ Direct |
| Design evaluation harnesses + quality scoring systems | AgentProbe 5-metric LLM-as-judge eval engine | ✅ Direct |
| Production monitoring + iteration | AgentProbe React dashboard + regression drift tracking | ✅ Direct |
| Async Python, HTTP APIs, streaming (SSE, webhooks) | FastAPI 15-endpoint backend | ✅ Strong |
| Data validation (Pydantic, JSON Schema) | FastAPI Pydantic models implicit in backend | ✅ Strong |
| AWS services (Bedrock, S3, ECR, CloudFront) | Entrata AWS S3/EC2/RDS/Glue, 100% PHI compliance | ✅ Solid |
| Observability (Langfuse, OpenTelemetry, Datadog) | AgentProbe trace-level agent observability | ✅ Partial (custom vs vendor tools) |

### Gaps
- AWS Bedrock / ECR / CloudFront: not explicitly mentioned in CV (general AWS experience is strong, Bedrock is a reasonable learning curve)
- Streaming protocols (SSE, webhooks): FastAPI supports both; not explicitly called out in CV

### Best Proof Points
1. **AgentProbe eval harnesses**: 5-metric LLM-as-judge (factual accuracy, hallucination, retrieval, completeness, compliance) — production quality gates blocking failing runs
2. **AgentProbe agents**: 3-agent LangGraph runtime with tool calling, inter-agent state handoffs, multi-provider routing
3. **Entrata scale**: 20+ production microservices, 100K+ MAU, FastAPI backend, async service delivery
4. **AI pipelines**: 1.6M financial records processed with output validation and quality gates

---

## C) North Star Alignment

| Dimension | Assessment |
|-----------|------------|
| **Archetype fit** | Core match — Agentic / Automation is Priority #2 archetype; eval harness focus = bonus +0.3 |
| **Seniority fit** | Mid-Senior IC = comfortable range |
| **Domain fit** | Wellness AI is novel (no prior vertical experience) but agent patterns are domain-agnostic |
| **Mission** | Future uses AI to personalize fitness coaching at scale — positive, meaningful product |

---

## D) Comp

| Dimension | Assessment |
|-----------|------------|
| **Range** | $215,000–$250,000 base — well above target ($100K–$140K), top quartile US AI Engineer market |
| **Equity** | Included — significant upside at a growth-stage startup |
| **Benefits** | Health, 401k, wellness stipend, flexible PTO |
| **Comp score** | 5.0/5 — exceptional |

---

## E) Cultural Signals

| Signal | Assessment |
|--------|------------|
| **Remote** | Fully remote (continental US) ✅ |
| **Startup stage** | Growth-stage AI startup — implies equity upside, fast pace, autonomy |
| **AI-first product** | Entire product is AI-driven coaching — engineering will be central |
| **Posting quality** | Specific, technical, realistic requirements — signals mature engineering team |

---

## F) Red Flags / Concerns

| Flag | Severity | Notes |
|------|----------|-------|
| Visa sponsorship unconfirmed | Medium | Application asks about eligibility — neither confirmed nor denied. Not a hard "no sponsorship." Worth confirming in recruiter screen. |
| Startup risk | Low | Future has raised significant funding; fitness AI space is competitive but durable |
| AWS Bedrock gap | Low | Nice-to-have, not required; Entrata AWS experience is solid foundation |

---

## G) Posting Legitimacy

| Signal | Assessment |
|--------|------------|
| Posting medium | Greenhouse (direct API) — real ATS |
| JD specificity | High — LangGraph, Pydantic, SSE/webhooks, eval harnesses, named tools |
| Salary transparency | Disclosed ($215K-$250K) — strong signal |
| Apply button | Active ✅ |

**Verdict: High Confidence** — specific JD, salary disclosed, real ATS, active apply.

---

## Recommended CV Angle

**Title:** Applied AI Engineer — eval harnesses, tool calling, LangGraph agents
**Lead with:** AgentProbe (eval harnesses → 5-metric LLM-as-judge, production quality gates) + Entrata (async Python services, production scale)
**Skip:** R/statistical modeling, Tableau — not relevant here

---

## STAR Story Bank

**"Tell me about a production AI system you shipped"**
> At Entrata I automated AI data transformation pipelines across 1.6M financial records — output validation, quality gates, compliance controls on regulated data. Then at AgentProbe I took that a step further and built the evaluation infrastructure itself: a 5-metric LLM-as-judge engine that blocks non-compliant agent outputs before they hit production. The same principle — you don't ship AI without a gate.

**"How do you evaluate LLM outputs in production?"**
> AgentProbe's eval engine scores factual accuracy, hallucination rate, retrieval quality, completeness, and compliance — five metrics per run, LLM-as-judge architecture. Failing runs are blocked by CI/CD quality gates before production. The React dashboard tracks regression drift and retrieval quality across concurrent test suites, so you can see when prompt changes degrade accuracy.

---

## Machine Summary

```yaml
company: Future
role: Applied AI Engineer
date: 2026-06-17
score: 4.5
archetype: Agentic / Automation + AI Platform / LLMOps
comp_range: "$215K-$250K"
location: Remote (continental US)
remote: true
visa_risk: medium
legitimacy: High Confidence
top_proof_points:
  - AgentProbe 5-metric LLM-as-judge eval harness = direct JD match
  - AgentProbe 3-agent LangGraph runtime with tool calling
  - Entrata async Python microservices at scale (100K+ MAU)
recommendation: Apply — perfect stack match, exceptional comp, remote
```
