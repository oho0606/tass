# TASS Rule Catalog



# Category : Confirmation (CF)



# Version : 1.0



**Status:** Frozen v1.0



**Machine-readable:** [rules/catalog/CF_v1.0.yaml](../rules/catalog/CF_v1.0.yaml)



---



## Category Information



| Field | Value |

|-------|-------|

| Category Code | CF |

| Category Name | Confirmation |

| Status | Frozen v1.0 |

| Total Rules | 60 |

| Rule Range | CF0001 – CF0060 |



---



## Trend Confirmation (CF0001–CF0010)



```text

CF0001  Close Confirms Bullish Trend

CF0002  Close Confirms Bearish Trend

CF0003  SMA20 Confirms Bullish Trend

CF0004  SMA20 Confirms Bearish Trend

CF0005  EMA20 Confirms Bullish Trend

CF0006  EMA20 Confirms Bearish Trend

CF0007  SMA Alignment Confirms Bullish Trend

CF0008  SMA Alignment Confirms Bearish Trend

CF0009  Higher High Confirms Bullish Trend

CF0010  Lower Low Confirms Bearish Trend

```



---



## Volume Confirmation (CF0011–CF0020)



```text

CF0011  Volume Confirms Bullish Trend

CF0012  Volume Confirms Bearish Trend

CF0013  Up Bar Volume Confirms Uptrend

CF0014  Down Bar Volume Confirms Downtrend

CF0015  OBV Rising Confirms Bullish Trend

CF0016  OBV Falling Confirms Bearish Trend

CF0017  Volume Above Average Confirms Bullish Trend

CF0018  Volume Above Average Confirms Bearish Trend

CF0019  Volume Spike Confirms Bullish Trend

CF0020  Volume Spike Confirms Bearish Trend

```



---



## Momentum Confirmation (CF0021–CF0030)



```text

CF0021  RSI Confirms Bullish Trend

CF0022  RSI Confirms Bearish Trend

CF0023  MACD Confirms Bullish Trend

CF0024  MACD Confirms Bearish Trend

CF0025  Stochastic Confirms Bullish Trend

CF0026  Stochastic Confirms Bearish Trend

CF0027  CCI Confirms Bullish Trend

CF0028  CCI Confirms Bearish Trend

CF0029  Rate Of Change Confirms Bullish Trend

CF0030  Rate Of Change Confirms Bearish Trend

```



---



## Volatility Confirmation (CF0031–CF0040)



```text

CF0031  ATR Rising Confirms Bullish Trend

CF0032  ATR Rising Confirms Bearish Trend

CF0033  Bollinger Band Width Expanding Confirms Breakout

CF0034  Bollinger Band Width Contracting Confirms Consolidation

CF0035  Volatility Above Average Confirms Bullish Trend

CF0036  Volatility Above Average Confirms Bearish Trend

CF0037  True Range Above Average Confirms Bullish Trend

CF0038  True Range Above Average Confirms Bearish Trend

CF0039  Historical Volatility Rising Confirms Bullish Trend

CF0040  Historical Volatility Rising Confirms Bearish Trend

```



---



## Multi-Indicator Confirmation (CF0041–CF0050)



```text

CF0041  Price And Volume Agreement

CF0042  Price And Momentum Agreement

CF0043  Price And Volatility Agreement

CF0044  Trend And Volume Agreement

CF0045  Trend And Momentum Agreement

CF0046  Trend And Volatility Agreement

CF0047  Momentum And Volume Agreement

CF0048  MACD And RSI Agreement

CF0049  SMA And EMA Agreement

CF0050  Multi Indicator Agreement

```



---



## Confirmation Quality (CF0051–CF0060)



```text

CF0051  Confirmation Present

CF0052  Confirmation Absent

CF0053  Confirmation Sustained

CF0054  Confirmation Lost

CF0055  Confirmation Restored

CF0056  Confirmation Increasing

CF0057  Confirmation Decreasing

CF0058  Confirmation Duration Long

CF0059  Confirmation Duration Short

CF0060  Confirmation Structure Stable

```



---



## Summary



| Field | Value |

|-------|-------|

| Category | Confirmation |

| Code | CF |

| Total Rules | 60 |

| Rule Range | CF0001 – CF0060 |

| Status | Frozen v1.0 |



---



## Next Category



| Code | Name | Target |

|------|------|--------|

| DQ | Data Quality | 60 Rules |



---



## Notes



This catalog defines all Atomic Rules related to Confirmation.



Each Rule represents one objective fact.



Composite logic, scoring, and investment decisions are **not** included.



These Rules are immutable after Freeze and become the official Confirmation Rule Catalog for TASS.



---



## Implementation Status



| Rule ID | Status |

|---------|--------|

| CF0001–CF0060 | Implemented (engine/rules/) |



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

* [rules/catalog/CF_v1.0.yaml](../rules/catalog/CF_v1.0.yaml)



---



# End of Catalog



No new CF atomic IDs may be invented outside CF0001–CF0060 until catalog v2.0.

