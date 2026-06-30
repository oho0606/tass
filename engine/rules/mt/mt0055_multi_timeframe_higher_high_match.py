"""MT0055 — Multi Timeframe Higher High Match. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0055MultiTimeframeHigherHighMatchRule(SpecRule):
    rule_id = "MT0055"
    rule_name = "Multi Timeframe Higher High Match"


def evaluate_mt0055(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0055."""
    return run_spec_rule(MT0055MultiTimeframeHigherHighMatchRule, df)
