"""GP0003 — Gap Up Low Above Prior High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0003GapUpLowAbovePriorHighRule(SpecRule):
    rule_id = "GP0003"
    rule_name = "Gap Up Low Above Prior High"


def evaluate_gp0003(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0003."""
    return run_spec_rule(GP0003GapUpLowAbovePriorHighRule, df)
