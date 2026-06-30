# TASS-011 : Rule Taxonomy Specification

**Version:** v1.0.0

**Status:** Standard

**Author:** TASS Project

---

# 1. Purpose

This document defines the official Rule Taxonomy for TASS (Technical Analysis Scoring System).

Every Rule in the system **MUST** belong to exactly one Category.

This taxonomy is the foundation of:

* Rule Registry
* Rule Database
* Rule Engine
* Composite Rule Engine
* Scoring Engine
* Explainability
* Backtesting
* AI Code Generation

**No Rule may exist outside this taxonomy.**

---

# 2. Taxonomy Structure

```text
Rule
│
├── TR   Trend
├── MA   Moving Average
├── PA   Price Action
├── VL   Volume
├── MO   Momentum
├── VO   Volatility
├── MS   Market Structure
├── SR   Support & Resistance
├── BO   Breakout
├── PB   Pullback
├── PT   Pattern
├── CS   Candlestick
├── GP   Gap
├── RK   Risk
├── EN   Entry
├── EX   Exit
├── MR   Market Regime
├── MT   Multi Timeframe
├── CF   Confirmation
├── DQ   Data Quality
└── MTA  Meta Rules
```

---

# 3. Category Code Convention

| Code | Name |
|------|------|
| TR | Trend |
| MA | Moving Average |
| PA | Price Action |
| VL | Volume |
| MO | Momentum |
| VO | Volatility |
| MS | Market Structure |
| SR | Support & Resistance |
| BO | Breakout |
| PB | Pullback |
| PT | Pattern |
| CS | Candlestick |
| GP | Gap |
| RK | Risk |
| EN | Entry |
| EX | Exit |
| MR | Market Regime |
| MT | Multi Timeframe |
| CF | Confirmation |
| DQ | Data Quality |
| MTA | Meta Rules |

---

# 4. Rule ID Format

```text
{CATEGORY}-{NUMBER}           Atomic Rule     e.g. TR-001, MA-001, VL-001
{CATEGORY}-C{NUMBER}          Composite Rule  e.g. TR-C001, CF-C001
{CATEGORY}-E{NUMBER}          Engine Rule     e.g. TR-E001
```

Rules **MUST NOT** use legacy prefixes (`TREND`, `VOLUME`, `TASS-RULE-*`). Use two-letter category codes only.

Legacy IDs (`TREND-001`, etc.) are deprecated aliases. See `rules/registry.yaml` and `engine/core/rule_registry.py`.

---

# 5. Category Definitions

## TR — Trend

**Purpose:** Determine trend direction and trend quality.

**Subcategories:** Direction, Strength, Quality, Slope, Persistence, Exhaustion, Confirmation, State

**Catalog:** 80 frozen atomic rules (TR0001–TR0080). See [TASS-014](TASS-014_TR_Rule_Catalog_v1.0.md).

**Example Rules:** Higher High, Higher Low, ADX Rising, Positive Slope, Trend Established

---

## MA — Moving Average

**Purpose:** Analyze moving averages.

**Subcategories:** Price Position, EMA Position, Alignment, Crossovers, Slope, Distance & Structure

**Catalog:** 60 frozen atomic rules (MA0001–MA0060). See [TASS-015](TASS-015_MA_Rule_Catalog_v1.0.md).

**Example Rules:** Price Above SMA20, EMA Golden Cross, SMA Bullish Alignment, Moving Average Compression

---

## PA — Price Action

**Purpose:** Analyze raw price movement.

**Subcategories:** High, Low, Close, Range, Body, Wick, Swing

**Example Rules:** Strong Close, Inside Bar, Outside Bar, Long Upper Shadow, Wide Range Bar

---

## VL — Volume

**Purpose:** Analyze trading volume.

**Subcategories:** Absolute Volume, Relative Volume, Volume Trend, Volume Spike, OBV, Money Flow

**Example Rules:** Volume Surge, OBV Rising, Relative Volume > 2, Volume Expansion

---

## MO — Momentum

**Purpose:** Analyze market momentum.

**Subcategories:** RSI, MACD, CCI, ROC, MFI, Stochastic, Momentum

**Example Rules:** MACD Positive, MACD Cross, RSI Above 50, RSI Bullish, CCI Positive

---

## VO — Volatility

**Purpose:** Analyze volatility.

**Subcategories:** ATR, True Range, Historical Volatility, Bollinger Band, Keltner Channel, Compression, Expansion

**Example Rules:** ATR Stable, ATR Rising, Bollinger Squeeze, Volatility Expansion

---

## MS — Market Structure

**Purpose:** Analyze market structure.

**Subcategories:** Higher High, Higher Low, Lower High, Lower Low, Swing, Structure Break

