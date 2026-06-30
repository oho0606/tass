"""CCS002 — Bearish Candle Group. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CCS002",
    rule_name="Bearish Candle Group",
    atomic_prefix="CS",
    mode="bearish",
)


def evaluate_ccs002(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CCS002 from atomic rule results."""
    return _RULE.evaluate(atomic)
