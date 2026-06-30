"""PT0016 — Rounding Bottom Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PT0016RoundingBottomFormedRule(SpecRule):
    rule_id = "PT0016"
    rule_name = "Rounding Bottom Formed"


def evaluate_pt0016(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PT0016."""
    return run_spec_rule(PT0016RoundingBottomFormedRule, df)
