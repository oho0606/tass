"""CF0048 — MACD And RSI Agreement. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0048MACDAndRSIAgreementRule(SpecRule):
    rule_id = "CF0048"
    rule_name = "MACD And RSI Agreement"


def evaluate_cf0048(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0048."""
    return run_spec_rule(CF0048MACDAndRSIAgreementRule, df)
