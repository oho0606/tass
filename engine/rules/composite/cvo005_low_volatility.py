"""CVO005 — Low Volatility. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CVO005",
    rule_name="Low Volatility",
    atomic_prefix="VO",
    mode="bullish",
)


def evaluate_cvo005(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CVO005 from atomic rule results."""
    return _RULE.evaluate(atomic)
