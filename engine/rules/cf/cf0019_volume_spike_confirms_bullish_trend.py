"""CF0019 — Volume Spike Confirms Bullish Trend. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0019VolumeSpikeConfirmsBullishTrendRule(SpecRule):
    rule_id = "CF0019"
    rule_name = "Volume Spike Confirms Bullish Trend"


def evaluate_cf0019(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0019."""
    return run_spec_rule(CF0019VolumeSpikeConfirmsBullishTrendRule, df)
