# TASS Rule Catalog

# Category : Trend (TR)

# Version : 1.0

**Status:** Frozen v1.0

**Machine-readable:** [rules/catalog/TR_v1.0.yaml](../rules/catalog/TR_v1.0.yaml)

---

## Trend Direction

```text
TR0001  Higher High
TR0002  Higher Low
TR0003  Lower High
TR0004  Lower Low
TR0005  Uptrend
TR0006  Downtrend
TR0007  Sideways Trend
TR0008  Trend Reversal Up
TR0009  Trend Reversal Down
TR0010  Trend Continuation
```

---

## Trend Strength

```text
TR0011  Strong Uptrend
TR0012  Weak Uptrend
TR0013  Strong Downtrend
TR0014  Weak Downtrend
TR0015  ADX Rising
TR0016  ADX Falling
TR0017  ADX Above Threshold
TR0018  ADX Below Threshold
TR0019  Trend Momentum Increasing
TR0020  Trend Momentum Decreasing
```

---

## Trend Quality

```text
TR0021  Clean Uptrend
TR0022  Clean Downtrend
TR0023  Choppy Trend
TR0024  Smooth Trend
TR0025  Noisy Trend
TR0026  Stable Trend
TR0027  Unstable Trend
TR0028  Trend Consistency High
TR0029  Trend Consistency Low
TR0030  Trend Integrity
```

---

## Trend Slope

```text
TR0031  Positive Slope
TR0032  Negative Slope
TR0033  Flat Slope
TR0034  Increasing Slope
TR0035  Decreasing Slope
TR0036  Accelerating Trend
TR0037  Decelerating Trend
TR0038  Slope Breakout
TR0039  Slope Reversal
TR0040  Slope Stability
```

---

## Trend Persistence

```text
TR0041  Consecutive Higher Highs
TR0042  Consecutive Higher Lows
TR0043  Consecutive Lower Highs
TR0044  Consecutive Lower Lows
TR0045  Trend Persistence High
TR0046  Trend Persistence Low
TR0047  Trend Duration Short
TR0048  Trend Duration Medium
TR0049  Trend Duration Long
TR0050  Trend Age Increasing
```

---

## Trend Exhaustion

```text
TR0051  Trend Exhaustion Up
TR0052  Trend Exhaustion Down
TR0053  Buying Exhaustion
TR0054  Selling Exhaustion
TR0055  Trend Climax
TR0056  Trend Weakening
TR0057  Trend Failure
TR0058  Failed Trend Continuation
TR0059  Failed Trend Reversal
TR0060  Exhaustion Recovery
```

---

## Trend Confirmation

```text
TR0061  Price Confirms Trend
TR0062  Volume Confirms Trend
TR0063  Momentum Confirms Trend
TR0064  Volatility Confirms Trend
TR0065  Multi Indicator Confirmation
TR0066  Multi Timeframe Confirmation
TR0067  Trend Confirmation Strong
TR0068  Trend Confirmation Weak
TR0069  Trend Confirmation Lost
TR0070  Trend Confirmation Restored
```

---

## Trend State

```text
TR0071  Trend Established
TR0072  Trend Emerging
TR0073  Trend Maturing
TR0074  Trend Ending
TR0075  Trend Restarting
TR0076  Bull Trend State
TR0077  Bear Trend State
TR0078  Neutral Trend State
TR0079  Trend Transition
TR0080  Trend Undefined
```

---

## Summary

| Field | Value |
|-------|-------|
| Total Rules | 80 |
| Status | Frozen v1.0 |
| Next Category | MA (Moving Average) |

---

## Implementation Status

| Rule ID | Status | Notes |
|---------|--------|-------|
| TR0001 | Implemented | Class-based (`TR0001HigherHighRule`) |
| TR0002–TR0004 | Draft | Functional MVP implementations |
| TR0005–TR0080 | Frozen | Catalog only — no implementation yet |
| TRC001–TRC004 | Draft | Composite rules (separate ID space) |
| TRE001 | Stable | Trend domain engine |

Composite (`TRC*`) and engine (`TRE*`) rules are **not** part of the 80-rule atomic catalog.

---

## Related Documents

* [TASS-011 Rule Taxonomy](TASS-011_Rule_Taxonomy_Specification.md)
* [TASS-012 Rule Specification Standard](TASS-012_Rule_Specification_Standard.md)
* [TASS-013 Rule Database](TASS-013_Rule_Database_Specification.md)
* [rules/registry.yaml](../rules/registry.yaml)
* [rules/catalog/TR_v1.0.yaml](../rules/catalog/TR_v1.0.yaml)

---

# End of Catalog

This document is the official frozen Rule Catalog for Trend (TR) category v1.0.

All new TR atomic rules **MUST** use an ID from this catalog. No new TR atomic IDs may be invented outside TR0001–TR0080 until catalog v2.0.
