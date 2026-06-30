"""Shared helpers for VL volume spike rules (VL0031–VL0040)."""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from engine.core.rule_base import BaseRule
from engine.core.types import RuleResult, RuleVerdict
from engine.rules.vl._helpers import (
    DEFAULT_N_PERIOD,
    SPIKE_MULTIPLIER,
    SPIKE_THRESHOLD,
    SUDDEN_CHANGE_PCT,
    SLOPE_LOOKBACK,
    validate_volume_df,
    volume_avg,
    volume_slope_pct,
)
from engine.rules.vl._scoring import confidence_risk_for_pass, score_from_verdict

SpikeTrend = Literal["expansion", "contraction"]


class VolumeSpikeRule(BaseRule):
    """PASS when volume exceeds average by spike multiplier."""

    rule_id: str
    rule_name: str
    multiplier: float = SPIKE_MULTIPLIER

    def default_parameters(self) -> dict[str, Any]:
        return {"multiplier": self.multiplier, "period": DEFAULT_N_PERIOD}

    def validate_input(self, df: pd.DataFrame) -> bool:
        return validate_volume_df(df)

    def calculate(self, df: pd.DataFrame) -> dict[str, Any]:
        multiplier = float(self._parameters["multiplier"])
        current = float(df["volume"].iloc[-1])
        avg = volume_avg(df)
        passed = current >= avg * multiplier
        return {"volume": current, "average": avg, "multiplier": multiplier, "passed": passed}

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


class SpikeThresholdRule(BaseRule):
    """PASS when relative volume exceeds spike threshold."""

    rule_id: str
    rule_name: str
    threshold: float = SPIKE_THRESHOLD

    def default_parameters(self) -> dict[str, Any]:
        return {"threshold": self.threshold}

    def validate_input(self, df: pd.DataFrame) -> bool:
        return validate_volume_df(df)

    def calculate(self, df: pd.DataFrame) -> dict[str, Any]:
        threshold = float(self._parameters["threshold"])
        avg = volume_avg(df)
        current = float(df["volume"].iloc[-1])
        rel = current / avg if avg else 0.0
        passed = rel >= threshold
        return {"relative_volume": round(rel, 4), "threshold": threshold, "passed": passed}

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


class SuddenVolumeChangeRule(BaseRule):
    """PASS when volume changes suddenly vs prior bar."""

    rule_id: str
    rule_name: str
    direction: Literal["increase", "decrease"]
    change_pct: float = SUDDEN_CHANGE_PCT

    def default_parameters(self) -> dict[str, Any]:
        return {"direction": self.direction, "change_pct": self.change_pct}

    def validate_input(self, df: pd.DataFrame) -> bool:
        return validate_volume_df(df, min_bars=2)

    def calculate(self, df: pd.DataFrame) -> dict[str, Any]:
        change_pct = float(self._parameters["change_pct"])
        current = float(df["volume"].iloc[-1])
        prior = float(df["volume"].iloc[-2])
        pct = ((current - prior) / prior * 100.0) if prior else 0.0
        direction = self._parameters["direction"]
        passed = pct >= change_pct if direction == "increase" else pct <= -change_pct
        return {"change_pct": round(pct, 4), "passed": passed}

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


class VolumeSpreadTrendRule(BaseRule):
    """PASS when volume average spread expands or contracts."""

    rule_id: str
    rule_name: str
    trend: SpikeTrend
    lookback: int = SLOPE_LOOKBACK

    def default_parameters(self) -> dict[str, Any]:
        return {"trend": self.trend, "lookback": self.lookback}

    def validate_input(self, df: pd.DataFrame) -> bool:
        lookback = int(self._parameters["lookback"])
        return validate_volume_df(df, min_bars=lookback * 2 + DEFAULT_N_PERIOD)

    def _avg_spread(self, frame: pd.DataFrame) -> float:
        short = float(frame["volume"].iloc[-5:].mean())
        long = volume_avg(frame)
        return abs(short - long)

    def calculate(self, df: pd.DataFrame) -> dict[str, Any]:
        lookback = int(self._parameters["lookback"])
        current = self._avg_spread(df)
        previous = self._avg_spread(df.iloc[:-lookback])
        delta = current - previous
        passed = delta > 0.0 if self.trend == "expansion" else delta < 0.0
        return {"current_spread": round(current, 4), "delta": round(delta, 4), "passed": passed}

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


class VolumeClimaxRule(BaseRule):
    """PASS when volume is at climax level (very high relative volume)."""

    rule_id: str
    rule_name: str
    climax_multiplier: float = 3.0

    def default_parameters(self) -> dict[str, Any]:
        return {"climax_multiplier": self.climax_multiplier}

    def validate_input(self, df: pd.DataFrame) -> bool:
        return validate_volume_df(df)

    def calculate(self, df: pd.DataFrame) -> dict[str, Any]:
        multiplier = float(self._parameters["climax_multiplier"])
        current = float(df["volume"].iloc[-1])
        avg = volume_avg(df)
        passed = current >= avg * multiplier
        return {"volume": current, "average": avg, "passed": passed}

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


class VolumeDryUpRule(BaseRule):
    """PASS when volume dries up (well below average)."""

    rule_id: str
    rule_name: str
    dry_multiplier: float = 0.5

    def default_parameters(self) -> dict[str, Any]:
        return {"dry_multiplier": self.dry_multiplier}

    def validate_input(self, df: pd.DataFrame) -> bool:
        return validate_volume_df(df)

    def calculate(self, df: pd.DataFrame) -> dict[str, Any]:
        multiplier = float(self._parameters["dry_multiplier"])
        current = float(df["volume"].iloc[-1])
        avg = volume_avg(df)
        passed = current <= avg * multiplier
        return {"volume": current, "average": avg, "passed": passed}

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


class SpikeCompareRule(BaseRule):
    """PASS when current spike is above or below prior spike."""

    rule_id: str
    rule_name: str
    comparison: Literal["above_prior", "below_prior"]
    multiplier: float = SPIKE_MULTIPLIER

    def default_parameters(self) -> dict[str, Any]:
        return {"comparison": self.comparison, "multiplier": self.multiplier}

    def validate_input(self, df: pd.DataFrame) -> bool:
        return validate_volume_df(df, min_bars=DEFAULT_N_PERIOD + 2)

    def calculate(self, df: pd.DataFrame) -> dict[str, Any]:
        multiplier = float(self._parameters["multiplier"])
        current = float(df["volume"].iloc[-1])
        prior = float(df["volume"].iloc[-2])
        avg = volume_avg(df)
        current_spike = current / avg if avg else 0.0
        prior_spike = prior / avg if avg else 0.0
        is_spike = current_spike >= multiplier
        comparison = self._parameters["comparison"]
        if comparison == "above_prior":
            passed = is_spike and current_spike > prior_spike
        else:
            passed = is_spike and current_spike < prior_spike
        return {
            "current_spike": round(current_spike, 4),
            "prior_spike": round(prior_spike, 4),
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


def run_spike_rule(rule_cls: type[BaseRule], df: pd.DataFrame) -> RuleResult:
    """Run volume spike rule class."""
    rule = rule_cls()
    rule.initialize()
    return rule.run(df)
