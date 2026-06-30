# TASS Rule Catalog

# Category : Data Quality (DQ)

# Version : 1.0

**Status:** Frozen v1.0

**Machine-readable:** [rules/catalog/DQ_v1.0.yaml](../rules/catalog/DQ_v1.0.yaml)

---

## Category Information

| Field | Value |
|-------|-------|
| Category Code | DQ |
| Category Name | Data Quality |
| Status | Frozen v1.0 |
| Total Rules | 60 |
| Rule Range | DQ0001 – DQ0060 |

---

## Missing Data (DQ0001–DQ0010)

```text
DQ0001  Open Price Missing
DQ0002  High Price Missing
DQ0003  Low Price Missing
DQ0004  Close Price Missing
DQ0005  Volume Missing
DQ0006  OHLC All Missing
DQ0007  Consecutive Missing Bar
DQ0008  Leading History Gap
DQ0009  Internal History Gap
DQ0010  Latest Bar Missing
```

---

## Data Integrity (DQ0011–DQ0020)

```text
DQ0011  High Below Low
DQ0012  Close Outside High Low Range
DQ0013  Open Outside High Low Range
DQ0014  Negative Price Present
DQ0015  Zero Price Present
DQ0016  Negative Volume Present
DQ0017  Duplicate Timestamp
DQ0018  Identical OHLC Values
DQ0019  Timestamp Out of Sequence
DQ0020  Price Adjustment Mismatch
```

---

## Corporate Actions (DQ0021–DQ0030)

```text
DQ0021  Stock Split Present
DQ0022  Reverse Split Present
DQ0023  Dividend Present
DQ0024  Rights Issue Present
DQ0025  Merger Present
DQ0026  Spinoff Present
DQ0027  Symbol Change Present
DQ0028  Delisting Event Present
DQ0029  Price Adjustment Applied
DQ0030  Price Unadjusted
```

---

## Liquidity & Trading Status (DQ0031–DQ0040)

```text
DQ0031  Trading Halted
DQ0032  Trading Suspended
DQ0033  Delisted Instrument
DQ0034  No Trade Session
DQ0035  Zero Volume Session
DQ0036  Low Volume Session
DQ0037  Low Liquidity Session
DQ0038  Wide Bid Ask Spread
DQ0039  Limit Up Lock
DQ0040  Limit Down Lock
```

---

## Abnormal Market Data (DQ0041–DQ0050)

```text
DQ0041  Price Spike Present
DQ0042  Abnormal Price Gap
DQ0043  Volume Spike Present
DQ0044  Abnormal Return Present
DQ0045  Abnormal Range Present
DQ0046  Tick Size Violation
DQ0047  Stale Quote Present
DQ0048  After Hours Trade Present
DQ0049  Erroneous Tick Present
DQ0050  Statistical Outlier Present
```

---

## Overall Data Quality (DQ0051–DQ0060)

```text
DQ0051  Required History Present
DQ0052  Required History Absent
DQ0053  Current Bar Present
DQ0054  Current Bar Absent
DQ0055  Session Data Complete
DQ0056  Session Data Incomplete
DQ0057  Data Feed Current
DQ0058  Data Feed Stale
DQ0059  Instrument Data Present
DQ0060  Instrument Data Absent
```

---

## Summary

| Field | Value |
|-------|-------|
| Category | Data Quality |
| Code | DQ |
| Total Rules | 60 |
| Rule Range | DQ0001 – DQ0060 |
| Status | Frozen v1.0 |

---

## Next Category

| Code | Name | Target |
|------|------|--------|
| CR | Composite Rule Library | Approximately 100 Composite Rules |

---

## Notes

This catalog defines all Atomic Rules related to Data Quality.

Each Rule represents one objective fact.

Composite logic, scoring, and investment decisions are **not** included.

These Rules are immutable after Freeze and become the official Data Quality Rule Catalog for TASS.

---

## Implementation Status

| Rule ID | Status |
|---------|--------|
| DQ0001–DQ0060 | Implemented (engine/rules/) |

---

## Related Documents

* [TASS-011 Rule Taxonomy](TASS-011_Rule_Taxonomy_Specification.md)
* [TASS-012 Rule Specification Standard](TASS-012_Rule_Specification_Standard.md)
* [TASS-013 Rule Database](TASS-013_Rule_Database_Specification.md)
* [TASS-014 TR Rule Catalog](TASS-014_TR_Rule_Catalog_v1.0.md)
* [TASS-015 MA Rule Catalog](TASS-015_MA_Rule_Catalog_v1.0.md)
* [TASS-016 PA Rule Catalog](TASS-016_PA_Rule_Catalog_v1.0.md)
* [TASS-017 VL Rule Catalog](TASS-017_VL_Rule_Catalog_v1.0.md)
* [TASS-017 MO Rule Catalog](TASS-017_MO_Rule_Catalog_v1.0.md)
* [TASS-018 VO Rule Catalog](TASS-018_VO_Rule_Catalog_v1.0.md)
* [TASS-019 MS Rule Catalog](TASS-019_MS_Rule_Catalog_v1.0.md)
* [TASS-019 SR Rule Catalog](TASS-019_SR_Rule_Catalog_v1.0.md)
* [TASS-020 BO Rule Catalog](TASS-020_BO_Rule_Catalog_v1.0.md)
* [TASS-020 PB Rule Catalog](TASS-020_PB_Rule_Catalog_v1.0.md)
* [TASS-020 PT Rule Catalog](TASS-020_PT_Rule_Catalog_v1.0.md)
* [TASS-021 CS Rule Catalog](TASS-021_CS_Rule_Catalog_v1.0.md)
* [TASS-022 GP Rule Catalog](TASS-022_GP_Rule_Catalog_v1.0.md)
* [TASS-023 RK Rule Catalog](TASS-023_RK_Rule_Catalog_v1.0.md)
* [TASS-023 EN Rule Catalog](TASS-023_EN_Rule_Catalog_v1.0.md)
* [TASS-024 MR Rule Catalog](TASS-024_MR_Rule_Catalog_v1.0.md)
* [TASS-025 MT Rule Catalog](TASS-025_MT_Rule_Catalog_v1.0.md)
* [rules/catalog/DQ_v1.0.yaml](../rules/catalog/DQ_v1.0.yaml)

---

# End of Catalog

No new DQ atomic IDs may be invented outside DQ0001–DQ0060 until catalog v2.0.
