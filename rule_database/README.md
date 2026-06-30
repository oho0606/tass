# TASS Rule Database

**SSOT** for all TASS Rules per [docs/TASS-013_Rule_Database_Specification.md](../docs/TASS-013_Rule_Database_Specification.md).

## Layout

| Path | Purpose |
|------|---------|
| `schema.sql` | SQLite table definitions |
| `tass_rules.db` | Runtime database (auto-seeded) |
| `rules/{RULE_ID}/` | Per-rule human + machine files |
| `categories/` | Category exports |
| `exports/` | JSON/CSV exports |

## Usage

```python
from engine.core.rule_database import get_rule_database

db = get_rule_database()
rule = db.get_rule("TR0001")
db.search(category_code="TR", status="Draft")
db.validate_rule("TR0001")
```

## Seed / rebuild

```bash
python scripts/seed_rule_database.py
```

## Principles

- One Rule → One Record → One Folder
- Immutable Rule IDs (`TR0001`, `TRC001`, `TRE001`)
- All changes recorded in `rule_history` (never deleted)
