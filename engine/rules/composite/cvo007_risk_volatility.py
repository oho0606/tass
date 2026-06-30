"""CVO007 — Risk Volatility. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CVO007",
    rule_name="Risk Volatility",
    atomic_prefix="VO",
    mode="bearish",
)


def evaluate_cvo007(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CVO007 from atomic rule results."""
    return _RULE.evaluate(atomic)
