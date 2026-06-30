"""PT0036 — Ascending Channel Active. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PT0036AscendingChannelActiveRule(SpecRule):
    rule_id = "PT0036"
    rule_name = "Ascending Channel Active"


def evaluate_pt0036(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PT0036."""
    return run_spec_rule(PT0036AscendingChannelActiveRule, df)
