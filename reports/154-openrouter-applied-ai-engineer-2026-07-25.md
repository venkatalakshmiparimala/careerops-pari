# OpenRouter — Applied AI Engineer

**Date:** 2026-07-25
**URL:** https://jobs.ashbyhq.com/openrouter/407f71b5-4b1f-4666-91bd-394f3c26f19d
**Archetype:** Applied AI Engineer / Agentic Automation
**Score:** 4.4/5
**Legitimacy:** High Confidence
**PDF:** output/cv-venkata-lakshmi-parimala-pasupuleti-openrouter-2026-07-25.pdf

---

## A) Role Summary

| Dimension | Detail |
|-----------|--------|
| Archetype | Applied AI Engineer — internal agentic automation + eval ownership |
| Domain | LLM infrastructure / GTM automation |
| Function | Build production agentic workflows, own eval layer |
| Seniority | Mid-Senior |
| Remote | Yes — US remote |
| Team | ~20 people, Series A/B stage |
| TL;DR | Build internal AI agents automating support + GTM operations on OpenRouter's own infrastructure; own evals, guardrails, and monitoring. Drive measurable impact. |

**Comp:** Not disclosed for this role. Related Platform SWE role: $215K–$285K base. Applied AI Engineer likely $130K–$180K range based on company stage and role scope.

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| Production LLM/agentic systems shipped | AgentProbe (3-agent LangGraph, FastAPI, 15 endpoints), LeaseI (8-agent HITL), Entrata AI pipeline (1.6M records) | ✅ Strong |
| Experience across 3+ agent harnesses | LangGraph, LangChain, direct OpenAI/Anthropic API, Groq, Ollama — AgentProbe multi-provider routing | ✅ Strong |
| Evals and data rigor | AgentProbe's 5-metric LLM-as-judge eval engine (factual accuracy, hallucination, retrieval, completeness, compliance) — CI-integrated, regression gate blocks failing runs | ✅ Direct proof point |
| Guardrails and monitoring | LeaseI validation guardrails + deterministic compliance logic; AgentProbe trace-level observability; Magizhs validation guardrails blocking non-compliant outputs | ✅ Strong |
| Security mindset | 100% PHI compliance on AWS S3 migration; Libsodium encryption; HIPAA-compliant AI on FHIR | ✅ Strong |
| Python production quality | 8+ years Python at Entrata (1M+ records, 100K+ MAU) | ✅ Strong |
| GTM/support automation context | ClickHouse GTM framing + OpenRouter's internal GTM tooling need | ✅ Moderate |
| Integrate with company tools | Salesforce/Clay/n8n at Entrata; RabbitMQ integration; REST API pipelines | ✅ Moderate |
| SQL | 200+ queries tuned, 30% perf gain | ✅ Strong |

**Gaps:**
| Gap | Severity | Mitigation |
|-----|----------|------------|
| No prior OpenRouter-specific experience | Mild | OpenRouter's own platform is the stack — she uses it; can frame AgentProbe's multi-provider LLM routing (which already hits OpenRouter) as direct product familiarity |
| GTM domain ownership | Mild | Engineering depth is there; would pair with OpenRouter team on GTM logic |

---

## C) Level and Strategy

**Level detected in JD:** Mid-Senior Applied AI Engineer — own workflows end-to-end, drive measurable impact

**Sell senior plan:**
- Lead with AgentProbe eval engine: "I built the exact eval + observability layer you're asking me to own. 5 metrics, CI-integrated, regression gate, per-run drift monitoring — not a demo, it's live."
- Emphasize multi-harness experience: LangGraph + LangChain + direct provider SDKs + tool calling across multiple orchestration patterns
- Frame the security/blast-radius mindset explicitly: PHI compliance, HIPAA, validation guardrails before output

---

## D) Comp and Demand

