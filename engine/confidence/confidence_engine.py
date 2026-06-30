"""Confidence Engine v1.0 — quantifies signal reliability (not probability)."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from engine.confidence.components import (
    compute_composite_agreement,
    compute_data_quality,
    compute_domain_agreement,
    compute_engine_consistency,
    compute_historical_consistency,
    compute_indicator_agreement,
    compute_rule_consistency,
    compute_signal_stability,
    compute_trend_agreement,
)
from engine.confidence.config import (
    DEFAULT_COMPONENT_WEIGHTS,
    ConfidenceEngineConfig,
    load_confidence_config,
)
from engine.confidence.grades import grade_from_score, level_from_score
from engine.core.types import (
    AgreementReport,
    ConfidenceBreakdown,
    ConfidenceResult,
    ConsistencyReport,
    MasterScoreResult,
    ProbabilityResult,
    RuleResult,
    TrendEngineResult,
)
from engine.data.validator import DataValidationResult


@dataclass
class ConfidenceEngineInput:
    master: MasterScoreResult
    probability: ProbabilityResult | None = None
    trend: TrendEngineResult | None = None
    atomic_results: dict[str, RuleResult] | None = None
    composite_results: dict[str, RuleResult] | None = None
    data_quality: DataValidationResult | None = None
    volume_agreement: float | None = None
    momentum_agreement: float | None = None
    volatility_agreement: float | None = None
    multi_timeframe_agreement: float | None = None
    market_regime_agreement: float | None = None
    historical_consistency: float | None = None


def _resolve_config(config: ConfidenceEngineConfig | None) -> ConfidenceEngineConfig:
    if config is not None:
        return config
    return load_confidence_config()


def _resolve_weights(config: ConfidenceEngineConfig) -> dict[str, float]:
    if config.component_weights:
        return dict(config.component_weights)
    return dict(DEFAULT_COMPONENT_WEIGHTS)


def _extract_rule_results(
    trend: TrendEngineResult | None,
    atomic_results: dict[str, RuleResult] | None,
    composite_results: dict[str, RuleResult] | None,
) -> tuple[dict[str, RuleResult], dict[str, RuleResult]]:
    atomics = dict(atomic_results) if atomic_results else {}
    composites = dict(composite_results) if composite_results else {}

    if trend is not None:
        atomics = atomics or dict(trend.atomic_results)
        composites = composites or dict(trend.composite_results)

    return atomics, composites


def compute_confidence(
    inputs: ConfidenceEngineInput | MasterScoreResult,
    config: ConfidenceEngineConfig | None = None,
    config_path: Path | None = None,
) -> ConfidenceResult:
    """Compute signal reliability (0–100). Does not modify Master Score or Probability."""
    resolved = _resolve_config(config)
    if config_path is not None and config is None:
        resolved = load_confidence_config(config_path)

    if isinstance(inputs, MasterScoreResult):
        engine_input = ConfidenceEngineInput(master=inputs)
    else:
        engine_input = inputs

    master = engine_input.master
    weights = _resolve_weights(resolved)
    atomics, composites = _extract_rule_results(
        engine_input.trend,
        engine_input.atomic_results,
        engine_input.composite_results,
    )

    components: list[tuple[str, float, list[str]]] = []

    rule_score, rule_reasons = compute_rule_consistency(
        atomics, composites, weights["rule_consistency"]
    )
    components.append(("rule_consistency", rule_score, rule_reasons))

    engine_score, engine_reasons = compute_engine_consistency(
        master, engine_input.trend, atomics, weights["engine_consistency"]
    )
    components.append(("engine_consistency", engine_score, engine_reasons))

    indicator_score, indicator_reasons = compute_indicator_agreement(
        atomics, weights["indicator_agreement"]
    )
    components.append(("indicator_agreement", indicator_score, indicator_reasons))

    composite_score, composite_reasons = compute_composite_agreement(
        composites, weights["composite_agreement"]
    )
    components.append(("composite_agreement", composite_score, composite_reasons))

    trend_score, trend_reasons = compute_trend_agreement(
        engine_input.trend, composites, weights["trend_agreement"]
    )
    components.append(("trend_agreement", trend_score, trend_reasons))

    volume_score, volume_reasons = compute_domain_agreement(
        "volume",
        master.domains,
        engine_input.volume_agreement,
        weights["volume_agreement"],
        resolved.pending_domain_ratio,
    )
    components.append(("volume_agreement", volume_score, volume_reasons))

    momentum_score, momentum_reasons = compute_domain_agreement(
        "momentum",
        master.domains,
        engine_input.momentum_agreement,
        weights["momentum_agreement"],
        resolved.pending_domain_ratio,
    )
    components.append(("momentum_agreement", momentum_score, momentum_reasons))

    volatility_score, volatility_reasons = compute_domain_agreement(
        "volatility",
        master.domains,
        engine_input.volatility_agreement,
        weights["volatility_agreement"],
        resolved.pending_domain_ratio,
    )
    components.append(("volatility_agreement", volatility_score, volatility_reasons))

    mtf_score, mtf_reasons = compute_domain_agreement(
        "multi_timeframe",
        master.domains,
        engine_input.multi_timeframe_agreement,
        weights["multi_timeframe"],
        resolved.pending_domain_ratio,
    )
    components.append(("multi_timeframe", mtf_score, mtf_reasons))

    regime_score, regime_reasons = compute_domain_agreement(
        "market_regime",
        master.domains,
        engine_input.market_regime_agreement,
        weights["market_regime"],
        resolved.pending_domain_ratio,
    )
    components.append(("market_regime", regime_score, regime_reasons))

    dq_score, dq_reasons = compute_data_quality(engine_input.data_quality, weights["data_quality"])
    components.append(("data_quality", dq_score, dq_reasons))

    stability_score, stability_reasons = compute_signal_stability(
        atomics, composites, weights["signal_stability"]
    )
    components.append(("signal_stability", stability_score, stability_reasons))

    historical_score, historical_reasons = compute_historical_consistency(
        engine_input.historical_consistency,
        weights["historical_consistency"],
        resolved.default_historical_consistency,
    )
    components.append(("historical_consistency", historical_score, historical_reasons))

    total = round(sum(score for _, score, _ in components), 2)
    total = max(0.0, min(100.0, total))

    grade = grade_from_score(total)
    level = level_from_score(total)

    agreement_keys = (
        "indicator_agreement",
        "composite_agreement",
        "trend_agreement",
        "volume_agreement",
        "momentum_agreement",
        "volatility_agreement",
        "multi_timeframe",
        "market_regime",
    )
    score_map = {key: score for key, score, _ in components}
    agreement_total = round(sum(score_map[k] for k in agreement_keys), 2)

    agreement_report = AgreementReport(
        indicator_agreement=score_map["indicator_agreement"],
        composite_agreement=score_map["composite_agreement"],
        trend_agreement=score_map["trend_agreement"],
        volume_agreement=score_map["volume_agreement"],
        momentum_agreement=score_map["momentum_agreement"],
        volatility_agreement=score_map["volatility_agreement"],
        multi_timeframe_agreement=score_map["multi_timeframe"],
        market_regime_agreement=score_map["market_regime"],
        agreement_score=agreement_total,
        reasons=_collect_reasons(components, agreement_keys),
    )

    consistency_report = ConsistencyReport(
        rule_consistency=score_map["rule_consistency"],
        engine_consistency=score_map["engine_consistency"],
        signal_stability=score_map["signal_stability"],
        historical_consistency=score_map["historical_consistency"],
        reasons=_collect_reasons(
            components,
            (
                "rule_consistency",
                "engine_consistency",
                "signal_stability",
                "historical_consistency",
            ),
        ),
    )

    breakdown = [
        ConfidenceBreakdown(
            component_key=key,
            component_name=key.replace("_", " ").title(),
            score=round(score, 2),
            maximum=weights[key],
        )
        for key, score, _ in components
    ]

    prob_value = (
        engine_input.probability.winning_probability
        if engine_input.probability is not None
        else None
    )

    reasons = [
        f"Confidence {total:.1f}/100 ({grade.label}, {level.label})",
        f"Rule consistency {score_map['rule_consistency']:.1f}/{weights['rule_consistency']:.0f}",
        f"Engine consistency {score_map['engine_consistency']:.1f}/{weights['engine_consistency']:.0f}",
        f"Agreement score {agreement_total:.1f}",
        f"Data quality {score_map['data_quality']:.1f}/{weights['data_quality']:.0f}",
        f"Confidence Engine v{resolved.version} ({resolved.status})",
    ]

    return ConfidenceResult(
        confidence_score=total,
        confidence_grade=grade.label,
        confidence_level=level.label,
        confidence_stars=grade.stars,
        rule_consistency=score_map["rule_consistency"],
        engine_consistency=score_map["engine_consistency"],
        agreement_score=agreement_total,
        data_quality=score_map["data_quality"],
        timeframe_agreement=score_map["multi_timeframe"],
        historical_stability=score_map["historical_consistency"],
        breakdown=breakdown,
        agreement_report=agreement_report,
        consistency_report=consistency_report,
        master_score=master.total_score,
        probability=prob_value,
        version=resolved.version,
        reasons=reasons,
    )


def _collect_reasons(
    components: list[tuple[str, float, list[str]]],
    keys: tuple[str, ...],
) -> list[str]:
    reasons: list[str] = []
    for key, _, key_reasons in components:
        if key in keys:
            reasons.extend(key_reasons)
    return reasons
