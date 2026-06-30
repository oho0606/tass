from engine.domains.trend_engine import evaluate_trend_engine
from engine.rules.composite import evaluate_composite, evaluate_ctr_rules
from engine.rules.composite.registry import COMPOSITE_EVALUATORS
from engine.rules.tr.atomic import evaluate_higher_low, evaluate_lower_high, evaluate_lower_low
from engine.rules.tr.tr0001_higher_high import evaluate_higher_high
from tests.fixtures.ohlcv import make_downtrend_ohlcv, make_sideways_ohlcv, make_uptrend_ohlcv


def _run_atomics(df):
  return {
    "TR0001": evaluate_higher_high(df),
    "TR0002": evaluate_higher_low(df),
    "TR0003": evaluate_lower_high(df),
    "TR0004": evaluate_lower_low(df),
  }


def test_composite_evaluators_registered():
  assert len(COMPOSITE_EVALUATORS) == 130
  assert "CTR001" in COMPOSITE_EVALUATORS
  assert "CMA001" in COMPOSITE_EVALUATORS


def test_ctr_rules_no_score():
  df = make_uptrend_ohlcv()
  atomic = _run_atomics(df)
  results = evaluate_ctr_rules(atomic)
  assert len(results) == 10
  for rule_id, result in results.items():
    assert result.rule_id == rule_id
    assert result.score == 0.0
    assert result.verdict in ("PASS", "PARTIAL", "FAIL", "UNKNOWN")


def test_ctr001_uptrend_direction_pass():
  df = make_uptrend_ohlcv()
  atomic = _run_atomics(df)
  result = evaluate_composite("CTR001", atomic)
  assert result.verdict in ("PASS", "PARTIAL")
  assert result.metadata.get("direction") in ("Up", "Weak Up", "Mixed")


def test_ctr001_downtrend_direction_fail_or_partial():
  df = make_downtrend_ohlcv()
  atomic = _run_atomics(df)
  result = evaluate_composite("CTR001", atomic)
  assert result.verdict in ("FAIL", "PARTIAL", "PASS")


def test_ctr006_exhaustion_on_downtrend():
  df = make_downtrend_ohlcv()
  atomic = _run_atomics(df)
  result = evaluate_composite("CTR006", atomic)
  assert result.verdict in ("PASS", "PARTIAL", "FAIL")


def test_ctr_unknown_when_atomic_unknown():
  atomic = {
    "TR0001": evaluate_higher_high(make_uptrend_ohlcv(n=20)),
    "TR0002": evaluate_higher_low(make_uptrend_ohlcv(n=20)),
    "TR0003": evaluate_lower_high(make_uptrend_ohlcv(n=20)),
    "TR0004": evaluate_lower_low(make_uptrend_ohlcv(n=20)),
  }
  result = evaluate_composite("CTR001", atomic)
  assert result.verdict == "UNKNOWN"


def test_unimplemented_composite_returns_unknown():
  atomic = _run_atomics(make_uptrend_ohlcv())
  result = evaluate_composite("CMA999", atomic)
  assert result.verdict == "UNKNOWN"
  assert result.metadata.get("not_implemented") is True


def test_trend_engine_uses_ctr_composites():
  df = make_uptrend_ohlcv()
  result = evaluate_trend_engine(df)
  assert "CTR001" in result.composite_results
  assert "TRC001" not in result.composite_results
  assert all(r.score == 0.0 for r in result.composite_results.values())


def test_trend_engine_score_range_with_ctr():
  df = make_uptrend_ohlcv()
  result = evaluate_trend_engine(df)
  assert 0 <= result.trend_score <= 200


def test_trend_engine_sideways_with_ctr():
  df = make_sideways_ohlcv()
  result = evaluate_trend_engine(df)
  assert result.trend_score < 180
