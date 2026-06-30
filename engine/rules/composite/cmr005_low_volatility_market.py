"""CMR005 — Low Volatility Market. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CMR005",
    rule_name="Low Volatility Market",
    atomic_prefix="MR",
    mode="bullish",
)


def evaluate_cmr005(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CMR005 from atomic rule results."""
    return _RULE.evaluate(atomic)
