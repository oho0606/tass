# Rule Catalogs

Frozen rule ID catalogs per category. Atomic catalogs define official atomic rule IDs; the composite library defines official composite rule IDs.

## Atomic Rule Catalogs

| Catalog | Version | Rules | Status |
|---------|---------|-------|--------|
| [TR_v1.0.yaml](TR_v1.0.yaml) | 1.0 | 80 (TR0001–TR0080) | Frozen |
| [MA_v1.0.yaml](MA_v1.0.yaml) | 1.0 | 60 (MA0001–MA0060) | Frozen |
| [PA_v1.0.yaml](PA_v1.0.yaml) | 1.0 | 60 (PA0001–PA0060) | Frozen |
| [VL_v1.0.yaml](VL_v1.0.yaml) | 1.0 | 60 (VL0001–VL0060) | Frozen |
| [MO_v1.0.yaml](MO_v1.0.yaml) | 1.0 | 60 (MO0001–MO0060) | Frozen |
| [VO_v1.0.yaml](VO_v1.0.yaml) | 1.0 | 60 (VO0001–VO0060) | Frozen |
| [MS_v1.0.yaml](MS_v1.0.yaml) | 1.0 | 60 (MS0001–MS0060) | Frozen |
| [SR_v1.0.yaml](SR_v1.0.yaml) | 1.0 | 60 (SR0001–SR0060) | Frozen |
| [PB_v1.0.yaml](PB_v1.0.yaml) | 1.0 | 60 (PB0001–PB0060) | Frozen |
| [BO_v1.0.yaml](BO_v1.0.yaml) | 1.0 | 60 (BO0001–BO0060) | Frozen |
| [PT_v1.0.yaml](PT_v1.0.yaml) | 1.0 | 60 (PT0001–PT0060) | Frozen |
| [GP_v1.0.yaml](GP_v1.0.yaml) | 1.0 | 60 (GP0001–GP0060) | Frozen |
| [EN_v1.0.yaml](EN_v1.0.yaml) | 1.0 | 60 (EN0001–EN0060) | Frozen |
| [RK_v1.0.yaml](RK_v1.0.yaml) | 1.0 | 60 (RK0001–RK0060) | Frozen |
| [MR_v1.0.yaml](MR_v1.0.yaml) | 1.0 | 60 (MR0001–MR0060) | Frozen |
| [MT_v1.0.yaml](MT_v1.0.yaml) | 1.0 | 60 (MT0001–MT0060) | Frozen |
| [CF_v1.0.yaml](CF_v1.0.yaml) | 1.0 | 60 (CF0001–CF0060) | Frozen |
| [DQ_v1.0.yaml](DQ_v1.0.yaml) | 1.0 | 60 (DQ0001–DQ0060) | Frozen |

## Composite Rule Library

| Catalog | Version | Rules | Status |
|---------|---------|-------|--------|
| [Composite_v1.0.yaml](Composite_v1.0.yaml) | 1.0 | 130 (CTR001–CDQ002) | Frozen |

Human-readable: [TASS-027 Composite Rule Library](../docs/TASS-027_Composite_Rule_Library_v1.0.md)

Atomic catalogs — human docs: [TASS-014 TR](../docs/TASS-014_TR_Rule_Catalog_v1.0.md) · [TASS-015 MA](../docs/TASS-015_MA_Rule_Catalog_v1.0.md) · … · [TASS-026 DQ](../docs/TASS-026_DQ_Rule_Catalog_v1.0.md)

Catalogs are loaded into the Rule Database on seed. Entries in `rules/registry.yaml` override catalog defaults when both define the same rule ID.
