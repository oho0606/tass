# TASS-029 : Confidence Engine

**Version:** v1.0

**Status:** Frozen

---

# Purpose

Confidence Engine는 추천 신호의 신뢰도(Confidence)를 계산하는 계층이다.

Confidence는 수익 확률(Probability)과 다르다.

- **Probability** — "성공 가능성"
- **Confidence** — "현재 분석 결과를 얼마나 신뢰할 수 있는가"

Confidence Engine은 추천을 수행하지 않는다. Master Score와 Probability를 보조 평가한다.

---

# Architecture

```
OHLCV
  ↓
Indicator Layer
  ↓
Atomic Rule Library
  ↓
Composite Rule Library
  ↓
Domain Engine
  ↓
Scoring Engine
  ↓
Master Score
  ↓
Probability Engine
  ↓
Confidence Engine
  ↓
Risk Engine
  ↓
Recommendation Engine
```

---

# Principles

1. Confidence는 신뢰도를 의미한다.
2. Probability와 독립적으로 계산한다.
3. Rule의 일관성을 평가한다.
4. Engine 간 일관성을 평가한다.
5. Multi Timeframe 일치성을 평가한다.
6. Data Quality를 반영한다.
7. Explainable 해야 한다.
8. 재현 가능해야 한다.

---

# Input

- Master Score
- Probability
- Domain Engine Results
- Composite Rule Results
- Atomic Rule Results
- Market Regime
- Multi Timeframe Result
- Data Quality Result

---

# Confidence Components

| Component | Weight |
|-----------|--------|
| Rule Consistency | 20 |
| Engine Consistency | 20 |
| Indicator Agreement | 10 |
| Composite Agreement | 10 |
| Trend Agreement | 10 |
| Volume Agreement | 5 |
| Momentum Agreement | 5 |
| Volatility Agreement | 5 |
| Multi Timeframe | 5 |
| Market Regime | 5 |
| Data Quality | 3 |
| Signal Stability | 1 |
| Historical Consistency | 1 |
| **Maximum** | **100** |

---

# Confidence Range

0 ~ 100

---

# Confidence Grade

| Range | Grade | Stars |
|-------|-------|-------|
| 95 ~ 100 | Exceptional | ★★★★★ |
| 90 ~ 94 | Excellent | ★★★★★ |
| 80 ~ 89 | Strong | ★★★★☆ |
| 70 ~ 79 | Good | ★★★★☆ |
| 60 ~ 69 | Average | ★★★☆☆ |
| 50 ~ 59 | Weak | ★★☆☆☆ |
| Below 50 | Low | ★☆☆☆☆ |

---

# Confidence Level

| Threshold | Level |
|-----------|-------|
| 95+ | Very High Confidence |
| 90+ | High Confidence |
| 80+ | Reliable |
| 70+ | Acceptable |
| 60+ | Caution |
| Below 60 | Do Not Trust |

---

# Explainability

Confidence Engine는 다음 정보를 제공한다.

- Overall Confidence
- Rule Consistency
- Engine Consistency
- Agreement Score
- Data Quality
- Timeframe Agreement
- Historical Stability
- Confidence Grade
- Confidence Level

---

# Design Rules

- Confidence는 Probability를 변경하지 않는다.
- Confidence는 Master Score를 변경하지 않는다.
- Confidence는 Risk를 변경하지 않는다.
- Confidence는 Recommendation Engine의 판단 근거로만 사용된다.

---

# Output

- Confidence Score
- Confidence Grade
- Confidence Level
- Confidence Breakdown
- Agreement Report
- Consistency Report

---

# Implementation

- Module: `engine/confidence/`
- Config: `config/confidence_v1.yaml`
- Entry point: `compute_confidence(ConfidenceEngineInput)`
- Types: `ConfidenceResult` in `engine/core/types.py`

---

# Engine Independence

Confidence Engine은 독립적으로 테스트·유지보수·버전 관리·개선이 가능해야 한다.

---

# Summary

| | |
|---|---|
| **Input** | Master Score, Probability, Domain/Rule Results |
| **Output** | Confidence Score (0–100) |
| **Purpose** | Signal Reliability |
| **Status** | Frozen v1.0 |

Confidence Engine는 현재 분석 결과의 신뢰도를 정량화하는 유일한 계층이다. Confidence는 Probability와 독립적인 평가 지표이며 추천 품질을 보장하기 위한 핵심 요소이다.
