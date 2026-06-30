"""SR0017 — Prior High As Horizontal Resistance. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0017PriorHighAsHorizontalResistanceRule(SpecRule):
    rule_id = "SR0017"
    rule_name = "Prior High As Horizontal Resistance"


def evaluate_sr0017(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0017."""
    return run_spec_rule(SR0017PriorHighAsHorizontalResistanceRule, df)
