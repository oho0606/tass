"""PT0020 — V Bottom Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PT0020VBottomFormedRule(SpecRule):
    rule_id = "PT0020"
    rule_name = "V Bottom Formed"


def evaluate_pt0020(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PT0020."""
    return run_spec_rule(PT0020VBottomFormedRule, df)
