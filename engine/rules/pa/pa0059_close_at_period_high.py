"""PA0059 — Close At Period High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0059CloseAtPeriodHighRule(SpecRule):
    rule_id = "PA0059"
    rule_name = "Close At Period High"


def evaluate_pa0059(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0059."""
    return run_spec_rule(PA0059CloseAtPeriodHighRule, df)
