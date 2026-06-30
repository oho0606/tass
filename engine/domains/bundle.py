"""Evaluate all domain engines for one OHLCV frame."""

from __future__ import annotations

import pandas as pd

from engine.core.types import DomainBundle, DomainEngineResult
from engine.domains._config import DOMAIN_ENGINE_CONFIGS
from engine.domains._generic_engine import evaluate_generic_domain_engine
from engine.domains.moving_average_engine import evaluate_moving_average_engine
from engine.domains.trend_engine import evaluate_trend_engine
from engine.domains.volume_engine import evaluate_volume_engine

IMPLEMENTED_GENERIC_KEYS = frozenset(DOMAIN_ENGINE_CONFIGS.keys())
PENDING_ENGINE_KEYS: frozenset[str] = frozenset()


def evaluate_generic_domains(df: pd.DataFrame) -> dict[str, DomainEngineResult]:
    """Evaluate all catalog-driven generic domain engines."""
    return {
        key: evaluate_generic_domain_engine(config, df)
        for key, config in DOMAIN_ENGINE_CONFIGS.items()
    }


def evaluate_domain_bundle(df: pd.DataFrame) -> DomainBundle:
    """Evaluate trend, MA, volume, and all generic domain engines."""
    return DomainBundle(
        trend=evaluate_trend_engine(df),
        moving_average=evaluate_moving_average_engine(df),
        volume=evaluate_volume_engine(df),
        domains=evaluate_generic_domains(df),
    )
