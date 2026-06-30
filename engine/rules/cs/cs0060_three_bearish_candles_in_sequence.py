"""CS0060 — Three Bearish Candles In Sequence. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0060ThreeBearishCandlesInSequenceRule(SpecRule):
    rule_id = "CS0060"
    rule_name = "Three Bearish Candles In Sequence"


def evaluate_cs0060(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0060."""
    return run_spec_rule(CS0060ThreeBearishCandlesInSequenceRule, df)
