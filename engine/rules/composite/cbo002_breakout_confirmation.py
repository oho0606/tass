"""CBO002 — Breakout Confirmation. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CBO002",
    rule_name="Breakout Confirmation",
    atomic_prefix="BO",
    mode="quality",
)


def evaluate_cbo002(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CBO002 from atomic rule results."""
    return _RULE.evaluate(atomic)
