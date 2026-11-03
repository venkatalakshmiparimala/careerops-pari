# Evaluation: Glean — Machine Learning Engineer, LLM Evals & Observability

**Date:** 2026-06-03
**URL:** https://job-boards.greenhouse.io/gleanwork/jobs/4694716005
**Archetype:** AI Platform / LLMOps
**Score:** 4.1/5
**Legitimacy:** High Confidence
**PDF:** output/cv-glean-2026-06-03.pdf

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | AI Platform / LLMOps |
| Domain | LLM evaluation pipelines, observability, AI agent quality |
| Function | Build |
| Seniority | Mid-Senior (2+ years required; 8+ matched) |
| Remote | Hybrid 3-4 days/week — Mountain View, CA (SF Bay Area) |
| Comp | $200K–$300K base + variable + equity |
| TL;DR | Build the eval and observability layer for Glean's AI assistant — large-scale pipelines, LLM judges, trace dashboards, and automated prompt iteration — to prevent regressions before every release. |

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| 2+ years SWE experience | 8+ years at Entrata (2017–2024) | ✅ Exceeds |
| Python proficiency | Entrata, AgentProbe (Python/FastAPI), AI on FHIR (Flask), CrashClarity | ✅ Strong |
| Go proficiency | Not in stack — Go AND Python listed as required | ⚠️ Real gap |
| LLM evaluation | AgentProbe: 5-metric eval engine (factual accuracy, hallucination, retrieval, completeness, compliance) | ✅ Direct proof |
| LLM-powered judges | AgentProbe uses LLMs to evaluate LLM outputs — same pattern | ✅ Direct proof |
| Observability for AI agents | AgentProbe: trace enrichment (RAG Tracer agent), dashboards (React) | ✅ Direct proof |
| Distributed data pipelines | AWS Glue + S3 pipelines at Entrata; Python ETL; distributed microservices | ✅ Adjacent |
| RLHF experience | Not in CV | ⚠️ Gap |
| NLP / large ML systems | spaCy, BERT, embeddings (AI on FHIR); scikit-learn, RF, LR (CrashClarity) | ✅ Adjacent |
| Analytical rigor / offline metrics | 5-metric eval engine design; 30% DB perf improvement via measurement | ✅ Strong |
| Cross-functional, customer-focused | 120+ Agile sprints; 100K+ MAU at Entrata | ✅ Strong |
| Eval dataset design (sampling, diversity) | Not explicitly in CV | ⚠️ Soft gap |

**Gaps and mitigations:**
- **Go** — Hard: listed as required alongside Python. Mitigation: lead with Python depth, note willingness to ramp; Go and Python share concurrency patterns. Not a dealbreaker at a company that also lists Python.
- **RLHF** — Soft: feedback loop from human preference signals. AgentProbe's Auto Fix agent is adjacent (uses eval outputs to iterate). Mitigate by framing AgentProbe as automated quality iteration.
- **Eval dataset design** — Soft: not explicitly in CV but the mindset (sampling strategies, coverage) maps to ML project work (CrashClarity feature engineering). Mention eval design thinking in cover letter.
- **Distributed data pipelines at scale** — Soft: AWS Glue + S3 pipelines mitigate; Entrata's 1M+ record system demonstrates distributed systems thinking.

---

## C) Level and Strategy

**Level detected:** Mid-senior (2+ years minimum, role scope suggests senior/staff). Parimala at 8+ years is well above minimum — positioned as a strong senior hire.

**Sell senior plan:**
- Lead with AgentProbe as a production demonstration of the exact eval/observability system Glean is building — 5-metric eval engine, LLM judges, trace dashboards
- Frame Entrata scale (1M+ records, distributed microservices) as proof of data pipeline maturity
- Quote: *"I built AgentProbe specifically because I needed a reliable eval framework for RAG and multi-agent systems. The 5-metric engine — factual accuracy, hallucination, retrieval, completeness, compliance — is the same surface area this role owns."*

**If they downlevel:** Accept if base ≥ $170K with equity; request 6-month review tied to eval pipeline delivery metrics.

---

## D) Comp and Demand

| Source | Range | Notes |
|--------|-------|-------|
| Job posting | $200K–$300K base + equity | Listed directly |
| Market (Levels.fyi, 2026) | $180K–$260K | MLE at enterprise AI unicorn |
| Glean valuation | ~$2.2B | Series F, strong equity upside |

**Assessment:** $200K–$300K base is 43–115% above Parimala's $100K–$140K target. This is a significant step-up opportunity with meaningful equity at a high-valuation company. H-1B sponsorship highly likely (established 200+ person company, tech-heavy workforce).

---

## E) Customization Plan

