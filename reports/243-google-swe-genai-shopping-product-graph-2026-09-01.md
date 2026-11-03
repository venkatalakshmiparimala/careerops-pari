# Evaluation: Google — Software Engineer, Generative AI, Shopping Product Graph (Commerce)

**Date:** 2026-09-01
**URL:** (pasted — verify on careers.google.com)
**Archetype:** Applied AI / GenAI SWE (E-commerce domain — off-target)
**Score:** 3.5/5
**Legitimacy:** High Confidence
**PDF:** —

---

## A) Role Summary

| Dimension | Detail |
|-----------|--------|
| Archetype | Applied GenAI SWE — build ML/LLM systems for Google's Shopping Product Graph: large-scale clustering, LLM inference to extract product facts, product modeling powering AI Mode Search, Ads, YouTube |
| Team | Google Commerce — Shopping Product Graph; powers 1B+ daily shopping queries |
| Function | Write product/system code; implement GenAI solutions; ML infrastructure; data preparation; debug/triage system issues |
| Seniority | **$147K–$210K** → L4/L5 at Google. No hard block. |
| Location | Pittsburgh, PA — in-person interviews required; relocation needed from Virginia |
| Comp | **$147,000–$210,000 + 15% bonus + equity** |
| H-1B | Google is a tier-1 H-1B sponsor ✅ |
| TL;DR | Minimum quals all met (Python, M.S., ML infra, GenAI). Two preferred quals match precisely: AgentProbe = "AI auto-raters" and LeaseI = "1yr GenAI agents." Core domain gap: shopping/product graph/e-commerce — no product data, merchant, or clustering-at-scale experience. Score 3.5/5 — below 4.5 general threshold. |

---

## B) Match with CV

### Minimum Qualifications

| Requirement | CV Match | Quality |
|-------------|----------|---------|
| Bachelor's degree | B.Tech CS + M.S. Data Analytics Engineering ✅ | STRONG |
| 2yr software dev in Python/C++/SQL (or 1yr with advanced degree) | M.S. + 8yr Python → 1yr threshold met 8× over | STRONG |
| **1yr ML infrastructure (model deployment, evaluation, optimization, data processing, debugging)** | **AgentProbe: model evaluation, data processing, debugging ✅; LeaseI: FastAPI model deployment ✅; ML infra coverage is partial (no SageMaker/Vertex/TFX at scale)** | MODERATE |
| GenAI techniques/concepts (LLMs, language modeling) | LangChain, LangGraph, OpenAI API, Anthropic API, RAG, LLM-as-judge — production usage | STRONG |

### Preferred Qualifications

| Requirement | CV Match | Quality |
|-------------|----------|---------|
| Master's degree in CS or related | M.S. Data Analytics Engineering, GPA 3.87 | STRONG |
| 2yr data structures and algorithms | B.Tech CS curriculum; GMU coursework | MODERATE |
| **1yr experience building Generative AI Agents** | **LeaseI (8-agent LangGraph, 2026) + Magizhs agentic planner (2025) — two shipped agentic systems** | **STRONG** |
| **1yr developing AI auto-raters and agentic systems to assess headroom and improve quality** | **AgentProbe: LLM-as-judge, 5-metric eval engine, pass@k harness, CI regression gate — this IS an AI auto-rater system** | **EXACT MATCH** |
| Experience exploring web/merchant data sources to improve ML/product understanding | No web scraping, merchant data, or product catalog experience | GAP |
| Experience developing accessible technologies | No accessibility development experience | GAP |

### Responsibilities

| Responsibility | CV Match | Quality |
|----------------|----------|---------|
| Write product/system development code | 20+ production modules, 8yr Python | STRONG |
| Design/code reviews, best practices | 300+ peer code reviews, 120+ Agile sprints | STRONG |
| Triage/debug/resolve product issues | RCA ownership at Entrata; AgentProbe debugging dashboard (40% reduction) | STRONG |
| **Implement GenAI solutions, ML infrastructure, data preparation** | **LangGraph agentic systems ✅; FastAPI serving ✅; data pipelines (ETL, HUD import) ✅; but no product-graph-scale ML infrastructure** | MODERATE |
| Contribute to documentation/educational content | GMU teaching (600+ students); AgentProbe README | MODERATE |

---

## C) Assessment

**No hard block fires.**

Salary $147K–$210K = L4/L5 at Google (not L6/L7 Staff tier). Title is "Software Engineer" — not Senior/Staff. No language hard block (Python ✅). No clearance required. Pittsburgh requires relocation from Virginia — user is open to onsite.

**Two preferred quals are precise matches — rare for this pipeline.**

