"""Shared pytest fixtures for TASS."""

from __future__ import annotations

import pytest

import engine.core.rule_database as rule_db_mod
import engine.core.rule_registry as rule_registry_mod


@pytest.fixture(autouse=True)
def isolated_rule_database(tmp_path, monkeypatch):
  """Each test gets a fresh SQLite rule database seeded from registry.yaml."""
  db_path = tmp_path / "tass_rules.db"
  monkeypatch.setattr(rule_db_mod, "DB_PATH", db_path)
  if rule_db_mod._default_db is not None:
    rule_db_mod._default_db.close()
  rule_db_mod._default_db = None
  rule_registry_mod._default_registry = None
  yield
  if rule_db_mod._default_db is not None:
    rule_db_mod._default_db.close()
  rule_db_mod._default_db = None
  rule_registry_mod._default_registry = None
