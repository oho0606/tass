"""SR0052 — Support Level Second Touch. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0052SupportLevelSecondTouchRule(SpecRule):
    rule_id = "SR0052"
    rule_name = "Support Level Second Touch"


def evaluate_sr0052(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0052."""
    return run_spec_rule(SR0052SupportLevelSecondTouchRule, df)
