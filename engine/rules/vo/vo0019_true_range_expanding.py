"""VO0019 — True Range Expanding. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0019TrueRangeExpandingRule(SpecRule):
    rule_id = "VO0019"
    rule_name = "True Range Expanding"


def evaluate_vo0019(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0019."""
    return run_spec_rule(VO0019TrueRangeExpandingRule, df)
