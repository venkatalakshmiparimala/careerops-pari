# run from project root: python3 notebooks/generate_notebooks.py
# then open notebooks/ in Jupyter and run all cells

import sys
import nbformat as nbf
from pathlib import Path

NB_DIR = Path(__file__).parent
NB_DIR.mkdir(exist_ok=True)

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from config import REFERRAL_DISCOUNT_RATE, BLACK_FRIDAY_DISCOUNT_RATE, SHIPPING_TIER_LOW, SHIPPING_TIER_MID, CARRIER_COST_PER_ORDER


def code(src):
    return nbf.v4.new_code_cell(src)


def md(src):
    return nbf.v4.new_markdown_cell(src)


def save(nb, filename):
    path = NB_DIR / filename
    with open(path, "w") as f:
        nbf.write(nb, f)
    print(f"created: {path}")


# --- notebook 1: data quality ---

nb1 = nbf.v4.new_notebook()

nb1.cells = [

md("""# Data Quality Report
Systematic profiling and cleaning of the three source datasets.
All fixes are implemented in `src/clean.py`. This notebook documents what was found,
what was fixed, and what the data looks like after cleaning."""),

code("""\
import sys
from pathlib import Path

     
project_root = Path().resolve().parent
sys.path.insert(0, str(project_root / 'src'))



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns

from load     import load_sales, load_buyers, load_vendor_files
from clean    import clean_sales, clean_buyers, clean_vendors, verify_sku_match_rate
from checks   import run_all_checks
from features import build_line_items, build_orders

FIGURES_DIR = project_root / 'outputs' / 'figures'
FIGURES_DIR.mkdir(parents=True, exist_ok=True)

sns.set_theme(style='whitegrid', palette='muted')
print('imports ok')"""),

md("""## 1. Raw Data — Before Cleaning
Shapes and basic column inspection before any transforms are applied."""),

code("""\
sales_raw   = load_sales()
buyers_raw  = load_buyers()
vendors_raw = load_vendor_files()

print('=== RAW SHAPES ===')
print(f'sales:   {sales_raw.shape}')
print(f'buyers:  {buyers_raw.shape}')
print(f'vendors: {vendors_raw.shape}')
print()
print('=== SALES COLUMNS ===')
print(sales_raw.dtypes)
print()
print('=== ORDER STATUS VALUES (raw) ===')
print(sales_raw['order_status'].value_counts())"""),


md("""## 2. Sales Cleaning
Issues found and fixed in `sales.csv`."""),

code("""\
sales = clean_sales(sales_raw)

print('==== AFTER CLEANING====')
     
print(f'rows before: {len(sales_raw):,}')
print(f'rows after:  {len(sales):,}')
print(f'rows removed: {len(sales_raw) - len(sales):,}')
print()
print('=== ORDER STATUS VALUES (clean) ===')
print(sales['order_status'].value_counts())
print()
print('===DATETIME FORMATS===')
print(f'rows with time component:  {sales["datetime_has_time"].sum():,}')
print(f'rows date-only (no hour):  {(~sales["datetime_has_time"]).sum():,}')
print()
print('=== QUANTITY ===')
print(f'valid quantities:   {sales["quantity_is_valid"].sum():,}')
print(f'invalid quantities: {(~sales["quantity_is_valid"]).sum():,}')"""),


md("""## 3. Buyers Cleaning
Issues fixed from `buyer.csv`."""),

code("""\
buyers = clean_buyers(buyers_raw)

print('=== AFTER CLEANING ===')
print(f'rows before: {len(buyers_raw):,}')
print(f'rows after:  {len(buyers):,}')
print(f'rows removed: {len(buyers_raw) - len(buyers):,}')
print()
print('=== NULL RATES AFTER CLEANING ===')
null_rates = buyers.isna().mean().sort_values(ascending=False)
print(null_rates[null_rates > 0].apply(lambda x: f'{x:.2%}'))
print()
     
print('=== CUSTOMER GROUP DISTRIBUTION ===')
print(buyers['customer_group'].value_counts())"""),

md("""## 4. Vendors Cleaning + SKU Match Rate
Biggest issue: NKDLI.csv stored key columns in lowercase, silently dropping 46 SKUs from the join."""),

code("""\
vendors = clean_vendors(vendors_raw)

print('=== VENDOR CATALOG ===')
print(f'total SKUs: {len(vendors):,}')
print(f'unique vendors: {vendors["vendor"].nunique()}')
print()

print('=== SKU MATCH RATE ===')
rate = verify_sku_match_rate(sales, vendors, label='post-clean')
print()

print('=== PROFIT MARGIN SUMMARY ===')
     
pm = vendors['profit_margin'].dropna()
print(f'min:      {pm.min():.4f}')
print(f'max:      {pm.max():.4f}')
print(f'negative: {(pm < 0).sum()} SKUs (loss-leaders)')
print(f'positive: {(pm >= 0).sum()} SKUs')"""),

md("""## 5. Profit Margin Distribution
The distribution is bimodal -- two natural pricing tiers exist across all vendors.
Loss-leader products (margin < 0) are shown separately on the left panel."""),

code("""\
fig, axes = plt.subplots(1, 2, figsize=(12, 4),
                         gridspec_kw={'width_ratios': [1, 4]})

ax_neg = axes[0]
neg_m = vendors.loc[vendors['profit_margin_is_neg'], 'profit_margin']
ax_neg.hist(neg_m, bins=8, color='tomato', alpha=0.9)
ax_neg.set_xlim(-0.06, 0.0)
ax_neg.set_xlabel('Profit Margin')
ax_neg.set_ylabel('SKU Count')
ax_neg.set_title(f'Loss-Leaders\\n({len(neg_m)} SKUs, margin < 0)', fontsize=9)
ax_neg.axvline(0, color='black', lw=0.8, ls='--')

ax_pos = axes[1]
pos_m = vendors.loc[~vendors['profit_margin_is_neg'], 'profit_margin']
ax_pos.hist(pos_m, bins=40, color='steelblue', alpha=0.8)
ax_pos.set_xlabel('Profit Margin')
ax_pos.set_title(
    'Positive-Margin SKUs — Bimodal Distribution\\n'
    'Low tier 5-35%: most SKUs   High tier 70-93%: cross-vendor, not a scale bug',
    fontsize=9
)
ax_pos.axvline(0.5, color='gray', lw=0.8, ls=':')
ax_pos.text(0.22, 95, 'Low-margin\\ntier\\n(5-35%)',
            fontsize=8, ha='center', color='navy')
ax_pos.text(0.79, 95, 'High-margin\\ntier\\n(70-93%)',
            fontsize=8, ha='center', color='navy')

fig.suptitle('Vendor Product Profit Margin Distribution', fontweight='bold')
plt.tight_layout()
plt.savefig(FIGURES_DIR / 'dq_profit_margin_dist.png', dpi=150, bbox_inches='tight')
plt.show()
print('saved: dq_profit_margin_dist.png')"""),

md("""## 6. Pipeline Checks
Runing all 27 assertions to confirm the cleaned data meets every expectation."""),

code("""\
line_items = build_line_items(sales, vendors, buyers)
orders     = build_orders(line_items)
run_all_checks(sales, buyers, vendors, line_items, orders)"""),

]

