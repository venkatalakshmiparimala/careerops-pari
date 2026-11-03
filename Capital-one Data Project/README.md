# E-Commerce Strategy Analysis
Capital One Data Analyst Challenge

---

## Business Problem
A St. Louis-based e-commerce company provided two years of operational data and asked for
analysis to evaluate three strategic decisions:
1. Whether to maintain 24/7 operational staffing
2. Whether to continue a wide product catalog strategy
3. Whether to continue its referral discount program

Five specific questions were scoped, plus a future-state recommendation.

---

## Project Structure

```
├── Data/
│   ├── Raw/            ← Original files — NEVER edited
│   └── Processed/      ← Cleaned outputs (written by 01_data_quality.ipynb)
├── src/
│   ├── config.py       ← All constants, assumptions, file paths
│   ├── load.py         ← Raw file I/O only (no transforms)
│   ├── clean.py        ← All cleaning functions for 3 dataset types
│   └── features.py     ← Joins, grain aggregation, derived columns
├── ├── notebooks/
│   ├── 01_data_quality.ipynb   ← Run first: QA report + writes Processed/
│   ├── 02_analysis.ipynb       ← Run second: 5 business questions + charts
│   └── 03_report.ipynb         ← Run third: executive summary + findings
├── outputs/figures/    ← Charts saved by the analysis notebook
└── requirements.txt
```

---

## How to Run

```bash
pip install -r requirements.txt
jupyter notebook
```

Run the three notebooks in order:
1. `notebooks/01_data_quality.ipynb` — QA report, writes cleaned CSVs to `Data/Processed/`
2. `notebooks/02_analysis.ipynb` — the five business questions and supporting charts
3. `notebooks/03_report.ipynb` — executive summary and final recommendations

---

## Documented Assumptions

A2, A3, A6, and A10 are engineering/business judgment calls made where the brief was
silent. A1, A4, A5, A7, A8, and A9 are not judgment calls — they are stated directly in
the challenge brief's assumptions section.

