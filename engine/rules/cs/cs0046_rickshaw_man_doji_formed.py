"""CS0046 — Rickshaw Man Doji Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0046RickshawManDojiFormedRule(SpecRule):
    rule_id = "CS0046"
    rule_name = "Rickshaw Man Doji Formed"


def evaluate_cs0046(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0046."""
    return run_spec_rule(CS0046RickshawManDojiFormedRule, df)
