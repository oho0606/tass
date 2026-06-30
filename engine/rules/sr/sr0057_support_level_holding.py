"""SR0057 — Support Level Holding. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0057SupportLevelHoldingRule(SpecRule):
    rule_id = "SR0057"
    rule_name = "Support Level Holding"


def evaluate_sr0057(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0057."""
    return run_spec_rule(SR0057SupportLevelHoldingRule, df)
