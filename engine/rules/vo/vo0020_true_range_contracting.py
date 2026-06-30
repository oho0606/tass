"""VO0020 — True Range Contracting. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0020TrueRangeContractingRule(SpecRule):
    rule_id = "VO0020"
    rule_name = "True Range Contracting"


def evaluate_vo0020(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0020."""
    return run_spec_rule(VO0020TrueRangeContractingRule, df)
