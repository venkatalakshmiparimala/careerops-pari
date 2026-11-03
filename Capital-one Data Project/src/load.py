import pandas as pd
from config import RAW_DIR, VENDOR_FILES


def load_sales():
    return pd.read_csv(RAW_DIR / "sales.csv", dtype=str, low_memory=False)


def load_buyers():
    return pd.read_csv(RAW_DIR / "buyer.csv", dtype=str, low_memory=False)


def load_vendor_files():
    # stacking all 11 vendor files into one df
    # _source_file tracks which file each row came from -- critical for debugging
    frames = []
    for filename in VENDOR_FILES:
        df = pd.read_csv(RAW_DIR / filename, dtype=str, low_memory=False)
        df["_source_file"] = filename
        frames.append(df)
    return pd.concat(frames, ignore_index=True)
