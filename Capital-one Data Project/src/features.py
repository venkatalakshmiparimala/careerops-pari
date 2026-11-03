# joins the 3 cleaned datasets and builds all derived columns
#
# two main outputs:
#   line_items -- one row per sales line item with product + buyer attributes
#   orders     -- aggregated to order grain (one row per order_id)

import pandas as pd
import numpy as np
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from config import (
    COMPANY_TZ,
    FALLBACK_TZ,
    REVENUE_STATUSES,
    BLACK_FRIDAY_DATES,
    BLACK_FRIDAY_DISCOUNT_RATE,
    REFERRAL_DISCOUNT_RATE,
    SHIPPING_TIER_LOW,
    SHIPPING_TIER_MID,
    SHIPPING_TIER_FREE,
    CARRIER_COST_PER_ORDER,
    SEGMENT_COL,
)


def _resolve_tz(tz_string):
    # convert a timezone string to ZoneInfo, fall back to Central if bad or null
    if not tz_string or not isinstance(tz_string, str):
        return FALLBACK_TZ
    try:
        return ZoneInfo(tz_string.strip())
    except (ZoneInfoNotFoundError, KeyError):
        return FALLBACK_TZ


def build_line_items(sales, vendors, buyers):
    line_items = sales.merge(
        vendors[[
            "sku_id", "price", "profit_margin", "profit_margin_is_neg",
            "category_name", "subcategory_name", "active_product",
            "currently_active_vendor"
        ]],
        on="sku_id",
        how="left",
    )

    buyer_cols = [
        "buyer_id", SEGMENT_COL, "customer_segment", "region", "state",
        "timezone", "is_referred", "is_active_buyer",
        "preferred_channel", "preferred_payment",
    ]
    buyer_cols = list(dict.fromkeys(buyer_cols))
    buyer_cols = [c for c in buyer_cols if c in buyers.columns]
    line_items = line_items.merge(buyers[buyer_cols], on="buyer_id", how="left")

    line_items["unit_revenue"] = line_items["price"] * line_items["quantity"]
    line_items["is_revenue_eligible"] = line_items["order_status"].isin(REVENUE_STATUSES)

    # timezone conversion for staffing analysis (Q1)
    tz_series = line_items.get("timezone", pd.Series("", index=line_items.index))
    line_items["order_datetime_central"] = pd.NaT

    for tz_str in tz_series.unique():
        # NaN == NaN is always False in pandas -- must use isna() to match null-tz rows
        mask = tz_series.isna() if pd.isna(tz_str) else tz_series == tz_str
        buyer_tz = _resolve_tz(tz_str)

        time_mask = mask & line_items["datetime_has_time"]
        date_mask = mask & ~line_items["datetime_has_time"]

        if time_mask.any():
            converted = (
                line_items.loc[time_mask, "order_datetime"]
                .dt.tz_localize(buyer_tz, ambiguous="NaT", nonexistent="NaT")
                .dt.tz_convert(COMPANY_TZ)
                .dt.tz_localize(None)
            )
            line_items.loc[time_mask, "order_datetime_central"] = converted

        if date_mask.any():
            line_items.loc[date_mask, "order_datetime_central"] = (
                line_items.loc[date_mask, "order_datetime"]
            )

    # NaN for date-only rows -- hour=0 is meaningless on those
    line_items["order_hour_central"] = np.where(
        line_items["datetime_has_time"],
        line_items["order_datetime_central"].dt.hour,
        np.nan,
    )
    line_items["order_hour_central"] = pd.to_numeric(
        line_items["order_hour_central"], errors="coerce"
    )

    line_items["order_date"] = line_items["order_datetime"].dt.date

    dt_col = line_items["order_datetime_central"]
    valid = ~dt_col.isna()
    line_items["order_quarter"] = pd.Series(pd.NA, index=line_items.index, dtype="object")
    if valid.any():
        line_items.loc[valid, "order_quarter"] = (
            dt_col[valid].dt.year.astype(int).astype(str)
            + "-Q"
            + dt_col[valid].dt.quarter.astype(int).astype(str)
        )

    line_items["is_black_friday"] = line_items["order_date"].isin(BLACK_FRIDAY_DATES)

    # BF 20% discount applies to delivered BF orders; raw price data does not include it
    bf_eligible = line_items["is_black_friday"] & line_items["is_revenue_eligible"]
    bf_multiplier = np.where(bf_eligible, 1.0 - BLACK_FRIDAY_DISCOUNT_RATE, 1.0)

    line_items["unit_profit"] = (
        line_items["unit_revenue"] * bf_multiplier * line_items["profit_margin"]
    )

    # mask revenue/profit for ineligible orders; BF discount baked into eligible figures
    line_items["eligible_revenue"] = (
        line_items["unit_revenue"] * bf_multiplier
    ).where(line_items["is_revenue_eligible"])
    line_items["eligible_profit"] = line_items["unit_profit"].where(
        line_items["is_revenue_eligible"]
    )

    return line_items


