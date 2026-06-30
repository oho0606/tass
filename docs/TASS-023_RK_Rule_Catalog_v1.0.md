# TASS Rule Catalog

# Category : Risk (RK)

# Version : 1.0

**Status:** Frozen v1.0

**Machine-readable:** [rules/catalog/RK_v1.0.yaml](../rules/catalog/RK_v1.0.yaml)

---

## Category Information

| Field | Value |
|-------|-------|
| Category Code | RK |
| Category Name | Risk |
| Status | Frozen v1.0 |
| Total Rules | 60 |
| Rule Range | RK0001 – RK0060 |

---

## ATR Risk (RK0001–RK0010)

```text
RK0001  ATR Above 20-Period Average
RK0002  ATR Below 20-Period Average
RK0003  ATR Rising
RK0004  ATR Falling
RK0005  ATR At 20-Period High
RK0006  ATR At 20-Period Low
RK0007  ATR Expanding
RK0008  ATR Contracting
RK0009  True Range Above ATR
RK0010  True Range Below ATR
```

---

## Volatility Risk (RK0011–RK0020)

```text
RK0011  Historical Volatility Above 20-Period Average
RK0012  Historical Volatility Below 20-Period Average
RK0013  Historical Volatility Rising
RK0014  Historical Volatility Falling
RK0015  Bollinger Band Width Expanding
RK0016  Bollinger Band Width Contracting
RK0017  Daily Range Above 20-Period Average
RK0018  Daily Range Below 20-Period Average
RK0019  Close-To-Close Volatility Above 20-Period Average
RK0020  High-Low Volatility Above 20-Period Average
```

---

## Gap Risk (RK0021–RK0030)

```text
RK0021  Overnight Gap Up Present
RK0022  Overnight Gap Down Present
RK0023  Gap Size Above ATR
RK0024  Gap Size Below ATR
RK0025  Unfilled Gap Up Present
RK0026  Unfilled Gap Down Present
RK0027  Gap Up Filled Same Session
RK0028  Gap Down Filled Same Session
RK0029  Gap Up From Prior High
RK0030  Gap Down From Prior Low
```

---

## Liquidity Risk (RK0031–RK0040)

```text
RK0031  Volume Below 20-Period Average
RK0032  Volume Above 20-Period Average
RK0033  Bid-Ask Spread Above 20-Period Average
RK0034  Bid-Ask Spread Below 20-Period Average
RK0035  Turnover Below 20-Period Average
RK0036  Turnover Above 20-Period Average
RK0037  Volume Declining
RK0038  Volume Increasing
RK0039  Dollar Volume Below 20-Period Average
RK0040  Dollar Volume Above 20-Period Average
```

---

## Drawdown Risk (RK0041–RK0050)

```text
RK0041  Price Below 20-Period High
RK0042  Price At 20-Period Low
RK0043  Current Drawdown Above 10 Percent
RK0044  Current Drawdown Below 10 Percent
RK0045  New 20-Period Low Made
RK0046  New 20-Period High Made
RK0047  Drawdown Increasing
RK0048  Drawdown Decreasing
RK0049  Price Underwater From Peak
RK0050  Price Above Prior Peak
```

---

## Overall Risk Quality (RK0051–RK0060)

```text
RK0051  ATR Near 20-Period Average
RK0052  ATR Extended Above 20-Period Average
RK0053  ATR Extended Below 20-Period Average
RK0054  Volatility Near 20-Period Average
RK0055  Volatility Extended Above 20-Period Average
RK0056  Volatility Extended Below 20-Period Average
RK0057  Volume Near 20-Period Average
RK0058  Drawdown Near 20-Period Average
RK0059  Gap Frequency Above 20-Period Average
RK0060  Risk Structure Stable
```

---

## Summary

| Field | Value |
|-------|-------|
| Category | Risk |
| Code | RK |
| Total Rules | 60 |
| Rule Range | RK0001 – RK0060 |
| Status | Frozen v1.0 |

---

## Next Category

| Code | Name | Target |
|------|------|--------|
| EN | Entry | 60 Rules |

---

## Notes

This catalog defines all Atomic Rules related to Risk.

Each Rule represents one objective fact.

Composite logic, scoring, and investment decisions are **not** included.

These Rules are immutable after Freeze and become the official Risk Rule Catalog for TASS.

---

## Implementation Status

| Rule ID | Status |
|---------|--------|
| RK0001–RK0060 | Implemented (engine/rules/) |

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
* [TASS-021 CS Rule Catalog](TASS-021_CS_Rule_Catalog_v1.0.md)
* [TASS-022 GP Rule Catalog](TASS-022_GP_Rule_Catalog_v1.0.md)
* [rules/catalog/RK_v1.0.yaml](../rules/catalog/RK_v1.0.yaml)

---

# End of Catalog

No new RK atomic IDs may be invented outside RK0001–RK0060 until catalog v2.0.
