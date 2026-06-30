"""CPB001 — Healthy Pullback. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CPB001",
    rule_name="Healthy Pullback",
    atomic_prefix="PB",
    mode="bullish",
)


def evaluate_cpb001(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CPB001 from atomic rule results."""
    return _RULE.evaluate(atomic)
