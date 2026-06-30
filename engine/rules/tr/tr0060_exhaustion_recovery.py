"""TR0060 — Exhaustion Recovery. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0060ExhaustionRecoveryRule(TrendSpecRule):
    rule_id = "TR0060"
    rule_name = "Exhaustion Recovery"


def evaluate_tr0060(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0060."""
    return run_trend_spec_rule(TR0060ExhaustionRecoveryRule, df)
