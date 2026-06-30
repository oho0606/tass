"""Shared helpers for VL absolute volume rules (VL0001–VL0010)."""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from engine.core.rule_base import BaseRule
from engine.core.types import RuleResult, RuleVerdict
from engine.rules.vl._helpers import (
    AT_EXTREME_TOLERANCE_PCT,
    DEFAULT_N_PERIOD,
    near_equal,
    period_high,
    period_low,
    validate_volume_df,
    volume_avg,
)
from engine.rules.vl._scoring import confidence_risk_for_pass, score_from_verdict

AbsoluteMode = Literal[
    "above_avg",
    "below_avg",
    "equal_avg",
    "above_prior",
    "below_prior",
    "equal_prior",
    "above_high",
    "below_low",
    "at_high",
    "at_low",
]


class AbsoluteVolumeRule(BaseRule):
    """PASS when absolute volume satisfies comparison mode."""

    rule_id: str
    rule_name: str
    mode: AbsoluteMode
    period: int = DEFAULT_N_PERIOD

    def default_parameters(self) -> dict[str, Any]:
        return {"mode": self.mode, "period": self.period}

    def validate_input(self, df: pd.DataFrame) -> bool:
        period = int(self._parameters["period"])
        return validate_volume_df(df, min_bars=period + 1)

    def calculate(self, df: pd.DataFrame) -> dict[str, Any]:
        period = int(self._parameters["period"])
        mode = self._parameters["mode"]
        current = float(df["volume"].iloc[-1])
        prior = float(df["volume"].iloc[-2])
        avg = volume_avg(df, period)
        high = period_high(df, period)
        low = period_low(df, period)

        passed = False
        if mode == "above_avg":
            passed = current > avg
        elif mode == "below_avg":
            passed = current < avg
        elif mode == "equal_avg":
            passed = near_equal(current, avg)
        elif mode == "above_prior":
            passed = current > prior
        elif mode == "below_prior":
            passed = current < prior
        elif mode == "equal_prior":
            passed = near_equal(current, prior)
        elif mode == "above_high":
            passed = current > high
        elif mode == "below_low":
            passed = current < low
        elif mode == "at_high":
            passed = near_equal(current, high, AT_EXTREME_TOLERANCE_PCT)
        else:
            passed = near_equal(current, low, AT_EXTREME_TOLERANCE_PCT)

        return {
            "volume": current,
            "prior_volume": prior,
            "average": avg,
            "period_high": high,
            "period_low": low,
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


def run_absolute_rule(rule_cls: type[BaseRule], df: pd.DataFrame) -> RuleResult:
    """Run absolute volume rule class."""
    rule = rule_cls()
    rule.initialize()
    return rule.run(df)
