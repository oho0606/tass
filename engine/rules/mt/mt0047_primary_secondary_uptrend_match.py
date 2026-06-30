"""MT0047 — Primary Secondary Uptrend Match. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0047PrimarySecondaryUptrendMatchRule(SpecRule):
    rule_id = "MT0047"
    rule_name = "Primary Secondary Uptrend Match"


def evaluate_mt0047(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0047."""
    return run_spec_rule(MT0047PrimarySecondaryUptrendMatchRule, df)
