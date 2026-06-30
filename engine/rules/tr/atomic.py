from __future__ import annotations

from collections.abc import Callable

import numpy as np
import pandas as pd

from engine.core.pivots import find_pivot_highs, find_pivot_lows
from engine.core.taxonomy import to_canonical_id
from engine.core.types import RuleResult
from engine.rules.tr._scoring import bearish_absence_score, bullish_quality_score, confidence_risk


def _unknown(rule_id: str, reason: str) -> RuleResult:
    return RuleResult(rule_id=rule_id, verdict="UNKNOWN", score=0.0, reasons=[reason])


def _evaluate_bullish_pivot(
    df: pd.DataFrame,
    rule_id: str,
    pivot_fn: Callable[[pd.Series], list[int]],
    price_col: str,
    label: str,
    lookback: int = 40,
    min_pivots: int = 2,
) -> RuleResult:
    cid = to_canonical_id(rule_id)
    if len(df) < lookback:
        return _unknown(cid, f"데이터 부족 ({len(df)}일 < {lookback}일)")

    window = df.tail(lookback)
    pivots = pivot_fn(window[price_col])
    if len(pivots) < 2:
        return RuleResult(
            rule_id=cid,
            verdict="FAIL",
            score=0.0,
            reasons=[f"{label} 구조 미형성"],
            metadata={"pivot_count": len(pivots)},
        )

    prices = [float(window[price_col].iloc[i]) for i in pivots]
    structure_count = sum(1 for i in range(1, len(prices)) if prices[i] > prices[i - 1])

    rises = []
    for i in range(1, len(prices)):
        prev, curr = prices[i - 1], prices[i]
        if prev != 0 and curr > prev:
            rises.append(((curr - prev) / prev) * 100)
    avg_rise = float(np.mean(rises)) if rises else 0.0

    vol = window["volume"]
    volume_ok = (
        bool(vol.iloc[-5:].mean() > vol.iloc[-20:].mean() * 0.9) if len(vol) >= 20 else False
    )

    score, verdict, grade = bullish_quality_score(structure_count, min_pivots, avg_rise, volume_ok)
    conf, risk = confidence_risk(grade)

    reasons: list[str] = []
    if verdict == "PASS":
        reasons.append(f"{label} 품질 {grade}")
        if volume_ok:
            reasons.append("거래량 지지")
    else:
        reasons.append(f"{label} 미충족")

    return RuleResult(
        rule_id=cid,
        verdict=verdict,
        score=score,
        confidence_delta=conf,
        risk_delta=risk,
        reasons=reasons,
        metadata={
            "structure_count": structure_count,
            "avg_change_pct": avg_rise,
            "quality_grade": grade,
            "pivot_count": len(pivots),
        },
    )


def _evaluate_bearish_detection(
    df: pd.DataFrame,
    rule_id: str,
    pivot_fn: Callable[[pd.Series], list[int]],
    price_col: str,
    label: str,
    lookback: int = 40,
) -> RuleResult:
    cid = to_canonical_id(rule_id)
    if len(df) < lookback:
        return _unknown(cid, "데이터 부족")

    window = df.tail(lookback)
    pivots = pivot_fn(window[price_col])
    if len(pivots) < 2:
        return RuleResult(
            rule_id=cid,
            verdict="PASS",
            score=20.0,
            reasons=[f"{label} 미감지"],
            metadata={"bearish_count": 0},
        )

    prices = [float(window[price_col].iloc[i]) for i in pivots]
    bearish_count = sum(1 for i in range(1, len(prices)) if prices[i] < prices[i - 1])

    score, verdict, grade = bearish_absence_score(bearish_count, min_bearish=2)
    conf, risk = confidence_risk(grade)

    reasons = [f"{label} 미감지"] if verdict == "PASS" else [f"{label} 감지됨"]

    return RuleResult(
        rule_id=cid,
        verdict=verdict,
        score=score,
        confidence_delta=conf,
        risk_delta=risk,
        reasons=reasons,
        metadata={"bearish_count": bearish_count, "quality_grade": grade},
    )


def evaluate_higher_low(df: pd.DataFrame) -> RuleResult:
    return _evaluate_bullish_pivot(df, "TR0002", find_pivot_lows, "low", "Higher Low")


def evaluate_lower_high(df: pd.DataFrame) -> RuleResult:
    return _evaluate_bearish_detection(df, "TR0003", find_pivot_highs, "high", "Lower High")


def evaluate_lower_low(df: pd.DataFrame) -> RuleResult:
    return _evaluate_bearish_detection(df, "TR0004", find_pivot_lows, "low", "Lower Low")
