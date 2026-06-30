"""Shared helpers for MA distance and structure rules (MA0051–MA0060)."""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from engine.core.rule_base import BaseRule
from engine.core.types import RuleResult, RuleVerdict
from engine.rules.ma._alignment import DEFAULT_PERIODS, _alignment_pairs, _ma_column
from engine.rules.ma._helpers import MaType
from engine.rules.ma._scoring import confidence_risk_for_pass, score_from_verdict

SpreadTrend = Literal["compression", "expansion"]
DEFAULT_REFERENCE_PERIOD = 20
DEFAULT_SHORT_PERIOD = 5
DEFAULT_LONG_PERIOD = 60
EXTENDED_DISTANCE_PCT = 5.0
NEAR_DISTANCE_PCT = 1.5
CONVERGENCE_SPREAD_PCT = 2.0
DIVERGENCE_SPREAD_PCT = 8.0
SPREAD_LOOKBACK = 5
SUPPORT_TOLERANCE_PCT = 1.0
STRUCTURE_LOOKBACK = 5


def _distance_pct(close: float, ma_value: float) -> float:
    if ma_value == 0.0:
        return 0.0
    return (close - ma_value) / ma_value * 100.0


def _spread_pct(short_ma: float, long_ma: float) -> float:
    if long_ma == 0.0:
        return 0.0
    return abs(short_ma - long_ma) / long_ma * 100.0


class PriceDistanceRule(BaseRule):
    """PASS when price distance from MA matches extended/near criteria."""

    rule_id: str
    rule_name: str
    mode: Literal["extended_above", "extended_below", "near"]
    ma_type: MaType = "sma"
    period: int = DEFAULT_REFERENCE_PERIOD
    extended_pct: float = EXTENDED_DISTANCE_PCT
    near_pct: float = NEAR_DISTANCE_PCT

    def default_parameters(self) -> dict[str, Any]:
        return {
            "mode": self.mode,
            "ma_type": self.ma_type,
            "period": self.period,
            "extended_pct": self.extended_pct,
            "near_pct": self.near_pct,
        }

    def validate_input(self, df: pd.DataFrame) -> bool:
        if df is None or df.empty:
            return False
        period = int(self._parameters["period"])
        if len(df) < period:
            return False
        if "close" not in df.columns:
            return False
        column = _ma_column(self.ma_type, period)
        if column not in df.columns:
            return False
        if pd.isna(df["close"].iloc[-1]) or pd.isna(df[column].iloc[-1]):
            return False
        return True

    def calculate(self, df: pd.DataFrame) -> dict[str, Any]:
        period = int(self._parameters["period"])
        column = _ma_column(self.ma_type, period)
        close = float(df["close"].iloc[-1])
        ma_value = float(df[column].iloc[-1])
        distance = _distance_pct(close, ma_value)
        mode = self._parameters["mode"]
        extended = float(self._parameters["extended_pct"])
        near = float(self._parameters["near_pct"])
        if mode == "extended_above":
            passed = distance >= extended
        elif mode == "extended_below":
            passed = distance <= -extended
        else:
            passed = abs(distance) <= near
        return {
            "close": close,
            "ma_value": ma_value,
            "distance_pct": round(distance, 4),
            "passed": passed,
        }

    def evaluate(self, df: pd.DataFrame) -> RuleVerdict:
        _ = df
        return "PASS" if self._calculation.get("passed") else "FAIL"

    def _build_result(self, verdict: RuleVerdict) -> RuleResult:
        score = score_from_verdict(verdict)
        passed = verdict == "PASS"
        conf, risk = confidence_risk_for_pass(passed)
        labels = {
            "extended_above": "MA 상단 과열",
            "extended_below": "MA 하단 과열",
            "near": "MA 근접",
        }
        return RuleResult(
            rule_id=self.rule_id,
            verdict=verdict,
            score=score,
            confidence_delta=conf,
            risk_delta=risk,
            reasons=[labels[self.mode]],
            metadata=dict(self._calculation),
        )


