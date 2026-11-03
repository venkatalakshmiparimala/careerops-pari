import sys
sys.path.insert(0, 'src')

from load import load_sales, load_buyers, load_vendor_files
from clean import clean_sales, clean_buyers, clean_vendors, verify_sku_match_rate
from features import build_line_items, build_orders
from checks import run_all_checks

print("=== loading ===")
sales_raw = load_sales()
buyers_raw = load_buyers()
vendors_raw = load_vendor_files()

print("\n=== cleaning ===")
sales = clean_sales(sales_raw)
buyers = clean_buyers(buyers_raw)
vendors = clean_vendors(vendors_raw)

print("\n=== sku match rate ===")
verify_sku_match_rate(sales, vendors, label="post-clean")

print("\n=== shapes after cleaning ===")
print("sales:  ", sales.shape)
print("buyers: ", buyers.shape)
print("vendors:", vendors.shape)

print("\n=== building features ===")
line_items = build_line_items(sales, vendors, buyers)
orders = build_orders(line_items)

print("line_items:", line_items.shape)
print("orders:", orders.shape)
print("BF orders:", orders["is_black_friday"].sum())
print("revenue-eligible:", orders["is_revenue_eligible"].sum())
print()
print(orders[["order_id", "order_revenue", "order_profit",
              "is_black_friday", "is_revenue_eligible", "is_referred"]].head())

print("\n=== checks ===")
run_all_checks(sales, buyers, vendors, line_items, orders)
