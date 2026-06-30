"""CVO002 — Volatility Expansion. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CVO002",
    rule_name="Volatility Expansion",
    atomic_prefix="VO",
    mode="bullish",
)


def evaluate_cvo002(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CVO002 from atomic rule results."""
    return _RULE.evaluate(atomic)
