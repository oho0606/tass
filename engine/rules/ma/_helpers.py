"""Shared helpers for MA price-position atomic rules (MA0001–MA0020)."""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from engine.core.rule_base import BaseRule
from engine.core.types import RuleResult, RuleVerdict
from engine.rules.ma._scoring import confidence_risk_for_pass, score_from_verdict

MaType = Literal["sma", "ema"]
Direction = Literal["above", "below"]


class PricePositionRule(BaseRule):
    """Base class for price above/below moving average rules."""

    rule_id: str
    rule_name: str
    ma_type: MaType
    period: int
    direction: Direction
    version: str = "1.0.0"

    def default_parameters(self) -> dict[str, Any]:
        """Return rule parameters including MA type and period."""
        return {
            "ma_type": self.ma_type,
            "period": self.period,
            "direction": self.direction,
        }

    def _ma_column(self) -> str:
        """Resolve indicator column name for this rule."""
        prefix = "ma" if self.ma_type == "sma" else "ema"
        return f"{prefix}_{self.period}"

    def validate_input(self, df: pd.DataFrame) -> bool:
        """Validate OHLCV and MA indicator availability."""
        if df is None or df.empty:
            return False
        if "close" not in df.columns:
            return False
        column = self._ma_column()
        if column not in df.columns:
            return False
        if len(df) < self.period:
            return False
        if pd.isna(df[column].iloc[-1]) or pd.isna(df["close"].iloc[-1]):
            return False
        return True

    def calculate(self, df: pd.DataFrame) -> dict[str, Any]:
        """Compute latest close, MA value, and distance."""
        column = self._ma_column()
        close = float(df["close"].iloc[-1])
        ma_value = float(df[column].iloc[-1])
        distance_pct = ((close - ma_value) / ma_value * 100.0) if ma_value else 0.0
        passed = close > ma_value if self.direction == "above" else close < ma_value
        return {
            "close": close,
            "ma_value": ma_value,
            "ma_column": column,
            "distance_pct": round(distance_pct, 4),
            "direction": self.direction,
            "passed": passed,
        }

    def evaluate(self, df: pd.DataFrame) -> RuleVerdict:
        """Return PASS when price satisfies position vs MA."""
        _ = df
        return "PASS" if self._calculation.get("passed") else "FAIL"

    def _build_result(self, verdict: RuleVerdict) -> RuleResult:
        """Build ``RuleResult`` with score and explainability metadata."""
        passed = bool(self._calculation.get("passed"))
        score = score_from_verdict(verdict)
        conf, risk = confidence_risk_for_pass(passed)
        ma_label = self.ma_type.upper()
        direction_label = "상회" if self.direction == "above" else "하회"
        reasons: list[str] = []
        if verdict == "PASS":
            reasons.append(f"종가가 {ma_label}{self.period} {direction_label}")
        elif verdict == "UNKNOWN":
            reasons.append("전제조건 미충족")
        else:
            reasons.append(f"종가가 {ma_label}{self.period} {direction_label} 아님")

        return RuleResult(
            rule_id=self.rule_id,
            verdict=verdict,
            score=score,
            confidence_delta=conf,
            risk_delta=risk,
            reasons=reasons,
            metadata=dict(self._calculation),
        )


def run_price_position_rule(rule_cls: type[PricePositionRule], df: pd.DataFrame) -> RuleResult:
    """Functional entry point for a price-position rule class."""
    rule = rule_cls()
    rule.initialize()
    return rule.run(df)
