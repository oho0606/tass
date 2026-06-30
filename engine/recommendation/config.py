"""Configuration loader for Recommendation Engine v1.0."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml

DEFAULT_VALIDATION_COMPOSITES: tuple[str, ...] = (
    "CTR001",
    "CTR002",
    "CTR003",
    "CTR004",
    "CTR005",
    "CTR008",
    "CTR009",
    "CTR010",
)


@dataclass(frozen=True)
class GateThresholds:
    master_score_min: float = 700.0
    probability_min: float = 60.0
    confidence_min: float = 70.0
    risk_max: float = 30.0
    market_regime_min: float = 50.0
    max_composite_failures: int = 0
    critical_conflict_min_pass: int = 2
    critical_conflict_min_fail: int = 2
    validation_composites: tuple[str, ...] = DEFAULT_VALIDATION_COMPOSITES


@dataclass(frozen=True)
class GradeThreshold:
    stars: str
    action: str
    master_score_min: float | None = None
    probability_min: float | None = None
    confidence_min: float | None = None
    risk_max: float | None = None


@dataclass(frozen=True)
class RecommendationEngineConfig:
    version: str = "1.0"
    status: str = "frozen"
    top_n: int = 20
    gates: GateThresholds = GateThresholds()
    grades: tuple[GradeThreshold, ...] = ()
    recommendable_actions: tuple[str, ...] = ("STRONG BUY", "BUY", "WATCHLIST", "HOLD")


DEFAULT_GRADES: tuple[GradeThreshold, ...] = (
    GradeThreshold("★★★★★", "STRONG BUY", 950, 90.0, 95.0, 10.0),
    GradeThreshold("★★★★☆", "BUY", 900, 80.0, 90.0, 20.0),
    GradeThreshold("★★★☆☆", "WATCHLIST", 850, 70.0, 80.0, 30.0),
    GradeThreshold("★★☆☆☆", "HOLD", 800, 60.0, 70.0, 40.0),
    GradeThreshold("★☆☆☆☆", "NOT RECOMMENDED"),
)


def load_recommendation_config(path: Path | None = None) -> RecommendationEngineConfig:
    if path is None:
        path = Path("config/recommendation_v1.yaml")
    if not path.exists():
        return RecommendationEngineConfig(grades=DEFAULT_GRADES)

    with path.open(encoding="utf-8") as f:
        raw = yaml.safe_load(f) or {}

    gates_raw = raw.get("gates") or {}
    gates = GateThresholds(
        master_score_min=float(gates_raw.get("master_score_min", 700)),
        probability_min=float(gates_raw.get("probability_min", 60.0)),
        confidence_min=float(gates_raw.get("confidence_min", 70.0)),
        risk_max=float(gates_raw.get("risk_max", 30.0)),
        market_regime_min=float(gates_raw.get("market_regime_min", 50.0)),
        max_composite_failures=int(gates_raw.get("max_composite_failures", 0)),
        critical_conflict_min_pass=int(gates_raw.get("critical_conflict_min_pass", 2)),
        critical_conflict_min_fail=int(gates_raw.get("critical_conflict_min_fail", 2)),
        validation_composites=tuple(
            str(item) for item in gates_raw.get("validation_composites") or []
        )
        or DEFAULT_VALIDATION_COMPOSITES,
    )

    grades: list[GradeThreshold] = []
    for item in raw.get("grades") or []:
        grades.append(
            GradeThreshold(
                stars=str(item["stars"]),
                action=str(item["action"]),
                master_score_min=(
                    float(item["master_score_min"]) if "master_score_min" in item else None
                ),
                probability_min=(
                    float(item["probability_min"]) if "probability_min" in item else None
                ),
                confidence_min=(
                    float(item["confidence_min"]) if "confidence_min" in item else None
                ),
                risk_max=float(item["risk_max"]) if "risk_max" in item else None,
            )
        )

    recommendable = tuple(str(a) for a in raw.get("recommendable_actions") or [])

    return RecommendationEngineConfig(
        version=str(raw.get("version", "1.0")),
        status=str(raw.get("status", "frozen")),
        top_n=int(raw.get("top_n", 20)),
        gates=gates,
        grades=tuple(grades) if grades else DEFAULT_GRADES,
        recommendable_actions=recommendable or ("STRONG BUY", "BUY", "WATCHLIST", "HOLD"),
    )
