"""Shared helpers for VL relative volume rules (VL0011–VL0020)."""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from engine.core.rule_base import BaseRule
from engine.core.types import RuleResult, RuleVerdict
from engine.rules.vl._helpers import (
    DEFAULT_N_PERIOD,
    RELATIVE_THRESHOLD,
    near_equal,
    relative_volume_value,
    validate_volume_df,
)
from engine.rules.vl._scoring import confidence_risk_for_pass, score_from_verdict

RelativeMode = Literal[
    "above_1",
    "below_1",
    "equal_1",
    "above_2",
    "above_threshold",
    "below_threshold",
    "above_prior",
    "below_prior",
    "at_avg",
    "at_high",
]


class RelativeVolumeRule(BaseRule):
    """PASS when relative volume satisfies comparison mode."""

    rule_id: str
    rule_name: str
    mode: RelativeMode
    period: int = DEFAULT_N_PERIOD
    threshold: float = RELATIVE_THRESHOLD

    def default_parameters(self) -> dict[str, Any]:
        return {"mode": self.mode, "period": self.period, "threshold": self.threshold}

    def validate_input(self, df: pd.DataFrame) -> bool:
        period = int(self._parameters["period"])
        return validate_volume_df(df, min_bars=period + 1)

    def calculate(self, df: pd.DataFrame) -> dict[str, Any]:
        period = int(self._parameters["period"])
        mode = self._parameters["mode"]
        threshold = float(self._parameters["threshold"])
        current = relative_volume_value(df, period)
        prior = relative_volume_value(df.iloc[:-1], period) if len(df) > period + 1 else current

        passed = False
        if mode == "above_1":
            passed = current > 1.0
        elif mode == "below_1":
            passed = current < 1.0
        elif mode == "equal_1":
            passed = near_equal(current, 1.0)
        elif mode == "above_2":
            passed = current > 2.0
        elif mode == "above_threshold":
            passed = current > threshold
        elif mode == "below_threshold":
            passed = current < threshold
        elif mode == "above_prior":
            passed = current > prior
        elif mode == "below_prior":
            passed = current < prior
        elif mode == "at_avg":
            passed = near_equal(current, 1.0)
        else:
            rel_high = max(
                relative_volume_value(df.iloc[: i + 1], period) for i in range(period, len(df))
            )
            passed = near_equal(current, rel_high, 1.0)

        return {
            "relative_volume": round(current, 4),
            "prior_relative_volume": round(prior, 4),
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


def run_relative_rule(rule_cls: type[BaseRule], df: pd.DataFrame) -> RuleResult:
    """Run relative volume rule class."""
    rule = rule_cls()
    rule.initialize()
    return rule.run(df)