class MaSpreadTrendRule(BaseRule):
    """PASS when short/long MA spread is compressing or expanding."""

    rule_id: str
    rule_name: str
    trend: SpreadTrend
    ma_type: MaType = "sma"
    short_period: int = DEFAULT_SHORT_PERIOD
    long_period: int = DEFAULT_LONG_PERIOD
    lookback: int = SPREAD_LOOKBACK

    def default_parameters(self) -> dict[str, Any]:
        return {
            "trend": self.trend,
            "ma_type": self.ma_type,
            "short_period": self.short_period,
            "long_period": self.long_period,
            "lookback": self.lookback,
        }

    def validate_input(self, df: pd.DataFrame) -> bool:
        if df is None or df.empty:
            return False
        lookback = int(self._parameters["lookback"])
        short_period = int(self._parameters["short_period"])
        long_period = int(self._parameters["long_period"])
        if len(df) <= lookback or len(df) < long_period:
            return False
        for period in (short_period, long_period):
            column = _ma_column(self.ma_type, period)
            if column not in df.columns:
                return False
        return True

    def _current_spread(self, frame: pd.DataFrame) -> float:
        short_period = int(self._parameters["short_period"])
        long_period = int(self._parameters["long_period"])
        short_col = _ma_column(self.ma_type, short_period)
        long_col = _ma_column(self.ma_type, long_period)
        return _spread_pct(float(frame[short_col].iloc[-1]), float(frame[long_col].iloc[-1]))

    def calculate(self, df: pd.DataFrame) -> dict[str, Any]:
        lookback = int(self._parameters["lookback"])
        current = self._current_spread(df)
        previous = self._current_spread(df.iloc[:-lookback])
        delta = current - previous
        passed = delta < 0.0 if self.trend == "compression" else delta > 0.0
        return {
            "current_spread_pct": round(current, 4),
            "previous_spread_pct": round(previous, 4),
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
        label = "수렴 진행" if self.trend == "compression" else "확장 진행"
        return RuleResult(
            rule_id=self.rule_id,
            verdict=verdict,
            score=score,
            confidence_delta=conf,
            risk_delta=risk,
            reasons=[f"MA {label}"],
            metadata=dict(self._calculation),
        )


class MaSpreadLevelRule(BaseRule):
    """PASS when short/long MA spread is below (convergence) or above (divergence) threshold."""

    rule_id: str
    rule_name: str
    level: Literal["convergence", "divergence"]
    ma_type: MaType = "sma"
    short_period: int = DEFAULT_SHORT_PERIOD
    long_period: int = DEFAULT_LONG_PERIOD
    convergence_pct: float = CONVERGENCE_SPREAD_PCT
    divergence_pct: float = DIVERGENCE_SPREAD_PCT

    def default_parameters(self) -> dict[str, Any]:
        return {
            "level": self.level,
            "ma_type": self.ma_type,
            "short_period": self.short_period,
            "long_period": self.long_period,
            "convergence_pct": self.convergence_pct,
            "divergence_pct": self.divergence_pct,
        }

    def validate_input(self, df: pd.DataFrame) -> bool:
        if df is None or df.empty:
            return False
        long_period = int(self._parameters["long_period"])
        if len(df) < long_period:
            return False
        for period in (int(self._parameters["short_period"]), long_period):
            column = _ma_column(self.ma_type, period)
            if column not in df.columns or pd.isna(df[column].iloc[-1]):
                return False
        return True

    def calculate(self, df: pd.DataFrame) -> dict[str, Any]:
        short_period = int(self._parameters["short_period"])
        long_period = int(self._parameters["long_period"])
        short_col = _ma_column(self.ma_type, short_period)
        long_col = _ma_column(self.ma_type, long_period)
        spread = _spread_pct(float(df[short_col].iloc[-1]), float(df[long_col].iloc[-1]))
        level = self._parameters["level"]
        if level == "convergence":
            passed = spread <= float(self._parameters["convergence_pct"])
        else:
            passed = spread >= float(self._parameters["divergence_pct"])
        return {"spread_pct": round(spread, 4), "passed": passed}

    def evaluate(self, df: pd.DataFrame) -> RuleVerdict:
        _ = df
        return "PASS" if self._calculation.get("passed") else "FAIL"

    def _build_result(self, verdict: RuleVerdict) -> RuleResult:
        score = score_from_verdict(verdict)
        passed = verdict == "PASS"
        conf, risk = confidence_risk_for_pass(passed)
        label = "수렴 상태" if self.level == "convergence" else "확장 상태"
        return RuleResult(
            rule_id=self.rule_id,
            verdict=verdict,
            score=score,
            confidence_delta=conf,
            risk_delta=risk,
            reasons=[f"MA {label}"],
            metadata=dict(self._calculation),
        )


class DynamicLevelRule(BaseRule):
    """PASS when price tests MA as dynamic support or resistance and holds."""

    rule_id: str
    rule_name: str
    level: Literal["support", "resistance"]
    ma_type: MaType = "sma"
    period: int = DEFAULT_REFERENCE_PERIOD
    tolerance_pct: float = SUPPORT_TOLERANCE_PCT
    probe_bars: int = 3

    def default_parameters(self) -> dict[str, Any]:
        return {
            "level": self.level,
            "ma_type": self.ma_type,
            "period": self.period,
            "tolerance_pct": self.tolerance_pct,
            "probe_bars": self.probe_bars,
        }

    def validate_input(self, df: pd.DataFrame) -> bool:
        if df is None or df.empty:
            return False
        period = int(self._parameters["period"])
        probe_bars = int(self._parameters["probe_bars"])
        if len(df) < period or len(df) < probe_bars:
            return False
        column = _ma_column(self.ma_type, period)
        required = ("close", "high", "low", column)
        if any(col not in df.columns for col in required):
            return False
        window = df[list(required)].iloc[-probe_bars:]
        return not pd.isna(window).any().any()

    def calculate(self, df: pd.DataFrame) -> dict[str, Any]:
        period = int(self._parameters["period"])
        probe_bars = int(self._parameters["probe_bars"])
        tolerance = float(self._parameters["tolerance_pct"]) / 100.0
        column = _ma_column(self.ma_type, period)
        window = df.iloc[-probe_bars:]
        close = float(df["close"].iloc[-1])
        ma_value = float(df[column].iloc[-1])
        level = self._parameters["level"]

        if level == "support":
            above_ma = close > ma_value
            touched = any(
                float(row["low"]) <= float(row[column]) * (1.0 + tolerance)
                for _, row in window.iterrows()
            )
            passed = above_ma and touched
        else:
            below_ma = close < ma_value
            touched = any(
                float(row["high"]) >= float(row[column]) * (1.0 - tolerance)
                for _, row in window.iterrows()
            )
            passed = below_ma and touched

        return {
            "close": close,
            "ma_value": ma_value,
            "touched": touched,
            "passed": passed,
        }

    def evaluate(self, df: pd.DataFrame) -> RuleVerdict:
        _ = df
        return "PASS" if self._calculation.get("passed") else "FAIL"

    def _build_result(self, verdict: RuleVerdict) -> RuleResult:
        score = score_from_verdict(verdict)
        passed = verdict == "PASS"
        conf, risk = confidence_risk_for_pass(passed)
        label = "동적 지지 유지" if self.level == "support" else "동적 저항 유지"
        return RuleResult(
            rule_id=self.rule_id,
            verdict=verdict,
            score=score,
            confidence_delta=conf,
            risk_delta=risk,
            reasons=[label],
            metadata=dict(self._calculation),
        )


class MaStructureStableRule(BaseRule):
    """PASS when SMA bullish alignment structure is unchanged over lookback."""

    rule_id: str
    rule_name: str
    ma_type: MaType = "sma"
    periods: tuple[int, ...] = DEFAULT_PERIODS
    lookback: int = STRUCTURE_LOOKBACK

    def default_parameters(self) -> dict[str, Any]:
        return {
            "ma_type": self.ma_type,
            "periods": self.periods,
            "lookback": self.lookback,
        }

    def validate_input(self, df: pd.DataFrame) -> bool:
        if df is None or df.empty:
            return False
        lookback = int(self._parameters["lookback"])
        periods = self._parameters["periods"]
        if len(df) <= lookback or len(df) < max(periods):
            return False
        ma_type = self._parameters["ma_type"]
        for period in periods:
            column = _ma_column(ma_type, period)
            if column not in df.columns:
                return False
        return True

    def _aligned_count(self, frame: pd.DataFrame) -> int:
        periods = self._parameters["periods"]
        ma_type = self._parameters["ma_type"]
        values = [float(frame[_ma_column(ma_type, period)].iloc[-1]) for period in periods]
        return sum(1 for ok in _alignment_pairs(values, "bullish") if ok)

    def calculate(self, df: pd.DataFrame) -> dict[str, Any]:
        lookback = int(self._parameters["lookback"])
        current = self._aligned_count(df)
        previous = self._aligned_count(df.iloc[:-lookback])
        stable = current == previous
        return {
            "current_aligned_pairs": current,
            "previous_aligned_pairs": previous,
            "stable": stable,
            "passed": stable,
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
            reasons=["MA 구조 안정"],
            metadata=dict(self._calculation),
        )


def run_structure_rule(rule_cls: type[BaseRule], df: pd.DataFrame) -> RuleResult:
    """Run distance/structure rule class."""
    rule = rule_cls()
    rule.initialize()
    return rule.run(df)
