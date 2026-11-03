import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

BANNED_PHRASES = [
    "confirmed in brief",
    "confirmed in the brief",
    "Problem brief",
]

_SKIP_DIRS = {".git", "tests"}


def _project_files():
    for ext in ("*.py", "*.md", "*.ipynb"):
        for path in PROJECT_ROOT.rglob(ext):
            if not any(part in _SKIP_DIRS for part in path.parts):
                yield path


def test_no_fabricated_sourcing_claims():
    violations = []
    for path in _project_files():
        text = path.read_text(errors="ignore")
        for phrase in BANNED_PHRASES:
            if phrase in text:
                violations.append(f"{path.relative_to(PROJECT_ROOT)}: '{phrase}'")

    assert not violations, "Unverified sourcing claims found:\n" + "\n".join(violations)


def test_readme_mentions_current_referral_cost():
    from load import load_sales, load_buyers, load_vendor_files
    from clean import clean_sales, clean_buyers, clean_vendors
    from features import build_line_items, build_orders, estimate_referral_cost

    sales = clean_sales(load_sales())
    buyers = clean_buyers(load_buyers())
    vendors = clean_vendors(load_vendor_files())
    orders = build_orders(build_line_items(sales, vendors, buyers))

    _, cost = estimate_referral_cost(orders)
    readme = (PROJECT_ROOT / "README.md").read_text()

    assert f"{cost:,.2f}" in readme, \
        f"README referral cost is stale — pipeline says ${cost:,.2f}, update the Data Gap section"
