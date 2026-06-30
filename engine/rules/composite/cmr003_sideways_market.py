"""CMR003 — Sideways Market. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CMR003",
    rule_name="Sideways Market",
    atomic_prefix="MR",
    mode="neutral",
)


def evaluate_cmr003(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CMR003 from atomic rule results."""
    return _RULE.evaluate(atomic)
