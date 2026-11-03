# Evaluation: Nordstrom — Senior Software Engineer, AI Agentic Solutions (PDLC)

**Date:** 2026-10-02
**URL:** https://careers.nordstrom.com
**Archetype:** Agentic / Automation + AI Platform / LLMOps
**Score:** 4.7/5
**Legitimacy:** High Confidence
**PDF:** output/508-nordstrom-senior-swe-agentic-ai-2026-10-02.pdf

---

## A) Role Summary

| Attribute | Detail |
|---|---|
| **Archetype** | Agentic AI Engineer — all four pillars |
| **Domain** | Retail / E-Commerce — AI Agentic Solutions |
| **Function** | Build production agentic AI across commerce, personalization, inventory, customer service |
| **Seniority** | Senior IC (6+ years) |
| **Location** | Seattle, WA — Hybrid |
| **Comp** | $142K–$220.5K |
| **Sponsorship** | Not stated; Nordstrom Fortune 500, H-1B history |

---

## B) Match Analysis

### Strong Fits — All Four Team Pillars

| Nordstrom Pillar | Direct Proof Point |
|---|---|
| **Evaluations & Guardrails** | AgentProbe: CI regression harness, LLM-as-judge, offline benchmarks, online telemetry, golden datasets |
| **Agent Engineering** | LeaseI: 8-agent LangGraph, tool-use, multi-agent orchestration, HITL |
| **Context Engineering** | LeaseI: RAG retrieval, token-aware context assembly, citation grounding, hybrid search |
| **Memory & State Management** | LeaseI: durable workflow state, SQLite knowledge repository, session state |

- **LangGraph explicitly named** in JD — production LangGraph experience ✅
- **Anthropic API** (Claude Agent SDK adjacent) ✅
- **Open-source AI contributions** (nice-to-have hit) — AgentProbe ✅
- **Responsible deployment / responsible AI** — HITL, audit logging, hard safety boundaries in code ✅
- **Failure-mode analysis** — 300+ postmortems at Entrata, built internal debugging tools ✅
- **Python + AWS + CI/CD + Docker** ✅
- **Product-minded** — forward-deployed delivery across Entrata + Magizhs ✅

### Gaps
- Retail/e-commerce domain — no direct experience; customer-facing 100K+ MAU Entrata is a workable analog
- Spark/BigQuery (nice-to-haves only) — not production-used
- Visa sponsorship not confirmed — Nordstrom H-1B history but not stated in JD

---

## C) ATS Patch Log

| Term | Added To |
|---|---|
| `context engineering` | Summary, LeaseI bullet |
| `token economics` / `token efficiency` | AgentProbe bullet |
| `memory and state management` | LeaseI — explicit phrase |
| `durable workflow state` | LeaseI — patched from "durable state" |
| `failure-mode analysis` | Entrata bullet |
| `offline benchmarks` + `online telemetry` | AgentProbe bullet |
| `responsible deployment` | Summary |
| `product-minded` | Summary |

Post-patch ATS: ~96%

---

## D) Score Breakdown

| Dimension | Score | Notes |
|---|---|---|
| Role fit | 5.0 | All four team pillars = direct proof points; LangGraph + Anthropic + AgentProbe + LeaseI |
| Domain | 4.0 | No retail exp; 100K+ MAU customer-facing systems is workable analog |
| Location | 4.0 | Hybrid Seattle; user open to any US location |
| Comp | 4.8 | $142–220K — strong range |
| Sponsorship | 3.5 | Not stated; Fortune 500, likely capable |
| **Weighted** | **4.7** | Strong apply |

---

## E) Recommendation

**Apply — 4.7/5.** Highest-scoring role this session. All four team pillars map to existing proof points. LangGraph named explicitly. AgentProbe hits the open-source nice-to-have directly. Confirm sponsorship in first screen.

---

## G) Posting Legitimacy

**Tier: High Confidence** — Nordstrom active careers page, specific team description, comp range disclosed, Seattle hybrid details confirmed.

---

## Machine Summary

```yaml
company: Nordstrom
role: Senior Software Engineer — AI Agentic Solutions (PDLC)
archetype: agentic_ai_llmops
score: 4.7
apply: true
location: Seattle WA hybrid
sponsorship: not_stated_fortune500
comp_range: 142k-220k
key_match: all_four_pillars + langgraph_explicit + agentprobe_evals + leaseI_agentic
gaps: [retail_domain, spark_bigquery, sponsorship_unconfirmed]
ats_coverage: 96pct
report: 508-nordstrom-senior-swe-agentic-ai-2026-10-02.md
```
