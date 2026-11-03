# 554 — Uber · Sr Software Engineer, Experimentation Platform

**Date:** 2026-10-15
**Score:** 3.8/5
**URL:** https://www.uber.com/global/en/careers/
**PDF:** ✅
**Legitimacy:** High Confidence (Uber, NYSE: UBER)
**Verification:** confirmed (public JD, major employer)
**Note:** Shared CV with #552 (Code Lifecycle) and #553 (third Uber role)

---

## A — Role & Archetype Fit

**Archetype:** SWE — Data Infrastructure / Experimentation Platform

**Score: 4.0/5**

This role sits at the intersection of data engineering, distributed systems, and statistical experimentation — a closer match to Parimala's actual background than #552 (Code Lifecycle / Go monorepo). The Experimentation Platform team builds A/B testing infrastructure, experiment metric pipelines (Spark/Presto), causal inference productionization, and anomaly detection dashboards at Uber scale.

Key alignment angles:
- **GMU M.S. Data Analytics Engineering** — causal inference, statistical analysis, and experimental design are core curriculum topics; CrashClarity project (104K records, Random Forest, statistical significance testing) directly maps to "statistics for experiment analysis"
- **AgentProbe** — built an A/B experimentation framework that runs controlled tests across five LLM providers with statistical scoring; directly analogous to the experimentation methodology this role builds
- **Intuit** (with new framing): PySpark batch pipeline optimization, feature flag progressive delivery, A/B experimentation for LLM provider comparison, real-time dashboards and anomaly detection
- **Python (9+ years)** — the primary stack for this role; strong match
- **Distributed systems at scale** — Entrata 100K+ MAU, RabbitMQ async batch workflows, 1.6M+ record data pipelines

Primary gap: Go is still listed as preferred (not required); the role is more Python/Spark/Java-centric than #552. Parimala's stack aligns much better here.

---

## B — Technical Skills Match

**Score: 3.8/5**

| Requirement | Candidate | Gap |
|---|---|---|
| 5+ years SWE | 9+ years (Python/Java) | None |
| Go / Java / Python | Python (9+ yrs), Java (9+ yrs), Go (learning) | Minor for Go |
| Distributed systems: caching, sharding, consensus, fault tolerance | Entrata (multi-tenant, async batch, AWS) | Minor — domain differs |
| Debugging production-scale systems | 7+ years Entrata, CI/CD + observability at Intuit | None |
| Observability | Prometheus, Grafana, OpenTelemetry | None |
| Statistics / causal inference / experimental design | GMU M.S. coursework, CrashClarity (statistical modeling) | Moderate — academic, not production |
| A/B testing / quasi-experimental | AgentProbe (LLM provider A/B), Intuit framing | Moderate — different domain |
| Marketplace simulations | No direct experience | Major |
| PySpark / Spark / Presto / Pandas / Jupyter | PySpark (Intuit), Pandas (multiple projects), Jupyter (CrashClarity) | Minor for Presto/Scala |
| Feature flags / progressive delivery | Implemented at Intuit for LLM rollouts | Good match |
| Anomaly detection, real-time dashboards | Built at Intuit for LLM service monitoring | Good match |
| Causal inference model productionization | AgentProbe evaluation APIs; academic foundation | Moderate — not causal inference at Uber scale |
| Spark/Presto data pipelines for experiment metrics | PySpark at Intuit; no Presto production experience | Moderate |

Gaps are real but smaller than #552. The main gap is production-scale experimentation in a marketplace context (marketplace simulations, causal inference at Uber's traffic volume). The academic + project foundation is credible.

---

## C — Domain & Industry Fit

**Score: 3.8/5**

Experimentation platforms are core infrastructure at any data-driven tech company — they sit between data engineering, statistics, and product analytics. Parimala's background spans data pipelines (Entrata), statistical analysis (GMU coursework + CrashClarity), and experimentation tooling (AgentProbe).

