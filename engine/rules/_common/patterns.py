"""Candlestick and chart pattern detectors for catalog rules."""

from __future__ import annotations

import pandas as pd


def _metrics(df: pd.DataFrame, idx: int = -1) -> dict[str, float]:
    o = float(df["open"].iloc[idx])
    h = float(df["high"].iloc[idx])
    low = float(df["low"].iloc[idx])
    c = float(df["close"].iloc[idx])
    body = abs(c - o)
    rng = max(h - low, 1e-9)
    upper = h - max(o, c)
    lower = min(o, c) - low
    return {
        "open": o,
        "high": h,
        "low": low,
        "close": c,
        "body": body,
        "range": rng,
        "upper": upper,
        "lower": lower,
        "bullish": c >= o,
    }


def detect_pattern(df: pd.DataFrame, pattern: str) -> bool:
    """Detect named candlestick/chart pattern on latest bars."""
    name = pattern.lower()
    cur = _metrics(df)
    prev = _metrics(df, -2) if len(df) >= 2 else cur

    if "hammer" in name and "inverted" not in name:
        return cur["lower"] >= cur["body"] * 2 and cur["upper"] <= cur["body"]
    if "inverted hammer" in name or "shooting star" in name:
        return cur["upper"] >= cur["body"] * 2 and cur["lower"] <= cur["body"]
    if "marubozu" in name:
        return cur["body"] / cur["range"] >= 0.9
    if "engulfing" in name:
        if "bullish" in name:
            return cur["bullish"] and not prev["bullish"] and cur["body"] > prev["body"]
        return (not cur["bullish"]) and prev["bullish"] and cur["body"] > prev["body"]
    if "doji" in name:
        return cur["body"] / cur["range"] <= 0.1
    if "three white soldiers" in name:
        return all(float(df["close"].iloc[i]) > float(df["open"].iloc[i]) for i in (-3, -2, -1))
    if "three black crows" in name:
        return all(float(df["close"].iloc[i]) < float(df["open"].iloc[i]) for i in (-3, -2, -1))
    if "head and shoulders" in name:
        highs = df["high"].rolling(5).max()
        return float(highs.iloc[-10]) < float(highs.iloc[-5]) > float(highs.iloc[-1])
    if "double top" in name:
        return (
            abs(float(df["high"].iloc[-1]) - float(df["high"].rolling(20).max().iloc[-5]))
            / float(df["close"].iloc[-1])
            < 0.02
        )
    if "double bottom" in name:
        return (
            abs(float(df["low"].iloc[-1]) - float(df["low"].rolling(20).min().iloc[-5]))
            / float(df["close"].iloc[-1])
            < 0.02
        )
    if "flag" in name:
        return cur["range"] < prev["range"]
    if "triangle" in name or "channel" in name or "wedge" in name:
        return (
            float(df["high"].iloc[-20:].max()) - float(df["low"].iloc[-20:].min())
            < float(df["close"].iloc[-1]) * 0.08
        )
    if "boundary defined" in name:
        return True
    return cur["range"] > 0
