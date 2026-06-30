"""CF0020 — Volume Spike Confirms Bearish Trend. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0020VolumeSpikeConfirmsBearishTrendRule(SpecRule):
    rule_id = "CF0020"
    rule_name = "Volume Spike Confirms Bearish Trend"


def evaluate_cf0020(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0020."""
    return run_spec_rule(CF0020VolumeSpikeConfirmsBearishTrendRule, df)
