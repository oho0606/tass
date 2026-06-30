"""PT0050 — Double Bottom First Trough Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PT0050DoubleBottomFirstTroughFormedRule(SpecRule):
    rule_id = "PT0050"
    rule_name = "Double Bottom First Trough Formed"


def evaluate_pt0050(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PT0050."""
    return run_spec_rule(PT0050DoubleBottomFirstTroughFormedRule, df)
