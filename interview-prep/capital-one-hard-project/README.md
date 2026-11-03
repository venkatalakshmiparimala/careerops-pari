# Capital One BCP Field Strategy — HARD Take-Home Project
### Principal Data Analyst | Full-Spectrum Challenge

**Time limit:** 5–10 days
**Deliverables:** Jupyter notebook (all code) + 12-slide executive deck + live Power Day defense
**Difficulty:** Principal DA bar — covers every skill they will test

---

## Background

You are a Principal Data Analyst on the Business Cards & Payments (BCP) Field Strategy team. Capital One has given you access to 18 months of commercial card data covering 300 business accounts, 100K+ transactions, 500 merchants, 20 field reps, and a Q1 2026 A/B campaign test.

The VP of Field Strategy and the Chief Risk Officer are co-sponsoring your analysis for Q3 2026 planning. You have two audiences:
- **VP of Field Strategy** — wants growth levers, rep deployment strategy, campaign ROI
- **Chief Risk Officer** — wants fraud exposure quantified, data quality certified, churn risk contained

**Your job:** deliver a single analysis that serves both.

---

## Datasets

Run `python3 generate_data.py` to create all 5 files.

| File | Description | Rows |
|------|-------------|------|
| `accounts.csv` | Business account profiles | ~308 (includes dirty rows) |
| `transactions.csv` | Card transactions Jan 2023 – Jun 2026 | ~100K+ (includes data quality issues) |
| `merchants.csv` | Merchant reference table — name, category, MCC code | ~220 |
| `field_reps.csv` | Rep roster — quota, attainment, account mix | 20 |
| `ab_test.csv` | Q1 2026 A/B campaign test — Treatment vs Control | 200 |

### Data Dictionary

**accounts.csv**
| Column | Type | Notes |
|--------|------|-------|
| `account_id` | string | Unique account (ACC0001–ACC0300) — **contains duplicates** |
| `business_name` | string | Company name |
| `industry` | string | Technology / Professional Services / Healthcare / Retail / Construction / Restaurants / Manufacturing / Logistics |
| `business_size` | string | Small / Medium / Large |
| `state` | string | US state |
| `territory` | string | Northeast / Southeast / Midwest / West |
| `card_product` | string | Business Rewards / Business Platinum / Business Cash |
| `credit_limit_usd` | integer | Assigned credit limit |
| `acquisition_date` | date | YYYY-MM-DD |
| `rep_id` | string | Assigned field rep |

**transactions.csv**
| Column | Type | Notes |
|--------|------|-------|
| `transaction_id` | string | TXN0000001–... |
| `account_id` | string | Links to accounts.csv |
| `transaction_date` | string | **Mixed formats: YYYY-MM-DD and MM/DD/YYYY** |
| `amount_usd` | float | **Some negative values (credits)** |
| `merchant_id` | string | Links to merchants.csv |
| `merchant_category` | string | **300 NULL values** |
| `card_product` | string | Card used |
| `transaction_type` | string | PURCHASE / REVERSAL / CREDIT |
| `status` | string | SETTLED |

**merchants.csv**
| Column | Type | Notes |
|--------|------|-------|
| `merchant_id` | string | MER0001–... |
| `merchant_name` | string | Merchant name |
| `merchant_category` | string | Category |
| `mcc_code` | string | Standard Merchant Category Code |
| `city` / `state` | string | Merchant location |
| `is_high_risk` | integer | 1 = high-risk merchant flag |

**field_reps.csv**
| Column | Type | Notes |
|--------|------|-------|
| `rep_id` | string | REP01–REP20 |
| `rep_name` | string | Full name |
| `territory` | string | Territory |
| `quarterly_quota_usd` | integer | Q1 2026 spend quota |
| `q1_2026_actual_usd` | integer | Actual managed spend |
| `quota_attainment_pct` | float | % of quota |
| `active_account_count` | integer | Accounts managed |
| `avg_account_tenure_months` | integer | Avg tenure of their accounts |
| `pct_large_accounts` | float | % of accounts that are Large |
| `campaigns_run_q1` | integer | Outreach campaigns run in Q1 |

**ab_test.csv**
| Column | Type | Notes |
|--------|------|-------|
| `campaign_id` | string | AB0001–... |
| `account_id` | string | Account in the experiment |
| `industry` / `business_size` | string | Account attributes |
| `rep_id` | string | Rep who ran outreach (Treatment only) |
| `group` | string | Treatment / Control |
| `outreach_date` | date | Date of In-Person visit (Treatment) |
| `converted` | integer | 1 if spend increased >$500 in 30 days |
| `pre90_spend_usd` | float | Spend Oct–Dec 2025 (pre-experiment baseline) |
| `spend_30d_before_usd` | float | Spend 30 days before outreach |
| `spend_30d_after_usd` | float | Spend 30 days after outreach |
| `spend_lift_usd` | float | After minus before |
| `spend_lift_pct` | float | % lift |

