# cleaning functions for sales, buyer, and vendor datasets

import numpy as np
import pandas as pd
from zoneinfo import ZoneInfoNotFoundError

from config import (
    BOOLEAN_MAP,
    EPOCH_ZERO_SENTINEL,
    MAX_PLAUSIBLE_QUANTITY,
    ORDER_STATUS_CORRECTIONS,
    PCT_MARGIN_FILES,
)


def normalize_boolean(series):
    # vendor files use True/False, true/false, 1/0, and Y -- normalize all to real bool
    return series.str.strip().str.lower().map(BOOLEAN_MAP)


def _build_state_lookup(buyers_raw):
    # build state -> region and state -> timezone from rows that have all 3 filled
    # doing this empirically instead of a hardcoded census table because the company
    # has a non-standard "Other" region bucket that wouldn't match any standard mapping
    ref = buyers_raw.copy()
    ref["state"] = ref["state"].str.strip()
    ref["region"] = ref["region"].str.strip()
    ref["timezone"] = ref["timezone"].str.strip()

    ref_rows = ref[
        ref["state"].notna() & (ref["state"] != "") &
        ref["region"].notna() & (ref["region"] != "") &
        ref["timezone"].notna() & (ref["timezone"] != "")
    ]

    state_to_region = (
        ref_rows.groupby("state")["region"]
        .agg(lambda x: x.mode().iloc[0])
        .to_dict()
    )
    state_to_timezone = (
        ref_rows.groupby("state")["timezone"]
        .agg(lambda x: x.mode().iloc[0])
        .to_dict()
    )
    return state_to_region, state_to_timezone


def _parse_order_datetime(series):
    """
    order_datetime has three formats mixed in one column:
      1. m/d/yy H:MM  -- standard timestamp, has real time
      2. d-Mon-yy     -- date only, no time, hour=0 is meaningless on these
      3. 10-digit unix epoch -- ~800 rows, found late in profiling

    '1/1/70 0:00' appears ~190 times -- unix epoch zero, not real 1970 orders.
    null those out before parsing or they corrupt the date range.
    """
    raw = series.str.strip()
    raw = raw.where(raw != EPOCH_ZERO_SENTINEL, other=np.nan)

    has_time = pd.Series(True, index=series.index)
    parsed = pd.Series(pd.NaT, index=series.index, dtype="datetime64[ns]")

    # unix epoch integers -- exactly 10 digits
    epoch_mask = raw.str.match(r"^\d{10}$", na=False)
    if epoch_mask.any():
        parsed[epoch_mask] = pd.to_datetime(
            raw[epoch_mask].astype(float), unit="s"
        ).values

    # date-only rows like "15-Mar-24"
    dateonly_mask = raw.str.match(r"^\d{1,2}-[A-Za-z]{3}-\d{2}$", na=False)
    if dateonly_mask.any():
        parsed[dateonly_mask] = pd.to_datetime(
            raw[dateonly_mask], format="%d-%b-%y", errors="coerce"
        )
        has_time[dateonly_mask] = False

    # everything left -- standard m/d/yy H:MM format
    remainder = ~epoch_mask & ~dateonly_mask & raw.notna()
    if remainder.any():
        parsed[remainder] = pd.to_datetime(
            raw[remainder], format="%m/%d/%y %H:%M", errors="coerce"
        )

    return parsed, has_time


def clean_sales(df):
    out = df.copy()

    # strip whitespace first -- must happen before dedup or dupes won't match
    out["buyer_id"] = out["buyer_id"].str.strip()

    before = len(out)
    out = out.drop_duplicates()
    print(f"  [sales] dropped {before - len(out):,} exact duplicate rows")

    out["order_status"] = out["order_status"].str.strip().replace(ORDER_STATUS_CORRECTIONS)

    out["order_datetime"], out["datetime_has_time"] = _parse_order_datetime(out["order_datetime"])

    qty = pd.to_numeric(out["quantity"], errors="coerce")
    out["quantity_is_valid"] = qty.notna() & (qty <= MAX_PLAUSIBLE_QUANTITY)
    print(f"  [sales] {(~out['quantity_is_valid']).sum():,} rows flagged quantity_is_valid=False "
          f"(null or > {MAX_PLAUSIBLE_QUANTITY})")
    out["quantity"] = qty.where(out["quantity_is_valid"], other=np.nan)

    missing_buyer = out["buyer_id"].isna() | (out["buyer_id"] == "")
    print(f"  [sales] dropped {missing_buyer.sum():,} rows with null buyer_id")
    out = out[~missing_buyer].reset_index(drop=True)

    return out


