"""CMS005 — Lower Low Sequence. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CMS005",
    rule_name="Lower Low Sequence",
    atomic_prefix="MS",
    mode="bullish",
)


def evaluate_cms005(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CMS005 from atomic rule results."""
    return _RULE.evaluate(atomic)
