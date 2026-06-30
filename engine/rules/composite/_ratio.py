"""Ratio-based composite rules aggregating atomic verdicts by category."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from engine.core.composite_base import BaseCompositeRule
from engine.core.types import RuleResult, RuleVerdict
from engine.rules.composite._helpers import composite_result, verdict_from_ratio

MIN_ATOMIC_COVERAGE = 3


@dataclass(frozen=True)
class CategoryRatioCompositeRule(BaseCompositeRule):
    """Aggregate atomic PASS/FAIL ratios for a composite catalog rule."""

    rule_id: str
    rule_name: str
    atomic_prefix: str
    mode: str = "bullish"
    version: str = "1.0.0"
    dependencies: tuple[str, ...] = ()

    def _relevant(self, atomic: dict[str, RuleResult]) -> dict[str, RuleResult]:
        return {
            rule_id: result
            for rule_id, result in atomic.items()
            if rule_id.startswith(self.atomic_prefix) and result.verdict != "UNKNOWN"
        }

    def _missing_or_unknown(self, atomic: dict[str, RuleResult]) -> str | None:
        relevant = self._relevant(atomic)
        if len(relevant) < MIN_ATOMIC_COVERAGE:
            return f"Insufficient atomic coverage for {self.atomic_prefix}"
        if any(result.verdict == "UNKNOWN" for result in relevant.values()):
            return f"Atomic dependency UNKNOWN in {self.atomic_prefix}"
        return None

    def decide(
        self, atomic: dict[str, RuleResult]
    ) -> tuple[RuleVerdict, list[str], dict[str, Any]]:
        relevant = self._relevant(atomic)
        passed = sum(1 for result in relevant.values() if result.verdict == "PASS")
        partial = sum(1 for result in relevant.values() if result.verdict == "PARTIAL")
        failed = sum(1 for result in relevant.values() if result.verdict == "FAIL")
        total = len(relevant)
        pass_ratio = passed / total
        fail_ratio = failed / total

        metadata = {
            "mode": self.mode,
            "atomic_prefix": self.atomic_prefix,
            "passed": passed,
            "partial": partial,
            "failed": failed,
            "total": total,
            "pass_ratio": round(pass_ratio, 4),
            "fail_ratio": round(fail_ratio, 4),
        }

        if self.mode == "bearish":
            if fail_ratio >= 0.55:
                return "PASS", [f"{self.rule_name}: bearish consensus"], metadata
            if fail_ratio >= 0.35:
                return "PARTIAL", [f"{self.rule_name}: bearish leaning"], metadata
            return "FAIL", [f"{self.rule_name}: bearish signal weak"], metadata

        if self.mode == "quality":
            verdict = verdict_from_ratio(passed, partial, failed, pass_min=6, partial_min=4)
            if verdict == "PASS":
                return "PASS", [f"{self.rule_name}: high quality"], metadata
            if verdict == "PARTIAL":
                return "PARTIAL", [f"{self.rule_name}: moderate quality"], metadata
            return "FAIL", [f"{self.rule_name}: low quality"], metadata

        if self.mode == "neutral":
            balance = abs(passed - failed) / total
            if balance <= 0.2:
                return "PASS", [f"{self.rule_name}: balanced state"], metadata
            if balance <= 0.35:
                return "PARTIAL", [f"{self.rule_name}: mixed state"], metadata
            return "FAIL", [f"{self.rule_name}: imbalanced state"], metadata

        if pass_ratio >= 0.55:
            return "PASS", [f"{self.rule_name}: bullish consensus"], metadata
        if pass_ratio >= 0.35:
            return "PARTIAL", [f"{self.rule_name}: bullish leaning"], metadata
        return "FAIL", [f"{self.rule_name}: bullish signal weak"], metadata


def infer_composite_mode(rule_name: str) -> str:
    """Infer aggregation mode from composite rule name."""
    lower = rule_name.lower()
    bearish_keys = (
        "weakness",
        "bearish",
        "death",
        "distribution",
        "selling",
        "risk",
        "failure",
        "contraction",
        "exhaustion",
        "resistance",
        "breakdown",
        "downtrend",
        "decline",
        "loss",
        "danger",
    )
    quality_keys = (
        "quality",
        "stability",
        "confirmation",
        "agreement",
        "integrity",
        "consistency",
        "structure",
        "support",
        "alignment",
        "position",
    )
    neutral_keys = (
        "neutral",
        "mixed",
        "range",
        "compression",
        "sideways",
        "balance",
        "state",
    )
    if any(key in lower for key in bearish_keys):
        return "bearish"
    if any(key in lower for key in quality_keys):
        return "quality"
    if any(key in lower for key in neutral_keys):
        return "neutral"
    return "bullish"


def make_ratio_composite(
    rule_id: str,
    rule_name: str,
    atomic_prefix: str,
    mode: str | None = None,
) -> CategoryRatioCompositeRule:
    """Build a ratio composite rule instance."""
    resolved_mode = mode or infer_composite_mode(rule_name)
    return CategoryRatioCompositeRule(
        rule_id=rule_id,
        rule_name=rule_name,
        atomic_prefix=atomic_prefix,
        mode=resolved_mode,
    )
