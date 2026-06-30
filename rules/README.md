# rules

Rule specifications live here.

**Official taxonomy:** [docs/TASS-011_Rule_Taxonomy_Specification.md](../docs/TASS-011_Rule_Taxonomy_Specification.md)

**Registry:** [registry.yaml](registry.yaml) (seed) · **Catalog:** [catalog/TR_v1.0.yaml](catalog/TR_v1.0.yaml) · [catalog/MA_v1.0.yaml](catalog/MA_v1.0.yaml) (frozen) · **Database:** [rule_database/](../rule_database/) (SSOT)

**Structure:** [RULE_STRUCTURE.md](RULE_STRUCTURE.md)

Every Rule must:

- Belong to exactly one category (two-letter code: TR, MA, VL, …)
- Have a unique Rule ID (`TR-001`, `MA-001`, `TR-C001`, `TR-E001`)
- Be registered in `registry.yaml`
- Follow [RULE-000_RULE_TEMPLATE.md](RULE-000_RULE_TEMPLATE.md)

Rules are the core of TASS. Code must implement Rules, not replace them.

No Rule is valid until it is measurable, implementable, backtestable, and explainable.

## Directories by category

| Code | Path |
|------|------|
| TR | [tr/](tr/) |
| (future) | ma/, vl/, mo/, … |

Legacy `rules/trend/` is deprecated; use `rules/tr/`.
