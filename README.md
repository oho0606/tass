# TASS

TASS (Technical Analysis Scoring Specification)는 AI 기반 기술적 분석 종목 발굴 플랫폼입니다.

TASS는 사용자가 차트를 직접 분석하도록 돕는 도구가 아닙니다. 사용자가 웹사이트에 접속하면 `Today's Picks` 화면에서 오늘 가장 유리한 TOP 20 추천 종목을 확인하고, 종목별 추천 이유를 검토한 뒤 매수 여부를 결정하도록 돕는 플랫폼입니다.

## Project Structure

| Folder | Purpose |
|--------|---------|
| `engine/` | Python 구현 루트 (TASS-030 `src/`에 해당) |
| `api/` | REST API Layer (planned) |
| `config/` | YAML 설정 + Pydantic Settings (`.env`) |
| `tests/` | Unit, Integration, Regression tests |
| `scripts/` | CLI 도구 |
| `docs/` | 설계 문서 (TASS-001–030) |
| `agents/` | AI role definitions |
| `skills/` | Standard AI procedures |
| `specs/` | Machine-readable Rule specs |
| `rule_database/` | Rule 메타데이터 DB |
| `logs/` | 런타임 로그 |
| `database/` | DB 스키마 (planned) |
| `engine/application/` | Application Service (Recommendation, Backtest) |
| `main.py` | 애플리케이션 진입점 |

Application Layer: [docs/TASS-032_Application_Layer_v1.0.md](docs/TASS-032_Application_Layer_v1.0.md)

Python 구현 표준: [docs/TASS-030_Python_Implementation_Specification_v1.0.md](docs/TASS-030_Python_Implementation_Specification_v1.0.md)

## AI Collaboration Workflow

```text
read_project_spec → Agent role → Skill procedures → update_changelog
```

All AI tools (Cursor, Claude Code, Codex, ChatGPT) use the same `agents/` and `skills/` standards.

See [agents/README.md](agents/README.md) and [skills/README.md](skills/README.md).

## Design Documents

TASS의 설계 및 명세 문서는 `docs/` 폴더에 있습니다.

## Vision

사용자는 주식을 검색하러 오는 것이 아닙니다.

사용자는 오늘 살 만한 종목을 확인하러 옵니다.

따라서 TASS의 모든 개발 방향은 `Today's Picks`를 중심으로 결정합니다.

## Usage Mode

현재 TASS는 **단일 사용자 온디맨드 조회형** 운영을 기본으로 합니다.

- 알림(푸시/메일) 중심 워크플로우를 필수로 두지 않습니다.
- 포트폴리오/계정 기능 없이, 필요할 때 접속해 결과를 확인하는 흐름을 우선합니다.
- 우선순위는 추천 품질, 설명 가능성, 조회 편의성입니다.

## Core Philosophy

- Prediction: No
- Probability: Yes
- Opinion: No
- Data: Yes
- Emotion: No
- Rule: Yes

TASS는 미래를 예측하지 않습니다. TASS는 순수 기술적 분석 데이터와 검증 가능한 Rule을 통해 확률적으로 유리한 종목만 선별합니다.

## Allowed Data

- OHLCV
- Volume
- Moving averages
- ATR
- RSI
- MACD
- OBV
- Bollinger Bands
- Fibonacci
- Dow Theory
- Granville Rules
- Wyckoff Method
- Turtle Trading
- ADX
- DMI
- VWAP
- Relative Strength
- Other technical analysis data

## Forbidden Data

- News
- Disclosures
- Earnings
- Politics
- SNS
- YouTube
- Communities
- Analyst opinions
- Themes
- Rumors

## High-Level Flow

```text
User
↓
Frontend
↓
Backend API
↓
TASS Engine
↓
Scoring Engine
↓
Database
↓
Report Engine
↓
Recommended Stocks
```

## Recommendation Flow

```text
2700 stocks
↓
Primary filters
↓
Liquidity
↓
Volume
↓
Market environment
↓
Base trend
↓
100-300 candidates
↓
Detailed analysis
↓
Dow / Granville / Wyckoff / OBV / MACD / RSI / Bollinger / ATR / Relative Strength
↓
Final score
↓
Confidence
↓
TOP 20 Today's Picks
```

## Scoring System

The total score is 1000 points.

Scoring areas:

- Market environment
- Trend
- Moving average
- Volume
- Momentum
- Volatility
- Risk management

Every Rule must be implementable, measurable, and backtestable.

## Gate System

Gate has priority over total score.

Examples:

- Weak market: Gate Fail
- Insufficient volume: Gate Fail
- Insufficient liquidity: Gate Fail
- Long-term downtrend: Gate Fail

## Confidence

Confidence is calculated separately from the total score.

Confidence considers:

- Trend alignment
- Volume alignment
- Momentum alignment
- Volatility suitability
- Multi-timeframe alignment

## Development Principles

1. Design first.
2. Code is only the implementation of design.
3. Every Rule has a Rule ID.
4. Every Rule must be backtestable.
5. Every Rule must be implementable in Python.
6. Every Rule must be explainable.
7. Every Rule has a change history.
8. Every change must be validated with data.
9. Statistics come before intuition.
10. Structure comes before additional features.

## Current Phase

TASS is in **v1.0.0 GA (Phase 6 complete)** phase.

Current priorities:

- v1.1 real-time market data integration (KIS Open API)
- Broker adapter expansion (Kiwoom optional)
- On-demand viewer UX improvements
- Full Engine rollout readiness (v1.3)

## Running Daily Picks (MVP)

```bash
pip install -e ".[dev]"
cp .env.example .env

# 방법 1: main.py 진입점
python main.py picks --universe config/universe_sample.csv

# 방법 2: tass CLI (설치 후)
tass picks --universe config/universe_sample.csv

# 방법 3: 스크립트 직접 실행
python scripts/run_daily_picks.py --universe config/universe_sample.csv
```

Output: `output/picks_YYYY-MM-DD.json`

## Code Quality

```bash
pip install -e ".[dev]"
pre-commit install
pre-commit run --all-files
pytest tests/ -q
```

## Running Backtest

```bash
python main.py backtest
python scripts/run_backtest.py --rules TR0001 TR0002
```

Reports: `backtest/reports/`