**Example Rules:** Bullish Structure, Bearish Structure, Break of Structure

---

## SR — Support & Resistance

**Purpose:** Analyze support and resistance.

**Subcategories:** Horizontal, Trendline, Pivot, Dynamic, Fibonacci

**Example Rules:** Support Bounce, Resistance Break, Pivot Support

---

## BO — Breakout

**Purpose:** Analyze breakout conditions.

**Subcategories:** Price Breakout, Volume Breakout, Trend Breakout, Volatility Breakout

**Example Rules:** 52 Week High Breakout, Resistance Breakout, Volume Confirmed Breakout

---

## PB — Pullback

**Purpose:** Analyze pullback quality.

**Subcategories:** Healthy Pullback, Deep Pullback, MA Pullback, Volume Pullback

**Example Rules:** 20MA Pullback, Healthy Correction

---

## PT — Pattern

**Purpose:** Analyze chart patterns.

**Subcategories:** Triangle, Rectangle, Flag, Pennant, Wedge, Channel, Cup & Handle, Double Top, Double Bottom, Head & Shoulders

---

## CS — Candlestick

**Purpose:** Analyze candlestick patterns.

**Subcategories:** Bullish, Bearish, Continuation, Reversal

**Example Rules:** Hammer, Doji, Bullish Engulfing, Morning Star

---

## GP — Gap

**Purpose:** Analyze price gaps.

**Subcategories:** Gap Up, Gap Down, Breakaway Gap, Runaway Gap, Exhaustion Gap, Common Gap

---

## RK — Risk

**Purpose:** Quantify trading risk.

**Subcategories:** ATR Risk, Gap Risk, Liquidity, Maximum Drawdown, Position Size

---

## EN — Entry

**Purpose:** Evaluate entry timing.

**Subcategories:** Trend Entry, Breakout Entry, Pullback Entry, Reversal Entry

---

## EX — Exit

**Purpose:** Evaluate exit timing.

**Subcategories:** Stop Loss, ATR Exit, Trailing Stop, Profit Target, Time Exit

---

## MR — Market Regime

**Purpose:** Determine current market regime.

**Subcategories:** Bull, Bear, Sideways, High Volatility, Low Volatility

---

## MT — Multi Timeframe

**Purpose:** Compare multiple timeframes.

**Subcategories:** Weekly, Daily, 4H, 1H, Alignment, Conflict

---

## CF — Confirmation

**Purpose:** Validate signals using multiple confirmations.

**Subcategories:** Trend Confirmation, Volume Confirmation, Momentum Confirmation, Breakout Confirmation, Indicator Agreement

---

## DQ — Data Quality

**Purpose:** Validate market data quality.

**Subcategories:** Missing Data, Trading Halt, Corporate Action, Low Liquidity, Data Integrity

---

## MTA — Meta Rules

**Purpose:** Manage Rule metadata.

**Subcategories:** Rule Version, Rule Weight, Rule Priority, Rule Dependency, Rule Status, Rule Conflict, Rule Lifecycle

---

# 6. Development Rules

Every Rule **MUST** satisfy:

1. Belong to exactly one Category.
2. Have a unique Rule ID.
3. Follow the official Rule Specification (`rules/RULE-000_RULE_TEMPLATE.md`).
4. Be independently testable.
5. Return deterministic results.
6. Support unit testing.
7. Support backtesting.
8. Support explainability.
9. Be version controlled.
10. Be reusable by all Engines.

---

# 7. AI Development Instructions

When implementing any Rule:

1. Never create a Rule outside this taxonomy.
2. Always assign a Category Code (two letters).
3. Always assign a unique Rule ID.
4. Implement one Rule per class or module.
5. One Rule must evaluate only one objective fact.
6. Do not mix multiple concepts into a single Rule.
7. Every Rule must expose a standardized interface (`RuleResult`).
8. Every Rule must be stateless.
9. Every Rule must support dependency injection.
10. Every Rule must be usable by Atomic, Composite, Scoring, Backtest, and Explainability engines.

---

# 8. Related Documents

* [rules/RULE_STRUCTURE.md](../rules/RULE_STRUCTURE.md)
* [rules/registry.yaml](../rules/registry.yaml)
* [rules/RULE-000_RULE_TEMPLATE.md](../rules/RULE-000_RULE_TEMPLATE.md)
* [docs/TASS-014_TR_Rule_Catalog_v1.0.md](TASS-014_TR_Rule_Catalog_v1.0.md)

---

# End of Specification

This document is the official Rule Taxonomy Specification for TASS.

All future Rule development, Engine implementation, AI code generation, testing, and maintenance **MUST** comply with this specification.
