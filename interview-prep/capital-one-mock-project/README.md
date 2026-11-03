# Capital One — BCP Field Strategy Data Challenge
### Mock Take-Home Project (Principal Data Analyst)

**Team:** Business Cards & Payments (BCP) — Field Strategy
**Role:** Principal Data Analyst
**Time limit:** 5–10 days from receipt
**Deliverables:** Jupyter notebook + 10-slide executive deck + live presentation (Power Day)

---

## Background

Capital One's Business Cards & Payments division serves small and mid-size businesses across the United States through a network of 20 field representatives. The Field Strategy team decides which customers field reps target for outreach, upsell, and retention.

The **VP of Field Strategy** needs analysis ahead of Q3 2026 planning. She wants to know:

1. Where is spend growing and where is it declining across the portfolio?
2. Which customers should reps prioritize for Q3 outreach?
3. Are Q1 field campaigns working — and which channels drive the most lift?
4. Which customers are at churn risk, and how much revenue is at stake?

You have been given 4 datasets. Your analysis will be presented at the Q3 planning meeting.

---

## Datasets

Run `python generate_data.py` first to create the 4 CSV files.

| File | Description | Rows |
|------|-------------|------|
| `customers.csv` | Business customer profiles — industry, size, card product, territory | 250 |
| `transactions.csv` | Card transaction history (Jan 2024 – Jun 2026) | ~6,000 |
| `field_reps.csv` | Field rep roster — territory, quota, Q1 2026 attainment | 20 |
| `campaigns.csv` | Q1 2026 outreach campaign results — channel, spend before/after | 150 |

### Data Dictionary

**customers.csv**
| Column | Type | Description |
|--------|------|-------------|
| `customer_id` | string | Unique customer identifier (CUST001–CUST250) |
| `business_name` | string | Company name |
| `industry` | string | Technology / Professional Services / Healthcare / Retail / Construction / Restaurants / Manufacturing |
| `business_size` | string | Small (1–10 emp) / Medium (11–50) / Large (51–200) |
| `state` | string | US state |
| `territory` | string | Northeast / Southeast / Midwest / West |
| `card_product` | string | Business Rewards / Business Platinum / Business Cash |
| `credit_limit_usd` | integer | Assigned credit limit |
| `acquisition_date` | date | Date customer joined Capital One commercial cards |
| `rep_id` | string | Assigned field representative |

**transactions.csv**
| Column | Type | Description |
|--------|------|-------------|
| `transaction_id` | string | Unique transaction ID (TXN000001–...) |
| `customer_id` | string | Links to customers.csv |
| `transaction_date` | date | Date of transaction (YYYY-MM-DD) |
| `amount_usd` | float | Transaction amount in USD |
| `merchant_category` | string | Office Supplies / Travel / Dining / Fuel / Technology Equipment / Healthcare Supplies / Construction Supplies / Marketing & Advertising / Utilities / Other |
| `card_product` | string | Card used |

**field_reps.csv**
| Column | Type | Description |
|--------|------|-------------|
| `rep_id` | string | Unique rep identifier (REP01–REP20) |
| `rep_name` | string | Full name |
| `territory` | string | Assigned territory |
| `quarterly_quota_usd` | integer | Q1 2026 managed spend quota |
| `q1_2026_actual_usd` | integer | Actual managed spend Q1 2026 |
| `quota_attainment_pct` | float | % of quota achieved |
| `active_customer_count` | integer | Number of active accounts managed |

**campaigns.csv**
| Column | Type | Description |
|--------|------|-------------|
| `campaign_id` | string | Unique campaign record (CAMP0001–...) |
| `customer_id` | string | Customer who was contacted |
| `rep_id` | string | Rep who made contact |
| `outreach_date` | date | Date of outreach |
| `channel` | string | In-Person / Phone / Email |
| `converted` | integer | 1 if customer increased spend >$500 in 30 days post-outreach |
| `spend_30d_before_usd` | float | Card spend 30 days before outreach |
| `spend_30d_after_usd` | float | Card spend 30 days after outreach |
| `spend_lift_usd` | float | Dollar lift (after minus before) |
| `spend_lift_pct` | float | Percentage lift |

---

## Business Questions

Answer all 6. Each must appear in your slide deck with a clear, actionable recommendation.

