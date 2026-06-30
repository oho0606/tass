# TASS-028 : Probability Engine

**Version:** v1.0

**Status:** Frozen

---

# Purpose

Probability Engine는 Master Score를 실제 성공 확률(Winning Probability)로 변환하는 계층이다.

Probability Engine은 점수를 계산하지 않는다.

Probability Engine은 추천을 수행하지 않는다.

Probability Engine은 과거 검증된 백테스트 데이터를 기반으로 Master Score를 실제 확률로 변환한다.

Probability Engine은 Prediction을 수행하지 않는다.

Probability Engine은 Probability를 계산한다.

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

1. 확률은 반드시 Backtest 결과를 기반으로 한다.
2. 확률은 실시간 계산하지 않는다.
3. 확률 모델은 지속적으로 보정(Calibration)된다.
4. Probability는 Prediction이 아니다.
5. Probability는 Explainable 해야 한다.
6. 동일한 Master Score는 동일한 Probability를 반환해야 한다.
7. Probability는 Version 관리된다.
8. Probability는 재현 가능해야 한다.

---

# Input

Master Score: 0 ~ 1000

---

# Output

Winning Probability: 0.00% ~ 100.00%

---

# Probability Mapping

```
Master Score → Historical Success Rate → Calibrated Probability
```

---

# Default Mapping

| Master Score | Winning Probability |
|-------------|---------------------|
| 990 ~ 1000  | 95 ~ 99 %           |
| 950 ~ 989   | 90 ~ 94 %           |
| 900 ~ 949   | 82 ~ 89 %           |
| 850 ~ 899   | 74 ~ 81 %           |
| 800 ~ 849   | 66 ~ 73 %           |
| 750 ~ 799   | 58 ~ 65 %           |
| 700 ~ 749   | 50 ~ 57 %           |
| 650 ~ 699   | 42 ~ 49 %           |
| 600 ~ 649   | 35 ~ 41 %           |
| Below 600   | Below 35 %          |

---

# Calibration

Probability는 다음 검증 결과를 이용하여 자동 보정된다.

- Historical Backtest
- Walk Forward Test
- Paper Trading
- Live Trading
- Monte Carlo Simulation

---

# Calibration Rules

- 새로운 검증 결과가 추가되면 Probability Mapping을 재계산한다.
- 과최적화가 확인되면 기존 Mapping은 폐기된다.
- 모든 변경은 Version으로 관리된다.

---

# Probability Level

| Probability | Level       | Stars   |
|------------|-------------|---------|
| ≥ 95 %     | Exceptional | ★★★★★ |
| ≥ 90 %     | Excellent   | ★★★★★ |
| ≥ 80 %     | Strong      | ★★★★☆ |
| ≥ 70 %     | Good        | ★★★★☆ |
| ≥ 60 %     | Average     | ★★★☆☆ |
| ≥ 50 %     | Weak        | ★★☆☆☆ |
| < 50 %     | Reject      | ★☆☆☆☆ |

---

# Explainability

Probability Engine는 다음 정보를 제공해야 한다.

- Master Score
- Probability
- Historical Win Rate
- Sample Size
- Calibration Version
- Confidence Interval
- Last Calibration Date

---

# Validation

Probability Engine는 다음 검증을 통과해야 한다.

- Historical Backtest
- Walk Forward Test
- Monte Carlo
- Paper Trading
- Live Trading
- Probability Calibration Test

---

# Implementation

| Component | Path |
|-----------|------|
| Engine entry | `engine/probability/probability_engine.py` |
| Mapping tables | `engine/probability/mapping.py` |
| Calibration loader | `engine/probability/calibration.py` |
| Calibration config | `config/probability_v1.yaml` |
| Result type | `engine/core/types.py` → `ProbabilityResult` |

---

# Summary

| | |
|---|---|
| Input | Master Score |
| Output | Winning Probability |
| Range | 0 % ~ 100 % |
| Calculation | Historical Calibration |
| Status | Frozen v1.0 |

Probability Engine는 Master Score를 실제 성공 확률로 변환하는 유일한 계층이다.

Probability는 예측(Prediction)이 아니라 통계적으로 검증된 성공 가능성(Probability)을 의미한다.
