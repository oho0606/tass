# TASS Rule Catalog

# Category : Volume (VL)

# Version : 1.0

**Status:** Frozen v1.0

**Machine-readable:** [rules/catalog/VL_v1.0.yaml](../rules/catalog/VL_v1.0.yaml)

---

## Category Information

| Field | Value |
|-------|-------|
| Category Code | VL |
| Category Name | Volume |
| Status | Frozen v1.0 |
| Total Rules | 60 |
| Rule Range | VL0001 – VL0060 |

---

## Absolute Volume (VL0001–VL0010)

```text
VL0001  Volume Above N-Period Average
VL0002  Volume Below N-Period Average
VL0003  Volume Equal N-Period Average
VL0004  Volume Above Prior Volume
VL0005  Volume Below Prior Volume
VL0006  Volume Equal Prior Volume
VL0007  Volume Above N-Period High
VL0008  Volume Below N-Period Low
VL0009  Volume At N-Period High
VL0010  Volume At N-Period Low
```

---

## Relative Volume (VL0011–VL0020)

```text
VL0011  Relative Volume Above 1
VL0012  Relative Volume Below 1
VL0013  Relative Volume Equal 1
VL0014  Relative Volume Above 2
VL0015  Relative Volume Above Threshold
VL0016  Relative Volume Below Threshold
VL0017  Relative Volume Above Prior
VL0018  Relative Volume Below Prior
VL0019  Relative Volume At N-Period Average
VL0020  Relative Volume At N-Period High
```

---

## Volume Trend (VL0021–VL0030)

```text
VL0021  Volume Rising
VL0022  Volume Falling
VL0023  Volume Slope Positive
VL0024  Volume Slope Negative
VL0025  Volume Slope Increasing
VL0026  Volume Slope Decreasing
VL0027  Consecutive Higher Volume
VL0028  Consecutive Lower Volume
VL0029  Volume Flat
VL0030  Volume Turning
```

---

## Volume Spike (VL0031–VL0040)

```text
VL0031  Volume Spike
VL0032  Volume Above Spike Threshold
VL0033  Volume Sudden Increase
VL0034  Volume Sudden Decrease
VL0035  Volume Expansion
VL0036  Volume Contraction
VL0037  Volume Climax
VL0038  Volume Dry Up
VL0039  Volume Spike Above Prior Spike
VL0040  Volume Spike Below Prior Spike
```

---

## Volume Confirmation (VL0041–VL0050)

```text
VL0041  Up Bar Volume Above Average
VL0042  Down Bar Volume Above Average
VL0043  Up Bar Volume Below Average
VL0044  Down Bar Volume Below Average
VL0045  Up Bar Volume Above Prior Up Bar
VL0046  Down Bar Volume Above Prior Down Bar
VL0047  Price Up Volume Up
VL0048  Price Down Volume Up
VL0049  Price Up Volume Down
VL0050  Price Down Volume Down
```

---

## Volume Quality (VL0051–VL0060)

```text
VL0051  OBV Rising
VL0052  OBV Falling
VL0053  OBV Above Prior OBV
VL0054  OBV Below Prior OBV
VL0055  OBV Slope Increasing
VL0056  OBV Slope Decreasing
VL0057  Money Flow Positive
VL0058  Money Flow Negative
VL0059  Volume Structure Stable
VL0060  Volume Pattern Consistent
```

---

## Summary

| Field | Value |
|-------|-------|
| Category | Volume |
| Code | VL |
| Total Rules | 60 |
| Rule Range | VL0001 – VL0060 |
| Status | Frozen v1.0 |

---

## Next Category

| Code | Name | Target |
|------|------|--------|
| MO | Momentum | 60 Rules |

---

## Notes

This catalog defines all Atomic Rules related to Volume.

Each Rule represents one objective fact.

Composite logic, scoring, and investment decisions are **not** included.

These Rules are immutable after Freeze and become the official Volume Rule Catalog for TASS.

---

## Implementation Status

| Rule ID | Status |
|---------|--------|
| VL0001–VL0060 | ✅ Implemented (`engine/rules/vl/`) |

---

## Related Documents

* [TASS-011 Rule Taxonomy](TASS-011_Rule_Taxonomy_Specification.md)
* [TASS-012 Rule Specification Standard](TASS-012_Rule_Specification_Standard.md)
* [TASS-013 Rule Database](TASS-013_Rule_Database_Specification.md)
* [TASS-014 TR Rule Catalog](TASS-014_TR_Rule_Catalog_v1.0.md)
* [TASS-015 MA Rule Catalog](TASS-015_MA_Rule_Catalog_v1.0.md)
* [TASS-016 PA Rule Catalog](TASS-016_PA_Rule_Catalog_v1.0.md)
* [rules/catalog/VL_v1.0.yaml](../rules/catalog/VL_v1.0.yaml)

---

# End of Catalog

No new VL atomic IDs may be invented outside VL0001–VL0060 until catalog v2.0.
