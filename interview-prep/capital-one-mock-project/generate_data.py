"""
Capital One BCP Field Strategy — Mock Dataset Generator
Run: python generate_data.py
Outputs: customers.csv, transactions.csv, field_reps.csv, campaigns.csv
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

random.seed(42)
np.random.seed(42)

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ── Constants ──────────────────────────────────────────────────────────────────

INDUSTRIES = {
    'Technology':            0.15,
    'Professional Services': 0.20,
    'Healthcare':            0.15,
    'Retail':                0.20,
    'Construction':          0.15,
    'Restaurants':           0.10,
    'Manufacturing':         0.05,
}

SIZES = {'Small': 0.60, 'Medium': 0.30, 'Large': 0.10}

PRODUCTS = {
    'Business Rewards':  0.50,
    'Business Platinum': 0.25,
    'Business Cash':     0.25,
}

TERRITORIES = {
    'Northeast': ['REP01', 'REP02', 'REP03', 'REP04', 'REP05'],
    'Southeast': ['REP06', 'REP07', 'REP08', 'REP09', 'REP10'],
    'Midwest':   ['REP11', 'REP12', 'REP13', 'REP14', 'REP15'],
    'West':      ['REP16', 'REP17', 'REP18', 'REP19', 'REP20'],
}

TERRITORY_STATES = {
    'Northeast': ['NY', 'MA', 'PA', 'NJ', 'CT', 'VA', 'MD', 'DC'],
    'Southeast': ['FL', 'GA', 'NC', 'SC', 'TN', 'AL', 'MS'],
    'Midwest':   ['IL', 'OH', 'MI', 'IN', 'WI', 'MN', 'MO'],
    'West':      ['CA', 'WA', 'OR', 'CO', 'AZ', 'TX', 'NV'],
}

MERCHANT_CATEGORIES = [
    'Office Supplies', 'Travel', 'Dining', 'Fuel',
    'Technology Equipment', 'Healthcare Supplies',
    'Construction Supplies', 'Marketing & Advertising',
    'Utilities', 'Other'
]

# Category spend weights by industry — baked-in patterns for realistic analysis
INDUSTRY_CATEGORY_WEIGHTS = {
    'Technology':            [0.15, 0.20, 0.10, 0.05, 0.30, 0.02, 0.01, 0.12, 0.03, 0.02],
    'Professional Services': [0.20, 0.25, 0.15, 0.05, 0.10, 0.02, 0.01, 0.15, 0.05, 0.02],
    'Healthcare':            [0.15, 0.10, 0.08, 0.05, 0.10, 0.35, 0.01, 0.08, 0.05, 0.03],
    'Retail':                [0.20, 0.10, 0.10, 0.08, 0.15, 0.02, 0.05, 0.15, 0.10, 0.05],
    'Construction':          [0.10, 0.08, 0.07, 0.20, 0.05, 0.01, 0.35, 0.05, 0.07, 0.02],
    'Restaurants':           [0.10, 0.05, 0.25, 0.12, 0.08, 0.02, 0.01, 0.20, 0.12, 0.05],
    'Manufacturing':         [0.12, 0.10, 0.07, 0.18, 0.10, 0.02, 0.20, 0.08, 0.10, 0.03],
}

# ── Field Reps ─────────────────────────────────────────────────────────────────

REP_NAMES = [
    'James Carter', 'Priya Nair', 'Michael Torres', 'Sarah Kim', 'David Okafor',
    'Emily Chen', 'Marcus Webb', 'Aisha Patel', "Ryan O'Brien", 'Natalie Cruz',
    'Kevin Zhao', 'Lakshmi Iyer', 'Daniel Murphy', 'Fatima Hassan', 'Chris Anderson',
    'Yuki Tanaka', 'Brandon Lee', 'Olivia Smith', 'Raj Gupta', 'Megan Johnson'
]

# Performance multiplier vs quota — built-in signal for Q3 reps analysis
REP_PERFORMANCE = {
    'REP01': 1.05, 'REP02': 0.95, 'REP03': 1.18,  # NE: REP03 top
    'REP04': 1.02, 'REP05': 0.88,
    'REP06': 0.92, 'REP07': 0.74, 'REP08': 1.00,  # SE: REP07 underperformer
    'REP09': 1.08, 'REP10': 0.85,
    'REP11': 1.01, 'REP12': 1.22, 'REP13': 0.97,  # MW: REP12 top
    'REP14': 0.71, 'REP15': 1.03,                  # MW: REP14 underperformer
    'REP16': 1.09, 'REP17': 1.15, 'REP18': 0.99,  # W: REP17 top
    'REP19': 1.04, 'REP20': 0.93,
}


def generate_reps():
    rows = []
    rep_idx = 0
    for territory, reps in TERRITORIES.items():
        for rep_id in reps:
            quota = random.randint(220, 320) * 1000
            rows.append({
                'rep_id': rep_id,
                'rep_name': REP_NAMES[rep_idx],
                'territory': territory,
                'quarterly_quota_usd': quota,
                'q1_2026_actual_usd': int(quota * REP_PERFORMANCE[rep_id]),
                'quota_attainment_pct': round(REP_PERFORMANCE[rep_id] * 100, 1),
                'active_customer_count': random.randint(10, 18),
            })
            rep_idx += 1
    return pd.DataFrame(rows)


# ── Customers ──────────────────────────────────────────────────────────────────

BUSINESS_PREFIXES = [
    'Apex', 'Summit', 'Pioneer', 'Crestview', 'Nexus', 'Harbor', 'Falcon',
    'Sterling', 'Atlas', 'Meridian', 'Vanguard', 'Pinnacle', 'Horizon', 'Nova',
    'Cascade', 'Iron', 'Cobalt', 'Delta', 'Ember', 'Granite', 'Helix', 'Indigo',
    'Jade', 'Kestrel', 'Lumen', 'Maple', 'Nordic', 'Orbit', 'Pacific', 'Quest',
    'Relay', 'Sierra', 'Titan', 'Unity', 'Vector', 'Waypoint', 'Xenon', 'Yield',
    'Zenith', 'Amber', 'Bravo', 'Cedar', 'Dover', 'Echo', 'Flint', 'Grove',
]

BUSINESS_SUFFIXES = {
    'Technology':            ['Tech', 'Systems', 'Solutions', 'Digital', 'Labs', 'Software'],
    'Professional Services': ['Consulting', 'Advisors', 'Group', 'Partners', 'Associates'],
    'Healthcare':            ['Health', 'Medical', 'Care', 'Wellness', 'Clinic'],
    'Retail':                ['Retail', 'Goods', 'Supply', 'Mart', 'Depot'],
    'Construction':          ['Construction', 'Builders', 'Contractors', 'Development'],
    'Restaurants':           ['Restaurant', 'Kitchen', 'Bistro', 'Grill', 'Eatery'],
    'Manufacturing':         ['Manufacturing', 'Industries', 'Products', 'Works'],
}


def generate_customers(reps_df):
    industries  = list(INDUSTRIES.keys())
    ind_probs   = list(INDUSTRIES.values())
    size_keys   = list(SIZES.keys())
    size_probs  = list(SIZES.values())
    prod_keys   = list(PRODUCTS.keys())
    prod_probs  = list(PRODUCTS.values())

    # Build rep pool weighted by active_customer_count
    rep_pool = []
    for _, rep in reps_df.iterrows():
        rep_pool.extend([rep['rep_id']] * rep['active_customer_count'])
    random.shuffle(rep_pool)

    top_reps   = {'REP03', 'REP12', 'REP17'}
    under_reps = {'REP07', 'REP14'}

    prefixes = (BUSINESS_PREFIXES * 6)[:250]
    random.shuffle(prefixes)

    rows = []
    for i in range(250):
        cid      = f'CUST{i+1:03d}'
        industry = np.random.choice(industries, p=ind_probs)
        size     = np.random.choice(size_keys, p=size_probs)
        product  = np.random.choice(prod_keys, p=prod_probs)
        rep_id   = rep_pool[i % len(rep_pool)]

        # Top reps have more Large/Tech/ProServ customers — explains their quota attainment
        if rep_id in top_reps:
            if random.random() < 0.40:
                size = np.random.choice(['Medium', 'Large'], p=[0.55, 0.45])
            if random.random() < 0.35:
                industry = np.random.choice(['Technology', 'Professional Services'])

        # Credit limit by size
        if size == 'Small':
            credit_limit = random.randint(5, 20) * 1000
        elif size == 'Medium':
            credit_limit = random.randint(20, 75) * 1000
        else:
            credit_limit = random.randint(75, 200) * 1000

        acq_date  = datetime(2022, 1, 1) + timedelta(days=random.randint(0, 900))
        territory = reps_df[reps_df['rep_id'] == rep_id]['territory'].values[0]
        state     = random.choice(TERRITORY_STATES[territory])
        suffix    = random.choice(BUSINESS_SUFFIXES[industry])
        name      = f'{prefixes[i]} {suffix}'

        rows.append({
            'customer_id':      cid,
            'business_name':    name,
            'industry':         industry,
            'business_size':    size,
            'state':            state,
            'territory':        territory,
            'card_product':     product,
            'credit_limit_usd': credit_limit,
            'acquisition_date': acq_date.strftime('%Y-%m-%d'),
            'rep_id':           rep_id,
        })

    return pd.DataFrame(rows)


# ── Transactions ───────────────────────────────────────────────────────────────

def base_monthly_spend(size, product):
    base = {'Small': 2500, 'Medium': 8000, 'Large': 25000}[size]
    mult = {'Business Rewards': 1.4, 'Business Platinum': 1.2, 'Business Cash': 1.0}[product]
    return base * mult


def generate_transactions(customers_df):
    # 30 customers in Restaurants/Retail will show declining spend from Jan 2026 (churn signal)
    churn_candidates = customers_df[
        customers_df['industry'].isin(['Restaurants', 'Retail'])
    ].sample(30, random_state=42)['customer_id'].tolist()

    rows     = []
    txn_id   = 1
    start    = datetime(2024, 1, 1)
    end      = datetime(2026, 6, 30)

    for _, cust in customers_df.iterrows():
        cid       = cust['customer_id']
        industry  = cust['industry']
        size      = cust['business_size']
        product   = cust['card_product']
        acq_date  = datetime.strptime(cust['acquisition_date'], '%Y-%m-%d')
        cat_w     = INDUSTRY_CATEGORY_WEIGHTS[industry]

        monthly_base  = base_monthly_spend(size, product)
        txns_per_mo   = {'Small': 5, 'Medium': 12, 'Large': 25}[size]

        current = max(acq_date, start).replace(day=1)
        while current <= end:
            # Seasonal multiplier
            if current.month in [11, 12]:
                seasonal = 1.25    # Q4 holiday/year-end spike
            elif current.month in [1, 2]:
                seasonal = 0.88    # Q1 slow start
            else:
                seasonal = 1.00

            # YoY growth (8% general; Tech Equipment +20%; Travel -10% in 2026)
            yoy = 1.08 if current.year == 2026 else 1.00

            # Churn decay: declining 12% per month from Jan 2026
            churn_mult = 1.0
            if cid in churn_candidates and current >= datetime(2026, 1, 1):
                months_in = (current.year - 2026) * 12 + (current.month - 1)
                churn_mult = max(0.35, 1.0 - 0.12 * (months_in + 1))

            total_mo_spend = monthly_base * seasonal * yoy * churn_mult
            n_txns = max(1, int(np.random.normal(txns_per_mo, txns_per_mo * 0.2)))

            for _ in range(n_txns):
                category  = np.random.choice(MERCHANT_CATEGORIES, p=cat_w)
                cat_mult  = 1.0
                if category == 'Technology Equipment' and current.year == 2026:
                    cat_mult = 1.20
                elif category == 'Travel' and current.year == 2026:
                    cat_mult = 0.88

                avg_txn = (total_mo_spend / n_txns) * cat_mult
                amount  = max(10.0, round(
                    float(np.random.lognormal(np.log(max(1, avg_txn)), 0.5)), 2
                ))

                txn_date = current + timedelta(days=random.randint(0, 27))
                if txn_date > end:
                    txn_date = end

                rows.append({
                    'transaction_id':   f'TXN{txn_id:06d}',
                    'customer_id':      cid,
                    'transaction_date': txn_date.strftime('%Y-%m-%d'),
                    'amount_usd':       amount,
                    'merchant_category': category,
                    'card_product':     product,
                })
                txn_id += 1

            # Advance month
            current = (current.replace(day=28) + timedelta(days=4)).replace(day=1)

    return pd.DataFrame(rows)


# ── Campaigns ─────────────────────────────────────────────────────────────────

def generate_campaigns(customers_df, txns_df):
    sampled     = customers_df.sample(150, random_state=7)
    channels    = ['In-Person', 'Phone', 'Email']
    chan_probs  = [0.30, 0.35, 0.35]

    # Built-in signal: In-Person ~28% lift, Phone ~12%, Email ~5%
    lift_map    = {'In-Person': 0.28, 'Phone': 0.12, 'Email': 0.05}
    conv_map    = {'In-Person': 0.45, 'Phone': 0.22, 'Email': 0.08}

    rows = []
    for i, (_, cust) in enumerate(sampled.iterrows()):
        cid      = cust['customer_id']
        channel  = np.random.choice(channels, p=chan_probs)
        out_date = datetime(2026, 1, 1) + timedelta(days=random.randint(0, 89))

        cust_txns = txns_df[txns_df['customer_id'] == cid].copy()
        cust_txns['transaction_date'] = pd.to_datetime(cust_txns['transaction_date'])

        before_mask = (
            (cust_txns['transaction_date'] >= out_date - timedelta(days=30)) &
            (cust_txns['transaction_date'] <  out_date)
        )
        after_mask = (
            (cust_txns['transaction_date'] >= out_date) &
            (cust_txns['transaction_date'] <  out_date + timedelta(days=30))
        )

        spend_before = float(cust_txns[before_mask]['amount_usd'].sum())
        spend_after_raw = float(cust_txns[after_mask]['amount_usd'].sum())

        lift  = lift_map[channel] + float(np.random.normal(0, 0.05))
        spend_after = round(spend_after_raw * (1 + lift), 2) if spend_after_raw > 0 else round(spend_before * (1 + lift), 2)
        lift_usd = round(spend_after - spend_before, 2)
        lift_pct = round((lift_usd / spend_before * 100) if spend_before > 0 else 0.0, 1)

        converted = 1 if random.random() < conv_map[channel] else 0

        rows.append({
            'campaign_id':          f'CAMP{i+1:04d}',
            'customer_id':          cid,
            'rep_id':               cust['rep_id'],
            'outreach_date':        out_date.strftime('%Y-%m-%d'),
            'channel':              channel,
            'converted':            converted,
            'spend_30d_before_usd': round(spend_before, 2),
            'spend_30d_after_usd':  spend_after,
            'spend_lift_usd':       lift_usd,
            'spend_lift_pct':       lift_pct,
        })

    return pd.DataFrame(rows)


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print("Generating Capital One BCP Field Strategy datasets...\n")

    reps_df = generate_reps()
    reps_df.to_csv(os.path.join(OUT_DIR, 'field_reps.csv'), index=False)
    print(f"  field_reps.csv     : {len(reps_df)} rows")

    customers_df = generate_customers(reps_df)
    customers_df.to_csv(os.path.join(OUT_DIR, 'customers.csv'), index=False)
    print(f"  customers.csv      : {len(customers_df)} rows")

    txns_df = generate_transactions(customers_df)
    txns_df.to_csv(os.path.join(OUT_DIR, 'transactions.csv'), index=False)
    print(f"  transactions.csv   : {len(txns_df)} rows")

    campaigns_df = generate_campaigns(customers_df, txns_df)
    campaigns_df.to_csv(os.path.join(OUT_DIR, 'campaigns.csv'), index=False)
    print(f"  campaigns.csv      : {len(campaigns_df)} rows")

    print("\nDone. Open README.md for the full project brief and business questions.")
