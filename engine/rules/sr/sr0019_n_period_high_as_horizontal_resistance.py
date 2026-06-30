"""SR0019 — N-Period High As Horizontal Resistance. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0019NPeriodHighAsHorizontalResistanceRule(SpecRule):
    rule_id = "SR0019"
    rule_name = "N-Period High As Horizontal Resistance"


def evaluate_sr0019(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0019."""
    return run_spec_rule(SR0019NPeriodHighAsHorizontalResistanceRule, df)
