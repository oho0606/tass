"""Shared helpers for VL volume trend rules (VL0021–VL0030)."""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from engine.core.rule_base import BaseRule
from engine.core.types import RuleResult, RuleVerdict
from engine.rules.vl._helpers import (
    CONSECUTIVE_BARS,
    FLAT_SLOPE_THRESHOLD_PCT,
    SLOPE_LOOKBACK,
    validate_volume_df,
    volume_slope_pct,
)
from engine.rules.vl._scoring import confidence_risk_for_pass, score_from_verdict

VolumeDirection = Literal["rising", "falling"]
SlopeTrend = Literal["increasing", "decreasing"]
ConsecutiveMode = Literal["higher", "lower"]


class VolumeDirectionRule(BaseRule):
    """PASS when volume trend direction matches rule."""

    rule_id: str
    rule_name: str
    direction: VolumeDirection
    lookback: int = SLOPE_LOOKBACK

    def default_parameters(self) -> dict[str, Any]:
        return {"direction": self.direction, "lookback": self.lookback}

    def validate_input(self, df: pd.DataFrame) -> bool:
        lookback = int(self._parameters["lookback"])
        return validate_volume_df(df, min_bars=lookback + 2)

    def calculate(self, df: pd.DataFrame) -> dict[str, Any]:
        lookback = int(self._parameters["lookback"])
        slope = volume_slope_pct(df["volume"], lookback)
        direction = self._parameters["direction"]
        passed = slope > 0.0 if direction == "rising" else slope < 0.0
        return {"slope_pct": round(slope, 4), "passed": passed}

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
            reasons=[self.rule_name],
            metadata=dict(self._calculation),
        )


class VolumeSlopeTrendRule(BaseRule):
    """PASS when volume slope is accelerating or decelerating."""

    rule_id: str
    rule_name: str
    trend: SlopeTrend
    lookback: int = SLOPE_LOOKBACK

    def default_parameters(self) -> dict[str, Any]:
        return {"trend": self.trend, "lookback": self.lookback}

    def validate_input(self, df: pd.DataFrame) -> bool:
        lookback = int(self._parameters["lookback"])
        return validate_volume_df(df, min_bars=lookback * 2 + 2)

    def calculate(self, df: pd.DataFrame) -> dict[str, Any]:
        lookback = int(self._parameters["lookback"])
        current = volume_slope_pct(df["volume"], lookback)
        previous = volume_slope_pct(df["volume"].iloc[:-lookback], lookback)
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
        return RuleResult(
            rule_id=self.rule_id,
            verdict=verdict,
            score=score,
            confidence_delta=conf,
            risk_delta=risk,
            reasons=[self.rule_name],
            metadata=dict(self._calculation),
        )


class ConsecutiveVolumeRule(BaseRule):
    """PASS when volume rises or falls for consecutive bars."""

    rule_id: str
    rule_name: str
    mode: ConsecutiveMode
    bars: int = CONSECUTIVE_BARS

    def default_parameters(self) -> dict[str, Any]:
        return {"mode": self.mode, "bars": self.bars}

    def validate_input(self, df: pd.DataFrame) -> bool:
        bars = int(self._parameters["bars"])
        return validate_volume_df(df, min_bars=bars + 1)

    def calculate(self, df: pd.DataFrame) -> dict[str, Any]:
        bars = int(self._parameters["bars"])
        mode = self._parameters["mode"]
        volumes = [float(v) for v in df["volume"].iloc[-bars - 1 :].tolist()]
        comparisons = [
            volumes[i] > volumes[i - 1] if mode == "higher" else volumes[i] < volumes[i - 1]
            for i in range(1, len(volumes))
        ]
        passed = len(comparisons) == bars and all(comparisons)
        return {"bars": bars, "passed": passed}

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
            reasons=[self.rule_name],
            metadata=dict(self._calculation),
        )


class VolumeFlatRule(BaseRule):
    """PASS when volume slope is near zero."""

    rule_id: str
    rule_name: str
    lookback: int = SLOPE_LOOKBACK
    flat_threshold_pct: float = FLAT_SLOPE_THRESHOLD_PCT

    def default_parameters(self) -> dict[str, Any]:
        return {"lookback": self.lookback, "flat_threshold_pct": self.flat_threshold_pct}

    def validate_input(self, df: pd.DataFrame) -> bool:
        lookback = int(self._parameters["lookback"])
        return validate_volume_df(df, min_bars=lookback + 2)

    def calculate(self, df: pd.DataFrame) -> dict[str, Any]:
        lookback = int(self._parameters["lookback"])
        threshold = float(self._parameters["flat_threshold_pct"])
        slope = volume_slope_pct(df["volume"], lookback)
        passed = abs(slope) <= threshold
        return {"slope_pct": round(slope, 4), "passed": passed}

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
            reasons=[self.rule_name],
            metadata=dict(self._calculation),
        )


class VolumeTurningRule(BaseRule):
    """PASS when volume slope changes sign."""

    rule_id: str
    rule_name: str
    lookback: int = SLOPE_LOOKBACK

    def default_parameters(self) -> dict[str, Any]:
        return {"lookback": self.lookback}

    def validate_input(self, df: pd.DataFrame) -> bool:
        lookback = int(self._parameters["lookback"])
        return validate_volume_df(df, min_bars=lookback * 2 + 2)

    def calculate(self, df: pd.DataFrame) -> dict[str, Any]:
        lookback = int(self._parameters["lookback"])
        current = volume_slope_pct(df["volume"], lookback)
        previous = volume_slope_pct(df["volume"].iloc[:-lookback], lookback)
        turned = (current > 0.0 > previous) or (current < 0.0 < previous)
        return {
            "current_slope_pct": round(current, 4),
            "previous_slope_pct": round(previous, 4),
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
            reasons=[self.rule_name],
            metadata=dict(self._calculation),
        )


def run_trend_rule(rule_cls: type[BaseRule], df: pd.DataFrame) -> RuleResult:
    """Run volume trend rule class."""
    rule = rule_cls()
    rule.initialize()
    return rule.run(df)
