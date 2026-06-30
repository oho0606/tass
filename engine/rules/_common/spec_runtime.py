"""Catalog-driven rule specification runtime."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import pandas as pd

from engine.core.rule_base import BaseRule
from engine.core.types import RuleResult, RuleVerdict
from engine.rules._common.scoring import confidence_risk_for_pass, score_from_verdict

DEFAULT_LOOKBACK = 5
EQUAL_TOLERANCE_PCT = 2.0


@dataclass(frozen=True)
class RuleSpec:
    """Executable specification for a frozen catalog rule."""

    rule_id: str
    rule_name: str
    kind: str
    params: dict[str, Any] = field(default_factory=dict)


class SpecRule(BaseRule):
    """Base class for spec-driven catalog rules."""

    rule_id: str
    rule_name: str

    def default_parameters(self) -> dict[str, Any]:
        return {}

    def validate_input(self, df: pd.DataFrame) -> bool:
        return df is not None and len(df) >= 25 and "close" in df.columns

    def calculate(self, df: pd.DataFrame) -> dict[str, Any]:
        spec = _spec_for_rule(self.rule_id, self.rule_name)
        payload = evaluate_spec(df, spec)
        return {"passed": payload["passed"], **payload}

    def evaluate(self, df: pd.DataFrame) -> RuleVerdict:
        _ = df
        if self._calculation.get("passed"):
            return "PASS"
        return "FAIL"

    def _build_result(self, verdict: RuleVerdict) -> RuleResult:
        passed = verdict == "PASS"
        score = score_from_verdict(verdict)
        conf, risk = confidence_risk_for_pass(passed)
        return RuleResult(
            rule_id=self.rule_id,
            verdict=verdict,
            score=score,
            confidence_delta=conf,
            risk_delta=risk,
            reasons=[self.rule_name],
            metadata={k: v for k, v in self._calculation.items() if k != "passed"},
        )


_SPECS: dict[str, RuleSpec] = {}


def register_specs(specs: dict[str, RuleSpec]) -> None:
    """Register category specs for runtime lookup."""
    _SPECS.update(specs)


def _spec_for_rule(rule_id: str, rule_name: str) -> RuleSpec:
    if rule_id in _SPECS:
        return _SPECS[rule_id]
    from engine.rules._common.name_parser import parse_rule_name

    category = rule_id[:2]
    spec = parse_rule_name(rule_id, rule_name, category)
    _SPECS[rule_id] = spec
    return spec


def run_spec_rule(rule_cls: type[SpecRule], df: pd.DataFrame) -> RuleResult:
    """Run a spec-driven rule class."""
    rule = rule_cls()
    rule.initialize()
    return rule.run(df)


def evaluate_spec(df: pd.DataFrame, spec: RuleSpec) -> dict[str, Any]:
    """Evaluate a rule spec against OHLCV data."""
    kind = spec.kind
    params = spec.params
    handlers = {
        "compare": _eval_compare,
        "cross": _eval_cross,
        "slope": _eval_slope,
        "ohlc_compare": _eval_ohlc_compare,
        "spread_trend": _eval_spread_trend,
        "stable": _eval_stable,
        "candle": _eval_candle,
        "pattern": _eval_pattern,
        "pivot_event": _eval_pivot,
        "gap": _eval_gap,
        "dq_check": _eval_dq,
        "support_resistance": _eval_sr,
        "breakout": _eval_breakout,
        "pullback": _eval_pullback,
        "entry": _eval_entry,
        "exit": _eval_exit,
        "risk": _eval_risk,
        "market_regime": _eval_market_regime,
        "multi_timeframe": _eval_multi_timeframe,
        "confirmation": _eval_confirmation,
        "heuristic": _eval_heuristic,
    }
    handler = handlers.get(kind, _eval_heuristic)
    try:
        passed = bool(handler(df, params))
    except Exception:
        passed = False
    return {"passed": passed, "kind": kind, "params": params}


def _series(df: pd.DataFrame, key: str) -> pd.Series:
    if key in df.columns:
        return df[key]
    if key == "high_20":
        return df["high"].rolling(20).max()
    if key == "low_20":
        return df["low"].rolling(20).min()
    if key.startswith("ma_"):
        return df[key]
    return df["close"]


def _resolve_ref(df: pd.DataFrame, ref: Any, field: str = "close") -> float:
    if isinstance(ref, (int, float)):
        return float(ref)
    if ref == "prior":
        return float(_series(df, field).iloc[-2])
    if ref == "avg":
        return float(_series(df, field).rolling(20).mean().iloc[-1])
    if ref == "high":
        return float(_series(df, field).rolling(20).max().iloc[-1])
    if ref == "low":
        return float(_series(df, field).rolling(20).min().iloc[-1])
    if ref == "prior_high":
        return float(df["high"].iloc[-2])
    if ref == "prior_low":
        return float(df["low"].iloc[-2])
    if isinstance(ref, str) and ref in df.columns:
        return float(df[ref].iloc[-1])
    return float(ref)


def _near_equal(a: float, b: float, tol: float = EQUAL_TOLERANCE_PCT) -> bool:
    if b == 0:
        return a == 0
    return abs((a - b) / b * 100.0) <= tol


def _eval_compare(df: pd.DataFrame, params: dict[str, Any]) -> bool:
    series_key = params["series"]
    current = float(_series(df, series_key).iloc[-1])
    ref = _resolve_ref(df, params["ref"], series_key)
    op = params["op"]
    if op == "gt":
        return current > ref
    if op == "lt":
        return current < ref
    return _near_equal(current, ref)


def _eval_cross(df: pd.DataFrame, params: dict[str, Any]) -> bool:
    fast = _series(df, params["fast"])
    slow = _series(df, params["slow"])
    fp, fc = float(fast.iloc[-2]), float(fast.iloc[-1])
    sp, sc = float(slow.iloc[-2]), float(slow.iloc[-1])
    if params["direction"] == "above":
        return fp <= sp and fc > sc
    return fp >= sp and fc < sc


def _eval_slope(df: pd.DataFrame, params: dict[str, Any]) -> bool:
    series = _series(df, params["series"])
    lookback = DEFAULT_LOOKBACK
    if len(series) <= lookback:
        return False
    start = float(series.iloc[-lookback - 1])
    end = float(series.iloc[-1])
    slope = (end - start) / start * 100.0 if start else 0.0
    direction = params["direction"]
    if direction == "rising":
        return slope > 0.0
    if direction == "falling":
        return slope < 0.0
    if direction == "flat":
        return abs(slope) <= 2.0
    prev_start = float(series.iloc[-lookback * 2 - 1])
    prev_end = float(series.iloc[-lookback - 1])
    prev = (prev_end - prev_start) / prev_start * 100.0 if prev_start else 0.0
    return (slope > 0 > prev) or (slope < 0 < prev)


def _bar_metrics(df: pd.DataFrame) -> dict[str, float]:
    o = float(df["open"].iloc[-1])
    h = float(df["high"].iloc[-1])
    low = float(df["low"].iloc[-1])
    c = float(df["close"].iloc[-1])
    body = abs(c - o)
    rng = h - low if h > low else 0.0
    return {"open": o, "high": h, "low": low, "close": c, "body": body, "range": rng}


def _eval_ohlc_compare(df: pd.DataFrame, params: dict[str, Any]) -> bool:
    metrics = _bar_metrics(df)
    current = metrics[params["field"]]
    ref = _resolve_ref(df, params["ref"], params["field"])
    op = params["op"]
    if op == "gt":
        return current > ref
    if op == "lt":
        return current < ref
    return _near_equal(current, ref)


def _eval_spread_trend(df: pd.DataFrame, params: dict[str, Any]) -> bool:
    target = _series(df, params["target"])
    short = target.rolling(5).mean()
    long = target.rolling(20).mean()
    current = abs(float(short.iloc[-1]) - float(long.iloc[-1]))
    previous = abs(float(short.iloc[-6]) - float(long.iloc[-6]))
    if params["direction"] == "expand":
        return current > previous
    return current < previous


def _eval_stable(df: pd.DataFrame, params: dict[str, Any]) -> bool:
    series = _series(df, params["series"])
    window = series.iloc[-DEFAULT_LOOKBACK:]
    spread = float(window.max() - window.min())
    base = float(window.mean()) or 1.0
    return spread / base * 100.0 <= 5.0


def _eval_candle(df: pd.DataFrame, params: dict[str, Any]) -> bool:
    m = _bar_metrics(df)
    label = params["label"]
    if label == "Bullish Candle":
        return m["close"] > m["open"]
    if label == "Bearish Candle":
        return m["close"] < m["open"]
    if label == "Doji Candle":
        return m["range"] > 0 and m["body"] / m["range"] <= 0.1
    return False


def _eval_pattern(df: pd.DataFrame, params: dict[str, Any]) -> bool:
    from engine.rules._common.patterns import detect_pattern

    return detect_pattern(df, params["pattern"])


def _eval_pivot(df: pd.DataFrame, params: dict[str, Any]) -> bool:
    from engine.core.pivots import find_pivot_highs, find_pivot_lows

    event = params["event"].lower()
    highs = find_pivot_highs(df["high"], strength=3)
    lows = find_pivot_lows(df["low"], strength=3)
    if "swing high" in event or "higher high" in event:
        return len(highs) > 0 and highs[-1] >= len(df) - 5
    if "swing low" in event or "higher low" in event:
        return len(lows) > 0 and lows[-1] >= len(df) - 5
    if "lower high" in event:
        return len(highs) >= 2 and df["high"].iloc[highs[-1]] < df["high"].iloc[highs[-2]]
    if "lower low" in event:
        return len(lows) >= 2 and df["low"].iloc[lows[-1]] < df["low"].iloc[lows[-2]]
    return len(highs) > 0 or len(lows) > 0


def _eval_gap(df: pd.DataFrame, params: dict[str, Any]) -> bool:
    label = params["label"].lower()
    prev_high = float(df["high"].iloc[-2])
    prev_low = float(df["low"].iloc[-2])
    prev_close = float(df["close"].iloc[-2])
    o = float(df["open"].iloc[-1])
    if "gap up" in label:
        return o > prev_high
    if "gap down" in label:
        return o < prev_low
    if "open above prior close" in label:
        return o > prev_close
    if "open below prior close" in label:
        return o < prev_close
    return abs(o - prev_close) / prev_close * 100.0 >= 1.0 if prev_close else False


def _eval_dq(df: pd.DataFrame, params: dict[str, Any]) -> bool:
    check = params["check"]
    if check.endswith("_missing"):
        col = check.split("_")[0]
        col_map = {
            "open": "open",
            "high": "high",
            "low": "low",
            "close": "close",
            "volume": "volume",
        }
        key = col_map.get(col, "close")
        return not pd.isna(df[key].iloc[-1])
    if check == "high_below_low":
        return float(df["high"].iloc[-1]) >= float(df["low"].iloc[-1])
    if check == "close_outside_high_low_range":
        c, h, low = (
            float(df["close"].iloc[-1]),
            float(df["high"].iloc[-1]),
            float(df["low"].iloc[-1]),
        )
        return low <= c <= h
    if check == "negative_volume_present":
        return (df["volume"] >= 0).all()
    return not df[["open", "high", "low", "close"]].iloc[-1].isna().any()


def _eval_sr(df: pd.DataFrame, params: dict[str, Any]) -> bool:
    label = params["label"].lower()
    close = float(df["close"].iloc[-1])
    support = float(df["low"].rolling(20).min().iloc[-1])
    resistance = float(df["high"].rolling(20).max().iloc[-1])
    ma20 = float(df["ma_20"].iloc[-1]) if "ma_20" in df.columns else support
    if "above horizontal support" in label or "above dynamic support" in label:
        return close > support
    if "below horizontal resistance" in label or "below dynamic resistance" in label:
        return close < resistance
    if "near" in label or "at" in label or "touching" in label:
        level = support if "support" in label else resistance
        return _near_equal(close, level, 1.5)
    if "dynamic support present" in label:
        return close > ma20
    return close > support or close < resistance


def _eval_breakout(df: pd.DataFrame, params: dict[str, Any]) -> bool:
    label = params["label"].lower()
    close = float(df["close"].iloc[-1])
    high20 = float(df["high"].rolling(20).max().iloc[-2])
    low20 = float(df["low"].rolling(20).min().iloc[-2])
    if "close above n-period high" in label:
        return close > high20
    if "close below n-period low" in label:
        return close < low20
    if "bullish" in label:
        return close > float(df["open"].iloc[-1])
    if "bearish" in label:
        return close < float(df["open"].iloc[-1])
    return False


def _eval_pullback(df: pd.DataFrame, params: dict[str, Any]) -> bool:
    label = params["label"].lower()
    if "pullback in progress" in label:
        ma20 = float(df["ma_20"].iloc[-1])
        close = float(df["close"].iloc[-1])
        return close < close * 1.02 and close > ma20 * 0.95
    if "volume below" in label:
        return float(df["volume"].iloc[-1]) < float(df["volume_ma_20"].iloc[-1])
    return float(df["close"].iloc[-1]) < float(df["close"].rolling(5).max().iloc[-2])


def _eval_entry(df: pd.DataFrame, params: dict[str, Any]) -> bool:
    label = params["label"].lower()
    close = float(df["close"].iloc[-1])
    if "above sma20" in label:
        return close > float(df["ma_20"].iloc[-1])
    if "above sma60" in label:
        return close > float(df["ma_60"].iloc[-1])
    if "volume above" in label:
        return float(df["volume"].iloc[-1]) > float(df["volume_ma_20"].iloc[-1])
    if "wide range" in label:
        return (
            _bar_metrics(df)["range"] > df["high"].subtract(df["low"]).rolling(20).mean().iloc[-1]
        )
    return close > float(df["open"].iloc[-1])


def _eval_exit(df: pd.DataFrame, params: dict[str, Any]) -> bool:
    label = params["label"].lower()
    close = float(df["close"].iloc[-1])
    if "below sma20" in label:
        return close < float(df["ma_20"].iloc[-1])
    if "below sma60" in label:
        return close < float(df["ma_60"].iloc[-1])
    if "below ema20" in label:
        return close < float(df["ema_20"].iloc[-1])
    if "below ema60" in label:
        return close < float(df["ema_60"].iloc[-1])
    if "below prior close" in label:
        return close < float(df["close"].iloc[-2])
    if "below n-period low" in label:
        return close < float(df["low"].rolling(20).min().iloc[-1])
    if "volume below" in label:
        return float(df["volume"].iloc[-1]) < float(df["volume_ma_20"].iloc[-1])
    if "bearish" in label:
        return close < float(df["open"].iloc[-1])
    if "narrow range" in label:
        return (
            _bar_metrics(df)["range"] <= df["high"].subtract(df["low"]).rolling(20).mean().iloc[-1]
        )
    return close < float(df["open"].iloc[-1])


def _eval_risk(df: pd.DataFrame, params: dict[str, Any]) -> bool:
    label = params["label"].lower()
    if "atr above" in label:
        return float(df["atr_14"].iloc[-1]) > float(df["atr_14"].rolling(20).mean().iloc[-1])
    if "volume below" in label:
        return float(df["volume"].iloc[-1]) < float(df["volume_ma_20"].iloc[-1])
    if "gap" in label and "present" in label:
        return abs(float(df["open"].iloc[-1]) - float(df["close"].iloc[-2])) > 0
    return False


def _eval_market_regime(df: pd.DataFrame, params: dict[str, Any]) -> bool:
    label = params["label"].lower()
    close = float(df["close"].iloc[-1])
    if "close above sma200" in label:
        return close > float(df["ma_240"].iloc[-1])
    if "close below sma200" in label:
        return close < float(df["ma_240"].iloc[-1])
    if "close above sma60" in label:
        return close > float(df["ma_60"].iloc[-1])
    if "close below sma60" in label:
        return close < float(df["ma_60"].iloc[-1])
    if "sideways" in label or "between" in label:
        ma20 = float(df["ma_20"].iloc[-1])
        ma60 = float(df["ma_60"].iloc[-1])
        return min(ma20, ma60) <= close <= max(ma20, ma60)
    if "adx above" in label:
        return "adx_14" in df.columns and float(df["adx_14"].iloc[-1]) >= 25.0
    return close > float(df["ma_20"].iloc[-1])


def _eval_multi_timeframe(df: pd.DataFrame, params: dict[str, Any]) -> bool:
    label = params["label"].lower()
    close = float(df["close"].iloc[-1])
    long_ma = float(df["ma_240"].iloc[-1])
    short_ma = float(df["ma_20"].iloc[-1])
    up = close > short_ma > long_ma
    down = close < short_ma < long_ma
    if "uptrend match" in label or "supports" in label:
        return up
    if "downtrend match" in label or "conflict" in label or "opposes" in label:
        return down
    return up or down


def _eval_confirmation(df: pd.DataFrame, params: dict[str, Any]) -> bool:
    label = params["label"].lower()
    close = float(df["close"].iloc[-1])
    up = close > float(df["close"].iloc[-2])
    vol_up = float(df["volume"].iloc[-1]) > float(df["volume"].iloc[-2])
    if "bullish" in label and "volume" in label:
        return up and vol_up
    if "bearish" in label and "volume" in label:
        return (not up) and vol_up
    if "price and volume agreement" in label:
        return (up and vol_up) or ((not up) and not vol_up)
    if "confirmation present" in label:
        return up and vol_up
    if "confirmation absent" in label:
        return not (up and vol_up)
    return up


def _eval_heuristic(df: pd.DataFrame, params: dict[str, Any]) -> bool:
    label = params.get("label", "").lower()
    close = float(df["close"].iloc[-1])
    if "bullish" in label:
        return close > float(df["open"].iloc[-1])
    if "bearish" in label:
        return close < float(df["open"].iloc[-1])
    if "above" in label:
        return close > float(df["ma_20"].iloc[-1])
    if "below" in label:
        return close < float(df["ma_20"].iloc[-1])
    return close >= float(df["close"].iloc[-2])
