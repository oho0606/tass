"""MT0050 — Primary Downtrend Secondary Uptrend. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0050PrimaryDowntrendSecondaryUptrendRule(SpecRule):
    rule_id = "MT0050"
    rule_name = "Primary Downtrend Secondary Uptrend"


def evaluate_mt0050(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0050."""
    return run_spec_rule(MT0050PrimaryDowntrendSecondaryUptrendRule, df)
