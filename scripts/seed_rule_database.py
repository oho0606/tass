#!/usr/bin/env python3
"""Seed or rebuild the TASS Rule Database from registry.yaml."""

from __future__ import annotations

import argparse
from pathlib import Path

from engine.core.rule_database import DB_PATH, RuleDatabase


def main() -> int:
  parser = argparse.ArgumentParser(description="Seed TASS Rule Database")
  parser.add_argument("--rebuild", action="store_true", help="Delete and recreate database")
  args = parser.parse_args()

  if args.rebuild and DB_PATH.exists():
    DB_PATH.unlink()

  db = RuleDatabase()
  if args.rebuild or not DB_PATH.exists():
    db._init_schema()
  db.seed_from_registry()
  count = len(db.all_rules())
  print(f"Rule Database seeded: {count} rules at {DB_PATH}")
  db.close()
  return 0


if __name__ == "__main__":
  raise SystemExit(main())
