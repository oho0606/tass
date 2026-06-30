"""MT0058 — Multi Timeframe Volume Contraction Match. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0058MultiTimeframeVolumeContractionMatchRule(SpecRule):
    rule_id = "MT0058"
    rule_name = "Multi Timeframe Volume Contraction Match"


def evaluate_mt0058(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0058."""
    return run_spec_rule(MT0058MultiTimeframeVolumeContractionMatchRule, df)
