from engine.core.rule_database import get_rule_database
from engine.core.rule_registry import get_registry


def test_rule_database_has_tr_rules():
  db = get_rule_database()
  assert db.get_rule("TR0001") is not None
  assert db.get_rule("TREND-001") is not None
  assert db.get_rule("TR0080") is not None
  assert len(db.all_rules()) >= 275


def test_rule_database_search():
  db = get_rule_database()
  tr_rules = db.search(category_code="TR")
  assert len(tr_rules) == 95
  direction = db.search(category_code="TR")
  assert any(r.rule_id == "TR0010" and r.rule_name == "Trend Continuation" for r in direction)
  tagged = db.search(tag="Core")
  assert any(r.rule_id == "TR0001" for r in tagged)


def test_rule_database_validate_tr0001():
  db = get_rule_database()
  ok, errors = db.validate_rule("TR0001")
  assert ok, errors


def test_rule_database_tr0001_parameters():
  db = get_rule_database()
  rule = db.get_rule("TR0001")
  assert rule is not None
  assert len(rule.parameters) >= 3
  assert len(rule.inputs) >= 2
  assert "PASS" in str(rule.outputs) or len(rule.outputs) >= 1


def test_registry_facade_uses_database():
  reg = get_registry()
  assert reg.is_registered("TR0001")
  assert reg.resolve("TR-001") == "TR0001"
  assert len(reg.category_codes()) == 21


def test_rule_folder_exists():
  db = get_rule_database()
  rule = db.get_rule("TR0001")
  assert rule is not None
  from pathlib import Path

  assert Path(rule.folder_path).exists()


def test_composite_catalog_seeded(tmp_path):
  from engine.core.rule_database import RuleDatabase

  db = RuleDatabase(db_path=tmp_path / "composite_test.db")
  db.seed_from_registry()
  rule = db.get_rule("CTR001")
  assert rule is not None
  assert rule.rule_name == "Trend Direction"
  assert rule.rule_type == "composite"
  assert db.get_rule("CDQ002").rule_name == "Data Reliability"
  composite = db.search(tag="Composite")
  assert len(composite) == 130
  db.close()