def _shipping_charge(product_subtotal):
    """Customer-paid shipping tier based on post-discount product subtotal per order."""
    return np.where(
        product_subtotal < 50,
        SHIPPING_TIER_LOW,
        np.where(product_subtotal < 100, SHIPPING_TIER_MID, SHIPPING_TIER_FREE),
    )


def build_orders(line_items):
    agg_nums = (
        line_items
        .groupby("order_id", as_index=False)
        .agg(
            order_revenue=("eligible_revenue", "sum"),
            order_profit=("eligible_profit", "sum"),
            quantity=("quantity", "sum"),
            is_black_friday=("is_black_friday", "max"),
            is_revenue_eligible=("is_revenue_eligible", "max"),
            datetime_has_time=("datetime_has_time", "max"),
        )
    )

    keep_cols = [
        "order_id", "buyer_id", "order_datetime", "order_datetime_central",
        "order_status", "order_date", "order_hour_central", "order_quarter",
    ]
    optional_cols = [
        "customer_group", "customer_segment", "region", "state",
        "timezone", "is_referred", "is_active_buyer",
        "preferred_channel", "preferred_payment",
    ]
    keep_cols += [c for c in optional_cols if c in line_items.columns]

    order_attrs = (
        line_items[keep_cols]
        .drop_duplicates(subset="order_id", keep="first")
        .reset_index(drop=True)
    )

    orders = agg_nums.merge(order_attrs, on="order_id", how="left")

    for col in ("is_black_friday", "is_revenue_eligible", "datetime_has_time"):
        if col in orders.columns:
            orders[col] = orders[col].astype(bool)

    # Shipping economics (delivered orders only)
    # order_revenue at this point is the post-BF-discount product subtotal
    orders["shipping_revenue"] = np.where(
        orders["is_revenue_eligible"],
        _shipping_charge(orders["order_revenue"]),
        0.0,
    )
    orders["carrier_cost"] = np.where(
        orders["is_revenue_eligible"], CARRIER_COST_PER_ORDER, 0.0
    )
    orders["order_revenue"] = orders["order_revenue"] + orders["shipping_revenue"]
    orders["order_profit"] = (
        orders["order_profit"] + orders["shipping_revenue"] - orders["carrier_cost"]
    )

    return orders


def estimate_referral_cost(orders):
    if "is_referred" not in orders.columns:
        raise ValueError("orders df must have is_referred column")

    del_orders = orders[orders["is_revenue_eligible"]].copy()
    del_orders["is_ref"] = del_orders["is_referred"].fillna(False).infer_objects(copy=False).astype(bool)

    del_orders = del_orders.sort_values("order_datetime")
    del_orders["is_first_order"] = ~del_orders.duplicated(subset="buyer_id", keep="first")

    ref_first = del_orders[del_orders["is_ref"] & del_orders["is_first_order"]]
    discount_cost = (ref_first["order_revenue"] * REFERRAL_DISCOUNT_RATE).sum()

    summary = del_orders.groupby("is_ref").agg(
        total_orders=("order_id", "count"),
        total_revenue=("order_revenue", "sum"),
        unique_buyers=("buyer_id", "nunique"),
    ).reset_index()

    summary["avg_revenue_per_buyer"] = summary["total_revenue"] / summary["unique_buyers"]
    summary["avg_orders_per_buyer"] = summary["total_orders"] / summary["unique_buyers"]

    return summary, discount_cost
