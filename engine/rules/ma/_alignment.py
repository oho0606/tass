"""Shared helpers for MA alignment rules (MA0021–MA0030)."""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from engine.core.rule_base import BaseRule
from engine.core.types import RuleResult, RuleVerdict
from engine.rules.ma._helpers import MaType
from engine.rules.ma._scoring import confidence_risk_for_pass, score_from_verdict

AlignmentDirection = Literal["bullish", "bearish"]
TrendDirection = Literal["improving", "weakening"]
DEFAULT_PERIODS = (5, 20, 60, 120, 240)


def _ma_column(ma_type: MaType, period: int) -> str:
    prefix = "ma" if ma_type == "sma" else "ema"
    return f"{prefix}_{period}"


def _alignment_pairs(values: list[float], direction: AlignmentDirection) -> list[bool]:
    if direction == "bullish":
        return [values[i] > values[i + 1] for i in range(len(values) - 1)]
    return [values[i] < values[i + 1] for i in range(len(values) - 1)]


class AlignmentRule(BaseRule):
    """PASS when MAs are in bullish or bearish order."""

    rule_id: str
    rule_name: str
    ma_type: MaType
    direction: AlignmentDirection
    periods: tuple[int, ...] = DEFAULT_PERIODS

    def default_parameters(self) -> dict[str, Any]:
        return {"periods": self.periods, "direction": self.direction, "ma_type": self.ma_type}

    def validate_input(self, df: pd.DataFrame) -> bool:
        if df is None or df.empty:
            return False
        periods = self._parameters["periods"]
        if len(df) < max(periods):
            return False
        for period in periods:
            column = _ma_column(self.ma_type, period)
            if column not in df.columns or pd.isna(df[column].iloc[-1]):
                return False
        return True

    def calculate(self, df: pd.DataFrame) -> dict[str, Any]:
        periods = self._parameters["periods"]
        direction = self._parameters["direction"]
        values = [float(df[_ma_column(self.ma_type, period)].iloc[-1]) for period in periods]
        ordered = _alignment_pairs(values, direction)
        aligned_count = sum(1 for ok in ordered if ok)
        return {
            "values": dict(zip(periods, values, strict=True)),
            "aligned_pairs": aligned_count,
            "full_alignment": all(ordered),
            "partial_alignment": aligned_count >= len(periods) - 2,
        }

    def evaluate(self, df: pd.DataFrame) -> RuleVerdict:
        _ = df
        if self._calculation.get("full_alignment"):
            return "PASS"
        if self._calculation.get("partial_alignment"):
            return "PARTIAL"
        return "FAIL"

    def _build_result(self, verdict: RuleVerdict) -> RuleResult:
        score = score_from_verdict("PASS" if verdict == "PASS" else "FAIL")
        if verdict == "PARTIAL":
            score = 5.0
        passed = verdict == "PASS"
        conf, risk = confidence_risk_for_pass(passed)
        label = "정배열" if self.direction == "bullish" else "역배열"
        ma_label = self.ma_type.upper()
        reasons: list[str] = []
        if verdict == "PASS":
            reasons.append(f"{ma_label} {label}")
        elif verdict == "PARTIAL":
            reasons.append(f"{ma_label} 부분 {label}")
        else:
            reasons.append(f"{ma_label} {label} 미충족")
        return RuleResult(
            rule_id=self.rule_id,
            verdict=verdict,
            score=score,
            confidence_delta=conf,
            risk_delta=risk,
            reasons=reasons,
            metadata=dict(self._calculation),
        )


