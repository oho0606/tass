"""RK0003 — ATR Rising. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0003ATRRisingRule(SpecRule):
    rule_id = "RK0003"
    rule_name = "ATR Rising"


def evaluate_rk0003(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0003."""
    return run_spec_rule(RK0003ATRRisingRule, df)
