"""PT0018 — Rounding Bottom Active. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PT0018RoundingBottomActiveRule(SpecRule):
    rule_id = "PT0018"
    rule_name = "Rounding Bottom Active"


def evaluate_pt0018(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PT0018."""
    return run_spec_rule(PT0018RoundingBottomActiveRule, df)
