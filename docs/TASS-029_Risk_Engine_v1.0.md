# TASS-029 : Risk Engine

**Version:** v1.0

**Status:** Frozen

---

# Purpose

Risk Engine는 투자 대상 종목의 위험도를 정량적으로 평가하는 계층이다.

Risk Engine은 수익 가능성을 평가하지 않는다.

Risk Engine은 손실 가능성과 투자 위험만 평가한다.

Risk Engine은 Master Score, Probability, Confidence와 독립적으로 계산된다.

Risk Engine의 결과는 Recommendation Engine에서 최종 추천 여부를 결정하는 핵심 요소로 사용된다.

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

1. Risk는 항상 독립적으로 계산한다.
2. 높은 점수라고 낮은 Risk를 의미하지 않는다.
3. Risk는 손실 가능성을 의미한다.
4. Risk는 객관적이어야 한다.
5. Risk는 Explainable 해야 한다.
6. Risk는 재현 가능해야 한다.
7. Risk는 Version 관리된다.
8. Risk는 Recommendation 이전에 반드시 계산된다.

---

# Input

- OHLCV
- Domain Engine Results
- Master Score
- Probability
- Confidence
- Composite Rule Results
- Market Regime
- Data Quality

---

# Risk Components

| Component | Weight |
|-----------|--------|
| Volatility Risk | 20 |
| Gap Risk | 15 |
| Liquidity Risk | 10 |
| Trend Risk | 10 |
| Momentum Risk | 5 |
| Market Risk | 10 |
| Entry Timing Risk | 5 |
| Stop Loss Distance | 5 |
| ATR Risk | 5 |
| Maximum Drawdown Risk | 5 |
| Price Extension Risk | 3 |
| False Breakout Risk | 3 |
| Data Quality Risk | 2 |
| Signal Conflict Risk | 2 |
| **Maximum** | **100** |

---

# Risk Score

Range: 0 ~ 100 (0 = Lowest Risk, 100 = Highest Risk)

---

# Risk Grade

| Score | Grade | Stars |
|-------|-------|-------|
| 0 ~ 10 | Very Low Risk | ★★★★★ |
| 11 ~ 20 | Low Risk | ★★★★★ |
| 21 ~ 30 | Moderate Risk | ★★★★☆ |
| 31 ~ 40 | Elevated Risk | ★★★☆☆ |
| 41 ~ 50 | High Risk | ★★☆☆☆ |
| 51 ~ 70 | Very High Risk | ★☆☆☆☆ |
| 71 ~ 100 | Extreme Risk | Reject |

---

# Risk Level

| Score | Level |
|-------|-------|
| 0 ~ 10 | Excellent |
| 11 ~ 20 | Good |
| 21 ~ 30 | Acceptable |
| 31 ~ 40 | Caution |
| 41 ~ 50 | Danger |
| Above 50 | Reject |

---

# Risk Decision

| Score | Decision |
|-------|----------|
| ≤ 20 | PASS |
| 21 ~ 30 | PASS WITH CAUTION |
| 31 ~ 40 | REVIEW REQUIRED |
| > 40 | FAIL |

---

# Explainability

Risk Engine는 다음 정보를 제공한다.

- Overall Risk Score
- Component breakdown (14 components)
- Risk Grade / Risk Level / Decision
- Per-component reasons

---

# Implementation

| Item | Path |
|------|------|
| Entry point | `engine/risk/risk_engine.py` → `compute_risk()` |
| Config | `config/risk_v1.yaml` |
| Spec JSON | `specs/json/RISK-001.json` |
| Result type | `RiskResult` in `engine/core/types.py` |

---

# Design Rules

- Risk는 Master Score를 변경하지 않는다.
- Risk는 Probability를 변경하지 않는다.
- Risk는 Confidence를 변경하지 않는다.
- Risk > 40 (FAIL)이면 Recommendation 대상에서 제외된다.

---

# Output

- Risk Score
- Risk Grade
- Risk Level
- Risk Decision
- Risk Breakdown
- Component Report

---

# Validation

Unit Test, Integration Test, Regression Test, Historical Validation, Walk Forward Test, Monte Carlo Simulation, Paper Trading, Live Trading Validation

---

# Summary

Risk Engine는 투자 대상의 손실 가능성을 객관적으로 정량화하는 유일한 계층이다.

높은 Master Score라도 Risk가 기준치를 초과하면 추천 대상에서 제외된다.
