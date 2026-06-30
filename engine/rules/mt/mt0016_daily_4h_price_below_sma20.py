"""MT0016 — Daily 4H Price Below SMA20. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0016Daily4HPriceBelowSMA20Rule(SpecRule):
    rule_id = "MT0016"
    rule_name = "Daily 4H Price Below SMA20"


def evaluate_mt0016(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0016."""
    return run_spec_rule(MT0016Daily4HPriceBelowSMA20Rule, df)
