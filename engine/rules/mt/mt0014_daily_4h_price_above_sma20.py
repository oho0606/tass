"""MT0014 — Daily 4H Price Above SMA20. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0014Daily4HPriceAboveSMA20Rule(SpecRule):
    rule_id = "MT0014"
    rule_name = "Daily 4H Price Above SMA20"


def evaluate_mt0014(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0014."""
    return run_spec_rule(MT0014Daily4HPriceAboveSMA20Rule, df)
