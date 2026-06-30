"""GP0001 — Gap Up Open Above Prior High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0001GapUpOpenAbovePriorHighRule(SpecRule):
    rule_id = "GP0001"
    rule_name = "Gap Up Open Above Prior High"


def evaluate_gp0001(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0001."""
    return run_spec_rule(GP0001GapUpOpenAbovePriorHighRule, df)
