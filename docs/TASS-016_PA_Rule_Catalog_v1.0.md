# TASS Rule Catalog

# Category : Price Action (PA)

# Version : 1.0

**Status:** Frozen v1.0

**Machine-readable:** [rules/catalog/PA_v1.0.yaml](../rules/catalog/PA_v1.0.yaml)

---

## Category Information

| Field | Value |
|-------|-------|
| Category Code | PA |
| Category Name | Price Action |
| Status | Frozen v1.0 |
| Total Rules | 60 |
| Rule Range | PA0001 – PA0060 |

---

## High / Low (PA0001–PA0010)

```text
PA0001  Current High Above Prior High
PA0002  Current High Below Prior High
PA0003  Current High Equal Prior High
PA0004  Current Low Above Prior Low
PA0005  Current Low Below Prior Low
PA0006  Current Low Equal Prior Low
PA0007  Current High Above N-Period High
PA0008  Current Low Below N-Period Low
PA0009  Current High At N-Period High
PA0010  Current Low At N-Period Low
```

---

## Candle Body (PA0011–PA0020)

```text
PA0011  Bullish Candle
PA0012  Bearish Candle
PA0013  Doji Candle
PA0014  Long Body Candle
PA0015  Short Body Candle
PA0016  Body Larger Than Prior Body
PA0017  Body Smaller Than Prior Body
PA0018  Body Above Half Range
PA0019  Body Below Half Range
PA0020  Marubozu Body
```

---

## Upper / Lower Wick (PA0021–PA0030)

```text
PA0021  Long Upper Wick
PA0022  Long Lower Wick
PA0023  Short Upper Wick
PA0024  Short Lower Wick
PA0025  Upper Wick Larger Than Body
PA0026  Lower Wick Larger Than Body
PA0027  Upper Wick Larger Than Prior Wick
PA0028  Lower Wick Larger Than Prior Wick
PA0029  No Upper Wick
PA0030  No Lower Wick
```

---

## Price Range (PA0031–PA0040)

```text
PA0031  Wide Range Bar
PA0032  Narrow Range Bar
PA0033  Range Larger Than Prior Range
PA0034  Range Smaller Than Prior Range
PA0035  Inside Bar
PA0036  Outside Bar
PA0037  Range Above N-Period Average
PA0038  Range Below N-Period Average
PA0039  Range Expanding
PA0040  Range Contracting
```

---

## Swing Structure (PA0041–PA0050)

```text
PA0041  Swing High Formed
PA0042  Swing Low Formed
PA0043  Higher Swing High
PA0044  Lower Swing High
PA0045  Higher Swing Low
PA0046  Lower Swing Low
PA0047  Equal Swing Highs
PA0048  Equal Swing Lows
PA0049  Price Above Last Swing High
PA0050  Price Below Last Swing Low
```

---

## Price Strength & Closing (PA0051–PA0060)

```text
PA0051  Strong Close
PA0052  Weak Close
PA0053  Close Near High
PA0054  Close Near Low
PA0055  Close Above Midpoint
PA0056  Close Below Midpoint
PA0057  Close Above Prior Close
PA0058  Close Below Prior Close
PA0059  Close At Period High
PA0060  Close At Period Low
```

---

## Summary

| Field | Value |
|-------|-------|
| Category | Price Action |
| Code | PA |
| Total Rules | 60 |
| Rule Range | PA0001 – PA0060 |
| Status | Frozen v1.0 |

---

## Next Category

| Code | Name | Target |
|------|------|--------|
| VL | Volume | 60 Rules |

---

## Notes

This catalog defines all Atomic Rules related to Price Action.

Each Rule represents one objective fact.

Composite logic, scoring, and investment decisions are **not** included.

These Rules are immutable after Freeze and become the official Price Action Rule Catalog for TASS.

---

## Implementation Status

| Rule ID | Status |
|---------|--------|
| PA0001–PA0060 | Implemented (engine/rules/) |

---

## Related Documents

* [TASS-011 Rule Taxonomy](TASS-011_Rule_Taxonomy_Specification.md)
* [TASS-012 Rule Specification Standard](TASS-012_Rule_Specification_Standard.md)
* [TASS-013 Rule Database](TASS-013_Rule_Database_Specification.md)
* [TASS-014 TR Rule Catalog](TASS-014_TR_Rule_Catalog_v1.0.md)
* [TASS-015 MA Rule Catalog](TASS-015_MA_Rule_Catalog_v1.0.md)
* [rules/catalog/PA_v1.0.yaml](../rules/catalog/PA_v1.0.yaml)

---

# End of Catalog

No new PA atomic IDs may be invented outside PA0001–PA0060 until catalog v2.0.
