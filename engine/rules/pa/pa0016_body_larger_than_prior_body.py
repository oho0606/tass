"""PA0016 — Body Larger Than Prior Body. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0016BodyLargerThanPriorBodyRule(SpecRule):
    rule_id = "PA0016"
    rule_name = "Body Larger Than Prior Body"


def evaluate_pa0016(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0016."""
    return run_spec_rule(PA0016BodyLargerThanPriorBodyRule, df)
