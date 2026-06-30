# TASS Rule Catalog

# Category : Candlestick (CS)

# Version : 1.0

**Status:** Frozen v1.0

**Machine-readable:** [rules/catalog/CS_v1.0.yaml](../rules/catalog/CS_v1.0.yaml)

---

## Category Information

| Field | Value |
|-------|-------|
| Category Code | CS |
| Category Name | Candlestick |
| Status | Frozen v1.0 |
| Total Rules | 60 |
| Rule Range | CS0001 – CS0060 |

---

## Bullish Candlestick Patterns (CS0001–CS0010)

```text
CS0001  Hammer Formed
CS0002  Inverted Hammer Formed
CS0003  Bullish Marubozu Formed
CS0004  Bullish Engulfing Formed
CS0005  Piercing Line Formed
CS0006  Morning Star Formed
CS0007  Three White Soldiers Formed
CS0008  Bullish Harami Formed
CS0009  Bullish Belt Hold Formed
CS0010  Bullish Kicker Formed
```

---

## Bearish Candlestick Patterns (CS0011–CS0020)

```text
CS0011  Hanging Man Formed
CS0012  Shooting Star Formed
CS0013  Bearish Marubozu Formed
CS0014  Bearish Engulfing Formed
CS0015  Dark Cloud Cover Formed
CS0016  Evening Star Formed
CS0017  Three Black Crows Formed
CS0018  Bearish Harami Formed
CS0019  Bearish Belt Hold Formed
CS0020  Bearish Kicker Formed
```

---

## Reversal Candlestick Patterns (CS0021–CS0030)

```text
CS0021  Tweezer Bottom Formed
CS0022  Tweezer Top Formed
CS0023  Bullish Abandoned Baby Formed
CS0024  Bearish Abandoned Baby Formed
CS0025  Island Reversal Bottom Formed
CS0026  Island Reversal Top Formed
CS0027  Bullish Key Reversal Formed
CS0028  Bearish Key Reversal Formed
CS0029  Morning Doji Star Formed
CS0030  Evening Doji Star Formed
```

---

## Continuation Candlestick Patterns (CS0031–CS0040)

```text
CS0031  Rising Three Methods Formed
CS0032  Falling Three Methods Formed
CS0033  Bullish Mat Hold Formed
CS0034  Bearish Mat Hold Formed
CS0035  Upside Tasuki Gap Formed
CS0036  Downside Tasuki Gap Formed
CS0037  Bullish Side By Side White Lines Formed
CS0038  Bearish Side By Side White Lines Formed
CS0039  Bullish Separating Lines Formed
CS0040  Bearish Separating Lines Formed
```

---

## Doji & Indecision Patterns (CS0041–CS0050)

```text
CS0041  Standard Doji Formed
CS0042  Long Legged Doji Formed
CS0043  Dragonfly Doji Formed
CS0044  Gravestone Doji Formed
CS0045  Four Price Doji Formed
CS0046  Rickshaw Man Doji Formed
CS0047  Spinning Top Formed
CS0048  High Wave Candle Formed
CS0049  Doji Star Formed
CS0050  Double Doji Formed
```

---

## Candlestick Strength (CS0051–CS0060)

```text
CS0051  Strong Bullish Candle
CS0052  Strong Bearish Candle
CS0053  Body Larger Than N-Period Average
CS0054  Body Smaller Than N-Period Average
CS0055  Range Larger Than N-Period Average
CS0056  Range Smaller Than N-Period Average
CS0057  Body Dominates Candle Range
CS0058  Wick Dominates Candle Range
CS0059  Three Bullish Candles In Sequence
CS0060  Three Bearish Candles In Sequence
```

---

## Summary

| Field | Value |
|-------|-------|
| Category | Candlestick |
| Code | CS |
| Total Rules | 60 |
| Rule Range | CS0001 – CS0060 |
| Status | Frozen v1.0 |

---

## Next Category

| Code | Name | Target |
|------|------|--------|
| GP | Gap | 60 Rules |

---

## Notes

This catalog defines all Atomic Rules related to Candlestick.

Each Rule represents one objective fact.

Composite logic, scoring, and investment decisions are **not** included.

These Rules are immutable after Freeze and become the official Candlestick Rule Catalog for TASS.

---

## Implementation Status

| Rule ID | Status |
|---------|--------|
| CS0001–CS0060 | Implemented (engine/rules/) |

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
* [TASS-020 PT Rule Catalog](TASS-020_PT_Rule_Catalog_v1.0.md)
* [rules/catalog/CS_v1.0.yaml](../rules/catalog/CS_v1.0.yaml)

---

# End of Catalog

No new CS atomic IDs may be invented outside CS0001–CS0060 until catalog v2.0.
