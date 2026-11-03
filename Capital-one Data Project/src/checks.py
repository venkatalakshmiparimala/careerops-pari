# assert-based sanity checks for each pipeline stage

import pandas as pd


def _ok(msg):
    print(f"  ✓ {msg}")


def _assert(condition, msg, actual=None):
    if not condition:
        detail = f" (got: {actual})" if actual is not None else ""
        raise AssertionError(f"\n  ✗ CHECK FAILED: {msg}{detail}")
    _ok(msg)


def check_sales(df):
    print("[checks] sales")
    _assert(len(df) > 300_000, "row count > 300k after dedup", len(df))
    _assert(df["buyer_id"].isna().sum() == 0, "no null buyer_id rows remain")
    _assert(
        "Deliverred" not in df["order_status"].values,
        "order_status typo Deliverred fully corrected"
    )
    _assert(
        df["quantity_is_valid"].mean() > 0.998,
        "quantity_is_valid rate > 99.8%",
        f"{df['quantity_is_valid'].mean():.3%}"
    )
    _assert(df["order_datetime"].notna().sum() > 300_000, "parsed datetime coverage > 300k rows")


def check_buyers(df):
    print("[checks] buyers")
    _assert(len(df) > 40_000, "buyer row count > 40k after cleaning", len(df))
    _assert(df["buyer_id"].duplicated().sum() == 0, "one row per buyer_id")
    _assert(df["buyer_id"].isna().sum() == 0, "no null buyer_id rows remain")
    _assert(
        df["region"].isna().mean() < 0.05,
        "null region rate < 5% after imputation",
        f"{df['region'].isna().mean():.2%}"
    )
    _assert(
        df["timezone"].isna().mean() < 0.05,
        "null timezone rate < 5% after imputation",
        f"{df['timezone'].isna().mean():.2%}"
    )


def check_vendors(df):
    print("[checks] vendors")
    _assert(df["sku_id"].notna().all(), "all rows have a sku_id")
    _assert(df["sku_id"].duplicated().sum() == 0, "no duplicate sku_ids in vendor catalog")

    pm = df["profit_margin"].dropna()
    _assert(pm.max() < 1.5, "profit_margin max < 1.5 -- catches un-fixed 0-100 scale", pm.max())
    _assert(
        pm.between(-1, 1).all(),
        "all non-null margins in [-1, 1]",
        f"{(~pm.between(-1,1)).sum()} rows outside range"
    )
    _assert(len(df) >= 1_000, "vendor catalog has >= 1000 SKUs", len(df))


def check_sku_match(sales, vendors):
    print("[checks] sku match rate")
    sales_skus = set(sales["sku_id"].dropna().unique())
    vendor_skus = set(vendors["sku_id"].dropna().unique())
    matched = sales_skus & vendor_skus
    rate = len(matched) / len(sales_skus) if sales_skus else 0.0
    _assert(rate >= 0.999, "SKU match rate >= 99.9%", f"{rate:.1%}")


def check_line_items(df):
    print("[checks] line_items")
    _assert("eligible_revenue" in df.columns, "eligible_revenue column exists")
    _assert("eligible_profit" in df.columns, "eligible_profit column exists")
    _assert((df["eligible_revenue"].dropna() < 0).sum() == 0, "no negative eligible_revenue values")
    _assert("order_datetime_central" in df.columns, "timezone conversion produced order_datetime_central")

    central_coverage = df["order_datetime_central"].notna().mean()
    _assert(
        central_coverage > 0.90,
        "order_datetime_central coverage > 90%",
        f"{central_coverage:.1%}"
    )
    _assert("is_black_friday" in df.columns, "is_black_friday column exists")


def check_orders(df):
    print("[checks] orders")
    _assert(df["order_id"].duplicated().sum() == 0, "one row per order_id")

    bf_count = df["is_black_friday"].sum()
    _assert(bf_count > 500, "is_black_friday has > 500 True rows", bf_count)
    _assert(
        df["is_revenue_eligible"].sum() > 100_000,
        "at least 100k revenue-eligible orders",
        df["is_revenue_eligible"].sum()
    )
    _assert(
        df["customer_group"].isna().mean() < 0.30,
        "customer_group null rate < 30%",
        f"{df['customer_group'].isna().mean():.1%}"
    )
    _assert("shipping_revenue" in df.columns, "shipping_revenue column exists")
    _assert("carrier_cost" in df.columns, "carrier_cost column exists")
    _assert(
        (df.loc[df["is_revenue_eligible"], "shipping_revenue"] >= 0).all(),
        "all delivered orders have non-negative shipping_revenue"
    )
    _assert(
        (df.loc[~df["is_revenue_eligible"], "shipping_revenue"] == 0).all(),
        "non-delivered orders have zero shipping_revenue"
    )


def run_all_checks(sales, buyers, vendors, line_items, orders):
    print("\n=== running pipeline checks ===")
    check_sales(sales)
    check_buyers(buyers)
    check_vendors(vendors)
    check_sku_match(sales, vendors)
    check_line_items(line_items)
    check_orders(orders)
    print("=== all checks passed ===\n")
