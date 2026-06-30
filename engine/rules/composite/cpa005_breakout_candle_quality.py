"""CPA005 — Breakout Candle Quality. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CPA005",
    rule_name="Breakout Candle Quality",
    atomic_prefix="PA",
    mode="quality",
)


def evaluate_cpa005(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CPA005 from atomic rule results."""
    return _RULE.evaluate(atomic)
