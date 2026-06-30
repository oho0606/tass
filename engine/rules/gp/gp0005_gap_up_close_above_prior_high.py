"""GP0005 — Gap Up Close Above Prior High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0005GapUpCloseAbovePriorHighRule(SpecRule):
    rule_id = "GP0005"
    rule_name = "Gap Up Close Above Prior High"


def evaluate_gp0005(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0005."""
    return run_spec_rule(GP0005GapUpCloseAbovePriorHighRule, df)
