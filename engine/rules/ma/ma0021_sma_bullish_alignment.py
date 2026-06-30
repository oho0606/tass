"""MA0021 — SMA Bullish Alignment. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

from typing import Any

import pandas as pd

from engine.core.rule_base import BaseRule
from engine.core.types import RuleResult, RuleVerdict
from engine.rules.ma._scoring import confidence_risk_for_pass, score_from_verdict

_ALIGNMENT_PERIODS = (5, 20, 60, 120, 240)


class MA0021SMABullishAlignmentRule(BaseRule):
    """PASS when SMA periods are in bullish order (short > long)."""

    rule_id = "MA0021"
    rule_name = "SMA Bullish Alignment"
    version = "1.0.0"

    def default_parameters(self) -> dict[str, Any]:
        return {"periods": _ALIGNMENT_PERIODS}

    def validate_input(self, df: pd.DataFrame) -> bool:
        if df is None or df.empty:
            return False
        periods = self._parameters["periods"]
        for period in periods:
            column = f"ma_{period}"
            if column not in df.columns or pd.isna(df[column].iloc[-1]):
                return False
        return len(df) >= max(periods)

    def calculate(self, df: pd.DataFrame) -> dict[str, Any]:
        periods = self._parameters["periods"]
        values = {period: float(df[f"ma_{period}"].iloc[-1]) for period in periods}
        ordered = [values[periods[i]] > values[periods[i + 1]] for i in range(len(periods) - 1)]
        aligned_count = sum(1 for ok in ordered if ok)
        full_alignment = all(ordered)
        partial_alignment = aligned_count >= len(periods) - 2
        return {
            "values": values,
            "aligned_pairs": aligned_count,
            "full_alignment": full_alignment,
            "partial_alignment": partial_alignment,
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
        reasons = []
        if verdict == "PASS":
            reasons.append("SMA 정배열 (단기 > 장기)")
        elif verdict == "PARTIAL":
            reasons.append("SMA 부분 정배열")
        else:
            reasons.append("SMA 정배열 미충족")
        return RuleResult(
            rule_id=self.rule_id,
            verdict=verdict,
            score=score,
            confidence_delta=conf,
            risk_delta=risk,
            reasons=reasons,
            metadata=dict(self._calculation),
        )


def evaluate_ma0021(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0021."""
    rule = MA0021SMABullishAlignmentRule()
    rule.initialize()
    return rule.run(df)
