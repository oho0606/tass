"""Parse frozen catalog rule names into executable rule specs."""

from __future__ import annotations

import re
from typing import Any

from engine.rules._common.spec_runtime import RuleSpec

N_PERIOD = 20
EQUAL_TOL = 2.0


def _spec(rule_id: str, rule_name: str, kind: str, **params: Any) -> RuleSpec:
    return RuleSpec(rule_id=rule_id, rule_name=rule_name, kind=kind, params=params)


def parse_rule_name(rule_id: str, rule_name: str, category: str) -> RuleSpec:
    """Convert catalog rule name to ``RuleSpec`` using pattern matching."""
    name = rule_name.strip()
    cid = category.upper()

    if cid == "DQ":
        return _spec(rule_id, name, "dq_check", check=_dq_check_key(name))

    if name.endswith(" Formed"):
        pattern = name.replace(" Formed", "")
        if cid in {"CS", "PT"}:
            return _spec(rule_id, name, "pattern", pattern=pattern)
        if cid in {"MS", "PA"}:
            return _spec(rule_id, name, "pivot_event", event=pattern)

    m = re.match(r"^(.+) Above ([\d\.]+)$", name)
    if m:
        return _spec(
            rule_id,
            name,
            "compare",
            series=_series_key(m.group(1)),
            op="gt",
            ref=float(m.group(2)),
        )

    m = re.match(r"^(.+) Below ([\d\.]+)$", name)
    if m:
        return _spec(
            rule_id,
            name,
            "compare",
            series=_series_key(m.group(1)),
            op="lt",
            ref=float(m.group(2)),
        )

    if " Above Zero" in name:
        return _spec(
            rule_id,
            name,
            "compare",
            series=_series_key(name.split(" Above Zero")[0]),
            op="gt",
            ref=0.0,
        )
    if " Below Zero" in name:
        return _spec(
            rule_id,
            name,
            "compare",
            series=_series_key(name.split(" Below Zero")[0]),
            op="lt",
            ref=0.0,
        )
    if " Below Negative " in name:
        val = float(name.split(" Below Negative ")[1])
        return _spec(
            rule_id,
            name,
            "compare",
            series=_series_key(name.split(" Below Negative ")[0]),
            op="lt",
            ref=-val,
        )

    for phrase, op, ref in (
        (" Above Prior ", "gt", "prior"),
        (" Below Prior ", "lt", "prior"),
        (" Above N-Period Average", "gt", "avg"),
        (" Below N-Period Average", "lt", "avg"),
        (" Above N-Period High", "gt", "high"),
        (" Below N-Period Low", "lt", "low"),
        (" At N-Period High", "eq", "high"),
        (" At N-Period Low", "eq", "low"),
        (" At N-Period Average", "eq", "avg"),
        (" Above Prior High", "gt", "prior_high"),
        (" Below Prior High", "lt", "prior_high"),
        (" Above Prior Low", "gt", "prior_low"),
        (" Below Prior Low", "lt", "prior_low"),
        (" Equal Prior High", "eq", "prior_high"),
        (" Equal Prior Low", "eq", "prior_low"),
    ):
        if phrase in name:
            base = name.split(phrase)[0]
            return _spec(rule_id, name, "ohlc_compare", field=_ohlc_field(base), op=op, ref=ref)

    m = re.match(r"^(.+) Cross Above (.+)$", name)
    if m:
        return _spec(
            rule_id,
            name,
            "cross",
            fast=_series_key(m.group(1)),
            slow=_series_key(m.group(2)),
            direction="above",
        )

    m = re.match(r"^(.+) Cross Below (.+)$", name)
    if m:
        return _spec(
            rule_id,
            name,
            "cross",
            fast=_series_key(m.group(1)),
            slow=_series_key(m.group(2)),
            direction="below",
        )

    if name.endswith(" Rising"):
        return _spec(rule_id, name, "slope", series=_series_key(name[:-7]), direction="rising")
    if name.endswith(" Falling"):
        return _spec(rule_id, name, "slope", series=_series_key(name[:-8]), direction="falling")
    if name.endswith(" Flat"):
        return _spec(rule_id, name, "slope", series=_series_key(name[:-5]), direction="flat")
    if name.endswith(" Turning"):
        return _spec(rule_id, name, "slope", series=_series_key(name[:-9]), direction="turning")
    if name.endswith(" Expanding"):
        return _spec(
            rule_id, name, "spread_trend", target=_series_key(name[:-11]), direction="expand"
        )
    if name.endswith(" Contracting"):
        return _spec(
            rule_id, name, "spread_trend", target=_series_key(name[:-13]), direction="contract"
        )
    if name.endswith(" Stable"):
        return _spec(rule_id, name, "stable", series=_series_key(name[:-7]))

    if name.startswith("Close "):
        return _parse_close_rule(rule_id, name)
    if name.startswith("Price "):
        return _parse_price_rule(rule_id, name)
    if name.startswith("Entry "):
        return _parse_entry_rule(rule_id, name)
    if name.startswith("Exit "):
        return _parse_exit_rule(rule_id, name)
    if " Gap " in name or name.endswith(" Gap") or name.startswith("Gap "):
        return _spec(rule_id, name, "gap", label=name)
    if cid == "MT":
        return _spec(rule_id, name, "multi_timeframe", label=name)
    if cid == "CF":
        return _spec(rule_id, name, "confirmation", label=name)
    if cid == "RK":
        return _spec(rule_id, name, "risk", label=name)
    if cid == "EN":
        return _spec(rule_id, name, "entry", label=name)
    if cid == "EX":
        return _spec(rule_id, name, "exit", label=name)
    if cid == "MR":
        return _spec(rule_id, name, "market_regime", label=name)
    if cid == "BO":
        return _spec(rule_id, name, "breakout", label=name)
    if cid == "PB":
        return _spec(rule_id, name, "pullback", label=name)
    if cid == "SR":
        return _spec(rule_id, name, "support_resistance", label=name)

    if name in {"Bullish Candle", "Bearish Candle", "Doji Candle"}:
        return _spec(rule_id, name, "candle", label=name)

    return _spec(rule_id, name, "heuristic", label=name)


