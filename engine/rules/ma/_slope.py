"""Shared helpers for MA slope rules (MA0041–MA0050)."""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from engine.core.rule_base import BaseRule
from engine.core.types import RuleResult, RuleVerdict
from engine.rules.ma._helpers import MaType
from engine.rules.ma._scoring import confidence_risk_for_pass, score_from_verdict

SlopeDirection = Literal["rising", "falling"]
SlopeTrend = Literal["increasing", "decreasing"]
DEFAULT_SLOPE_PERIOD = 20
DEFAULT_SLOPE_LOOKBACK = 5
FLAT_SLOPE_THRESHOLD_PCT = 0.05


def _ma_column(ma_type: MaType, period: int) -> str:
    prefix = "ma" if ma_type == "sma" else "ema"
    return f"{prefix}_{period}"


def _slope_pct(series: pd.Series, lookback: int) -> float:
    """Percent change of MA over ``lookback`` bars."""
    if len(series) <= lookback:
        return 0.0
    start = float(series.iloc[-lookback - 1])
    end = float(series.iloc[-1])
    if start == 0.0:
        return 0.0
    return (end - start) / start * 100.0


class MaSlopeRule(BaseRule):
    """PASS when MA slope direction matches rule (rising or falling)."""

    rule_id: str
    rule_name: str
    ma_type: MaType
    direction: SlopeDirection
    period: int = DEFAULT_SLOPE_PERIOD
    lookback: int = DEFAULT_SLOPE_LOOKBACK

    def default_parameters(self) -> dict[str, Any]:
        return {
            "ma_type": self.ma_type,
            "period": self.period,
            "lookback": self.lookback,
            "direction": self.direction,
        }

    def validate_input(self, df: pd.DataFrame) -> bool:
        if df is None or df.empty:
            return False
        lookback = int(self._parameters["lookback"])
        period = int(self._parameters["period"])
        if len(df) <= lookback:
            return False
        column = _ma_column(self.ma_type, period)
        if column not in df.columns:
            return False
        window = df[column].iloc[-lookback - 1 :]
        return not pd.isna(window).any()

    def calculate(self, df: pd.DataFrame) -> dict[str, Any]:
        lookback = int(self._parameters["lookback"])
        period = int(self._parameters["period"])
        column = _ma_column(self.ma_type, period)
        slope = _slope_pct(df[column], lookback)
        direction = self._parameters["direction"]
        passed = slope > 0.0 if direction == "rising" else slope < 0.0
        return {
            "slope_pct": round(slope, 4),
            "lookback": lookback,
            "period": period,
            "passed": passed,
        }

    def evaluate(self, df: pd.DataFrame) -> RuleVerdict:
        _ = df
        return "PASS" if self._calculation.get("passed") else "FAIL"

    def _build_result(self, verdict: RuleVerdict) -> RuleResult:
        score = score_from_verdict(verdict)
        passed = verdict == "PASS"
        conf, risk = confidence_risk_for_pass(passed)
        label = "상승" if self.direction == "rising" else "하락"
        return RuleResult(
            rule_id=self.rule_id,
            verdict=verdict,
            score=score,
            confidence_delta=conf,
            risk_delta=risk,
            reasons=[f"{self.ma_type.upper()}{self.period} 기울기 {label}"],
            metadata=dict(self._calculation),
        )


class MaSlopeTrendRule(BaseRule):
    """PASS when MA slope is accelerating (increasing) or decelerating (decreasing)."""

    rule_id: str
    rule_name: str
    ma_type: MaType
    trend: SlopeTrend
    period: int = DEFAULT_SLOPE_PERIOD
    lookback: int = DEFAULT_SLOPE_LOOKBACK

    def default_parameters(self) -> dict[str, Any]:
        return {
            "ma_type": self.ma_type,
            "period": self.period,
            "lookback": self.lookback,
            "trend": self.trend,
        }

    def validate_input(self, df: pd.DataFrame) -> bool:
        if df is None or df.empty:
            return False
        lookback = int(self._parameters["lookback"])
        period = int(self._parameters["period"])
        if len(df) <= lookback * 2:
            return False
        column = _ma_column(self.ma_type, period)
        if column not in df.columns:
            return False
        window = df[column].iloc[-lookback * 2 - 1 :]
        return not pd.isna(window).any()

    def calculate(self, df: pd.DataFrame) -> dict[str, Any]:
        lookback = int(self._parameters["lookback"])
        period = int(self._parameters["period"])
        column = _ma_column(self.ma_type, period)
        current = _slope_pct(df[column], lookback)
        previous = _slope_pct(df[column].iloc[:-lookback], lookback)
        delta = current - previous
        passed = delta > 0.0 if self.trend == "increasing" else delta < 0.0
        return {
            "current_slope_pct": round(current, 4),
            "previous_slope_pct": round(previous, 4),
            "delta": round(delta, 4),
            "passed": passed,
        }

    def evaluate(self, df: pd.DataFrame) -> RuleVerdict:
        _ = df
        return "PASS" if self._calculation.get("passed") else "FAIL"

    def _build_result(self, verdict: RuleVerdict) -> RuleResult:
        score = score_from_verdict(verdict)
        passed = verdict == "PASS"
        conf, risk = confidence_risk_for_pass(passed)
        label = "가속" if self.trend == "increasing" else "감속"
        return RuleResult(
            rule_id=self.rule_id,
            verdict=verdict,
            score=score,
            confidence_delta=conf,
            risk_delta=risk,
            reasons=[f"{self.ma_type.upper()}{self.period} 기울기 {label}"],
            metadata=dict(self._calculation),
        )


