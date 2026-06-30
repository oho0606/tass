"""MS0055 — Structure Leg Extended. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0055StructureLegExtendedRule(SpecRule):
    rule_id = "MS0055"
    rule_name = "Structure Leg Extended"


def evaluate_ms0055(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0055."""
    return run_spec_rule(MS0055StructureLegExtendedRule, df)
