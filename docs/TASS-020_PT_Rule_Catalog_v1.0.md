# TASS Rule Catalog

# Category : Pattern (PT)

# Version : 1.0

**Status:** Frozen v1.0

**Machine-readable:** [rules/catalog/PT_v1.0.yaml](../rules/catalog/PT_v1.0.yaml)

---

## Category Information

| Field | Value |
|-------|-------|
| Category Code | PT |
| Category Name | Pattern |
| Status | Frozen v1.0 |
| Total Rules | 60 |
| Rule Range | PT0001 – PT0060 |

---

## Continuation Patterns (PT0001–PT0010)

```text
PT0001  Bull Flag Formed
PT0002  Bear Flag Formed
PT0003  Bull Flag Active
PT0004  Bear Flag Active
PT0005  Bull Pennant Formed
PT0006  Bear Pennant Formed
PT0007  Bull Pennant Active
PT0008  Bear Pennant Active
PT0009  Rectangle Continuation Formed
PT0010  Rectangle Continuation Active
```

---

## Reversal Patterns (PT0011–PT0020)

```text
PT0011  Head And Shoulders Formed
PT0012  Inverse Head And Shoulders Formed
PT0013  Head And Shoulders Active
PT0014  Inverse Head And Shoulders Active
PT0015  Rounding Top Formed
PT0016  Rounding Bottom Formed
PT0017  Rounding Top Active
PT0018  Rounding Bottom Active
PT0019  V Top Formed
PT0020  V Bottom Formed
```

---

## Triangle Patterns (PT0021–PT0030)

```text
PT0021  Ascending Triangle Formed
PT0022  Descending Triangle Formed
PT0023  Symmetrical Triangle Formed
PT0024  Ascending Triangle Active
PT0025  Descending Triangle Active
PT0026  Symmetrical Triangle Active
PT0027  Triangle Upper Trendline Present
PT0028  Triangle Lower Trendline Present
PT0029  Triangle Apex Present
PT0030  Triangle Boundaries Converging
```

---

## Channel & Wedge Patterns (PT0031–PT0040)

```text
PT0031  Ascending Channel Formed
PT0032  Descending Channel Formed
PT0033  Horizontal Channel Formed
PT0034  Rising Wedge Formed
PT0035  Falling Wedge Formed
PT0036  Ascending Channel Active
PT0037  Descending Channel Active
PT0038  Horizontal Channel Active
PT0039  Rising Wedge Active
PT0040  Falling Wedge Active
```

---

## Double Top / Double Bottom (PT0041–PT0050)

```text
PT0041  Double Top Formed
PT0042  Double Bottom Formed
PT0043  Double Top Active
PT0044  Double Bottom Active
PT0045  Double Top Peaks Equal
PT0046  Double Bottom Troughs Equal
PT0047  Double Top Neckline Present
PT0048  Double Bottom Neckline Present
PT0049  Double Top First Peak Formed
PT0050  Double Bottom First Trough Formed
```

---

## Pattern Quality (PT0051–PT0060)

```text
PT0051  Pattern Upper Boundary Defined
PT0052  Pattern Lower Boundary Defined
PT0053  Pattern Boundaries Parallel
PT0054  Pattern Boundaries Converging
PT0055  Pattern Minimum Duration Met
PT0056  Pattern Trendline Touches Met
PT0057  Pattern Height Defined
PT0058  Pattern Width Defined
PT0059  Pattern Neckline Defined
PT0060  Pattern Structure Complete
```

---

## Summary

| Field | Value |
|-------|-------|
| Category | Pattern |
| Code | PT |
| Total Rules | 60 |
| Rule Range | PT0001 – PT0060 |
| Status | Frozen v1.0 |

---

## Next Category

| Code | Name | Target |
|------|------|--------|
| CS | Candlestick | 60 Rules |

---

## Notes

This catalog defines all Atomic Rules related to Pattern.

Each Rule represents one objective fact.

Composite logic, scoring, and investment decisions are **not** included.

These Rules are immutable after Freeze and become the official Pattern Rule Catalog for TASS.

---

## Implementation Status

| Rule ID | Status |
|---------|--------|
| PT0001–PT0060 | Implemented (engine/rules/) |

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
* [rules/catalog/PT_v1.0.yaml](../rules/catalog/PT_v1.0.yaml)

---

# End of Catalog

No new PT atomic IDs may be invented outside PT0001–PT0060 until catalog v2.0.
