"""MT0007 — Daily 4H Downtrend Match. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0007Daily4HDowntrendMatchRule(SpecRule):
    rule_id = "MT0007"
    rule_name = "Daily 4H Downtrend Match"


def evaluate_mt0007(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0007."""
    return run_spec_rule(MT0007Daily4HDowntrendMatchRule, df)