def clean_buyers(df):
    out = df.copy()

    out["buyer_id"] = out["buyer_id"].str.strip()

    null_buyer = out["buyer_id"].isna() | (out["buyer_id"] == "")
    print(f"  [buyers] dropped {null_buyer.sum():,} rows with null buyer_id")
    out = out[~null_buyer]

    before = len(out)
    out = out.drop_duplicates()
    print(f"  [buyers] dropped {before - len(out):,} exact duplicate rows")

    before = len(out)
    out = out.drop_duplicates(subset="buyer_id", keep="first")
    print(f"  [buyers] deduped to one row per buyer_id ({before - len(out):,} additional rows removed)")

    out["signup_date"] = pd.to_datetime(out["signup_date"], format="mixed", errors="coerce")
    out["is_referred"] = normalize_boolean(out["is_referred"])
    out["wishlist_size"] = pd.to_numeric(out["wishlist_size"], errors="coerce")

    # impute region and timezone from state
    # pass the original df so lookup is built from all rows before dedup
    state_to_region, state_to_timezone = _build_state_lookup(df)
    state_col = out["state"].str.strip()

    no_region = out["region"].isna() | (out["region"].str.strip() == "")
    no_tz = out["timezone"].isna() | (out["timezone"].str.strip() == "")

    out.loc[no_region, "region"] = state_col[no_region].map(state_to_region)
    out.loc[no_tz, "timezone"] = state_col[no_tz].map(state_to_timezone)

    print(f"  [buyers] null region after imputation:   {out['region'].isna().sum():,}")
    print(f"  [buyers] null timezone after imputation: {out['timezone'].isna().sum():,}")

    return out.reset_index(drop=True)


def clean_vendors(df):
    """
    Biggest issue: NKDLI.csv stores category_id, subcategory_id, vendor,
    product_num all in lowercase. A case-sensitive join on sku_id silently
    drops 46 SKUs. Fix = uppercase all 4 key cols before building sku_id.

    Other issues:
    - ROPIK and JDTOJ store profit_margin as 0-100, rest use 0-1 fraction
    - ROPIK has '$7.9' in the price column -- strip currency symbol
    - boolean cols have 4 different spellings across files
    - some negative margins exist -- real loss-leaders, not errors, flag them
    """
    out = df.copy()

    # uppercase key cols first -- fixes the NKDLI silent join failure
    for col in ["category_id", "subcategory_id", "vendor", "product_num"]:
        out[col] = out[col].str.strip().str.upper()

    out["sku_id"] = out["subcategory_id"] + "-" + out["vendor"] + "-" + out["product_num"]

    is_pct = out["_source_file"].isin(PCT_MARGIN_FILES)
    pct_col = pd.to_numeric(out.get("pct_profit_margin", np.nan), errors="coerce")
    fraction_col = pd.to_numeric(out.get("profit_margin", np.nan), errors="coerce")
    out["profit_margin"] = np.where(is_pct, pct_col / 100.0, fraction_col)

    if "pct_profit_margin" in out.columns:
        out = out.drop(columns=["pct_profit_margin"])

    # ROPIK has currency symbol in price -- strip and convert
    out["price"] = (
        out["price"]
        .str.replace(r"[^\d.]", "", regex=True)
        .pipe(pd.to_numeric, errors="coerce")
    )

    out["active_product"] = normalize_boolean(out["active_product"])
    out["currently_active_vendor"] = normalize_boolean(out["currently_active_vendor"])

    # flag negatives but keep them -- loss-leader products are real business decisions
    out["profit_margin_is_neg"] = out["profit_margin"].fillna(0) < 0
    neg_count = out["profit_margin_is_neg"].sum()
    if neg_count > 0:
        files = out.loc[out["profit_margin_is_neg"], "_source_file"].unique()
        print(f"  [vendors] {neg_count:,} negative margin rows "
              f"(loss-leaders) in: {', '.join(sorted(files))}")

    return out.reset_index(drop=True)


def verify_sku_match_rate(sales, vendors, label=""):
    # run before and after clean_vendors to prove the NKDLI fix worked
    sales_skus = set(sales["sku_id"].dropna().unique())
    vendor_skus = set(vendors["sku_id"].dropna().unique())
    matched = sales_skus & vendor_skus
    rate = len(matched) / len(sales_skus) if sales_skus else 0.0
    tag = f" [{label}]" if label else ""
    print(f"  [sku_match{tag}] {len(matched):,} / {len(sales_skus):,} sales SKUs matched ({rate:.1%})")
    return rate
