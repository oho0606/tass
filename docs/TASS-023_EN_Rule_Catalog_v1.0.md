# TASS Rule Catalog

# Category : Entry (EN)

# Version : 1.0

**Status:** Frozen v1.0

**Machine-readable:** [rules/catalog/EN_v1.0.yaml](../rules/catalog/EN_v1.0.yaml)

---

## Category Information

| Field | Value |
|-------|-------|
| Category Code | EN |
| Category Name | Entry |
| Status | Frozen v1.0 |
| Total Rules | 60 |
| Rule Range | EN0001 – EN0060 |

---

## Trend Following Entry (EN0001–EN0010)

```text
EN0001  Entry Close Above SMA20
EN0002  Entry Close Above SMA60
EN0003  Entry Close Above EMA20
EN0004  Entry Close Above EMA60
EN0005  Entry High Above Prior Bar High
EN0006  Entry Low Above Prior Bar Low
EN0007  Entry Close Above Prior Close
EN0008  Entry Close Above N-Period High
EN0009  Entry Open Below Entry Close
EN0010  Entry Close Above Prior Bar Open
```

---

## Breakout Entry (EN0011–EN0020)

```text
EN0011  Entry Close Above Prior Swing High
EN0012  Entry Close Below Prior Swing Low
EN0013  Entry Close Above Horizontal Resistance
EN0014  Entry Close Below Horizontal Support
EN0015  Entry Close Above 52-Week High
EN0016  Entry Close Below 52-Week Low
EN0017  Entry Close Above Upper Bollinger Band
EN0018  Entry Close Below Lower Bollinger Band
EN0019  Entry Close Above R1
EN0020  Entry Close Below S1
```

---

## Pullback Entry (EN0021–EN0030)

```text
EN0021  Entry Close Above Pullback Low
EN0022  Entry Low Above Pullback Low
EN0023  Entry Close Above SMA20 After Touch
EN0024  Entry Close Above EMA20 After Touch
EN0025  Entry Close Above 38.2 Percent Retracement
EN0026  Entry Close Above 50 Percent Retracement
EN0027  Entry Close Above 61.8 Percent Retracement
EN0028  Entry Bar Following Pullback Low
EN0029  Entry Close Above Prior Pullback High
EN0030  Entry Low At Pullback Support Level
```

---

## Reversal Entry (EN0031–EN0040)

```text
EN0031  Entry Close Above Prior Swing Low
EN0032  Entry Close Below Prior Swing High
EN0033  Entry Low At N-Period Low
EN0034  Entry High At N-Period High
EN0035  Entry Close Above Support Level
EN0036  Entry Close Below Resistance Level
EN0037  Entry Close Above Reversal Bar High
EN0038  Entry Close Below Reversal Bar Low
EN0039  Entry Close Above Double Bottom Level
EN0040  Entry Close Below Double Top Level
```

---

## Entry Confirmation (EN0041–EN0050)

```text
EN0041  Entry Bar Volume Above N-Period Average
EN0042  Entry Bar Volume Below N-Period Average
EN0043  Entry Bar Volume Above Prior Bar
EN0044  Entry Bar Volume Below Prior Bar
EN0045  Entry Bar Relative Volume Above 1
EN0046  Entry Bar Relative Volume Above 2
EN0047  Entry Bar Bullish
EN0048  Entry Bar Bearish
EN0049  Entry Bar RSI Above 50
EN0050  Entry Bar RSI Below 50
```

---

## Entry Quality (EN0051–EN0060)

```text
EN0051  Entry Bar Wide Range
EN0052  Entry Bar Narrow Range
EN0053  Entry Close Near Bar High
EN0054  Entry Close Near Bar Low
EN0055  Entry Bar Body Above Half Range
EN0056  Entry Bar Body Below Half Range
EN0057  Entry Bar Overlapping Prior Bar
EN0058  Entry Gap Up At Entry Bar
EN0059  Entry Gap Down At Entry Bar
EN0060  Entry Wick Rejection At Support
```

---

## Summary

| Field | Value |
|-------|-------|
| Category | Entry |
| Code | EN |
| Total Rules | 60 |
| Rule Range | EN0001 – EN0060 |
| Status | Frozen v1.0 |

---

## Next Category

| Code | Name | Target |
|------|------|--------|
| EX | Exit | 60 Rules |

---

## Notes

This catalog defines all Atomic Rules related to Entry.

Each Rule represents one objective fact.

Composite logic, scoring, and investment decisions are **not** included.

These Rules are immutable after Freeze and become the official Entry Rule Catalog for TASS.

---

## Implementation Status

| Rule ID | Status |
|---------|--------|
| EN0001–EN0060 | Implemented (engine/rules/) |

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
* [rules/catalog/EN_v1.0.yaml](../rules/catalog/EN_v1.0.yaml)

---

# End of Catalog

No new EN atomic IDs may be invented outside EN0001–EN0060 until catalog v2.0.
