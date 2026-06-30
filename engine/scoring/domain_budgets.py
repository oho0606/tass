"""Fixed engine weights for Scoring Engine v1.0 (Frozen)."""

from __future__ import annotations

MASTER_MAX_SCORE = 1000.0

# Engine key → (display name, maximum score / weight)
ENGINE_WEIGHTS: dict[str, tuple[str, float]] = {
    "trend": ("Trend", 200.0),
    "moving_average": ("Moving Average", 150.0),
    "price_action": ("Price Action", 100.0),
    "volume": ("Volume", 150.0),
    "momentum": ("Momentum", 150.0),
    "volatility": ("Volatility", 100.0),
    "market_structure": ("Market Structure", 50.0),
    "support_resistance": ("Support & Resistance", 20.0),
    "breakout": ("Breakout", 20.0),
    "pullback": ("Pullback", 20.0),
    "pattern": ("Pattern", 20.0),
    "candlestick": ("Candlestick", 20.0),
    "gap": ("Gap", 10.0),
    "risk": ("Risk", 50.0),
    "entry": ("Entry", 50.0),
    "exit": ("Exit", 50.0),
    "market_regime": ("Market Regime", 30.0),
    "multi_timeframe": ("Multi Timeframe", 30.0),
    "confirmation": ("Confirmation", 30.0),
    "data_quality": ("Data Quality", 20.0),
}

# Legacy aliases used by MVP pipeline consumers
DOMAIN_ALIASES: dict[str, str] = {
    "ma": "moving_average",
}

MVP_ENGINES: frozenset[str] = frozenset({"trend", "moving_average", "volume"})
