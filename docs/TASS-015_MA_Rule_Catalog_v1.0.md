# TASS Rule Catalog

# Category : Moving Average (MA)

# Version : 1.0

**Status:** Frozen v1.0

**Machine-readable:** [rules/catalog/MA_v1.0.yaml](../rules/catalog/MA_v1.0.yaml)

---

## Category Information

| Field | Value |
|-------|-------|
| Category Code | MA |
| Category Name | Moving Average |
| Status | Frozen v1.0 |
| Total Rules | 60 |
| Rule Range | MA0001 – MA0060 |

---

## Price Position (MA0001–MA0010)

```text
MA0001  Price Above SMA5
MA0002  Price Above SMA20
MA0003  Price Above SMA60
MA0004  Price Above SMA120
MA0005  Price Above SMA240
MA0006  Price Below SMA5
MA0007  Price Below SMA20
MA0008  Price Below SMA60
MA0009  Price Below SMA120
MA0010  Price Below SMA240
```

---

## EMA Position (MA0011–MA0020)

```text
MA0011  Price Above EMA5
MA0012  Price Above EMA20
MA0013  Price Above EMA60
MA0014  Price Above EMA120
MA0015  Price Above EMA240
MA0016  Price Below EMA5
MA0017  Price Below EMA20
MA0018  Price Below EMA60
MA0019  Price Below EMA120
MA0020  Price Below EMA240
```

---

## Moving Average Alignment (MA0021–MA0030)

```text
MA0021  SMA Bullish Alignment
MA0022  SMA Bearish Alignment
MA0023  EMA Bullish Alignment
MA0024  EMA Bearish Alignment
MA0025  SMA Alignment Improving
MA0026  SMA Alignment Weakening
MA0027  EMA Alignment Improving
MA0028  EMA Alignment Weakening
MA0029  Full Bullish Alignment
MA0030  Full Bearish Alignment
```

---

## Crossovers (MA0031–MA0040)

```text
MA0031  SMA Golden Cross
MA0032  SMA Death Cross
MA0033  EMA Golden Cross
MA0034  EMA Death Cross
MA0035  Short MA Cross Above Mid MA
MA0036  Short MA Cross Below Mid MA
MA0037  Mid MA Cross Above Long MA
MA0038  Mid MA Cross Below Long MA
MA0039  Multiple Golden Cross
MA0040  Multiple Death Cross
```

---

## Slope (MA0041–MA0050)

```text
MA0041  SMA Rising
MA0042  SMA Falling
MA0043  EMA Rising
MA0044  EMA Falling
MA0045  SMA Slope Increasing
MA0046  SMA Slope Decreasing
MA0047  EMA Slope Increasing
MA0048  EMA Slope Decreasing
MA0049  Moving Average Flat
MA0050  Moving Average Turning
```

---

## Distance & Structure (MA0051–MA0060)

```text
MA0051  Price Extended Above MA
MA0052  Price Extended Below MA
MA0053  Price Near Moving Average
MA0054  Moving Average Compression
MA0055  Moving Average Expansion
MA0056  Moving Average Convergence
MA0057  Moving Average Divergence
MA0058  Dynamic Support Holding
MA0059  Dynamic Resistance Holding
MA0060  Moving Average Structure Stable
```

---

## Summary

| Field | Value |
|-------|-------|
| Category | Moving Average |
| Code | MA |
| Total Rules | 60 |
| Rule Range | MA0001 – MA0060 |
| Status | Frozen v1.0 |

---

## Next Category

| Code | Name | Target |
|------|------|--------|
| PA | Price Action | 60 Rules |

---

## Notes

This catalog defines all Atomic Rules related to Moving Averages.

Each Rule represents one objective fact.

Composite logic, scoring, and investment decisions are **not** included.

These Rules are immutable after Freeze and become the official Moving Average Rule Catalog for TASS.

---

## Implementation Status

| Rule ID | Status |
|---------|--------|
| MA0001–MA0020 | ✅ Implemented (Price Position) |
| MA0021 | ✅ Implemented (SMA Bullish Alignment) |
| MA0022–MA0030 | ✅ Implemented (Alignment) |
| MA0031–MA0040 | ✅ Implemented (Crossover) |
| MA0041–MA0060 | ✅ Implemented (Slope, Distance & Structure) |

---

## Related Documents

* [TASS-011 Rule Taxonomy](TASS-011_Rule_Taxonomy_Specification.md)
* [TASS-012 Rule Specification Standard](TASS-012_Rule_Specification_Standard.md)
* [TASS-013 Rule Database](TASS-013_Rule_Database_Specification.md)
* [TASS-014 TR Rule Catalog](TASS-014_TR_Rule_Catalog_v1.0.md)
* [rules/catalog/MA_v1.0.yaml](../rules/catalog/MA_v1.0.yaml)

---

# End of Catalog

No new MA atomic IDs may be invented outside MA0001–MA0060 until catalog v2.0.
