from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from enum import Enum
from typing import Any, Literal

import pandas as pd

RuleVerdict = Literal["PASS", "PARTIAL", "FAIL", "UNKNOWN"]
RuleStatus = RuleVerdict | Literal["WARN"]  # WARN deprecated; use PASS+low score
GateStatus = Literal["PASS", "WARN", "FAIL"]


class TrendGrade(str, Enum):
    S = "S"
    A = "A"
    B = "B"
    C = "C"
    D = "D"


class TrendState(str, Enum):
    STRONG_UP = "Strong Up Trend"
    UP = "Up Trend"
    SIDEWAYS = "Sideways"
    WEAK_DOWN = "Weak Down Trend"
    DOWN = "Down Trend"


@dataclass(frozen=True)
class OHLCVBar:
    date: date
    open: float
    high: float
    low: float
    close: float
    volume: float


@dataclass
class RuleResult:
    rule_id: str
    verdict: RuleVerdict
    score: float
    status: RuleStatus = ""  # mirrors verdict; WARN legacy composite
    confidence_delta: float = 0.0
    risk_delta: float = 0.0
    reasons: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.status:
            self.status = self.verdict  # type: ignore[assignment]


@dataclass
class TrendEngineResult:
    trend_score: float
    trend_grade: TrendGrade
    trend_state: TrendState
    trend_confidence: float
    trend_risk: float
    atomic_results: dict[str, RuleResult]
    composite_results: dict[str, RuleResult]
    reasons: list[str] = field(default_factory=list)


@dataclass
class MovingAverageEngineResult:
    ma_score: float
    ma_grade: str
    ma_state: str
    atomic_results: dict[str, RuleResult]
    reasons: list[str] = field(default_factory=list)


@dataclass
class VolumeEngineResult:
    vl_score: float
    vl_grade: str
    vl_state: str
    atomic_results: dict[str, RuleResult]
    reasons: list[str] = field(default_factory=list)


@dataclass
class DomainEngineResult:
    """Generic domain engine output for catalog-driven domains."""

    engine_key: str
    score: float
    max_score: float
    grade: str
    state: str
    atomic_results: dict[str, RuleResult]
    composite_results: dict[str, RuleResult] = field(default_factory=dict)
    reasons: list[str] = field(default_factory=list)


@dataclass
class DomainBundle:
    """All domain engine outputs for one symbol evaluation."""

    trend: TrendEngineResult
    moving_average: MovingAverageEngineResult
    volume: VolumeEngineResult
    domains: dict[str, DomainEngineResult] = field(default_factory=dict)


@dataclass
class GateResult:
    status: GateStatus
    reasons: list[str] = field(default_factory=list)
    failed_gates: list[str] = field(default_factory=list)


@dataclass
class DomainScore:
    score: float
    max_score: float
    grade: str | None = None
    state: str | None = None
    status: str = "implemented"


@dataclass
class EngineBreakdown:
    engine_name: str
    engine_key: str
    raw_score: float
    maximum_score: float
    normalized_score: float
    weight: float
    contribution: float
    final_score: float
    status: str = "implemented"


@dataclass
class MasterScoreResult:
    total_score: float
    max_score: float
    mvp_mode: bool
    domains: dict[str, DomainScore | None]
    grade: str | None = None
    grade_stars: str | None = None
    interpretation: str | None = None
    engine_breakdown: list[EngineBreakdown] = field(default_factory=list)
    reasons: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class ConfidenceInterval:
    lower: float
    upper: float


@dataclass
class ProbabilityResult:
    master_score: float
    winning_probability: float
    probability_grade: str
    probability_level: str
    calibration_version: str
    historical_win_rate: float
    sample_size: int
    confidence_interval: ConfidenceInterval
    last_calibration_date: str
    score_bucket_min: float
    score_bucket_max: float
    reasons: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class ConfidenceBreakdown:
    component_key: str
    component_name: str
    score: float
    maximum: float


