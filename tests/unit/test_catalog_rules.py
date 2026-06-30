"""Smoke tests for catalog-driven rule categories."""

from __future__ import annotations

import pytest

from engine.indicators.registry import compute_all
from engine.rules.catalog_registry import CATEGORY_EVALUATORS, rule_count
from tests.fixtures.ohlcv import make_uptrend_ohlcv


@pytest.mark.parametrize(
    "category,expected",
    [
        ("TR", 80),
        ("MA", 60),
        ("VL", 60),
        ("PA", 60),
        ("MO", 60),
        ("VO", 60),
        ("MS", 60),
        ("SR", 60),
        ("BO", 60),
        ("PB", 60),
        ("PT", 60),
        ("CS", 60),
        ("GP", 60),
        ("RK", 60),
        ("EN", 60),
        ("EX", 60),
        ("MR", 60),
        ("MT", 60),
        ("CF", 60),
        ("DQ", 60),
    ],
)
def test_category_registry_size(category: str, expected: int) -> None:
    assert len(CATEGORY_EVALUATORS[category]) == expected


def test_total_atomic_rule_count() -> None:
    assert rule_count() >= 1220


@pytest.mark.parametrize("category", ["MO", "VO", "PA", "DQ", "CS"])
def test_sample_rules_evaluate(category: str) -> None:
    df = compute_all(make_uptrend_ohlcv(n=260))
    mapping = CATEGORY_EVALUATORS[category]
    sample_ids = sorted(mapping.keys())[:3]
    for rule_id in sample_ids:
        result = mapping[rule_id](df)
        assert result.rule_id == rule_id
        assert result.verdict in ("PASS", "FAIL", "PARTIAL", "UNKNOWN")
