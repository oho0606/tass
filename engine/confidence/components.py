"""Confidence component calculators for Confidence Engine v1.0."""

from __future__ import annotations

from engine.core.types import (
    DomainScore,
    MasterScoreResult,
    RuleResult,
    RuleVerdict,
    TrendEngineResult,
)
from engine.data.validator import DataValidationResult

_BULLISH_PASS = frozenset({"TR0001", "TR0002"})
_BULLISH_FAIL = frozenset({"TR0003", "TR0004"})

_VERDICT_WEIGHT: dict[RuleVerdict, float] = {
    "PASS": 1.0,
    "PARTIAL": 0.5,
    "FAIL": 0.0,
    "UNKNOWN": 0.25,
}

_UP_DIRECTIONS = frozenset({"Up", "Weak Up", "Strong Up Trend", "Up Trend"})
_DOWN_DIRECTIONS = frozenset({"Down", "Weak Down", "Down Trend", "Weak Down Trend"})


def _rule_direction(rule_id: str, verdict: RuleVerdict) -> int:
    if verdict == "UNKNOWN":
        return 0
    if rule_id in _BULLISH_PASS:
        if verdict == "PASS":
            return 1
        if verdict == "FAIL":
            return -1
        return 0
    if rule_id in _BULLISH_FAIL:
        if verdict == "FAIL":
            return 1
        if verdict == "PASS":
            return -1
        return 0
    if verdict == "PASS":
        return 1
    if verdict == "FAIL":
        return -1
    return 0


def _alignment_ratio(signals: list[int]) -> float:
    active = [s for s in signals if s != 0]
    if not active:
        return 0.5
    majority = max(set(active), key=active.count)
    return active.count(majority) / len(active)


def _verdict_weighted_ratio(results: dict[str, RuleResult]) -> float:
    if not results:
        return 0.5
    total = sum(_VERDICT_WEIGHT.get(r.verdict, 0.0) for r in results.values())
    return total / len(results)


def compute_rule_consistency(
    atomic_results: dict[str, RuleResult],
    composite_results: dict[str, RuleResult],
    maximum: float,
) -> tuple[float, list[str]]:
    reasons: list[str] = []

    signals = [_rule_direction(rid, r.verdict) for rid, r in atomic_results.items()]
    atomic_ratio = _alignment_ratio(signals)

    pass_count = sum(1 for r in composite_results.values() if r.verdict == "PASS")
    fail_count = sum(1 for r in composite_results.values() if r.verdict == "FAIL")
    comp_total = len(composite_results) or 1
    pass_rate = pass_count / comp_total
    conflict = min(pass_rate, fail_count / comp_total) if pass_count and fail_count else 0.0
    comp_ratio = max(0.0, pass_rate - conflict * 2.0)

    score = maximum * (0.6 * atomic_ratio + 0.4 * comp_ratio)
    reasons.append(f"Atomic alignment {atomic_ratio:.0%}, composite pass rate {pass_rate:.0%}")
    if conflict > 0:
        reasons.append("Composite PASS/FAIL conflict detected")

    return max(0.0, min(maximum, score)), reasons


def compute_engine_consistency(
    master: MasterScoreResult,
    trend: TrendEngineResult | None,
    atomic_results: dict[str, RuleResult],
    maximum: float,
) -> tuple[float, list[str]]:
    reasons: list[str] = []
    implemented = [b for b in master.engine_breakdown if b.status == "implemented"]

    if len(implemented) >= 2:
        norms = [b.normalized_score for b in implemented]
        mean = sum(norms) / len(norms)
        variance = sum((n - mean) ** 2 for n in norms) / len(norms)
        coherence = 1.0 - min(1.0, variance * 4.0)
        score = maximum * coherence
        reasons.append(f"Cross-engine normalized variance {variance:.3f}")
        return max(0.0, min(maximum, score)), reasons

    if trend is None or not atomic_results:
        reasons.append("Single engine — neutral coherence baseline")
        return maximum * 0.5, reasons

    trend_norm = trend.trend_score / 200.0
    atomic_norm = sum(r.score for r in atomic_results.values()) / (20.0 * len(atomic_results))
    diff = abs(trend_norm - atomic_norm)
    coherence = 1.0 - min(1.0, diff)
    score = maximum * coherence
    reasons.append(f"Trend vs atomic score coherence {coherence:.0%}")
    return max(0.0, min(maximum, score)), reasons


