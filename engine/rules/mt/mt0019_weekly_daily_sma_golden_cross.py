"""MT0019 — Weekly Daily SMA Golden Cross. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0019WeeklyDailySMAGoldenCrossRule(SpecRule):
    rule_id = "MT0019"
    rule_name = "Weekly Daily SMA Golden Cross"


def evaluate_mt0019(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0019."""
    return run_spec_rule(MT0019WeeklyDailySMAGoldenCrossRule, df)
