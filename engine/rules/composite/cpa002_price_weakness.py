"""CPA002 — Price Weakness. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CPA002",
    rule_name="Price Weakness",
    atomic_prefix="PA",
    mode="bearish",
)


def evaluate_cpa002(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CPA002 from atomic rule results."""
    return _RULE.evaluate(atomic)
