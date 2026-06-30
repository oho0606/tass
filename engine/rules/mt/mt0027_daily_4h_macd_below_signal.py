"""MT0027 — Daily 4H MACD Below Signal. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0027Daily4HMACDBelowSignalRule(SpecRule):
    rule_id = "MT0027"
    rule_name = "Daily 4H MACD Below Signal"


def evaluate_mt0027(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0027."""
    return run_spec_rule(MT0027Daily4HMACDBelowSignalRule, df)
