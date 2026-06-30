"""CVO006 — Breakout Volatility. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CVO006",
    rule_name="Breakout Volatility",
    atomic_prefix="VO",
    mode="bullish",
)


def evaluate_cvo006(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CVO006 from atomic rule results."""
    return _RULE.evaluate(atomic)