---

## DATA QUALITY AUDIT (Do This First — Before Any Analysis)

**8 data quality issues are deliberately embedded. Find and fix all 8 before proceeding.**

Not finding them is an automatic fail at Principal level — you cannot govern data you haven't audited.

| # | Issue | Where | Impact if Missed |
|---|-------|--------|-----------------|
| 1 | Duplicate account_id rows | accounts.csv | Double-counts spend, inflates RFM scores |
| 2 | Reversed transactions (PURCHASE + REVERSAL same merchant/amount/account within 24h) | transactions.csv | Overstates gross spend |
| 3 | Multi-swipe transactions (same account/merchant/amount within 2 hours, charged 3x) | transactions.csv | Inflates spend, false fraud signals |
| 4 | Velocity burst transactions (10+ transactions in 1-hour window, 20 accounts) | transactions.csv | These ARE legitimate fraud signals — flag, don't delete |
| 5 | NULL merchant_category (300 rows) | transactions.csv | Category analysis is wrong |
| 6 | Mixed date formats (MM/DD/YYYY vs YYYY-MM-DD) | transactions.csv | Date joins and time-series break silently |
| 7 | Negative amount_usd (credits, 25 rows) | transactions.csv | Understates spend in aggregations |
| 8 | Pre-period spend imbalance in A/B test (15 Treatment accounts have 40% higher baseline) | ab_test.csv | Inflates measured lift — groups aren't balanced |

**For each issue:**
- Detect it programmatically (show the code and the count)
- Document your decision: remove, impute, flag, or keep with caveat
- Quantify the impact: how many rows affected? What % of total spend?

---

## Business Questions

### Q1 — Data Quality Audit & Governance Report
*(See above — this is mandatory before Q2–Q8)*

Deliverable: a data quality summary table showing each issue, rows affected, dollar impact, and your treatment decision. This goes on slide 2 of your deck.

---

### Q2 — RFM Segmentation & Customer Lifetime Value
Using only clean transactions (post-audit), build a full RFM model as of 2026-06-30.

**Steps:**
- Calculate R (days since last transaction), F (transaction count last 6 months), M (total spend last 6 months)
- Score each dimension 1–5 using quintiles (1=worst, 5=best)
- Combine: `rfm_score = R_score*100 + F_score*10 + M_score`
- Assign each account to one of 5 tiers:

| Tier | RFM Pattern | Label |
|------|-------------|-------|
| 1 | R≥4, F≥4, M≥4 | Champions |
| 2 | R≥3, F≥3, M≥3 | Loyal |
| 3 | R≥3, F≤2 OR M≤2 | Promising |
| 4 | R≤2, F≥3 | At Risk |
| 5 | R≤2, F≤2 | Hibernating / Lost |

**Then:**
- Profile each tier: industry mix, size, card product, avg monthly spend, credit utilization
- Estimate Customer Lifetime Value (CLV) per tier: `CLV = avg_monthly_spend × avg_remaining_tenure_months × gross_margin` (assume 8% gross margin on spend)
- Which tier has the highest total CLV at risk if they churn?
- Which tier should Q3 outreach prioritize?

---

### Q3 — Cohort Retention Analysis
Build the classic retention heatmap by acquisition cohort.

**Steps:**
- Group accounts by acquisition month (Jan 2023 – Jun 2025 — 30 cohorts)
- For each cohort, define Month 0 = acquisition month
- For each subsequent month (Month 1–36), calculate: what % of the original cohort made ≥1 transaction?
- Output a retention matrix: rows = cohorts, columns = months since acquisition

**Answer:**
- Which acquisition cohort has the best 12-month retention? Worst?
- What is the median "time to first churn" (first month with 0 transactions) across all accounts?
- Is there a difference in retention between card products? Between industries?
- What does the retention curve tell you about when Capital One should intervene?

---

### Q4 — Fraud & Anomaly Detection System
Build a fraud risk scoring system across 3 signal types.

**Signal 1 — Velocity Risk:**
For each account, in any rolling 60-minute window in the last 90 days (Apr–Jun 2026):
- Count the max number of transactions in any 1-hour window
- Flag accounts where max_hourly_txns > 5
- Calculate velocity risk score: `min(100, max_hourly_txns * 8)`

**Signal 2 — Amount Anomaly:**
For each transaction, compare to the account's own historical mean and std:
- `z_score = (amount - account_mean) / account_std`
- Flag transactions where `z_score > 3.5`
- Per account: count flagged transactions, sum flagged dollar amounts

