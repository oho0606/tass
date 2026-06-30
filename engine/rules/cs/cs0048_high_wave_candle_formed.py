"""CS0048 — High Wave Candle Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0048HighWaveCandleFormedRule(SpecRule):
    rule_id = "CS0048"
    rule_name = "High Wave Candle Formed"


def evaluate_cs0048(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0048."""
    return run_spec_rule(CS0048HighWaveCandleFormedRule, df)
