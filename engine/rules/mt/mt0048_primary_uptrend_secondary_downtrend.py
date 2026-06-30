"""MT0048 — Primary Uptrend Secondary Downtrend. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0048PrimaryUptrendSecondaryDowntrendRule(SpecRule):
    rule_id = "MT0048"
    rule_name = "Primary Uptrend Secondary Downtrend"


def evaluate_mt0048(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0048."""
    return run_spec_rule(MT0048PrimaryUptrendSecondaryDowntrendRule, df)
