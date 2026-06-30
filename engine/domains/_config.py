"""Domain engine configuration: atomic subsets and category mapping."""

from __future__ import annotations

from dataclasses import dataclass

from engine.scoring.domain_budgets import ENGINE_WEIGHTS

RULE_MAX_SCORE = 10.0


@dataclass(frozen=True)
class DomainEngineConfig:
    engine_key: str
    atomic_prefix: str
    atomic_rules: tuple[str, ...]
    atomic_weights: dict[str, float]
    composite_rules: tuple[str, ...] = ()


def _weights(rule_ids: tuple[str, ...], overrides: dict[str, float] | None = None) -> dict[str, float]:
    base = {rule_id: 1.0 for rule_id in rule_ids}
    if overrides:
        base.update(overrides)
    return base


DOMAIN_ENGINE_CONFIGS: dict[str, DomainEngineConfig] = {
    "price_action": DomainEngineConfig(
        engine_key="price_action",
        atomic_prefix="PA",
        atomic_rules=("PA0001", "PA0004", "PA0007", "PA0009", "PA0011", "PA0057"),
        atomic_weights=_weights(
            ("PA0001", "PA0004", "PA0007", "PA0009", "PA0011", "PA0057"),
            {"PA0007": 1.2, "PA0057": 1.1},
        ),
    ),
    "momentum": DomainEngineConfig(
        engine_key="momentum",
        atomic_prefix="MO",
        atomic_rules=("MO0003", "MO0005", "MO0011", "MO0013", "MO0017", "MO0019"),
        atomic_weights=_weights(
            ("MO0003", "MO0005", "MO0011", "MO0013", "MO0017", "MO0019"),
            {"MO0011": 1.2, "MO0013": 1.2},
        ),
    ),
    "volatility": DomainEngineConfig(
        engine_key="volatility",
        atomic_prefix="VO",
        atomic_rules=("VO0036", "VO0051", "VO0054", "VO0059", "VO0029", "VO0056"),
        atomic_weights=_weights(
            ("VO0036", "VO0051", "VO0054", "VO0059", "VO0029", "VO0056"),
            {"VO0059": 1.2},
        ),
    ),
    "market_structure": DomainEngineConfig(
        engine_key="market_structure",
        atomic_prefix="MS",
        atomic_rules=("MS0001", "MS0002", "MS0004", "MS0006", "MS0007", "MS0009"),
        atomic_weights=_weights(
            ("MS0001", "MS0002", "MS0004", "MS0006", "MS0007", "MS0009"),
            {"MS0001": 1.2, "MS0004": 1.1},
        ),
    ),
    "support_resistance": DomainEngineConfig(
        engine_key="support_resistance",
        atomic_prefix="SR",
        atomic_rules=("SR0001", "SR0003", "SR0021", "SR0010"),
        atomic_weights=_weights(("SR0001", "SR0003", "SR0021", "SR0010"), {"SR0001": 1.2}),
    ),
    "breakout": DomainEngineConfig(
        engine_key="breakout",
        atomic_prefix="BO",
        atomic_rules=("BO0001", "BO0003", "BO0005", "BO0007"),
        atomic_weights=_weights(("BO0001", "BO0003", "BO0005", "BO0007"), {"BO0001": 1.3}),
    ),
    "pullback": DomainEngineConfig(
        engine_key="pullback",
        atomic_prefix="PB",
        atomic_rules=("PB0001", "PB0003", "PB0005", "PB0007"),
        atomic_weights=_weights(("PB0001", "PB0003", "PB0005", "PB0007")),
    ),
    "pattern": DomainEngineConfig(
        engine_key="pattern",
        atomic_prefix="PT",
        atomic_rules=("PT0001", "PT0003", "PT0005", "PT0007"),
        atomic_weights=_weights(("PT0001", "PT0003", "PT0005", "PT0007")),
    ),
    "candlestick": DomainEngineConfig(
        engine_key="candlestick",
        atomic_prefix="CS",
        atomic_rules=("CS0001", "CS0003", "CS0005", "CS0007"),
        atomic_weights=_weights(("CS0001", "CS0003", "CS0005", "CS0007")),
    ),
    "gap": DomainEngineConfig(
        engine_key="gap",
        atomic_prefix="GP",
        atomic_rules=("GP0001", "GP0003"),
        atomic_weights=_weights(("GP0001", "GP0003")),
    ),
    "risk": DomainEngineConfig(
        engine_key="risk",
        atomic_prefix="RK",
        atomic_rules=("RK0001", "RK0003", "RK0005", "RK0007", "RK0009"),
        atomic_weights=_weights(
            ("RK0001", "RK0003", "RK0005", "RK0007", "RK0009"),
            {"RK0005": 0.8},
        ),
    ),
    "entry": DomainEngineConfig(
        engine_key="entry",
        atomic_prefix="EN",
        atomic_rules=("EN0001", "EN0002", "EN0003", "EN0004", "EN0007", "EN0008"),
        atomic_weights=_weights(
            ("EN0001", "EN0002", "EN0003", "EN0004", "EN0007", "EN0008"),
            {"EN0001": 1.2, "EN0008": 1.1},
        ),
    ),
    "exit": DomainEngineConfig(
        engine_key="exit",
        atomic_prefix="EX",
        atomic_rules=("EX0001", "EX0002", "EX0003", "EX0004", "EX0007", "EX0008"),
        atomic_weights=_weights(
            ("EX0001", "EX0002", "EX0003", "EX0004", "EX0007", "EX0008"),
            {"EX0001": 1.2, "EX0008": 1.1},
        ),
        composite_rules=("CEX001", "CEX002", "CEX003", "CEX004", "CEX005"),
    ),
    "market_regime": DomainEngineConfig(
        engine_key="market_regime",
        atomic_prefix="MR",
        atomic_rules=("MR0001", "MR0003", "MR0005", "MR0007"),
        atomic_weights=_weights(("MR0001", "MR0003", "MR0005", "MR0007"), {"MR0001": 1.2}),
    ),
    "multi_timeframe": DomainEngineConfig(
        engine_key="multi_timeframe",
        atomic_prefix="MT",
        atomic_rules=("MT0001", "MT0003", "MT0005", "MT0007"),
        atomic_weights=_weights(("MT0001", "MT0003", "MT0005", "MT0007"), {"MT0001": 1.2}),
    ),
    "confirmation": DomainEngineConfig(
        engine_key="confirmation",
        atomic_prefix="CF",
        atomic_rules=("CF0001", "CF0003", "CF0005", "CF0007"),
        atomic_weights=_weights(("CF0001", "CF0003", "CF0005", "CF0007"), {"CF0001": 1.2}),
    ),
    "data_quality": DomainEngineConfig(
        engine_key="data_quality",
        atomic_prefix="DQ",
        atomic_rules=("DQ0011", "DQ0012", "DQ0016", "DQ0051"),
        atomic_weights=_weights(
            ("DQ0011", "DQ0012", "DQ0016", "DQ0051"),
            {"DQ0051": 1.3},
        ),
    ),
}


def domain_budget(engine_key: str) -> float:
    """Return frozen budget for a domain engine key."""
    return ENGINE_WEIGHTS[engine_key][1]