| Source | Data |
|--------|------|
| OpenRouter Platform SWE | $215K–$285K base |
| Applied AI Engineer estimate | $130K–$180K (company stage + role) |
| Parimala's target | $100K–$140K |

**Assessment:** Even the low end of estimated range ($130K) meets or exceeds target. Strong financial upside if this role is comped at platform SWE rates. Score: **3.5/5** (undisclosed).

---

## E) Customization Plan

| # | Section | Change | Why |
|---|---------|--------|-----|
| 1 | Summary | Lead with "LLM eval engine builder + agentic automation engineer" framing | JD explicitly wants evals rigor and agentic systems |
| 2 | Competencies | Lead with "LLM Evaluation & Observability" and "Multi-Agent Agentic Architecture" | Primary JD keywords |
| 3 | AgentProbe | Emphasize 5-metric eval engine, CI regression gate, multi-harness patterns | Direct match to "evals + 3+ agent harnesses" requirement |
| 4 | Entrata | Lead with AI pipeline bullet; add guardrails/compliance controls language | Matches "security mindset" and "production systems" |
| 5 | Skills | Ensure "evals frameworks", "LLM observability", "guardrails", "monitoring" appear | ATS keywords |

---

## F) Interview Plan

| # | JD Ask | Story | S | T | A | R |
|---|--------|-------|---|---|---|---|
| 1 | Evals + data rigor | AgentProbe: 5-metric LLM-as-judge eval engine | Needed CI-gated evals for agent quality | Build automated scoring into merge pipeline | LLM-as-judge with 5 metrics, GitHub Actions integration, regression gate | Every commit auto-scored; failing agent runs blocked before production |
| 2 | Multi-harness experience | AgentProbe: LangGraph + LangChain + direct SDK + Groq + Ollama routing | Single-provider lock-in is a risk | Build multi-provider routing that degrades gracefully | Dynamic LLM Router selecting provider by capability/cost/latency | 4+ providers working via unified interface; zero provider lock-in |
| 3 | Security mindset | Entrata: PHI compliance + Libsodium | 100% of resident SSNs/phone numbers in plaintext on AWS S3 | Migrate to encrypted storage while updating 50%+ of codebase | Libsodium encryption at rest + in transit, zero downtime migration | 100% PHI compliance; zero security incidents |
| 4 | Guardrails before action | Magizhs intern: validation guardrails blocking non-compliant drone missions | LLM reasoning could produce FAA violations | Deterministic rule engine checks every output before export | FAA altitude + battery + no-fly-zone validation pre-export | Zero non-compliant missions exported; grounded, cited rejection reasons |
| 5 | GTM automation | ClickHouse GTM context + Entrata Salesforce/Clay/n8n | GTM workflows running on manual CRM operations | Automate reporting, data sync, and workflow orchestration | Salesforce API integrations, custom objects, Clay + n8n pipelines | CRM workflows automated across commercial systems |

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Posting freshness | Active on Ashby with specific JD | Positive |
| Description quality | Technical and specific: evals, guardrails, blast radius, multi-harness — language from practitioners | Positive |
| Company | OpenRouter is a real, active company with $200M+ funding and 300+ model integrations | Positive |
| H-1B sponsorship | Not disclosed; very small company (~20 ppl); sponsorship uncertain | Caution |

**Recommended action:** Strong match technically. Confirm H-1B sponsorship before applying. If confirmed, this is a top-tier application.

---

## Machine Summary

```yaml
company: OpenRouter
role: Applied AI Engineer
date: 2026-07-25
score: 4.4
archetype: Applied AI Engineer / Agentic Automation
status: Evaluated
pdf: output/cv-venkata-lakshmi-parimala-pasupuleti-openrouter-2026-07-25.pdf
report: reports/154-openrouter-applied-ai-engineer-2026-07-25.md
comp_range: undisclosed ($130K-$180K est)
h1b_risk: unconfirmed
notes: Direct evals/observability match via AgentProbe; multi-harness patterns; confirm sponsorship before applying
```
