"""VO0046 — Bollinger Band Width Contracting. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0046BollingerBandWidthContractingRule(SpecRule):
    rule_id = "VO0046"
    rule_name = "Bollinger Band Width Contracting"


def evaluate_vo0046(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0046."""
    return run_spec_rule(VO0046BollingerBandWidthContractingRule, df)
