# Evaluation: Amazon — Senior Business Intelligence Engineer (AI Analytics)

**Date:** 2026-08-19
**URL:** https://amazon.jobs (Senior BIE — AI Analytics)
**Archetype:** BI Engineer / Applied AI Analytics
**Score:** 4.0/5
**Legitimacy:** High Confidence
**PDF:** ❌

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | Senior BIE — AI-focused analytics |
| Domain | AI analytics, executive BI, multi-TB data |
| Function | Build AI tools + automated reporting + executive decision support |
| Seniority | Senior (L5 at Amazon) |
| Location | Not specified in JD (likely Seattle or NYC; verify) |
| Team | AI analytics — cross-functional, product + program metrics |
| Comp | Base not shown in JD; Amazon Senior BIE typical: $140K–$185K base + RSUs + sign-on |
| TL;DR | Build AI tools for business stakeholders + own executive BI dashboards + drive automated insights from large datasets using Python, SQL, AWS stack |

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| Python scripting + automation | Primary language; 80% manual workload eliminated at Entrata | ✅ Strong |
| Advanced SQL | 200+ queries tuned, 30% perf gain, 1.6M+ records | ✅ Strong |
| AWS S3, EC2, RDS | Production: 100% PHI migration, zero incidents | ✅ Strong |
| AI tools for non-technical stakeholders | LeaseI: 3-surface AI platform for compliance ops teams | ✅ Exact match |
| ML / data mining / info retrieval | Random Forest, Isolation Forest, XGBoost, TF-IDF RAG, ChromaDB | ✅ Strong |
| BI space experience | Tableau, Power BI, ggplot2 dashboards; GMU faculty dashboards (40% comprehension boost) | ✅ Match |
| Executive-level decision support | Faculty/leadership dashboards at GMU; dual VP+CRO audience in Capital One project | ✅ Match |
| Master's in quant field | MS Data Analytics Engineering, GPA 3.87, GMU | ✅ Strong |
| AWS Redshift | "Evaluating" in profile — not production | ⚠️ Gap |
| Hadoop | Not in stack; PySpark/Apache Spark adjacent | ⚠️ Gap |
| Multi-TB datasets | 1.6M records at Entrata; not explicitly TB-scale | ⚠️ Gap |

**Gap mitigation:**
- Hadoop: "Experienced with distributed processing via Apache Spark/PySpark; Hadoop is a familiar paradigm — HDFS + MapReduce concepts apply directly."
- Redshift: "Worked with PostgreSQL/Oracle at production scale; Redshift is PostgreSQL-compatible — minimal ramp needed."
- Multi-TB: Frame Entrata's 100K+ MAU at 99.5% uptime as scale signal; Capital One take-home (100K transactions) adds analytical credibility.

## C) Level and Strategy

**The Amazon Senior concern:** Previous rejection was Senior SA (Amazon Connect) — system design + architecture loop. BIE at Amazon has a fundamentally different loop: SQL coding (hard/medium LeetCode-style), analytical case study, BI metrics design, behavioral (Leadership Principles). No system design round. Her SQL strength and analytical background are a much stronger fit for BIE than SA.

**Also note:** This is the 4th Amazon application. Different teams operate independently at Amazon, but ensure the application identity is consistent. Existing applications: #144 (Connect SA — Rejected), #196 (Partner SA AWS SAIL — Applied), #198 (Ring/Blink AI Data Engineer — Evaluated), #205 (WWPS BIE — Evaluated).

**Key framing:** "I build AI tools that business teams actually use — not demos, not prototypes. LeaseI is a 3-surface AI platform that compliance operations teams use for document review and root-cause investigation. AgentProbe is an open-source AI evaluation toolkit. That's the exact profile this role describes: AI tools for non-technical stakeholders derived from real production data."

## D) Comp and Demand

| Source | Range |
|--------|-------|
| JD posted | Not shown (verify on application) |
| Levels.fyi (Amazon Senior BIE) | $140K–$185K base + RSUs (~$50K–$100K/yr) + sign-on |
| Amazon H-1B | Confirmed top sponsor |

High-demand role: AI + BI hybrid is a rare combination Amazon is actively hiring for post-Bedrock push.

## E) Customization Plan