**Signal 3 — New Merchant Risk:**
For accounts with >12 months of history:
- Identify transactions at merchants never seen by that account before (first-time merchant)
- Flag if first-time merchant is also `is_high_risk = 1` in merchants.csv
- Count flagged transactions per account in last 90 days

**Composite Fraud Risk Score (0–100):**
`fraud_score = (velocity_score * 0.4) + (amount_anomaly_score * 0.35) + (new_merchant_score * 0.25)`

Define `amount_anomaly_score` and `new_merchant_score` using a 0–100 normalization of your choice — justify it.

**Deliverables:**
- Top 20 highest fraud-risk accounts with their scores and primary signal driver
- Total dollar exposure in the flagged transaction population
- Recommended escalation threshold (what score triggers a human review?)
- One SQL query that could run in production to flag new velocity bursts daily

---

### Q5 — Churn Prediction Model
Build a binary churn classifier.

**Definition:** An account is churned if it has **zero transactions in the last 60 days** (May 1 – Jun 30, 2026).

**Feature Engineering (build all of these):**

| Feature | Description |
|---------|-------------|
| `rfm_r_score` | Recency score from Q2 |
| `rfm_f_score` | Frequency score from Q2 |
| `rfm_m_score` | Monetary score from Q2 |
| `spend_trend` | (last 3 months spend) / (prior 3 months spend) — ratio < 1 = declining |
| `avg_txn_amount` | Mean transaction amount last 6 months |
| `days_since_last_txn` | As of 2026-06-30 |
| `account_tenure_days` | Days since acquisition_date |
| `credit_utilization` | avg_monthly_spend / credit_limit_usd |
| `txn_frequency_trend` | Transactions last 3 months / prior 3 months |
| `industry` | One-hot encoded |
| `business_size` | Ordinal encoded (Small=1, Medium=2, Large=3) |
| `card_product` | One-hot encoded |
| `in_ab_treatment` | 1 if account received Q1 campaign |
| `fraud_score` | From Q4 |

**Model:**
- Train/test split: 80/20 stratified
- Train: Random Forest (n_estimators=100, random_state=42) AND Logistic Regression
- Report for both: Accuracy, Precision, Recall, F1, ROC-AUC
- Plot ROC curve for both on the same chart
- Feature importance (Random Forest) — top 10 features, bar chart
- Score all non-churned accounts → output top 50 highest churn-risk accounts for Q3 retention outreach

**The hard question:** If you could only run outreach on 30 accounts (budget constraint), which 30 do you choose and why? Show the expected revenue saved.

---

### Q6 — A/B Test Analysis: Was the Campaign Real?
Analyze the Q1 2026 In-Person outreach experiment.

**Step 1 — Pre-Period Balance Check (MANDATORY)**
Before claiming lift, verify the groups were balanced:
- Compare `pre90_spend_usd` between Treatment and Control
- Run a t-test on pre-period spend — are groups statistically similar?
- If not: what does that mean for your lift estimate? How do you adjust?

