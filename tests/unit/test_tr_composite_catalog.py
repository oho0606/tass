"""Tests for TR catalog and composite rule libraries."""

from __future__ import annotations

import pytest

from engine.core.types import RuleResult
from engine.indicators.registry import compute_all
from engine.rules.catalog_registry import CATEGORY_EVALUATORS, rule_count
from engine.rules.composite.registry import COMPOSITE_EVALUATORS
from tests.fixtures.ohlcv import make_uptrend_ohlcv


def test_tr_registry_size() -> None:
    assert len(CATEGORY_EVALUATORS["TR"]) == 80


def test_total_atomic_rule_count_includes_tr() -> None:
    assert rule_count() == 1220


def test_composite_registry_size() -> None:
    assert len(COMPOSITE_EVALUATORS) == 130


@pytest.mark.parametrize(
    "rule_id",
    ["TR0001", "TR0005", "TR0020", "TR0040", "TR0080"],
)
def test_tr_rules_evaluate(rule_id: str) -> None:
    df = compute_all(make_uptrend_ohlcv(n=260))
    result = CATEGORY_EVALUATORS["TR"][rule_id](df)
    assert result.rule_id == rule_id
    assert result.verdict in ("PASS", "FAIL", "PARTIAL", "UNKNOWN")


def _make_atomic_snapshot(prefix: str, *, pass_count: int, total: int) -> dict[str, RuleResult]:
    atomic: dict[str, RuleResult] = {}
    for idx in range(1, total + 1):
        rule_id = f"{prefix}{idx:04d}"
        verdict = "PASS" if idx <= pass_count else "FAIL"
        atomic[rule_id] = RuleResult(
            rule_id=rule_id,
            verdict=verdict,
            status=verdict,
            score=1.0 if verdict == "PASS" else 0.0,
            reasons=[rule_id],
            metadata={},
        )
    return atomic


def test_composite_cma001_bullish_quality() -> None:
    atomic = _make_atomic_snapshot("MA", pass_count=40, total=60)
    result = COMPOSITE_EVALUATORS["CMA001"](atomic)
    assert result.verdict in ("PASS", "PARTIAL")


def test_composite_cma004_bearish_mode() -> None:
    atomic = _make_atomic_snapshot("MA", pass_count=10, total=60)
    result = COMPOSITE_EVALUATORS["CMA004"](atomic)
    assert result.verdict in ("PASS", "PARTIAL", "FAIL")


def test_composite_ctr001_handcrafted() -> None:
    atomic = {
        "TR0001": RuleResult(
            rule_id="TR0001",
            verdict="PASS",
            status="PASS",
            score=1.0,
            reasons=[],
            metadata={},
        ),
        "TR0002": RuleResult(
            rule_id="TR0002",
            verdict="PASS",
            status="PASS",
            score=1.0,
            reasons=[],
            metadata={},
        ),
        "TR0003": RuleResult(
            rule_id="TR0003",
            verdict="FAIL",
            status="FAIL",
            score=0.0,
            reasons=[],
            metadata={},
        ),
        "TR0004": RuleResult(
            rule_id="TR0004",
            verdict="FAIL",
            status="FAIL",
            score=0.0,
            reasons=[],
            metadata={},
        ),
    }
    result = COMPOSITE_EVALUATORS["CTR001"](atomic)
    assert result.verdict in ("PASS", "PARTIAL", "FAIL")
