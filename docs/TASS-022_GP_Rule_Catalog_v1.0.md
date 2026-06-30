# TASS Rule Catalog

# Category : Gap (GP)

# Version : 1.0

**Status:** Frozen v1.0

**Machine-readable:** [rules/catalog/GP_v1.0.yaml](../rules/catalog/GP_v1.0.yaml)

---

## Category Information

| Field | Value |
|-------|-------|
| Category Code | GP |
| Category Name | Gap |
| Status | Frozen v1.0 |
| Total Rules | 60 |
| Rule Range | GP0001 – GP0060 |

---

## Gap Up (GP0001–GP0010)

```text
GP0001  Gap Up Open Above Prior High
GP0002  Gap Up Open Above Prior Close
GP0003  Gap Up Low Above Prior High
GP0004  Gap Up Low Above Prior Close
GP0005  Gap Up Close Above Prior High
GP0006  Gap Up Close Above Prior Close
GP0007  Gap Up Range Larger Than Prior Range
GP0008  Gap Up Size Larger Than Prior Range
GP0009  Gap Up Bar Bullish
GP0010  Consecutive Gap Up Day
```

---

## Gap Down (GP0011–GP0020)

```text
GP0011  Gap Down Open Below Prior Low
GP0012  Gap Down Open Below Prior Close
GP0013  Gap Down High Below Prior Low
GP0014  Gap Down High Below Prior Close
GP0015  Gap Down Close Below Prior Low
GP0016  Gap Down Close Below Prior Close
GP0017  Gap Down Range Larger Than Prior Range
GP0018  Gap Down Size Larger Than Prior Range
GP0019  Gap Down Bar Bearish
GP0020  Consecutive Gap Down Day
```

---

## Breakaway Gap (GP0021–GP0030)

```text
GP0021  Breakaway Gap Up Open Above N-Period High
GP0022  Breakaway Gap Up Low Above N-Period High
GP0023  Breakaway Gap Down Open Below N-Period Low
GP0024  Breakaway Gap Down High Below N-Period Low
GP0025  Breakaway Gap Up Open Outside N-Period Range
GP0026  Breakaway Gap Down Open Outside N-Period Range
GP0027  Breakaway Gap Up Size Exceeds N-Period Average Range
GP0028  Breakaway Gap Down Size Exceeds N-Period Average Range
GP0029  Breakaway Gap Up Volume Above N-Period Average
GP0030  Breakaway Gap Down Volume Above N-Period Average
```

---

## Continuation (Runaway) Gap (GP0031–GP0040)

```text
GP0031  Continuation Gap Up Low Above Prior High
GP0032  Continuation Gap Up Unfilled At Close
GP0033  Continuation Gap Up Bar Bullish
GP0034  Continuation Gap Up Size Below N-Period Average Gap
GP0035  Continuation Gap Up After Higher Close
GP0036  Continuation Gap Down High Below Prior Low
GP0037  Continuation Gap Down Unfilled At Close
GP0038  Continuation Gap Down Bar Bearish
GP0039  Continuation Gap Down Size Below N-Period Average Gap
GP0040  Continuation Gap Down After Lower Close
```

---

## Exhaustion Gap (GP0041–GP0050)

```text
GP0041  Exhaustion Gap Up Open Above Prior High
GP0042  Exhaustion Gap Up Filled Intraday
GP0043  Exhaustion Gap Up Bar Bearish
GP0044  Exhaustion Gap Up At N-Period High
GP0045  Exhaustion Gap Up Size Exceeds N-Period Average Gap
GP0046  Exhaustion Gap Down Open Below Prior Low
GP0047  Exhaustion Gap Down Filled Intraday
GP0048  Exhaustion Gap Down Bar Bullish
GP0049  Exhaustion Gap Down At N-Period Low
GP0050  Exhaustion Gap Down Size Exceeds N-Period Average Gap
```

---

## Gap Quality (GP0051–GP0060)

```text
GP0051  Gap Size Above N-Period Average
GP0052  Gap Size Below N-Period Average
GP0053  Gap Size Exceeds Prior Gap Size
GP0054  Gap Size Below Prior Gap Size
GP0055  Gap Unfilled At Close
GP0056  Gap Filled Intraday
GP0057  Gap Partially Filled Intraday
GP0058  Gap Volume Above N-Period Average
GP0059  Gap Volume Below N-Period Average
GP0060  Gap Range Above N-Period Average
```

---

## Summary

| Field | Value |
|-------|-------|
| Category | Gap |
| Code | GP |
| Total Rules | 60 |
| Rule Range | GP0001 – GP0060 |
| Status | Frozen v1.0 |

---

## Next Category

| Code | Name | Target |
|------|------|--------|
| RK | Risk | 60 Rules |

---

## Notes

This catalog defines all Atomic Rules related to Gap.

Each Rule represents one objective fact.

Composite logic, scoring, and investment decisions are **not** included.

These Rules are immutable after Freeze and become the official Gap Rule Catalog for TASS.

---

## Implementation Status

| Rule ID | Status |
|---------|--------|
| GP0001–GP0060 | Implemented (engine/rules/) |

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
* [rules/catalog/GP_v1.0.yaml](../rules/catalog/GP_v1.0.yaml)

---

# End of Catalog

No new GP atomic IDs may be invented outside GP0001–GP0060 until catalog v2.0.
