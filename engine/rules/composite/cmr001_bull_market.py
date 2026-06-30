"""CMR001 — Bull Market. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CMR001",
    rule_name="Bull Market",
    atomic_prefix="MR",
    mode="bullish",
)


def evaluate_cmr001(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CMR001 from atomic rule results."""
    return _RULE.evaluate(atomic)
