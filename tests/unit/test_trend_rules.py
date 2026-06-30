from engine.core.rule_registry import get_registry
from engine.core.taxonomy import to_canonical_id, validate_rule_id
from engine.domains.trend_engine import evaluate_trend_engine
from engine.rules.tr.atomic import evaluate_higher_low, evaluate_lower_high, evaluate_lower_low
from engine.rules.tr.tr0001_higher_high import TR0001HigherHighRule, evaluate_higher_high
from tests.fixtures.ohlcv import make_downtrend_ohlcv, make_sideways_ohlcv, make_uptrend_ohlcv


def test_trend_001_uptrend_pass():
  df = make_uptrend_ohlcv()
  result = evaluate_higher_high(df)
  assert result.verdict in ("PASS", "FAIL")
  assert result.rule_id == "TR0001"
  assert result.score > 0


def test_trend_001_downtrend_fail():
  df = make_downtrend_ohlcv()
  result = evaluate_higher_high(df)
  assert result.verdict == "FAIL"
  assert result.score == 0


def test_trend_001_short_data_unknown():
  df = make_uptrend_ohlcv(n=20)
  result = evaluate_higher_high(df)
  assert result.verdict == "UNKNOWN"


def test_tr0001_class_interface():
  rule = TR0001HigherHighRule()
  rule.initialize({"lookback": 40})
  df = make_uptrend_ohlcv()
  assert rule.validate_input(df)
  rule.run(df)
  meta = rule.metadata()
  assert meta["rule_id"] == "TR0001"
  explain = rule.explain()
  assert "verdict" in explain


def test_trend_002_uptrend():
  df = make_uptrend_ohlcv()
  result = evaluate_higher_low(df)
  assert result.rule_id == "TR0002"


def test_trend_003_downtrend_detects():
  df = make_downtrend_ohlcv()
  result = evaluate_lower_high(df)
  assert result.rule_id == "TR0003"


def test_trend_004_uptrend_no_failure():
  df = make_uptrend_ohlcv()
  result = evaluate_lower_low(df)
  assert result.score >= 14


def test_trend_engine_score_range():
  df = make_uptrend_ohlcv()
  result = evaluate_trend_engine(df)
  assert 0 <= result.trend_score <= 200
  assert "TR0001" in result.atomic_results


def test_trend_engine_sideways():
  df = make_sideways_ohlcv()
  result = evaluate_trend_engine(df)
  assert result.trend_score < 180


def test_canonical_id_aliases():
  assert to_canonical_id("TR-001") == "TR0001"
  assert to_canonical_id("TREND-C001") == "TRC001"
  assert validate_rule_id("TR0001")
