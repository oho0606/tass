"""SR0003 — Price At Horizontal Support. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0003PriceAtHorizontalSupportRule(SpecRule):
    rule_id = "SR0003"
    rule_name = "Price At Horizontal Support"


def evaluate_sr0003(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0003."""
    return run_spec_rule(SR0003PriceAtHorizontalSupportRule, df)
