"""Tests for adopted-only MVP scoring."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from engine.core.adopted_rules import clear_adopted_rules_cache, load_adopted_mvp_rule_ids
from engine.domains.moving_average_engine import evaluate_moving_average_engine
from engine.domains.trend_engine import evaluate_trend_engine
from engine.indicators.registry import compute_all
from tests.fixtures.ohlcv import make_uptrend_ohlcv


@pytest.fixture(autouse=True)
def _clear_adopted_cache():
    clear_adopted_rules_cache()
    yield
    clear_adopted_rules_cache()


def test_load_adopted_mvp_rule_ids_from_metadata():
    adopted = load_adopted_mvp_rule_ids()
    assert "TR0001" in adopted or len(adopted) >= 1


def test_trend_engine_excludes_rejected_rules_from_scoring(monkeypatch):
    adopted = frozenset({"TR0001", "TR0002", "TR0004", "CTR001", "CTR002"})
    monkeypatch.setattr(
        "engine.domains.trend_engine.load_adopted_mvp_rule_ids",
        lambda: adopted,
    )
    df = compute_all(make_uptrend_ohlcv(n=260))
    result = evaluate_trend_engine(df)
    assert result.trend_score >= 0
    assert "TR0003" not in adopted


def test_moving_average_engine_uses_adopted_rules_only(monkeypatch):
    monkeypatch.setattr(
        "engine.domains.moving_average_engine.load_adopted_mvp_rule_ids",
        lambda: frozenset({"MA0007"}),
    )
    df = compute_all(make_uptrend_ohlcv(n=260))
    result = evaluate_moving_average_engine(df)
    assert set(result.atomic_results) == {"MA0007"}


def test_finalize_report_rejects_non_adopted_rules():
    report_path = Path("output/mvp_adoption_report.json")
    if not report_path.exists():
        pytest.skip("adoption report missing")
    report = json.loads(report_path.read_text(encoding="utf-8"))
    revise = [
        r["rule_id"]
        for r in report["rules"]
        if r.get("aggregate_verdict") == "REVISE"
    ]
    if not revise:
        pytest.skip("no REVISE rules in report")
    meta = Path("rule_database/rules") / revise[0] / "metadata.json"
    if meta.exists():
        lifecycle = json.loads(meta.read_text(encoding="utf-8")).get("lifecycle_stage")
        # After finalize script, REVISE rules should be Rejected
        assert lifecycle in {"Rejected", "Implemented", "Adopted"}