def _parse_close_rule(rule_id: str, name: str) -> RuleSpec:
    if "Above SMA" in name:
        period = int(re.search(r"SMA(\d+)", name).group(1))
        return _spec(rule_id, name, "compare", series="close", op="gt", ref=f"ma_{period}")
    if "Below SMA" in name:
        period = int(re.search(r"SMA(\d+)", name).group(1))
        return _spec(rule_id, name, "compare", series="close", op="lt", ref=f"ma_{period}")
    if "Above N-Period High" in name:
        return _spec(rule_id, name, "compare", series="close", op="gt", ref="high_20")
    if "Below N-Period Low" in name:
        return _spec(rule_id, name, "compare", series="close", op="lt", ref="low_20")
    return _spec(rule_id, name, "heuristic", label=name)


def _parse_price_rule(rule_id: str, name: str) -> RuleSpec:
    return _spec(rule_id, name, "support_resistance", label=name)


def _parse_entry_rule(rule_id: str, name: str) -> RuleSpec:
    return _spec(rule_id, name, "entry", label=name)


def _parse_exit_rule(rule_id: str, name: str) -> RuleSpec:
    return _spec(rule_id, name, "exit", label=name)


def _ohlc_field(base: str) -> str:
    mapping = {
        "Current High": "high",
        "Current Low": "low",
        "Body": "body",
        "Range": "range",
    }
    return mapping.get(base.strip(), "close")


def _series_key(label: str) -> str:
    normalized = label.strip().lower()
    mapping = {
        "rsi": "rsi_14",
        "macd": "macd",
        "macd histogram": "macd_hist",
        "signal line": "macd_signal",
        "atr": "atr_14",
        "true range": "true_range",
        "historical volatility": "hist_vol_20",
        "bollinger band width": "bb_width_20",
        "volume": "volume",
        "obv": "obv",
        "mfi": "mfi_14",
        "cci": "cci_20",
        "stochastic": "stoch_k_14",
        "stochastic %k": "stoch_k_14",
        "stochastic %d": "stoch_d_14",
        "rate of change": "roc_12",
        "momentum": "momentum_10",
        "adx": "adx_14",
        "close": "close",
    }
    return mapping.get(normalized, normalized.replace(" ", "_"))


def _dq_check_key(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")
