"""SR0053 — Support Level Multiple Touches. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0053SupportLevelMultipleTouchesRule(SpecRule):
    rule_id = "SR0053"
    rule_name = "Support Level Multiple Touches"


def evaluate_sr0053(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0053."""
    return run_spec_rule(SR0053SupportLevelMultipleTouchesRule, df)
