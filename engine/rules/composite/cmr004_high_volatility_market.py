"""CMR004 — High Volatility Market. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CMR004",
    rule_name="High Volatility Market",
    atomic_prefix="MR",
    mode="bullish",
)


def evaluate_cmr004(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CMR004 from atomic rule results."""
    return _RULE.evaluate(atomic)
