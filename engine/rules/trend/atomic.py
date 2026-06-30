from __future__ import annotations

from collections.abc import Callable

import numpy as np
import pandas as pd

from engine.core.pivots import find_pivot_highs, find_pivot_lows
from engine.core.types import RuleResult


def _confidence_risk(grade: str) -> tuple[float, float]:
    mapping = {
        "Excellent": (5.0, -5.0),
        "Strong": (3.0, -3.0),
        "Good": (2.0, -2.0),
        "Weak": (-2.0, 2.0),
        "Fail": (-5.0, 6.0),
    }
    return mapping.get(grade, (0.0, 0.0))


def _bullish_quality_score(
    structure_count: int,
    min_count: int,
    avg_rise_pct: float,
    volume_ok: bool,
) -> tuple[float, str, str]:
    if structure_count < min_count:
        return 0.0, "FAIL", "Fail"

    rise_score = min(avg_rise_pct / 3.0, 1.0) if avg_rise_pct > 0 else 0.0
    count_score = min((structure_count - min_count + 1) / 3.0, 1.0)
    vol_bonus = 0.15 if volume_ok else 0.0
    raw = count_score * 0.5 + rise_score * 0.35 + vol_bonus

    if raw >= 0.85:
        return 20.0, "PASS", "Excellent"
    if raw >= 0.70:
        return 17.0, "PASS", "Strong"
    if raw >= 0.55:
        return 14.0, "PASS", "Good"
    if raw >= 0.35:
        return 8.0, "WARN", "Weak"
    return 0.0, "FAIL", "Fail"


def _bearish_absence_score(
    bearish_count: int,
    min_bearish: int,
) -> tuple[float, str, str]:
    """Higher score when bearish pattern is absent."""
    if bearish_count >= min_bearish + 1:
        return 0.0, "FAIL", "Fail"
    if bearish_count == min_bearish:
        return 8.0, "WARN", "Weak"
    if bearish_count == 1:
        return 14.0, "PASS", "Good"
    return 20.0, "PASS", "Excellent"


def _evaluate_bullish_pivot(
    df: pd.DataFrame,
    rule_id: str,
    pivot_fn: Callable[[pd.Series], list[int]],
    price_col: str,
    label: str,
    lookback: int = 40,
    min_pivots: int = 2,
) -> RuleResult:
    if len(df) < lookback:
        return RuleResult(
            rule_id=rule_id,
            status="FAIL",
            score=0.0,
            reasons=[f"데이터 부족 ({len(df)}일 < {lookback}일)"],
        )

    window = df.tail(lookback)
    pivots = pivot_fn(window[price_col])
    if len(pivots) < 2:
        return RuleResult(
            rule_id=rule_id,
            status="FAIL",
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

    score, status, grade = _bullish_quality_score(structure_count, min_pivots, avg_rise, volume_ok)
    conf, risk = _confidence_risk(grade)

    reasons: list[str] = []
    if status == "PASS":
        reasons.append(f"{label} 품질 {grade}")
        if volume_ok:
            reasons.append("거래량 지지")
    elif status == "WARN":
        reasons.append(f"{label} 약화")
    else:
        reasons.append(f"{label} 미충족")

    return RuleResult(
        rule_id=rule_id,
        status=status,  # type: ignore[arg-type]
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
    if len(df) < lookback:
        return RuleResult(rule_id=rule_id, status="FAIL", score=0.0, reasons=["데이터 부족"])

    window = df.tail(lookback)
    pivots = pivot_fn(window[price_col])
    if len(pivots) < 2:
        return RuleResult(
            rule_id=rule_id,
            status="PASS",
            score=20.0,
            reasons=[f"{label} 미감지"],
            metadata={"bearish_count": 0},
        )

    prices = [float(window[price_col].iloc[i]) for i in pivots]
    bearish_count = sum(1 for i in range(1, len(prices)) if prices[i] < prices[i - 1])

    score, status, grade = _bearish_absence_score(bearish_count, min_bearish=2)
    conf, risk = _confidence_risk(grade)

    reasons = [f"{label} 미감지"] if status == "PASS" else [f"{label} 감지됨"]

    return RuleResult(
        rule_id=rule_id,
        status=status,  # type: ignore[arg-type]
        score=score,
        confidence_delta=conf,
        risk_delta=risk,
        reasons=reasons,
        metadata={"bearish_count": bearish_count, "quality_grade": grade},
    )


def evaluate_higher_high(df: pd.DataFrame) -> RuleResult:
    return _evaluate_bullish_pivot(df, "TREND-001", find_pivot_highs, "high", "Higher High")


def evaluate_higher_low(df: pd.DataFrame) -> RuleResult:
    return _evaluate_bullish_pivot(df, "TREND-002", find_pivot_lows, "low", "Higher Low")


def evaluate_lower_high(df: pd.DataFrame) -> RuleResult:
    return _evaluate_bearish_detection(df, "TREND-003", find_pivot_highs, "high", "Lower High")


def evaluate_lower_low(df: pd.DataFrame) -> RuleResult:
    return _evaluate_bearish_detection(df, "TREND-004", find_pivot_lows, "low", "Lower Low")
