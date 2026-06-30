"""CBO005 — Breakout Continuation. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CBO005",
    rule_name="Breakout Continuation",
    atomic_prefix="BO",
    mode="bullish",
)


def evaluate_cbo005(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CBO005 from atomic rule results."""
    return _RULE.evaluate(atomic)
