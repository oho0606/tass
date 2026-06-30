"""MT0056 — Multi Timeframe Lower Low Match. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0056MultiTimeframeLowerLowMatchRule(SpecRule):
    rule_id = "MT0056"
    rule_name = "Multi Timeframe Lower Low Match"


def evaluate_mt0056(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0056."""
    return run_spec_rule(MT0056MultiTimeframeLowerLowMatchRule, df)
