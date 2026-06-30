"""PT0048 — Double Bottom Neckline Present. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PT0048DoubleBottomNecklinePresentRule(SpecRule):
    rule_id = "PT0048"
    rule_name = "Double Bottom Neckline Present"


def evaluate_pt0048(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PT0048."""
    return run_spec_rule(PT0048DoubleBottomNecklinePresentRule, df)
