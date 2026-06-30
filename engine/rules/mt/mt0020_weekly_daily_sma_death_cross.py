"""MT0020 — Weekly Daily SMA Death Cross. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0020WeeklyDailySMADeathCrossRule(SpecRule):
    rule_id = "MT0020"
    rule_name = "Weekly Daily SMA Death Cross"


def evaluate_mt0020(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0020."""
    return run_spec_rule(MT0020WeeklyDailySMADeathCrossRule, df)
