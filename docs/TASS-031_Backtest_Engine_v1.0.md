# TASS-031 : Backtest Engine

**Version:** v1.0

**Status:** Frozen

---

# Purpose

Backtest Engine은 TASS의 모든 Rule이 운영에 포함되기 전 반드시 거치는 검증 계층이다.

Backtest Engine은 수익률 극대화가 목적이 아니다.

목적은 Rule, Score, Weight, Gate, Confidence, Risk의 **데이터 기반 검증**이다.

---

# Architecture

```
OHLCV
  ↓
Rule Evaluator (walk-forward)
  ↓
Signal Generator
  ↓
Trade Simulator (fees, slippage)
  ↓
Metrics Calculator
  ↓
Verdict (ADOPT / REJECT / REVISE)
  ↓
Report (JSON + Markdown)
```

---

# Principles

1. Backtest는 Rule을 수정하지 않는다.
2. 동일 입력 → 동일 출력 (재현성).
3. 수수료·슬리피지를 반드시 반영한다.
4. In-sample / Out-of-sample 분리로 과최적화를 검사한다.
5. 결과는 `backtest/reports/`에 기록한다.
6. API Layer는 Backtest Engine을 직접 호출하지 않는다 (Application Service 경유 예정).

---

# Module Structure

| Module | Class / Function | Responsibility |
|--------|------------------|----------------|
| `backtest_engine.py` | `BacktestEngine` | Orchestration |
| `rule_backtest.py` | `backtest_rule()` | Walk-forward Rule test |
| `simulator.py` | `simulate_trades()` | Trade simulation |
| `metrics.py` | `calculate_metrics()` | TASS-009 §8 metrics |
| `report.py` | `save_json_report()` | Report output |
| `registry.py` | `RULE_EVALUATORS` | Rule evaluator map |
| `config.py` | `load_backtest_config()` | YAML config |

---

# Configuration

`config/backtest_v1.yaml`

| Section | Key | Default |
|---------|-----|---------|
| trading | commission_rate | 0.015% |
| trading | slippage_rate | 0.1% |
| trading | hold_days | 20 |
| trading | stop_loss_pct | 5% |
| trading | take_profit_pct | 15% |
| evaluation | min_trades | 5 |
| evaluation | in_sample_ratio | 0.7 |
| evaluation | min_win_rate | 40% |

---

# Verdict

| Verdict | Condition |
|---------|-----------|
| ADOPT | TASS-009 기준 충족 |
| REVISE | 부분 개선, Rule 재검토 필요 |
| REJECT | 승률·MDD·OOS 기준 미달 |
| INSUFFICIENT_DATA | 거래/데이터 부족 |

---

# CLI

```bash
python main.py backtest
python scripts/run_backtest.py --rules TR0001 TR0002
```

---

# Regression

Rule 변경 시 `tests/regression/test_tr_rules_regression.py`가 자동 실행된다.

Baseline: `tests/regression/baselines/tr0001_synthetic.json`

---

# Implementation Status

| # | Layer | Status |
|---|-------|--------|
| 10 | Backtest | ✅ v1.0 |
| 11 | REST API | ⬜ Last (user decision) |
| 12 | Frontend | ⬜ Planned |

---

# References

- TASS-009 Backtest Framework
- TASS-030 Python Implementation Specification
