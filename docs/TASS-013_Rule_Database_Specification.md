# TASS-013 : Rule Database Specification

**Version:** v1.0.0

**Status:** Standard

---

# 1. Purpose

The Rule Database is the **single source of truth (SSOT)** for every Rule in TASS.

Every Rule MUST exist in the Rule Database before implementation.

Every Engine, AI Agent, Backtest, Explainability Module, and Registry MUST reference this database.

Related: [TASS-011](TASS-011_Rule_Taxonomy_Specification.md) | [TASS-012](TASS-012_Rule_Specification_Standard.md)

---

# 2. Design Principles

- Single Source of Truth
- Normalized Structure
- Immutable Rule IDs
- Version Controlled
- Machine Readable + Human Readable
- Fully Explainable
- Backtest Driven
- AI Friendly

---

# 3. Database Architecture

```text
Rule Database
├── Categories
├── Subcategories
├── Rules
├── Rule Versions
├── Rule Parameters
├── Rule Inputs
├── Rule Outputs
├── Rule Dependencies
├── Rule Tags
├── Rule Tests
├── Rule Backtests
├── Rule Performance
├── Rule Lifecycle
└── Rule History
```

---

# 4. Storage Layout

```text
rule_database/
├── README.md
├── schema.sql
├── tass_rules.db          # SQLite SSOT (generated)
├── categories/
├── rules/
│   ├── TR0001/
│   │   ├── specification.md
│   │   ├── metadata.json
│   │   ├── parameters.json
│   │   ├── README.md
│   │   └── changelog.md
│   └── ...
├── versions/
├── tests/
├── backtests/
├── performance/
├── history/
└── exports/
```

---

# 5. Python API

Module: `engine.core.rule_database`

```python
from engine.core.rule_database import get_rule_database

db = get_rule_database()
rule = db.get_rule("TR0001")           # O(1) lookup
results = db.search(status="Draft")    # indexed search
db.validate_rule("TR0001")             # metadata + deps check
```

---

# 6. Validation Rules

The database MUST reject:

- Duplicate Rule IDs / Versions
- Missing Metadata, Category, Subcategory
- Invalid or circular dependencies
- Invalid weight or version format

---

# 7. AI Integration Rules

Every AI Agent MUST:

1. Read Rule Database first (`skills/read_project_spec` → `get_rule_database()`)
2. Never create duplicate Rules
3. Always update Rule History on change
4. Always validate dependencies

---

# 8. Explainability Support

Every Rule MUST expose: Why PASS/FAIL, input values, calculated values, thresholds, parameters, decision path.

---

# End of Specification

All Rule management MUST comply with TASS-013.
