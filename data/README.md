# Data Directory

Local workspace for the CapMetro APC dataset and derived outputs.
Raw and processed data are **not committed** to git (see `.gitignore`).

## Structure

```
data/
├── raw/            ← Unmodified source file from Jared
├── processed/      ← Cleaned subset (Route 801, direction code 6)
├── audit/          ← Checksums, filter logs, row-count verification
└── README.md       ← This file
```

## Source

- **Dataset:** APC Raw July 2021–December 2021
- **Portal:** Texas Open Data, Socrata ID `im6q-3pc9`
- **Publisher:** Capital Metropolitan Transportation Authority
- **Expected raw SHA-256:** `8368412e47df32ff8a3c2837048797664315c0e7ae51c44676766b5af7f23e21`

## Cleaning Rules

Applied by `scripts/clean_capmetro_apc.py`:

1. `current_route_id == route_id` (reported route matches actual)
2. `import_error == 0` AND `import_trip_error == 0`
3. `bs_id != 0` (valid stop ID)
4. `direction_code_id == 6`

## Expected Output (Route 801, direction code 6)

| Metric | Expected |
|--------|----------|
| Clean rows | 229,421 |
| Service-day codes | 184 |
| Distinct stop IDs | 29 |
| Recorded boardings | 420,201 |

## Reproduction

```bash
python scripts/clean_capmetro_apc.py
```

Verify output checksum and row counts match the values above.
