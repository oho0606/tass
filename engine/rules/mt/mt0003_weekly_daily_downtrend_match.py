"""MT0003 — Weekly Daily Downtrend Match. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0003WeeklyDailyDowntrendMatchRule(SpecRule):
    rule_id = "MT0003"
    rule_name = "Weekly Daily Downtrend Match"


def evaluate_mt0003(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0003."""
    return run_spec_rule(MT0003WeeklyDailyDowntrendMatchRule, df)
