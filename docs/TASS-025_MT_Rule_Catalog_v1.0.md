# TASS Rule Catalog

# Category : Multi Timeframe (MT)

# Version : 1.0

**Status:** Frozen v1.0

**Machine-readable:** [rules/catalog/MT_v1.0.yaml](../rules/catalog/MT_v1.0.yaml)

---

## Category Information

| Field | Value |
|-------|-------|
| Category Code | MT |
| Category Name | Multi Timeframe |
| Status | Frozen v1.0 |
| Total Rules | 60 |
| Rule Range | MT0001 – MT0060 |

---

## Trend Alignment (MT0001–MT0010)

```text
MT0001  Weekly Daily Uptrend Match
MT0002  Weekly Daily Uptrend Conflict
MT0003  Weekly Daily Downtrend Match
MT0004  Weekly Daily Downtrend Conflict
MT0005  Daily 4H Uptrend Match
MT0006  Daily 4H Uptrend Conflict
MT0007  Daily 4H Downtrend Match
MT0008  Daily 4H Downtrend Conflict
MT0009  4H 1H Uptrend Match
MT0010  4H 1H Uptrend Conflict
```

---

## Moving Average Alignment (MT0011–MT0020)

```text
MT0011  Weekly Daily Price Above SMA20
MT0012  Weekly Daily Price Below SMA20
MT0013  Weekly Above SMA20 Daily Below SMA20
MT0014  Daily 4H Price Above SMA20
MT0015  Daily Above SMA20 4H Below SMA20
MT0016  Daily 4H Price Below SMA20
MT0017  Weekly Daily SMA Bullish Alignment
MT0018  Weekly Daily SMA Bearish Alignment
MT0019  Weekly Daily SMA Golden Cross
MT0020  Weekly Daily SMA Death Cross
```

---

## Momentum Alignment (MT0021–MT0030)

```text
MT0021  Weekly Daily RSI Above 50
MT0022  Weekly Daily RSI Below 50
MT0023  Weekly RSI Above 50 Daily Below 50
MT0024  Weekly Daily MACD Above Zero
MT0025  Weekly Daily MACD Below Zero
MT0026  Daily 4H MACD Above Signal
MT0027  Daily 4H MACD Below Signal
MT0028  Weekly Daily RSI Rising
MT0029  Weekly Daily RSI Falling
MT0030  Daily 4H Stochastic Above 50
```

---

## Breakout Alignment (MT0031–MT0040)

```text
MT0031  Weekly Daily Close Above N-Period High
MT0032  Weekly Daily Close Below N-Period Low
MT0033  Weekly Daily Swing High Break
MT0034  Weekly Daily Swing Low Break
MT0035  Weekly Daily Resistance Break
MT0036  Weekly Daily Support Break
MT0037  Daily 4H Breakout Above Range
MT0038  Daily 4H Breakout Below Range
MT0039  Weekly Breakout Confirmed By Daily Close
MT0040  Daily Breakout Rejected By Weekly Close
```

---

## Timeframe Agreement (MT0041–MT0050)

```text
MT0041  Weekly Daily 4H Trend Match
MT0042  Weekly Daily 4H Trend Conflict
MT0043  Daily 4H 1H Trend Match
MT0044  Daily 4H 1H Trend Conflict
MT0045  Higher Timeframe Trend Matches Lower Timeframe
MT0046  Higher Timeframe Trend Opposes Lower Timeframe
MT0047  Primary Secondary Uptrend Match
MT0048  Primary Uptrend Secondary Downtrend
MT0049  Primary Secondary Downtrend Match
MT0050  Primary Downtrend Secondary Uptrend
```

---

## Multi Timeframe Quality (MT0051–MT0060)

```text
MT0051  Weekly Trend Supports Daily Trend
MT0052  Weekly Trend Opposes Daily Trend
MT0053  Higher Timeframe Range Contains Lower Timeframe
MT0054  Lower Timeframe Range Extends Beyond Higher Timeframe
MT0055  Multi Timeframe Higher High Match
MT0056  Multi Timeframe Lower Low Match
MT0057  Multi Timeframe Volume Expansion Match
MT0058  Multi Timeframe Volume Contraction Match
MT0059  Multi Timeframe Bars Synchronized
MT0060  Multi Timeframe Bars Desynchronized
```

---

## Summary

| Field | Value |
|-------|-------|
| Category | Multi Timeframe |
| Code | MT |
| Total Rules | 60 |
| Rule Range | MT0001 – MT0060 |
| Status | Frozen v1.0 |

---

## Next Category

| Code | Name | Target |
|------|------|--------|
| CF | Confirmation | 60 Rules |

---

## Notes

This catalog defines all Atomic Rules related to Multi Timeframe.

Each Rule represents one objective fact.

Composite logic, scoring, and investment decisions are **not** included.

These Rules are immutable after Freeze and become the official Multi Timeframe Rule Catalog for TASS.

---

## Implementation Status

| Rule ID | Status |
|---------|--------|
| MT0001–MT0060 | Implemented (engine/rules/) |

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
* [TASS-024 MR Rule Catalog](TASS-024_MR_Rule_Catalog_v1.0.md)
* [rules/catalog/MT_v1.0.yaml](../rules/catalog/MT_v1.0.yaml)

---

# End of Catalog

No new MT atomic IDs may be invented outside MT0001–MT0060 until catalog v2.0.
