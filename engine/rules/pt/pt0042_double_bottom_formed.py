"""PT0042 — Double Bottom Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PT0042DoubleBottomFormedRule(SpecRule):
    rule_id = "PT0042"
    rule_name = "Double Bottom Formed"


def evaluate_pt0042(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PT0042."""
    return run_spec_rule(PT0042DoubleBottomFormedRule, df)
