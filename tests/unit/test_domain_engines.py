"""Tests for generic domain engines and full scoring bundle."""

from __future__ import annotations

import pytest

from engine.domains._config import DOMAIN_ENGINE_CONFIGS
from engine.domains.bundle import (
    IMPLEMENTED_GENERIC_KEYS,
    PENDING_ENGINE_KEYS,
    evaluate_domain_bundle,
    evaluate_generic_domains,
)
from engine.indicators.registry import compute_all
from engine.scoring import MASTER_MAX_SCORE, compute_master_score
from engine.scoring.domain_budgets import ENGINE_WEIGHTS, MVP_ENGINES
from tests.fixtures.ohlcv import make_uptrend_ohlcv


@pytest.mark.parametrize("engine_key", sorted(DOMAIN_ENGINE_CONFIGS.keys()))
def test_generic_domain_engine_evaluates(engine_key: str) -> None:
    df = compute_all(make_uptrend_ohlcv(n=260))
    results = evaluate_generic_domains(df)
    result = results[engine_key]
    budget = ENGINE_WEIGHTS[engine_key][1]
    assert result.engine_key == engine_key
    assert 0.0 <= result.score <= budget
    assert result.max_score == budget
    assert result.grade in {"S", "A", "B", "C", "D"}
    assert len(result.atomic_results) == len(DOMAIN_ENGINE_CONFIGS[engine_key].atomic_rules)


def test_domain_bundle_includes_core_and_generic() -> None:
    df = compute_all(make_uptrend_ohlcv(n=260))
    bundle = evaluate_domain_bundle(df)
    assert bundle.trend.trend_score > 0
    assert bundle.moving_average.ma_score > 0
    assert bundle.volume.vl_score > 0
    assert set(bundle.domains.keys()) == IMPLEMENTED_GENERIC_KEYS


def test_full_mode_master_score_uses_all_implemented_domains() -> None:
    df = compute_all(make_uptrend_ohlcv(n=260))
    bundle = evaluate_domain_bundle(df)
    master = compute_master_score(bundle=bundle, mvp_mode=False)
    assert master.max_score == MASTER_MAX_SCORE
    assert master.mvp_mode is False
    active = {key for key, domain in master.domains.items() if domain is not None}
    assert active == set(ENGINE_WEIGHTS.keys())
    assert master.domains["exit"] is not None
    assert master.domains["exit"].status == "implemented"
    implemented = {
        key for key, domain in master.domains.items() if domain and domain.status == "implemented"
    }
    assert implemented == set(ENGINE_WEIGHTS.keys()) - PENDING_ENGINE_KEYS
    assert master.total_score > 0


def test_exit_domain_engine_uses_composite_rules() -> None:
    df = compute_all(make_uptrend_ohlcv(n=260))
    results = evaluate_generic_domains(df)
    exit_result = results["exit"]
    budget = ENGINE_WEIGHTS["exit"][1]
    assert exit_result.engine_key == "exit"
    assert 0.0 <= exit_result.score <= budget
    assert len(exit_result.atomic_results) == 6
    assert len(exit_result.composite_results) == 5
    assert len(exit_result.reasons) > 0


def test_mvp_mode_still_uses_three_domains() -> None:
    df = compute_all(make_uptrend_ohlcv(n=260))
    bundle = evaluate_domain_bundle(df)
    master = compute_master_score(bundle=bundle, mvp_mode=True)
    assert master.max_score == 500.0
    assert master.mvp_mode is True
    for key in MVP_ENGINES:
        assert master.domains[key] is not None
        assert master.domains[key].status == "implemented"
    assert master.domains["momentum"] is None
