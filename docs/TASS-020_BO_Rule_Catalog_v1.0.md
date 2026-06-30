# TASS Rule Catalog

# Category : Breakout (BO)

# Version : 1.0

**Status:** Frozen v1.0

**Machine-readable:** [rules/catalog/BO_v1.0.yaml](../rules/catalog/BO_v1.0.yaml)

---

## Category Information

| Field | Value |
|-------|-------|
| Category Code | BO |
| Category Name | Breakout |
| Status | Frozen v1.0 |
| Total Rules | 60 |
| Rule Range | BO0001 – BO0060 |

---

## Price Breakout (BO0001–BO0010)

```text
BO0001  Close Above N-Period High
BO0002  Close Below N-Period Low
BO0003  High Above N-Period High
BO0004  Low Below N-Period Low
BO0005  Open Above N-Period High
BO0006  Open Below N-Period Low
BO0007  Close Above Prior High
BO0008  Close Below Prior Low
BO0009  Price Above 52-Week High
BO0010  Price Below 52-Week Low
```

---

## Volume Breakout (BO0011–BO0020)

```text
BO0011  Breakout Bar Volume Above N-Period Average
BO0012  Breakout Bar Volume Below N-Period Average
BO0013  Breakout Bar Volume Above Prior Volume
BO0014  Breakout Bar Volume Below Prior Volume
BO0015  Breakout Bar Volume Above N-Period High
BO0016  Breakout Bar Volume At N-Period High
BO0017  Breakout Bar Relative Volume Above 1
BO0018  Breakout Bar Relative Volume Above 2
BO0019  Breakout Bar Volume Spike
BO0020  Breakout Bar Volume Rising
```

---

## Moving Average Breakout (BO0021–BO0030)

```text
BO0021  Close Cross Above SMA5
BO0022  Close Cross Below SMA5
BO0023  Close Cross Above SMA20
BO0024  Close Cross Below SMA20
BO0025  Close Cross Above SMA60
BO0026  Close Cross Below SMA60
BO0027  Close Cross Above EMA20
BO0028  Close Cross Below EMA20
BO0029  Close Cross Above EMA60
BO0030  Close Cross Below EMA60
```

---

## Volatility Breakout (BO0031–BO0040)

```text
BO0031  Breakout Bar True Range Above N-Period Average
BO0032  Breakout Bar True Range Above N-Period High
BO0033  Breakout Bar ATR Above N-Period Average
BO0034  Breakout Bar ATR Above Prior ATR
BO0035  Price Above Upper Bollinger Band
BO0036  Price Below Lower Bollinger Band
BO0037  Breakout Bar Bollinger Band Width Expanding
BO0038  Breakout Bar Volatility Expanding
BO0039  Breakout Bar Historical Volatility Above N-Period Average
BO0040  Breakout Bar Bollinger Band Width At N-Period High
```

---

## Resistance Breakout Confirmation (BO0041–BO0050)

```text
BO0041  Close Above Horizontal Resistance
BO0042  Close Below Horizontal Support
BO0043  High Above Horizontal Resistance
BO0044  Low Below Horizontal Support
BO0045  Close Above Prior Swing High
BO0046  Close Below Prior Swing Low
BO0047  Close Above Trendline Resistance
BO0048  Close Below Trendline Support
BO0049  Close Above R1
BO0050  Close Below S1
```

---

## Breakout Quality (BO0051–BO0060)

```text
BO0051  Breakout Bar Bullish
BO0052  Breakout Bar Bearish
BO0053  Breakout Bar Wide Range
BO0054  Breakout Bar Narrow Range
BO0055  Breakout Close Near High
BO0056  Breakout Close Near Low
BO0057  Breakout Body Above Half Range
BO0058  Breakout Body Below Half Range
BO0059  Breakout Gap Up
BO0060  Breakout Gap Down
```

---

## Summary

| Field | Value |
|-------|-------|
| Category | Breakout |
| Code | BO |
| Total Rules | 60 |
| Rule Range | BO0001 – BO0060 |
| Status | Frozen v1.0 |

---

## Next Category

| Code | Name | Target |
|------|------|--------|
| PB | Pullback | 60 Rules |

---

## Notes

This catalog defines all Atomic Rules related to Breakout.

Each Rule represents one objective fact.

Composite logic, scoring, and investment decisions are **not** included.

These Rules are immutable after Freeze and become the official Breakout Rule Catalog for TASS.

---

## Implementation Status

| Rule ID | Status |
|---------|--------|
| BO0001–BO0060 | Implemented (engine/rules/) |

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
* [rules/catalog/BO_v1.0.yaml](../rules/catalog/BO_v1.0.yaml)

---

# End of Catalog

No new BO atomic IDs may be invented outside BO0001–BO0060 until catalog v2.0.
