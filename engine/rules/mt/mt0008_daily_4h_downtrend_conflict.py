"""MT0008 — Daily 4H Downtrend Conflict. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0008Daily4HDowntrendConflictRule(SpecRule):
    rule_id = "MT0008"
    rule_name = "Daily 4H Downtrend Conflict"


def evaluate_mt0008(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0008."""
    return run_spec_rule(MT0008Daily4HDowntrendConflictRule, df)
