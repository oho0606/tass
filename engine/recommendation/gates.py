"""Gate evaluation for Recommendation Engine v1.0."""

from __future__ import annotations

from engine.core.types import (
    ConfidenceResult,
    MasterScoreResult,
    ProbabilityResult,
    RecommendationGateReport,
    RiskResult,
    RuleResult,
    TrendEngineResult,
    TrendState,
)
from engine.recommendation.config import GateThresholds
from engine.recommendation.normalize import normalized_master_score, normalized_probability


def _market_regime_pass(
    *,
    confidence: ConfidenceResult,
    trend: TrendEngineResult,
    thresholds: GateThresholds,
    explicit: bool | None,
) -> tuple[bool, str]:
    regime_score = confidence.agreement_report.market_regime_agreement
    if explicit is not None:
        return explicit, f"{regime_score:.1f}%"
    if regime_score >= thresholds.market_regime_min:
        return True, f"{regime_score:.1f}%"
    if trend.trend_state in (TrendState.UP, TrendState.STRONG_UP):
        return True, f"{regime_score:.1f}% (trend-favorable)"
    return False, f"{regime_score:.1f}%"


def _detect_critical_conflict(
    atomics: dict[str, RuleResult],
    thresholds: GateThresholds,
) -> tuple[bool, str]:
    verdicts = [r.verdict for r in atomics.values()]
    pass_count = verdicts.count("PASS")
    fail_count = verdicts.count("FAIL")
    if (
        pass_count >= thresholds.critical_conflict_min_pass
        and fail_count >= thresholds.critical_conflict_min_fail
    ):
        return True, f"PASS={pass_count}, FAIL={fail_count}"
    return False, f"PASS={pass_count}, FAIL={fail_count}"


def _composite_validation(
    composites: dict[str, RuleResult],
    thresholds: GateThresholds,
) -> tuple[bool, str]:
    scoped = {
        rule_id: result
        for rule_id, result in composites.items()
        if rule_id in thresholds.validation_composites
    }
    fail_count = sum(1 for r in scoped.values() if r.verdict == "FAIL")
    if fail_count > thresholds.max_composite_failures:
        return False, f"{fail_count} core composite FAIL"
    return True, f"{fail_count} core composite FAIL (max {thresholds.max_composite_failures})"


def evaluate_recommendation_gates(
    *,
    master: MasterScoreResult,
    probability: ProbabilityResult,
    confidence: ConfidenceResult,
    risk: RiskResult,
    trend: TrendEngineResult,
    data_quality_pass: bool,
    market_regime_pass: bool | None,
    thresholds: GateThresholds,
) -> tuple[bool, list[RecommendationGateReport], list[str], list[str]]:
    reports: list[RecommendationGateReport] = []
    passed: list[str] = []
    failed: list[str] = []
    effective_master = normalized_master_score(master)
    effective_probability = normalized_probability(master, probability)
    master_min = thresholds.master_score_min

    gate_checks: list[tuple[str, str, bool, str, str, str]] = [
        (
            "master_score",
            "Master Score",
            effective_master >= master_min,
            f">= {master_min:.0f}",
            f"{effective_master:.0f}",
            "Master Score below minimum",
        ),
        (
            "probability",
            "Probability",
            effective_probability >= thresholds.probability_min,
            f">= {thresholds.probability_min:.0f}%",
            f"{effective_probability:.1f}%",
            "Winning probability below minimum",
        ),
        (
            "confidence",
            "Confidence",
            confidence.confidence_score >= thresholds.confidence_min,
            f">= {thresholds.confidence_min:.0f}",
            f"{confidence.confidence_score:.1f}",
            "Confidence below minimum",
        ),
        (
            "risk",
            "Risk",
            risk.risk_score <= thresholds.risk_max,
            f"<= {thresholds.risk_max:.0f}",
            f"{risk.risk_score:.1f}",
            "Risk above maximum",
        ),
        (
            "data_quality",
            "Data Quality",
            data_quality_pass,
            "PASS",
            "PASS" if data_quality_pass else "FAIL",
            "Data quality validation failed",
        ),
    ]

    regime_pass, regime_detail = _market_regime_pass(
        confidence=confidence,
        trend=trend,
        thresholds=thresholds,
        explicit=market_regime_pass,
    )
    gate_checks.append(
        (
            "market_regime",
            "Market Regime",
            regime_pass,
            f">= {thresholds.market_regime_min:.0f}%",
            regime_detail,
            "Market regime unfavorable",
        )
    )

    conflict, conflict_detail = _detect_critical_conflict(trend.atomic_results, thresholds)
    gate_checks.append(
        (
            "critical_rule_conflict",
            "Critical Rule Conflict",
            not conflict,
            "None",
            conflict_detail,
            "Critical rule conflict detected",
        )
    )

    composite_ok, composite_detail = _composite_validation(trend.composite_results, thresholds)
    gate_checks.append(
        (
            "composite_validation",
            "Composite Validation",
            composite_ok,
            "PASS",
            composite_detail,
            "Composite validation failed",
        )
    )

    all_pass = True
    for key, name, ok, threshold, actual, reason in gate_checks:
        status = "PASS" if ok else "FAIL"
        reports.append(
            RecommendationGateReport(
                gate_key=key,
                gate_name=name,
                status=status,
                threshold=threshold,
                actual=actual,
                reason=reason if not ok else f"{name} passed",
            )
        )
        if ok:
            passed.append(name)
        else:
            failed.append(name)
            all_pass = False

    return all_pass, reports, passed, failed
