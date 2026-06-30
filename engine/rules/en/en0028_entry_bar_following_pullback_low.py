"""EN0028 — Entry Bar Following Pullback Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0028EntryBarFollowingPullbackLowRule(SpecRule):
    rule_id = "EN0028"
    rule_name = "Entry Bar Following Pullback Low"


def evaluate_en0028(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0028."""
    return run_spec_rule(EN0028EntryBarFollowingPullbackLowRule, df)
