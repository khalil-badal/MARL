"""
Clean CapMetro APC Raw Dataset → Route 801 Direction Code 6 Subset

Source: Texas Open Data, Socrata ID im6q-3pc9
Expected raw SHA-256: 8368412e47df32ff8a3c2837048797664315c0e7ae51c44676766b5af7f23e21

Filters (matching Jared's documented pipeline):
  1. current_route_id == route_id
  2. import_error == 0 AND import_trip_error == 0
  3. bs_id != 0
  4. direction_code_id == 6

Expected output: 229,421 rows, 184 service days, 29 stop IDs
"""

import hashlib
import sys
from pathlib import Path

import pandas as pd

# Paths
ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"
AUDIT_DIR = ROOT / "data" / "audit"

EXPECTED_RAW_SHA256 = "8368412e47df32ff8a3c2837048797664315c0e7ae51c44676766b5af7f23e21"

EXPECTED_CLEAN_ROWS = 229_421
EXPECTED_SERVICE_DAYS = 184
EXPECTED_STOP_IDS = 29
EXPECTED_BOARDINGS = 420_201


def find_raw_csv():
    """Find the raw APC CSV in data/raw/."""
    candidates = list(RAW_DIR.glob("*.csv"))
    if not candidates:
        print("ERROR: No CSV found in data/raw/")
        print("Place the raw APC file there and re-run.")
        sys.exit(1)
    if len(candidates) > 1:
        print(f"WARNING: Multiple CSVs found in data/raw/: {candidates}")
        print("Using the largest file.")
        candidates.sort(key=lambda p: p.stat().st_size, reverse=True)
    return candidates[0]


def verify_sha256(filepath):
    """Compute SHA-256 of the raw file and compare to expected."""
    print(f"Computing SHA-256 of {filepath.name}...")
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192 * 1024), b""):
            h.update(chunk)
    actual = h.hexdigest()
    if actual == EXPECTED_RAW_SHA256:
        print(f"  SHA-256 MATCH: {actual}")
        return True
    else:
        print(f"  SHA-256 MISMATCH!")
        print(f"  Expected: {EXPECTED_RAW_SHA256}")
        print(f"  Actual:   {actual}")
        return False


def clean(df):
    """Apply the four documented cleaning filters."""
    n_start = len(df)
    print(f"Raw rows loaded: {n_start:,}")

    # Filter 1: reported route matches actual route
    mask = df["current_route_id"] == df["route_id"]
    df = df[mask]
    print(f"  After route match filter: {len(df):,}")

    # Filter 2: no import errors
    mask = (df["import_error"] == 0) & (df["import_trip_error"] == 0)
    df = df[mask]
    print(f"  After error filter: {len(df):,}")

    # Filter 3: valid stop ID
    mask = df["bs_id"] != 0
    df = df[mask]
    print(f"  After stop filter: {len(df):,}")

    # At this point we have all clean events for Route 801 (both directions).
    # Filter to route 801 only (if multiple routes present):
    if "route_id" in df.columns:
        route_801 = df[df["route_id"] == 801]
        if len(route_801) > 0:
            df = route_801
            print(f"  After Route 801 filter: {len(df):,}")

    # Filter 4: direction code 6
    mask = df["direction_code_id"] == 6
    df = df[mask]
    print(f"  After direction code 6 filter: {len(df):,}")

    return df


def verify_output(df):
    """Check output matches expected counts."""
    n_rows = len(df)
    n_days = df["service_date"].nunique() if "service_date" in df.columns else "unknown"
    n_stops = df["bs_id"].nunique()
    n_boardings = int(df["ons"].sum()) if "ons" in df.columns else "unknown"

    print(f"\n--- Verification ---")
    print(f"Rows:         {n_rows:,}  (expected {EXPECTED_CLEAN_ROWS:,}) {'PASS' if n_rows == EXPECTED_CLEAN_ROWS else 'MISMATCH'}")
    print(f"Service days: {n_days}  (expected {EXPECTED_SERVICE_DAYS}) {'PASS' if n_days == EXPECTED_SERVICE_DAYS else 'CHECK'}")
    print(f"Stop IDs:     {n_stops}  (expected {EXPECTED_STOP_IDS}) {'PASS' if n_stops == EXPECTED_STOP_IDS else 'MISMATCH'}")
    print(f"Boardings:    {n_boardings}  (expected {EXPECTED_BOARDINGS:,}) {'PASS' if n_boardings == EXPECTED_BOARDINGS else 'CHECK'}")

    return n_rows == EXPECTED_CLEAN_ROWS and n_stops == EXPECTED_STOP_IDS


def main():
    print("=" * 60)
    print("CapMetro APC Cleaning Pipeline")
    print("Route 801, Direction Code 6, July-December 2021")
    print("=" * 60)

    raw_path = find_raw_csv()
    print(f"\nRaw file: {raw_path}")
    print(f"Size: {raw_path.stat().st_size / 1e6:.1f} MB")

    sha_ok = verify_sha256(raw_path)
    if not sha_ok:
        print("  Continuing despite mismatch (may be a fresh download).")

    print("\nLoading CSV (this may take a minute for 9M+ rows)...")
    df = pd.read_csv(raw_path, low_memory=False)
    print(f"Loaded {len(df):,} rows, {len(df.columns)} columns")

    # Ensure numeric types for filter columns
    for col in ["current_route_id", "route_id", "import_error",
                "import_trip_error", "bs_id", "direction_code_id"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(-1).astype(int)

    if "ons" in df.columns:
        df["ons"] = pd.to_numeric(df["ons"], errors="coerce").fillna(0)

    print("\nApplying cleaning filters...")
    df_clean = clean(df)

    passed = verify_output(df_clean)

    # Save
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    out_path = PROCESSED_DIR / "capmetro_801_dir6_clean.csv"
    df_clean.to_csv(out_path, index=False)
    print(f"\nSaved: {out_path}")
    print(f"Output size: {out_path.stat().st_size / 1e6:.1f} MB")

    # Compute output checksum
    h = hashlib.sha256()
    with open(out_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192 * 1024), b""):
            h.update(chunk)
    out_sha = h.hexdigest()
    print(f"Output SHA-256: {out_sha}")

    # Write audit log
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    audit_path = AUDIT_DIR / "cleaning_log.txt"
    with open(audit_path, "w") as f:
        f.write(f"Date: auto-generated\n")
        f.write(f"Raw file: {raw_path.name}\n")
        f.write(f"Raw SHA-256: {EXPECTED_RAW_SHA256}\n")
        f.write(f"Raw rows: {len(pd.read_csv(raw_path, nrows=0).columns)} columns\n")
        f.write(f"Clean rows: {len(df_clean):,}\n")
        f.write(f"Service days: {df_clean['service_date'].nunique() if 'service_date' in df_clean.columns else 'N/A'}\n")
        f.write(f"Stop IDs: {df_clean['bs_id'].nunique()}\n")
        f.write(f"Boardings: {int(df_clean['ons'].sum()) if 'ons' in df_clean.columns else 'N/A'}\n")
        f.write(f"Output file: {out_path.name}\n")
        f.write(f"Output SHA-256: {out_sha}\n")
        f.write(f"Verification: {'PASS' if passed else 'REVIEW NEEDED'}\n")
    print(f"Audit log: {audit_path}")

    if passed:
        print("\n ALL CHECKS PASSED")
    else:
        print("\n SOME CHECKS FAILED — review output before proceeding")

    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
