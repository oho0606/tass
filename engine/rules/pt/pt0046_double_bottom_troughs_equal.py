"""PT0046 — Double Bottom Troughs Equal. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PT0046DoubleBottomTroughsEqualRule(SpecRule):
    rule_id = "PT0046"
    rule_name = "Double Bottom Troughs Equal"


def evaluate_pt0046(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PT0046."""
    return run_spec_rule(PT0046DoubleBottomTroughsEqualRule, df)
