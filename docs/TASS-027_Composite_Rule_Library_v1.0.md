# TASS Composite Rule Library

# Version : 1.0

**Status:** Frozen v1.0

**Machine-readable:** [rules/catalog/Composite_v1.0.yaml](../rules/catalog/Composite_v1.0.yaml)

---

## Purpose

Composite Rule은 Atomic Rule의 결과를 조합하여 하나의 의미 있는 시장 상태(State)를 판단하는 규칙이다.

Composite Rule은 투자 의사결정을 직접 수행하지 않으며, Domain Engine의 입력(Input)으로만 사용된다.

Composite Rule은 Atomic Rule만 참조할 수 있으며 다른 Composite Rule을 참조해서는 안 된다.

---

## Composite Rule Architecture

```text
OHLCV
    ↓
Indicator
    ↓
Atomic Rule
    ↓
Composite Rule
    ↓
Domain Engine
    ↓
Master Score
    ↓
Recommendation
```

---

## Composite Rule Principles

1. Composite Rule은 Atomic Rule만 입력으로 사용한다.
2. Composite Rule은 하나의 의미(State)만 판단한다.
3. Composite Rule은 점수를 계산하지 않는다.
4. Composite Rule은 추천을 하지 않는다.
5. Composite Rule은 Domain Engine에서 재사용된다.
6. Composite Rule은 독립적으로 테스트 가능해야 한다.
7. Composite Rule은 항상 동일한 입력에 동일한 결과를 반환해야 한다.
8. Composite Rule은 설명 가능(Explainable)해야 한다.

---

## Return Type

| Verdict | Description |
|---------|-------------|
| PASS | State condition fully satisfied |
| PARTIAL | State condition partially satisfied |
| FAIL | State condition not satisfied |
| UNKNOWN | Insufficient or invalid input |

---

## Composite Category

| Code | Name |
|------|------|
| CTR | Trend Composite |
| CMA | Moving Average Composite |
| CPA | Price Action Composite |
| CVL | Volume Composite |
| CMO | Momentum Composite |
| CVO | Volatility Composite |
| CMS | Market Structure Composite |
| CSR | Support & Resistance Composite |
| CBO | Breakout Composite |
| CPB | Pullback Composite |
| CPT | Pattern Composite |
| CCS | Candlestick Composite |
| CGP | Gap Composite |
| CRK | Risk Composite |
| CEN | Entry Composite |
| CEX | Exit Composite |
| CMR | Market Regime Composite |
| CMT | Multi Timeframe Composite |
| CCF | Confirmation Composite |
| CDQ | Data Quality Composite |

---

## Composite Rule ID Convention

```text
CTR001 ~ CTR999
CMA001 ~ CMA999
CPA001 ~ CPA999
CVL001 ~ CVL999
CMO001 ~ CMO999
CVO001 ~ CVO999
CMS001 ~ CMS999
CSR001 ~ CSR999
CBO001 ~ CBO999
CPB001 ~ CPB999
CPT001 ~ CPT999
CCS001 ~ CCS999
CGP001 ~ CGP999
CRK001 ~ CRK999
CEN001 ~ CEN999
CEX001 ~ CEX999
CMR001 ~ CMR999
CMT001 ~ CMT999
CCF001 ~ CCF999
CDQ001 ~ CDQ999
```

Composite Rule ID는 `C` + Atomic Category Code + 3-digit number 형식을 사용한다.

Legacy Domain Engine composite IDs (`TRC001`, `MAC001` 등)는 별도 네임스페이스이며, 본 라이브러리 ID와 1:1 대응하지 않을 수 있다.

---

## Composite Rule Catalog

### Trend Composite (CTR001–CTR010)

```text
CTR001  Trend Direction
CTR002  Trend Strength
CTR003  Trend Quality
CTR004  Trend Stability
CTR005  Trend Continuation
CTR006  Trend Exhaustion
CTR007  Trend Reversal
CTR008  Trend Acceleration
CTR009  Trend Consistency
CTR010  Trend Confirmation
```

---

### Moving Average Composite (CMA001–CMA010)

```text
CMA001  MA Position Quality
CMA002  MA Alignment Quality
CMA003  Golden Cross Strength
CMA004  Death Cross Strength
CMA005  MA Trend Quality
CMA006  MA Compression State
CMA007  MA Expansion State
CMA008  Dynamic Support Quality
CMA009  Dynamic Resistance Quality
CMA010  MA Structure Quality
```

---

### Price Action Composite (CPA001–CPA010)

```text
CPA001  Price Strength
CPA002  Price Weakness
CPA003  Bullish Price Structure
CPA004  Bearish Price Structure
CPA005  Breakout Candle Quality
CPA006  Pullback Candle Quality
CPA007  Swing Quality
CPA008  Range Quality
CPA009  Price Stability
CPA010  Price Confirmation
```

---

### Volume Composite (CVL001–CVL010)

```text
CVL001  Volume Confirmation
CVL002  Volume Expansion
CVL003  Volume Contraction
CVL004  Accumulation
CVL005  Distribution
CVL006  Buying Pressure
CVL007  Selling Pressure
CVL008  Volume Quality
CVL009  Volume Stability
CVL010  Smart Money Activity
```

