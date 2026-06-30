"""MT0006 — Daily 4H Uptrend Conflict. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0006Daily4HUptrendConflictRule(SpecRule):
    rule_id = "MT0006"
    rule_name = "Daily 4H Uptrend Conflict"


def evaluate_mt0006(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0006."""
    return run_spec_rule(MT0006Daily4HUptrendConflictRule, df)
