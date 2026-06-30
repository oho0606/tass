"""CDQ002 — Data Reliability. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CDQ002",
    rule_name="Data Reliability",
    atomic_prefix="DQ",
    mode="bullish",
)


def evaluate_cdq002(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CDQ002 from atomic rule results."""
    return _RULE.evaluate(atomic)
