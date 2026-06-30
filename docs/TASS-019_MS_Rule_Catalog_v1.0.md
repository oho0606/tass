# TASS Rule Catalog

# Category : Market Structure (MS)

# Version : 1.0

**Status:** Frozen v1.0

**Machine-readable:** [rules/catalog/MS_v1.0.yaml](../rules/catalog/MS_v1.0.yaml)

---

## Category Information

| Field | Value |
|-------|-------|
| Category Code | MS |
| Category Name | Market Structure |
| Status | Frozen v1.0 |
| Total Rules | 60 |
| Rule Range | MS0001 – MS0060 |

---

## Higher High / Higher Low (MS0001–MS0010)

```text
MS0001  Higher High Formed
MS0002  Higher High Confirmed
MS0003  Higher High Exceeds Prior
MS0004  Higher High Active
MS0005  Consecutive Higher High
MS0006  Higher Low Formed
MS0007  Higher Low Confirmed
MS0008  Higher Low Exceeds Prior
MS0009  Higher Low Active
MS0010  Consecutive Higher Low
```

---

## Lower High / Lower Low (MS0011–MS0020)

```text
MS0011  Lower High Formed
MS0012  Lower High Confirmed
MS0013  Lower High Below Prior
MS0014  Lower High Active
MS0015  Consecutive Lower High
MS0016  Lower Low Formed
MS0017  Lower Low Confirmed
MS0018  Lower Low Below Prior
MS0019  Lower Low Active
MS0020  Consecutive Lower Low
```

---

## Swing High / Swing Low (MS0021–MS0030)

```text
MS0021  Swing High Formed
MS0022  Swing Low Formed
MS0023  Swing High Confirmed
MS0024  Swing Low Confirmed
MS0025  Swing High Active
MS0026  Swing Low Active
MS0027  Recent Swing High
MS0028  Recent Swing Low
MS0029  Equal Swing High
MS0030  Equal Swing Low
```

---

## Break of Structure (MS0031–MS0040)

```text
MS0031  Bullish Break of Structure
MS0032  Bearish Break of Structure
MS0033  BOS Above Swing High
MS0034  BOS Below Swing Low
MS0035  Bullish BOS With Close
MS0036  Bearish BOS With Close
MS0037  Bullish BOS On Current Bar
MS0038  Bearish BOS On Current Bar
MS0039  Price Above BOS Level
MS0040  Price Below BOS Level
```

---

## Change of Character (MS0041–MS0050)

```text
MS0041  Bullish Change of Character
MS0042  Bearish Change of Character
MS0043  CHoCH Above Lower High
MS0044  CHoCH Below Higher Low
MS0045  Bullish CHoCH With Close
MS0046  Bearish CHoCH With Close
MS0047  Bullish CHoCH On Current Bar
MS0048  Bearish CHoCH On Current Bar
MS0049  Price Above CHoCH Level
MS0050  Price Below CHoCH Level
```

---

## Market Structure Quality (MS0051–MS0060)

```text
MS0051  Swing Spacing Narrow
MS0052  Swing Spacing Wide
MS0053  Swing Overlap Present
MS0054  Swing Overlap Absent
MS0055  Structure Leg Extended
MS0056  Structure Leg Compressed
MS0057  Equal Highs In Structure
MS0058  Equal Lows In Structure
MS0059  Internal Swing Present
MS0060  External Swing Present
```

---

## Summary

| Field | Value |
|-------|-------|
| Category | Market Structure |
| Code | MS |
| Total Rules | 60 |
| Rule Range | MS0001 – MS0060 |
| Status | Frozen v1.0 |

---

## Next Category

| Code | Name | Target |
|------|------|--------|
| SR | Support & Resistance | 60 Rules |

---

## Notes

This catalog defines all Atomic Rules related to Market Structure.

Each Rule represents one objective fact.

Composite logic, scoring, and investment decisions are **not** included.

These Rules are immutable after Freeze and become the official Market Structure Rule Catalog for TASS.

---

## Implementation Status

| Rule ID | Status |
|---------|--------|
| MS0001–MS0060 | Implemented (engine/rules/) |

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
* [rules/catalog/MS_v1.0.yaml](../rules/catalog/MS_v1.0.yaml)

---

# End of Catalog

No new MS atomic IDs may be invented outside MS0001–MS0060 until catalog v2.0.
