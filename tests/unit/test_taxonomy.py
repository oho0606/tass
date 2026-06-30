from engine.core.rule_database import get_rule_database
from engine.core.rule_registry import get_registry
from engine.core.taxonomy import (
  CategoryCode,
  LEGACY_ALIASES,
  composite_library_code,
  is_composite_library_id,
  normalize_rule_id,
  parse_category_from_rule_id,
  parse_rule_type,
  to_canonical_id,
  validate_rule_id,
  RuleType,
)


def test_all_21_categories_defined():
  assert len(CategoryCode) == 21


def test_canonical_id_tr0001():
  assert to_canonical_id("TR0001") == "TR0001"
  assert to_canonical_id("TR-001") == "TR0001"
  assert to_canonical_id("TREND-001") == "TR0001"
  assert to_canonical_id("TR-C001") == "TRC001"
  assert to_canonical_id("TR-E001") == "TRE001"


def test_normalize_legacy_trend_ids():
  assert normalize_rule_id("TREND-001") == "TR0001"
  assert normalize_rule_id("TREND-C001") == "TRC001"
  assert normalize_rule_id("TREND-E001") == "TRE001"


def test_parse_category_tr():
  assert parse_category_from_rule_id("TR0001") == CategoryCode.TR
  assert parse_category_from_rule_id("TREND-001") == CategoryCode.TR


def test_parse_rule_types():
  assert parse_rule_type("TR0001") == RuleType.ATOMIC
  assert parse_rule_type("TRC001") == RuleType.COMPOSITE
  assert parse_rule_type("CTR001") == RuleType.COMPOSITE
  assert parse_rule_type("TRE001") == RuleType.ENGINE


def test_composite_library_ids():
  assert to_canonical_id("CTR001") == "CTR001"
  assert is_composite_library_id("CTR001") is True
  assert composite_library_code("CMA010") == "CMA"
  assert parse_category_from_rule_id("CTR001") == CategoryCode.TR
  assert parse_category_from_rule_id("CDQ002") == CategoryCode.DQ
  assert validate_rule_id("CCF005") is True


def test_parse_category_ma():
  assert parse_category_from_rule_id("MA0001") == CategoryCode.MA
  assert parse_category_from_rule_id("MA0031") == CategoryCode.MA


def test_validate_rule_id():
  assert validate_rule_id("TR0001") is True
  assert validate_rule_id("TREND-001") is True
  assert validate_rule_id("INVALID") is False


def test_registry_loads_tr_rules():
  reg = get_registry()
  assert reg.is_registered("TR0001")
  assert reg.is_registered("TREND-001")
  assert reg.resolve("TR-002") == "TR0002"
  tr_rules = reg.rules_by_category(CategoryCode.TR)
  atomic = [r for r in tr_rules if r.rule_id.startswith("TR0")]
  assert len(atomic) == 80
  assert reg.is_registered("TR0080")
  assert len(tr_rules) == 95  # 80 atomic + 4 legacy composite + 1 engine + 10 library composite


def test_tr_catalog_frozen_rules():
  db = get_rule_database()
  frozen = db.search(category_code="TR", status="Frozen")
  assert len(frozen) == 86
  assert all(r.rule_id >= "TR0005" or r.rule_id.startswith("CTR") for r in frozen)


def test_ma_catalog_frozen_rules():
  db = get_rule_database()
  ma_rules = db.search(category_code="MA")
  assert len(ma_rules) == 70
  assert db.get_rule("MA0001").rule_name == "Price Above SMA5"
  assert db.get_rule("MA0060").rule_name == "Moving Average Structure Stable"
  frozen = db.search(category_code="MA", status="Frozen")
  assert len(frozen) == 70


def test_registry_has_21_categories():
  reg = get_registry()
  assert len(reg.category_codes()) == 21


def test_legacy_aliases_point_to_canonical():
  for legacy, canonical in LEGACY_ALIASES.items():
    assert to_canonical_id(legacy) == canonical