**Step 2 — Primary Analysis**
- Primary metric: `spend_lift_pct` (30-day spend lift)
- Run: two-sample t-test + Mann-Whitney U test (report both)
- Calculate: effect size (Cohen's d)
- Calculate: 95% confidence interval for the mean lift
- Report: p-value, significance at α=0.05, and what it means in plain English

**Step 3 — Secondary Metrics**
- Conversion rate by group (spend > baseline + $500 in 30 days)
- Run chi-square test on conversion rates
- What is the revenue impact per treated account?

**Step 4 — Power Analysis**
- What sample size would be needed to detect a 10% lift with 80% power at α=0.05?
- Was this experiment adequately powered?

**Step 5 — Recommendation**
Given the pre-period imbalance you found in Step 1 — do you trust the headline lift number? What is your adjusted estimate? Would you recommend scaling In-Person outreach to all accounts in Q3?

---

### Q7 — Field Rep Attribution: Luck vs Skill
Determine which reps are genuinely outperforming vs. just managing better accounts.

**Step 1 — Raw Performance**
- Plot quota_attainment_pct for all 20 reps
- Identify top 3 and bottom 3

**Step 2 — Account Mix Control**
- Build a multiple linear regression:
  `quota_attainment ~ pct_large_accounts + avg_account_tenure_months + campaigns_run_q1 + territory`
- This controls for the accounts a rep was assigned
- Calculate residuals: positive residual = rep outperforming their account mix ("true alpha")
- Negative residual = rep underperforming their account mix ("needs coaching")

**Step 3 — Customer Mix Analysis**
- For top 3 reps: what % of their accounts are Large? Technology/ProServ?
- For bottom 3 reps: same breakdown
- Does the performance gap survive after controlling for account mix?

**Step 4 — Recommendation**
- Which bottom reps should be reassigned to better accounts (account-mix problem)?
- Which bottom reps need coaching (genuine underperformance)?
- If you could reallocate 20 Large accounts from top reps to struggling reps, what quota lift would you project?

---

### Q8 — Executive Synthesis: Q3 Action Plan
Tie every analysis into a single Q3 plan for the VP + CRO.

This slide must be **one page**, **fully quantified**, and **immediately actionable**.

| Initiative | Target Accounts | Method | Expected Impact |
|------------|----------------|--------|-----------------|
| Retention outreach | Top 50 churn-risk (from Q5) | In-Person (from Q6) | $X revenue saved |
| Fraud escalation | Top 20 fraud-risk (from Q4) | Human review queue | $Y exposure mitigated |
| Rep redeployment | Bottom 3 reps (from Q7) | Account reassignment | Z% quota lift |
| Champion expansion | Champions tier (from Q2) | Upsell to Platinum | $W incremental spend |

**North-star metric:** Define ONE metric the VP should track weekly in Q3. Justify why.

**What would you do with 3 more months and a data warehouse?** (One paragraph — shows Principal-level thinking about future state.)

---

## Deliverables

### 1. Jupyter Notebook
- Sections clearly labeled Q0 (Data Quality) through Q8
- Every analysis reproducible top-to-bottom
- Markdown cells explaining WHY at each decision point (not just WHAT)
- Visualizations: minimum 2 charts per question

### 2. Executive Slide Deck (12 slides max)

| Slide | Content |
|-------|---------|
| 1 | Executive Summary — 3 findings, 1 recommendation per audience (VP + CRO) |
| 2 | Data Quality Certification — issues found, impact, treatment |
| 3 | RFM Segmentation — tier map + CLV by tier |
| 4 | Cohort Retention — heatmap + intervention timing |
| 5 | Fraud Risk — top 20 accounts, exposure, escalation threshold |
| 6 | Churn Model — ROC curve, top features, 30-account shortlist |
| 7 | A/B Test — lift estimate, confidence interval, pre-period caveat |
| 8 | Rep Attribution — raw vs adjusted performance |
| 9 | Q3 Action Plan — the 4-initiative table, fully quantified |
| 10 | North-Star Metric — definition, current baseline, Q3 target |
| 11 | Data Governance Roadmap — what you'd fix in 90 days |
| 12 | Appendix — methodology notes, SQL snippets, model params |

### 3. Power Day Defense (15–20 min)
Interviewers will pick 2 of the 8 questions and go deep. Expect:
- "Walk me through your fraud score weighting — why 40/35/25?"
- "Your A/B test lift was 26% — why don't I trust that number?"
- "If the churn model has 78% recall, what does that mean for the 22% we miss?"
- "Your regression shows REP07 is underperforming even after controlling for mix — what do you tell their manager?"

---

## Grading Rubric (Principal DA Bar)

| Dimension | Weight | Fail | Pass | Exceed |
|-----------|--------|------|------|--------|
| Data Quality | 20% | Missed ≥3 issues | Found all 8, basic treatment | Quantified dollar impact, governance recommendation |
| Statistical Rigor | 20% | Wrong test or no significance testing | Correct tests, p-values reported | Pre-period balance check, effect size, power analysis |
| Modeling | 15% | No model or no evaluation | Train/test split, accuracy reported | ROC-AUC, feature importance, business interpretation |
| Business Framing | 20% | Findings not connected to decisions | Recommendations present | Every recommendation is quantified with projected impact |
| Communication | 15% | Slides describe data | Slides have takeaways | Every slide has a single declarative headline + number |
| Depth | 10% | Answered only what was asked | Answered all 8 questions | Found a non-obvious insight not asked for |

**Principal-level pass = average of 4.0/5.0 across all dimensions.**

---

## Tips

- **Q0 (Data Quality) sets the tone.** If you skip it or do it poorly, everything downstream is suspect. The CRO will ask about it first.
- **Never say "the model shows X."** Say "the model suggests X — and here's the business decision that follows."
- **The A/B test pre-period imbalance is a trap.** If you report the raw 26% lift without flagging it, you fail Q6 at Principal level.
- **Q8 must have dollar amounts.** "Increase retention" is not an executive recommendation. "$340K in at-risk revenue, recoverable with 30 targeted outreach visits" is.
- **Show your SQL.** At least 2 questions should include a production-ready SQL query — not just pandas.

---

*Synthetic dataset generated for interview preparation. All names, accounts, and transactions are fictional.*