---

### Momentum Composite (CMO001–CMO010)

```text
CMO001  Momentum Strength
CMO002  Momentum Agreement
CMO003  Momentum Continuation
CMO004  Momentum Reversal
CMO005  Momentum Divergence
CMO006  Bullish Momentum
CMO007  Bearish Momentum
CMO008  Momentum Quality
CMO009  Momentum Stability
CMO010  Momentum Confirmation
```

---

### Volatility Composite (CVO001–CVO010)

```text
CVO001  Volatility Compression
CVO002  Volatility Expansion
CVO003  Stable Volatility
CVO004  High Volatility
CVO005  Low Volatility
CVO006  Breakout Volatility
CVO007  Risk Volatility
CVO008  ATR Stability
CVO009  Volatility Quality
CVO010  Volatility Confirmation
```

---

### Market Structure Composite (CMS001–CMS010)

```text
CMS001  Bull Structure
CMS002  Bear Structure
CMS003  Structure Break
CMS004  Higher High Sequence
CMS005  Lower Low Sequence
CMS006  Swing Structure
CMS007  Trend Structure
CMS008  Structure Quality
CMS009  Structure Stability
CMS010  Structure Confirmation
```

---

### Support & Resistance Composite (CSR001–CSR005)

```text
CSR001  Support Quality
CSR002  Resistance Quality
CSR003  Support Break
CSR004  Resistance Break
CSR005  Dynamic Support Quality
```

---

### Breakout Composite (CBO001–CBO005)

```text
CBO001  Breakout Quality
CBO002  Breakout Confirmation
CBO003  False Breakout
CBO004  Strong Breakout
CBO005  Breakout Continuation
```

---

### Pullback Composite (CPB001–CPB005)

```text
CPB001  Healthy Pullback
CPB002  Deep Pullback
CPB003  Pullback Recovery
CPB004  Pullback Quality
CPB005  Pullback Confirmation
```

---

### Pattern Composite (CPT001–CPT005)

```text
CPT001  Continuation Pattern
CPT002  Reversal Pattern
CPT003  Bullish Pattern
CPT004  Bearish Pattern
CPT005  Pattern Quality
```

---

### Candlestick Composite (CCS001–CCS005)

```text
CCS001  Bullish Candle Group
CCS002  Bearish Candle Group
CCS003  Reversal Candle Group
CCS004  Continuation Candle Group
CCS005  Candle Quality
```

---

### Gap Composite (CGP001–CGP003)

```text
CGP001  Bullish Gap
CGP002  Bearish Gap
CGP003  Gap Quality
```

---

### Risk Composite (CRK001–CRK005)

```text
CRK001  Overall Risk
CRK002  Volatility Risk
CRK003  Gap Risk
CRK004  Liquidity Risk
CRK005  Position Risk
```

---

### Entry Composite (CEN001–CEN005)

```text
CEN001  Entry Quality
CEN002  Breakout Entry
CEN003  Pullback Entry
CEN004  Trend Entry
CEN005  Entry Confirmation
```

---

### Exit Composite (CEX001–CEX005)

```text
CEX001  Exit Quality
CEX002  Stop Loss Exit
CEX003  Target Exit
CEX004  Trailing Exit
CEX005  Exit Confirmation
```

---

### Market Regime Composite (CMR001–CMR005)

```text
CMR001  Bull Market
CMR002  Bear Market
CMR003  Sideways Market
CMR004  High Volatility Market
CMR005  Low Volatility Market
```

---

### Multi Timeframe Composite (CMT001–CMT005)

```text
CMT001  Full Alignment
CMT002  Partial Alignment
CMT003  Timeframe Conflict
CMT004  Higher Timeframe Agreement
CMT005  Lower Timeframe Agreement
```

---

### Confirmation Composite (CCF001–CCF005)

```text
CCF001  Trend Confirmation
CCF002  Volume Confirmation
CCF003  Momentum Confirmation
CCF004  Breakout Confirmation
CCF005  Full Confirmation
```

---

### Data Quality Composite (CDQ001–CDQ002)

```text
CDQ001  Data Integrity
CDQ002  Data Reliability
```

---

## Summary

| Field | Value |
|-------|-------|
| Composite Categories | 20 |
| Composite Rules | 130 |
| Rule Type | State Evaluation |
| Input | Atomic Rules |
| Output | PASS · PARTIAL · FAIL · UNKNOWN |
| Status | Frozen v1.0 |

Composite Rule Library는 Domain Engine의 유일한 입력으로 사용된다.

---

## Related Documents

* [TASS-011 Rule Taxonomy](TASS-011_Rule_Taxonomy_Specification.md)
* [TASS-012 Rule Specification Standard](TASS-012_Rule_Specification_Standard.md)
* [TASS-013 Rule Database](TASS-013_Rule_Database_Specification.md)
* [rules/catalog/Composite_v1.0.yaml](../rules/catalog/Composite_v1.0.yaml)
* [rules/registry.yaml](../rules/registry.yaml)

---

# End of Library

This document is the official frozen Composite Rule Library v1.0.

All new Composite Rules **MUST** use an ID from this library. No new Composite IDs may be invented outside this catalog until library v2.0.
