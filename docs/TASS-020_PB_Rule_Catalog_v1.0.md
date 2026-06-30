# TASS Rule Catalog

# Category : Pullback (PB)

# Version : 1.0

**Status:** Frozen v1.0

**Machine-readable:** [rules/catalog/PB_v1.0.yaml](../rules/catalog/PB_v1.0.yaml)

---

## Category Information

| Field | Value |
|-------|-------|
| Category Code | PB |
| Category Name | Pullback |
| Status | Frozen v1.0 |
| Total Rules | 60 |
| Rule Range | PB0001 – PB0060 |

---

## Healthy Pullback (PB0001–PB0010)

```text
PB0001  Pullback In Progress
PB0002  Retracement Below 38.2 Percent
PB0003  Retracement Between 38.2 And 50 Percent
PB0004  Retracement Between 50 And 61.8 Percent
PB0005  Pullback Low Above Prior Swing Low
PB0006  Pullback High Below Prior Swing High
PB0007  Pullback Duration Fewer Than N Bars
PB0008  Pullback Range Narrower Than Prior Leg
PB0009  Pullback Close Above Prior Leg Midpoint
PB0010  Pullback Bar Count Fewer Than N
```

---

## Deep Pullback (PB0011–PB0020)

```text
PB0011  Retracement Above 61.8 Percent
PB0012  Retracement Above 78.6 Percent
PB0013  Pullback Low Below Prior Swing Low
PB0014  Pullback Low Below Prior Higher Low
PB0015  Pullback Duration Greater Than N Bars
PB0016  Pullback Range Wider Than Prior Leg
PB0017  Pullback Depth Above N-Period Average
PB0018  Price Below 50 Percent Retracement Level
PB0019  Pullback Low At N-Period Low
PB0020  Pullback Bar Count Greater Than N
```

---

## Moving Average Pullback (PB0021–PB0030)

```text
PB0021  Price Touching SMA20 During Pullback
PB0022  Price Touching SMA60 During Pullback
PB0023  Price Touching EMA20 During Pullback
PB0024  Price Touching EMA60 During Pullback
PB0025  Price Closing Above SMA20 During Pullback
PB0026  Price Closing Below SMA20 During Pullback
PB0027  Price Closed Above SMA20 After Touch
PB0028  Price Closed Above SMA60 After Touch
PB0029  Price Above SMA During Pullback
PB0030  Price Below SMA During Pullback
```

---

## Volume Pullback (PB0031–PB0040)

```text
PB0031  Pullback Volume Below N-Period Average
PB0032  Pullback Volume Decreasing
PB0033  Pullback Volume Lower Than Advance Volume
PB0034  Pullback Volume At N-Period Low
PB0035  Pullback Volume Below Prior Bar
PB0036  Pullback Volume Increasing
PB0037  Pullback Volume Above N-Period Average
PB0038  Pullback Volume Higher Than Advance Volume
PB0039  Pullback Volume Spike
PB0040  Pullback Volume Flat
```

---

## Trend Continuation Pullback (PB0041–PB0050)

```text
PB0041  Pullback Following Advance Leg
PB0042  Pullback Following Decline Leg
PB0043  Pullback Low Above Prior Higher Low
PB0044  Pullback High Below Prior Lower High
PB0045  Higher Low Formed During Pullback
PB0046  Lower High Formed During Pullback
PB0047  Pullback Low Above Rising SMA
PB0048  Pullback High Below Falling SMA
PB0049  Pullback Within Up Trend Channel
PB0050  Pullback Within Down Trend Channel
```

---

## Pullback Quality (PB0051–PB0060)

```text
PB0051  Pullback Overlapping Prior Bars
PB0052  Pullback Body Size Decreasing
PB0053  Pullback Range Contracting
PB0054  Pullback Range Expanding
PB0055  Pullback Gap Present
PB0056  Pullback Close Near Bar High
PB0057  Pullback Close Near Bar Low
PB0058  Pullback Wick Rejection At Support
PB0059  Pullback Wick Rejection At MA
PB0060  Pullback Candle Count Decreasing
```

---

## Summary

| Field | Value |
|-------|-------|
| Category | Pullback |
| Code | PB |
| Total Rules | 60 |
| Rule Range | PB0001 – PB0060 |
| Status | Frozen v1.0 |

---

## Next Category

| Code | Name | Target |
|------|------|--------|
| PT | Pattern | 60 Rules |

---

## Notes

This catalog defines all Atomic Rules related to Pullback.

Each Rule represents one objective fact.

Composite logic, scoring, and investment decisions are **not** included.

These Rules are immutable after Freeze and become the official Pullback Rule Catalog for TASS.

---

## Implementation Status

| Rule ID | Status |
|---------|--------|
| PB0001–PB0060 | Implemented (engine/rules/) |

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
* [rules/catalog/PB_v1.0.yaml](../rules/catalog/PB_v1.0.yaml)

---

# End of Catalog

No new PB atomic IDs may be invented outside PB0001–PB0060 until catalog v2.0.
