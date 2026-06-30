"""CVO009 — Volatility Quality. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CVO009",
    rule_name="Volatility Quality",
    atomic_prefix="VO",
    mode="quality",
)


def evaluate_cvo009(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CVO009 from atomic rule results."""
    return _RULE.evaluate(atomic)
