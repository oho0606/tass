"""Risk grade, level, and decision mapping for Risk Engine v1.0 (Frozen)."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RiskGrade:
    label: str
    stars: str
    min_score: float
    max_score: float


@dataclass(frozen=True)
class RiskLevel:
    label: str
    min_score: float
    max_score: float


@dataclass(frozen=True)
class ComponentWeight:
    key: str
    label: str
    weight: int


DEFAULT_COMPONENT_WEIGHTS: tuple[ComponentWeight, ...] = (
    ComponentWeight("volatility_risk", "Volatility Risk", 20),
    ComponentWeight("gap_risk", "Gap Risk", 15),
    ComponentWeight("liquidity_risk", "Liquidity Risk", 10),
    ComponentWeight("trend_risk", "Trend Risk", 10),
    ComponentWeight("momentum_risk", "Momentum Risk", 5),
    ComponentWeight("market_risk", "Market Risk", 10),
    ComponentWeight("entry_timing_risk", "Entry Timing Risk", 5),
    ComponentWeight("stop_loss_distance", "Stop Loss Distance", 5),
    ComponentWeight("atr_risk", "ATR Risk", 5),
    ComponentWeight("maximum_drawdown_risk", "Maximum Drawdown Risk", 5),
    ComponentWeight("price_extension_risk", "Price Extension Risk", 3),
    ComponentWeight("false_breakout_risk", "False Breakout Risk", 3),
    ComponentWeight("data_quality_risk", "Data Quality Risk", 2),
    ComponentWeight("signal_conflict_risk", "Signal Conflict Risk", 2),
)

RISK_GRADES: tuple[RiskGrade, ...] = (
    RiskGrade("Very Low Risk", "★★★★★", 0.0, 10.0),
    RiskGrade("Low Risk", "★★★★★", 11.0, 20.0),
    RiskGrade("Moderate Risk", "★★★★☆", 21.0, 30.0),
    RiskGrade("Elevated Risk", "★★★☆☆", 31.0, 40.0),
    RiskGrade("High Risk", "★★☆☆☆", 41.0, 50.0),
    RiskGrade("Very High Risk", "★☆☆☆☆", 51.0, 70.0),
    RiskGrade("Extreme Risk", "Reject", 71.0, 100.0),
)

RISK_LEVELS: tuple[RiskLevel, ...] = (
    RiskLevel("Excellent", 0.0, 10.0),
    RiskLevel("Good", 11.0, 20.0),
    RiskLevel("Acceptable", 21.0, 30.0),
    RiskLevel("Caution", 31.0, 40.0),
    RiskLevel("Danger", 41.0, 50.0),
    RiskLevel("Reject", 51.0, 100.0),
)


def clamp_risk_score(score: float) -> float:
    return max(0.0, min(100.0, score))


def grade_from_score(score: float) -> RiskGrade:
    """Map risk score to grade using contiguous upper bounds."""
    clamped = clamp_risk_score(score)
    if clamped <= 10.0:
        return RISK_GRADES[0]
    if clamped <= 20.0:
        return RISK_GRADES[1]
    if clamped <= 30.0:
        return RISK_GRADES[2]
    if clamped <= 40.0:
        return RISK_GRADES[3]
    if clamped <= 50.0:
        return RISK_GRADES[4]
    if clamped <= 70.0:
        return RISK_GRADES[5]
    return RISK_GRADES[6]


def level_from_score(score: float) -> RiskLevel:
    """Map risk score to level using contiguous upper bounds."""
    clamped = clamp_risk_score(score)
    if clamped <= 10.0:
        return RISK_LEVELS[0]
    if clamped <= 20.0:
        return RISK_LEVELS[1]
    if clamped <= 30.0:
        return RISK_LEVELS[2]
    if clamped <= 40.0:
        return RISK_LEVELS[3]
    if clamped <= 50.0:
        return RISK_LEVELS[4]
    return RISK_LEVELS[5]


def decision_from_score(score: float) -> str:
    clamped = clamp_risk_score(score)
    if clamped <= 20.0:
        return "PASS"
    if clamped <= 30.0:
        return "PASS WITH CAUTION"
    if clamped <= 40.0:
        return "REVIEW REQUIRED"
    return "FAIL"


def scale_linear(value: float, low: float, high: float, *, invert: bool = False) -> float:
    """Map value to 0–100 risk (low input → low risk, high input → high risk)."""
    if high <= low:
        return 50.0
    ratio = (value - low) / (high - low)
    if invert:
        ratio = 1.0 - ratio
    return clamp_risk_score(ratio * 100.0)
