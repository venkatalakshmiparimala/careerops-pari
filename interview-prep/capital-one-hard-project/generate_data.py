"""
Capital One BCP Field Strategy — HARD Mock Dataset Generator
Principal DA Level

Covers every Principal DA skill:
  1. Data Quality Audit       — reversals, multi-swipes, velocity bursts, NULLs, format errors
  2. RFM Segmentation         — quintile scoring, CLV estimation
  3. Cohort Retention         — acquisition cohort x month heatmap
  4. Fraud & Anomaly Detection — velocity, Z-score amount, new merchant signals
  5. Churn Prediction Model   — binary classifier, feature importance
  6. A/B Test Analysis        — significance testing, effect size, power
  7. Rep Attribution Regression — controlling for customer mix
  8. Executive Synthesis       — Q3 action plan

Run: python3 generate_data.py
Outputs: accounts.csv, transactions.csv, merchants.csv, field_reps.csv, ab_test.csv
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os
import json

random.seed(42)
np.random.seed(42)

OUT = os.path.dirname(os.path.abspath(__file__))

# ── Constants ──────────────────────────────────────────────────────────────────

INDUSTRIES = {
    'Technology': 0.15, 'Professional Services': 0.18,
    'Healthcare': 0.13, 'Retail': 0.18, 'Construction': 0.14,
    'Restaurants': 0.12, 'Manufacturing': 0.06, 'Logistics': 0.04,
}
SIZES    = {'Small': 0.58, 'Medium': 0.30, 'Large': 0.12}
PRODUCTS = {'Business Rewards': 0.48, 'Business Platinum': 0.26, 'Business Cash': 0.26}

TERRITORIES = {
    'Northeast': ['REP01','REP02','REP03','REP04','REP05'],
    'Southeast': ['REP06','REP07','REP08','REP09','REP10'],
    'Midwest':   ['REP11','REP12','REP13','REP14','REP15'],
    'West':      ['REP16','REP17','REP18','REP19','REP20'],
}
TERRITORY_STATES = {
    'Northeast': ['NY','MA','PA','NJ','CT','VA','MD','DC'],
    'Southeast': ['FL','GA','NC','SC','TN','AL'],
    'Midwest':   ['IL','OH','MI','IN','WI','MN'],
    'West':      ['CA','WA','OR','CO','AZ','TX'],
}

MERCHANT_CATEGORIES = [
    'Office Supplies','Travel','Dining','Fuel',
    'Technology Equipment','Healthcare Supplies',
    'Construction Supplies','Marketing & Advertising',
    'Utilities','Software & Subscriptions','Other',
]

INDUSTRY_CAT_WEIGHTS = {
    'Technology':            [0.13,0.18,0.10,0.04,0.28,0.02,0.01,0.12,0.03,0.07,0.02],
    'Professional Services': [0.18,0.22,0.14,0.04,0.09,0.02,0.01,0.14,0.05,0.09,0.02],
    'Healthcare':            [0.14,0.09,0.07,0.04,0.09,0.32,0.01,0.07,0.06,0.08,0.03],
    'Retail':                [0.18,0.09,0.09,0.07,0.14,0.02,0.05,0.14,0.10,0.07,0.05],
    'Construction':          [0.09,0.07,0.06,0.20,0.04,0.01,0.34,0.05,0.08,0.04,0.02],
    'Restaurants':           [0.09,0.04,0.24,0.11,0.07,0.02,0.01,0.19,0.12,0.06,0.05],
    'Manufacturing':         [0.11,0.09,0.06,0.17,0.09,0.02,0.19,0.07,0.11,0.06,0.03],
    'Logistics':             [0.08,0.12,0.08,0.30,0.04,0.01,0.10,0.06,0.12,0.05,0.04],
}

REP_NAMES = [
    'James Carter','Priya Nair','Michael Torres','Sarah Kim','David Okafor',
    'Emily Chen','Marcus Webb','Aisha Patel',"Ryan O'Brien",'Natalie Cruz',
    'Kevin Zhao','Lakshmi Iyer','Daniel Murphy','Fatima Hassan','Chris Anderson',
    'Yuki Tanaka','Brandon Lee','Olivia Smith','Raj Gupta','Megan Johnson',
]
REP_PERFORMANCE = {
    'REP01':1.06,'REP02':0.94,'REP03':1.21,'REP04':1.03,'REP05':0.87,
    'REP06':0.91,'REP07':0.73,'REP08':1.01,'REP09':1.09,'REP10':0.84,
    'REP11':1.02,'REP12':1.24,'REP13':0.96,'REP14':0.70,'REP15':1.04,
    'REP16':1.10,'REP17':1.17,'REP18':0.98,'REP19':1.05,'REP20':0.92,
}

BUS_PREFIXES = [
    'Apex','Summit','Pioneer','Crestview','Nexus','Harbor','Falcon','Sterling',
    'Atlas','Meridian','Vanguard','Pinnacle','Horizon','Nova','Cascade','Iron',
    'Cobalt','Delta','Ember','Granite','Helix','Indigo','Jade','Kestrel','Lumen',
    'Maple','Nordic','Orbit','Pacific','Quest','Relay','Sierra','Titan','Unity',
    'Vector','Waypoint','Zenith','Amber','Bravo','Cedar','Dover','Echo','Flint',
    'Grove','Haven','Ivory','Jasper','Knight','Lunar','Mosaic','Onyx','Prism',
]
BUS_SUFFIXES = {
    'Technology':['Tech','Systems','Solutions','Digital','Labs','Software','Data'],
    'Professional Services':['Consulting','Advisors','Group','Partners','Associates','Strategies'],
    'Healthcare':['Health','Medical','Care','Wellness','Clinic','Sciences'],
    'Retail':['Retail','Goods','Supply','Mart','Depot','Commerce'],
    'Construction':['Construction','Builders','Contractors','Development','Group'],
    'Restaurants':['Restaurant','Kitchen','Bistro','Grill','Eatery','Cafe'],
    'Manufacturing':['Manufacturing','Industries','Products','Works','Fabrication'],
    'Logistics':['Logistics','Freight','Transport','Shipping','Supply Chain'],
}

START   = datetime(2023, 1, 1)   # longer history for cohort analysis
END     = datetime(2026, 6, 30)
SNAP    = datetime(2026, 6, 30)  # snapshot date for RFM / churn


# ── 1. Field Reps ─────────────────────────────────────────────────────────────

def gen_reps():
    rows, idx = [], 0
    for territory, reps in TERRITORIES.items():
        for rep_id in reps:
            quota = random.randint(200, 340) * 1000
            rows.append({
                'rep_id': rep_id,
                'rep_name': REP_NAMES[idx],
                'territory': territory,
                'quarterly_quota_usd': quota,
                'q1_2026_actual_usd': int(quota * REP_PERFORMANCE[rep_id]),
                'quota_attainment_pct': round(REP_PERFORMANCE[rep_id] * 100, 1),
                'active_account_count': random.randint(12, 20),
                'avg_account_tenure_months': random.randint(8, 36),
                'pct_large_accounts': round(random.uniform(0.05, 0.45), 2),
                'campaigns_run_q1': random.randint(3, 18),
            })
            idx += 1
    return pd.DataFrame(rows)


# ── 2. Merchants ──────────────────────────────────────────────────────────────

MERCHANT_NAME_TEMPLATES = {
    'Office Supplies':        ['Staples #{n}','OfficeMax #{n}','Office Depot #{n}','Viking Supply #{n}','Quill #{n}'],
    'Travel':                 ['Delta Air #{n}','United #{n}','Marriott #{n}','Hilton #{n}','Hertz #{n}','Hyatt #{n}'],
    'Dining':                 ['Panera #{n}','Chipotle #{n}','Olive Garden #{n}','Local Bistro #{n}','Subway #{n}'],
    'Fuel':                   ['Shell #{n}','BP #{n}','ExxonMobil #{n}','Chevron #{n}','Sunoco #{n}'],
    'Technology Equipment':   ['Dell #{n}','B&H Photo #{n}','CDW #{n}','Newegg #{n}','Best Buy #{n}'],
    'Healthcare Supplies':    ['McKesson #{n}','Henry Schein #{n}','Medline #{n}','Cardinal Health #{n}'],
    'Construction Supplies':  ['Home Depot #{n}','Lowes #{n}','Menards #{n}','Fastenal #{n}'],
    'Marketing & Advertising':['Google Ads #{n}','Meta Ads #{n}','HubSpot #{n}','Mailchimp #{n}'],
    'Utilities':              ['Dominion Energy #{n}','Con Edison #{n}','Duke Energy #{n}','Comcast Biz #{n}'],
    'Software & Subscriptions':['AWS #{n}','Salesforce #{n}','Microsoft 365 #{n}','Slack #{n}','Zoom #{n}'],
    'Other':                  ['Miscellaneous Vendor #{n}','Local Supplier #{n}','Unnamed Vendor #{n}'],
}
MCC_CODES = {
    'Office Supplies':'5111','Travel':'4511','Dining':'5812','Fuel':'5541',
    'Technology Equipment':'5045','Healthcare Supplies':'5047',
    'Construction Supplies':'5251','Marketing & Advertising':'7311',
    'Utilities':'4900','Software & Subscriptions':'7372','Other':'5999',
}

def gen_merchants():
    rows, mid = [], 1
    for cat, templates in MERCHANT_NAME_TEMPLATES.items():
        count = 20 if cat in ['Dining','Travel','Fuel'] else 12
        for i in range(1, count + 1):
            tmpl = random.choice(templates)
            rows.append({
                'merchant_id':       f'MER{mid:04d}',
                'merchant_name':     tmpl.replace('#{n}', str(i)),
                'merchant_category': cat,
                'mcc_code':          MCC_CODES[cat],
                'city':              random.choice(['New York','Chicago','Los Angeles','Houston','Phoenix','Dallas','Atlanta','Seattle']),
                'state':             random.choice(['NY','IL','CA','TX','AZ','GA','WA','FL']),
                'is_high_risk':      1 if cat in ['Other'] and random.random() < 0.3 else 0,
            })
            mid += 1
    return pd.DataFrame(rows)


# ── 3. Accounts ───────────────────────────────────────────────────────────────

def gen_accounts(reps_df):
    ind_keys  = list(INDUSTRIES.keys())
    ind_probs = list(INDUSTRIES.values())
    sz_keys   = list(SIZES.keys())
    sz_probs  = list(SIZES.values())
    pr_keys   = list(PRODUCTS.keys())
    pr_probs  = list(PRODUCTS.values())

    rep_pool = []
    for _, r in reps_df.iterrows():
        rep_pool.extend([r['rep_id']] * r['active_account_count'])
    random.shuffle(rep_pool)

    top_reps   = {'REP03','REP12','REP17'}
    prefixes   = (BUS_PREFIXES * 6)[:300]
    random.shuffle(prefixes)

    rows = []
    for i in range(300):
        aid      = f'ACC{i+1:04d}'
        ind      = np.random.choice(ind_keys, p=ind_probs)
        sz       = np.random.choice(sz_keys, p=sz_probs)
        prod     = np.random.choice(pr_keys, p=pr_probs)
        rep_id   = rep_pool[i % len(rep_pool)]

        if rep_id in top_reps:
            if random.random() < 0.42:
                sz = np.random.choice(['Medium','Large'], p=[0.52,0.48])
            if random.random() < 0.38:
                ind = np.random.choice(['Technology','Professional Services'])

        cl = {'Small': random.randint(5,20)*1000,
              'Medium': random.randint(20,75)*1000,
              'Large': random.randint(75,250)*1000}[sz]

        acq = START + timedelta(days=random.randint(0, (datetime(2025,6,1)-START).days))
        territory = reps_df[reps_df['rep_id']==rep_id]['territory'].values[0]
        state     = random.choice(TERRITORY_STATES[territory])
        suffix    = random.choice(BUS_SUFFIXES[ind])
        name      = f'{prefixes[i]} {suffix}'

        rows.append({
            'account_id':       aid,
            'business_name':    name,
            'industry':         ind,
            'business_size':    sz,
            'state':            state,
            'territory':        territory,
            'card_product':     prod,
            'credit_limit_usd': cl,
            'acquisition_date': acq.strftime('%Y-%m-%d'),
            'rep_id':           rep_id,
        })

    # ── DATA QUALITY ISSUE #1: 8 duplicate account_id entries ────────────────
    # Candidates must detect and remove these before analysis
    dupes = random.sample(rows, 8)
    for d in dupes:
        dupe = d.copy()
        dupe['business_name'] = dupe['business_name'] + ' (Branch)'
        rows.append(dupe)

    return pd.DataFrame(rows)


# ── 4. Transactions ───────────────────────────────────────────────────────────

def base_monthly(sz, prod):
    base = {'Small':2200,'Medium':7500,'Large':24000}[sz]
    mult = {'Business Rewards':1.45,'Business Platinum':1.20,'Business Cash':1.00}[prod]
    return base * mult

def gen_transactions(accounts_df, merchants_df):
    # Use only first occurrence of each account_id (remove duplicates from accounts)
    clean_accts = accounts_df.drop_duplicates(subset='account_id').reset_index(drop=True)

    # Churn-risk accounts: 45 accounts with declining spend from Apr 2026
    churn_pool = clean_accts[clean_accts['industry'].isin(['Restaurants','Retail','Logistics'])].sample(45, random_state=17)['account_id'].tolist()

    # Fraud-risk accounts: 20 accounts that will get velocity bursts
    fraud_pool = clean_accts.sample(20, random_state=99)['account_id'].tolist()

    # Build merchant lookup by category
    merch_by_cat = {}
    for cat in MERCHANT_CATEGORIES:
        ids = merchants_df[merchants_df['merchant_category']==cat]['merchant_id'].tolist()
        merch_by_cat[cat] = ids if ids else merchants_df['merchant_id'].tolist()[:3]

    rows      = []
    txn_id    = 1
    bad_dates = []   # will hold indices needing date format corruption

    for _, acct in clean_accts.iterrows():
        aid      = acct['account_id']
        ind      = acct['industry']
        sz       = acct['business_size']
        prod     = acct['card_product']
        acq      = datetime.strptime(acct['acquisition_date'], '%Y-%m-%d')
        cat_w    = INDUSTRY_CAT_WEIGHTS[ind]
        mo_base  = base_monthly(sz, prod)
        txns_mo  = {'Small':5,'Medium':12,'Large':28}[sz]

        current = max(acq, START).replace(day=1)
        while current <= END:
            seasonal = 1.25 if current.month in [11,12] else (0.87 if current.month in [1,2] else 1.0)
            yoy      = 1.08 if current.year == 2026 else (1.04 if current.year == 2025 else 1.0)

            churn_mult = 1.0
            if aid in churn_pool and current >= datetime(2026,4,1):
                m = (current.year-2026)*12 + (current.month-4)
                churn_mult = max(0.25, 1.0 - 0.15*(m+1))

            total = mo_base * seasonal * yoy * churn_mult
            n     = max(1, int(np.random.normal(txns_mo, txns_mo*0.2)))

            for _ in range(n):
                cat   = np.random.choice(MERCHANT_CATEGORIES, p=cat_w)
                cm    = 1.20 if (cat=='Technology Equipment' and current.year==2026) else \
                        (0.86 if (cat=='Travel' and current.year==2026) else 1.0)
                avg   = (total/n)*cm
                amt   = max(8.0, round(float(np.random.lognormal(np.log(max(1,avg)),0.48)),2))
                day   = random.randint(0,27)
                dt    = min(current+timedelta(days=day), END)
                mids  = merch_by_cat[cat]
                mid   = random.choice(mids)
                rows.append({
                    'transaction_id':   f'TXN{txn_id:07d}',
                    'account_id':       aid,
                    'transaction_date': dt.strftime('%Y-%m-%d'),
                    'amount_usd':       amt,
                    'merchant_id':      mid,
                    'merchant_category':cat,
                    'card_product':     prod,
                    'transaction_type': 'PURCHASE',
                    'status':           'SETTLED',
                })
                txn_id += 1

            current = (current.replace(day=28) + timedelta(days=4)).replace(day=1)

    # ── DATA QUALITY ISSUE #2: Reversed transactions (150 pairs) ─────────────
    # A REVERSAL follows within 1-23 hours of a PURCHASE: same amount, merchant, account
    # Candidate must identify: any account with PURCHASE + REVERSAL same merchant+amount within 24h
    base_rows = list(rows)
    reversal_targets = random.sample(base_rows, 150)
    for t in reversal_targets:
        purchase_dt = datetime.strptime(t['transaction_date'], '%Y-%m-%d')
        rev_dt      = purchase_dt + timedelta(hours=random.randint(1,23))
        if rev_dt > END: rev_dt = purchase_dt
        rows.append({
            'transaction_id':   f'TXN{txn_id:07d}',
            'account_id':       t['account_id'],
            'transaction_date': rev_dt.strftime('%Y-%m-%d'),
            'amount_usd':       t['amount_usd'],
            'merchant_id':      t['merchant_id'],
            'merchant_category':t['merchant_category'],
            'card_product':     t['card_product'],
            'transaction_type': 'REVERSAL',
            'status':           'SETTLED',
        })
        txn_id += 1

    # ── DATA QUALITY ISSUE #3: Multi-swipe transactions (60 sets of 3) ───────
    # Same account, same merchant, same amount within 2 hours — vendor charged 3x
    # First transaction is legitimate; 2nd and 3rd are multi-swipes
    ms_targets = random.sample(base_rows, 60)
    for t in ms_targets:
        purchase_dt = datetime.strptime(t['transaction_date'], '%Y-%m-%d')
        for k in range(2):
            ms_dt = purchase_dt + timedelta(minutes=random.randint(5, 110))
            if ms_dt > END: ms_dt = purchase_dt
            rows.append({
                'transaction_id':   f'TXN{txn_id:07d}',
                'account_id':       t['account_id'],
                'transaction_date': ms_dt.strftime('%Y-%m-%d'),
                'amount_usd':       t['amount_usd'],
                'merchant_id':      t['merchant_id'],
                'merchant_category':t['merchant_category'],
                'card_product':     t['card_product'],
                'transaction_type': 'PURCHASE',
                'status':           'SETTLED',
            })
            txn_id += 1

    # ── DATA QUALITY ISSUE #4: Velocity burst transactions (20 fraud accounts) ─
    # 10-15 transactions in a 1-hour window on a single day
    burst_date = datetime(2026, 5, 15)
    for faid in fraud_pool:
        acct_row = clean_accts[clean_accts['account_id']==faid]
        if acct_row.empty: continue
        prod = acct_row.iloc[0]['card_product']
        cat  = random.choice(MERCHANT_CATEGORIES)
        mids = merch_by_cat[cat]
        burst_hour = random.randint(9, 20)
        n_burst = random.randint(10, 16)
        for b in range(n_burst):
            bt = burst_date.replace(hour=burst_hour, minute=random.randint(0,59))
            amt = round(random.uniform(50, 500), 2)
            rows.append({
                'transaction_id':   f'TXN{txn_id:07d}',
                'account_id':       faid,
                'transaction_date': bt.strftime('%Y-%m-%d'),
                'amount_usd':       amt,
                'merchant_id':      random.choice(mids),
                'merchant_category':cat,
                'card_product':     prod,
                'transaction_type': 'PURCHASE',
                'status':           'SETTLED',
            })
            txn_id += 1

    df = pd.DataFrame(rows)

    # ── DATA QUALITY ISSUE #5: 300 NULL merchant_category values ─────────────
    null_idx = df.sample(300, random_state=7).index
    df.loc[null_idx, 'merchant_category'] = None

    # ── DATA QUALITY ISSUE #6: 80 transactions with wrong date format ────────
    # MM/DD/YYYY instead of YYYY-MM-DD — candidate must standardize before analysis
    fmt_idx = df.sample(80, random_state=11).index
    df.loc[fmt_idx, 'transaction_date'] = df.loc[fmt_idx, 'transaction_date'].apply(
        lambda d: datetime.strptime(d, '%Y-%m-%d').strftime('%m/%d/%Y') if pd.notna(d) else d
    )

    # ── DATA QUALITY ISSUE #7: 25 negative amount transactions (credits) ─────
    # These are legitimate credits but must be handled — not counted as spend
    neg_idx = df.sample(25, random_state=23).index
    df.loc[neg_idx, 'amount_usd'] = df.loc[neg_idx, 'amount_usd'] * -1
    df.loc[neg_idx, 'transaction_type'] = 'CREDIT'

    return df.reset_index(drop=True)


# ── 5. A/B Test ───────────────────────────────────────────────────────────────

def gen_ab_test(accounts_df, transactions_df):
    """
    Proper A/B test: Q1 2026 In-Person outreach campaign.
    100 Treatment accounts (received visit) vs 100 Control accounts (no outreach).
    Groups matched on RFM tier and industry to reduce confounding.
    Primary metric: 30-day spend lift.
    Built-in: In-Person drives ~26% lift. Control group: ~3% natural drift.
    Pre-period imbalance on 15 treatment accounts (candidates should catch this).
    """
    clean_accts = accounts_df.drop_duplicates('account_id')
    txns = transactions_df.copy()

    # Standardize dates — use only cleanly formatted dates for this calculation
    def safe_date(d):
        for fmt in ['%Y-%m-%d','%m/%d/%Y']:
            try: return datetime.strptime(str(d), fmt)
            except: pass
        return None

    txns['dt'] = txns['transaction_date'].apply(safe_date)
    txns = txns[txns['dt'].notna()].copy()
    txns = txns[txns['amount_usd'] > 0].copy()  # exclude credits

    # Compute 90-day pre-period spend per account (Oct–Dec 2025) for matching
    pre_start = datetime(2025, 10, 1)
    pre_end   = datetime(2025, 12, 31)
    pre = txns[(txns['dt'] >= pre_start) & (txns['dt'] <= pre_end)]
    pre_spend = pre.groupby('account_id')['amount_usd'].sum().reset_index()
    pre_spend.columns = ['account_id','pre90_spend']

    eligible = clean_accts.merge(pre_spend, on='account_id', how='left')
    eligible['pre90_spend'] = eligible['pre90_spend'].fillna(0)
    eligible = eligible[eligible['pre90_spend'] > 500]   # must be active

    # Sample treatment (100) and control (100)
    eligible_sorted = eligible.sort_values('pre90_spend')
    n = min(200, len(eligible_sorted))
    pool = eligible_sorted.sample(n, random_state=55).reset_index(drop=True)
    pool['group'] = ['Treatment' if i < n//2 else 'Control' for i in range(n)]

    # Compute 30-day before/after for campaign window Jan 15, 2026
    rows = []
    for i, (_, acct) in enumerate(pool.iterrows()):
        aid       = acct['account_id']
        group     = acct['group']
        out_date  = datetime(2026, 1, 15) + timedelta(days=random.randint(0, 59))

        before_mask = (txns['account_id']==aid) & \
                      (txns['dt'] >= out_date - timedelta(days=30)) & \
                      (txns['dt'] < out_date)
        after_mask  = (txns['account_id']==aid) & \
                      (txns['dt'] >= out_date) & \
                      (txns['dt'] < out_date + timedelta(days=30))

        spend_before = float(txns[before_mask]['amount_usd'].sum())
        spend_after_base = float(txns[after_mask]['amount_usd'].sum())

        if group == 'Treatment':
            lift = 0.26 + float(np.random.normal(0, 0.06))
            spend_after = round(max(spend_after_base, spend_before) * (1 + lift), 2)
            converted   = 1 if random.random() < 0.44 else 0
        else:
            # Control: organic drift ~3%
            drift = 0.03 + float(np.random.normal(0, 0.04))
            spend_after = round(spend_after_base * (1 + drift), 2)
            converted   = 1 if random.random() < 0.10 else 0

        lift_usd = round(spend_after - spend_before, 2)
        lift_pct = round((lift_usd / spend_before * 100) if spend_before > 0 else 0.0, 1)

        rows.append({
            'campaign_id':           f'AB{i+1:04d}',
            'account_id':            aid,
            'industry':              acct['industry'],
            'business_size':         acct['business_size'],
            'rep_id':                acct['rep_id'],
            'group':                 group,
            'outreach_date':         out_date.strftime('%Y-%m-%d'),
            'converted':             converted,
            'pre90_spend_usd':       round(acct['pre90_spend'], 2),
            'spend_30d_before_usd':  round(spend_before, 2),
            'spend_30d_after_usd':   spend_after,
            'spend_lift_usd':        lift_usd,
            'spend_lift_pct':        lift_pct,
        })

    # ── DATA QUALITY ISSUE #8: 15 treatment accounts have pre-period imbalance ─
    # Their pre90_spend is 40% higher than matched controls → inflates lift estimate
    # Candidate should check for pre-period balance before trusting results
    treatment_rows = [r for r in rows if r['group']=='Treatment']
    for r in random.sample(treatment_rows, 15):
        r['pre90_spend_usd'] = round(r['pre90_spend_usd'] * 1.40, 2)
        r['spend_30d_before_usd'] = round(r['spend_30d_before_usd'] * 1.40, 2)

    return pd.DataFrame(rows)


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print("Generating Capital One BCP Hard Mock Datasets...\n")

    reps_df = gen_reps()
    reps_df.to_csv(os.path.join(OUT, 'field_reps.csv'), index=False)
    print(f"  field_reps.csv   : {len(reps_df):>6,} rows")

    merch_df = gen_merchants()
    merch_df.to_csv(os.path.join(OUT, 'merchants.csv'), index=False)
    print(f"  merchants.csv    : {len(merch_df):>6,} rows")

    accts_df = gen_accounts(reps_df)
    accts_df.to_csv(os.path.join(OUT, 'accounts.csv'), index=False)
    print(f"  accounts.csv     : {len(accts_df):>6,} rows  (includes 8 duplicate rows — find them)")

    txns_df = gen_transactions(accts_df, merch_df)
    txns_df.to_csv(os.path.join(OUT, 'transactions.csv'), index=False)
    print(f"  transactions.csv : {len(txns_df):>6,} rows  (reversals, multi-swipes, velocity bursts, NULLs, bad dates, credits embedded)")

    ab_df = gen_ab_test(accts_df, txns_df)
    ab_df.to_csv(os.path.join(OUT, 'ab_test.csv'), index=False)
    print(f"  ab_test.csv      : {len(ab_df):>6,} rows  (100 Treatment / 100 Control — pre-period imbalance on 15 rows)")

    print("\nDone. Open README.md for the full project brief, 8 questions, and grading rubric.")
    print("\nData quality issues embedded (find ALL of them before any analysis):")
    print("  1. Duplicate account_id entries in accounts.csv")
    print("  2. Reversed transactions (PURCHASE + REVERSAL same merchant/amount within 24h)")
    print("  3. Multi-swipe transactions (same account/merchant/amount within 2 hours, 3x)")
    print("  4. Velocity burst transactions (10+ transactions in 1 hour, 20 accounts)")
    print("  5. NULL merchant_category (300 rows)")
    print("  6. Wrong date format — MM/DD/YYYY mixed with YYYY-MM-DD (80 rows)")
    print("  7. Negative amount_usd transactions (credits, 25 rows)")
    print("  8. Pre-period spend imbalance in A/B test treatment group (15 accounts)")
