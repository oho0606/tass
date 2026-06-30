"""MT0015 — Daily Above SMA20 4H Below SMA20. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0015DailyAboveSMA204HBelowSMA20Rule(SpecRule):
    rule_id = "MT0015"
    rule_name = "Daily Above SMA20 4H Below SMA20"


def evaluate_mt0015(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0015."""
    return run_spec_rule(MT0015DailyAboveSMA204HBelowSMA20Rule, df)
