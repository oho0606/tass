"""CVO010 — Volatility Confirmation. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CVO010",
    rule_name="Volatility Confirmation",
    atomic_prefix="VO",
    mode="quality",
)


def evaluate_cvo010(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CVO010 from atomic rule results."""
    return _RULE.evaluate(atomic)
