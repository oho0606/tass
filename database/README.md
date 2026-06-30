# Database

| Artifact | Path | Purpose |
|----------|------|---------|
| Rule DB schema | `rule_database/schema.sql` | TASS-013 SSOT tables |
| Rule DB file | `rule_database/tass_rules.db` | SQLite (auto-seeded) |
| Rule folders | `rule_database/rules/{RULE_ID}/` | Per-rule human + machine SSOT |
| Python API | `engine.core.rule_database` | Query, lifecycle, validation |
| MVP manifest | `config/mvp_operational_rules.yaml` | 26 production MVP rules |
| SSOT scripts | `scripts/retrofill_mvp_rule_ssot.py`, `scripts/verify_rule_ssot.py` | Retrofill + 3-way verify |
| Ops persistence | Alembic `daily_picks` table | Scaffold only — picks JSON is primary (v1.0-rc1) |

Specification: [docs/TASS-013_Rule_Database_Specification.md](../docs/TASS-013_Rule_Database_Specification.md)

Future (v2.0): PostgreSQL-backed picks history, backtest results persistence.
