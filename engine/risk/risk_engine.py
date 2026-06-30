"""Risk Engine v1.0 — quantifies investment loss potential independently of Master Score."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd

from engine.core.types import (
    GateResult,
    MasterScoreResult,
    ProbabilityResult,
    RiskComponentScore,
    RiskResult,
    TrendEngineResult,
)
from engine.risk.components import evaluate_components
from engine.risk.config import RiskEngineConfigData, load_risk_config
from engine.risk.mapping import decision_from_score, grade_from_score, level_from_score


@dataclass
class RiskEngineConfig:
    config: RiskEngineConfigData | None = None
    config_path: Path | None = None


def _resolve_config(config: RiskEngineConfig | None) -> RiskEngineConfigData:
    if config and config.config:
        return config.config
    if config and config.config_path:
        return load_risk_config(config.config_path)
    return load_risk_config()


def compute_risk(
    df: pd.DataFrame,
    trend: TrendEngineResult,
    master: MasterScoreResult,
    *,
    probability: ProbabilityResult | None = None,
    gate: GateResult | None = None,
    data_valid: bool = True,
    config: RiskEngineConfig | None = None,
) -> RiskResult:
    """Quantify investment risk (0–100, higher = more dangerous).

    Risk Engine does not score, predict, or recommend.
    It does not modify Master Score, Probability, or Confidence.
    """
    cfg = _resolve_config(config)
    components = evaluate_components(
        df=df,
        trend=trend,
        master=master,
        probability=probability,
        gate=gate,
        data_valid=data_valid,
        component_weights=cfg.component_weights,
        thresholds=cfg.thresholds,
    )

    risk_score = round(sum(c.contribution for c in components), 2)
    grade = grade_from_score(risk_score)
    level = level_from_score(risk_score)
    decision = decision_from_score(risk_score)

    breakdown = [
        RiskComponentScore(
            key=c.key,
            label=c.label,
            score=c.score,
            weight=c.weight,
            contribution=c.contribution,
            reasons=list(c.reasons),
        )
        for c in components
    ]

    top_contributors = sorted(components, key=lambda c: c.contribution, reverse=True)[:3]
    reasons = [
        f"Overall Risk Score {risk_score:.2f}/100 ({grade.label}, {decision})",
        f"Risk Level: {level.label}",
        f"Config v{cfg.version} ({cfg.status})",
    ]
    for comp in top_contributors:
        reasons.append(f"{comp.label}: {comp.score:.1f} → +{comp.contribution:.2f} pts")

    return RiskResult(
        risk_score=risk_score,
        risk_grade=grade.label,
        risk_grade_stars=grade.stars,
        risk_level=level.label,
        risk_decision=decision,
        components=breakdown,
        config_version=cfg.version,
        reasons=reasons,
    )
