"""CBO004 — Strong Breakout. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CBO004",
    rule_name="Strong Breakout",
    atomic_prefix="BO",
    mode="bullish",
)


def evaluate_cbo004(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CBO004 from atomic rule results."""
    return _RULE.evaluate(atomic)