def compute_indicator_agreement(
    atomic_results: dict[str, RuleResult],
    maximum: float,
) -> tuple[float, list[str]]:
    signals = [_rule_direction(rid, r.verdict) for rid, r in atomic_results.items()]
    ratio = _alignment_ratio(signals)
    score = maximum * ratio
    reasons = [f"Indicator directional agreement {ratio:.0%}"]
    return max(0.0, min(maximum, score)), reasons


def compute_composite_agreement(
    composite_results: dict[str, RuleResult],
    maximum: float,
) -> tuple[float, list[str]]:
    ratio = _verdict_weighted_ratio(composite_results)
    score = maximum * ratio
    pass_count = sum(1 for r in composite_results.values() if r.verdict == "PASS")
    reasons = [
        f"Composite weighted agreement {ratio:.0%} ({pass_count}/{len(composite_results)} PASS)"
    ]
    return max(0.0, min(maximum, score)), reasons


def compute_trend_agreement(
    trend: TrendEngineResult | None,
    composite_results: dict[str, RuleResult],
    maximum: float,
) -> tuple[float, list[str]]:
    if trend is None:
        return maximum * 0.5, ["Trend domain unavailable — neutral score"]

    ctr001 = composite_results.get("CTR001")
    direction = str(ctr001.metadata.get("direction", "Mixed")) if ctr001 else "Mixed"
    state = trend.trend_state.value

    if direction in _UP_DIRECTIONS and state in _UP_DIRECTIONS:
        ratio = 1.0
        reasons = [f"Trend direction aligned ({direction} / {state})"]
    elif direction in _DOWN_DIRECTIONS and state in _DOWN_DIRECTIONS:
        ratio = 1.0
        reasons = [f"Trend direction aligned ({direction} / {state})"]
    elif direction == "Mixed" or state == "Sideways":
        ratio = 0.5
        reasons = [f"Mixed or sideways trend ({direction} / {state})"]
    else:
        ratio = 0.25
        reasons = [f"Trend direction mismatch ({direction} vs {state})"]

    return max(0.0, min(maximum, maximum * ratio)), reasons


def compute_domain_agreement(
    domain_key: str,
    domains: dict[str, DomainScore | None],
    override: float | None,
    maximum: float,
    pending_ratio: float,
) -> tuple[float, list[str]]:
    if override is not None:
        clamped = max(0.0, min(1.0, override))
        return maximum * clamped, [f"{domain_key} agreement override {clamped:.0%}"]

    domain = domains.get(domain_key)
    if domain is None or domain.status == "pending":
        return maximum * pending_ratio, [
            f"{domain_key} domain pending — neutral {pending_ratio:.0%}"
        ]

    ratio = domain.score / domain.max_score if domain.max_score > 0 else pending_ratio
    return max(0.0, min(maximum, maximum * ratio)), [f"{domain_key} domain score ratio {ratio:.0%}"]


def compute_data_quality(
    data_quality: DataValidationResult | None,
    maximum: float,
) -> tuple[float, list[str]]:
    if data_quality is None:
        return maximum * 0.67, ["Data quality not provided — assumed acceptable"]

    if not data_quality.valid:
        return 0.0, [f"Data invalid: {', '.join(data_quality.errors)}"]

    penalty = min(len(data_quality.warnings) * 0.5, maximum)
    score = maximum - penalty
    reasons = ["Data validation passed"]
    if data_quality.warnings:
        reasons.append(f"Warnings: {', '.join(data_quality.warnings)}")
    return max(0.0, min(maximum, score)), reasons


def compute_signal_stability(
    atomic_results: dict[str, RuleResult],
    composite_results: dict[str, RuleResult],
    maximum: float,
) -> tuple[float, list[str]]:
    all_results = list(atomic_results.values()) + list(composite_results.values())
    if not all_results:
        return maximum * 0.5, ["No rule results — neutral stability"]

    unknown_count = sum(1 for r in all_results if r.verdict == "UNKNOWN")
    unknown_ratio = unknown_count / len(all_results)
    stability = 1.0 - unknown_ratio
    score = maximum * stability
    reasons = [f"Signal stability {stability:.0%} ({unknown_count} UNKNOWN)"]
    return max(0.0, min(maximum, score)), reasons


def compute_historical_consistency(
    override: float | None,
    maximum: float,
    default_ratio: float,
) -> tuple[float, list[str]]:
    ratio = default_ratio if override is None else max(0.0, min(1.0, override))
    if override is None:
        reasons = [f"Historical consistency baseline {ratio:.0%} (no history)"]
    else:
        reasons = [f"Historical consistency {ratio:.0%}"]
    return max(0.0, min(maximum, maximum * ratio)), reasons
