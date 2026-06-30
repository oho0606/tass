"""Shared helpers for VL volume quality rules (VL0051–VL0060)."""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from engine.core.rule_base import BaseRule
from engine.core.types import RuleResult, RuleVerdict
from engine.rules.vl._helpers import (
    MONEY_FLOW_LOOKBACK,
    SLOPE_LOOKBACK,
    validate_volume_df,
    volume_slope_pct,
)
from engine.rules.vl._scoring import confidence_risk_for_pass, score_from_verdict

ObvDirection = Literal["rising", "falling"]
ObvCompare = Literal["above_prior", "below_prior"]
ObvSlopeTrend = Literal["increasing", "decreasing"]
MoneyFlowDirection = Literal["positive", "negative"]


def _obv_slope(obv: pd.Series, lookback: int = SLOPE_LOOKBACK) -> float:
    return volume_slope_pct(obv, lookback)


class ObvDirectionRule(BaseRule):
    """PASS when OBV slope matches direction."""

    rule_id: str
    rule_name: str
    direction: ObvDirection
    lookback: int = SLOPE_LOOKBACK

    def default_parameters(self) -> dict[str, Any]:
        return {"direction": self.direction, "lookback": self.lookback}

    def validate_input(self, df: pd.DataFrame) -> bool:
        lookback = int(self._parameters["lookback"])
        if not validate_volume_df(df, min_bars=lookback + 2):
            return False
        return "obv" in df.columns and not pd.isna(df["obv"].iloc[-lookback - 1 :]).any()

    def calculate(self, df: pd.DataFrame) -> dict[str, Any]:
        lookback = int(self._parameters["lookback"])
        slope = _obv_slope(df["obv"], lookback)
        direction = self._parameters["direction"]
        passed = slope > 0.0 if direction == "rising" else slope < 0.0
        return {"obv_slope_pct": round(slope, 4), "passed": passed}

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


class ObvCompareRule(BaseRule):
    """PASS when OBV is above or below prior OBV."""

    rule_id: str
    rule_name: str
    comparison: ObvCompare

    def default_parameters(self) -> dict[str, Any]:
        return {"comparison": self.comparison}

    def validate_input(self, df: pd.DataFrame) -> bool:
        if not validate_volume_df(df, min_bars=2):
            return False
        return "obv" in df.columns and not pd.isna(df["obv"].iloc[-2:]).any()

    def calculate(self, df: pd.DataFrame) -> dict[str, Any]:
        current = float(df["obv"].iloc[-1])
        prior = float(df["obv"].iloc[-2])
        comparison = self._parameters["comparison"]
        passed = current > prior if comparison == "above_prior" else current < prior
        return {"obv": current, "prior_obv": prior, "passed": passed}

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


class ObvSlopeTrendRule(BaseRule):
    """PASS when OBV slope is increasing or decreasing."""

    rule_id: str
    rule_name: str
    trend: ObvSlopeTrend
    lookback: int = SLOPE_LOOKBACK

    def default_parameters(self) -> dict[str, Any]:
        return {"trend": self.trend, "lookback": self.lookback}

    def validate_input(self, df: pd.DataFrame) -> bool:
        lookback = int(self._parameters["lookback"])
        if not validate_volume_df(df, min_bars=lookback * 2 + 2):
            return False
        return "obv" in df.columns

    def calculate(self, df: pd.DataFrame) -> dict[str, Any]:
        lookback = int(self._parameters["lookback"])
        current = _obv_slope(df["obv"], lookback)
        previous = _obv_slope(df["obv"].iloc[:-lookback], lookback)
        delta = current - previous
        passed = delta > 0.0 if self.trend == "increasing" else delta < 0.0
        return {"delta": round(delta, 4), "passed": passed}

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


class MoneyFlowRule(BaseRule):
    """PASS when net money flow over lookback is positive or negative."""

    rule_id: str
    rule_name: str
    direction: MoneyFlowDirection
    lookback: int = MONEY_FLOW_LOOKBACK

    def default_parameters(self) -> dict[str, Any]:
        return {"direction": self.direction, "lookback": self.lookback}

    def validate_input(self, df: pd.DataFrame) -> bool:
        lookback = int(self._parameters["lookback"])
        if not validate_volume_df(df, min_bars=lookback + 1):
            return False
        return "money_flow" in df.columns

    def calculate(self, df: pd.DataFrame) -> dict[str, Any]:
        lookback = int(self._parameters["lookback"])
        net = float(df["money_flow"].iloc[-lookback:].sum())
        direction = self._parameters["direction"]
        passed = net > 0.0 if direction == "positive" else net < 0.0
        return {"net_money_flow": round(net, 4), "passed": passed}

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


class VolumeStructureStableRule(BaseRule):
    """PASS when relative volume band is stable over lookback."""

    rule_id: str
    rule_name: str
    lookback: int = SLOPE_LOOKBACK
    stability_pct: float = 5.0

    def default_parameters(self) -> dict[str, Any]:
        return {"lookback": self.lookback, "stability_pct": self.stability_pct}

    def validate_input(self, df: pd.DataFrame) -> bool:
        lookback = int(self._parameters["lookback"])
        return validate_volume_df(df, min_bars=lookback + 2) and "relative_volume" in df.columns

    def calculate(self, df: pd.DataFrame) -> dict[str, Any]:
        lookback = int(self._parameters["lookback"])
        stability = float(self._parameters["stability_pct"])
        window = df["relative_volume"].iloc[-lookback:]
        spread = float(window.max() - window.min())
        passed = spread <= stability
        return {"spread": round(spread, 4), "passed": passed}

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


class VolumePatternConsistentRule(BaseRule):
    """PASS when price-volume agreement pattern holds over lookback."""

    rule_id: str
    rule_name: str
    lookback: int = SLOPE_LOOKBACK
    min_matches: int = 3

    def default_parameters(self) -> dict[str, Any]:
        return {"lookback": self.lookback, "min_matches": self.min_matches}

    def validate_input(self, df: pd.DataFrame) -> bool:
        lookback = int(self._parameters["lookback"])
        return validate_volume_df(df, min_bars=lookback + 2)

    def calculate(self, df: pd.DataFrame) -> dict[str, Any]:
        lookback = int(self._parameters["lookback"])
        min_matches = int(self._parameters["min_matches"])
        matches = 0
        for offset in range(1, lookback + 1):
            idx = -offset
            price_up = float(df["close"].iloc[idx]) > float(df["close"].iloc[idx - 1])
            volume_up = float(df["volume"].iloc[idx]) > float(df["volume"].iloc[idx - 1])
            if price_up == volume_up:
                matches += 1
        passed = matches >= min_matches
        return {"matches": matches, "passed": passed}

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


def run_quality_rule(rule_cls: type[BaseRule], df: pd.DataFrame) -> RuleResult:
    """Run volume quality rule class."""
    rule = rule_cls()
    rule.initialize()
    return rule.run(df)
