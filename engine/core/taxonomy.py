from __future__ import annotations

import re
from enum import Enum


class CategoryCode(str, Enum):
    """Official TASS Rule Taxonomy category codes (TASS-011)."""

    TR = "TR"
    MA = "MA"
    PA = "PA"
    VL = "VL"
    MO = "MO"
    VO = "VO"
    MS = "MS"
    SR = "SR"
    BO = "BO"
    PB = "PB"
    PT = "PT"
    CS = "CS"
    GP = "GP"
    RK = "RK"
    EN = "EN"
    EX = "EX"
    MR = "MR"
    MT = "MT"
    CF = "CF"
    DQ = "DQ"
    MTA = "MTA"


CATEGORY_NAMES: dict[CategoryCode, str] = {
    CategoryCode.TR: "Trend",
    CategoryCode.MA: "Moving Average",
    CategoryCode.PA: "Price Action",
    CategoryCode.VL: "Volume",
    CategoryCode.MO: "Momentum",
    CategoryCode.VO: "Volatility",
    CategoryCode.MS: "Market Structure",
    CategoryCode.SR: "Support & Resistance",
    CategoryCode.BO: "Breakout",
    CategoryCode.PB: "Pullback",
    CategoryCode.PT: "Pattern",
    CategoryCode.CS: "Candlestick",
    CategoryCode.GP: "Gap",
    CategoryCode.RK: "Risk",
    CategoryCode.EN: "Entry",
    CategoryCode.EX: "Exit",
    CategoryCode.MR: "Market Regime",
    CategoryCode.MT: "Multi Timeframe",
    CategoryCode.CF: "Confirmation",
    CategoryCode.DQ: "Data Quality",
    CategoryCode.MTA: "Meta Rules",
}


class RuleType(str, Enum):
    ATOMIC = "atomic"
    COMPOSITE = "composite"
    ENGINE = "engine"


_HYPHEN_ATOMIC = re.compile(r"^([A-Z]{2})-(\d+)$")
_HYPHEN_COMPOSITE = re.compile(r"^([A-Z]{2})-C(\d+)$", re.IGNORECASE)
_HYPHEN_ENGINE = re.compile(r"^([A-Z]{2})-E(\d+)$", re.IGNORECASE)

_CANONICAL_ATOMIC = re.compile(r"^([A-Z]{2})(\d{4})$")
_CANONICAL_COMPOSITE = re.compile(r"^([A-Z]{2})C(\d{3})$", re.IGNORECASE)
_CANONICAL_ENGINE = re.compile(r"^([A-Z]{2})E(\d{3})$", re.IGNORECASE)
_COMPOSITE_LIBRARY = re.compile(
    r"^C(TR|MA|PA|VL|MO|VO|MS|SR|BO|PB|PT|CS|GP|RK|EN|EX|MR|MT|CF|DQ)(\d{3})$",
    re.IGNORECASE,
)

COMPOSITE_LIBRARY_CODES: tuple[str, ...] = (
    "CTR",
    "CMA",
    "CPA",
    "CVL",
    "CMO",
    "CVO",
    "CMS",
    "CSR",
    "CBO",
    "CPB",
    "CPT",
    "CCS",
    "CGP",
    "CRK",
    "CEN",
    "CEX",
    "CMR",
    "CMT",
    "CCF",
    "CDQ",
)

COMPOSITE_TO_ATOMIC: dict[str, CategoryCode] = {
    "CTR": CategoryCode.TR,
    "CMA": CategoryCode.MA,
    "CPA": CategoryCode.PA,
    "CVL": CategoryCode.VL,
    "CMO": CategoryCode.MO,
    "CVO": CategoryCode.VO,
    "CMS": CategoryCode.MS,
    "CSR": CategoryCode.SR,
    "CBO": CategoryCode.BO,
    "CPB": CategoryCode.PB,
    "CPT": CategoryCode.PT,
    "CCS": CategoryCode.CS,
    "CGP": CategoryCode.GP,
    "CRK": CategoryCode.RK,
    "CEN": CategoryCode.EN,
    "CEX": CategoryCode.EX,
    "CMR": CategoryCode.MR,
    "CMT": CategoryCode.MT,
    "CCF": CategoryCode.CF,
    "CDQ": CategoryCode.DQ,
}

LEGACY_ALIASES: dict[str, str] = {
    "TREND-001": "TR0001",
    "TREND-002": "TR0002",
    "TREND-003": "TR0003",
    "TREND-004": "TR0004",
    "TREND-C001": "TRC001",
    "TREND-C002": "TRC002",
    "TREND-C003": "TRC003",
    "TREND-C004": "TRC004",
    "TREND-E001": "TRE001",
    "TR-001": "TR0001",
    "TR-002": "TR0002",
    "TR-003": "TR0003",
    "TR-004": "TR0004",
    "TR-C001": "TRC001",
    "TR-C002": "TRC002",
    "TR-C003": "TRC003",
    "TR-C004": "TRC004",
    "TR-E001": "TRE001",
}


def resolve_hyphen_alias(rule_id: str) -> str:
    return LEGACY_ALIASES.get(rule_id, rule_id)


def is_composite_library_id(rule_id: str) -> bool:
    return bool(_COMPOSITE_LIBRARY.match(to_canonical_id(rule_id)))


def composite_library_code(rule_id: str) -> str | None:
    cid = to_canonical_id(rule_id)
    m = _COMPOSITE_LIBRARY.match(cid)
    return f"C{m.group(1).upper()}" if m else None


def to_canonical_id(rule_id: str) -> str:
    """Canonical ID per TASS-012: TR0001, TRC001, TRE001; TASS-027: CTR001."""
    rid = resolve_hyphen_alias(rule_id)
    if (
        _CANONICAL_ATOMIC.match(rid)
        or _CANONICAL_COMPOSITE.match(rid)
        or _CANONICAL_ENGINE.match(rid)
        or _COMPOSITE_LIBRARY.match(rid)
    ):
        return rid.upper() if _COMPOSITE_LIBRARY.match(rid) else rid
    m = _HYPHEN_ENGINE.match(rid)
    if m:
        return f"{m.group(1)}E{int(m.group(2)):03d}"
    m = _HYPHEN_COMPOSITE.match(rid)
    if m:
        return f"{m.group(1)}C{int(m.group(2)):03d}"
    m = _HYPHEN_ATOMIC.match(rid)
    if m:
        return f"{m.group(1)}{int(m.group(2)):04d}"
    return rid


def normalize_rule_id(rule_id: str) -> str:
    return to_canonical_id(rule_id)


def parse_category_from_rule_id(rule_id: str) -> CategoryCode:
    cid = to_canonical_id(rule_id)
    comp_code = composite_library_code(cid)
    if comp_code:
        return COMPOSITE_TO_ATOMIC[comp_code]
    return CategoryCode(cid[:2])


def parse_rule_type(rule_id: str) -> RuleType:
    cid = to_canonical_id(rule_id)
    if _CANONICAL_ENGINE.match(cid):
        return RuleType.ENGINE
    if _CANONICAL_COMPOSITE.match(cid) or _COMPOSITE_LIBRARY.match(cid):
        return RuleType.COMPOSITE
    return RuleType.ATOMIC


def validate_rule_id(rule_id: str) -> bool:
    try:
        cid = to_canonical_id(rule_id)
        parse_category_from_rule_id(cid)
        return bool(
            _CANONICAL_ATOMIC.match(cid)
            or _CANONICAL_COMPOSITE.match(cid)
            or _CANONICAL_ENGINE.match(cid)
            or _COMPOSITE_LIBRARY.match(cid)
        )
    except ValueError:
        return False
