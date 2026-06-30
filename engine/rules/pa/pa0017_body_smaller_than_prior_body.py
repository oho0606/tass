"""PA0017 — Body Smaller Than Prior Body. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0017BodySmallerThanPriorBodyRule(SpecRule):
    rule_id = "PA0017"
    rule_name = "Body Smaller Than Prior Body"


def evaluate_pa0017(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0017."""
    return run_spec_rule(PA0017BodySmallerThanPriorBodyRule, df)
