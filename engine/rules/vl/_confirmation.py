"""Shared helpers for VL volume confirmation rules (VL0041–VL0050)."""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from engine.core.rule_base import BaseRule
from engine.core.types import RuleResult, RuleVerdict
from engine.rules.vl._helpers import (
    DEFAULT_N_PERIOD,
    is_down_bar,
    is_up_bar,
    validate_volume_df,
    volume_avg,
)
from engine.rules.vl._scoring import confidence_risk_for_pass, score_from_verdict

BarVolumeMode = Literal["up_above_avg", "down_above_avg", "up_below_avg", "down_below_avg"]
PriceVolumeMode = Literal["up_up", "down_up", "up_down", "down_down"]


class BarVolumeRule(BaseRule):
    """PASS when bar direction and volume vs average match mode."""

    rule_id: str
    rule_name: str
    mode: BarVolumeMode
    period: int = DEFAULT_N_PERIOD

    def default_parameters(self) -> dict[str, Any]:
        return {"mode": self.mode, "period": self.period}

    def validate_input(self, df: pd.DataFrame) -> bool:
        return validate_volume_df(df)

    def calculate(self, df: pd.DataFrame) -> dict[str, Any]:
        mode = self._parameters["mode"]
        current = float(df["volume"].iloc[-1])
        avg = volume_avg(df)
        up = is_up_bar(df)
        down = is_down_bar(df)
        above = current > avg
        below = current < avg
        passed = False
        if mode == "up_above_avg":
            passed = up and above
        elif mode == "down_above_avg":
            passed = down and above
        elif mode == "up_below_avg":
            passed = up and below
        else:
            passed = down and below
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


class PriorSameBarVolumeRule(BaseRule):
    """PASS when same-direction bar volume exceeds prior same-direction bar."""

    rule_id: str
    rule_name: str
    bar_direction: Literal["up", "down"]

    def default_parameters(self) -> dict[str, Any]:
        return {"bar_direction": self.bar_direction}

    def validate_input(self, df: pd.DataFrame) -> bool:
        return validate_volume_df(df, min_bars=5)

    def _find_prior_same_bar(self, df: pd.DataFrame, direction: str) -> float | None:
        checker = is_up_bar if direction == "up" else is_down_bar
        if not checker(df):
            return None
        current_vol = float(df["volume"].iloc[-1])
        for offset in range(2, min(len(df), 30)):
            idx = -offset
            slice_df = df.iloc[: len(df) + idx + 1]
            if checker(slice_df):
                return float(slice_df["volume"].iloc[-1])
        return None

    def calculate(self, df: pd.DataFrame) -> dict[str, Any]:
        direction = self._parameters["bar_direction"]
        current = float(df["volume"].iloc[-1])
        prior = self._find_prior_same_bar(df, direction)
        passed = (
            prior is not None
            and current > prior
            and (is_up_bar(df) if direction == "up" else is_down_bar(df))
        )
        return {"volume": current, "prior_same_bar_volume": prior, "passed": passed}

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


class PriceVolumeAgreementRule(BaseRule):
    """PASS when price and volume direction agree."""

    rule_id: str
    rule_name: str
    mode: PriceVolumeMode

    def default_parameters(self) -> dict[str, Any]:
        return {"mode": self.mode}

    def validate_input(self, df: pd.DataFrame) -> bool:
        return validate_volume_df(df, min_bars=2)

    def calculate(self, df: pd.DataFrame) -> dict[str, Any]:
        mode = self._parameters["mode"]
        price_up = float(df["close"].iloc[-1]) > float(df["close"].iloc[-2])
        price_down = float(df["close"].iloc[-1]) < float(df["close"].iloc[-2])
        volume_up = float(df["volume"].iloc[-1]) > float(df["volume"].iloc[-2])
        volume_down = float(df["volume"].iloc[-1]) < float(df["volume"].iloc[-2])
        passed = False
        if mode == "up_up":
            passed = price_up and volume_up
        elif mode == "down_up":
            passed = price_down and volume_up
        elif mode == "up_down":
            passed = price_up and volume_down
        else:
            passed = price_down and volume_down
        return {"passed": passed}

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


def run_confirmation_rule(rule_cls: type[BaseRule], df: pd.DataFrame) -> RuleResult:
    """Run volume confirmation rule class."""
    rule = rule_cls()
    rule.initialize()
    return rule.run(df)
