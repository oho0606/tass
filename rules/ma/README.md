# MA — Moving Average Rules

Category code: **MA** (Moving Average)

| Document | Purpose |
|----------|---------|
| [TASS-015 MA Catalog v1.0](../../docs/TASS-015_MA_Rule_Catalog_v1.0.md) | **Frozen** 60 atomic rules (MA0001–MA0060) |
| [MA_v1.0.yaml](../catalog/MA_v1.0.yaml) | Machine-readable catalog |
| [TASS-011 Taxonomy](../../docs/TASS-011_Rule_Taxonomy_Specification.md) | Category structure |

## Atomic Catalog (60 rules — Frozen v1.0)

| Subcategory | Rule IDs | Count |
|-------------|----------|-------|
| Price Position | MA0001–MA0010 | 10 |
| EMA Position | MA0011–MA0020 | 10 |
| Alignment | MA0021–MA0030 | 10 |
| Crossovers | MA0031–MA0040 | 10 |
| Slope | MA0041–MA0050 | 10 |
| Distance & Structure | MA0051–MA0060 | 10 |

## Implementation Status

| Rule ID | Status |
|---------|--------|
| MA0001–MA0060 | ✅ Implemented (`engine/rules/ma/`) |

Domain engine MVP subset: see `engine/rules/ma/registry.py` (`MA_ENGINE_RULES`).
