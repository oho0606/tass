"""PT0044 — Double Bottom Active. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PT0044DoubleBottomActiveRule(SpecRule):
    rule_id = "PT0044"
    rule_name = "Double Bottom Active"


def evaluate_pt0044(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PT0044."""
    return run_spec_rule(PT0044DoubleBottomActiveRule, df)
