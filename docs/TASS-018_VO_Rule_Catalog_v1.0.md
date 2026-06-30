# TASS Rule Catalog

# Category : Volatility (VO)

# Version : 1.0

**Status:** Frozen v1.0

**Machine-readable:** [rules/catalog/VO_v1.0.yaml](../rules/catalog/VO_v1.0.yaml)

---

## Category Information

| Field | Value |
|-------|-------|
| Category Code | VO |
| Category Name | Volatility |
| Status | Frozen v1.0 |
| Total Rules | 60 |
| Rule Range | VO0001 – VO0060 |

---

## ATR (VO0001–VO0010)

```text
VO0001  ATR Rising
VO0002  ATR Falling
VO0003  ATR Above Prior ATR
VO0004  ATR Below Prior ATR
VO0005  ATR Above N-Period Average
VO0006  ATR Below N-Period Average
VO0007  ATR At N-Period High
VO0008  ATR At N-Period Low
VO0009  ATR Flat
VO0010  ATR Turning
```

---

## True Range (VO0011–VO0020)

```text
VO0011  True Range Above Prior True Range
VO0012  True Range Below Prior True Range
VO0013  True Range Above N-Period Average
VO0014  True Range Below N-Period Average
VO0015  True Range At N-Period High
VO0016  True Range At N-Period Low
VO0017  Wide True Range
VO0018  Narrow True Range
VO0019  True Range Expanding
VO0020  True Range Contracting
```

---

## Historical Volatility (VO0021–VO0030)

```text
VO0021  Historical Volatility Rising
VO0022  Historical Volatility Falling
VO0023  Historical Volatility Above Prior
VO0024  Historical Volatility Below Prior
VO0025  Historical Volatility Above N-Period Average
VO0026  Historical Volatility Below N-Period Average
VO0027  Historical Volatility At N-Period High
VO0028  Historical Volatility At N-Period Low
VO0029  Historical Volatility Flat
VO0030  Historical Volatility Turning
```

---

## Bollinger Bands (VO0031–VO0040)

```text
VO0031  Price Above Upper Bollinger Band
VO0032  Price Below Lower Bollinger Band
VO0033  Price At Upper Bollinger Band
VO0034  Price At Lower Bollinger Band
VO0035  Price At Middle Bollinger Band
VO0036  Price Inside Bollinger Bands
VO0037  Bollinger Band Width Above Average
VO0038  Bollinger Band Width Below Average
VO0039  Bollinger Band Width At N-Period Low
VO0040  Bollinger Band Width At N-Period High
```

---

## Volatility Expansion & Contraction (VO0041–VO0050)

```text
VO0041  Volatility Expanding
VO0042  Volatility Contracting
VO0043  ATR Expanding
VO0044  ATR Contracting
VO0045  Bollinger Band Width Expanding
VO0046  Bollinger Band Width Contracting
VO0047  Historical Volatility Expanding
VO0048  Historical Volatility Contracting
VO0049  Volatility At N-Period High
VO0050  Volatility At N-Period Low
```

---

## Volatility Stability (VO0051–VO0060)

```text
VO0051  ATR Stable
VO0052  Historical Volatility Stable
VO0053  Bollinger Band Width Stable
VO0054  True Range Stable
VO0055  ATR Within N-Period Range
VO0056  Historical Volatility Within N-Period Range
VO0057  Bollinger Band Width Within N-Period Range
VO0058  Consecutive Stable ATR
VO0059  Volatility Consistency High
VO0060  Volatility Consistency Low
```

---

## Summary

| Field | Value |
|-------|-------|
| Category | Volatility |
| Code | VO |
| Total Rules | 60 |
| Rule Range | VO0001 – VO0060 |
| Status | Frozen v1.0 |

---

## Next Category

| Code | Name | Target |
|------|------|--------|
| MS | Market Structure | 60 Rules |

---

## Notes

This catalog defines all Atomic Rules related to Volatility.

Each Rule represents one objective fact.

Composite logic, scoring, and investment decisions are **not** included.

These Rules are immutable after Freeze and become the official Volatility Rule Catalog for TASS.

---

## Implementation Status

| Rule ID | Status |
|---------|--------|
| VO0001–VO0060 | Implemented (engine/rules/) |

---

## Related Documents

* [TASS-011 Rule Taxonomy](TASS-011_Rule_Taxonomy_Specification.md)
* [TASS-012 Rule Specification Standard](TASS-012_Rule_Specification_Standard.md)
* [TASS-013 Rule Database](TASS-013_Rule_Database_Specification.md)
* [TASS-014 TR Rule Catalog](TASS-014_TR_Rule_Catalog_v1.0.md)
* [TASS-015 MA Rule Catalog](TASS-015_MA_Rule_Catalog_v1.0.md)
* [TASS-016 PA Rule Catalog](TASS-016_PA_Rule_Catalog_v1.0.md)
* [TASS-017 VL Rule Catalog](TASS-017_VL_Rule_Catalog_v1.0.md)
* [rules/catalog/VO_v1.0.yaml](../rules/catalog/VO_v1.0.yaml)

---

# End of Catalog

No new VO atomic IDs may be invented outside VO0001–VO0060 until catalog v2.0.
