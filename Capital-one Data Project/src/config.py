import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

PROJECT_ROOT = Path(__file__).parent.parent
RAW_DIR = PROJECT_ROOT / "Data" / "Raw"
PROCESSED_DIR = PROJECT_ROOT / "Data" / "Processed"
FIGURES_DIR = PROJECT_ROOT / "outputs" / "figures"

# Timestamps have no timezone label in the raw data; treated as buyer's local time
# (buyer.timezone), then converted to Central for Q1 staffing analysis.
COMPANY_TZ = ZoneInfo("America/Chicago")  # St. Louis HQ = Central
FALLBACK_TZ = COMPANY_TZ  # default when buyer timezone is null or unrecognized

# sales cleaning
MAX_PLAUSIBLE_QUANTITY = 50  # max observed in real data was 327,783,095 -- clearly corrupted
EPOCH_ZERO_SENTINEL = "1/1/70 0:00"  # unix epoch zero, ~190 rows, null these out
ORDER_STATUS_CORRECTIONS = {"Deliverred": "Delivered"}  # typo, 3714 rows of it

# only Delivered orders count for revenue/profit
# all statuses count for volume -- staffing has to handle everything
REVENUE_STATUSES = frozenset({"Delivered"})

# 10% off first order for referred buyers
REFERRAL_DISCOUNT_RATE = 0.10

# Black Friday: 20% off all items purchased that day (based on customer's local timezone).
# Raw price data does NOT include this discount — it must be applied in code.
BLACK_FRIDAY_DISCOUNT_RATE = 0.20

# Black Friday eligibility based on customer's LOCAL timezone, not the company timezone
BLACK_FRIDAY_DATES = frozenset({
    datetime.date(2024, 11, 29),
    datetime.date(2025, 11, 28),
})

# Customer-paid shipping tiers (per delivered order, based on post-discount product subtotal)
SHIPPING_TIER_LOW  = 7.99   # order product total < $50
SHIPPING_TIER_MID  = 4.99   # $50 ≤ order product total < $100
SHIPPING_TIER_FREE = 0.00   # order product total ≥ $100

# Flat fee the company pays the carrier per delivered order (regardless of size or weight)
CARRIER_COST_PER_ORDER = 4.99

# customer_group = internal segmentation (VIP/Frequent/Regular/Occasional/Dormant)
# NOT customer_segment which is behavioral (e.g. "Bargain Hunter")
SEGMENT_COL = "customer_group"
SEGMENT_ORDER = ["VIP", "Frequent", "Regular", "Occasional", "Dormant"]

VENDOR_FILES = [
    "CPSFP.csv", "EYMKE.csv", "JDTOJ.csv", "JSCZL.csv", "KWOXE.csv",
    "PQYYY.csv", "ROPIK.csv", "SOPAJ.csv", "TAAFL.csv", "WQEPS.csv",
    "NKDLI.csv",
]

# ROPIK and JDTOJ use 0-100 scale for profit margin, all others use 0-1
PCT_MARGIN_FILES = frozenset({"ROPIK.csv", "JDTOJ.csv"})

# NKDLI has all key cols in lowercase -- causes 46 SKUs to silently drop from join
LOWERCASE_KEY_FILES = frozenset({"NKDLI.csv"})

# boolean values found across all 11 vendor files
BOOLEAN_MAP = {
    "true": True,
    "false": False,
    "1": True,
    "0": False,
    "y": True,
    "n": False,
}
