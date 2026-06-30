"""VO0044 — ATR Contracting. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0044ATRContractingRule(SpecRule):
    rule_id = "VO0044"
    rule_name = "ATR Contracting"


def evaluate_vo0044(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0044."""
    return run_spec_rule(VO0044ATRContractingRule, df)
