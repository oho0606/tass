"""Shared helpers for MA crossover rules (MA0031–MA0040)."""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from engine.core.rule_base import BaseRule
from engine.core.types import RuleResult, RuleVerdict
from engine.rules.ma._helpers import MaType
from engine.rules.ma._scoring import confidence_risk_for_pass, score_from_verdict

CrossDirection = Literal["golden", "death"]


def _ma_column(ma_type: MaType, period: int) -> str:
    prefix = "ma" if ma_type == "sma" else "ema"
    return f"{prefix}_{period}"


def _detect_cross(
    fast_prev: float,
    fast_curr: float,
    slow_prev: float,
    slow_curr: float,
    direction: CrossDirection,
) -> bool:
    """Detect crossover on latest bar."""
    if direction == "golden":
        return fast_prev <= slow_prev and fast_curr > slow_curr
    return fast_prev >= slow_prev and fast_curr < slow_curr


class CrossoverRule(BaseRule):
    """PASS when fast MA crosses slow MA (golden or death)."""

    rule_id: str
    rule_name: str
    ma_type: MaType
    fast_period: int
    slow_period: int
    direction: CrossDirection

    def default_parameters(self) -> dict[str, Any]:
        return {
            "ma_type": self.ma_type,
            "fast_period": self.fast_period,
            "slow_period": self.slow_period,
            "direction": self.direction,
        }

    def validate_input(self, df: pd.DataFrame) -> bool:
        if df is None or len(df) < max(self.fast_period, self.slow_period) + 1:
            return False
        for period in (self.fast_period, self.slow_period):
            column = _ma_column(self.ma_type, period)
            if column not in df.columns:
                return False
            if pd.isna(df[column].iloc[-2:]).any():
                return False
        return True

    def calculate(self, df: pd.DataFrame) -> dict[str, Any]:
        fast_col = _ma_column(self.ma_type, self.fast_period)
        slow_col = _ma_column(self.ma_type, self.slow_period)
        fast_prev = float(df[fast_col].iloc[-2])
        fast_curr = float(df[fast_col].iloc[-1])
        slow_prev = float(df[slow_col].iloc[-2])
        slow_curr = float(df[slow_col].iloc[-1])
        crossed = _detect_cross(fast_prev, fast_curr, slow_prev, slow_curr, self.direction)
        return {
            "fast_prev": fast_prev,
            "fast_curr": fast_curr,
            "slow_prev": slow_prev,
            "slow_curr": slow_curr,
            "crossed": crossed,
        }

    def evaluate(self, df: pd.DataFrame) -> RuleVerdict:
        _ = df
        return "PASS" if self._calculation.get("crossed") else "FAIL"

    def _build_result(self, verdict: RuleVerdict) -> RuleResult:
        score = score_from_verdict(verdict)
        passed = verdict == "PASS"
        conf, risk = confidence_risk_for_pass(passed)
        cross_label = "골든크로스" if self.direction == "golden" else "데드크로스"
        return RuleResult(
            rule_id=self.rule_id,
            verdict=verdict,
            score=score,
            confidence_delta=conf,
            risk_delta=risk,
            reasons=[
                f"{self.ma_type.upper()} {cross_label} ({self.fast_period}/{self.slow_period})"
            ],
            metadata=dict(self._calculation),
        )


class MultipleCrossoverRule(BaseRule):
    """PASS when multiple MA pairs show same crossover direction."""

    rule_id: str
    rule_name: str
    ma_type: MaType
    pairs: tuple[tuple[int, int], ...]
    direction: CrossDirection
    min_crosses: int = 2

    def default_parameters(self) -> dict[str, Any]:
        return {
            "pairs": self.pairs,
            "direction": self.direction,
            "min_crosses": self.min_crosses,
            "ma_type": self.ma_type,
        }

    def validate_input(self, df: pd.DataFrame) -> bool:
        if df is None or len(df) < 3:
            return False
        for fast, slow in self.pairs:
            for period in (fast, slow):
                column = _ma_column(self.ma_type, period)
                if column not in df.columns or pd.isna(df[column].iloc[-2:]).any():
                    return False
        return True

    def calculate(self, df: pd.DataFrame) -> dict[str, Any]:
        crosses: list[str] = []
        for fast, slow in self.pairs:
            fast_col = _ma_column(self.ma_type, fast)
            slow_col = _ma_column(self.ma_type, slow)
            if _detect_cross(
                float(df[fast_col].iloc[-2]),
                float(df[fast_col].iloc[-1]),
                float(df[slow_col].iloc[-2]),
                float(df[slow_col].iloc[-1]),
                self.direction,
            ):
                crosses.append(f"{fast}/{slow}")
        return {"crosses": crosses, "cross_count": len(crosses)}

    def evaluate(self, df: pd.DataFrame) -> RuleVerdict:
        _ = df
        return "PASS" if self._calculation.get("cross_count", 0) >= self.min_crosses else "FAIL"

    def _build_result(self, verdict: RuleVerdict) -> RuleResult:
        score = score_from_verdict(verdict)
        passed = verdict == "PASS"
        conf, risk = confidence_risk_for_pass(passed)
        label = "복수 골든크로스" if self.direction == "golden" else "복수 데드크로스"
        return RuleResult(
            rule_id=self.rule_id,
            verdict=verdict,
            score=score,
            confidence_delta=conf,
            risk_delta=risk,
            reasons=[label],
            metadata=dict(self._calculation),
        )


def run_crossover_rule(rule_cls: type[BaseRule], df: pd.DataFrame) -> RuleResult:
    """Run crossover rule class."""
    rule = rule_cls()
    rule.initialize()
    return rule.run(df)
