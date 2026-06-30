"""CF0045 — Trend And Momentum Agreement. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0045TrendAndMomentumAgreementRule(SpecRule):
    rule_id = "CF0045"
    rule_name = "Trend And Momentum Agreement"


def evaluate_cf0045(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0045."""
    return run_spec_rule(CF0045TrendAndMomentumAgreementRule, df)