| # | Section | Change | Why |
|---|---------|--------|-----|
| 1 | Summary | Lead with "AI tools for business stakeholders" framing — LeaseI named explicitly | JD is AI-first BI, not traditional BI |
| 2 | LeaseI | Front and center — 3-surface platform, non-technical stakeholder access, compliance ops team | Direct match to "AI tools for non-technical stakeholders" |
| 3 | AgentProbe | Frame as automated insight infrastructure — 5-metric eval engine, CI-integrated | Matches "automated solutions for recurrent reporting" |
| 4 | Entrata | SQL at scale (200+ queries), 1.6M records, ETL pipelines, 100% PHI compliance on S3 | Matches "extract, transform, clean large datasets" + AWS |
| 5 | Skills | Add "AWS Redshift (PostgreSQL-compatible)", "Hadoop (Spark paradigm)", "multi-TB ETL" | ATS coverage |
| 6 | GMU | Tableau dashboards + Isolation Forest = BI + anomaly detection for executive stakeholders | Matches "actionable insights" + "executive decision support" |

## F) Interview Plan

Amazon BIE Power Day: SQL round + analytical case + behavioral (LPs). No system design.

| Round | What They Test | Your Proof Point |
|-------|---------------|-----------------|
| SQL coding | Window functions, CTEs, aggregations, joins on large tables | 200+ SQL queries at Entrata; velocity burst detection SQL from Capital One project |
| Analytical case | "Given this dataset with X problems, what do you do first?" | Capital One take-home: 8 data quality issues found programmatically before analysis |
| BI metrics design | Define a north-star metric for a product | Capital One Q8: defined north-star metric for VP of Field Strategy |
| Behavioral — Customer Obsession | AI tool built for non-technical users | LeaseI: compliance ops teams; tenant self-service safety boundary |
| Behavioral — Invent and Simplify | Automated a painful manual process | Entrata: eliminated 80% manual workload via Python/PL-SQL automation |
| Behavioral — Dive Deep | Found an error others missed | Entrata: PHI pipeline — 50%+ codebase had insecure data paths; found and fixed them all |
| Behavioral — Deliver Results | Quantified business impact | Entrata: 30% query perf gain, 40% debugging time reduction, 99.5% uptime |

**LP stories to lock in:**
1. **Customer Obsession** → LeaseI: designed tenant self-service safety boundary so AI never auto-resolves eligibility for a tenant (protects the customer from AI error)
2. **Invent and Simplify** → AgentProbe: zero-cost local AI evaluation toolkit — removed vendor dependency entirely
3. **Dive Deep** → Capital One data quality audit: 8 issues detected programmatically, dollar impact quantified before any analysis
4. **Deliver Results** → Entrata: 200+ SQL queries → 30% perf gain, 80% manual workload eliminated, 100% PHI compliance

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Company | Amazon — verified, publicly traded | Positive |
| Role type | BIE is an established Amazon job family | Positive |
| JD quality | Specific responsibilities, realistic requirements, clear team description | Positive |
| Amazon layoffs | Amazon had targeted layoffs in 2025 but BIE/analytics roles were protected | Neutral |
| Multiple Amazon apps | 4th Amazon app — different teams are independent; track identity consistency | Neutral |
| Location not specified | Verify before applying — relocation could be a factor | ⚠️ Check |

Verify location and salary range on the actual application page before submitting.

## Keywords extracted

business intelligence engineer, BIE, AI analytics, Python, SQL, AWS, Redshift, S3, Hadoop, machine learning, data mining, information retrieval, ETL, data science, executive decision support, automated reporting, operational metrics, self-service analytics, data integrity, scalable processes, cloud storage, cloud computing, BI, non-technical stakeholders, cross-functional

---

## Machine Summary

```yaml
role: Senior Business Intelligence Engineer (AI Analytics)
company: Amazon
score: 4.0
archetype: bie-ai-analytics
level: senior
location: unspecified (verify)
remote: unknown
comp_min: 140000
comp_max: 185000
visa_confirmed: true
h1b_sponsor: confirmed (top sponsor)
apply_threshold_met: true
hard_block: false
notes: >
  Strong technical match — Python, SQL, AWS, AI tools for non-technical stakeholders (LeaseI = exact match).
  Gaps: Hadoop, Redshift, multi-TB explicit experience.
  Amazon Senior concern: prior rejection was SA loop (system design); BIE loop is SQL + analytical — different bar.
  4th Amazon application — verify identity consistency across apps.
  Location not shown in JD — confirm before applying.
```
