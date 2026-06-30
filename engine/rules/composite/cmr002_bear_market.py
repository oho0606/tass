"""CMR002 — Bear Market. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CMR002",
    rule_name="Bear Market",
    atomic_prefix="MR",
    mode="bullish",
)


def evaluate_cmr002(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CMR002 from atomic rule results."""
    return _RULE.evaluate(atomic)