| # | Section | Current | Proposed change | Why |
|---|---------|---------|-----------------|-----|
| 1 | Summary | Generic SWE + AI builder | Lead with: *"ML engineer specializing in LLM evaluation pipelines and AI observability — built AgentProbe, a 5-metric eval engine with LLM judges, trace dashboards, and automated fix agents"* | Mirrors JD language exactly |
| 2 | AgentProbe bullet | General description | Add: *"Designed LLM-powered judges scoring correctness, completeness, and response quality — the same eval surface the Glean role owns"* | Maps proof to JD requirement |
| 3 | AgentProbe bullet | Mentions eval metrics | Add: *"Built trace enrichment pipeline and React observability dashboard for agent run visualization"* | Hits observability + dashboards requirement |
| 4 | Entrata pipeline bullet | AWS S3 migration | Reframe as: *"Built distributed data pipelines on AWS (S3, Glue, EC2) processing 1M+ records with automated quality checks and zero security incidents"* | Surfaces distributed pipeline depth |
| 5 | Skills | Python listed | Add: *"Go (familiar, actively ramping)"* | Addresses Go gap honestly |

---

## F) Interview Plan

| # | JD Requirement | Story | S | T | A | R | Reflection |
|---|----------------|-------|---|---|---|---|------------|
| 1 | LLM eval pipelines + judges | AgentProbe 5-metric eval engine | No reliable pre-deployment LLM testing tool | Build eval framework for RAG and multi-agent systems | LLM-as-judge pattern: LLM Router queries evaluator models for each metric | 5-metric eval engine, catches hallucinations and retrieval failures before deploy | Would add confidence intervals on judge scores from day one |
| 2 | Observability for AI agents | AgentProbe RAG Tracer + dashboard | Agents failed silently — no trace visibility | Build trace enrichment and visualization | LangGraph RAG Tracer agent + React dashboard with per-query breakdown | Full trace visibility: retrieval → generation → eval score per query | Async trace streaming matters — sync was too slow at scale |
| 3 | Regression prevention | Entrata quality discipline | Frequent regressions in multi-module system | Establish quality gates before release | TDD/BDD, peer code reviews, integration test suite | Sub-10 bug count for 6+ consecutive months | Automated gate > manual review: build the check, not the checker |
| 4 | Distributed data pipelines | Entrata AWS migration | All client data in manual, insecure processes | Migrate to AWS S3 with automated quality validation | Automated pipelines, Libsodium encryption, quality checks at each stage | 100% PHI compliance, zero incidents, 80% workload eliminated | Schema validation at ingestion catches 80% of downstream issues |
| 5 | Offline metrics and user experience | AgentProbe eval engine design | Hard to know if eval metrics predict real quality | Design metrics that correlate with user satisfaction | 5 metrics chosen based on where RAG systems fail users most (hallucination, incomplete answers) | Metrics are actionable — Auto Fix agent uses them to trigger corrections | Precision of metric matters more than quantity of metrics |

**Case study to present:** AgentProbe eval engine — walk through: query → RAG retrieval → LLM generation → LLM judge scoring → 5-metric output → Auto Fix agent. Frame it as: *"This is the eval loop I'd apply to Glean's assistant at scale."*

**Red flag questions:**
- *"You don't have Go experience — how will you ramp?"* → *"Python and Go share concurrency patterns and typed interfaces. I've read through Go's standard library and the main differences are manageable. I expect 4-6 weeks to be productive; I've ramped into new stacks before."*
- *"Your ML background is project-scale, not production ML at Glean's scale"* → *"Fair. AgentProbe is smaller scale, but the eval system design — judges, trace enrichment, metric selection — is identical. The scale question is an infrastructure challenge, which Entrata's distributed systems background directly addresses."*

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Posting freshness | Active on Greenhouse job board | Positive |
| Apply button | Active | Positive |
| JD specificity | Detailed responsibilities (sampling strategies, LLM judges, trace enrichment), named tech (Go, Python, RLHF) | Positive |
| Company health | No layoffs or hiring freeze announced in 2026; CEO publicly stated AI won't replace workers | Positive |
| Valuation | ~$2.2B Series F — well-funded, growth stage | Positive |
| Salary listed | Yes ($200K–$300K) | Positive |
| Reposting | Not seen in scan-history.tsv | Positive |

---

## Keywords Extracted

llm evaluation, observability, evals pipeline, llm judges, trace enrichment, regression prevention, sampling strategies, query diversity, offline metrics, prompt iteration, rlhf, distributed data pipelines, machine learning engineer, python, go, nlp, ai agents, correctness scoring, completeness scoring, response quality, agentic ai, langchain, langraph, chromadb, fastapi, rag

---

## Machine Summary

```yaml
report_num: 033
company: Glean
role: Machine Learning Engineer, LLM Evals & Observability
date: 2026-06-03
score: 4.1
archetype: AI Platform / LLMOps
legitimacy: High Confidence
location: Mountain View, CA — hybrid 3-4 days/week
comp_range: "$200K–$300K base + equity"
visa_risk: low
key_gaps:
  - Go (real gap — listed as required alongside Python)
  - RLHF (soft gap)
  - Eval dataset design at scale (soft gap)
key_strengths:
  - AgentProbe = direct proof of LLM eval engine + LLM judges + observability
  - 8+ years exceeds 2+ requirement significantly
  - Trace enrichment, dashboards, automated fix agents all demonstrated
  - Exceptional comp ($200-300K base)
location_risk: medium — hybrid 3-4d/wk, Bay Area relocation from Virginia
recommend: strong apply — domain match is exceptional; Go gap is addressable
```