save(nb1, "01_data_quality.ipynb")


# --- notebook 2: analysis ---

nb2 = nbf.v4.new_notebook()

nb2.cells = [

md(f"""# E-Commerce Strategy Analysis
**Five Business Questions**

---

## Assumptions

| # | Assumption | Source | Impact if Wrong |
|---|---|---|---|
| A1 | Timestamps are in buyer's local timezone | Stated as fact in source|
| A2 | Buyers with null timezone default to Central | Engineering judgment | Minor — very few unresolved after imputation |
| A3 | Customer segment = `customer_group` field | Engineering judgment — brief says "segment", data has two segment columns | Changes Q2/Q4/Q5 groupings entirely |
| A4 | Referral discount = {int(REFERRAL_DISCOUNT_RATE*100)}% off first order only | Dollar estimate scales linearly with rate |
| A5 | Black Friday eligibility based on customer's LOCAL timezone | Slightly more BF orders vs company tz |
| A6 | Delivered orders only count for revenue/profit | Business logic — Cancelled orders never fulfilled | Volume metrics count all statuses |
| A7 | Black Friday = {int(BLACK_FRIDAY_DISCOUNT_RATE*100)}% off all items that day (customer's local tz); not in raw price data | All BF revenue/profit already reflect the discount applied in pipeline |
| A8 | Customer shipping: <$50→${SHIPPING_TIER_LOW}, $50–$99.99→${SHIPPING_TIER_MID}, ≥$100→free; company carrier cost ${CARRIER_COST_PER_ORDER}/order | Net shipping P&L included in order_revenue and order_profit for every delivered order |"""),

code("""\
import sys
from pathlib import Path

project_root = Path().resolve().parent
sys.path.insert(0, str(project_root / 'src'))

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns

from load     import load_sales, load_buyers, load_vendor_files
from clean    import clean_sales, clean_buyers, clean_vendors
from features import build_line_items, build_orders, estimate_referral_cost
from config   import SEGMENT_ORDER, REFERRAL_DISCOUNT_RATE

FIGURES_DIR = project_root / 'outputs' / 'figures'
FIGURES_DIR.mkdir(parents=True, exist_ok=True)

sns.set_theme(style='whitegrid', palette='muted')

# run full pipeline
sales_raw   = load_sales()
buyers_raw  = load_buyers()
vendors_raw = load_vendor_files()

sales   = clean_sales(sales_raw)
buyers  = clean_buyers(buyers_raw)
vendors = clean_vendors(vendors_raw)

line_items = build_line_items(sales, vendors, buyers)
orders     = build_orders(line_items)

print(f'orders: {len(orders):,} rows')
print(f'revenue-eligible: {orders["is_revenue_eligible"].sum():,}')
print(f'BF orders: {orders["is_black_friday"].sum():,}')"""),

md("""---
## Q1 — Order Volume by Hour
*Does the current 24/7 staffing model make sense given actual order patterns?*"""),

code("""\
timed = orders[orders['datetime_has_time'] & orders['order_hour_central'].notna()]

hourly = (
    timed.groupby('order_hour_central')
    .agg(order_count=('order_id', 'count'))
    .reset_index()
    .sort_values('order_hour_central')
)

overnight = hourly[hourly['order_hour_central'].between(0, 5)]['order_count'].sum()
total     = hourly['order_count'].sum()
overnight_pct = overnight / total * 100
peak_pct      = 100 - overnight_pct

peak_hours = hourly.nlargest(6, 'order_count')['order_hour_central'].values

uniform_overnight_pct = 6 / 24 * 100  # expected share if orders were evenly distributed

print(f'Total orders with time: {total:,}')
print(f'Overnight (12am-6am):  {overnight:,} ({overnight_pct:.1f}%)'
      f'  [vs. {uniform_overnight_pct:.0f}% if evenly distributed]')
print(f'Peak window (6am-12am): {peak_pct:.1f}%')

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

ax = axes[0]
colors = ['tomato' if h in peak_hours else 'steelblue'
          for h in hourly['order_hour_central']]
ax.bar(hourly['order_hour_central'], hourly['order_count'], color=colors)
ax.set_xlabel('Hour of Day (Central Time)')
ax.set_ylabel('Order Count')
ax.set_title('Order Volume by Hour of Day\\n(Red = Top 6 Peak Hours)')
ax.set_xticks(range(0, 24))

ax2 = axes[1]
ax2.pie(
    [overnight_pct, peak_pct],
    labels=[f'Overnight\\n12am-6am\\n{overnight_pct:.1f}%',
            f'Daytime\\n6am-12am\\n{peak_pct:.1f}%'],
    colors=['steelblue', 'tomato'],
    autopct='%1.1f%%',
    startangle=90,
)
ax2.set_title('Overnight vs Daytime Order Share')

plt.suptitle('Q1: Order Volume by Hour — Central Time', fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig(FIGURES_DIR / 'q1_hourly_volume.png', dpi=150, bbox_inches='tight')
plt.show()
print('saved: q1_hourly_volume.png')"""),

md("""### Q1 Findings
**Finding:** Order volume is heavily concentrated in daytime hours.
The overnight window (12am-6am Central) represents a small fraction of total orders.
"""),

md("""---
## Q2 — Average Profit per Order by Quarter & Segment
* Which customer segments drive profitability, and is it consistent over time?*"""),

code("""\
q2 = orders[
    orders['is_revenue_eligible'] &
    orders['customer_group'].notna() &
    orders['order_quarter'].notna()
].copy()

q2_agg = (
    q2.groupby(['order_quarter', 'customer_group'], as_index=False)
    .agg(
        avg_profit  = ('order_profit', 'mean'),
        order_count = ('order_id',     'count'),
    )
)

pivot = q2_agg.pivot(index='customer_group', columns='order_quarter', values='avg_profit')
seg_present = [s for s in SEGMENT_ORDER if s in pivot.index]
pivot = pivot.loc[seg_present]

print('Average profit per order ($):')
print(pivot.round(2).to_string())

fig, axes = plt.subplots(1, 2, figsize=(16, 5))

ax = axes[0]
sns.heatmap(pivot, annot=True, fmt='.1f', cmap='YlOrRd',
            linewidths=0.5, ax=ax, cbar_kws={'label': 'Avg Profit ($)'})
ax.set_title('Avg Profit per Order by Quarter & Segment')
ax.set_xlabel('Quarter')
ax.set_ylabel('Customer Group')
plt.setp(ax.get_xticklabels(), rotation=45, ha='right')

ax2 = axes[1]
quarters = sorted(q2_agg['order_quarter'].dropna().unique())
colors_map = {'VIP': 'gold', 'Frequent': 'steelblue', 'Regular': 'green',
              'Occasional': 'orange', 'Dormant': 'gray'}
for seg in seg_present:
    d = q2_agg[q2_agg['customer_group'] == seg].set_index('order_quarter')
    d = d.reindex(quarters)
    ax2.plot(quarters, d['avg_profit'],
             marker='o', label=seg, color=colors_map.get(seg))

ax2.set_xlabel('Quarter')
ax2.set_ylabel('Avg Profit per Order ($)')
ax2.set_title('Quarterly Profit Trend by Segment')
ax2.legend()
plt.setp(ax2.get_xticklabels(), rotation=45, ha='right')

plt.suptitle('Q2: Average Profit per Order by Quarter & Customer Segment',
             fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig(FIGURES_DIR / 'q2_profit_by_quarter_segment.png', dpi=150, bbox_inches='tight')
plt.show()
print('saved: q2_profit_by_quarter_segment.png')"""),

md("""### Q2 Findings

**Finding:** VIP customers consistently generate the highest average profit per order
across all quarters. Occasional buyers show the lowest and most volatile returns.

**Note on Dormant:** Dormant does not appear in this table because Dormant buyers have
zero orders in the dataset -- not low activity, literally none. This affects ~23,700 of
the ~47,500 total buyers (~50%). See Q5 for acquisition/reactivation implications.
"""),

md("""---
## Q3 — Referral Program Cost
*How much revenue is the referral program costing, and is it worth it?*"""),

code("""\
from features import estimate_referral_cost

summary, discount_cost = estimate_referral_cost(orders)

print('=== REFERRAL PROGRAM SUMMARY ===')
print(summary.round(2).to_string(index=False))
print()
print(f'Estimated revenue lost to referral discounts: ${discount_cost:,.2f}')
print(f'(Rate: {REFERRAL_DISCOUNT_RATE:.0%} off first order, referred buyers only )')

fig, axes = plt.subplots(1, 3, figsize=(14, 5))

metrics = [
    ('avg_revenue_per_buyer', 'Avg Revenue per Buyer ($)', axes[0]),
    ('avg_orders_per_buyer',  'Avg Orders per Buyer',      axes[1]),
    ('total_revenue',         'Total Revenue ($)',          axes[2]),
]

labels = ['Not Referred', 'Referred']
colors = ['steelblue', 'tomato']

for col, title, ax in metrics:
    vals = [
        summary.loc[summary['is_ref'] == False, col].values[0],
        summary.loc[summary['is_ref'] == True,  col].values[0],
    ]
    bars = ax.bar(labels, vals, color=colors)
    ax.set_title(title)
    ax.yaxis.set_major_formatter(
        mticker.FuncFormatter(lambda x, _: f'${x:,.0f}')
        if '$' in title else mticker.FuncFormatter(lambda x, _: f'{x:.2f}')
    )
    for bar, val in zip(bars, vals):
        ax.text(bar.get_x() + bar.get_width()/2,
                bar.get_height() * 1.01,
                f'${val:,.2f}' if '$' in title else f'{val:.2f}',
                ha='center', va='bottom', fontsize=9)

plt.suptitle(f'Q3: Referral Program Impact\\n'
             f'Estimated Cost: ${discount_cost:,.2f} '
             f'({REFERRAL_DISCOUNT_RATE:.0%} off first order, referred buyers only)',
             fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig(FIGURES_DIR / 'q3_referral_program.png', dpi=150, bbox_inches='tight')
plt.show()
print('saved: q3_referral_program.png')"""),

md("""### Q3 Findings

**Finding:** Referred and non-referred buyers show nearly identical average revenue
per buyer and orders per buyer. The referral program is acquiring customers who behave
the same as organic customers -- the discount appears to provide no behavioral lift.
"""),

md("""---
## Q4 — Black Friday Impact
*How does Black Friday affect volume and revenue by customer segment?*"""),

code("""\
delivered = orders[orders['is_revenue_eligible']].copy()
bf        = delivered[delivered['is_black_friday']]

annual = delivered.groupby(delivered['order_datetime'].dt.year).agg(
    total_orders  = ('order_id',      'count'),
    total_revenue = ('order_revenue', 'sum'),
).reset_index()
annual.columns = ['year', 'total_orders', 'total_revenue']

bf_annual = bf.groupby(bf['order_datetime'].dt.year).agg(
    bf_orders  = ('order_id',      'count'),
    bf_revenue = ('order_revenue', 'sum'),
).reset_index()
bf_annual.columns = ['year', 'bf_orders', 'bf_revenue']

summary_yr = annual.merge(bf_annual, on='year')
summary_yr['bf_order_pct']   = summary_yr['bf_orders']  / summary_yr['total_orders']  * 100
summary_yr['bf_revenue_pct'] = summary_yr['bf_revenue'] / summary_yr['total_revenue'] * 100

print('Black Friday share of annual sales:')
print(summary_yr.round(2).to_string(index=False))

bf_seg = bf[bf['customer_group'].notna()].groupby('customer_group').agg(
    bf_orders     = ('order_id',      'count'),
    bf_revenue    = ('order_revenue', 'sum'),
    avg_order_val = ('order_revenue', 'mean'),
).reset_index()

all_seg = delivered[delivered['customer_group'].notna()].groupby('customer_group').agg(
    all_orders  = ('order_id',      'count'),
    all_revenue = ('order_revenue', 'sum'),
).reset_index()

seg = bf_seg.merge(all_seg, on='customer_group')
seg['order_pct']   = seg['bf_orders']  / seg['all_orders']  * 100
seg['revenue_pct'] = seg['bf_revenue'] / seg['all_revenue'] * 100

_seg_order = [s for s in SEGMENT_ORDER if s in seg['customer_group'].values]
seg = seg.set_index('customer_group').reindex(_seg_order).reset_index()

print()
print('Black Friday by segment:')
print(seg[['customer_group','bf_orders','order_pct',
           'bf_revenue','revenue_pct','avg_order_val']].round(2).to_string(index=False))

fig, axes = plt.subplots(1, 2, figsize=(14, 5))
width = 0.35

ax = axes[0]
x  = range(len(seg))
ax.bar([i - width/2 for i in x], seg['bf_orders'], width,
       label='BF Orders', color='tomato')
ax2 = ax.twinx()
ax2.plot(list(x), seg['order_pct'], 'D--', color='navy',
         markersize=7, label='BF % of Annual')
ax.set_xticks(list(x))
ax.set_xticklabels(seg['customer_group'], rotation=20)
ax.set_ylabel('BF Order Count')
ax2.set_ylabel('BF % of Annual Orders')
ax.set_title('Black Friday Volume by Segment')
h1, l1 = ax.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax.legend(h1 + h2, l1 + l2, fontsize=8, loc='upper right')

ax3 = axes[1]
non_bf     = delivered[delivered['customer_group'].notna() & ~delivered['is_black_friday']]
non_bf_aov = non_bf.groupby('customer_group')['order_revenue'].mean().reset_index()
non_bf_aov.columns = ['customer_group', 'non_bf_aov']
aov = seg[['customer_group', 'avg_order_val']].merge(non_bf_aov, on='customer_group')

_aov_order = [s for s in SEGMENT_ORDER if s in aov['customer_group'].values]
aov = aov.set_index('customer_group').reindex(_aov_order)

x3 = range(len(aov))
ax3.bar([i - width/2 for i in x3], aov['avg_order_val'], width,
        label='Black Friday', color='tomato')
ax3.bar([i + width/2 for i in x3], aov['non_bf_aov'], width,
        label='Rest of Year', color='steelblue')
ax3.set_xticks(list(x3))
ax3.set_xticklabels(aov.index, rotation=20)
ax3.set_ylabel('Avg Order Value ($)')
ax3.set_title('Black Friday vs Rest-of-Year AOV by Segment')
ax3.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${x:.2f}'))
ax3.legend()

plt.suptitle('Q4: Black Friday Impact on Annual Sales by Segment',
             fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig(FIGURES_DIR / 'q4_black_friday.png', dpi=150, bbox_inches='tight')
plt.show()
print('saved: q4_black_friday.png')"""),

md("""### Q4 Findings

**Note on figures:** Revenue and profit for Black Friday orders already reflect the 20% discount
applied in the pipeline (`BLACK_FRIDAY_DISCOUNT_RATE = 0.20` in `features.py`). The raw price
data does not include this discount — it is computed before any aggregation.

**Finding:** Black Friday drives a volume spike concentrated in Regular and Occasional segments.
BF average order value is lower than rest-of-year by construction (20% reduction on product revenue),
making Black Friday primarily an acquisition and volume event rather than a margin event.
The shipping tier also shifts downward on BF (lower order totals → more orders hit the $7.99 tier),
which compresses net order profit further relative to rest-of-year orders.
"""),

md("""---
## Q5 — Best Customer Base & Future KPIs
*Where is our best customer base and what KPIs should we track to acquire more customers?*"""),

code("""\
delivered = orders[orders['is_revenue_eligible']].copy()

region_perf = (
    delivered[delivered['region'].notna()]
    .groupby('region')
    .agg(
        unique_buyers = ('buyer_id',      'nunique'),
        total_revenue = ('order_revenue', 'sum'),
        total_orders  = ('order_id',      'count'),
    )
    .reset_index()
)
region_perf['revenue_per_buyer'] = (
    region_perf['total_revenue'] / region_perf['unique_buyers']
)
region_perf['orders_per_buyer'] = (
    region_perf['total_orders'] / region_perf['unique_buyers']
)

print('Revenue per buyer by region:')
print(region_perf[['region','unique_buyers','revenue_per_buyer',
                   'orders_per_buyer']].round(2).to_string(index=False))

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

ax = axes[0]
rp = region_perf.sort_values('revenue_per_buyer')
bar_colors = sns.color_palette('muted', len(rp))
bars = ax.barh(rp['region'], rp['revenue_per_buyer'], color=bar_colors)
ax.set_xlabel('Revenue per Buyer ($)')
ax.set_title('Revenue per Buyer by Region')
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${x:,.0f}'))
for bar in bars:
    w = bar.get_width()
    ax.text(w * 1.01, bar.get_y() + bar.get_height()/2,
            f'${w:,.2f}', va='center', fontsize=8)

ax2 = axes[1]
seg_freq = (
    delivered[delivered['customer_group'].notna()]
    .groupby('customer_group')
    .agg(
        orders = ('order_id', 'count'),
        buyers = ('buyer_id', 'nunique'),
    )
    .assign(opb=lambda d: d['orders'] / d['buyers'])
    .reindex([s for s in SEGMENT_ORDER if s in delivered['customer_group'].unique()])
    .reset_index()
)
colors2 = ['gold' if s == 'VIP' else 'steelblue' for s in seg_freq['customer_group']]
ax2.bar(seg_freq['customer_group'], seg_freq['opb'], color=colors2)
ax2.set_ylabel('Avg Orders per Buyer')
ax2.set_title('Purchase Frequency by Segment\\n(Gold = VIP benchmark)')
for i, v in enumerate(seg_freq['opb']):
    ax2.text(i, v + 0.02, f'{v:.2f}', ha='center', va='bottom', fontsize=9)

plt.suptitle('Q5: Best Customer Base & Acquisition Opportunity',
             fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig(FIGURES_DIR / 'q5_customer_base.png', dpi=150, bbox_inches='tight')
plt.show()
print('saved: q5_customer_base.png')"""),

md("""### Q5 Findings

**Headline finding:** Roughly half the buyer base (~23,700 of ~47,500) has never placed
a single order. Before optimizing acquisition spend on new customers, it is worth
understanding why half of existing buyers never converted -- whether that is a
data/labeling artifact (e.g. "Dormant" assigned at signup rather than earned through
inactivity) or a genuine activation failure. Check signup_date distribution for Dormant
buyers: if they skew recent, the label is a default for new signups, not a business problem.

**Finding:** Revenue per buyer is broadly similar across regions -- the spread is narrow,
suggesting channel targeting matters more than geography alone.
VIP buyers order significantly more frequently than all other segments.

**Recommended KPIs to track:**

| KPI | Why |
|---|---|
| Buyer activation rate (% who place ≥1 order within N days) | This dataset offers zero visibility into it -- biggest gap |
| Revenue per new buyer (by region) | Measures acquisition quality, not just volume |
| 90-day repurchase rate | Leading indicator of whether new buyers become Frequent |
| BF new buyer conversion rate | Measures acquisition effectiveness of the event |
| Catalog profit margin % | Tracks health of product rationalization effort |
| Referred buyer 90-day retention | Measures referral program ROI beyond first order |"""),

md("""---
## Summary of Recommendations

| Question | Finding | Recommendation |
|---|---|---|
| Q1: 24/7 Staffing | Overnight = small % of orders | Tiered staffing -- full days, reduced overnight |
| Q2: Profit by Segment | VIP/Frequent drive stable profit | Invest in retention; Dormant = 0 orders, see Q5 |
| Q3: Referral Program | No behavioral lift vs organic | Confirm terms, run cohort retention analysis |
| Q4: Black Friday | Volume spike, margin compressed | Acquisition event + Q1 follow-up campaign |
| Q5: Best Customers | Similar revenue across regions | Focus on channel quality + VIP frequency KPIs |"""),

]

save(nb2, "02_analysis.ipynb")

print("\ndone -- both notebooks created in notebooks/")