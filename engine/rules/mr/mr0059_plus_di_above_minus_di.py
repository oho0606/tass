"""MR0059 — Plus DI Above Minus DI. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0059PlusDIAboveMinusDIRule(SpecRule):
    rule_id = "MR0059"
    rule_name = "Plus DI Above Minus DI"


def evaluate_mr0059(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0059."""
    return run_spec_rule(MR0059PlusDIAboveMinusDIRule, df)