### Q1 — Spend Trends (Portfolio Overview)
Analyze total and average monthly spend across the portfolio (Jan 2024 – Jun 2026).
- Which merchant categories have the highest total spend?
- Which categories are growing or declining year-over-year (2024 vs 2025 vs 2026 H1)?
- Are there seasonal patterns that should influence Q3 rep scheduling?

### Q2 — Customer Segmentation
Segment the 250 customers into **3 tiers** based on spend behavior, utilization, and growth trajectory.
- Define your segmentation criteria clearly and justify the method
- Profile each tier: size distribution, industry mix, card product, average monthly spend, credit utilization
- Which tier should Field Strategy prioritize for Q3 outreach and why?

### Q3 — Field Rep Performance
Evaluate the 20 field reps against their Q1 2026 quotas.
- Build a rep performance league table (quota attainment %)
- Identify the top 3 and bottom 3 reps
- What customer or territory patterns explain the performance gap?
- What would you recommend underperforming reps do differently in Q3?

### Q4 — Campaign Effectiveness
Assess whether Q1 2026 field outreach drove meaningful spend lift.
- What was the average spend lift by channel (In-Person, Phone, Email)?
- Is the difference between channels statistically significant? *(Use a t-test or Mann-Whitney U — show your p-values)*
- What is the conversion rate by channel?
- Which channel should Field Strategy invest in for Q3, and what is the expected ROI?

### Q5 — Churn Risk
Identify customers showing declining spend over the last 3 months (Apr–Jun 2026).
- How many customers are at risk?
- Estimate the annual revenue at risk if these customers churn
- What patterns do at-risk customers share (industry, size, territory, rep)?
- What retention action do you recommend — and for which tier?

### Q6 — Q3 Recommendation (Synthesis)
Deliver a concrete Q3 action plan for the VP of Field Strategy:
- Which customer segments should reps prioritize? (Be specific — numbers, not adjectives)
- Which outreach channel should be the primary Q3 investment?
- Which territories need the most attention?
- What is your projected spend impact from the recommended strategy?

---

## Deliverables

### 1. Jupyter Notebook (or .py scripts)
- All code runs top to bottom without errors
- Markdown cells explaining your reasoning at each step
- Data quality section: missing values, duplicates, outliers, join validation
- At least one visualization per question (matplotlib, seaborn, or plotly)

### 2. Executive Slide Deck (10 slides max)
Suggested structure:
| Slide | Content |
|-------|---------|
| 1 | Executive Summary — 3 key findings + #1 recommendation |
| 2 | Portfolio Spend Overview — categories, trends, seasonality |
| 3 | Customer Segmentation — tier definitions + profiles |
| 4 | Segmentation — Q3 prioritization rationale |
| 5 | Field Rep Performance — league table + root cause |
| 6 | Campaign Effectiveness — channel comparison + stats |
| 7 | Churn Risk — at-risk customers + revenue impact |
| 8 | Q3 Action Plan — concrete, prioritized, quantified |
| 9 | Data Quality & Caveats |
| 10 | Appendix — additional charts, methodology |

### 3. Power Day Presentation (10–15 min)
You will present to a panel (VP + 2 Principal DAs). Be ready to:
- Walk your methodology and key findings
- Defend analytical choices under pressure ("why this segmentation method?")
- Answer "what would you do with 3 more weeks and more data?"
- Quantify tradeoffs you made

---

## Evaluation Criteria (Principal DA bar)

| Dimension | Weight | What they look for |
|-----------|--------|--------------------|
| Business framing | 30% | Do findings drive Field Strategy decisions — not just describe data? |
| Analytical rigor | 25% | Correct stats, clean joins, defensible segmentation, proper significance testing |
| Data quality awareness | 20% | Did you catch and call out data issues before acting on them? |
| Communication | 15% | Can a VP read your slide deck without explanation? |
| Insight depth | 10% | Did you find something non-obvious that a junior analyst would miss? |

---

## Tips for a Principal-Level Submission

- **Lead every slide with the business implication** — not the chart title. "In-Person campaigns pay back in 6 weeks — invest here for Q3" beats "Channel Comparison."
- **Quantify everything** — "28% spend lift vs 5% for Email" beats "In-Person outperformed Email"
- **Call out data limitations** — show you govern, not just report
- **One recommendation per question** — "it depends" is not a Principal-level answer
- **The synthesis slide is where you win** — connect all 5 analyses into a single Q3 action plan with projected impact

---

*Dataset is synthetic — generated for interview preparation. All names, companies, and transactions are fictional.*
