# TASS Rule Catalog

# Category : Momentum (MO)

# Version : 1.0

**Status:** Frozen v1.0

**Machine-readable:** [rules/catalog/MO_v1.0.yaml](../rules/catalog/MO_v1.0.yaml)

---

## Category Information

| Field | Value |
|-------|-------|
| Category Code | MO |
| Category Name | Momentum |
| Status | Frozen v1.0 |
| Total Rules | 60 |
| Rule Range | MO0001 – MO0060 |

---

## RSI (MO0001–MO0010)

```text
MO0001  RSI Above 70
MO0002  RSI Below 30
MO0003  RSI Above 50
MO0004  RSI Below 50
MO0005  RSI Rising
MO0006  RSI Falling
MO0007  RSI Cross Above 50
MO0008  RSI Cross Below 50
MO0009  RSI Cross Above 70
MO0010  RSI Cross Below 30
```

---

## MACD (MO0011–MO0020)

```text
MO0011  MACD Above Zero
MO0012  MACD Below Zero
MO0013  MACD Above Signal Line
MO0014  MACD Below Signal Line
MO0015  MACD Cross Above Signal
MO0016  MACD Cross Below Signal
MO0017  MACD Histogram Positive
MO0018  MACD Histogram Negative
MO0019  MACD Histogram Rising
MO0020  MACD Histogram Falling
```

---

## Stochastic (MO0021–MO0030)

```text
MO0021  Stochastic Above 80
MO0022  Stochastic Below 20
MO0023  Stochastic Above 50
MO0024  Stochastic Below 50
MO0025  Stochastic %K Above %D
MO0026  Stochastic %K Below %D
MO0027  Stochastic %K Cross Above %D
MO0028  Stochastic %K Cross Below %D
MO0029  Stochastic Rising
MO0030  Stochastic Falling
```

---

## CCI (MO0031–MO0040)

```text
MO0031  CCI Above 100
MO0032  CCI Below Negative 100
MO0033  CCI Above Zero
MO0034  CCI Below Zero
MO0035  CCI Rising
MO0036  CCI Falling
MO0037  CCI Cross Above Zero
MO0038  CCI Cross Below Zero
MO0039  CCI Cross Above 100
MO0040  CCI Cross Below Negative 100
```

---

## MFI (MO0041–MO0050)

```text
MO0041  MFI Above 80
MO0042  MFI Below 20
MO0043  MFI Above 50
MO0044  MFI Below 50
MO0045  MFI Rising
MO0046  MFI Falling
MO0047  MFI Cross Above 50
MO0048  MFI Cross Below 50
MO0049  MFI Cross Above 80
MO0050  MFI Cross Below 20
```

---

## Momentum Strength (MO0051–MO0060)

```text
MO0051  Rate of Change Positive
MO0052  Rate of Change Negative
MO0053  Rate of Change Rising
MO0054  Rate of Change Falling
MO0055  Rate of Change Cross Above Zero
MO0056  Rate of Change Cross Below Zero
MO0057  Momentum Above Zero
MO0058  Momentum Below Zero
MO0059  Momentum Rising
MO0060  Momentum Falling
```

---

## Summary

| Field | Value |
|-------|-------|
| Category | Momentum |
| Code | MO |
| Total Rules | 60 |
| Rule Range | MO0001 – MO0060 |
| Status | Frozen v1.0 |

---

## Next Category

| Code | Name | Target |
|------|------|--------|
| VO | Volatility | 60 Rules |

---

## Notes

This catalog defines all Atomic Rules related to Momentum.

Each Rule represents one objective fact.

Composite logic, scoring, and investment decisions are **not** included.

These Rules are immutable after Freeze and become the official Momentum Rule Catalog for TASS.

---

## Implementation Status

| Rule ID | Status |
|---------|--------|
| MO0001–MO0060 | Implemented (engine/rules/) |

---

## Related Documents

* [TASS-011 Rule Taxonomy](TASS-011_Rule_Taxonomy_Specification.md)
* [TASS-012 Rule Specification Standard](TASS-012_Rule_Specification_Standard.md)
* [TASS-013 Rule Database](TASS-013_Rule_Database_Specification.md)
* [TASS-014 TR Rule Catalog](TASS-014_TR_Rule_Catalog_v1.0.md)
* [TASS-015 MA Rule Catalog](TASS-015_MA_Rule_Catalog_v1.0.md)
* [TASS-016 PA Rule Catalog](TASS-016_PA_Rule_Catalog_v1.0.md)
* [rules/catalog/MO_v1.0.yaml](../rules/catalog/MO_v1.0.yaml)

---

# End of Catalog

No new MO atomic IDs may be invented outside MO0001–MO0060 until catalog v2.0.
