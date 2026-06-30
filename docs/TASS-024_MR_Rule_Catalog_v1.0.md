# TASS Rule Catalog

# Category : Market Regime (MR)

# Version : 1.0

**Status:** Frozen v1.0

**Machine-readable:** [rules/catalog/MR_v1.0.yaml](../rules/catalog/MR_v1.0.yaml)

---

## Category Information

| Field | Value |
|-------|-------|
| Category Code | MR |
| Category Name | Market Regime |
| Status | Frozen v1.0 |
| Total Rules | 60 |
| Rule Range | MR0001 – MR0060 |

---

## Bull Market (MR0001–MR0010)

```text
MR0001  Close Above SMA200
MR0002  Close Above SMA60
MR0003  Close Above SMA20
MR0004  SMA20 Above SMA60
MR0005  SMA60 Above SMA200
MR0006  SMA20 Rising
MR0007  SMA60 Rising
MR0008  SMA200 Rising
MR0009  N-Period Return Positive
MR0010  Close At N-Period High
```

---

## Bear Market (MR0011–MR0020)

```text
MR0011  Close Below SMA200
MR0012  Close Below SMA60
MR0013  Close Below SMA20
MR0014  SMA20 Below SMA60
MR0015  SMA60 Below SMA200
MR0016  SMA20 Falling
MR0017  SMA60 Falling
MR0018  SMA200 Falling
MR0019  N-Period Return Negative
MR0020  Close At N-Period Low
```

---

## Sideways Market (MR0021–MR0030)

```text
MR0021  Close Between SMA20 And SMA60
MR0022  SMA20 Flat
MR0023  SMA60 Flat
MR0024  Close Within N-Period Range
MR0025  N-Period Return Near Zero
MR0026  SMA20 Near SMA60
MR0027  Price Range Narrow
MR0028  ADX Below Threshold
MR0029  Close Near N-Period Midpoint
MR0030  Overlapping Range Bars Present
```

---

## High Volatility Regime (MR0031–MR0040)

```text
MR0031  ATR Above N-Period Average
MR0032  ATR At N-Period High
MR0033  Historical Volatility Above N-Period Average
MR0034  Historical Volatility At N-Period High
MR0035  Bollinger Band Width Above Average
MR0036  Bollinger Band Width At N-Period High
MR0037  True Range Above N-Period Average
MR0038  Wide Daily Range
MR0039  Volatility Above Prior Period
MR0040  Consecutive Wide Range Bars
```

---

## Low Volatility Regime (MR0041–MR0050)

```text
MR0041  ATR Below N-Period Average
MR0042  ATR At N-Period Low
MR0043  Historical Volatility Below N-Period Average
MR0044  Historical Volatility At N-Period Low
MR0045  Bollinger Band Width Below Average
MR0046  Bollinger Band Width At N-Period Low
MR0047  True Range Below N-Period Average
MR0048  Narrow Daily Range
MR0049  Volatility Below Prior Period
MR0050  Consecutive Narrow Range Bars
```

---

## Market Regime Strength (MR0051–MR0060)

```text
MR0051  ADX Above Threshold
MR0052  ADX Rising
MR0053  ADX At N-Period High
MR0054  ADX Falling
MR0055  Consecutive Close Above SMA200
MR0056  Consecutive Close Below SMA200
MR0057  SMA200 Slope Steep
MR0058  SMA200 Slope Flat
MR0059  Plus DI Above Minus DI
MR0060  Minus DI Above Plus DI
```

---

## Summary

| Field | Value |
|-------|-------|
| Category | Market Regime |
| Code | MR |
| Total Rules | 60 |
| Rule Range | MR0001 – MR0060 |
| Status | Frozen v1.0 |

---

## Next Category

| Code | Name | Target |
|------|------|--------|
| MT | Multi Timeframe | 60 Rules |

---

## Notes

This catalog defines all Atomic Rules related to Market Regime.

Each Rule represents one objective fact.

Composite logic, scoring, and investment decisions are **not** included.

These Rules are immutable after Freeze and become the official Market Regime Rule Catalog for TASS.

---

## Implementation Status

| Rule ID | Status |
|---------|--------|
| MR0001–MR0060 | Implemented (engine/rules/) |

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
* [rules/catalog/MR_v1.0.yaml](../rules/catalog/MR_v1.0.yaml)

---

# End of Catalog

No new MR atomic IDs may be invented outside MR0001–MR0060 until catalog v2.0.