class MaFlatRule(BaseRule):
    """PASS when MA slope is near zero (flat)."""

    rule_id: str
    rule_name: str
    ma_type: MaType = "sma"
    period: int = DEFAULT_SLOPE_PERIOD
    lookback: int = DEFAULT_SLOPE_LOOKBACK
    flat_threshold_pct: float = FLAT_SLOPE_THRESHOLD_PCT

    def default_parameters(self) -> dict[str, Any]:
        return {
            "ma_type": self.ma_type,
            "period": self.period,
            "lookback": self.lookback,
            "flat_threshold_pct": self.flat_threshold_pct,
        }

    def validate_input(self, df: pd.DataFrame) -> bool:
        if df is None or df.empty:
            return False
        lookback = int(self._parameters["lookback"])
        period = int(self._parameters["period"])
        if len(df) <= lookback:
            return False
        column = _ma_column(self.ma_type, period)
        if column not in df.columns:
            return False
        window = df[column].iloc[-lookback - 1 :]
        return not pd.isna(window).any()

    def calculate(self, df: pd.DataFrame) -> dict[str, Any]:
        lookback = int(self._parameters["lookback"])
        period = int(self._parameters["period"])
        threshold = float(self._parameters["flat_threshold_pct"])
        column = _ma_column(self.ma_type, period)
        slope = _slope_pct(df[column], lookback)
        passed = abs(slope) <= threshold
        return {
            "slope_pct": round(slope, 4),
            "flat_threshold_pct": threshold,
            "passed": passed,
        }

    def evaluate(self, df: pd.DataFrame) -> RuleVerdict:
        _ = df
        return "PASS" if self._calculation.get("passed") else "FAIL"

    def _build_result(self, verdict: RuleVerdict) -> RuleResult:
        score = score_from_verdict(verdict)
        passed = verdict == "PASS"
        conf, risk = confidence_risk_for_pass(passed)
        return RuleResult(
            rule_id=self.rule_id,
            verdict=verdict,
            score=score,
            confidence_delta=conf,
            risk_delta=risk,
            reasons=[f"{self.ma_type.upper()}{self.period} 횡보(기울기 ≈ 0)"],
            metadata=dict(self._calculation),
        )


class MaTurningRule(BaseRule):
    """PASS when MA slope changes sign (turning point)."""

    rule_id: str
    rule_name: str
    ma_type: MaType = "sma"
    period: int = DEFAULT_SLOPE_PERIOD
    lookback: int = DEFAULT_SLOPE_LOOKBACK

    def default_parameters(self) -> dict[str, Any]:
        return {
            "ma_type": self.ma_type,
            "period": self.period,
            "lookback": self.lookback,
        }

    def validate_input(self, df: pd.DataFrame) -> bool:
        if df is None or df.empty:
            return False
        lookback = int(self._parameters["lookback"])
        period = int(self._parameters["period"])
        if len(df) <= lookback * 2:
            return False
        column = _ma_column(self.ma_type, period)
        if column not in df.columns:
            return False
        window = df[column].iloc[-lookback * 2 - 1 :]
        return not pd.isna(window).any()

    def calculate(self, df: pd.DataFrame) -> dict[str, Any]:
        lookback = int(self._parameters["lookback"])
        period = int(self._parameters["period"])
        column = _ma_column(self.ma_type, period)
        current = _slope_pct(df[column], lookback)
        previous = _slope_pct(df[column].iloc[:-lookback], lookback)
        turned = (current > 0.0 > previous) or (current < 0.0 < previous)
        return {
            "current_slope_pct": round(current, 4),
            "previous_slope_pct": round(previous, 4),
            "turned": turned,
            "passed": turned,
        }

    def evaluate(self, df: pd.DataFrame) -> RuleVerdict:
        _ = df
        return "PASS" if self._calculation.get("passed") else "FAIL"

    def _build_result(self, verdict: RuleVerdict) -> RuleResult:
        score = score_from_verdict(verdict)
        passed = verdict == "PASS"
        conf, risk = confidence_risk_for_pass(passed)
        return RuleResult(
            rule_id=self.rule_id,
            verdict=verdict,
            score=score,
            confidence_delta=conf,
            risk_delta=risk,
            reasons=[f"{self.ma_type.upper()}{self.period} 기울기 전환"],
            metadata=dict(self._calculation),
        )


def run_slope_rule(rule_cls: type[BaseRule], df: pd.DataFrame) -> RuleResult:
    """Run slope rule class."""
    rule = rule_cls()
    rule.initialize()
    return rule.run(df)
