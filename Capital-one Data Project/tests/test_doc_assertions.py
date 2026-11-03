import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

_SKIP_DIRS = {".git", "tests"}
REMOVED_COLUMNS = ["shipping_cost", "net_shipping"]


def _readme():
    return (PROJECT_ROOT / "README.md").read_text()


def _project_files():
    for ext in ("*.py", "*.md", "*.ipynb"):
        for path in PROJECT_ROOT.rglob(ext):
            if not any(part in _SKIP_DIRS for part in path.parts):
                yield path


def test_readme_mentions_actual_referral_rate():
    from config import REFERRAL_DISCOUNT_RATE
    rate_str = f"{int(round(REFERRAL_DISCOUNT_RATE * 100))}%"
    assert rate_str in _readme(), f"README doesn't mention referral rate ({rate_str}) — update Assumption A4"


def test_readme_mentions_referral_caveat():
    readme = _readme()
    # keeps the estimate from being read as confirmed fact
    assert "confirm with business" in readme.lower(), \
        "README lost the 'confirm with business' caveat on the referral cost estimate"


def test_no_shipping_columns_in_project_files():
    # these were removed because they were fabricated, make sure they stay gone
    hits = []
    for path in _project_files():
        text = path.read_text(errors="ignore")
        for col in REMOVED_COLUMNS:
            if col in text:
                hits.append(f"{path.relative_to(PROJECT_ROOT)}: '{col}'")

    assert not hits, "Removed shipping columns found:\n" + "\n".join(hits)


def test_referral_rate_is_sourced_in_config():
    # ASSUMPTION_NOTES was replaced by inline source comments once the rate was confirmed
    config_text = (PROJECT_ROOT / "src" / "config.py").read_text()
    assert "REFERRAL_DISCOUNT_RATE" in config_text, "REFERRAL_DISCOUNT_RATE missing from config"