"1 year developing AI auto-raters and new agentic systems to assess headroom and improve quality" — this is the most specific preferred qual in the posting, and AgentProbe is an exact answer. LLM-as-judge is an auto-rater. Pass@k harness assesses headroom. CI regression gate measures quality improvement. This is not a stretch.

"1 year building Generative AI Agents" — LeaseI (8-agent, 2026) + Magizhs (LangGraph agentic planner, 2025) = two shipped agentic systems.

**The domain gap is the blocker.**

The Shopping Product Graph team does three things at its core:
1. **Large-scale ML clustering** on billions of product records — grouping similar products across merchants
2. **LLM inference at scale** to extract product attributes, facts, and features
3. **Product understanding** — modeling what a "product" is across different representations from different merchants

None of these are in the CV. The closest proof points are LLM inference (LeaseI, AgentProbe) and data pipelines (HUD import) — but at housing-compliance scale (180K records), not at product-graph scale (billions of products). A recruiter screening for "Shopping Product Graph" experience will flag the absence of e-commerce, merchant data, product taxonomy, or clustering domain.

**What is genuinely interesting:**

The "AI auto-raters" callout is rare — most JDs don't name this pattern explicitly. AgentProbe is exactly what they're describing: automated quality assessment of LLM/agent outputs. If the team is prioritizing evaluation infrastructure candidates, this is a genuine differentiator.

**Google LeetCode prereq applies.** Even at L4/L5, Google conducts 2-3 DSA coding rounds (medium-hard), a system design round, and a behavioral round. Same prep requirement as #229 (Launch) and #220 (SecLM).

**Score: 3.5/5** — below 4.5 general threshold.

| Factor | Weight |
|--------|--------|
| Preferred qual: AgentProbe = AI auto-raters (exact) | ++ |
| Preferred qual: LeaseI + Magizhs = GenAI agents (1yr) | ++ |
| Python, M.S., GenAI min quals met | + |
| Google H-1B tier-1 | + |
| E-commerce/shopping/product graph domain gap | --- |
| Large-scale clustering gap | -- |
| Merchant/web data exploration gap | - |
| Pittsburgh relocation needed | - |
| LeetCode DSA prep required before applying | - |

---

## D) Comp

| Metric | Value |
|--------|-------|
| Base | $147,000–$210,000 |
| Bonus | 15% target |
| Equity | Google RSUs |
| TC estimate | $185K–$260K |
| H-1B | Tier-1 ✅ |
| Comp score | 5.0/5 |

---

## E) Recommendation

**SKIP** — below 4.5 general threshold. Shopping/product graph domain gap will block recruiter screen. No e-commerce, merchant data, product taxonomy, or clustering-at-scale experience.

If you have any shopping/product/merchant data experience to surface (even tangential — price comparison, catalog work, recommendation systems), reconsider. Without it, apply only if you're willing to invest the 3–4 week LeetCode prep and accept a likely screen rejection on domain fit.

**If user overrides:** Frame around "AI auto-raters" (AgentProbe) and "GenAI agents" (LeaseI) — skip trying to bridge the product graph domain and let the eval infrastructure angle carry the application.

---

## G) Posting Legitimacy

**High Confidence**

| Signal | Finding |
|--------|---------|
| Company | Google — verifiable on careers.google.com |
| Team | Shopping Product Graph, Commerce — specific named team with described mission |
| Salary | $147K–$210K posted explicitly — Google standard L4/L5 band |
| In-person | "In most instances, this position requires in-person interviews" — standard Google language |

---

## Machine Summary

```yaml
company: Google
role: Software Engineer, Generative AI, Shopping Product Graph (Commerce)
date: 2026-09-01
score: 3.5
archetype: Applied GenAI SWE (E-commerce domain — off-target)
legitimacy: High Confidence
recommend: SKIP — below 4.5 general threshold; shopping/product graph domain gap; no e-commerce/merchant/clustering-at-scale experience; AgentProbe=AI auto-raters is a genuine match but domain will block screen
comp_low: 147000
comp_high: 210000
comp_bonus: 15% target
comp_tc_est: 185000-260000
location: Pittsburgh, PA (in-person interviews; relocation needed)
h1b_sponsor: yes — Google tier-1
hard_block: NO — $147K-$210K = L4/L5 (not L6/L7); "Software Engineer" title; Python not excluded
key_gap: shopping/e-commerce/product graph domain; large-scale ML clustering; merchant/web data exploration; LeetCode DSA prep required
key_strength: AgentProbe = AI auto-raters (exact preferred qual match); LeaseI+Magizhs = GenAI agents (1yr preferred qual); Python; M.S.; Google H-1B tier-1
priority: skip — 3.5/5, below 4.5 general threshold
```
