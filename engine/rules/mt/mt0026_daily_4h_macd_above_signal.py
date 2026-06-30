"""MT0026 — Daily 4H MACD Above Signal. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0026Daily4HMACDAboveSignalRule(SpecRule):
    rule_id = "MT0026"
    rule_name = "Daily 4H MACD Above Signal"


def evaluate_mt0026(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0026."""
    return run_spec_rule(MT0026Daily4HMACDAboveSignalRule, df)
