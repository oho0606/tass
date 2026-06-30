"""EX0039 — Exit Close Below Double Bottom Level. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0039ExitCloseBelowDoubleBottomLevelRule(SpecRule):
    rule_id = "EX0039"
    rule_name = "Exit Close Below Double Bottom Level"


def evaluate_ex0039(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0039."""
    return run_spec_rule(EX0039ExitCloseBelowDoubleBottomLevelRule, df)
