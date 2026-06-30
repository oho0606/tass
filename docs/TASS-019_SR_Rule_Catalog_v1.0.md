# TASS Rule Catalog

# Category : Support & Resistance (SR)

# Version : 1.0

**Status:** Frozen v1.0

**Machine-readable:** [rules/catalog/SR_v1.0.yaml](../rules/catalog/SR_v1.0.yaml)

---

## Category Information

| Field | Value |
|-------|-------|
| Category Code | SR |
| Category Name | Support & Resistance |
| Status | Frozen v1.0 |
| Total Rules | 60 |
| Rule Range | SR0001 – SR0060 |

---

## Horizontal Support (SR0001–SR0010)

```text
SR0001  Price Above Horizontal Support
SR0002  Price Below Horizontal Support
SR0003  Price At Horizontal Support
SR0004  Price Near Horizontal Support
SR0005  Price Touching Horizontal Support
SR0006  Horizontal Support Level Identified
SR0007  Prior Low As Horizontal Support
SR0008  Swing Low As Horizontal Support
SR0009  N-Period Low As Horizontal Support
SR0010  Price Crossing Above Horizontal Support
```

---

## Horizontal Resistance (SR0011–SR0020)

```text
SR0011  Price Above Horizontal Resistance
SR0012  Price Below Horizontal Resistance
SR0013  Price At Horizontal Resistance
SR0014  Price Near Horizontal Resistance
SR0015  Price Touching Horizontal Resistance
SR0016  Horizontal Resistance Level Identified
SR0017  Prior High As Horizontal Resistance
SR0018  Swing High As Horizontal Resistance
SR0019  N-Period High As Horizontal Resistance
SR0020  Price Crossing Below Horizontal Resistance
```

---

## Dynamic Support & Resistance (SR0021–SR0030)

```text
SR0021  Price Above Dynamic Support
SR0022  Price Below Dynamic Support
SR0023  Price At Dynamic Support
SR0024  Price Near Dynamic Support
SR0025  Price Touching Dynamic Support
SR0026  Dynamic Support Present
SR0027  Price Above Dynamic Resistance
SR0028  Price Below Dynamic Resistance
SR0029  Price At Dynamic Resistance
SR0030  Price Touching Dynamic Resistance
```

---

## Pivot Levels (SR0031–SR0040)

```text
SR0031  Price Above Pivot Point
SR0032  Price Below Pivot Point
SR0033  Price At Pivot Point
SR0034  Price Above S1
SR0035  Price Below S1
SR0036  Price At S1
SR0037  Price Above R1
SR0038  Price Below R1
SR0039  Price At R1
SR0040  Price At S2
```

---

## Fibonacci Levels (SR0041–SR0050)

```text
SR0041  Price Above Fibonacci 23.6 Level
SR0042  Price Below Fibonacci 23.6 Level
SR0043  Price At Fibonacci 23.6 Level
SR0044  Price Above Fibonacci 38.2 Level
SR0045  Price Below Fibonacci 38.2 Level
SR0046  Price At Fibonacci 38.2 Level
SR0047  Price Above Fibonacci 50.0 Level
SR0048  Price Below Fibonacci 50.0 Level
SR0049  Price At Fibonacci 50.0 Level
SR0050  Price At Fibonacci 61.8 Level
```

---

## Support & Resistance Strength (SR0051–SR0060)

```text
SR0051  Support Level First Touch
SR0052  Support Level Second Touch
SR0053  Support Level Multiple Touches
SR0054  Resistance Level First Touch
SR0055  Resistance Level Second Touch
SR0056  Resistance Level Multiple Touches
SR0057  Support Level Holding
SR0058  Resistance Level Holding
SR0059  Confluent Support Levels Present
SR0060  Confluent Resistance Levels Present
```

---

## Summary

| Field | Value |
|-------|-------|
| Category | Support & Resistance |
| Code | SR |
| Total Rules | 60 |
| Rule Range | SR0001 – SR0060 |
| Status | Frozen v1.0 |

---

## Next Category

| Code | Name | Target |
|------|------|--------|
| BO | Breakout | 60 Rules |

---

## Notes

This catalog defines all Atomic Rules related to Support & Resistance.

Each Rule represents one objective fact.

Composite logic, scoring, and investment decisions are **not** included.

These Rules are immutable after Freeze and become the official Support & Resistance Rule Catalog for TASS.

---

## Implementation Status

| Rule ID | Status |
|---------|--------|
| SR0001–SR0060 | Implemented (engine/rules/) |

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
* [rules/catalog/SR_v1.0.yaml](../rules/catalog/SR_v1.0.yaml)

---

# End of Catalog

No new SR atomic IDs may be invented outside SR0001–SR0060 until catalog v2.0.