The marketplace simulation angle (Uber's two-sided marketplace: drivers + riders) has no direct equivalent in her background. However, the statistical experimentation methodology transfers — an A/B testing framework is an A/B testing framework, whether for LLM providers or pricing algorithms.

Uber is a top-tier employer ($202K–$224K + bonus + equity). SF 50% in-office is acceptable per memory (open to any US location, onsite/hybrid fine). Senior IC bar at Uber is rigorous — consistent with the strategy note to avoid multi-round FAANG loops, but this role's focus on Python/data pipelines reduces the pure SWE algorithm bar somewhat in favor of systems + stats depth.

---

## D — Compensation & Level

**Score: 4.2/5**

$202,000–$224,000 base + bonus + equity — top-of-market, no comp floor (per memory 2026-07-30). Sponsorship unknown; Uber has a strong H1B track record. Level is Senior IC (comparable to L5/L6 at Uber). Given the strategy shift away from formal-leveling FAANG loops, this is a borderline case — the role is data/experimentation-focused rather than pure SWE, which may mean a different technical bar than a core distributed systems Senior SWE screen.

---

## E — Growth & Strategic Value

**Score: 3.8/5**

Experimentation platforms are one of the most transferable infrastructure domains in tech — every data-driven company (DoorDash, Airbnb, Stripe, Snowflake, Databricks) runs an experimentation team. Building on the statistics + data engineering foundation from GMU and the AgentProbe project, this role would significantly strengthen Parimala's "applied AI / data systems" narrative. Better strategic alignment than #552 (Go monorepo) — this compounds with her existing trajectory.

Caveat: the strategy shift (2026-07-30) prioritizes PropTech, mid-level, and shorter interview loops. Uber remains a multi-round FAANG-tier loop. Score is 3.8/5 — above the 3.5 at which to consider, below the 4.3 fast-track threshold.

---

## F — Red Flags & Risks

- **Marketplace simulation gap** — Uber's experimentation team works on two-sided marketplace dynamics (surge pricing, driver allocation). No equivalent background. Would surface in technical screen.
- **Production causal inference at scale** — academic foundation + small-project framing may not hold up against candidates with production experience at Lyft/DoorDash/Airbnb experimentation teams.
- **Senior bar at formal-leveling company** — per memory, consistent rejection pattern at Senior level at formal-leveling companies. Uber's bar is high.
- **Score is 3.8/5** — above the 3.5 floor but below the 4.3 fast-track threshold (per memory: Quick Score First). User explicitly requested pipeline; proceeding.
- **Go still in preferred list** — not a hard requirement here, but Uber's Senior SWEs are expected to ramp on Go. Less of a blocker than #552.

---

## G — Posting Legitimacy

**Tier: High Confidence**

Uber (NYSE: UBER) is publicly traded. Experimentation Platform teams at Uber are well-documented in engineering blog posts (Uber Engineering Blog has published articles on their experimentation infrastructure). Salary band matches Uber's published Senior SWE ranges. No legitimacy concerns.

---

## H — Recommendation

**Optional apply (3.8/5 — borderline, user call).**

This is the strongest of the three Uber roles for Parimala's actual background. The Python + data pipelines + statistical analysis + experimentation angle aligns significantly better than #552. The CV has been updated to front-load these terms: A/B testing, causal inference, experimental design, PySpark, feature flags, anomaly detection.

**Strongest angles to lead with in application:**
1. GMU M.S. Data Analytics Engineering = causal inference, statistical analysis, experimental design (directly named in JD preferred qualifications)
2. AgentProbe = open-source A/B experimentation framework for LLM evaluation — same methodology, different domain
3. PySpark / batch pipeline optimization at Intuit + large-scale data pipelines at Entrata (1.6M+ records)
4. 9+ years Python + Java; production distributed systems ownership

**If applying:** Tailor cover letter to lead with the statistics/experimentation angle, not the LLM/AI angle. The hiring team is looking for someone who thinks in terms of statistical significance, experimental validity, and metric pipeline correctness — not someone who fine-tuned a model.

---

## Story Bank Additions

**STAR: A/B Experimentation Framework (AgentProbe)**
- *Situation:* Needed to compare LLM providers (Anthropic, OpenAI, Azure OpenAI, Groq, Ollama) for production use at Intuit; no off-the-shelf tool met evaluation requirements
- *Task:* Build a controlled experimentation system that could run parallel provider tests with statistically sound scoring
- *Action:* Built AgentProbe — 15-endpoint FastAPI backend, LLM-as-judge scoring on accuracy/hallucination/retrieval quality, CI regression harness with golden datasets, statistical comparison across providers
- *Result:* Evaluated 1,240+ test cases; statistically significant accuracy comparisons guided provider selection; caught 3 regressions pre-release
- *Relevance:* Maps directly to "build A/B testing experimentation frameworks, productionize causal-inference models into APIs"

**STAR: Large-Scale Statistical Analysis (CrashClarity / GMU)**
- *Situation:* M.S. capstone project requiring end-to-end statistical analysis and ML pipeline on real-world data
- *Task:* Analyze 104K+ accident records, build ML classifiers, apply causal inference and statistical significance testing
- *Action:* Feature engineering in Pandas/Jupyter, Random Forest + Logistic Regression (85%+ accuracy), statistical significance tests, interactive dashboard
- *Result:* Demonstrated causal analysis methodology; published as portfolio project
- *Relevance:* Maps to "statistics, causal inference, experimental design" in JD preferred qualifications

---

## Machine Summary

```yaml
report: 554
company: Uber
role: Sr Software Engineer Experimentation Platform
date: 2026-10-15
score: 3.8
archetype: SWE — Data Infrastructure / Experimentation Platform
location: San Francisco (50% in-office)
workplace: Hybrid
salary_range: "$202,000–$224,000"
sponsorship: unknown
legitimacy: high_confidence
recommendation: optional_apply
shared_cv_with:
  - 552
  - 553
primary_strengths:
  - GMU M.S. Data Analytics Engineering (causal inference, stats, experimental design)
  - AgentProbe A/B experimentation framework for LLM provider comparison
  - PySpark batch pipeline optimization (Intuit)
  - Feature flags / progressive delivery (Intuit)
  - Real-time dashboards + anomaly detection (Intuit)
  - 9+ years Python + Java; 1.6M+ record data pipeline ownership (Entrata)
primary_gaps:
  - Marketplace simulation (Uber-specific two-sided marketplace dynamics)
  - Production causal inference at platform scale (academic/project foundation only)
  - Go (preferred, not required; less critical than #552)
strategy_note: "3.8/5 — borderline; best of 3 Uber roles; user requested pipeline; strongest angle = stats/causal inference + AgentProbe as experimentation proxy"
```