class AlignmentTrendRule(BaseRule):
    """PASS when alignment strength is improving or weakening."""

    rule_id: str
    rule_name: str
    ma_type: MaType
    trend: TrendDirection
    periods: tuple[int, ...] = DEFAULT_PERIODS
    lookback: int = 5

    def default_parameters(self) -> dict[str, Any]:
        return {
            "periods": self.periods,
            "lookback": self.lookback,
            "ma_type": self.ma_type,
            "trend": self.trend,
        }

    def validate_input(self, df: pd.DataFrame) -> bool:
        if df is None or df.empty:
            return False
        periods = self._parameters["periods"]
        lookback = int(self._parameters["lookback"])
        if len(df) <= lookback or len(df) < max(periods):
            return False
        for period in periods:
            column = _ma_column(self.ma_type, period)
            if column not in df.columns:
                return False
        return True

    def _aligned_count(self, frame: pd.DataFrame, direction: AlignmentDirection) -> int:
        periods = self._parameters["periods"]
        values = [float(frame[_ma_column(self.ma_type, period)].iloc[-1]) for period in periods]
        return sum(1 for ok in _alignment_pairs(values, direction) if ok)

    def calculate(self, df: pd.DataFrame) -> dict[str, Any]:
        lookback = int(self._parameters["lookback"])
        direction: AlignmentDirection = "bullish"
        current = self._aligned_count(df, direction)
        previous = self._aligned_count(df.iloc[:-lookback], direction)
        delta = current - previous
        passed = delta > 0 if self.trend == "improving" else delta < 0
        return {
            "current_aligned_pairs": current,
            "previous_aligned_pairs": previous,
            "delta": delta,
            "passed": passed,
        }

    def evaluate(self, df: pd.DataFrame) -> RuleVerdict:
        _ = df
        return "PASS" if self._calculation.get("passed") else "FAIL"

    def _build_result(self, verdict: RuleVerdict) -> RuleResult:
        score = score_from_verdict(verdict)
        passed = verdict == "PASS"
        conf, risk = confidence_risk_for_pass(passed)
        trend_label = "강화" if self.trend == "improving" else "약화"
        return RuleResult(
            rule_id=self.rule_id,
            verdict=verdict,
            score=score,
            confidence_delta=conf,
            risk_delta=risk,
            reasons=[f"{self.ma_type.upper()} 정배열 {trend_label}"],
            metadata=dict(self._calculation),
        )


class FullAlignmentRule(BaseRule):
    """PASS when both SMA and EMA are fully aligned."""

    rule_id: str
    rule_name: str
    direction: AlignmentDirection
    periods: tuple[int, ...] = DEFAULT_PERIODS

    def default_parameters(self) -> dict[str, Any]:
        return {"periods": self.periods, "direction": self.direction}

    def validate_input(self, df: pd.DataFrame) -> bool:
        if df is None or df.empty or len(df) < max(self.periods):
            return False
        for ma_type in ("sma", "ema"):
            for period in self.periods:
                column = _ma_column(ma_type, period)
                if column not in df.columns or pd.isna(df[column].iloc[-1]):
                    return False
        return True

    def _is_full(self, df: pd.DataFrame, ma_type: MaType) -> bool:
        values = [float(df[_ma_column(ma_type, period)].iloc[-1]) for period in self.periods]
        return all(_alignment_pairs(values, self.direction))

    def calculate(self, df: pd.DataFrame) -> dict[str, Any]:
        sma_full = self._is_full(df, "sma")
        ema_full = self._is_full(df, "ema")
        return {"sma_full": sma_full, "ema_full": ema_full, "passed": sma_full and ema_full}

    def evaluate(self, df: pd.DataFrame) -> RuleVerdict:
        _ = df
        return "PASS" if self._calculation.get("passed") else "FAIL"

    def _build_result(self, verdict: RuleVerdict) -> RuleResult:
        score = score_from_verdict(verdict)
        passed = verdict == "PASS"
        conf, risk = confidence_risk_for_pass(passed)
        label = "정배열" if self.direction == "bullish" else "역배열"
        return RuleResult(
            rule_id=self.rule_id,
            verdict=verdict,
            score=score,
            confidence_delta=conf,
            risk_delta=risk,
            reasons=[f"SMA+EMA 완전 {label}"],
            metadata=dict(self._calculation),
        )


def run_alignment_rule(rule_cls: type[BaseRule], df: pd.DataFrame) -> RuleResult:
    """Run alignment rule class."""
    rule = rule_cls()
    rule.initialize()
    return rule.run(df)
