# 101 — Zillow · Machine Learning Engineer, Shopping AI

**Date:** 2026-06-22
**Score:** 4.1/5
**URL:** https://zillow.wd5.myworkdayjobs.com/en-US/Zillow_Group_External/job/Remote-USA/Machine-Learning-Engineer--Zillow-Shopping-AI_P747947-1
**PDF:** ❌ (below 4.5 cutoff)
**Legitimacy:** High Confidence — Zillow is NASDAQ-listed (Z), posting appears on Workday, LinkedIn, BuiltIn, multiple boards

---

> ⚠️ **Score 4.1 — below 4.5 cutoff.** Main gaps: role is consumer shopping ML (recommendations, ranking, semantic search) not PropTech SaaS; prefers "large consumer tech" background; Spark/Databricks/Airflow are expected (not in stack). Real estate domain checks out but product context is different.

---

## Block A — Role Summary

| Field | Detail |
|---|---|
| Archetype | ML Engineer (Consumer Real Estate) |
| Domain | Consumer real estate marketplace, shopping personalization |
| Function | Build and own production ML systems for ranking, recommendations, semantic search |
| Seniority | Mid-level (BS+4 or MS+2) |
| Location | Remote USA |
| Comp | $138,300–$232,500 base (varies by state) |
| TL;DR | Build production ML models powering Zillow's core home-shopping experience — ranking, recommendations, autocomplete, LLMs |

---

## Block B — Match with CV

| JD Requirement | CV Evidence | Strength |
|---|---|---|
| Python | 8+ years production Python at Entrata | ✅ Strong |
| LLMs / GenAI experience | AgentProbe (multi-provider LLM routing, LLM-as-judge); LeaseI (LangGraph RAG + compliance) | ✅ Strong |
| Production ML systems | Entrata: AI pipeline on 1.6M financial records; AgentProbe: 15-endpoint FastAPI backend | ✅ Good |
| Real estate domain | 8 years Entrata — tenant, property, lease, affordable housing | ✅ Good — different product but same sector |
| BS + 4 years or MS + 2 years | MS May 2026 + 2 years AI/ML project work; 8 years SWE overall | ✅ Meets bar |
| Personalized ranking / recommendations | ❌ None — different ML paradigm from what she has built | Hard gap |
| Hive / Spark / Airflow / Databricks | ❌ Not in stack | Gap |
| Large consumer tech background (preferred) | ❌ Entrata is mid-size B2B SaaS, not large consumer tech | Preference miss |
| Offline experimentation → online A/B testing → monitoring | ❌ No A/B testing or online ranking experiment experience | Gap |

### Gaps
- **Recommendation systems / ranking** — core ML paradigm for this role; her models are classification/regression/RAG, not collaborative filtering or learning-to-rank. Hard to bridge without a side project.
- **Spark/Databricks/Airflow** — expected for large-scale data processing. She has PostgreSQL, RabbitMQ, AWS Glue — adjacent but not identical.
- **"Preferably large consumer tech"** — this is a soft preference, not hard requirement, but it narrows the field. Entrata has 100K+ MAU and 1M+ records — that's real scale, just B2B.
- **A/B testing** — Zillow's production ML depends heavily on online experimentation. She has quality gates and CI/CD (AgentProbe) but no A/B testing track record.

---

## Block C — Level & Strategy

**Level:** Mid-level (BS+4 or MS+2). Parimala has 8 years SWE + MS — she meets the bar technically, but her ML is RAG/classification, not ranking/recommendations.

**The honest position:** She's strong on LLMs and production engineering but the Shopping AI team needs someone with recommendation systems experience. Her real estate domain knowledge is a plus, but this team builds shopping UX (search result ranking, display optimization), not property management tooling. The overlap is domain (real estate) but not product type (consumer marketplace vs. SaaS).

**If they interview:** Lead with the LLM/GenAI angle (they're pioneering LLM applications to shopping) and 8 years of real estate data experience. Be transparent that recommendation systems aren't your primary expertise but GenAI + real estate is a strong combo for what they're explicitly building.

---

## Block D — Comp

| State group | Base range |
|---|---|
| CA, WA, NY, NJ, CT, MA, MD, DC | $145,500–$232,500 |
| CO, HI, IL, MN, NV, OH, RI, VT | $138,300–$220,900 |
| All other US | $138,300–$220,900 |

Zillow MLE total comp (Levels.fyi): $256K–$292K+ with equity. Strong comp for mid-level. H-1B sponsorship: Zillow is an active H-1B sponsor.

---

## Block E — Why 4.1 Not 4.5

| Factor | Score |
|---|---|
| CV match | 3.5 — Python/LLM strong; ranking/recommendations/Spark are hard gaps |
| North Star fit | 3.8 — ML Engineer (real estate) yes, but consumer shopping ≠ PropTech SaaS |
| Comp | 5.0 — top of market |
| Company quality | 4.5 — NASDAQ-listed, strong H-1B sponsor, stable |
| Red flags | -0.5 — consumer tech preference miss, missing key stack (Spark, A/B testing, ranking) |
| **Global** | **4.1/5** |

---

## Block G — Posting Legitimacy

**High Confidence.**
- Zillow is publicly traded (NASDAQ: Z / ZG), actively hiring ML engineers
- Role on Zillow Workday system (direct): confirmed 200 OK
- Appears on LinkedIn, BuiltIn, Jobgether, Remote Source — broad distribution
- Salary band disclosed = legitimacy signal
- Confirmed live as of 2026-06-22

## Machine Summary

```yaml
id: 101
company: Zillow
role: Machine Learning Engineer, Shopping AI
date: 2026-06-22
score: 4.1
status: Evaluated
pdf: false
url: https://zillow.wd5.myworkdayjobs.com/en-US/Zillow_Group_External/job/Remote-USA/Machine-Learning-Engineer--Zillow-Shopping-AI_P747947-1
location: Remote USA
comp_base: "$138,300–$232,500"
archetype: ML Engineer
domain: Consumer Real Estate
verdict: below_cutoff
skip_reason: "Consumer shopping ML (ranking/recommendations/Spark) — different paradigm from her RAG/classification stack; consumer tech preference miss"
```