@dataclass
class AgreementReport:
    indicator_agreement: float
    composite_agreement: float
    trend_agreement: float
    volume_agreement: float
    momentum_agreement: float
    volatility_agreement: float
    multi_timeframe_agreement: float
    market_regime_agreement: float
    agreement_score: float
    reasons: list[str] = field(default_factory=list)


@dataclass
class ConsistencyReport:
    rule_consistency: float
    engine_consistency: float
    signal_stability: float
    historical_consistency: float
    reasons: list[str] = field(default_factory=list)


@dataclass
class ConfidenceResult:
    confidence_score: float
    confidence_grade: str
    confidence_level: str
    confidence_stars: str
    rule_consistency: float
    engine_consistency: float
    agreement_score: float
    data_quality: float
    timeframe_agreement: float
    historical_stability: float
    breakdown: list[ConfidenceBreakdown]
    agreement_report: AgreementReport
    consistency_report: ConsistencyReport
    master_score: float
    probability: float | None
    version: str
    reasons: list[str] = field(default_factory=list)


@dataclass
class RiskComponentScore:
    key: str
    label: str
    score: float
    weight: int
    contribution: float
    reasons: list[str] = field(default_factory=list)


@dataclass
class RiskResult:
    risk_score: float
    risk_grade: str
    risk_grade_stars: str
    risk_level: str
    risk_decision: str
    components: list[RiskComponentScore]
    config_version: str
    reasons: list[str] = field(default_factory=list)


RecommendationAction = Literal[
    "STRONG BUY",
    "BUY",
    "WATCHLIST",
    "HOLD",
    "NOT RECOMMENDED",
    "REJECT",
]


@dataclass(frozen=True)
class RecommendationGateReport:
    gate_key: str
    gate_name: str
    status: Literal["PASS", "FAIL"]
    threshold: str
    actual: str
    reason: str


@dataclass
class RecommendationResult:
    symbol: str
    name: str
    recommendation: RecommendationAction
    recommendation_grade: str
    recommendation_rank: int | None
    master_score: float
    winning_probability: float
    confidence_score: float
    risk_score: float
    recommendation_reason: list[str]
    domain_breakdown: dict[str, Any]
    composite_breakdown: dict[str, Any]
    gate_report: list[RecommendationGateReport]
    passed_conditions: list[str]
    failed_conditions: list[str]
    is_candidate: bool
    version: str
    volume: float | None = None
    max_score: float | None = None
    grade: str | None = None
    probability_grade: str | None = None
    probability_level: str | None = None
    confidence_grade: str | None = None
    confidence_level: str | None = None
    confidence_stars: str | None = None
    risk_grade: str | None = None
    risk_grade_stars: str | None = None
    risk_level: str | None = None
    risk_decision: str | None = None
    risk_breakdown: list[dict[str, Any]] | None = None
    gate: GateStatus | None = None
    pipeline_gate_report: list[dict[str, Any]] | None = None


@dataclass
class PickResult:
    rank: int
    symbol: str
    name: str
    total_score: float
    max_score: float
    domains: dict[str, Any]
    confidence: float | None
    risk: float | None
    reasons: list[str]
    gate: GateStatus
    grade: str | None = None
    probability: float | None = None
    probability_grade: str | None = None
    probability_level: str | None = None
    risk_grade: str | None = None
    risk_grade_stars: str | None = None
    risk_level: str | None = None
    risk_decision: str | None = None
    risk_breakdown: list[dict[str, Any]] | None = None
    confidence_grade: str | None = None
    confidence_level: str | None = None
    confidence_stars: str | None = None
    recommendation: RecommendationAction | None = None
    recommendation_grade: str | None = None
    recommendation_reason: list[str] | None = None
    passed_conditions: list[str] | None = None
    failed_conditions: list[str] | None = None
    gate_report: list[dict[str, Any]] | None = None
    composite_breakdown: dict[str, Any] | None = None


IndicatorFrame = pd.DataFrame
