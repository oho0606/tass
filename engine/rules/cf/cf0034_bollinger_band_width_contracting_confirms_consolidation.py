"""CF0034 — Bollinger Band Width Contracting Confirms Consolidation. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0034BollingerBandWidthContractingConfirmsConsolidationRule(SpecRule):
    rule_id = "CF0034"
    rule_name = "Bollinger Band Width Contracting Confirms Consolidation"


def evaluate_cf0034(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0034."""
    return run_spec_rule(CF0034BollingerBandWidthContractingConfirmsConsolidationRule, df)