| # | Assumption | Source | Where Used | Impact if Wrong |
|---|---|---|---|---|
| A1 | `order_datetime` is captured in the **buyer's local timezone** (buyer.timezone). Timestamps are converted to **America/Chicago (Central)** for the Q1 staffing analysis. | Challenge brief | Q1 | Hour distribution shifts 5–6 hours if UTC |
| A2 | Buyers with null or unresolvable timezone default to **Central**. | Engineering judgment | Q1 | Minor — very few buyers remain unresolved after state-based imputation |
| A3 | "Customer segment" in Q2/Q4/Q5 = `buyer.customer_group` (VIP / Frequent / Regular / Occasional / Dormant). `buyer.customer_segment` (behavioral, e.g. "Bargain Hunter") is available as a secondary cut. | Engineering judgment | Q2, Q4, Q5 | Changes which grouping is shown in segment charts |
| A4 | Referral discount = 10% off the referred buyer's first Delivered order. Raw data contains only an `is_referred` flag, not a discount amount — the dollar impact is calculated from the confirmed rate. | Challenge brief | Q3 | Dollar estimate scales linearly if production rate differs — core finding (referred vs. non-referred behavior identical) holds regardless of rate |
| A5 | Black Friday eligibility is evaluated in the customer's local timezone, not a fixed company timezone. | Challenge brief | Q4 | Slightly more BF orders vs a fixed-zone cutoff |
| A6 | `order_status = 'Delivered'` orders only count toward revenue and profit metrics. All statuses (including Cancelled) count toward **volume** metrics. | Business logic | Q1 vs Q2–Q5 | Q1 uses full order count; financial questions use delivered-only |
| A7 | Black Friday = 20% off all items purchased that day (based on customer's local timezone). Raw price data does **not** include this discount — applied in `features.py`. | Challenge brief | Q4 | All BF revenue/profit figures already reflect the 20% reduction |
| A8 | Customer shipping tiers per delivered order: order total <$50 → $7.99, $50–$99.99 → $4.99, ≥$100 → free. Company pays a **flat $4.99 per delivered order** to its 3rd-party carrier, regardless of order size or weight. | Challenge brief | Q2–Q5 profit figures | Net shipping P&L included in `order_revenue` and `order_profit` for every delivered order |
| A9 | Taxes are ignored — pre-calculated into the raw price data, per the brief. | Challenge brief | All revenue/profit figures | No adjustment needed; figures already net of tax |
| A10 | The 10% referral discount is applied to the buyer's **shipping-inclusive order total**, not just the product subtotal. The brief says "10% off first order" without specifying which. | Engineering judgment | Q3 | Adds roughly $2,200 to the Q3 cost estimate vs. a product-only reading; the core finding (no behavioral lift) holds under either reading |

---

## Key Data Quality Issues Resolved

| Issue | Dataset | Fix |
|---|---|---|
| 24,878 exact full-row duplicates | sales.csv | `drop_duplicates()` |
| "Deliverred" typo in order_status | sales.csv | String replacement map |
| 3 mixed datetime formats in one column | sales.csv | Format-aware parsing per row |
| Epoch-zero "1/1/70 0:00" sentinel | sales.csv | Nulled before parsing |
| Quantity sentinel ~327M (**outlier**) | sales.csv | Flagged as statistical outlier; nulled and marked via `quantity_is_valid` |
| **NKDLI.csv lowercase key columns** | Vendor files | Uppercase before SKU join → 95.6% → **100%** match rate |
| Negative profit margins (**outliers**) | Vendor files | Identified as loss-leader SKUs; flagged via `profit_margin_is_neg`, kept intentionally |
| pct_profit_margin (0–100) vs profit_margin (0–1) | ROPIK, JDTOJ | Divided pct columns by 100 |
| Currency symbol "$7.9" in price | ROPIK.csv | Stripped non-numeric chars before cast |
| Inconsistent boolean spellings (True/1/Y) | All vendor files | Uniform `BOOLEAN_MAP` in config.py |
| Null region/timezone | buyer.csv | Empirically derived state→region/timezone lookup |

---

## Dataset Scale

| Entity | Count (post-clean) |
|---|---|
| Total buyers | 47,500 |
| Dormant buyers (0 orders) | ~23,700 (~50% of buyer base) |
| Sales rows (after dedup) | 350,804 (from 376,004 raw; 25,200 removed) |

---

## Catalog Strategy Finding

Strategic decision #2 (whether to continue a wide product catalog) is answered directly
from the vendor catalog and sales data:

| Metric | Value |
|---|---|
| Total SKUs in catalog | 1,037 |
| SKUs with at least one delivered sale | 1,037 (100%) |
| Revenue from top 10% of SKUs | 53.3% |
| Revenue from top 20% of SKUs | 66.0% |
| Revenue from bottom 50% of SKUs | 9.1% |
| SKUs tied to a currently active vendor | 487 (47.0%) |
| SKUs at negative profit margin (loss-leaders) | 111 (10.7%) |

**Finding:** Every SKU in the catalog has sold at least once, so the width itself isn't
generating obvious dead inventory — but revenue is heavily concentrated in a small slice
of it (the classic long-tail pattern: top 20% of SKUs drive two-thirds of revenue, while
the bottom half contributes under 10%). The bigger risk isn't breadth, it's **vendor
continuity**: more than half the catalog (53%) is tied to a vendor no longer marked
active, meaning over 500 SKUs could lose supply with no advance warning in the data.
Loss-leader SKUs (111, 10.7% of catalog) are concentrated in **Pet Supplies** (avg
margin 5.1%, 26% of its SKUs negative), **Toys & Games**, **Sports & Outdoors**, and
**Books** — while **Electronics** and **Beauty** carry the strongest margins (~51–53%).

**Recommendation:** Don't narrow the catalog on breadth alone — the long tail isn't
dead weight, it's still selling. Instead: (1) prioritize re-sourcing or replacing the
53% of SKUs tied to inactive vendors before that becomes a stockout problem, and
(2) review Pet Supplies pricing/sourcing specifically, since it's the one category
losing money on over a quarter of its SKUs rather than carrying occasional loss-leaders.

---

## Data Gap

No explicit referral discount *dollar amount* exists in the raw data — only an
`is_referred` flag. The 10% referral rate itself is not something we inferred; it is
stated directly in the challenge brief's assumptions (see A4). The ~$24,368.40
revenue-lost estimate applies that confirmed rate to the first Delivered order of each
referred buyer.

**Because the raw data contains no discount amount to independently verify against,
we recommend the team confirm with business that this brief-stated 10% rate still
matches what is actually applied in production before using the dollar estimate
operationally.** If production uses a different rate, the dollar estimate would change
proportionally, but the core finding — referred vs. non-referred buyer behavior is
statistically identical — would not.