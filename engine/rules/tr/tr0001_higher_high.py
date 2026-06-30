"""
TR0001 — Higher High Quality
TASS-012: One Rule · One Class · One File
"""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd

from engine.core.pivots import find_pivot_highs
from engine.core.rule_base import BaseRule
from engine.core.types import RuleResult, RuleVerdict

# Shared scoring helpers (no circular import with atomic.py)
from engine.rules.tr._scoring import bullish_quality_score, confidence_risk


class TR0001HigherHighRule(BaseRule):
    rule_id = "TR0001"
    rule_name = "Higher High"
    version = "1.0.0"

    def default_parameters(self) -> dict[str, Any]:
        return {"lookback": 40, "pivot_strength": 3, "min_hh_count": 2}

    def validate_input(self, df: pd.DataFrame) -> bool:
        if df is None or df.empty:
            return False
        required = {"high", "low", "close", "volume"}
        if not required.issubset(df.columns):
            return False
        lookback = int(self._parameters["lookback"])
        if len(df) < lookback:
            return False
        if df[["high", "low", "close"]].tail(lookback).isna().any().any():
            return False
        return True

    def calculate(self, df: pd.DataFrame) -> dict[str, Any]:
        lookback = int(self._parameters["lookback"])
        min_hh = int(self._parameters["min_hh_count"])
        window = df.tail(lookback)
        pivots = find_pivot_highs(window["high"])
        if len(pivots) < 2:
            return {
                "pivot_count": len(pivots),
                "hh_count": 0,
                "avg_rise_pct": 0.0,
                "volume_ok": False,
            }

        prices = [float(window["high"].iloc[i]) for i in pivots]
        hh_count = sum(1 for i in range(1, len(prices)) if prices[i] > prices[i - 1])
        rises = [
            ((prices[i] - prices[i - 1]) / prices[i - 1]) * 100
            for i in range(1, len(prices))
            if prices[i - 1] != 0 and prices[i] > prices[i - 1]
        ]
        avg_rise = float(np.mean(rises)) if rises else 0.0
        vol = window["volume"]
        volume_ok = (
            bool(vol.iloc[-5:].mean() > vol.iloc[-20:].mean() * 0.9) if len(vol) >= 20 else False
        )

        return {
            "pivot_count": len(pivots),
            "hh_count": hh_count,
            "avg_rise_pct": avg_rise,
            "volume_ok": volume_ok,
            "min_hh_count": min_hh,
            "current_swing_high": prices[-1] if prices else None,
            "previous_swing_high": prices[-2] if len(prices) > 1 else None,
        }

    def evaluate(self, df: pd.DataFrame) -> RuleVerdict:
        c = self._calculation
        if c.get("pivot_count", 0) < 2:
            return "FAIL"
        score, verdict, grade = bullish_quality_score(
            c["hh_count"], c["min_hh_count"], c["avg_rise_pct"], c["volume_ok"]
        )
        self._calculation["score"] = score
        self._calculation["quality_grade"] = grade
        return verdict

    def _build_result(self, verdict: RuleVerdict) -> RuleResult:
        c = self._calculation
        score = float(c.get("score", 0.0))
        grade = c.get("quality_grade", "Fail")
        conf, risk = confidence_risk(grade)
        reasons: list[str] = []
        if verdict == "PASS":
            reasons.append(f"Higher High 품질 {grade}")
            if c.get("volume_ok"):
                reasons.append("거래량 지지")
        elif verdict == "UNKNOWN":
            reasons.append("전제조건 미충족")
        else:
            reasons.append("Higher High 미충족")

        return RuleResult(
            rule_id=self.rule_id,
            verdict=verdict,
            score=score,
            confidence_delta=conf,
            risk_delta=risk,
            reasons=reasons,
            metadata=dict(c),
        )


def evaluate_higher_high(df: pd.DataFrame) -> RuleResult:
    """Functional entry point (backward compatible)."""
    rule = TR0001HigherHighRule()
    rule.initialize()
    return rule.run(df)
