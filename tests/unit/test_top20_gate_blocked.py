"""Tests for Today's Picks ranking and gate-blocked UX."""

from __future__ import annotations

from engine.core.types import GateResult
from engine.domains.moving_average_engine import evaluate_moving_average_engine
from engine.domains.trend_engine import evaluate_trend_engine
from engine.domains.volume_engine import evaluate_volume_engine
from engine.recommendation.top20 import build_candidate, is_gate_eligible, rank_top20
from engine.scoring import compute_master_score
from tests.fixtures.ohlcv import make_uptrend_ohlcv


def _candidate(symbol: str, name: str, *, gate_status: str):
    entry = type("Entry", (), {"symbol": symbol, "name": name, "market": "KS"})()
    df = make_uptrend_ohlcv(n=260, start=100 + int(symbol[:2]))
    from engine.indicators.registry import compute_all

    df = compute_all(df)
    trend = evaluate_trend_engine(df)
    master = compute_master_score(
        trend=trend,
        moving_average=evaluate_moving_average_engine(df),
        volume=evaluate_volume_engine(df),
        mvp_mode=True,
    )
    gate = GateResult(status=gate_status, reasons=[gate_status], failed_gates=[])
    return build_candidate(
        entry,
        master,
        trend,
        gate_status,  # type: ignore[arg-type]
        df=df,
        gate=gate,
        data_valid=True,
    )


def test_is_gate_eligible_excludes_fail_only():
    assert is_gate_eligible("PASS") is True
    assert is_gate_eligible("WARN") is True
    assert is_gate_eligible("FAIL") is False


def test_rank_top20_excludes_gate_fail_from_picks():
    pass_candidate = _candidate("005930", "삼성전자", gate_status="PASS")
    fail_candidate = _candidate("000660", "SK하이닉스", gate_status="FAIL")

    result = rank_top20([pass_candidate, fail_candidate], top_n=2)

    assert len(result.picks) == 1
    assert result.picks[0].symbol == "005930"
    assert all(pick.gate != "FAIL" for pick in result.picks)
    assert len(result.gate_blocked) == 1
    assert result.gate_blocked[0].symbol == "000660"
    assert result.gate_blocked[0].rank == 0


def test_rank_top20_eligible_only_false_keeps_fail_in_picks():
    pass_candidate = _candidate("005930", "삼성전자", gate_status="PASS")
    fail_candidate = _candidate("000660", "SK하이닉스", gate_status="FAIL")

    result = rank_top20(
        [pass_candidate, fail_candidate],
        top_n=2,
        eligible_only=False,
    )

    assert len(result.picks) == 2
    assert result.gate_blocked == []
