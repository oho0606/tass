"""Shared scoring utilities for TR rules."""

from __future__ import annotations

from engine.core.types import RuleVerdict


def confidence_risk(grade: str) -> tuple[float, float]:
    mapping = {
        "Excellent": (5.0, -5.0),
        "Strong": (3.0, -3.0),
        "Good": (2.0, -2.0),
        "Weak": (-2.0, 2.0),
        "Fail": (-5.0, 6.0),
    }
    return mapping.get(grade, (0.0, 0.0))


def bullish_quality_score(
    structure_count: int,
    min_count: int,
    avg_rise_pct: float,
    volume_ok: bool,
) -> tuple[float, RuleVerdict, str]:
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
        return 8.0, "PASS", "Weak"
    return 0.0, "FAIL", "Fail"


def bearish_absence_score(
    bearish_count: int,
    min_bearish: int,
) -> tuple[float, RuleVerdict, str]:
    if bearish_count >= min_bearish + 1:
        return 0.0, "FAIL", "Fail"
    if bearish_count == min_bearish:
        return 8.0, "PASS", "Weak"
    if bearish_count == 1:
        return 14.0, "PASS", "Good"
    return 20.0, "PASS", "Excellent"
