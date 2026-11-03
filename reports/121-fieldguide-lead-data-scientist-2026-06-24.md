# 121 — Fieldguide · Lead Data Scientist

**Date:** 2026-06-24
**Score:** 3.9/5
**URL:** https://jobs.ashbyhq.com/fieldguide/fd1c14ef-a6bb-4cfe-a9fa-2c0d4ca033b9
**PDF:** ❌ (below 4.0 apply threshold)
**Legitimacy:** Proceed with Caution

---

## A) Match with CV — 3.7/5

**Strong overlaps:**
- SQL depth: 200+ queries optimized at Entrata across 1M+ property records — direct proof point for "large, complex datasets"
- Python (pandas, NumPy): 8+ years production use across Entrata, GMU research, LeaseI, CrashClarity
- ETL pipelines + data infrastructure: built compliance data pipelines at Entrata (AWS S3, encrypted data migration, recertification workflows) — maps to "scalable data infrastructure, preprocessing, ETL, orchestration"
- Data visualization: Tableau + ggplot2 + Quarto at GMU (faculty dashboards improving comprehension 40%) + property performance dashboards at Entrata
- ML prototyping → production: LeaseI (LangGraph RAG, 93.6% precision), CrashClarity (Random Forest + Logistic Regression, 85%+ accuracy) — satisfies bonus points requirement
- Graduate degree in quantitative field: M.S. Data Analytics Engineering, GPA 3.87

**Gaps:**
- **dbt / Airflow**: not in cv.md; Entrata used internal ETL tooling, not modern data stack. This is a real gap — many Lead DS job screens use dbt as a filter.
- **Customer-facing analytics product**: Parimala's production experience is full-stack engineering (PHP, JS, backend) and research analytics (GMU). "Shipping customer-facing analytics features" on a SaaS product is adjacent but not a direct match.
- **Audit/advisory domain**: no prior experience with CPA firm workflows, cybersecurity audits, or financial advisory — new domain vs her property management expertise.
- **Lead-level data science**: her DS experience is academic (GMU Research Associate) + project-based (LeaseI, CrashClarity), not industry-level "lead DS" shipping a customer-facing data product.

---

## B) North Star Alignment — 3.5/5

Maps to **Data Analyst** archetype (#2 priority per profile): Python/SQL heavy, analytics product, translate data to decisions — strong conceptual fit.

However:
- Audit/advisory software (CPA firms, cybersecurity, privacy audits) is a **neutral domain** — no scoring boost vs proptech or fraud roles
- "Lead Data Scientist" title sits in Tier 2 per role targeting (evaluate, apply if ≥ 4.0 AND Python/SQL, not pure research) — this qualifies
- Product framing ("Fieldguide Insights" — customer-facing analytics) is more DS/product than pure DA
- No LangGraph/agentic/RAG components in this role — the AI upside of Parimala's stack is unused here

---

## C) Compensation — 4.5/5

Salary not disclosed in JD. Market rate for Lead Data Scientist at a well-funded SF startup (Goldman Sachs Alternatives, Bessemer, 8VC, YC — ~Series B/C scale):
- PayScale: $153K avg; Glassdoor: $221K avg; ZipRecruiter: $165K avg; Salary.com: $173K
- Likely range: **$150K–$200K** total comp (base + equity)
- Well above profile's $120K+ target → scores 4.5

*Note: salary UNCONFIRMED. Verify before applying.*

---

## D) Cultural Signals — 4.0/5

- **Remote-first**: "built as a remote-first company that enables you to do your best work from anywhere" — excellent for location flexibility ✓
- **Investors**: Goldman Sachs Alternatives, Bessemer, 8VC, Y Combinator — top-tier, signals legitimate funding and runway
- **Mission**: building software that automates audit and advisory work (50% effort consolidation, work-life balance for practitioners) — meaningful problem
- **Team culture**: "deliberate and self-reflective," "inclusive, driven, humble, supportive" — signals thoughtful early-stage culture
- **Early-stage upside**: equity at a well-backed startup has real potential
- **Risk**: early-stage = typical startup uncertainty

---

## E) Red Flags — 3.5/5

- **Posting age: ~161 days** (posted ~Jan 15, 2026, still active Jun 24, 2026). For a startup data science role this is significantly long. Possible explanations: very selective hiring bar, budgeted but not urgently backfilling, or low-priority open req. Raise with recruiter upfront.
- **H1B sponsorship: UNCONFIRMED**. Not mentioned in JD. SF VC-backed startups can sponsor but many decline for junior/mid roles. Need to verify before investing application effort. Email hr@fieldguide.ai or check H1B sponsor databases.
- **dbt/Airflow gap**: these appear explicitly in the JD ("modern data tooling such as dbt, Airflow or equivalent") — a resume without these terms may screen out pre-call.
- **Looker not in profile**: JD mentions "Tableau, Power BI, Looker" — Parimala has Tableau + Power BI but not Looker.

---

## F) Global Score — 3.9/5

| Block | Score | Weight |
|-------|-------|--------|
| A. CV Match | 3.7 | 35% |
| B. North Star | 3.5 | 20% |
| C. Comp | 4.5 | 20% |
| D. Culture | 4.0 | 15% |
| E. Red Flags | 3.5 | 10% |
| **Global** | **3.9** | 100% |

**Verdict: Borderline. Do not apply without addressing two blockers first:**
1. Confirm H1B sponsorship
2. Verify posting is still actively hiring (5-month age on a startup DS role is unusual)

If both clear → the role is worth applying for (DA archetype, strong comp, remote-first). However, the dbt/Airflow gap and Lead-level framing means this competes more on SQL/Python/ML breadth than on domain expertise (unlike proptech roles where Parimala has an unmatched edge).

---

## G) Posting Legitimacy — Proceed with Caution

- **Active on Ashby**: confirmed in active board via API ✓
- **JD quality**: detailed, technical, specific responsibilities — not a ghost posting template ✓
- **Company legitimacy**: Goldman Sachs, Bessemer, 8VC, YC backed — verifiably real ✓
- **Posting age**: ~161 days. For a well-funded startup's product data scientist role, 5+ months is atypically long. Could mean very selective bar (positive signal for comp) or budget freeze/deprioritized.
- **No team size or headcount mentioned** — can't assess urgency

**Recommendation**: Email recruit@fieldguide.io before applying. Ask: "Is the Lead Data Scientist role still actively hiring?" and "Does Fieldguide sponsor H1B?" Two emails, two blockers cleared.

---

## Interview Angle (if you apply)

**Lead with:** 200+ SQL queries at scale (1M+ Entrata records) + compliance analytics pipelines → "I've built analytics infrastructure over regulated, high-stakes data at production scale — exactly the kind of environment audit firms operate in."

**Frame the domain gap:** "I've spent 8 years building analytics for compliance-heavy regulated environments (LIHTC, HUD, PHI-sensitive data). Audit data has the same characteristics — structured, rule-based, regulated, high-stakes. The workflows are new to me; the data patterns are not."

**Use GMU as the bridge:** R²=0.977 regression models, Isolation Forest anomaly detection, Tableau/Quarto dashboards for faculty leadership → demonstrates you can build and present DS work at a product level.

**Acknowledge dbt/Airflow honestly:** "I've built ETL pipelines using AWS Glue and custom Python — not dbt specifically, but I've owned the same problems dbt solves. I'd get productive on it quickly."
