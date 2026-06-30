# TR — Trend Rules

Category code: **TR** (Trend)

| Document | Purpose |
|----------|---------|
| [TASS-014 TR Catalog v1.0](../../docs/TASS-014_TR_Rule_Catalog_v1.0.md) | **Frozen** 80 atomic rules (TR0001–TR0080) |
| [TR_v1.0.yaml](../catalog/TR_v1.0.yaml) | Machine-readable catalog |
| [TASS-011 Taxonomy](../../docs/TASS-011_Rule_Taxonomy_Specification.md) | Category structure |
| [registry.yaml](../registry.yaml) | Implementation registry |

## Atomic Catalog (80 rules — Frozen v1.0)

| Subcategory | Rule IDs | Count |
|-------------|----------|-------|
| Direction | TR0001–TR0010 | 10 |
| Strength | TR0011–TR0020 | 10 |
| Quality | TR0021–TR0030 | 10 |
| Slope | TR0031–TR0040 | 10 |
| Persistence | TR0041–TR0050 | 10 |
| Exhaustion | TR0051–TR0060 | 10 |
| Confirmation | TR0061–TR0070 | 10 |
| State | TR0071–TR0080 | 10 |

## Implementation Status

| Rule ID | Status | Name |
|---------|--------|------|
| TR0001 | Implemented | Higher High |
| TR0002 | Draft | Higher Low |
| TR0003 | Draft | Lower High |
| TR0004 | Draft | Lower Low |
| TR0005–TR0080 | Frozen | Catalog only |
| TRC001 | Draft | Trend Structure (composite) |
| TRC002 | Draft | Trend Quality (composite) |
| TRC003 | Draft | Trend Continuation (composite) |
| TRC004 | Draft | Trend Failure (composite) |
| TRE001 | Stable | Trend Engine |

Composite (`TRC*`) and engine (`TRE*`) rules use a separate ID space and are not part of the 80-rule atomic catalog.

## Legacy IDs

`TREND-*` and `TR-*` hyphen forms are deprecated aliases. Use canonical IDs (`TR0001`, `TRC001`, `TRE001`).
