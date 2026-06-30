"""MT0049 — Primary Secondary Downtrend Match. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0049PrimarySecondaryDowntrendMatchRule(SpecRule):
    rule_id = "MT0049"
    rule_name = "Primary Secondary Downtrend Match"


def evaluate_mt0049(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0049."""
    return run_spec_rule(MT0049PrimarySecondaryDowntrendMatchRule, df)
